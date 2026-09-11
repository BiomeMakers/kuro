"""The cycle a claim must survive, as an object.

Three claims were made and killed on 9 September 2026. Each took hours, and each died at a
different step: the first at the bibliography, the second at a confounder, the third at the null
with multiple-comparison correction. The steps were the same every time and were carried out by
hand. This is that cycle as code.

    h = Hypothesis(
        claim='*305 counts persons',
        refuted_by='an attestation of *305 with a fraction, or outside a personnel total',
        kind='distributional',
        units=['*305'])
    h.run(corpus, reference=ref, measure=my_measure, null=my_null)
    print(h.report())

A Hypothesis cannot be built without a refutation condition: that is the protocol's third
requirement made structural rather than advisory.
"""
import json, math, os, re, statistics as st
from datetime import date

KINDS = {
    'distributional': ('scribe', 'site', 'support'),
    'arithmetic': ('edition',),
    'positional': ('scribe', 'genre'),
    'absence': ('instrument',),
    'lexical': ('scribe', 'genre'),
    'predictive': ('baseline', 'leakage'),
}

CONFOUNDER_NOTE = {
    'scribe': 'field and scribe were almost perfectly confounded once before; check that the '
              'effect survives a null that shuffles labels within scribe',
    'site': 'several sign categories proved local to Haghia Triada; check across sites',
    'support': 'the corpus classification by support cuts across classification by content',
    'instrument': 'before interpreting an absence, check the instrument could have seen it: '
                  'the -so claim measured a gap in the transliterated syllabary',
    'edition': 'figures depend on which fraction system the edition applies; declare it',
    'genre': 'the libation formula has syntax the accounts do not; do not mix genres',
    'baseline': 'a predictor must beat always guessing the commonest element, not only a '
                'shuffled null; it is easy to beat the second and lose to the first',
    'leakage': 'whatever was used to align the material cannot also be predicted from it: the '
               'first libation run scored 20.2% and eleven of seventeen hits were the anchor',
}


