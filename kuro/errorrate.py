"""What each instrument gets wrong on corpora where the answer is known.

A p-value says how surprising a result would be under the null. It says nothing about how often
this instrument, on this kind of material, reports something that is not there. That second number
can be measured, because five corpora here have known or partly known answers, and it is what lets
a result be written as:

    p = 0.01, with an instrument that reports a false positive in N% of trials on corpora
    where the answer is known.

No proposed reading of Linear A can state that today.

    from kuro import ErrorRate
    er = ErrorRate()
    er.measure('positional_test', trials_on_known_corpora)
    print(er.report())

The measurement is deliberately simple: run the instrument on a corpus where the answer is known,
under conditions where it should find nothing, and count how often it finds something anyway.
"""
import json, os, random, statistics as st
from collections import defaultdict


class ErrorRate:
    """False-positive rates per instrument, measured on corpora with known answers."""

    def __init__(self, path=None):
        self.path = path or 'data/derived/error_rates.json'
        self.rates = {}
        if os.path.exists(self.path):
            with open(self.path, encoding='utf-8') as f:
                self.rates = json.load(f)

    def measure(self, instrument, corpus, trial, n=500, alpha=0.05, seed=0):
        """Run `trial` n times on material where nothing should be found; keep the whole curve.

        `trial` must return a p-value from a run in which the true answer is 'no effect' — for
        instance the instrument applied to a shuffled version of a known corpus, or applied to
        two halves of one homogeneous group.

        The rate is kept for several thresholds, not only for 0.05. A result at p = 0.0001 is not
        qualified by how often the instrument errs at 0.05; it is qualified by how often it errs
        at 0.0001, and that is usually a very different number.
        """
        rng = random.Random(seed)
        ps = [p for p in (trial(rng) for _ in range(n)) if p is not None]
        if not ps:
            raise ValueError('the trial returned no usable p-value; check it can run on this corpus')
        curve = {str(t): sum(1 for p in ps if p < t) / len(ps)
                 for t in (0.05, 0.01, 0.001, 0.0001)}
        rec = {'corpus': corpus, 'trials': len(ps), 'alpha': alpha,
               'false_positives': sum(1 for p in ps if p < alpha),
               'rate': sum(1 for p in ps if p < alpha) / len(ps),
               'curve': curve,
               'min_p_seen': min(ps),
               'median_p': st.median(ps)}
        self.rates.setdefault(instrument, []).append(rec)
        return rec

    MIN_TRIALS = 30   # below this, a rate of 0% says nothing about the instrument

    def rate_for(self, instrument):
        """The pooled false-positive rate, with a flag when there were too few trials to mean it.

        A rate of 0.0% from seven usable trials looks like a perfect instrument and is not a
        measurement: it is the absence of one. The adjacency test produced exactly that — seven
        usable trials out of 450 attempted, because pairs sharing enough documents are rare — and
        reporting it as 0.0% alongside a rate measured over 400 trials would be misleading.
        """
        recs = self.rates.get(instrument, [])
        if not recs:
            return None
        hits = sum(r['false_positives'] for r in recs)
        trials = sum(r['trials'] for r in recs)
        return {'instrument': instrument, 'corpora': len(recs), 'trials': trials,
                'false_positives': hits, 'rate': hits / trials,
                'underpowered': trials < self.MIN_TRIALS,
                'resolution': 1 / trials if trials else None}

    def rate_at(self, instrument, p):
        """The false-positive rate at the threshold this result actually reached.

        Returns None when the trials never reached that far down: with 400 trials, nothing can be
        said about behaviour at 0.0001, and saying it anyway would be inventing a number.
        """
        recs = self.rates.get(instrument, [])
        if not recs:
            return None
        thresholds = [float(t) for t in recs[0].get('curve', {})]
        usable = [t for t in thresholds if t >= p]
        if not usable:
            return None
        t = min(usable)
        trials = sum(r['trials'] for r in recs)
        rate = sum(r['curve'][str(t)] * r['trials'] for r in recs) / trials
        floor = 1.0 / trials
        return {'threshold': t, 'rate': rate, 'trials': trials,
                'resolution_floor': floor,
                'below_resolution': rate < floor}

    def qualify(self, instrument, p):
        """The sentence a result should carry, given what this instrument gets wrong at that p."""
        r5 = self.rate_for(instrument)
        if r5 is None:
            return (f'p = {p:.4g}. The false-positive rate of this instrument has not been '
                    f'measured, so the p-value stands alone.')
        if p == 0:
            return (f'p below the resolution of the null used. The instrument was tested '
                    f'{r5["trials"]} times on corpora with known answers and reported a false '
                    f'positive in {100 * r5["rate"]:.1f}% of them at the 5% threshold; a run that '
                    f'produces no null draw at or above the observed value cannot be qualified '
                    f'more finely than that.')
        if r5.get('underpowered'):
            return (f'p = {p:.4g}. The false-positive rate of this instrument could not be '
                    f'measured: only {r5["trials"]} trials were usable, below the {self.MIN_TRIALS} '
                    f'needed for a rate to mean anything. The p-value stands alone.')
        at = self.rate_at(instrument, p)
        if at is None:
            return (f'p = {p:.4g}. The instrument was tested {r5["trials"]} times on corpora with '
                    f'known answers and reported a false positive in {100 * r5["rate"]:.1f}% of '
                    f'them at the 5% threshold; its behaviour at {p:.4g} was not resolvable with '
                    f'that number of trials, so nothing is claimed about it.')
        if at['below_resolution']:
            return (f'p = {p:.4g}, at a threshold where the instrument produced no false positive '
                    f'in {at["trials"]} trials on corpora with known answers — that is, below the '
                    f'resolution of {at["resolution_floor"]:.4f} those trials afford.')
        return (f'p = {p:.4g}, with an instrument that reports a false positive in '
                f'{100 * at["rate"]:.2f}% of {at["trials"]} trials on corpora where the answer is '
                f'known, at the {at["threshold"]:g} threshold.')

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.rates, f, ensure_ascii=False, indent=1)

    def report(self):
        if not self.rates:
            return 'no error rates measured yet'
        lines = ['false-positive rates, measured on corpora with known answers', '']
        for inst in sorted(self.rates):
            r = self.rate_for(inst)
            flag = '  NOT MEASURED: too few usable trials' if r.get('underpowered') else ''
            lines.append(f'  {inst:<26} {100 * r["rate"]:5.1f}%  '
                         f'({r["false_positives"]}/{r["trials"]} over {r["corpora"]} corpora)'
                         + flag)
            for rec in self.rates[inst]:
                c = rec.get('curve', {})
                curve = '  '.join(f'{t}:{100 * v:.1f}%' for t, v in c.items())
                lines.append(f'      {rec["corpus"]:<30} {curve}')
        return '\n'.join(lines)
