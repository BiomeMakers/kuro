"""Where the hypotheses come from, so that the supply does not depend on one person's afternoon.

Three sources, of decreasing automation and increasing value:

1. **Combinatorial** — from the dictionary: every measurable unit against every category its
   constraints have not eliminated; every pair that shares documents and passes the power check;
   every unit that shares a property with one already established. Thousands, cheaply, and mostly
   dull. The system ranks them by what they would settle.

2. **Bibliographic** — from the reference index: the literature is full of claims stated without
   being measured ("*308 is measured in proportion to OLIV", "the same commodities recur in the
   same order"). Each is a hypothesis already formed by someone who knows the field, waiting for
   a null. Three were run on 9 September 2026 and two produced results.

3. **Transfer** — from other fields with the same structural problem. Not automated here; see
   `kuro.transfer`, which describes the problem's shape so that a method from elsewhere can be
   matched to it. Every instrument in this package came from outside epigraphy.

    from kuro import Generator
    g = Generator(dictionary, corpus_docs)
    g.combinatorial(limit=200)
    g.from_literature(reference)
"""
import json, re
from collections import Counter, defaultdict

# The first run of this generator offered the word divider and the numeral 1 as its best
# candidates. A unit is a sign-group or a logogram; everything else in the token stream is
# punctuation, numerals or fractions, and proposing a claim about them wastes the cycle.
_SIGN_GROUP = re.compile(r'^[A-Za-z][A-Za-z\u2080-\u2089\d\-]*$')
_LOGOGRAM = re.compile(r'^\*?[A-Z0-9][A-Z0-9+*\[\]?]*$')
# A fraction is written with the fraction slash: 1/2 is superscript one, U+2044, subscript two.
# Testing for the subscript alone would reject SA-RA2, whose final sign is the same character.
_FRACTION_SLASH = '\u2044'
_SUPERSCRIPTS = set('\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u2070')


def is_unit(token):
    """True for a sign-group or a logogram; false for dividers, numerals and fractions.

    Written as an allow-list rather than a deny-list, after a deny-list let the divider and the
    numeral 1 through and they came out as the two best candidates of the first run.
    """
    if not isinstance(token, str) or len(token) < 2:
        return False
    if any(ord(ch) > 0xFFFF for ch in token):        # raw Linear A glyphs, not transliteration
        return False
    if _FRACTION_SLASH in token or any(ch in _SUPERSCRIPTS for ch in token):
        return False
    core = token.lstrip('*')
    if not core or core.isdigit() and token == core:  # a bare numeral
        return False
    if '-' in token and _SIGN_GROUP.match(token):     # KU-RO, SA-RA2
        return True
    return bool(_LOGOGRAM.match(token))               # CYP, *305, VIR+KA


class Candidate(dict):
    """A hypothesis not yet built: claim, units, kind, and why it is worth running."""

    @property
    def form(self):
        return self['units'][0] if self.get('units') else None

    def __getitem__(self, k):
        if k == 'form' and 'form' not in self:
            return self.form
        return dict.__getitem__(self, k)

    def __repr__(self):
        return f'<{self["kind"]}: {self["claim"][:60]} (value {self["value"]:.2f})>'


