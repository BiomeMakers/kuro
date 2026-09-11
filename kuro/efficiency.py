"""What the cycle costs and what it saves, measured rather than assumed.

The literature on automated discovery systems reports filtering efficiency as two numbers: how much
work the filter removes, and how much of the good it removes with it. A filter that rejects
everything scores perfectly on the first and worthlessly on the second, so neither is reported
alone. This module computes both for our cycle, and a third the others do not need: how many claims
would have looked like results without it.

    from kuro import Efficiency
    e = Efficiency()
    e.record(candidate, verdict, p)
    print(e.report())
"""
from collections import Counter


class Efficiency:
    def __init__(self, alpha=0.05):
        self.alpha = alpha
        self.rows = []

    def record(self, claim, verdict, p=None, gated_at=None):
        self.rows.append({'claim': claim, 'verdict': verdict, 'p': p, 'gated_at': gated_at})

    @property
    def counts(self):
        return Counter(r['verdict'] for r in self.rows)

    def summary(self):
        n = len(self.rows)
        if not n:
            return {}
        gated = sum(1 for r in self.rows if r['verdict'] == 'published_already')
        measured = [r for r in self.rows if r['p'] is not None]
        naive = sum(1 for r in measured if r['p'] < self.alpha)
        survives = sum(1 for r in self.rows if r['verdict'] == 'survives')
        borderline = sum(1 for r in self.rows if r['verdict'] == 'borderline')
        return {
            'candidates': n,
            'gated_by_literature': gated,
            'gated_share': gated / n,
            'measured': len(measured),
            'would_look_like_results_at_alpha': naive,
            'survive_the_cycle': survives,
            'borderline': borderline,
            'reduction': 1 - survives / naive if naive else None,
            'note': ('reduction is only meaningful beside the recall of true effects, which this '
                     'corpus cannot supply: there is no key. It is reported as what it is — how '
                     'many apparent results the cycle removes — and not as accuracy.')}

    def report(self):
        s = self.summary()
        if not s:
            return 'nothing recorded'
        lines = [f'{s["candidates"]} candidates through the cycle', '',
                 f'  filtered by the novelty gate   {s["gated_by_literature"]:>4} '
                 f'({100 * s["gated_share"]:.0f}%)',
                 f'  measured                       {s["measured"]:>4}',
                 f'  would pass a bare p < {self.alpha}      {s["would_look_like_results_at_alpha"]:>4}',
                 f'  borderline after correction    {s["borderline"]:>4}',
                 f'  survive the whole cycle        {s["survive_the_cycle"]:>4}', '']
        if s['reduction'] is not None:
            lines.append(f'  apparent results removed: {100 * s["reduction"]:.0f}%')
        lines += ['', '  ' + s['note']]
        return '\n'.join(lines)
