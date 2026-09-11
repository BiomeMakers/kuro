"""The layer above: a surviving hypothesis is a constraint, not a result.

If it is established that *305 counts persons, that restricts every document where it appears, and
so changes what the other units of those documents can be. The cycle therefore does not end when a
hypothesis is filed: each survival triggers a second pass over the units that share its documents,
now with one constraint more.

That has a failure mode which must be prevented by design rather than by care: if A is used to
restrict B and B is later used to support A, the result is a castle of cards that no reviewer can
unpick. The rule enforced here is simple:

    a hypothesis may use another as a constraint only if that other survived without using it.

Dependencies are recorded, and `check_cycles()` fails if any cycle exists.

    it = Iteration()
    it.add(h_305, uses=[])                  # survived on its own
    it.add(h_ti_a, uses=['*305 counts persons'])
    it.check_cycles()                       # raises if a cycle was built
    it.next_pass(corpus)                    # which units are now further constrained
"""
from collections import defaultdict, deque


class CircularSupport(Exception):
    """Raised when hypotheses support each other in a cycle."""


class Iteration:
    def __init__(self):
        self.nodes = {}          # claim -> hypothesis
        self.uses = defaultdict(set)   # claim -> claims it used as constraints
        self.rounds = []

    def add(self, hypothesis, uses=()):
        """Record a hypothesis and which established claims it leaned on."""
        claim = hypothesis.claim
        for u in uses:
            if u not in self.nodes:
                raise ValueError(f'cannot lean on "{u}": it is not established here')
            if self.nodes[u].verdict() != 'survives':
                raise ValueError(f'cannot lean on "{u}": its verdict is '
                                 f'{self.nodes[u].verdict()}, not survives')
        self.nodes[claim] = hypothesis
        self.uses[claim] = set(uses)
        self.check_cycles()
        return claim

    def check_cycles(self):
        """Fail if any hypothesis supports itself through a chain of others."""
        colour = {}

        def visit(n, path):
            colour[n] = 'grey'
            for m in self.uses.get(n, ()):
                if colour.get(m) == 'grey':
                    raise CircularSupport(
                        'circular support: ' + ' -> '.join(path + [n, m]) +
                        '. A hypothesis may use another as a constraint only if that other '
                        'survived without using it.')
                if colour.get(m) != 'black':
                    visit(m, path + [n])
            colour[n] = 'black'

        for n in list(self.nodes):
            if colour.get(n) != 'black':
                visit(n, [])
        return True

    def established(self):
        return [c for c, h in self.nodes.items() if h.verdict() == 'survives']

    def provenance(self, claim):
        """The full chain a claim rests on, in the order it must be read."""
        out, seen = [], set()
        q = deque([claim])
        while q:
            c = q.popleft()
            if c in seen:
                continue
            seen.add(c)
            for u in self.uses.get(c, ()):
                out.append((c, u))
                q.append(u)
        return out

    def next_pass(self, units_by_document, constraints=None):
        """Which units are newly constrained by what has just been established.

        units_by_document: {document: [units]}. Returns the units that share a document with an
        established claim's units and are therefore worth a second look, with what constrains them.
        """
        touched = defaultdict(set)
        for claim in self.established():
            h = self.nodes[claim]
            for doc, units in units_by_document.items():
                if any(u in units for u in h.units):
                    for u in units:
                        if u not in h.units:
                            touched[u].add(claim)
        self.rounds.append(dict(touched))
        return dict(sorted(touched.items(), key=lambda kv: -len(kv[1])))

    def report(self):
        lines = [f'{len(self.nodes)} hypotheses, {len(self.established())} established', '']
        for c, h in self.nodes.items():
            deps = self.uses.get(c) or set()
            lines.append(f'  [{h.verdict():>17}] {c}')
            if deps:
                lines.append('                      rests on: ' + '; '.join(sorted(deps)))
        if self.rounds:
            lines += ['', f'{len(self.rounds)} iteration rounds; last touched '
                          f'{len(self.rounds[-1])} units']
        return '\n'.join(lines)
