"""Name matching against a reference lexicon, with a null.

A Linear A unit that coincides with a Linear B place or person name is the
classical route to a reading (pa-i-to, su-ki-ri-ta, di-ki-te). The route has
prior art and no null: with two syllabaries that share most of their signs,
some coincidences are expected by chance. NameMatcher counts the matches and
compares them with what shuffled units of the same lengths produce.

Three match grades, from strict to loose:
  exact   the unit equals a reference word
  stem    the unit equals a reference word minus its last syllable (the
          reference language adds an ending: pa-i-to / pa-i-ti-jo)
  near    one syllable differs (substitution), same length
"""
import random
import re
from collections import Counter, defaultdict

SUB = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')


def syls(word):
    return [s.translate(SUB) for s in word.lower().split('-') if s]


class NameMatcher:
    def __init__(self, units, reference, seed=0):
        """units: iterable of Linear A units ('KU-PA-RI'); reference: iterable of words
        in the reference lexicon ('ku-pa-ri-jo'). Only syllabic units are kept."""
        self.units = sorted({'-'.join(syls(u)) for u in units
                             if re.fullmatch(r'[A-Za-z₀-₉0-9\-]+', u) and '-' in u})
        self.ref = sorted({'-'.join(syls(w)) for w in reference if '-' in w})
        self.ref_set = set(self.ref)
        self.ref_stems = defaultdict(set)
        for w in self.ref:
            s = syls(w)
            if len(s) >= 3:
                self.ref_stems['-'.join(s[:-1])].add(w)
        self.ref_by_len = defaultdict(list)
        for w in self.ref:
            self.ref_by_len[len(syls(w))].append(syls(w))
        self.rng = random.Random(seed)

    def match(self, units=None):
        units = units if units is not None else self.units
        out = {'exact': [], 'stem': [], 'near': []}
        for u in units:
            s = syls(u)
            if u in self.ref_set:
                out['exact'].append((u, u)); continue
            if len(s) >= 2 and u in self.ref_stems:
                out['stem'].append((u, sorted(self.ref_stems[u])[0])); continue
            if len(s) >= 3:
                for r in self.ref_by_len[len(s)]:
                    if sum(a != b for a, b in zip(s, r)) == 1:
                        out['near'].append((u, '-'.join(r))); break
        return out

    def shuffled_units(self):
        """same multiset of syllables and word lengths, order destroyed."""
        pool = [x for u in self.units for x in syls(u)]
        self.rng.shuffle(pool)
        out, i = [], 0
        for u in self.units:
            n = len(syls(u))
            out.append('-'.join(pool[i:i + n])); i += n
        return out

    def null(self, reps=200):
        obs = {k: len(v) for k, v in self.match().items()}
        counts = {k: [] for k in obs}
        for _ in range(reps):
            m = self.match(self.shuffled_units())
            for k in obs:
                counts[k].append(len(m[k]))
        res = {}
        for k in obs:
            c = counts[k]
            res[k] = {'observed': obs[k], 'null_mean': sum(c) / len(c),
                      'null_max': max(c),
                      'p': sum(1 for x in c if x >= obs[k]) / len(c)}
        return res

    def unit_probability(self, unit, grade='exact', reps=500):
        """how often a shuffled unit of this length lands on a match of this grade;
        the per-unit chance level, for ranking individual coincidences."""
        n = len(syls(unit))
        pool = [x for u in self.units for x in syls(u)]
        hits = 0
        for _ in range(reps):
            w = '-'.join(self.rng.sample(pool, n))
            m = self.match([w])
            if grade == 'exact' and m['exact']: hits += 1
            elif grade == 'stem' and (m['exact'] or m['stem']): hits += 1
            elif grade == 'near' and any(m.values()): hits += 1
        return hits / reps


BREAK = '\U0001076b'


def broken_status(inscriptions):
    """From the raw lineara.xyz records: for every syllabic unit, whether it is intact in at
    least one attestation. The 'words' field keeps the break sign; 'transliteratedWords'
    drops it. Returns {unit: 'intact' | 'broken'}. A unit broken everywhere must not enter
    an exact match: ]MA-TE-RE is not MA-TE-RE."""
    status = {}
    for _, it in inscriptions:
        w = [x for x in it.get('words', []) if x != '\n']
        t = [x for x in it.get('transliteratedWords', []) if x != '\n']
        if len(w) != len(t):
            continue
        for raw, tr in zip(w, t):
            if not isinstance(tr, str) or '-' not in tr:
                continue
            u = '-'.join(syls(tr))
            intact = BREAK not in raw
            status[u] = 'intact' if (intact or status.get(u) == 'intact') else 'broken'
    return status