class Generator:
    def __init__(self, dictionary, docs, reference=None, constraints=None, lessons=None,
                 manifest_path='manifest.json'):
        self.manifest_path = manifest_path
        self.dic = dictionary
        self.docs = [[t for t in d if is_unit(t)] for d in docs]
        self.reference = reference
        self.constraints = constraints
        self.lessons = lessons
        self.doc_units = [set(d) for d in self.docs]

    @staticmethod
    def informativeness(n):
        """How much a unit of n attestations can tell us. Peaks in the middle band.

        Frequent units are grammaticalised and occur with everything, so their distribution does
        not discriminate: KU-RO appears in 46 documents and tells us nothing about any of them.
        Rare units have no distribution to measure: 596 units occur once. The band from three to
        about fifteen attestations is the only one with cases enough to measure and specificity
        enough for the measurement to mean something — and it is where every result of this
        project has come from (*305 at twelve, *308 at twelve, KI-RE-TA-NA at four).

        Ranking by raw frequency, which the first version of this generator did, puts exactly the
        useless end on top.
        """
        if n < 3:
            return 0.0
        if n <= 15:
            return 1.0 + (n - 3) / 24.0          # 1.0 at three, 1.5 at fifteen
        return max(0.2, 1.5 * (15.0 / n) ** 0.5)  # decays as attestations grow

    def _untreated_bonus(self, units):
        """A unit no indexed work treats is worth more: it is where a claim can still be new."""
        if self.reference is None:
            return 0.0
        return sum(2.0 for u in units if not self.reference.mentioned(u))

    # ---- 1. combinatorial ----------------------------------------------------------------------
    def from_dictionary(self, limit=200, min_attestations=3):
        """Alias of combinatorial(), named for where the candidates come from."""
        return self.combinatorial(limit=limit, min_attestations=min_attestations)

    def combinatorial(self, limit=200, min_attestations=3):
        """Every claim the dictionary makes possible, ranked by what settling it would buy.

        Value is deliberately simple and stated rather than tuned: a claim about a frequent unit
        with no reading is worth more than one about a rare unit already glossed, and a claim that
        would eliminate several categories at once is worth more than one that eliminates none.
        """
        out = []
        forms = [f for f, e in self.dic.entries.items()
                 if e.get('attestations', 0) >= min_attestations and is_unit(f)]
        freq = {f: self.dic[f].get('attestations', 0) for f in forms}

        # (a) category claims for units with no gloss
        if self.constraints is not None:
            docs3 = [(i, list(d), None) for i, d in enumerate(self.docs)]
            for f in forms:
                e = self.dic[f]
                if e.get('gloss'):
                    continue
                res = self.constraints.categories(f, docs3)
                remaining = res['remaining']
                if 1 <= len(remaining) <= 3:
                    for cat in remaining:
                        out.append(Candidate(
                            kind='category', claim=f'{f} is a {cat}', units=[f],
                            hypothesis_kind='distributional',
                            value=self.informativeness(freq[f]) + (4 - len(remaining)) + self._untreated_bonus([f]),
                            why=f'{len(res["ruled_out"])} categories already eliminated; '
                                f'{len(remaining)} remain'))

        # (a bis) with no constraint set, still ask the open question for each unread unit,
        # so that every form appears in the ranking and can be compared with the others
        if self.constraints is None:
            for f in forms:
                if self.dic[f].get('gloss'):
                    continue
                out.append(Candidate(
                    kind='category', claim=f'what class does {f} belong to',
                    units=[f], hypothesis_kind='distributional',
                    value=self.informativeness(freq[f]) + self._untreated_bonus([f]),
                    why=f'{freq[f]} attestations, no reading proposed'))

        # (b) pair claims for units that share documents
        pairs = Counter()
        for units in self.doc_units:
            us = [u for u in units if u in freq]
            for i, a in enumerate(sorted(us)):
                for b in sorted(us)[i + 1:]:
                    pairs[(a, b)] += 1
        for (a, b), joint in pairs.items():
            if joint < 4:
                continue
            unread = sum(1 for x in (a, b) if not self.dic[x].get('gloss'))
            if not unread:
                continue
            out.append(Candidate(
                kind='adjacency', claim=f'{a} is immediately followed by {b} above chance',
                units=[a, b], hypothesis_kind='positional',
                value=joint / 4 + unread + self._untreated_bonus([a, b])
                      + min(self.informativeness(freq[a]), self.informativeness(freq[b])),
                why=f'{joint} documents contain both; {unread} of the two have no reading'))

        # (c) units sharing a property with something established
        established = [f for f, e in self.dic.entries.items()
                       if e.get('status') in ('established', 'proposed') and e.get('gloss')]
        for f in forms:
            if self.dic[f].get('gloss'):
                continue
            with_est = [e for e in established
                        if any(f in u and e in u for u in self.doc_units)]
            if with_est:
                out.append(Candidate(
                    kind='by_association',
                    claim=f'{f} belongs to the same class as {with_est[0]}',
                    units=[f, with_est[0]], hypothesis_kind='distributional',
                    value=self.informativeness(freq[f]) + len(with_est) + self._untreated_bonus([f]),
                    why=f'shares documents with {len(with_est)} units that have a reading'))

        out.sort(key=lambda c: -c['value'])
        return self._filter_affordable(out)[:limit]

    def _filter_affordable(self, cands):
        if self.lessons is None:
            return cands
        kept = []
        for c in cands:
            test = 'adjacency' if c['kind'] == 'adjacency' else 'cooccurrence'
            if self.lessons.affordable(c['units'], self.docs, test=test)['run']:
                kept.append(c)
        return kept

    # ---- 2. from the literature ------------------------------------------------------------------
    # Claims stated in the reference works without a number attached. The pattern is what
    # gives them away: a proportion, a recurrence, an exclusion, an "always" or a "never".
    # Patterns that give away a claim stated without a number. Widened after the first version
    # found three candidates in a hundred thousand words: the markers were too narrow, and the
    # literature states most of its claims in hedged or descriptive prose rather than in formulas.
    CLAIM_MARKERS = (
        # proportions and quantities
        (r'in proportion to ([\w+*]+)', 'a stated proportion, never quantified'),
        (r'(?:twice|half|double|the same) (?:as|the) (?:many|much|amount|quantity)',
         'a stated quantitative relation'),
        (r'always (?:in|with|followed by|accompanied by|preceded by) ([\w+*\-]+)',
         'a stated invariant'),
        (r'(?:only|exclusively) (?:in|at|with|on) ([\w+*\- ]{3,24})', 'a stated exclusivity'),
        # order and position
        (r'the same \w+ in the same order', 'a stated recurrence of order'),
        (r'(?:always|usually|generally) (?:comes|stands|appears|occurs) (?:first|last|before|after)',
         'a stated positional regularity'),
        (r'(?:heading|heads|at the head of) (?:the |a )?(?:list|tablet|document)',
         'a stated heading position'),
        (r'immediately (?:precedes|follows|before|after)', 'a stated adjacency'),
        # exclusion and co-occurrence
        (r'mutually exclusive', 'a stated exclusion'),
        (r'never (?:occurs|appears|found|attested) (?:with|together|alongside)',
         'a stated exclusion'),
        (r'(?:occurs|appears|found) (?:only )?(?:with|together with|alongside) ([\w+*\-]+)',
         'a stated association'),
        (r'(?:accompanies|accompanied by) ([\w+*\-]+)', 'a stated association'),
        # hedged identifications, which are hypotheses by another name
        (r'(?:seems|appears|is likely|probably|most probably) to (?:be|represent|record|denote|mean)',
         'a hedged identification'),
        (r'(?:may|might|could) (?:be|represent|record|denote|indicate) ',
         'a hedged identification'),
        (r'(?:presumably|perhaps|possibly) (?:a|an|the) ', 'a hedged identification'),
        (r'(?:is|are) (?:probably|possibly|perhaps) ', 'a hedged identification'),
        # morphology
        (r'(?:suffix|prefix|ending) (?:in |-)([\w\u2080-\u2089]+)', 'a stated affix'),
        (r'(?:variant|variants) of ([\w+*\-]+)', 'a stated variation'),
        # classification
        (r'(?:belongs|belong) to (?:the |a )?(?:same |)(?:group|class|series|set)',
         'a stated grouping'),
        (r'(?:the same|one) (?:scribe|hand) (?:wrote|for)', 'a stated attribution'),
    )

    def from_literature(self, reference=None, limit=60):
        """Claims the literature states without measuring. Each is a hypothesis already formed.

        Claims this project has already measured are excluded: see `literature_done()`. Offering
        one again would waste a cycle and, the second time, would look like a new result.
        """
        reference = reference if reference is not None else self.reference
        if reference is None or not len(reference):
            return []
        out = []
        for work, text in reference.works.items():
            flat = re.sub(r'\s+', ' ', text)
            for pattern, why in self.CLAIM_MARKERS:
                for m in re.finditer(pattern, flat, re.I):
                    seg = flat[max(0, m.start() - 160):m.start() + 200]
                    # a sign number needs its asterisk or an AB/A prefix: bare '301' is a page
                    # number ("Weilhartner 2014, 301-2" produced a false *301 on 10 Sep 2026)
                    found = re.findall(
                        r'\*\d{2,3}[a-z]?|(?:AB|A)\s?\d{2,3}[a-z]?|[A-Z][A-Z0-9]+(?:\+[A-Z0-9]+)*|'
                        r'[A-Z]{2,}(?:-[A-Z0-9\u2080-\u2089]+)+', seg)
                    units = []
                    for u in found:
                        u = re.sub(r'^(?:AB|A)\s?', '*', u)
                        for form in (u, u.upper()):
                            if form in self.dic.entries and form not in units:
                                units.append(form)
                                break
                    units = [u for u in units if is_unit(u)][:3]
                    if not units:
                        continue
                    out.append(Candidate(
                        kind='from_literature',
                        claim=seg.strip()[:180],
                        units=units, hypothesis_kind='distributional',
                        value=2 + len(units),
                        why=f'{why}, in {work}',
                        source=work))
        # one candidate per distinct unit set, keeping the fullest quotation
        seen = {}
        measured = self._already_measured_keys()
        def already(claim):
            low = claim.lower()
            if any(k in low for k in ('same order', 'mutually exclusive', 'in proportion to oliv')):
                return True
            words = [w for w in re.findall(r'[\w+*\-\u2080-\u2089]{3,}', low)
                     if w not in ('the', 'and', 'that', 'with', 'from', 'this')]
            key = tuple(sorted(words)[:4])
            return key in measured
        out = [c for c in out if not already(c['claim'])]
        for c in out:
            key = tuple(sorted(c['units']))
            if key not in seen or len(c['claim']) > len(seen[key]['claim']):
                seen[key] = c
        out = sorted(seen.values(), key=lambda c: -c['value'])
        out = [Candidate({**c, 'hypothesis': self._to_hypothesis(c)}) for c in out]
        return self._filter_affordable(out)[:limit]

    def _to_hypothesis(self, c):
        from .hypothesis import Hypothesis
        return Hypothesis(claim=c['claim'],
                          refuted_by=f'an attestation contradicting it: {c["why"]}',
                          kind=c.get('hypothesis_kind', 'distributional'), units=c['units'])

    # Claims from the literature this project has already measured. Offering them again would
    # waste the cycle and, worse, would look like a new result the second time.
    LITERATURE_DONE = [
        {'claim': 'the same commodities recur in the same order below the total',
         'source': 'Younger', 'measured': 'four of four tablets: *303 > figs > wine, additions '
                                          'appended and never interpolated'},
        {'claim': 'TE and SA-RA2 are mutually exclusive in mixed-commodity tablets',
         'source': 'Schoep 2002', 'measured': '58 and 20 documents, 0 overlaps, but 0.67 expected '
                                              'and p = 0.50: correct as description, not as inference'},
        {'claim': '*308 is measured in proportion to OLIV, always in fractions',
         'source': 'Younger', 'measured': 'the proportion is 26-28% across the block'},
        {'claim': 'the last name or commodity cited governs until another is stated',
         'source': 'Younger, continuity principle',
         'measured': '156 of 331 runs have two or more logograms under one word: 47%'},
    ]

    def literature_done(self, dictionary=None, manifest_path=None):
        """What has already been measured here: the hand list, plus everything on record.

        The hand list was the first version and is kept as a seed, but a generator that depends on
        someone remembering to update a list will re-offer a measured claim the moment they forget.
        The dictionary's evidence notes and the manifest's withdrawals are the record, so they are
        read too.
        """
        out = list(self.LITERATURE_DONE)
        dic = dictionary if dictionary is not None else self.dic
        if dic is not None:
            for form, e in dic.entries.items():
                for ev in e.get('evidence', []):
                    if ev.get('source') == 'Acedo':
                        out.append({'claim': ev.get('note', '')[:120], 'source': 'this project',
                                    'measured': f'{ev["kind"]}, {ev["year"]}'})
        if manifest_path:
            try:
                with open(manifest_path, encoding='utf-8') as f:
                    for w in json.load(f).get('withdrawn', []):
                        out.append({'claim': w['claim'], 'source': 'this project',
                                    'measured': 'withdrawn: ' + w['why'][:80]})
            except (FileNotFoundError, KeyError, ValueError):
                pass
        return out

    def _already_measured_keys(self):
        keys = set()
        for d in self.literature_done(manifest_path=self.manifest_path):
            words = [w for w in re.findall(r'[\w+*\-\u2080-\u2089]{3,}', d['claim'].lower())
                     if w not in ('the', 'and', 'that', 'with', 'from', 'this')]
            if len(words) >= 3:
                keys.add(tuple(sorted(words)[:4]))
        return keys

    # ---- 3. transfer from other fields -----------------------------------------------------------
    @staticmethod
    def problem_shape():
        """The shape of this problem, for matching a method from another field to it."""
        from .transfer import SHAPE, CANDIDATE_FIELDS
        return {**SHAPE,
                'fields_with_the_same_shape': [(c['field'], c['status']) for c in CANDIDATE_FIELDS]}

    @staticmethod
    def transplant_checklist(method, field):
        """What to ask before importing a method. Every instrument here came from outside."""
        return {'method': method, 'field': field,
                'rule': 'a transplanted method is calibrated before it is applied: it must '
                        'recover the known answer in a corpus that has one, or it is not used '
                        'on the corpus that has none',
                'questions': [
                    f'does {method} recover the known answer in Etruscan, Proto-Elamite or '
                    f'Iberian, where the answer is known?',
                    f'what does {method} assume about the exchangeability of documents, and does '
                    f'this corpus satisfy it? (the hypergeometric test does not: 9.2% false '
                    f'positives, from the site structure)',
                    f'what is its false-positive rate here, measured and not assumed?',
                    f'what in {field} plays the role of the scribe, and did they control for it?',
                    'what would refute a result obtained with it?']}

    def report(self, cands):
        by = Counter(c['kind'] for c in cands)
        lines = [f'{len(cands)} candidates: ' + ', '.join(f'{k} {v}' for k, v in by.most_common()),
                 '']
        for c in cands[:15]:
            lines.append(f'  [{c["value"]:5.1f}] {c["claim"][:78]}')
            lines.append(f'          {c["why"]}')
        return '\n'.join(lines)
