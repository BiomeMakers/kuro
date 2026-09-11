"""Search over the sound values of the Linear A syllabograms.

Every phonological comparison of Minoan assumes the Linear B values for the ~75 Linear A signs.
ValueSearch turns the assumption into a variable: for a candidate language, find the assignment
of consonant values to signs that brings the Minoan consonant-bigram profile closest to it, by
simulated annealing over swaps (the inventory of values is preserved, so the search cannot
invent consonants the script could not write).

The null is the point of the exercise: with 75 free values anything can be made to resemble
anything. The same search is run on a control Minoan whose syllable order inside words has been
destroyed (same signs, same word lengths, no real sequences). A candidate counts only if the
real corpus can be brought closer than the control can, by more than the spread of the control.
"""
import math, random
from collections import Counter

VOWELS = set('aeiou')


def consonant_of(syl):
    s = ''.join(ch for ch in syl.lower() if ch.isalpha() or ch in '₂₃')
    s = s.replace('₂', '').replace('₃', '')
    return ''.join(ch for ch in s if ch not in VOWELS)


def profile(skeletons):
    cnt = Counter()
    for s in skeletons:
        s = '#' + s + '#'
        for a, b in zip(s, s[1:]):
            cnt[a + b] += 1
    tot = sum(cnt.values()) or 1
    return {k: v / tot for k, v in cnt.items()}


def jsd(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * math.log(a[k] / m[k]) for k in a if a[k] > 0)
    return 0.5 * kl(p) + 0.5 * kl(q)


class ValueSearch:
    # signs whose Linear B value is anchored by the place and personal names shared with Linear B
    # (pa-i-to, su-ki-ri-ta, se-to-i-ja, da-i-pi-ta, i-ta-ja, ki-da-ro) plus the five plain vowels
    ANCHORED = {'pa', 'i', 'to', 'su', 'ki', 'ri', 'ta', 'se', 'ja', 'da', 'pi', 'ro', 'a', 'e', 'o', 'u'}

    def __init__(self, words, seed=0, fixed=()):
        """words: Linear A words as lists of syllable tokens ('pa','i','to'); fixed: signs whose
        value the search may not move ('anchored' for the toponym-anchored set)."""
        self.words = [w for w in words if w]
        self.signs = sorted({s for w in self.words for s in w})
        self.fixed = set(self.ANCHORED) if fixed == 'anchored' else set(fixed)
        self.free = [s for s in self.signs if s not in self.fixed]
        self.lb = {s: consonant_of(s) for s in self.signs}
        self.rng = random.Random(seed)

    def skeletons(self, words, assign):
        return [''.join(assign.get(s, '') for s in w) for w in words]

    def distance(self, words, assign, target):
        return jsd(profile(self.skeletons(words, assign)), target)

    def anneal(self, words, target, steps=4000, t0=0.02, seed=None):
        """simulated annealing over swaps of two signs' values; returns (best_distance, assignment)."""
        rng = random.Random(seed if seed is not None else self.rng.random())
        assign = dict(self.lb)
        cur = self.distance(words, assign, target); best, best_a = cur, dict(assign)
        for i in range(steps):
            t = t0 * (1 - i / steps) + 1e-6
            a, b = rng.sample(self.free, 2)
            assign[a], assign[b] = assign[b], assign[a]
            d = self.distance(words, assign, target)
            if d < cur or rng.random() < math.exp((cur - d) / t):
                cur = d
                if d < best:
                    best, best_a = d, dict(assign)
            else:
                assign[a], assign[b] = assign[b], assign[a]
        return best, best_a

    def control_words(self, seed):
        """same signs and word lengths, syllable order destroyed across the corpus."""
        rng = random.Random(seed)
        pool = [s for w in self.words for s in w]; rng.shuffle(pool)
        out, i = [], 0
        for w in self.words:
            out.append(pool[i:i + len(w)]); i += len(w)
        return out

    def run(self, target, steps=4000, controls=5, seed_offset=0):
        lb = self.distance(self.words, self.lb, target)
        real, real_a = self.anneal(self.words, target, steps, seed=1)
        ctrl = [self.anneal(self.control_words(seed=10 + seed_offset + k), target, steps, seed=100 + seed_offset + k)[0] for k in range(controls)]
        mean = sum(ctrl) / len(ctrl); sd = (sum((x - mean) ** 2 for x in ctrl) / max(1, len(ctrl) - 1)) ** 0.5
        return {'lb': lb, 'real_best': real, 'control_best': ctrl, 'control_mean': mean, 'control_sd': sd,
                'z': (mean - real) / sd if sd > 0 else None, 'assignment': real_a,
                'changed': sum(1 for s in self.signs if real_a[s] != self.lb[s]), 'fixed': sorted(self.fixed & set(self.signs))}
