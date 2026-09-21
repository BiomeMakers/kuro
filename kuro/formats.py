"""Tablet formats as profile models, learned from the corpus.

The votive formula was fixed by hand: a fixed opening, slots, anchors. The administrative
tablets have formats too, and nobody has enumerated them. This module learns them.

Each tablet becomes a sequence of functional categories (W a syllabic word, C a commodity
sign, N a figure, f a fraction, T a term of summation, L an isolated sign, | a separator).
Recurrent n-grams over those sequences are counted against a first-order Markov null that
preserves the category frequencies and the transitions between them, so a motif counts only
if the order carries information the transition probabilities do not.

A motif that survives is a format: a fragment of the template a scribe follows. The
validation is that the procedure recovers, without being told, the transaction pattern
| L | C fixed by hand on 10 September 2026 (SA-RO . TE . VIN).
"""
import random
import re
from collections import Counter, defaultdict

COMMODITY = {'GRA', 'NI', 'VIN', 'OLIV', 'OLE', 'CYP', 'FIC', 'AROM', 'TELA', 'LANA', 'VIR',
             'MA-RU', '*303', '*304', '*308', '*316', '*188', '*21F', '*21M', '*22F', '*22M', '*23M'}
TOTALS = {'KU-RO', 'KI-RO', 'PO-TO-KU-RO', 'DA-I'}
FRACTION_LETTERS = set('JEDBKFLMXY')


def is_number(t):
    return bool(re.fullmatch(r'\d+', t))


def is_fraction(t):
    # the edition writes some values as approximations ('≈ 1/6'); they are fractions
    t = t.replace('≈', '').strip()
    return t in FRACTION_LETTERS or bool(re.fullmatch(r'[¹²³⁴⁵⁶⁷⁸⁹][⁄/][₀-₉]+|½|⅓|¼', t))


def category(t):
    """One letter per token: the functional class, not the reading."""
    if t == '𐄁':
        return '|'
    if t in TOTALS:
        return 'T'
    if is_number(t):
        return 'N'
    if is_fraction(t):
        return 'f'
    if t.split('+')[0] in COMMODITY:
        return 'C'
    if '-' in t:
        return 'W'
    if re.fullmatch(r'\*?[A-Z][A-Z0-9]*(\+.*)?', t):
        return 'L'
    return '.'


class FormatModel:
    """Motifs of functional categories, against a first-order Markov null."""

    def __init__(self, documents, seed=0):
        """documents: list of (name, token list)."""
        self.docs = [(n, ''.join(category(t) for t in toks)) for n, toks in documents]
        self.docs = [(n, s) for n, s in self.docs if len(s) >= 4]
        self.rng = random.Random(seed)
        self.trans = defaultdict(Counter)
        for _, s in self.docs:
            for a, b in zip('^' + s, s + '$'):
                self.trans[a][b] += 1

    def _generate(self, length):
        out, cur = [], '^'
        for _ in range(length):
            nxt = [k for k in self.trans[cur] if k != '$']
            if not nxt:
                break
            cur = self.rng.choices(nxt, [self.trans[cur][k] for k in nxt])[0]
            out.append(cur)
        return ''.join(out)

    def _count(self, docs, k):
        c = Counter()
        for _, s in docs:
            for i in range(len(s) - k + 1):
                c[s[i:i + k]] += 1
        return c

    def motifs(self, k, reps=60, min_count=5):
        """n-grams of length k with their observed count, null mean and ratio."""
        obs = self._count(self.docs, k)
        null = Counter()
        for _ in range(reps):
            fake = [(n, self._generate(len(s))) for n, s in self.docs]
            for g, c in self._count(fake, k).items():
                null[g] += c / reps
        out = []
        for g, c in obs.items():
            if c < min_count:
                continue
            e = null.get(g, 0.0)
            out.append({'motif': g, 'observed': c, 'null': round(e, 2),
                        'ratio': round(c / e, 1) if e >= 0.5 else float('inf')})
        return sorted(out, key=lambda x: (-x['ratio'], -x['observed']))

    def documents_with(self, motif):
        return [n for n, s in self.docs if motif in s]
