"""What the failures taught, applied to the next hypothesis before it is run.

Six claims have been withdrawn in this project and three notation artefacts were caught in a
single afternoon. Their reasons repeat, and a system that files failures without using them will
repeat them too.

Two dangers are avoided here, and they pull in opposite directions.

**Strangling.** If every failure adds a rule and rules block, the system eventually refuses
everything — not because the hypotheses are bad but because it has accumulated prohibitions.
So a lesson **warns and schedules a check; it never rejects**. A hypothesis that resembles a past
failure is born with the relevant control marked pending. It may run. What it may not do is skip
the control silently.

**Flooding.** Without a brake, a generator produces thousands of claims the corpus cannot decide.
The brake here is not a count, which would be arbitrary, but power: a hypothesis is not run if the
corpus lacks the material to see the effect. That is measured, not guessed.

    from kuro import Lessons
    L = Lessons.from_manifest('manifest.json')
    L.advise(hypothesis)              # warnings, and controls now marked pending
    L.affordable(units, corpus)       # can this corpus decide it at all?
"""
import json, re
from collections import Counter

# Each pattern: how to recognise a claim of this shape, what went wrong before, what to do now.
PATTERNS = [
    {'id': 'wrong_null',
     'matches': lambda h: h.kind in ('distributional', 'lexical'),
     'needs_keyword': True,
     'trigger': ('ascendency', 'compositional', 'window of vitality', 'index', 'ratio'),
     'lesson': 'two claims died because the null did not preserve what the claim was not trying '
               'to explain (row and column sums; syllable transitions)',
     'requires': None,
     'note': 'state what your null preserves and why that is everything except the hypothesis'},
    {'id': 'absence',
     'matches': lambda h: h.kind == 'absence' or re.search(
         r'\b(no|never|absent|lacks|without|none)\b', h.claim, re.I),
     'needs_keyword': False,
     'trigger': (),
     'lesson': 'three claims about an absence measured the instrument, not the object: the '
               'syllable so is not in the transliterated syllabary; the Minoan animal words do '
               'not exist to search with; the MUL sign has a proposed substitute',
     'requires': 'instrument',
     'note': 'what would have to be in the corpus for the instrument to detect what you say '
             'is missing?'},
    {'id': 'haghia_triada_cooccurrence',
     'matches': lambda h: h.kind == 'distributional',
     'needs_keyword': False,
     'trigger': ('co-occur', 'block', 'dossier'),
     'lesson': 'the hypergeometric test is anti-conservative on this corpus: 9.2% false positives '
               'at the 5% threshold, 11.9% for pairs from a single site, because documents are '
               'not exchangeable across sites',
     'requires': 'site',
     'note': 'use a null that preserves site, not the plain hypergeometric'},
    {'id': 'scribe_confound',
     'matches': lambda h: h.kind in ('lexical', 'distributional'),
     'needs_keyword': True,
     'trigger': ('lexicon', 'vocabulary', 'field', 'profile', 'syllable', 'phonolog'),
     'lesson': 'the semantic-field claim died here: field and scribe are almost perfectly '
               'confounded at Haghia Triada, and two scribes of one field differ more from each '
               'other than the two fields do',
     'requires': 'scribe',
     'note': 'shuffle the label within scribe, not across the corpus'},
    {'id': 'notation',
     'matches': lambda h: any(re.search(r'[*\d]', u) for u in h.units),
     'needs_keyword': False,
     'trigger': (),
     'lesson': 'three apparent gaps in one afternoon were notation artefacts: CYP for A*303, a '
               'subscript written flat, sign numbers padded to three digits with a lowercase '
               'form letter',
     'requires': None,
     'note': 'check the unit under every written form before claiming it is untreated',
     'automatic': True},
]


