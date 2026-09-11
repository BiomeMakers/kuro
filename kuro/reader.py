"""The piece that was missing: something that reads.

The bibliographic generator finds passages with a regular expression and hands back the nearest
unit name with 170 characters of context. That is a pointer, not a claim, and running 26 of them
through the cycle gave four "survivors" that were nothing: units concentrated at one site, which
had nothing to do with what the passages said.

What produced a result was reading the 26 by hand and writing each as a proposition. Seven of them
contained one; one was worth something. That is the job this module automates: not finding the
passage, which the regex does, but **reading it** and returning a structured proposition or "none".

The idea came from a news item about ten thousand agents solving a mathematics problem with a
verifier behind them. Linear A has no verifier, but by now it has a judge — a null per claim,
calibrated instruments, confounders by type, a refutation condition — and the judge was the half we
built first. This is the other half, at our scale: not ten thousand agents, but as many readings as
there are passages, each one producing something the judge can try.

    from kuro import Reader
    reader = Reader(model=my_call)          # any callable: prompt -> text
    props = reader.read_all(candidates)     # one Proposition or None per passage
    for p in props: p.to_hypothesis()       # straight into the cycle

The output format is fixed and strict. A reading that cannot fill all four fields — units, kind,
claim, and what would refute it — is discarded, because a proposition without a refutation condition
is not assessable and the cycle will not hold it anyway.
"""
import json, re

KINDS = ('distributional', 'positional', 'arithmetic', 'lexical', 'absence', 'predictive')

PROMPT = """You are reading a passage from the scholarly literature on Linear A, an undeciphered
Bronze Age script. Your job is to decide whether the passage states a claim that can be tested on
the transliterated corpus by counting, and if so, to write that claim in a fixed format.

The corpus records, for 1,719 documents: which sign-groups and logograms they contain, in what
order, with what quantities and fractions, at which site, on what support, and by which scribe.
A testable claim is one about those things: that two units occur together, that one follows
another, that a unit carries fractions or never does, that a quantity equals a sum, that a form
is confined to a site, that an ending alternates with another. A claim about meaning, etymology,
or pronunciation is NOT testable here and must be answered NONE.

Passage:
\"\"\"
{passage}
\"\"\"

Units mentioned in or near the passage (transliterated as in the corpus): {units}

Answer with EXACTLY one of the two forms below and nothing else.

Form 1, when the passage states a testable claim:
UNITS: <one or more corpus units, comma-separated, exactly as transliterated>
KIND: <one of: distributional, positional, arithmetic, lexical, absence, predictive>
CLAIM: <the claim in one sentence, as a statement about the corpus, attributed to the passage>
REFUTED_BY: <one concrete observation in the corpus that would show the claim false>
SOURCE_SAYS: <a quotation of at most 20 words from the passage that states the claim>

Form 2, when it does not:
NONE: <at most ten words on why — e.g. "about meaning", "bibliography only", "about Linear B">
"""


class Proposition(dict):
    """A claim read from a passage, in the four fields the cycle needs."""

    def to_hypothesis(self):
        from .hypothesis import Hypothesis
        return Hypothesis(claim=self['claim'], refuted_by=self['refuted_by'],
                          kind=self['kind'], units=list(self['units']))


class Reader:
    def __init__(self, model, known_units=None):
        """model: callable taking a prompt string and returning the model's text."""
        self.model = model
        self.known = set(known_units or [])
        self.log = []

    @staticmethod
    def parse(text):
        """Turn the model's answer into a Proposition, or None. Strict: all four fields or nothing."""
        t = text.strip()
        if t.upper().startswith('NONE'):
            return None
        fields = {}
        for line in t.splitlines():
            m = re.match(r'^\s*(UNITS|KIND|CLAIM|REFUTED_BY|SOURCE_SAYS)\s*:\s*(.+?)\s*$', line)
            if m:
                fields[m.group(1).lower()] = m.group(2)
        need = ('units', 'kind', 'claim', 'refuted_by')
        if not all(k in fields and fields[k].strip() for k in need):
            return None
        kind = fields['kind'].strip().lower()
        if kind not in KINDS:
            return None
        units = [u.strip() for u in fields['units'].split(',') if u.strip()]
        if not units:
            return None
        if len(fields['refuted_by'].split()) < 4:
            return None                     # "nothing" or "n/a" is not a refutation condition
        return Proposition(units=units, kind=kind, claim=fields['claim'].strip(),
                           refuted_by=fields['refuted_by'].strip(),
                           source_says=fields.get('source_says', '').strip())

    def read(self, passage, units=()):
        """Read one passage. Returns a Proposition or None, and logs why."""
        prompt = PROMPT.format(passage=passage.strip()[:2500], units=', '.join(units) or 'none')
        try:
            answer = self.model(prompt)
        except Exception as e:
            self.log.append({'passage': passage[:60], 'outcome': 'error', 'why': str(e)[:80]})
            return None
        prop = self.parse(answer)
        if prop is None:
            why = answer.strip().split('\n')[0][:80]
            self.log.append({'passage': passage[:60], 'outcome': 'none', 'why': why})
            return None
        # units the corpus does not have are a sign the model invented one
        if self.known:
            unknown = [u for u in prop['units'] if u not in self.known
                       and u.upper() not in self.known]
            if unknown:
                self.log.append({'passage': passage[:60], 'outcome': 'rejected',
                                 'why': f'units not in corpus: {unknown}'})
                return None
        self.log.append({'passage': passage[:60], 'outcome': 'proposition',
                         'why': prop['claim'][:80]})
        return prop

    def read_all(self, candidates):
        """candidates: iterable of dicts with 'claim' (the passage) and 'units'. Returns Propositions."""
        out = []
        for c in candidates:
            p = self.read(c.get('claim', ''), c.get('units', ()))
            if p is not None:
                p['source'] = c.get('source')
                out.append(p)
        return out

    def report(self):
        from collections import Counter
        c = Counter(e['outcome'] for e in self.log)
        lines = [f'{len(self.log)} passages read: ' + ', '.join(f'{k} {v}' for k, v in c.items())]
        for e in self.log:
            if e['outcome'] == 'proposition':
                lines.append(f'  + {e["why"]}')
        return '\n'.join(lines)
