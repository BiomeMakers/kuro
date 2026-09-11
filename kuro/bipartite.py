"""A null that preserves what makes documents non-exchangeable.

The hypergeometric test asks whether two units share more documents than chance, and it assumes
documents are interchangeable. They are not: measured on this corpus it reports a false positive
in 8.0% of trials at the 5% threshold, and still 1.5% at 0.0001, because a document belongs to a
site, a scribe and a genre, and units of one site meet each other more than the test expects.

The fix is not to correct afterwards but to draw the null from the right space. A document-unit
corpus is a bipartite graph: documents on one side, units on the other. The configuration model
draws random graphs **preserving both degree sequences** — how many documents each unit appears
in, and how many units each document holds — so everything the corpus fixes stays fixed and only
the pairing is random.

    from kuro import BipartiteNull
    nb = BipartiteNull(docs)
    nb.cooccurrence('CYP', 'NI')            # p under the configuration model
    nb.calibrate(trials=400)                # its false-positive rate on this corpus

Curveball is used for the shuffling: it swaps 2x2 checkerboards, which is the standard way to
sample the configuration model without bias toward any particular graph.
"""
import random
from collections import Counter


class BipartiteNull:
    def __init__(self, docs, seed=0, burn_in=None, strata=None):
        """docs: a list of documents, each a collection of units (repeats ignored).

        `strata`: an optional label per document (site, scribe, genre). When given, documents are
        only ever swapped with others of the same stratum, so the null preserves the structure that
        makes documents non-exchangeable. Without it the configuration model preserves the degree
        sequences and nothing else — and on this corpus that turned out to change nothing: the
        plain bipartite null gives the same 8.0% as the hypergeometric, because degrees were never
        the cause. Site was.
        """
        keep = [i for i, d in enumerate(docs) if d]
        self.docs = [sorted(set(docs[i])) for i in keep]
        self.strata = [strata[i] for i in keep] if strata is not None else None
        self.units = sorted({u for d in self.docs for u in d})
        self.index = {u: i for i, u in enumerate(self.units)}
        self.rng = random.Random(seed)
        # rows are documents, held as sets of unit indices
        self.rows = [set(self.index[u] for u in d) for d in self.docs]
        self.edges = sum(len(r) for r in self.rows)
        self.burn_in = burn_in if burn_in is not None else max(1000, 5 * self.edges)

    # ---- degree sequences, which the null must preserve -----------------------------------------
    def degrees(self):
        unit_deg = Counter()
        for r in self.rows:
            for i in r:
                unit_deg[i] += 1
        return {'documents': [len(r) for r in self.rows],
                'units': [unit_deg[i] for i in range(len(self.units))]}

    # ---- curveball -------------------------------------------------------------------------------
    def _partners(self, n):
        """Which documents may be swapped with which. Without strata, any two."""
        if self.strata is None:
            return None
        groups = {}
        for i, s in enumerate(self.strata):
            groups.setdefault(s, []).append(i)
        return [g for g in groups.values() if len(g) > 1]

    def _shuffle(self, rows, swaps):
        """Curveball: repeatedly trade the non-shared items of two documents.

        Each trade keeps both document sizes and every unit's total count, so the swapped graph
        has exactly the degree sequences of the original.
        """
        n = len(rows)
        if n < 2:
            return rows
        groups = self._partners(n)
        for _ in range(swaps):
            if groups:
                g = self.rng.choice(groups)
                a, b = self.rng.choice(g), self.rng.choice(g)
            else:
                a, b = self.rng.randrange(n), self.rng.randrange(n)
            if a == b:
                continue
            ra, rb = rows[a], rows[b]
            only_a = list(ra - rb)
            only_b = list(rb - ra)
            if not only_a or not only_b:
                continue
            pool = only_a + only_b
            self.rng.shuffle(pool)
            new_a, new_b = pool[:len(only_a)], pool[len(only_a):]
            rows[a] = (ra & rb) | set(new_a)
            rows[b] = (ra & rb) | set(new_b)
        return rows

    def sample(self, swaps=None):
        rows = [set(r) for r in self.rows]
        return self._shuffle(rows, swaps if swaps is not None else self.burn_in)

    # ---- the test --------------------------------------------------------------------------------
    def cooccurrence(self, a, b, n=1000, swaps_between=None):
        """How often a and b share a document, against the configuration model."""
        if a not in self.index or b not in self.index:
            return {'observed': 0, 'p': 1.0, 'note': 'one of the units is not attested'}
        ia, ib = self.index[a], self.index[b]
        obs = sum(1 for r in self.rows if ia in r and ib in r)
        rows = [set(r) for r in self.rows]
        self._shuffle(rows, self.burn_in)
        between = swaps_between if swaps_between is not None else max(100, self.edges // 4)
        null = []
        for _ in range(n):
            self._shuffle(rows, between)
            null.append(sum(1 for r in rows if ia in r and ib in r))
        k = sum(1 for x in null if x >= obs)
        return {'observed': obs, 'null_mean': sum(null) / n, 'p': k / n, 'p_floor': 1 / n,
                'preserves': ('document sizes and unit totals'
                              + (', within stratum' if self.strata is not None else ''))}

    def calibrate(self, trials=300, alpha=0.05, min_docs=3, max_docs=40, n=300):
        """The false-positive rate of this null on this corpus, for comparison with the old one.

        Pairs are drawn at random, where by construction there is nothing to find beyond what the
        degree sequences already imply. A null worth having should return close to alpha.
        """
        unit_deg = Counter()
        for r in self.rows:
            for i in r:
                unit_deg[i] += 1
        cands = [i for i, d in unit_deg.items() if min_docs <= d <= max_docs]
        if len(cands) < 4:
            return {'note': 'not enough units in the band to calibrate'}
        hits, ps = 0, []
        for _ in range(trials):
            ia, ib = self.rng.sample(cands, 2)
            r = self.cooccurrence(self.units[ia], self.units[ib], n=n)
            ps.append(r['p'])
            if r['p'] < alpha:
                hits += 1
        return {'trials': trials, 'alpha': alpha, 'false_positives': hits,
                'rate': hits / trials,
                'curve': {str(t): sum(1 for p in ps if p < t) / len(ps)
                          for t in (0.05, 0.01, 0.001)}}
