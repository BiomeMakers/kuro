"""Claims that predict held-out material, which the rest of this package cannot express.

Every other instrument here describes the corpus: how often two units meet, whether a class has a
distinctive vocabulary, how quantities distribute. None of them predicts. That matters because the
protocol's third requirement is a prediction about unseen text, and it was demanded of others seven
times before this project could meet it once.

A predictive claim is contrasted differently from a distributional one, and both differences are
easy to get wrong:

**The baseline is not a permutation.** Predicting a held-out slot has to beat *guessing the most
frequent element*, which is often surprisingly hard. A predictor can beat a shuffled null and still
be worse than always saying the same thing.

**And the alignment must not leak into the evaluation.** The first run of the libation experiment
scored 20.2% and eleven of its seventeen hits were the anchor position — the very position used to
align the inscriptions. Predicting what you aligned on is circular. `held_out` therefore takes the
positions to exclude, and refuses to run without being told about them.

    from kuro import PredictiveTest
    t = PredictiveTest(items, key=lambda x: x['slots'])
    t.run(predictor, exclude_positions={0})
    t.report()
"""
import random
import statistics as st
from collections import Counter, defaultdict


class PredictiveTest:
    def __init__(self, items, exclude_positions=None, seed=0):
        """items: {name: {position: element}}. One entry per document."""
        self.items = {k: dict(v) for k, v in items.items()}
        if exclude_positions is None:
            raise ValueError(
                'exclude_positions must be given, even if empty. A position used to align the '
                'material cannot also be predicted from it: the libation experiment scored 20.2% '
                'that way and eleven of seventeen hits were the alignment anchor.')
        self.exclude = set(exclude_positions)
        self.rng = random.Random(seed)
        self.result = None

    # ---- the baseline that matters ---------------------------------------------------------------
    def base_rate(self):
        """Always guessing the most frequent element. The real bar, and often a high one."""
        c = Counter(e for sl in self.items.values()
                    for p, e in sl.items() if p not in self.exclude)
        if not c:
            return {'element': None, 'hits': 0, 'trials': 0, 'rate': 0.0}
        top = c.most_common(1)[0][0]
        trials = sum(c.values())
        return {'element': top, 'hits': c[top], 'trials': trials, 'rate': c[top] / trials}

    # ---- leave-one-out --------------------------------------------------------------------------
    def _evaluate(self, items, predictor):
        hits, trials, detail = 0, 0, []
        for name, slots in items.items():
            train = {k: v for k, v in items.items() if k != name}
            for pos, true in slots.items():
                if pos in self.exclude:
                    continue
                companions = {v for p, v in slots.items() if p != pos}
                guess = predictor(train, pos, companions)
                if guess is None:
                    continue
                trials += 1
                if guess == true:
                    hits += 1
                    detail.append((name, pos, true))
        return hits, trials, detail

    def run(self, predictor, n_null=2000):
        """Leave-one-out prediction, against the base rate and against a permutation null."""
        hits, trials, detail = self._evaluate(self.items, predictor)
        if not trials:
            return {'note': 'no slot could be predicted; check exclude_positions and the data'}
        null = []
        for _ in range(n_null):
            shuffled = {}
            for name, slots in self.items.items():
                free = [p for p in slots if p not in self.exclude]
                vals = [slots[p] for p in free]
                self.rng.shuffle(vals)
                s = {p: slots[p] for p in slots if p in self.exclude}
                s.update(dict(zip(free, vals)))
                shuffled[name] = s
            h, t, _ = self._evaluate(shuffled, predictor)
            null.append(h / t if t else 0.0)
        base = self.base_rate()
        rate = hits / trials
        k = sum(1 for x in null if x >= rate)
        self.result = {
            'hits': hits, 'trials': trials, 'rate': rate,
            'base_rate': base['rate'], 'base_element': base['element'],
            'beats_base': rate > base['rate'],
            'null_mean': st.mean(null), 'null_p95': sorted(null)[int(0.95 * len(null))],
            'p': k / n_null, 'p_floor': 1 / n_null,
            'excluded_positions': sorted(self.exclude),
            'hits_detail': detail,
            'concentration': Counter(e for _, _, e in detail).most_common(5)}
        return self.result

    def as_hypothesis(self, claim, refuted_by, units=()):
        """The claim this test supports, with its p already set and its baseline recorded."""
        from .hypothesis import Hypothesis
        if self.result is None:
            raise RuntimeError('run() first')
        h = Hypothesis(claim=claim, refuted_by=refuted_by, kind='predictive', units=list(units))
        h.p = self.result['p']
        h.p_floor = self.result['p_floor']
        h.observed = self.result['rate']
        h.null_mean = self.result['null_mean']
        shown = (f"p = {h.p:.4f}" if h.p else f"p < {h.p_floor:.4g}")
        h.log.append({'step': 'null', 'outcome': 'pass' if h.p < 0.05 else 'fail',
                      'detail': f'{self.result["hits"]}/{self.result["trials"]} '
                                f'({100 * self.result["rate"]:.1f}%) against a base rate of '
                                f'{100 * self.result["base_rate"]:.1f}% and a null of '
                                f'{100 * self.result["null_mean"]:.1f}%, {shown}'})
        h.log.append({'step': 'control:baseline',
                      'outcome': 'pass' if self.result['beats_base'] else 'stop',
                      'detail': ('beats always-guess-the-commonest'
                                 if self.result['beats_base'] else
                                 'does NOT beat always guessing the commonest element, so it '
                                 'predicts nothing a constant guess would not')})
        if not self.result['beats_base']:
            h.status = 'not_supported'
        h.log.append({'step': 'control:leakage', 'outcome': 'pass',
                      'detail': f'positions {self.result["excluded_positions"]} excluded from '
                                f'evaluation as used for alignment'})
        return h

    def report(self):
        r = self.result
        if not r:
            return 'not run'
        lines = [f'{r["hits"]}/{r["trials"]} predicted ({100 * r["rate"]:.1f}%)', '',
                 f'  base rate (always "{r["base_element"]}")   {100 * r["base_rate"]:5.1f}%',
                 f'  permutation null                {100 * r["null_mean"]:5.1f}%  '
                 f'(p95 {100 * r["null_p95"]:.1f}%)',
                 f'  p                               {r["p"]:.4f}',
                 f'  positions excluded              {r["excluded_positions"]}', '',
                 '  hits concentrate on:']
        for e, c in r['concentration']:
            lines.append(f'    {e:<24} {c}')
        return '\n'.join(lines)
