"""Provenance labels for every figure a report states.

Adapted from the practice of Briakos (2026), who labels each statistic in his thesis as
computed, cited or illustrative. A report that mixes a measured value with a remembered
one is the easiest kind of paper to discredit, and the hardest error to notice from inside.

    from kuro import Fact
    Fact.computed(0.215, 'mean Jaccard of logograms within series', source='inscriptions.json')
    Fact.cited(0.55, 'lower bound of the astringent-to-oil ratio', source='Dioscorides I.56 via Shelmerdine 1985')
    Fact.illustrative(0.20, 'typical olive oil yield from fruit')

Printing a Fact prints its value with its tier marker; `Fact.legend()` explains the markers.
"""
import hashlib, os
from dataclasses import dataclass, field
from typing import Optional

TIERS = {
    'computed': ('[C]', 'computed from the corpus in this run; the source file hash is recorded'),
    'cited': ('[L]', 'taken from published literature; the source is named'),
    'illustrative': ('[~]', 'illustrative only; not evidence, and not to be cited as a figure'),
}


def file_hash(path, length=16):
    """Short SHA256 of a data file, so a computed figure can be traced to its input."""
    if not os.path.exists(path):
        return 'missing'
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()[:length]


@dataclass
class Fact:
    """A number with its provenance. Never let a figure travel without one."""
    value: float
    what: str
    tier: str = 'computed'
    source: Optional[str] = None
    digest: Optional[str] = None

    @classmethod
    def computed(cls, value, what, source=None):
        d = file_hash(source) if source and os.path.exists(source) else None
        return cls(value, what, 'computed', source, d)

    @classmethod
    def cited(cls, value, what, source):
        return cls(value, what, 'cited', source)

    @classmethod
    def illustrative(cls, value, what, source=None):
        return cls(value, what, 'illustrative', source)

    def __str__(self):
        mark = TIERS[self.tier][0]
        v = f'{self.value:.4g}' if isinstance(self.value, float) else str(self.value)
        tail = ''
        if self.tier == 'computed' and self.digest:
            tail = f' (sha256:{self.digest})'
        elif self.source:
            tail = f' ({self.source})'
        return f'{mark} {v}  {self.what}{tail}'

    @staticmethod
    def legend():
        return '\n'.join(f'  {m}  {desc}' for m, desc in TIERS.values())
