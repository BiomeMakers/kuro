"""Co-occurrence at several orders, and co-exclusion.

Until now this project measured order zero only: two units in the same document. There is more,
and each order answers a different question.

  order 0  same document          — they belong to the same dossier
  order 1  adjacent               — they form a unit; this is what the continuity principle is about
  order 2  fixed separation       — there is a template
  co-exclusion                    — frequent units that never meet: incompatible categories

Each comes with its own null, because the same shuffle does not test all four.

    from kuro import Orders
    o = Orders(docs)
    o.adjacency('CYP', 'NI')          # do they go together, and how often
    o.fixed_separation('KU-RO')       # is it always the same distance from something
    o.coexclusion(min_expected=3)     # pairs that never meet and should have
"""
import random
from collections import Counter, defaultdict
from math import comb


class Orders:
    def __init__(self, docs, seed=0):
        """docs: list of token lists, already filtered to the units of interest."""
        self.docs = [list(d) for d in docs]
        self.rng = random.Random(seed)
        self.counts = Counter(t for d in self.docs for t in d)
        self.N = len(self.docs)

    # ---- order 0 ------------------------------------------------------------------------------
    def cooccurrence(self, a, b):
        both = sum(1 for d in self.docs if a in d and b in d)
        na = sum(1 for d in self.docs if a in d)
        nb = sum(1 for d in self.docs if b in d)
        exp = na * nb / self.N if self.N else 0
        p = (sum(comb(nb, x) * comb(self.N - nb, na - x)
                 for x in range(both, min(na, nb) + 1)) / comb(self.N, na)) if na and nb else 1
        return {'observed': both, 'expected': exp, 'p': p}

    # ---- hypotheses, ready made ---------------------------------------------------------------
    def as_hypothesis(self, result, claim, refuted_by, kind, units):
        """Turn a measurement into a Hypothesis with its p already set.

        Without this the measurement and the cycle live apart, and the p-value gets carried across
        by hand — which is where a confounder gets forgotten.
        """
        from .hypothesis import Hypothesis
        h = Hypothesis(claim=claim, refuted_by=refuted_by, kind=kind, units=units)
        h.p = result['p']
        h.p_floor = result.get('p_floor')
        h.observed = result.get('observed')
        h.null_mean = result.get('null_mean', result.get('expected'))
        shown = (f'p = {h.p:.4f}' if h.p else
                 f'p < {h.p_floor:.4g}' if h.p_floor else 'p = 0')
        h.log.append({'step': 'null', 'outcome': 'pass' if h.p < 0.05 else 'fail',
                      'detail': f'observed {h.observed}, null {h.null_mean}, {shown}'})
        return h

    def adjacency_hypothesis(self, a, b, n=2000):
        r = self.adjacency(a, b, n=n)
        return self.as_hypothesis(
            r, claim=f'{a} is immediately followed by {b} more often than chance',
            refuted_by=f'a corpus segment where {a} and {b} co-occur but are not adjacent',
            kind='positional', units=[a, b])

    def cooccurrence_hypothesis(self, a, b):
        r = self.cooccurrence(a, b)
        return self.as_hypothesis(
            r, claim=f'{a} and {b} share documents more often than chance',
            refuted_by=f'the association vanishing under a null that preserves site',
            kind='distributional', units=[a, b])

    # ---- order 1 ------------------------------------------------------------------------------
    def adjacency(self, a, b, n=2000):
        """How often a is immediately followed by b, against a null that shuffles within document.

        Shuffling within the document preserves which units share a document — so this tests
        adjacency and not co-occurrence, which order 0 already covers.
        """
        def count(docs):
            return sum(1 for d in docs for i in range(len(d) - 1) if d[i] == a and d[i + 1] == b)
        obs = count(self.docs)
        # only documents containing both can contribute; shuffling the rest is wasted work
        relevant = [list(d) for d in self.docs if a in d and b in d]
        if not relevant:
            return {'observed': obs, 'null_mean': 0.0, 'p': 1.0,
                    'note': 'no document contains both'}
        null = []
        for _ in range(n):
            tot = 0
            for e in relevant:
                self.rng.shuffle(e)
                tot += sum(1 for i in range(len(e) - 1) if e[i] == a and e[i + 1] == b)
            null.append(tot)
        k = sum(1 for x in null if x >= obs)
        return {'observed': obs, 'null_mean': sum(null) / n, 'p': k / n, 'p_floor': 1 / n,
                'documents_with_both': len(relevant)}

    # ---- order 2 ------------------------------------------------------------------------------
    def fixed_separation(self, unit, max_gap=6, min_n=4):
        """Units that sit at a constant distance from `unit`. A template leaves this trace."""
        gaps = defaultdict(Counter)
        for d in self.docs:
            idx = [i for i, t in enumerate(d) if t == unit]
            for i in idx:
                for j, t in enumerate(d):
                    g = j - i
                    if 0 < abs(g) <= max_gap:
                        gaps[t][g] += 1
        out = []
        for t, c in gaps.items():
            total = sum(c.values())
            if total < min_n:
                continue
            g, k = c.most_common(1)[0]
            if k >= min_n and k / total >= 0.75:
                out.append({'unit': t, 'gap': g, 'times': k, 'of': total,
                            'concentration': k / total})
        return sorted(out, key=lambda x: (-x['times'], abs(x['gap'])))

    # ---- co-exclusion -------------------------------------------------------------------------
    def coexclusion(self, min_expected=3.0):
        """Pairs that never share a document although they should have, by their frequencies.

        Only pairs whose expected co-occurrence exceeds `min_expected` are reported: below that,
        never meeting is what chance does, and reporting it would be the absence error again.
        """
        present = {t: {i for i, d in enumerate(self.docs) if t in d} for t in self.counts}
        units = [t for t in present if len(present[t]) >= 2]
        out = []
        for i, a in enumerate(units):
            for b in units[i + 1:]:
                na, nb = len(present[a]), len(present[b])
                exp = na * nb / self.N
                if exp < min_expected:
                    continue
                if not (present[a] & present[b]):
                    p = (1 - na / self.N) ** nb
                    out.append({'a': a, 'b': b, 'expected': exp, 'observed': 0, 'p': p})
        return sorted(out, key=lambda x: -x['expected'])

    def power_note(self, min_expected=3.0):
        """How many pairs could show co-exclusion at all. Below this, the measure is blind."""
        present = {t: sum(1 for d in self.docs if t in d) for t in self.counts}
        units = [t for t in present if present[t] >= 2]
        testable = sum(1 for i, a in enumerate(units) for b in units[i + 1:]
                       if present[a] * present[b] / self.N >= min_expected)
        return {'units': len(units), 'testable_pairs': testable,
                'note': 'a corpus where no pair reaches the expected threshold cannot show '
                        'co-exclusion; a null result there measures the corpus, not the language'}
