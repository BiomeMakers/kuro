"""What the genre forbids: constraints extracted from what has already been measured.

A receipt admits very little — who gives, who receives, what, how much, sometimes a total — and
that alone rules out most of what a sign-group could be. This module holds the rules already
measured in this project, each with its source and its known exception rate, and applies them as
**eliminations**: never "this is a commodity", always "this cannot be a person".

    from kuro import Constraints
    c = Constraints()
    c.categories('*305', corpus)      # what it can still be, and what each rule ruled out

The rules are only worth what their validation says. `validate()` applies them to the units whose
category is already known and reports recovery and false positives. A rule set that does not
recover what is known is not applied to what is unknown.
"""
import re
from collections import defaultdict

CATEGORIES = ('person_category', 'commodity', 'transaction_term', 'party', 'place')

FRACTIONS = {'¹⁄₂', '¹⁄₃', '²⁄₃', '¹⁄₄', '³⁄₄', '¹⁄₅', '¹⁄₆', '¹⁄₈', '¹⁄₁₆', '³⁄₈'}


class Rule:
    def __init__(self, name, rules_out, test, source, note, exceptions=0):
        self.name, self.rules_out, self.test = name, rules_out, test
        self.source, self.note, self.exceptions = source, note, exceptions

    def __repr__(self):
        return f'<Rule {self.name} rules out {self.rules_out}>'


def _profile(unit, docs):
    """How the unit behaves: attestations, fractions, heading, quantities, sites, companions."""
    p = dict(n=0, frac=0, head=0, whole=0, sites=set(), max_qty=0, with_logogram=0)
    for name, toks, site in docs:
        low = [t.lower() for t in toks]
        u = unit.lower()
        for i, t in enumerate(low):
            if t != u:
                continue
            p['n'] += 1
            p['sites'].add(site)
            if i == 0:
                p['head'] += 1
            j = i + 1
            while j < len(toks) and (re.fullmatch(r'\d+', toks[j]) or toks[j] in FRACTIONS):
                if toks[j] in FRACTIONS:
                    p['frac'] += 1
                else:
                    p['whole'] += 1
                    p['max_qty'] = max(p['max_qty'], int(toks[j]))
                j += 1
            if i + 1 < len(toks) and re.fullmatch(r'[A-Z*][A-Z0-9+*\[\]?]*', toks[i + 1]) \
                    and len(toks[i + 1]) > 1:
                p['with_logogram'] += 1
    return p


RULES = [
    Rule('fraction', 'person_category', lambda p: p['frac'] > 0,
         'Acedo 2026, personnel note',
         'people are not divided; any unit carrying a fraction cannot be a category of persons. '
         'No exception in the corpus.', exceptions=0),
    Rule('large_whole', 'person_category', lambda p: p['max_qty'] > 500,
         'Acedo 2026, personnel figures',
         'personnel figures are not rounded and do not reach the hundreds seen for grain; '
         'a maximum above 500 is a commodity quantity.', exceptions=1),
    Rule('never_quantified', 'commodity', lambda p: p['n'] >= 3 and p['whole'] + p['frac'] == 0,
         'Acedo 2026, JA-SA-SA-RA-ME',
         'a commodity is counted; a unit attested three or more times and never followed by a '
         'figure is not the thing being counted.', exceptions=0),
    # Two rules were written here and removed by validation, which is what validation is for.
    # 'single_site' ruled that a unit attested at one site only cannot be a transaction term.
    # It eliminated KI-RO, which is a transaction term and occurs only at Haghia Triada — as
    # does SA-RA2. Locality distinguishes category signs from general vocabulary, not
    # transaction terms from anything.
    # 'carries_logogram' ruled that a transaction term is not followed by a commodity logogram.
    # It eliminated KU-RO, which is followed by one on mixed-commodity tablets, where the total
    # is stated per commodity.
    # Both are kept here as comments rather than deleted: a rule that failed validation is
    # information, and someone will otherwise write them again.
]


class Constraints:
    def __init__(self, rules=None):
        self.rules = list(rules if rules is not None else RULES)

    def categories(self, unit, docs):
        """What the unit can still be, with the rule that ruled out each of the others."""
        p = _profile(unit, docs)
        out = {c: None for c in CATEGORIES}
        for r in self.rules:
            if r.test(p) and out.get(r.rules_out) is None:
                out[r.rules_out] = f'{r.name} ({r.source})'
        remaining = [c for c, why in out.items() if why is None]
        return {'unit': unit, 'profile': {k: (len(v) if isinstance(v, set) else v)
                                          for k, v in p.items()},
                'remaining': remaining, 'ruled_out': {c: w for c, w in out.items() if w}}

    def as_hypothesis(self, unit, category, docs):
        """The claim that a unit belongs to a category, with the eliminations as its support."""
        from .hypothesis import Hypothesis
        res = self.categories(unit, docs)
        if category not in res['remaining']:
            raise ValueError(f'{unit} cannot be {category}: ruled out by '
                             f'{res["ruled_out"][category]}')
        others = [c for c in res['remaining'] if c != category]
        h = Hypothesis(
            claim=f'{unit} is a {category}',
            refuted_by=('an attestation contradicting one of the rules that eliminated the '
                        'alternatives: ' + '; '.join(res['ruled_out'].values())
                        if res['ruled_out'] else
                        'no rule eliminated any alternative, so nothing would refute this'),
            kind='distributional', units=[unit])
        h.log.append({'step': 'constraints', 'outcome': 'pass' if not others else 'partial',
                      'detail': f'eliminated {len(res["ruled_out"])} categories; '
                                f'{len(res["remaining"])} remain'
                                + (f' ({", ".join(others)} also possible)' if others else '')})
        return h

    def validate(self, known, docs):
        """Apply the rules to units whose category is known. This decides whether they are used.

        `known` maps unit -> true category. Reports recall (the true category survived) and
        false eliminations (the true category was ruled out, which is the serious error).
        """
        kept, wrongly_eliminated, still_ambiguous = 0, [], 0
        for unit, truth in known.items():
            res = self.categories(unit, docs)
            if truth in res['remaining']:
                kept += 1
                if len(res['remaining']) > 1:
                    still_ambiguous += 1
            else:
                wrongly_eliminated.append((unit, truth, res['ruled_out'].get(truth)))
        n = len(known)
        return {'n': n, 'true_category_kept': kept,
                'recall': kept / n if n else 0,
                'wrongly_eliminated': wrongly_eliminated,
                'false_elimination_rate': len(wrongly_eliminated) / n if n else 0,
                'still_ambiguous': still_ambiguous}
