"""The alignment model, written from Luo et al. (2021) §3 for a CV syllabary.

The published repository holds only the phonological embedding; the model itself (their
"core training and model modules") is listed as not yet released. What follows is the
model as described, reimplemented for syllabic signs, with the three linguistic
constraints they name: plausibility of sound change, preservation of sounds, and
monotonic alignment.

The problem. A lost sign inventory S (Linear A syllabograms) with unknown values; a known
vocabulary V (words of a candidate language, as CV syllable sequences); a corpus of lost
units, each a sequence of signs. Find the mapping f: S -> CV values that makes as many lost
units as possible align, monotonically and with plausible sound changes, to words of V.

The objective, per unit x and candidate word y, is the minimum over monotonic alignments
of the summed phonetic distance between f(x_i) and y_j, with insertion and deletion
penalties: an edit distance on the phonetic geometry (their §3.2.2). A unit is matched
when its best alignment falls below a threshold; the corpus score is the number of matched
units, and f is searched by simulated annealing over value swaps (their EM step replaced by
annealing, which the kuro value search already uses and which handles a discrete map).

Preservation of sounds (their Ω_loss) is enforced by construction: values are a permutation
of the inventory, so no sound disappears.

Validation. On Linear B the values are known. Hide them, run, and count how many of the
recovered values are the true ones. That number is the whole point.
"""
import math
import random

from kuro.mixed import CONSONANTS, VOWELS, phonetic_distance, split_syllable

INSERT = 2.5    # cost of a syllable in the known word with no counterpart in the lost unit
DELETE = 2.5    # cost of a lost sign with no counterpart
MAX_DIST = 4    # a substitution costlier than this is treated as impossible

# The distance between two CV values is fixed; computing it inside the alignment loop
# recomputes the same 85x85 table millions of times. Build it once.
_VALUES = [c + v for c in CONSONANTS for v in VOWELS]
_INDEX = {v: i for i, v in enumerate(_VALUES)}
_DIST = [[0.0] * len(_VALUES) for _ in _VALUES]
for _i, _a in enumerate(_VALUES):
    for _j, _b in enumerate(_VALUES):
        _d = phonetic_distance(_a, _b)
        _DIST[_i][_j] = _d if _d is not None and _d <= MAX_DIST else 99.0


def syllables_of(word):
    """A known word as a list of CV values: 'ku-pa-ro' -> ['ku','pa','ro']."""
    out = []
    for s in word.lower().split('-'):
        if split_syllable(s) is not None:
            out.append(s)
    return out


def align_cost(lost_values, known_syls):
    """Edit distance on the phonetic geometry, monotonic by construction."""
    return align_cost_idx([_INDEX[v] for v in lost_values],
                          [_INDEX[v] for v in known_syls])


def align_cost_idx(lost_idx, known_idx, ceiling=None):
    """The same, on precomputed indices, with early exit once the ceiling is passed."""
    m = len(known_idx)
    prev = [j * INSERT for j in range(m + 1)]
    for i, li in enumerate(lost_idx, start=1):
        row = _DIST[li]
        cur = [i * DELETE] + [0.0] * m
        best = cur[0]
        for j in range(1, m + 1):
            v = prev[j - 1] + row[known_idx[j - 1]]
            a = prev[j] + DELETE
            if a < v:
                v = a
            a = cur[j - 1] + INSERT
            if a < v:
                v = a
            cur[j] = v
            if v < best:
                best = v
        if ceiling is not None and best > ceiling:
            return best
        prev = cur
    return prev[m]


class Aligner:
    """Search over sign values so that lost units align to a known vocabulary."""

    def __init__(self, units, vocabulary, fixed=None, threshold=3.0, seed=0):
        self.units = [tuple(u) for u in units]
        self.vocab = [syllables_of(w) for w in vocabulary]
        self.vocab = [v for v in self.vocab if 2 <= len(v) <= 6]
        # Index the vocabulary by length, storing value indices rather than strings, and
        # again by (length, first value): a word whose first syllable is too far from the
        # unit's first sign cannot align below the threshold, so most of the vocabulary can
        # be skipped without computing its alignment at all.
        self.by_len = {}
        self.by_first = {}
        for v in self.vocab:
            idx = [_INDEX[s] for s in v]
            self.by_len.setdefault(len(v), []).append(idx)
            self.by_first.setdefault((len(v), idx[0]), []).append(idx)
        # for each value, the values whose distance from it is within the threshold
        self.near = [[j for j in range(len(_VALUES)) if _DIST[i][j] <= max(threshold, 1.0)]
                     for i in range(len(_VALUES))]
        self.signs = sorted({s for u in self.units for s in u})
        self.fixed = dict(fixed or {})
        self.threshold = threshold
        self.rng = random.Random(seed)
        self.values = sorted(c + v for c in CONSONANTS for v in VOWELS if c != '' or True)

    def initial_map(self):
        free = [s for s in self.signs if s not in self.fixed]
        pool = [v for v in self.values if v not in self.fixed.values()]
        self.rng.shuffle(pool)
        f = dict(self.fixed)
        for s, v in zip(free, pool):
            f[s] = v
        return f

    def unit_cost(self, unit, f):
        lost = [_INDEX[f[s]] for s in unit]
        best = math.inf
        first = lost[0]
        for L in range(max(2, len(lost) - 1), min(6, len(lost) + 1) + 1):
            for start in self.near[first]:
                for known in self.by_first.get((L, start), ()):
                    c = align_cost_idx(lost, known, ceiling=best)
                    if c < best:
                        best = c
                        if best <= self.threshold:
                            return best
        return best

    def score(self, f, sample=None):
        units = self.units if sample is None else self.rng.sample(self.units, min(sample, len(self.units)))
        return sum(1 for u in units if self.unit_cost(u, f) <= self.threshold)

    def anneal(self, steps=2000, t0=2.0, sample=150):
        f = self.initial_map()
        free = [s for s in self.signs if s not in self.fixed]
        cur = self.score(f, sample)
        best, best_f = cur, dict(f)
        for i in range(steps):
            t = t0 * (0.05 / t0) ** (i / max(steps - 1, 1))
            # two moves: swap the values of two signs, or give one sign an unused value.
            # Swapping alone cannot reach values outside the initial assignment.
            if len(free) >= 2 and self.rng.random() < 0.5:
                a, b = self.rng.sample(free, 2)
                undo = (a, f[a], b, f[b])
                f[a], f[b] = f[b], f[a]
            else:
                a = self.rng.choice(free)
                used = set(f.values())
                unused = [v for v in self.values if v not in used]
                if not unused:
                    continue
                undo = (a, f[a], None, None)
                f[a] = self.rng.choice(unused)
            new = self.score(f, sample)
            if new >= cur or self.rng.random() < math.exp((new - cur) / max(t, 1e-9)):
                cur = new
                if cur > best:
                    best, best_f = cur, dict(f)
            else:
                a, va, b, vb = undo
                f[a] = va
                if b is not None:
                    f[b] = vb
        return best_f, best

    @staticmethod
    def recovered(found, truth):
        """How many signs the search assigned their true value, or one the phonetic
        geometry cannot tell from it (l/r are one liquid in the geometry, as in Linear B)."""
        n = 0
        for s, v in truth.items():
            got = found.get(s)
            if got is not None and phonetic_distance(got, v) == 0:
                n += 1
        return n
