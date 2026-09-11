"""The quantity profile of a logogram, against the base rate of all commodity logograms.

A reading of a logogram as a commodity class predicts how it is counted: persons and livestock
in whole units, bulk commodities in large whole figures, fine commodities (spices, saffron,
metal) in small fractional amounts, liquids and staples with fractions at the base rate.
ProfileTest measures the fraction rate of one logogram against the pooled base rate of every
logogram that carries a figure, with a binomial p in the direction the reading predicts, and
records the maximum figure and the companions. It cannot say WHICH commodity a sign is; it can
say whether a proposed class is compatible with how the sign is counted.

Calibrated on 10 Sep 2026 on logograms already read (VIR, GRA, CYP, OLE, VIN, OLIV, NI, *21-*23).
"""
import re
from collections import Counter, defaultdict
from math import comb

FR = set('JEDBKFLMXY')


def is_frac(x):
    return x in FR or bool(re.fullmatch(r'[¹²³⁴⁵⁶⁷⁸⁹][⁄/][₀-₉]+|½|⅓|¼|⅛|⅝|¾', x))


def is_num(x):
    return bool(re.fullmatch(r'\d+', x))


def is_logogram(t):
    return '-' not in t and bool(re.fullmatch(r'(?:\*\d+[A-Z]?|[A-Z][A-Z0-9]*[FM]?)(\+[A-Z0-9*\[\]?]+)*', t)) and len(t) >= 2


CLASSES = {
    # predicted direction of the fraction rate against the base, and whether large figures fit
    'persons':  ('below', 'large'),
    'livestock': ('below', 'large'),
    'bulk':     ('below', 'large'),
    'fine':     ('above', 'small'),
    'liquid':   ('base', 'any'),
    'staple':   ('base', 'any'),
    'textile':  ('below', 'any'),
}


class ProfileTest:
    def __init__(self, docs):
        """docs: list of token lists (transliteratedWords without newlines)."""
        self.stats = defaultdict(Counter)
        self.companions = defaultdict(Counter)
        for toks in docs:
            logos = [t.split('+')[0] for t in toks if is_logogram(t)]
            for i, t in enumerate(toks):
                if not is_logogram(t):
                    continue
                j, nums, fr = i + 1, [], False
                while j < len(toks) and (is_num(toks[j]) or is_frac(toks[j])):
                    fr = fr or is_frac(toks[j]); nums.append(toks[j]); j += 1
                if not nums:
                    continue
                ints = [int(x) for x in nums if is_num(x)]
                keys = {t, t.split('+')[0]}       # the ligature and its base sign both count
                for key in keys:
                    s = self.stats[key]; s['n'] += 1; s['frac'] += fr
                    if ints:
                        s['max'] = max(s['max'], max(ints)); s['sum'] += max(ints)
                for o in set(logos):
                    if o != t.split('+')[0]:
                        self.companions[t][o] += 1
        bases = {k: v for k, v in self.stats.items() if '+' not in k}
        tot = sum(s['n'] for s in bases.values())
        self.base = sum(s['frac'] for s in bases.values()) / tot if tot else 0.0

    def profile(self, sign):
        s = self.stats.get(sign)
        if not s or s['n'] == 0:
            return None
        return {'n': s['n'], 'frac': s['frac'], 'frac_rate': s['frac'] / s['n'], 'max': s['max'],
                'mean_max': s['sum'] / s['n'], 'base': self.base,
                'companions': self.companions[sign].most_common(4)}

    def test(self, sign, klass):
        """p-value that the sign's fraction rate lies in the direction the class predicts."""
        if klass not in CLASSES:
            raise ValueError(f'class must be one of {sorted(CLASSES)}')
        pr = self.profile(sign)
        if pr is None:
            return {'sign': sign, 'class': klass, 'p': None, 'why': 'no quantified attestation'}
        direction, size = CLASSES[klass]
        n, k, b = pr['n'], pr['frac'], self.base
        below = sum(comb(n, i) * b ** i * (1 - b) ** (n - i) for i in range(0, k + 1))
        above = sum(comb(n, i) * b ** i * (1 - b) ** (n - i) for i in range(k, n + 1))
        if direction == 'below':
            p = below
        elif direction == 'above':
            p = above
        else:
            p = min(1.0, 2 * min(below, above))   # 'base': compatible if NOT significantly off
        size_ok = True
        if size == 'small' and pr['max'] > 30:
            size_ok = False
        if size == 'large' and pr['max'] < 3 and n >= 5:
            size_ok = False
        return {'sign': sign, 'class': klass, 'p': p, 'direction': direction,
                'compatible': (p < 0.05 if direction != 'base' else p > 0.05) and size_ok,
                'profile': pr, 'size_ok': size_ok, 'n': n}