class Lessons:
    def __init__(self, withdrawn=(), patterns=None):
        self.withdrawn = list(withdrawn)
        self.patterns = list(patterns if patterns is not None else PATTERNS)
        self.hits = Counter()

    @classmethod
    def from_manifest(cls, path):
        try:
            with open(path, encoding='utf-8') as f:
                man = json.load(f)
        except FileNotFoundError:
            return cls()
        return cls(man.get('withdrawn', []))

    # ---- advising, never blocking --------------------------------------------------------------
    def advise(self, hypothesis):
        """Warn, and mark the relevant controls pending. Never rejects.

        Returns the advice. The hypothesis is annotated so that its verdict cannot come out as
        `survives` while a scheduled control is unrun — that is enforced by Hypothesis itself,
        which already returns `incomplete` for unchecked confounders.
        """
        advice = []
        text = (hypothesis.claim + ' ' + ' '.join(hypothesis.units)).lower()
        for p in self.patterns:
            if not p['matches'](hypothesis):
                continue
            # A pattern whose `matches` is already specific (a kind of claim) fires on its own.
            # Keywords only narrow the patterns that would otherwise fire on everything.
            if p.get('needs_keyword') and not any(t.lower() in text for t in p['trigger']):
                continue
            self.hits[p['id']] += 1
            item = {'id': p['id'], 'lesson': p['lesson'], 'do': p['note'],
                    'requires': p.get('requires'),
                    'automatic': bool(p.get('automatic'))}
            advice.append(item)
            if p.get('requires') and p['requires'] not in hypothesis.confounders():
                # the control matters for this claim even if its kind does not list it
                hypothesis.log.append(
                    {'step': 'advice', 'outcome': 'note',
                     'detail': f'{p["id"]}: {p["note"]} (control "{p["requires"]}" scheduled)'})
        hypothesis.advice = advice
        return advice

    def required_controls(self, hypothesis):
        """Controls this hypothesis must run because past failures say so."""
        return sorted({a['requires'] for a in getattr(hypothesis, 'advice', [])
                       if a.get('requires')})

    # ---- the brake: power, not a count ---------------------------------------------------------
    def affordable(self, units, docs, test='cooccurrence', min_expected=3.0, min_joint=4):
        """Whether the corpus can decide a claim about these units, for the test being used.

        Not a limit on how many hypotheses may be generated — that would be arbitrary — but on
        which ones the material can settle. A claim about two units of two attestations each is
        not refused because we are tired of hypotheses; it is refused because no outcome of it
        would mean anything.

        The threshold depends on the test, and getting this wrong in either direction is costly.
        A co-occurrence test needs the *expected* joint count to be reasonable, since it asks
        whether the observed exceeds it. An adjacency test asks something else — given that two
        units share documents, do they sit together — so what it needs is enough documents that
        actually contain both. Applying the co-occurrence threshold to adjacency would have
        refused CYP → NI, which is one of the clearest results in this corpus.
        """
        N = len(docs)
        present = {u: sum(1 for d in docs if u in d) for u in units}
        missing = [u for u, n in present.items() if n == 0]
        if missing:
            return {'run': False, 'why': f'not attested: {", ".join(missing)}',
                    'attestations': present}
        if len(units) < 2:
            n = present[units[0]]
            if n < 3:
                return {'run': False, 'attestations': present,
                        'why': f'{units[0]} has {n} attestation(s): no distribution to measure'}
            return {'run': True, 'attestations': present}

        us = list(units)
        joint = min(sum(1 for d in docs if a in d and b in d)
                    for i, a in enumerate(us) for b in us[i + 1:])
        exp = min(present[a] * present[b] / N
                  for i, a in enumerate(us) for b in us[i + 1:])

        if test in ('adjacency', 'separation', 'order'):
            if joint < min_joint:
                return {'run': False, 'attestations': present, 'joint': joint, 'expected': exp,
                        'why': f'only {joint} document(s) contain both: an ordering test needs '
                               f'at least {min_joint} to distinguish order from chance'}
            return {'run': True, 'attestations': present, 'joint': joint, 'expected': exp}

        if test == 'coexclusion':
            if exp < min_expected:
                return {'run': False, 'attestations': present, 'expected': exp,
                        'why': f'expected joint count {exp:.2f} is below {min_expected}: never '
                               f'meeting is what chance does at this frequency'}
            return {'run': True, 'attestations': present, 'expected': exp}

        # default: co-occurrence
        if exp < min_expected:
            return {'run': False, 'attestations': present, 'expected': exp, 'joint': joint,
                    'why': f'expected co-occurrence {exp:.2f} is below {min_expected}: no '
                           f'outcome of this test would be interpretable'}
        return {'run': True, 'attestations': present, 'expected': exp, 'joint': joint}

    def report(self):
        if not self.hits:
            return f'{len(self.withdrawn)} withdrawn claims on file; no lesson triggered yet'
        lines = [f'{len(self.withdrawn)} withdrawn claims on file', '',
                 'lessons triggered so far:']
        for pid, n in self.hits.most_common():
            p = next(x for x in self.patterns if x['id'] == pid)
            lines.append(f'  {pid:<28} {n:>3}x  — {p["note"]}')
        return '\n'.join(lines)
