"""Normalising the candidate lexicons so that they are objects of the same kind.

The anchored value search compared Minoan against eleven targets that were not comparable.
Ugaritic came from DULAT as a deduplicated lemma list, one entry per word. The TLHdig
languages came as raw token dumps: Hattian repeats *pa-la* 113 times, Luwian carries the
Sumerogram KI.MIN 94 times, Hurrian's commonest entry is a cuneiform sign, and Hittite's
top four are clitics. Comparing a lemma list with a token dump measures the difference
between those two things, not between the languages.

Normalisation makes every target one kind of object: deduplicated, alphabetic, without
logograms or single-syllable particles.
"""
import re
import unicodedata

VOWELS = set('aeiouāēīūáéíóúàèìòùâêîôûăĕĭŏŭ')
# Sumerograms and Akkadograms are written in capitals in the editorial convention
LOGOGRAM = re.compile(r'[A-Z]{2,}')
CUNEIFORM = re.compile('[\U00012000-\U0001247F]')


def is_usable(form):
    """A form is usable as lexical evidence if it is an alphabetic word of the language."""
    if not isinstance(form, str) or not form:
        return False
    if CUNEIFORM.search(form) or LOGOGRAM.search(form):
        return False
    stripped = form.strip('-–—.[]()<>?*')
    if len(stripped.replace('-', '')) < 3:
        return False
    return any(ch.isalpha() for ch in stripped)


def skeleton(form):
    """The consonant skeleton, with long and accented vowels treated as vowels.

    Decomposition is applied only to vowels: the consonant diacritics of Semitic and
    Anatolian transliteration (s-caron, s-dot, t-dot, h-breve) distinguish phonemes and
    must survive.
    """
    out = []
    for ch in form.lower():
        if not ch.isalpha():
            continue
        base = unicodedata.normalize('NFD', ch)[0]
        if base in VOWELS or ch in VOWELS:
            continue
        out.append(ch)
    return ''.join(out)


# Minoan skeletons run from one to four consonants, with 96% at four or fewer. A target
# whose forms are much longer is not comparable: a twelve-consonant skeleton contributes
# eleven bigrams that no Minoan word can produce. Iberian, a semi-syllabary whose
# transliteration does not segment as Minoan does, reaches twenty-four.
MAX_SKELETON = 6


def normalise(forms, max_skeleton=MAX_SKELETON):
    """One target, made comparable with the others and with Minoan.

    Deduplicated, alphabetic, without logograms, cuneiform signs or particles, and with
    skeletons no longer than Minoan itself produces. The length bound matters as much as
    the rest: without it Iberian returns a spuriously large negative because its long
    sequences fill the bigram profile with transitions Minoan cannot make.
    """
    out = set()
    for form in forms:
        if not is_usable(form):
            continue
        skel = skeleton(form)
        if skel and len(skel) <= max_skeleton:
            out.add(skel)
    return sorted(out)
