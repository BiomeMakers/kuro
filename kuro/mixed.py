"""A decipherment framework for mixed scripts: syllabary, logograms, ligatures, fractions.

Luo, Hartmann, Santus, Barzilay and Cao (2021) decipher unsegmented alphabetic scripts by
placing each character in a phonetic geometry (IPA features) and aligning spans of the lost
text to a known vocabulary. Their note 3 leaves other script types outside the work.

Linear A and Linear B are not alphabets. They are CV syllabaries carrying commodity
logograms, ligatures that bind a syllabogram to a logogram, and fractions. This module is
the extension, built so that it can be validated on Linear B — where the answer is known —
before anything is said about Linear A.

The four kinds of sign and what the framework does with each:
  syllabogram   a CV sign; its value is a (consonant, vowel) pair, each with IPA features,
                so the phonetic geometry of the alphabetic model extends directly
  logogram      no phonetic value; an unmatched span, exactly as the 2021 model treats
                characters it cannot align
  ligature      LOGO+SYL; the bound syllabogram is constrained to be the first syllable
                of a word in the logogram's semantic field (acrophony). This constraint
                exists in no published model
  fraction      numeric; excluded from alignment

Validation is the point. Run on Linear B with the Greek values hidden, the framework
must recover them; and it must report how many bits each constraint contributed, so
that the same accounting can be applied to Linear A with the answer unknown.
"""
import math
import re
from collections import defaultdict

# IPA feature vectors for the consonants and vowels a CV syllabary can carry.
# Each feature is binary; distance between two sounds is Hamming distance over features.
CONSONANTS = {
    'p': dict(voice=0, place='labial', manner='stop'),
    'b': dict(voice=1, place='labial', manner='stop'),
    't': dict(voice=0, place='alveolar', manner='stop'),
    'd': dict(voice=1, place='alveolar', manner='stop'),
    'k': dict(voice=0, place='velar', manner='stop'),
    'g': dict(voice=1, place='velar', manner='stop'),
    'q': dict(voice=0, place='labiovelar', manner='stop'),
    'm': dict(voice=1, place='labial', manner='nasal'),
    'n': dict(voice=1, place='alveolar', manner='nasal'),
    'r': dict(voice=1, place='alveolar', manner='liquid'),
    'l': dict(voice=1, place='alveolar', manner='liquid'),
    's': dict(voice=0, place='alveolar', manner='fricative'),
    'z': dict(voice=1, place='alveolar', manner='fricative'),
    'w': dict(voice=1, place='labial', manner='glide'),
    'j': dict(voice=1, place='palatal', manner='glide'),
    'h': dict(voice=0, place='glottal', manner='fricative'),
    '': dict(voice=0, place='none', manner='none'),      # bare vowel sign
}
VOWELS = {
    'a': dict(height='low', back='central', round=0),
    'e': dict(height='mid', back='front', round=0),
    'i': dict(height='high', back='front', round=0),
    'o': dict(height='mid', back='back', round=1),
    'u': dict(height='high', back='back', round=1),
}


def split_syllable(value):
    """'ka' -> ('k','a'); 'a' -> ('','a'). Returns None for anything that is not CV."""
    m = re.fullmatch(r'([a-z]?)([aeiou])', value)
    if not m or m.group(1) not in CONSONANTS:
        return None
    return m.group(1), m.group(2)


def phonetic_distance(value_a, value_b):
    """Distance between two CV values: feature mismatches of consonant plus of vowel."""
    sa, sb = split_syllable(value_a), split_syllable(value_b)
    if sa is None or sb is None:
        return None
    ca, cb = CONSONANTS[sa[0]], CONSONANTS[sb[0]]
    va, vb = VOWELS[sa[1]], VOWELS[sb[1]]
    return (sum(ca[k] != cb[k] for k in ca) + sum(va[k] != vb[k] for k in va))


class MixedCorpus:
    """A corpus of a mixed script, classified sign by sign into the four kinds."""

    LOGOGRAMS = {'GRA', 'NI', 'VIN', 'OLIV', 'OLE', 'CYP', 'FIC', 'AROM', 'TELA',
                 'LANA', 'VIR', 'MUL', 'OVIS', 'CAP', 'SUS', 'BOS', 'EQU', 'HORD',
                 'FAR', 'ROTA', 'CUR', 'HAS', 'PUG', 'GAL', 'AUR', 'AES'}
    FRACTION = re.compile(r'^[\d¹²³⁴⁵⁶⁷⁸⁹₀-₉⁄/½⅓⅔¼¾⅛JEDBKFLMXYZ]+$')

    def __init__(self, documents):
        """documents: list of (name, [tokens]); a token is 'KA-RU', 'GRA', 'GRA+PA', '12'."""
        self.units = []          # syllabic sequences, as tuples of sign names
        self.ligatures = []      # (logogram, bound syllabogram)
        self.logograms = defaultdict(int)
        self.fractions = 0
        for name, tokens in documents:
            for tok in tokens:
                self._classify(tok)

    def _classify(self, tok):
        if not isinstance(tok, str) or not tok or tok == '𐄁':
            return
        if '+' in tok:
            parts = tok.split('+')
            if parts[0] in self.LOGOGRAMS:
                for bound in parts[1:]:
                    if re.fullmatch(r'[A-Z]{1,3}[₂₃]?', bound):
                        self.ligatures.append((parts[0], bound.lower()))
                self.logograms[parts[0]] += 1
                return
        if tok in self.LOGOGRAMS:
            self.logograms[tok] += 1
            return
        if self.FRACTION.match(tok):
            self.fractions += 1
            return
        if '-' in tok:
            signs = tuple(s.lower() for s in tok.split('-') if s)
            if len(signs) >= 2:
                self.units.append(signs)

    def sign_inventory(self):
        return sorted({s for u in self.units for s in u} | {b for _, b in self.ligatures})

    def summary(self):
        return {'units': len(self.units), 'ligatures': len(self.ligatures),
                'logogram_tokens': sum(self.logograms.values()),
                'logogram_types': len(self.logograms), 'fractions': self.fractions,
                'signs': len(self.sign_inventory())}


def ligature_constraint(corpus, field_lexicon):
    """For each syllabogram bound to exactly one logogram, the set of CV values it may take
    under acrophony: the first syllables of words in that logogram's field.

    field_lexicon: {logogram: set of words}. Returns {sign: set of allowed values}.
    """
    bound_to = defaultdict(set)
    for logo, sign in corpus.ligatures:
        bound_to[sign].add(logo)
    allowed = {}
    for sign, logos in bound_to.items():
        if len(logos) != 1:
            continue
        logo = next(iter(logos))
        firsts = set()
        for w in field_lexicon.get(logo, ()):
            m = re.match(r'([a-z]?)([aeiou])', w.lower())
            if m and m.group(1) in CONSONANTS:
                firsts.add(m.group(1) + m.group(2))
        if firsts:
            allowed[sign] = firsts
    return allowed


def bits_removed(allowed, total_values):
    """How many bits a constraint dictionary removes from the search space."""
    return sum(math.log2(total_values) - math.log2(len(v)) for v in allowed.values())
