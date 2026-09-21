"""A decipherment attempt, scored: assign values to the free signs and measure the result.

Everything before this measured pieces: whether a word finds a match, whether a function
holds, how many bits the corpus carries. An attempt is the whole thing at once. It assigns a
value to each of the free signs, applies the assignment to the entire corpus, and is scored by
three quantities that are independent of each other:

  lexical   how many intact units become real words of the target language
  functional how many of the units with a measured function become words whose meaning is
            what the distribution requires
  control   how the same score behaves on fictitious grids in the sense of Packard (1974),
            which is the only thing that says whether a score means anything

The search is simulated annealing over assignments, with the sixteen signs anchored by the
place names shared with Linear B held fixed. Any grid can also be scored directly, so a
published proposal can be placed on the same scale as a search result.
"""
import json
import math
import random
import re
from collections import defaultdict


def normalise_target(word, permissive):
    """A lexicon word reduced to the shape the syllabary could write."""
    table = {'ʾ': '', 'ʿ': '', 'ḥ': 'h', 'ḫ': 'x', 'š': 's', 'ṯ': 't', 'ḏ': 'd', 'ṣ': 's',
             'ṭ': 't', 'ā': 'a', 'ī': 'i', 'ū': 'u', 'ē': 'e', 'ō': 'o', 'ġ': 'g',
             'ỉ': 'i', 'ủ': 'u', 'ả': 'a', '₂': '', '₃': '', '₄': '', 'ʔ': '',
             'û': 'u', 'î': 'i', 'â': 'a', 'ê': 'e', 'ô': 'o', 'ú': 'u', 'í': 'i', 'á': 'a'}
    word = re.sub(r'\s*\(.*?\)', '', word).lower()
    out = ''
    for ch in word:
        ch = table.get(ch, ch)
        if ch in 'aeiou' or ch in 'pbtdkgqxszrlmnwyjh':
            out += ch
    if permissive:
        for a, b in (('b', 'p'), ('d', 't'), ('g', 'k'), ('q', 'k'), ('x', 'k'),
                     ('z', 's'), ('l', 'r'), ('j', 'y')):
            out = out.replace(a, b)
        out = out.replace('h', '')
    else:
        out = out.replace('j', 'y').replace('x', 'k')
    return out


def apply_grid(unit, grid, permissive):
    """A Linear A sign group read through an assignment of values."""
    out = ''
    for s in unit.lower().split('-'):
        v = grid.get(s, s)
        m = re.match(r'([bdgklmnpqrstwzjh]?)([aeiou])', v)
        if m:
            out += m.group(1) + m.group(2)
        elif re.fullmatch(r'[aeiou]', v):
            out += v
    if permissive:
        for a, b in (('b', 'p'), ('d', 't'), ('g', 'k'), ('q', 'k'), ('z', 's'), ('j', 'y')):
            out = out.replace(a, b)
    else:
        out = out.replace('j', 'y')
    return out


class Attempt:
    def __init__(self, units, lexicon, functions=None, values=None, anchored=None,
                 permissive=True, seed=0):
        """units: intact syllabic sign groups. lexicon: {form: set of meanings}.
        functions: {unit: regex the meaning must match}. values: the pool of sound values.
        anchored: {sign: value} held fixed."""
        self.units = units
        self.permissive = permissive
        self.lex = {normalise_target(f, permissive): m for f, m in lexicon.items()}
        self.lex_by_shape = defaultdict(set)
        for f, m in lexicon.items():
            self.lex_by_shape[normalise_target(f, permissive)].add(m)
        self.functions = functions or {}
        self.anchored = dict(anchored or {})
        self.signs = sorted({s for u in units for s in u.split('-')})
        self.free = [s for s in self.signs if s not in self.anchored]
        self.values = list(values or sorted({v for v in self.anchored.values()}))
        self.rng = random.Random(seed)

    def random_grid(self):
        g = dict(self.anchored)
        for s in self.free:
            g[s] = self.rng.choice(self.values)
        return g

    def score(self, grid):
        """Three independent counts; higher is better on the first two."""
        lex = func = 0
        for u in self.units:
            shape = apply_grid(u, grid, self.permissive)
            if not shape:
                continue
            meanings = self.lex_by_shape.get(shape)
            if meanings:
                lex += 1
                pat = self.functions.get(u.upper())
                if pat and any(re.search(pat, m.lower()) for m in meanings):
                    func += 1
        return {'lexical': lex, 'functional': func, 'units': len(self.units)}

    def anneal(self, steps=20000, t0=3.0, t1=0.01, weight_function=10):
        """Simulated annealing over assignments. The functional score is weighted because
        it is scarce: a corpus has hundreds of units and only dozens of fixed functions."""
        grid = self.random_grid()
        s = self.score(grid)
        cur = s['lexical'] + weight_function * s['functional']
        best, best_s, best_grid = cur, s, dict(grid)
        for i in range(steps):
            t = t0 * (t1 / t0) ** (i / max(steps - 1, 1))
            sign = self.rng.choice(self.free)
            old = grid[sign]
            grid[sign] = self.rng.choice(self.values)
            s2 = self.score(grid)
            new = s2['lexical'] + weight_function * s2['functional']
            if new >= cur or self.rng.random() < math.exp((new - cur) / max(t, 1e-9)):
                cur = new
                if new > best:
                    best, best_s, best_grid = new, s2, dict(grid)
            else:
                grid[sign] = old
        return {'score': best_s, 'grid': best_grid, 'objective': best}

    def fictitious(self, n=40):
        """Packard's control: grids that keep no sign at its own value."""
        out = []
        for _ in range(n):
            vals = list(self.values)
            g = dict(self.anchored)
            for s in self.free:
                g[s] = self.rng.choice(vals)
            out.append(self.score(g))
        return out
