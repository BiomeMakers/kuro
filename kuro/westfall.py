"""Multiple-comparison correction that uses the dependence between tests instead of ignoring it.

Bonferroni assumes the tests are independent. Ours are not: forty adjacency candidates share units,
so CYP appears in several pairs and NI in several others. Forty overlapping tests are not forty
independent ones, and dividing alpha by forty throws away power that the correlation would have
given back.

The Westfall-Young permutation procedure keeps, for each permutation of the data, the **minimum**
p-value across the whole family. The distribution of that minimum carries the dependence between
tests, so the adjusted p-value is the proportion of permutations whose best result beats the
observed one. Where tests are strongly correlated it is markedly more powerful than Bonferroni;
where they are independent it converges to it.

    from kuro import WestfallYoung
    wy = WestfallYoung(statistics)      # one callable per hypothesis, taking a permuted world
    wy.run(permute, n=1000)
    wy.adjusted('CYP -> NI')

Terada, Tsuda and Sese, PNAS 110(32), 12996-13001, for the procedure and its fast variants.
"""
from collections import OrderedDict


class WestfallYoung:
    def __init__(self, tests):
        """tests: {name: callable(world) -> statistic}, higher meaning more extreme."""
        self.tests = OrderedDict(tests)
        self.observed = {}
        self.minima = []
        self.n = 0

    def run(self, permute, world, n=1000, seed=0):
        """Two passes: build each test's own null, then take the minimum p across the family.

        The first implementation took the maximum raw statistic across tests, which is wrong and
        was more conservative than Bonferroni: a pair occurring fifteen times and one occurring
        three times are not on the same scale, so the family maximum was always set by the
        frequent pairs and everything else was crushed. Westfall-Young needs **comparable**
        statistics, which means p-values, each computed against its own null.
        """
        import random
        rng = random.Random(seed)
        self.observed = {k: f(world) for k, f in self.tests.items()}

        # pass one: the null distribution of each statistic, from the same permutations
        worlds = [permute(world, rng) for _ in range(n)]
        null = {k: [f(w) for w in worlds] for k, f in self.tests.items()}
        self.raw = {k: sum(1 for v in null[k] if v >= self.observed[k]) / n for k in self.tests}

        # pass two: within each permutation, each test's p against its own null; keep the minimum
        self.minima = []
        for j in range(n):
            best = 1.0
            for k in self.tests:
                v = null[k][j]
                p = sum(1 for x in null[k] if x >= v) / n
                if p < best:
                    best = p
            self.minima.append(best)
        self.n = n
        return self

    def adjusted(self, name):
        """The share of permutations whose best p over the whole family is at least as small."""
        if not self.minima:
            raise RuntimeError('run() first')
        obs_p = self.raw[name]
        k = sum(1 for m in self.minima if m <= obs_p)
        return {'raw_p': obs_p, 'adjusted_p': k / self.n,
                'floor': 1 / self.n,
                'note': 'adjusted over the whole family using the distribution of the family '
                        'maximum, so the dependence between tests is used rather than assumed away'}

    def compare_with_bonferroni(self, name, alpha=0.05):
        a = self.adjusted(name)
        m = len(self.tests)
        return {'test': name, 'raw_p': a['raw_p'],
                'westfall_young': a['adjusted_p'],
                'bonferroni_threshold': alpha / m,
                'passes_wy': a['adjusted_p'] < alpha,
                'passes_bonferroni': a['raw_p'] < alpha / m,
                'power_gained': (a['adjusted_p'] < alpha) and not (a['raw_p'] < alpha / m)}

    def report(self, alpha=0.05):
        rows = [self.compare_with_bonferroni(k, alpha) for k in self.tests]
        gained = [r for r in rows if r['power_gained']]
        lines = [f'{len(self.tests)} tests, {self.n} permutations', '',
                 f'{"test":<34}{"raw p":>9}{"WY p":>9}  passes',
                 ]
        for r in sorted(rows, key=lambda x: x['raw_p'])[:12]:
            mark = ('WY only' if r['power_gained'] else
                    'both' if r['passes_bonferroni'] else
                    'WY' if r['passes_wy'] else '-')
            lines.append(f'{r["test"][:34]:<34}{r["raw_p"]:>9.4f}{r["westfall_young"]:>9.4f}  {mark}')
        lines += ['', f'declared by Westfall-Young and not by Bonferroni: {len(gained)}']
        return '\n'.join(lines)