class Hypothesis:
    """One claim, with everything needed to kill it."""

    def __init__(self, claim, refuted_by, kind, units=(), author='Acedo', year=None):
        if not refuted_by or not str(refuted_by).strip():
            raise ValueError(
                'a hypothesis needs a refutation condition. If you cannot say what observation '
                'would refute it, it is not assessable and this object will not hold it.')
        if kind not in KINDS:
            raise ValueError(f'kind must be one of {sorted(KINDS)}')
        self.claim = claim
        self.refuted_by = refuted_by
        self.kind = kind
        self.units = list(units)
        self.author = author
        self.year = year or date.today().year
        self.log = []
        self.status = 'unrun'
        self.p = None
        self.p_corrected = None

    def _step(self, name, outcome, detail):
        self.log.append({'step': name, 'outcome': outcome, 'detail': detail})
        return outcome

    # ---- step 1: has someone said it already? -------------------------------------------------
    # The first version of this asked whether the *units* were mentioned. Every frequent logogram
    # is catalogued somewhere in Younger, so the gate blocked everything: ten candidates out of ten
    # died here without being measured. What matters is whether the *claim* has been made, which
    # means the units and the predicate together, close enough to be one statement.
    PREDICATES = {
        'positional': ('follow', 'precede', 'adjacent', 'order', 'sequence', 'head', 'initial'),
        'distributional': ('co-occur', 'occurs with', 'associated', 'together with', 'accompan'),
        'arithmetic': ('sum', 'total', 'adds', 'proportion', 'ratio'),
        'lexical': ('suffix', 'prefix', 'ending', 'stem', 'root', 'derivat'),
        'absence': ('never', 'absent', 'no ', 'lacks'),
    }

    def check_literature(self, reference, window=400):
        """Stop only if the claim itself is treated: its units and its predicate, close together.

        A unit being catalogued is not the claim being made. The check reports both, because both
        matter: a catalogued unit means read before writing; a treated claim means do not claim.
        """
        if reference is None or not len(reference):
            return self._step('literature', 'skipped',
                              'no reference works indexed; novelty cannot be assessed')
        catalogued = [u for u in self.units if reference.mentioned(u)]
        preds = self.PREDICATES.get(self.kind, ())
        treated = []
        for name, text in reference.works.items():
            flat = re.sub(r'\s+', ' ', text)
            low = flat.lower()
            for u in self.units:
                for m in re.finditer(re.escape(u.lower()), low):
                    seg = low[max(0, m.start() - window):m.start() + window]
                    others = [v for v in self.units if v != u]
                    if others and not any(v.lower() in seg for v in others):
                        continue
                    if any(p in seg for p in preds):
                        treated.append((name, seg[max(0, window - 60):window + 90].strip()))
                        break
                if treated:
                    break
            if treated:
                break
        if treated:
            self.status = 'published_already'
            return self._step('literature', 'stop',
                              f'the claim appears treated in {treated[0][0]}: "{treated[0][1]}"')
        note = 'the claim is not stated in the indexed works'
        if catalogued:
            note += (f'; the units {", ".join(catalogued)} are catalogued there, so read the '
                     f'entries before writing — being uncatalogued is not what makes a claim new')
        return self._step('literature', 'pass', note)

    # ---- step 2: the null ---------------------------------------------------------------------
    def test(self, measure, null_sampler, n=2000, alternative='greater'):
        """measure() gives the observed value; null_sampler() one draw from the null."""
        obs = measure()
        draws = [null_sampler() for _ in range(n)]
        if alternative == 'greater':
            k = sum(1 for x in draws if x >= obs)
        elif alternative == 'less':
            k = sum(1 for x in draws if x <= obs)
        else:
            k = sum(1 for x in draws if abs(x) >= abs(obs))
        self.p = k / n
        self.p_floor = 1 / n          # no run of n draws can resolve below this
        self.observed, self.null_mean = obs, st.mean(draws) if draws else None
        shown = f'p = {self.p:.4f}' if k else f'p < {self.p_floor:.4g} (0 of {n} draws)'
        return self._step('null', 'pass' if self.p < 0.05 else 'fail',
                          f'observed {obs:.4f}, null mean {self.null_mean:.4f}, {shown}')

    # ---- step 3: the confounders this kind of claim carries -----------------------------------
    def confounders(self):
        return KINDS[self.kind]

    def control(self, name, p_value=None, note=''):
        """Record a confounder control. p_value is from the paired null, when one was run."""
        scheduled = {a.get('requires') for a in getattr(self, 'advice', [])}
        if name not in self.confounders() and name not in scheduled:
            self.log.append({'step': 'control', 'outcome': 'note',
                             'detail': f'{name} is not a standard confounder for a '
                                       f'{self.kind} claim, but was checked: {note}'})
            return 'note'
        if p_value is not None and p_value >= 0.05:
            self.status = 'confounded'
            return self._step(f'control:{name}', 'stop',
                              f'does not survive: paired null gives p = {p_value:.3f}. {note}')
        return self._step(f'control:{name}', 'pass',
                          (f'survives, p = {p_value:.3f}. ' if p_value is not None else '') + note)

    def unchecked_confounders(self):
        """Confounders this claim owes: those of its kind, plus any a past failure scheduled.

        The second part is what makes the system learn. A lesson never rejects a hypothesis — it
        adds a control to the list it must clear, so the claim can still run and still be judged,
        but cannot come out as `survives` while skipping the check that killed its predecessor.
        """
        done = {e['step'].split(':', 1)[1] for e in self.log if e['step'].startswith('control:')}
        owed = set(self.confounders())
        for a in getattr(self, 'advice', []):
            if a.get('requires'):
                owed.add(a['requires'])
        return sorted(owed - done)

    # ---- step 4: multiple comparisons ---------------------------------------------------------
    def correct(self, n_tests, method='auto', family_p=None, alpha=0.05):
        """Correct for the family of tests actually run, and say which method was used.

        Bonferroni controls the chance of any false positive, which is the right thing when a
        handful of tests are run and each will be published on its own. It is punishing when the
        family is large: at two hundred tests the threshold is 0.00025, and a real effect of
        ordinary size never clears it. For large families the literature on hypothesis-generation
        systems uses Benjamini-Hochberg, which controls the proportion of false positives among
        those declared, and needs the whole family's p-values.

        `method='auto'` picks Bonferroni up to twenty tests and Benjamini-Hochberg above, provided
        `family_p` is given; without it, it stays with Bonferroni and says so.
        """
        if self.p is None:
            raise RuntimeError('test() must run before correct()')
        if method == 'auto':
            method = 'bh' if (n_tests > 20 and family_p) else 'bonferroni'

        if method == 'bh':
            ps = sorted(family_p)
            m = len(ps)
            k = max([i + 1 for i, p in enumerate(ps) if p <= alpha * (i + 1) / m], default=0)
            threshold = alpha * k / m if k else 0.0
            ok = k > 0 and self.p <= threshold
            self.p_corrected = min(1.0, self.p * m / max(1, sum(1 for p in ps if p <= self.p)))
            self.correction_method = 'Benjamini-Hochberg'
            return self._step('multiple', 'pass' if ok else 'fail',
                              f'Benjamini-Hochberg over {m} tests at alpha {alpha}: {k} declared, '
                              f'threshold {threshold:.5f}, p = {self.p:.4f} — '
                              f'{"below" if ok else "above"}')

        threshold = alpha / n_tests
        self.p_corrected = min(1.0, self.p * n_tests)
        self.correction_method = 'Bonferroni'
        ok = self.p < threshold
        note = ''
        if n_tests > 20 and not family_p:
            note = ('; Bonferroni used because the family p-values were not supplied — at this '
                    'size Benjamini-Hochberg would be the appropriate choice')
        return self._step('multiple', 'pass' if ok else 'fail',
                          f'Bonferroni over {n_tests} tests, threshold {threshold:.5f}, '
                          f'p = {self.p:.4f} — {"below" if ok else "above"}{note}')

    # ---- step 5: verdict and filing ------------------------------------------------------------
    def verdict(self):
        if self.status in ('published_already', 'confounded'):
            return self.status
        unchecked = self.unchecked_confounders()
        if unchecked:
            self.status = 'incomplete'
            return self.status
        steps = {e['step']: e['outcome'] for e in self.log}
        if steps.get('null') != 'pass':
            self.status = 'not_supported'
        elif steps.get('multiple') == 'fail':
            self.status = 'borderline'
        else:
            self.status = 'survives'
        return self.status

    def to_evidence(self, kind_of_evidence='distribution'):
        """The dictionary entry this hypothesis earns, if it earned one."""
        if self.verdict() != 'survives':
            return None
        floor = getattr(self, 'p_floor', None)
        pstr = (f'p = {self.p:.4f}' if self.p else
                f'p < {floor:.4g}' if floor else 'p = 0')
        cstr = (f', corrected p = {self.p_corrected:.4f}'
                if self.p_corrected is not None and self.p else '')
        return {'kind': kind_of_evidence, 'source': self.author, 'year': self.year,
                'direction': 'for', 'note': f'{self.claim} ({pstr}{cstr})'}

    def to_withdrawal(self):
        """The manifest entry this hypothesis earns, if it failed."""
        if self.verdict() in ('survives', 'unrun'):
            return None
        why = next((e['detail'] for e in reversed(self.log)
                    if e['outcome'] in ('stop', 'fail')), 'no step failed explicitly')
        return {'claim': self.claim, 'why': why,
                'where_stated': f'hypothesis cycle, {date.today().isoformat()}'}

    # ---- step 6: file itself ------------------------------------------------------------------
    def file(self, dictionary=None, manifest_path=None, evidence_kind='distribution',
             error_rate=None, instrument=None):
        """Archive the outcome where it belongs, without being asked twice.

        A surviving hypothesis becomes evidence on each of its units in the dictionary. A failed
        one becomes an entry in the manifest's withdrawn list. Doing this by hand is how a claim
        ends up in a paper after its evidence has been retracted somewhere else.
        """
        v = self.verdict()
        filed = {'verdict': v, 'dictionary': [], 'manifest': None, 'qualified': None}
        if error_rate is not None and self.p is not None:
            filed['qualified'] = error_rate.qualify(instrument or self.kind, self.p)
        if v == 'survives' and dictionary is not None:
            ev = self.to_evidence(evidence_kind)
            if filed['qualified']:
                ev['note'] += f'. {filed["qualified"]}'
            for u in self.units:
                if u in dictionary.entries:
                    dictionary.entries[u].setdefault('evidence', []).append(dict(ev))
                    if not dictionary.entries[u].get('refuted_by'):
                        dictionary.entries[u]['refuted_by'] = self.refuted_by
                    filed['dictionary'].append(u)
        elif v in ('confounded', 'not_supported', 'borderline') and manifest_path:
            w = self.to_withdrawal()
            if os.path.exists(manifest_path):
                with open(manifest_path, encoding='utf-8') as f:
                    man = json.load(f)
                if not any(x['claim'] == w['claim'] for x in man.get('withdrawn', [])):
                    man.setdefault('withdrawn', []).append(w)
                    with open(manifest_path, 'w', encoding='utf-8') as f:
                        json.dump(man, f, ensure_ascii=False, indent=2)
                filed['manifest'] = w['claim']
        self.filed = filed
        return filed

    def report(self):
        out = [f'CLAIM   : {self.claim}',
               f'kind    : {self.kind}   units: {", ".join(self.units) or "-"}',
               f'refuted by: {self.refuted_by}', '']
        for e in self.log:
            out.append(f'  [{e["outcome"]:>7}] {e["step"]:<18} {e["detail"]}')
        unchecked = self.unchecked_confounders()
        if unchecked:
            out.append('')
            for c in unchecked:
                out.append(f'  [UNCHECKED] {c:<18} {CONFOUNDER_NOTE.get(c, "")}')
        out += ['', f'VERDICT : {self.verdict()}']
        f = getattr(self, 'filed', None)
        if f:
            if f['dictionary']:
                out.append(f'filed as evidence on: {", ".join(f["dictionary"])}')
            if f['manifest']:
                out.append('filed as a withdrawal in the manifest')
            if f['qualified']:
                out.append(f'qualified : {f["qualified"]}')
        return '\n'.join(out)
