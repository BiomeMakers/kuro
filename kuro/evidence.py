"""Provenance tags for every figure a report states.

Adopted from Briakos (2026), whose thesis labels each statistic by where it comes from.
The point is that a number computed from the corpus and a number recalled from the
literature must not read alike. Three tiers:

    COMPUTED  measured from the loaded corpus in this session; carries the corpus hash
    CITED     taken from a publication; carries the citation
    ILLUSTRATIVE  an order of magnitude or a general fact, not verified here

Use Value(x, COMPUTED, corpus_hash) and let str() do the work: the tag travels with
the number into every report, so no reader has to guess which is which.
"""
import hashlib, os

COMPUTED = 'computed'
CITED = 'cited'
ILLUSTRATIVE = 'illustrative'

MARK = {COMPUTED: '[C]', CITED: '[L]', ILLUSTRATIVE: '[~]'}
LEGEND = ('[C] computed from the loaded corpus   '
          '[L] taken from the literature, cited   '
          '[~] illustrative, not verified here')


def corpus_hash(path, n=16):
    """SHA-256 of the corpus file, truncated. Two runs on different files cannot be confused."""
    if not path or not os.path.exists(path):
        return 'unknown'
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()[:n]


class Value:
    """A number that carries where it came from."""

    __slots__ = ('value', 'tier', 'source')

    def __init__(self, value, tier=COMPUTED, source=''):
        self.value = value; self.tier = tier; self.source = source

    def __float__(self):
        return float(self.value)

    def __format__(self, spec):
        return format(self.value, spec)

    def __str__(self):
        v = self.value
        s = f'{v:.4g}' if isinstance(v, float) else str(v)
        tail = f' {self.source}' if self.source and self.tier != COMPUTED else ''
        return f'{s} {MARK[self.tier]}{tail}'

    __repr__ = __str__


def computed(v, h=''):
    return Value(v, COMPUTED, h)


def cited(v, ref):
    return Value(v, CITED, f'({ref})')


def illustrative(v, note=''):
    return Value(v, ILLUSTRATIVE, f'({note})' if note else '')
