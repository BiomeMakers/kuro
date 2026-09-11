"""Minimal tests on synthetic data where the answer is known."""
import random, numpy as np, pytest
from kuro import Document, shuffle_within_strata, curveball, shuffle_syllables
from kuro import profile_distance, affix_pairs, metacommunity, monopolies, confounder_jaccard, totals_check, hapax_by_length, form_screen

def docs_two_registers(n=40, seed=0):
    rng = random.Random(seed)
    A = [Document(id=f'A{i}', site='X', support='Tablet',
                  tokens=['-'.join(rng.choice(['ka','ro','ti']) for _ in range(3)) for _ in range(6)]) for i in range(n)]
    B = [Document(id=f'B{i}', site='Y', support='Tablet',
                  tokens=['-'.join(rng.choice(['pu','we','no']) for _ in range(3)) for _ in range(6)]) for i in range(n)]
    return A, B

def test_profile_distance_separates_and_floor_is_small():
    A, B = docs_two_registers()
    r = profile_distance(A, B, size=100, n_null=50)
    assert r['observed'] > r['floor'] and r['p'] < 0.05
    r2 = profile_distance(A, A[:20] + A[20:], size=100, n_null=50)
    assert r2['observed'] < 0.05

def test_affix_pairs_finds_planted_prefix():
    vocab = ['ka-'+w for w in ['ro-ti','pu-we','no-ma','ti-ka','we-ro']] + ['ro-ti','pu-we','no-ma','ti-ka','we-ro'] + \
            ['-'.join(random.Random(i).choice(['za','mi','du','se']) for _ in range(2)) for i in range(60)]
    r = affix_pairs(sorted(set(vocab)), 'ka', 'prefix', n_null=100)
    assert r['observed'] >= 5 and r['p'] < 0.05

def test_curveball_preserves_margins():
    rng = np.random.default_rng(0); M = (rng.random((30, 12)) < 0.3).astype(np.int8)
    B = curveball(M, iters=500, rng=random.Random(1))
    assert (B.sum(1) == M.sum(1)).all() and (B.sum(0) == M.sum(0)).all()

def test_shuffle_syllables_preserves_lengths():
    words = ['a-b-c', 'd-e', 'f-g-h-i']
    out = shuffle_syllables(words, random.Random(0))
    assert [w.count('-') for w in out] == [w.count('-') for w in words]

def test_shuffle_within_strata_keeps_stratum_composition():
    labels = {i: ('x' if i < 5 else 'y') for i in range(10)}
    strata = {i: ('s1' if i % 2 == 0 else 's2') for i in range(10)}
    out = shuffle_within_strata(labels, strata, random.Random(0))
    for s in ('s1', 's2'):
        ks = [k for k in labels if strata[k] == s]
        assert sorted(out[k] for k in ks) == sorted(labels[k] for k in ks)

def test_metacommunity_finds_planted_coexclusion():
    docs = []
    for i in range(60):
        block = ['aa-aa', 'bb-bb', 'cc-cc'] if i % 2 == 0 else ['dd-dd', 'ee-ee', 'ff-ff']
        docs.append(Document(id=str(i), tokens=block))
    r = metacommunity(docs, min_docs=5, n_null=40)
    assert r['coexclusion'], 'planted mutually exclusive blocks should be detected'

def test_monopolies_are_exclusive():
    docs = [Document(id=str(i), support='Tablet', tokens=['only-here'] if i < 5 else ['other-word']) for i in range(20)]
    m = monopolies(docs, lambda d: 'A' if int(d.id) < 5 else 'B', min_count=4)
    assert 'only-here' in m['A'] and 'other-word' in m['B']

def test_confounder_detects_the_true_factor():
    rng = random.Random(0); docs = []
    for h in range(4):
        for k in range(8):
            # vocabulary depends on the hand; the support label is orthogonal noise
            words = [f'w{h}-{j}' for j in rng.sample(range(8), 4)]
            docs.append(Document(id=f'{h}-{k}', hand=f'H{h}', support='T' if k % 2 else 'U', tokens=words))
    r = confounder_jaccard(docs, lambda d: d.hand, lambda d: d.support, n_null=60)
    same_hand = r['cells'][(True, True)] + r['cells'][(True, False)]
    diff_hand = r['cells'][(False, True)] + r['cells'][(False, False)]
    assert same_hand > diff_hand and r['effect_a_within_b'][1] < 0.05

def test_totals_check_adds_up():
    d = Document(id='t', tokens=['a-b', '2', 'c-d', '3', 'ku-ro', '5'])
    out = totals_check(d)
    assert out and out[0]['exact']

def test_hapax_by_length_separates_repeated_from_unique():
    docs = [Document(id=str(i), tokens=['a-b'] * 3 + [f'x{i}-y{i}-z{i}']) for i in range(20)]
    h = hapax_by_length(docs)
    assert h[2][0] == 0.0 and h[3][0] == 1.0  # 'a-b' repeated, 'x-y-z' unique

def test_form_screen_null_is_reasonable():
    vocab = ['ku-pa-ro', 'ka-na-ko'] + ['-'.join(random.Random(i).choice(['ti','mo','ra']) for _ in range(3)) for i in range(50)]
    match = lambda w, p: w.split('-')[:2] == p.split('-')[:2]
    r = form_screen(sorted(set(vocab)), ['ku-pa-ro', 'ka-na-ko'], match, n_null=50)
    assert r['observed'] >= 2 and r['null_mean'] < r['observed']


# ---- reports ----
from kuro import Corpus

def _toy_corpus():
    docs = [
        Document(id='T1', site='X', support='Tablet',
                 tokens=['a-b', 'GRA', '2', 'c-d', 'GRA', '3', 'ku-ro', '5']),
        Document(id='T2', site='X', support='Tablet',
                 tokens=['e-f', 'CYP', '1', 'OLE', '2']),
        Document(id='T3', site='Y', support='Stone vessel',
                 tokens=['a-ta-i-*301-wa-ja', 'ja-sa-sa-ra-me']),
        Document(id='T4', site='Y', support='Nodule', tokens=['CYP']),
    ]
    return Corpus(docs)

def test_classify_by_content_not_support():
    c = _toy_corpus()
    assert c.classify(c.docs['T1']) == 'accounting'
    assert c.classify(c.docs['T3']) == 'votive'      # stone vessel, but votive by content
    assert c.classify(c.docs['T4']) == 'label'

def test_arithmetic_finds_an_exact_total():
    c = _toy_corpus()
    out = c.arithmetic_check('T1')
    assert 'EXACT' in out

def test_tablet_report_separates_known_from_unknown():
    c = _toy_corpus()
    rep = c.tablet_report('T2')
    assert 'established reading: cyperus' in rep
    assert 'no established reading' in rep or 'sign-group' in rep

def test_sign_profile_reports_company_and_classes():
    c = _toy_corpus()
    prof = c.sign_profile('CYP')
    assert 'document(s)' in prof and 'ASSOCIATION WITH COMMODITY CLASSES' in prof

def test_missing_document_is_reported_not_raised():
    c = _toy_corpus()
    assert 'not in corpus' in c.tablet_report('NOPE')

def test_verify_flags_a_split_word():
    docs = [
        Document(id='V1', tokens=['ja-sa', '|', 'sa-ra-me']),
        Document(id='V2', tokens=['ja-sa-sa-ra-me', 'GRA', '1']),
        Document(id='V3', tokens=['ja-sa-sa-ra-me', 'VIN', '2']),
    ]
    out = Corpus(docs).verify('V1')
    assert 'straddle a line break' in out

def test_verify_is_quiet_when_there_is_nothing_to_flag():
    c = _toy_corpus()
    out = c.verify('T2', as_lines=True)
    body = [l for l in out[1:] if 'sigla' not in l]
    assert body == []


def test_evidence_tags_travel_with_the_number():
    from kuro import computed, cited, illustrative
    assert '[C]' in str(computed(0.8))
    assert '[L]' in str(cited(0.71, 'Dioscorides I.56')) and 'Dioscorides' in str(cited(0.71, 'Dioscorides I.56'))
    assert '[~]' in str(illustrative(20, 'olive oil yield'))

def test_capture_control_warns_when_groups_differ_in_length():
    docs = [Document(id=f'A{i}', site='Long', support='Tablet',
                     tokens=['w{}-x'.format(j) for j in range(20)]) for i in range(6)]
    docs += [Document(id=f'B{i}', site='Short', support='Tablet', tokens=['y-z']) for i in range(6)]
    out = Corpus(docs).capture_control('site')
    assert 'WARNING' in out

def test_capture_control_is_quiet_when_groups_are_comparable():
    docs = [Document(id=f'A{i}', site='One', support='Tablet', tokens=['a-b', 'c-d', 'e-f']) for i in range(6)]
    docs += [Document(id=f'B{i}', site='Two', support='Tablet', tokens=['g-h', 'i-j', 'k-l']) for i in range(6)]
    out = Corpus(docs).capture_control('site')
    assert 'WARNING' not in out and 'not explained by capture conditions' in out


# ---- provenance, power and capture control ----
from kuro import Fact, power_report, capture_artifact

def test_fact_marks_its_tier():
    assert '[C]' in str(Fact.computed(1.0, 'x'))
    assert '[L]' in str(Fact.cited(1.0, 'x', 'Someone 2020'))
    assert '[~]' in str(Fact.illustrative(1.0, 'x'))

def test_power_report_says_what_is_out_of_reach():
    out = power_report(n_documents=224, n_tokens=2481)
    assert 'co-exclusion' in out and 'needs about 800' in out
    out2 = power_report(n_documents=34000, n_tokens=500000)
    assert 'yes, above the threshold' in out2

def test_capture_artifact_detects_a_planted_artefact():
    docs = [Document(id=str(i), tokens=['a-b'] * (i % 7 + 1)) for i in range(40)]
    # the "signal" is exactly the capture variable: it must be flagged
    r = capture_artifact(docs, lambda d: len(d.words()), lambda d: len(d.tokens), n_null=100)
    assert r['r'] > 0.9 and 'control it' in r['verdict']

def test_capture_artifact_is_quiet_when_unrelated():
    import random as _r
    rng = _r.Random(0)
    docs = [Document(id=str(i), tokens=['a-b'] * (i % 5 + 1)) for i in range(40)]
    r = capture_artifact(docs, lambda d: len(d.words()), lambda d: rng.random(), n_null=200)
    assert abs(r['r']) < 0.5

from kuro import group_cohesion, factor_effects

def test_group_cohesion_finds_a_real_grouping():
    # four groups of three: enough permutations for p to reach below 0.05
    feats, labels = {}, {}
    for g, tag in enumerate('ABCD'):
        for k in range(3):
            i = g * 3 + k
            feats[i] = {tag + '1', tag + '2'}
            labels[i] = tag
    r = group_cohesion(feats, labels, feats, n_null=500)
    assert r['within'] > r['between'] and r['p'] < 0.05

def test_group_cohesion_rejects_a_fake_grouping():
    feats = {i:{chr(97+i)} for i in range(8)}
    labels = {i:('A' if i%2 else 'B') for i in range(8)}
    r = group_cohesion(feats, labels, feats, n_null=200)
    assert r['p'] > 0.05

def test_factor_effects_separates_a_real_from_a_redundant_factor():
    feats = {1:{'a','b'},2:{'a','b'},3:{'c','d'},4:{'c','d'}}
    real = {1:'X',2:'X',3:'Y',4:'Y'}          # tracks the features
    noise = {1:'p',2:'q',3:'p',4:'q'}          # does not
    r = factor_effects(feats, {'real':real,'noise':noise}, feats)
    top = r['cells'][0]
    assert top['real'] is True

def test_biblio_database_is_valid_and_linked():
    import json, os
    base = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'biblio')
    works = {w['id']: w for w in json.load(open(os.path.join(base, 'works.json')))}
    claims = json.load(open(os.path.join(base, 'claims.json')))
    for c in claims:
        assert c['status'] in {'CHECKED','PARTIAL','UNCHECKED','PRIOR ART','CONFLICT'}, c['id']
        for k in c['works']:
            assert k in works, f"{c['id']} points at unknown work {k}"

def test_manifest_is_valid_and_consistent():
    import json, os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    m = json.load(open(os.path.join(root, 'manifest.json'), encoding='utf-8'))
    for section in ('corpora', 'key_results', 'p_values', 'withdrawn', 'prior_art', 'disputed'):
        assert section in m, f'manifest lacks {section}'
    for k, v in m['p_values'].items():
        assert 0 <= v <= 1, f'{k} is not a probability: {v}'
    for w in m['withdrawn']:
        for field in ('claim', 'why', 'where_stated'):
            assert w.get(field), f'withdrawn entry lacks {field}'
    # a figure recorded twice under different names is the error the manifest exists to catch
    ks = m['key_results']
    assert ks['toponym_matches_cretan'] > ks['toponym_matches_non_cretan']
    assert ks['ht100_surviving_sum'] < ks['ht100_recorded_total']

def test_manifest_checker_runs():
    import subprocess, sys, os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    r = subprocess.run([sys.executable, os.path.join(root, 'scripts', 'check_manifest.py')],
                       capture_output=True, text=True)
    assert r.returncode == 0
    assert 'MANIFEST CHECK' in r.stdout

def test_language_versions_cite_the_same_authors():
    """A citation added to one language version and not the other is the error this catches."""
    import glob, os
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src = os.path.join(root, 'docs', 'papers', 'sources')
    if not os.path.isdir(src):
        return
    files = {os.path.basename(p): open(p, encoding='utf-8', errors='replace').read()
             for p in glob.glob(os.path.join(src, '*.md'))}
    authors = ['Montecchi', 'Younger', 'Uchitel', 'Davis', 'Finkelberg', 'Schoep', 'Chadwick',
               'Ferrara', 'Briakos', 'Escobar', 'Song', 'Ebeling', 'Koh', 'Hogan', 'Palmer',
               'Jiménez', 'Valério', 'Sarpaki', 'Soles', 'Corazza', 'Duhoux', 'Steele', 'Salgarella']
    mismatches = []
    for es in [n for n in files if n.endswith('_ES.md')]:
        en = es.replace('_ES.md', '_EN.md')
        if en not in files:
            continue
        a = {x for x in authors if x.lower() in files[es].lower()}
        b = {x for x in authors if x.lower() in files[en].lower()}
        if a ^ b:
            mismatches.append(f'{es}: {sorted(a ^ b)}')
    assert not mismatches, 'citations differ between language versions: ' + '; '.join(mismatches)

def test_reference_lookup_is_honest_when_empty():
    """With no reference texts, the lookup says so instead of implying the word is new."""
    from kuro import Reference
    r = Reference('/nonexistent/path')
    assert len(r) == 0
    out = r.lookup('KU-NI-SU')
    assert 'No reference texts' in out

def test_reference_finds_and_reports_absence():
    """A word present is reported with its passages; a word absent is not called new."""
    import os, tempfile
    from kuro import Reference
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'testwork_1999.txt'), 'w', encoding='utf-8') as f:
            f.write('KU-NI-SU first name in a list HT 86a.1-2 and again at HT 95a.3-4\n')
        r = Reference(d)
        assert len(r) == 1
        assert r.mentioned('KU-NI-SU')
        assert 'first name in a list' in r.lookup('KU-NI-SU')
        assert not r.mentioned('ZZ-ZZ-ZZ')
        out = r.lookup('ZZ-ZZ-ZZ')
        assert 'not proof of novelty' in out
        u = r.unread(['KU-NI-SU', 'ZZ-ZZ-ZZ'])
        assert u['mentioned'] == ['KU-NI-SU'] and u['not_mentioned'] == ['ZZ-ZZ-ZZ']

def test_dictionary_evidence_is_typed_signed_and_dated():
    from kuro import Dictionary
    d = Dictionary.load('data/derived/dictionary.json')
    from kuro.dictionary import KINDS, DIRECTIONS, STATUS
    for form, e in d.entries.items():
        assert e.get('status') in STATUS, f'{form}: bad status'
        for ev in e.get('evidence', []):
            for field in ('kind', 'source', 'year', 'direction', 'note'):
                assert ev.get(field), f'{form}: evidence lacks {field}'
            assert ev['kind'] in KINDS, f'{form}: unknown evidence kind {ev["kind"]}'
            assert ev['direction'] in DIRECTIONS
            assert 1900 < int(ev['year']) < 2100

def test_dictionary_flags_unassessable_claims():
    """A proposed reading with no refutation condition must be reported, not passed over."""
    from kuro import Dictionary
    d = Dictionary.load('data/derived/dictionary.json')
    assert d.unassessable() == [], (
        'these have a reading and no refutation condition: ' + ', '.join(d.unassessable()))

def test_dictionary_does_not_count_supports_as_confidence():
    """Contested entries are reported as contested, whatever their number of supports."""
    from kuro import Dictionary
    d = Dictionary.load('data/derived/dictionary.json')
    for form in d.contested():
        e = d[form]
        assert e.evidence_for and e.evidence_against
        assert 'AGAINST' in e.summary()

def test_reference_matches_notation_variants():
    """The same sign is written several ways; a lookup that misses them reports a false gap.

    This test exists because the first screening reported sixteen untouched units and eight of
    them were notation artefacts: CYP for A*303, subscript three written flat, the plus of a
    ligature.
    """
    import os, tempfile
    from kuro import Reference
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'w_2024.txt'), 'w', encoding='utf-8') as f:
            f.write('*303+D occurs at KH 7b. KU-PA3-NU is an anthroponym. *304 heads the list.\n')
        r = Reference(d)
        assert r.mentioned('CYP+D'), 'CYP not matched to *303'
        assert r.mentioned('KU-PA\u2083-NU'), 'subscript three not matched to flat 3'
        assert r.mentioned('AROM'), 'AROM not matched to *304'
        assert not r.mentioned('MA-RU-ME')

def test_reference_matches_padded_sign_numbers():
    """Editions pad sign numbers to three digits and lowercase the form letter: *22F is *022f.

    Added after this cost a false candidate: *22F looked untouched with fourteen attestations
    and was catalogued all along.
    """
    import os, tempfile
    from kuro import Reference
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'w_2024.txt'), 'w', encoding='utf-8') as f:
            f.write('ZU-*022f-DI name in a list HT 101.1; the E series includes *021f\n')
        r = Reference(d)
        assert r.mentioned('*22F'), 'zero-padded three-digit form not matched'
        assert r.mentioned('*21F')
        assert not r.mentioned('*21M')

# ---- the hypothesis cycle -------------------------------------------------------------------

def test_hypothesis_requires_a_refutation_condition():
    """The protocol's third requirement, made structural: no refutation, no object."""
    import pytest
    from kuro import Hypothesis
    with pytest.raises(ValueError):
        Hypothesis('something is true', '', 'distributional')
    with pytest.raises(ValueError):
        Hypothesis('something is true', None, 'distributional')

def test_hypothesis_stops_when_the_claim_is_treated_not_when_the_unit_is_listed():
    """A catalogued unit is not a made claim. Blocking on the first strangles the cycle."""
    from kuro import Hypothesis, Reference
    import os, tempfile
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'w_2024.txt'), 'w', encoding='utf-8') as f:
            f.write('KU-NI-SU is attested at HT 86a. Its stem KU-NI shows a suffix in -SU '
                    'that recurs in the same list.\n')
        # the claim is about the suffix, which the work does discuss near the unit
        h = Hypothesis('KU-NI-SU carries a suffix', 'no such suffix elsewhere', 'lexical',
                       units=['KU-NI-SU'])
        h.check_literature(Reference(d))
        assert h.verdict() == 'published_already', 'a treated claim was let through'
        # a different claim about the same catalogued unit is not blocked
        h2 = Hypothesis('KU-NI-SU co-occurs with wine above chance',
                        'the association vanishing under a site null', 'distributional',
                        units=['KU-NI-SU'])
        h2.check_literature(Reference(d))
        assert h2.status != 'published_already', (
            'blocked a claim merely because its unit is catalogued')
        assert 'catalogued' in h2.log[-1]['detail']

def test_hypothesis_reports_unchecked_confounders():
    """A claim with confounders left unchecked is incomplete, not supported."""
    from kuro import Hypothesis
    h = Hypothesis('x correlates with y', 'no correlation in a larger corpus', 'distributional')
    h.test(lambda: 1.0, lambda: 0.0, n=10)
    assert h.verdict() == 'incomplete'
    assert 'scribe' in h.unchecked_confounders()
    assert 'UNCHECKED' in h.report()

def test_hypothesis_confounded_claim_yields_a_withdrawal():
    from kuro import Hypothesis
    h = Hypothesis('the fields differ phonologically', 'the difference vanishing within a scribe',
                   'lexical')
    h.test(lambda: 1.0, lambda: 0.0, n=10)
    h.control('scribe', p_value=0.117, note='paired null')
    assert h.verdict() == 'confounded'
    w = h.to_withdrawal()
    assert w and 'why' in w and h.to_evidence() is None

def test_constraints_recover_the_known_categories():
    """The rule set is only applied to the unknown if it recovers the known. Phase 2's control."""
    import json, os, pytest
    from kuro import Constraints
    if not os.path.exists('data/raw/inscriptions.json'):
        pytest.skip('Linear A corpus not present (data/fetch.py lineara)')
    d = json.load(open('data/raw/inscriptions.json'))
    docs = [(n, [w for w in it.get('transliteratedWords', []) if isinstance(w, str) and w != '\n'],
             it.get('site')) for n, it in d]
    known = {'KU-RO': 'transaction_term', 'PO-TO-KU-RO': 'transaction_term',
             'KI-RO': 'transaction_term', 'GRA': 'commodity', 'NI': 'commodity',
             'VIN': 'commodity', 'OLIV': 'commodity', 'CYP': 'commodity',
             'VIR+KA': 'person_category', '*305': 'person_category', '*327': 'person_category',
             'TI+A': 'person_category', 'JA-SA-SA-RA-ME': 'party'}
    v = Constraints().validate(known, docs)
    assert v['false_elimination_rate'] == 0, (
        'the rules eliminate a category known to be right: ' + str(v['wrongly_eliminated']))
    assert v['recall'] == 1.0

def test_orders_report_their_own_blindness():
    """A co-exclusion measure on a corpus with no testable pair measures the corpus, not the text."""
    from kuro import Orders
    o = Orders([['A', 'B'], ['C', 'D']])
    note = o.power_note(min_expected=3.0)
    assert note['testable_pairs'] == 0
    assert 'measures the corpus' in note['note']
    assert o.coexclusion(min_expected=3.0) == []

def test_iteration_forbids_circular_support():
    """A may constrain B only if A survived without B. Phase 5's guard."""
    import pytest
    from kuro import Hypothesis, Iteration, CircularSupport
    passing = [{'step': 'null', 'outcome': 'pass', 'detail': ''},
               {'step': 'multiple', 'outcome': 'pass', 'detail': ''},
               {'step': 'control:scribe', 'outcome': 'pass', 'detail': ''},
               {'step': 'control:site', 'outcome': 'pass', 'detail': ''},
               {'step': 'control:support', 'outcome': 'pass', 'detail': ''}]
    a = Hypothesis('A holds', 'not A', 'distributional', units=['x'])
    b = Hypothesis('B holds', 'not B', 'distributional', units=['y'])
    a.log = list(passing); b.log = list(passing)
    it = Iteration()
    it.add(a); it.add(b, uses=['A holds'])
    assert it.provenance('B holds') == [('B holds', 'A holds')]
    it.uses['A holds'].add('B holds')
    with pytest.raises(CircularSupport):
        it.check_cycles()

def test_iteration_refuses_to_lean_on_a_failed_claim():
    from kuro import Hypothesis, Iteration
    import pytest
    a = Hypothesis('A holds', 'not A', 'distributional')
    a.test(lambda: 0.0, lambda: 1.0, n=10)          # fails the null
    b = Hypothesis('B holds', 'not B', 'distributional')
    it = Iteration()
    it.add(a)
    with pytest.raises(ValueError):
        it.add(b, uses=['A holds'])

def test_error_rate_qualifies_a_result_and_admits_when_it_cannot():
    from kuro import ErrorRate
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        er = ErrorRate(os.path.join(d, 'rates.json'))
        # unmeasured instrument: the sentence must say so, not imply a rate
        s = er.qualify('never_measured', 0.01)
        assert 'has not been measured' in s
        # measured: the sentence carries the rate
        er.measure('toy', 'synthetic', lambda rng: rng.random(), n=200, seed=1)
        s = er.qualify('toy', 0.01)
        assert 'false positive' in s and '%' in s
        r = er.rate_for('toy')
        assert 0.0 <= r['rate'] <= 1.0

def test_error_rate_is_recorded_per_corpus():
    """Pooling hides that an instrument behaves differently on different material."""
    from kuro import ErrorRate
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        er = ErrorRate(os.path.join(d, 'rates.json'))
        er.measure('toy', 'corpus A', lambda rng: 0.001, n=50, seed=1)
        er.measure('toy', 'corpus B', lambda rng: 0.9, n=50, seed=2)
        assert len(er.rates['toy']) == 2
        assert er.rates['toy'][0]['rate'] == 1.0 and er.rates['toy'][1]['rate'] == 0.0
        assert er.rate_for('toy')['rate'] == 0.5
        assert 'corpus A' in er.report() and 'corpus B' in er.report()

def test_p_of_zero_is_reported_as_a_bound_not_as_zero():
    """No run of n draws resolves below 1/n. Reporting p = 0 claims more than was measured."""
    from kuro import Hypothesis
    h = Hypothesis('x exceeds y', 'y exceeding x in a larger corpus', 'distributional')
    h.test(lambda: 100.0, lambda: 0.0, n=500)
    detail = [e for e in h.log if e['step'] == 'null'][0]['detail']
    assert 'p < 0.002' in detail and 'p = 0.0000' not in detail
    h.control('scribe'); h.control('site'); h.control('support'); h.correct(1)
    ev = h.to_evidence()
    assert 'p < ' in ev['note']

def test_error_rate_refuses_to_qualify_an_unresolved_p():
    from kuro import ErrorRate
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        er = ErrorRate(os.path.join(d, 'r.json'))
        er.measure('toy', 'synthetic', lambda rng: rng.random(), n=200, seed=1)
        s = er.qualify('toy', 0)
        assert 'cannot be qualified more finely' in s

def test_hypothesis_files_itself_where_it_belongs():
    from kuro import Hypothesis, Dictionary
    d = Dictionary([{'form': 'X', 'status': 'untouched', 'evidence': []}])
    h = Hypothesis('X behaves so', 'X behaving otherwise', 'distributional', units=['X'])
    h.test(lambda: 10.0, lambda: 0.0, n=100)
    h.control('scribe'); h.control('site'); h.control('support')
    h.correct(1)
    filed = h.file(dictionary=d)
    assert filed['verdict'] == 'survives' and filed['dictionary'] == ['X']
    assert d['X']['evidence'] and d['X']['refuted_by'] == 'X behaving otherwise'

def test_orders_returns_a_hypothesis_carrying_its_own_p():
    from kuro import Orders
    docs = [['A', 'B', 'C'], ['A', 'B'], ['A', 'B'], ['C', 'A'], ['B', 'A']]
    h = Orders(docs, seed=1).adjacency_hypothesis('A', 'B', n=200)
    assert h.p is not None
    assert h.units == ['A', 'B']
    assert h.refuted_by

# ---- lessons: the system learns from what failed ---------------------------------------------

def test_lessons_warn_but_never_reject():
    """A lesson schedules a control; it does not refuse the hypothesis.

    If failures could block, the system would eventually refuse everything — not because the
    claims are bad but because it accumulated prohibitions.
    """
    from kuro import Lessons, Hypothesis
    L = Lessons(withdrawn=[])
    h = Hypothesis('*21M co-occurs with the block', 'the association vanishing under a site null',
                   'distributional', units=['*21M', 'CYP'])
    advice = L.advise(h)
    assert advice, 'no lesson fired on a distributional claim about a numbered sign'
    assert 'site' in L.required_controls(h)
    # the hypothesis still runs
    h.test(lambda: 9.0, lambda: 1.0, n=200)
    h.control('scribe'); h.control('support')
    assert h.verdict() == 'incomplete', 'the scheduled control was not owed'
    h.control('site', p_value=0.02)
    h.correct(1)
    assert h.verdict() == 'survives', 'clearing the scheduled control did not let it through'

def test_lessons_fire_on_absence_claims_without_keywords():
    from kuro import Lessons, Hypothesis
    L = Lessons()
    h = Hypothesis('no sign-group ends in -mo', 'one that does', 'absence', units=['-mo'])
    ids = {a['id'] for a in L.advise(h)}
    assert 'absence' in ids
    assert 'instrument' in L.required_controls(h)

def test_affordability_threshold_depends_on_the_test():
    """Applying the co-occurrence threshold to adjacency would refuse a real result."""
    from kuro import Lessons
    docs = [['A', 'B'], ['A', 'B'], ['A', 'B'], ['A', 'B'], ['A'], ['B']] + [['C']] * 60
    L = Lessons()
    assert L.affordable(['A', 'B'], docs, test='adjacency')['run'], (
        'adjacency refused although four documents contain both')
    assert not L.affordable(['A', 'B'], docs, test='cooccurrence')['run'], (
        'co-occurrence allowed although the expected joint count is tiny')

def test_affordability_refuses_what_the_corpus_cannot_decide():
    from kuro import Lessons
    docs = [['A'], ['B'], ['C']] * 10
    L = Lessons()
    r = L.affordable(['A', 'B'], docs, test='adjacency')
    assert not r['run'] and 'contain both' in r['why']
    r2 = L.affordable(['Z'], docs)
    assert not r2['run'] and 'not attested' in r2['why']

# ---- generation ------------------------------------------------------------------------------

def test_generator_does_not_propose_punctuation_or_numerals():
    """Its first run proposed the divider and the numeral 1 as the best candidates."""
    from kuro.generate import is_unit
    for good in ('KU-RO', 'CYP', '*305', 'VIR+KA', 'SA-RA\u2082', 'CYP+D'):
        assert is_unit(good), f'{good} should be a unit'
    for bad in ('\U00010101', '1', '23', '\u00b9\u2044\u2082', '', 'x'):
        assert not is_unit(bad), f'{bad!r} should not be a unit'

def test_generator_ranks_untreated_units_above_treated_ones():
    from kuro import Generator, Dictionary
    class FakeRef:
        def mentioned(self, u): return u != 'NEW'
        def __len__(self): return 1
    dic = Dictionary([{'form': 'OLD', 'attestations': 6, 'evidence': [], 'status': 'untouched'},
                      {'form': 'NEW', 'attestations': 6, 'evidence': [], 'status': 'untouched'}])
    docs = [['OLD', 'NEW'] for _ in range(6)] + [['OLD'], ['NEW']]
    out = Generator(dic, docs, FakeRef()).from_dictionary(limit=20)
    forms = [c['form'] for c in out]
    assert forms.index('NEW') < forms.index('OLD'), (
        'a unit no indexed work treats should rank above one they do')

def test_literature_generator_marks_what_is_already_measured():
    from kuro import Generator, Dictionary
    g = Generator(Dictionary([]), [['A', 'B']], None)
    pending = g.from_literature()
    done = g.literature_done()
    assert done, 'nothing recorded as already measured'
    pending_claims = {x['hypothesis'].claim for x in pending}
    for c in done:
        assert c['claim'] not in pending_claims, 'a measured claim was offered again'
    for x in pending:
        assert x['hypothesis'].refuted_by

def test_problem_shape_names_fields_and_the_transplant_rule():
    """The methods that survived here came from other fields; the search should be deliberate."""
    from kuro import Generator
    shape = Generator.problem_shape()
    assert shape['fields_with_the_same_shape']
    names = [f for f, _ in shape['fields_with_the_same_shape']]
    assert any('basket' in n for n in names), 'market-basket analysis is the closest untried fit'
    chk = Generator.transplant_checklist('association rules', 'market-basket analysis')
    assert 'recover the known answer' in ' '.join(chk['questions'])
    assert chk['rule']

# ---- generation ------------------------------------------------------------------------------

def test_generator_only_proposes_what_the_corpus_can_decide():
    """The brake is power, not a count: candidates that fail affordability are not proposed."""
    from kuro import Generator, Dictionary, Lessons
    docs = ([['AA', 'BB']] * 4) + [['ZZ'], ['YY']] + [['QQ']] * 40
    dic = Dictionary([{'form': f, 'attestations': n, 'evidence': [], 'status': 'untouched'}
                      for f, n in [('AA', 4), ('BB', 4), ('ZZ', 1), ('YY', 1)]])
    g = Generator(dic, docs, lessons=Lessons())
    cands = g.combinatorial(limit=50)
    units = {tuple(sorted(c['units'])) for c in cands}
    assert ('AA', 'BB') in units
    assert not any('ZZ' in c['units'] or 'YY' in c['units'] for c in cands), (
        'proposed a claim about units the corpus cannot decide')

def test_generator_skips_units_that_already_have_a_reading():
    from kuro import Generator, Dictionary, Lessons
    docs = [['AA', 'BB']] * 6
    dic = Dictionary([
        {'form': 'AA', 'attestations': 6, 'gloss': 'known', 'status': 'established', 'evidence': []},
        {'form': 'BB', 'attestations': 6, 'gloss': 'known', 'status': 'established', 'evidence': []}])
    g = Generator(dic, docs, lessons=Lessons())
    assert g.combinatorial() == [], 'proposed a claim about two units that both have a reading'

def test_literature_generator_finds_unquantified_claims():
    """A claim stated without a number is a hypothesis someone else already formed."""
    import os, tempfile
    from kuro import Generator, Dictionary, Reference, Lessons
    docs = [['LANA', 'TELA']] * 8
    dic = Dictionary([{'form': 'LANA', 'attestations': 8, 'evidence': [], 'status': 'untouched'},
                      {'form': 'TELA', 'attestations': 8, 'evidence': [], 'status': 'untouched'}])
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'w_2024.txt'), 'w', encoding='utf-8') as f:
            f.write('TELA is always followed by LANA on these tablets\n')
        g = Generator(dic, docs, lessons=Lessons())
        lit = g.from_literature(Reference(d))
        assert lit and {'TELA', 'LANA'} <= set(lit[0]['units'])
        assert 'invariant' in lit[0]['why']
        assert lit[0]['hypothesis'].refuted_by, 'a generated candidate must carry a refutation'

def test_literature_generator_does_not_reoffer_what_we_measured():
    """A claim already measured here would look like a new result the second time."""
    import os, tempfile
    from kuro import Generator, Dictionary, Reference, Lessons
    docs = [['OLIV', 'CYP']] * 8
    dic = Dictionary([{'form': 'OLIV', 'attestations': 8, 'evidence': [], 'status': 'untouched'},
                      {'form': 'CYP', 'attestations': 8, 'evidence': [], 'status': 'untouched'}])
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'w_2024.txt'), 'w', encoding='utf-8') as f:
            f.write('the commodity is measured in proportion to OLIV, always in fractions\n')
        g = Generator(dic, docs, lessons=Lessons())
        offered = {c['claim'].lower() for c in g.from_literature(Reference(d))}
        assert not any('in proportion to oliv' in c for c in offered)
        assert any('OLIV' in x['measured'] or 'proportion' in x['claim']
                   for x in g.literature_done())

def test_problem_shape_states_what_does_not_transfer():
    """The cipher case is listed as a calibration corpus, not as a source of methods."""
    from kuro import ProblemShape
    txt = ProblemShape.candidates()
    assert 'no verifier' in ProblemShape.describe()
    assert 'differs' in txt or 'does not transfer' in txt
    assert ProblemShape.untried(), 'no untried field recorded'

def test_generator_ranks_the_middle_band_above_the_extremes():
    """Frequent units are grammaticalised; rare ones have no distribution. The middle informs.

    The first version ranked by raw frequency and put KU-RO-like units on top, which is exactly
    the end that cannot discriminate.
    """
    from kuro import Generator
    f = Generator.informativeness
    assert f(1) == 0.0 and f(2) == 0.0, 'a unit with no distribution should score zero'
    assert f(12) > f(3), 'within the band, more attestations should help'
    assert f(12) > f(170), 'a grammaticalised unit should not outrank the middle band'
    assert f(12) > f(60)
    assert f(200) > 0, 'frequent units should be demoted, not excluded'

def test_the_cycle_lets_something_through():
    """Forty-seven green tests were compatible with a cycle that produced nothing.

    The first end-to-end trial put ten candidates through and all ten died at the novelty gate,
    because the gate asked whether the units were mentioned rather than whether the claim was
    made. This test exists so that a strangled cycle fails loudly instead of looking healthy.
    """
    import os, tempfile
    from kuro import Hypothesis, Reference
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, 'w_2024.txt'), 'w', encoding='utf-8') as f:
            f.write('CYP is a commodity logogram attested at Haghia Triada and Khania. '
                    'NI denotes figs.\n')
        ref = Reference(d)
        # a claim whose units are catalogued but whose content is not stated anywhere
        h = Hypothesis('CYP is immediately followed by NI above chance',
                       'the adjacency vanishing under a within-document shuffle',
                       'positional', units=['CYP', 'NI'])
        h.check_literature(ref)
        assert h.status != 'published_already', (
            'the novelty gate blocked a claim merely because its units are catalogued; '
            'that strangles the cycle')

def test_benjamini_hochberg_replaces_bonferroni_for_large_families():
    """At two hundred tests Bonferroni's threshold is 0.00025 and nothing real clears it."""
    from kuro import Hypothesis
    family = [0.001] * 5 + [0.5] * 195
    h = Hypothesis('x', 'not x', 'distributional')
    h.test(lambda: 10.0, lambda: 0.0, n=1000)
    h.p = 0.001
    h.correct(200, family_p=family)
    assert h.correction_method == 'Benjamini-Hochberg'
    assert [e for e in h.log if e['step'] == 'multiple'][0]['outcome'] == 'pass', (
        'BH rejected a p-value that is among the five smallest of two hundred')
    h2 = Hypothesis('x', 'not x', 'distributional')
    h2.test(lambda: 10.0, lambda: 0.0, n=1000)
    h2.p = 0.001
    h2.correct(200)
    assert h2.correction_method == 'Bonferroni'
    assert 'would be the appropriate choice' in \
        [e for e in h2.log if e['step'] == 'multiple'][0]['detail'], (
        'Bonferroni at this family size should say what it is doing')

def test_efficiency_refuses_to_report_reduction_as_accuracy():
    """A filter that rejects everything scores perfectly on reduction alone."""
    from kuro import Efficiency
    e = Efficiency()
    for i in range(10):
        e.record(f'c{i}', 'published_already')
    for i in range(5):
        e.record(f'd{i}', 'not_supported', p=0.01)
    s = e.summary()
    assert s['reduction'] == 1.0
    assert 'not as accuracy' in s['note'] and 'no key' in s['note']
    assert 'apparent results removed' in e.report()

def test_error_rates_are_measured_for_every_instrument_in_use():
    """An instrument whose error rate is unmeasured qualifies nothing it produces."""
    import json, os
    p = 'data/derived/error_rates.json'
    if not os.path.exists(p):
        return
    rates = json.load(open(p, encoding='utf-8'))
    for inst in ('cooccurrence', 'positional_test', 'shared_fraction', 'arithmetic', 'constraints'):
        assert inst in rates, f'{inst} is used in the papers and has no measured error rate'
        for rec in rates[inst]:
            assert 'curve' in rec, f'{inst}: no threshold curve, so a low p cannot be qualified'
            c = rec['curve']
            ks = sorted((float(k) for k in c), reverse=True)
            for a, b in zip(ks, ks[1:]):
                assert c[str(a)] >= c[str(b)] - 1e-9, (
                    f'{inst}: false-positive rate rises as the threshold falls, which is impossible')

def test_a_superseded_measurement_is_kept_with_its_reason():
    """A measurement that was wrong is information; deleting it invites repeating it."""
    import json, os
    p = 'data/derived/error_rates.json'
    if not os.path.exists(p):
        return
    rates = json.load(open(p, encoding='utf-8'))
    sup = rates.get('shared_fraction_uniform_null')
    assert sup, 'the superseded uniform-null measurement was deleted rather than kept'
    assert 'note' in sup[0] and 'null was' in sup[0]['note']

# ---- the bipartite null ------------------------------------------------------------------------

def test_curveball_preserves_both_degree_sequences():
    """If a swap changes a degree, the null is testing something other than the hypothesis."""
    from collections import Counter
    from kuro import BipartiteNull
    docs = [['A', 'B', 'C'], ['A', 'B'], ['B', 'C'], ['A', 'C', 'D'], ['D', 'E'], ['A', 'E']]
    nb = BipartiteNull(docs, seed=1)
    before = nb.degrees()
    rows = nb.sample()
    ud = Counter()
    for r in rows:
        for i in r:
            ud[i] += 1
    after = {'documents': [len(r) for r in rows],
             'units': [ud[i] for i in range(len(nb.units))]}
    assert before == after, 'the shuffle changed a degree sequence'

def test_stratified_null_only_swaps_within_a_stratum():
    """Preserving degrees is not enough: on this corpus it changed nothing. Site was the cause."""
    from kuro import BipartiteNull
    docs = [['A', 'B'], ['A', 'C'], ['X', 'Y'], ['X', 'Z']]
    strata = ['s1', 's1', 's2', 's2']
    nb = BipartiteNull(docs, seed=2, strata=strata)
    for _ in range(5):
        rows = nb.sample()
        s1 = set().union(*rows[:2]) if rows[:2] else set()
        s2 = set().union(*rows[2:]) if rows[2:] else set()
        names1 = {nb.units[i] for i in s1}
        names2 = {nb.units[i] for i in s2}
        assert names1 <= {'A', 'B', 'C'}, 'a unit crossed strata'
        assert names2 <= {'X', 'Y', 'Z'}, 'a unit crossed strata'

def test_bipartite_reports_what_it_preserves():
    from kuro import BipartiteNull
    docs = [['A', 'B'], ['A', 'B'], ['A', 'C'], ['B', 'C']]
    r = BipartiteNull(docs, seed=3).cooccurrence('A', 'B', n=50)
    assert 'preserves' in r and 'document sizes' in r['preserves']
    r2 = BipartiteNull(docs, seed=3, strata=['x', 'x', 'y', 'y']).cooccurrence('A', 'B', n=50)
    assert 'within stratum' in r2['preserves']

def test_hierarchy_partitions_variance_to_one():
    from kuro import Hierarchy
    recs = [{'site': 'A', 'scribe': 's1', 'f': 1.0}, {'site': 'A', 'scribe': 's1', 'f': 1.2},
            {'site': 'A', 'scribe': 's2', 'f': 3.0}, {'site': 'A', 'scribe': 's2', 'f': 3.2},
            {'site': 'B', 'scribe': 's3', 'f': 8.0}, {'site': 'B', 'scribe': 's3', 'f': 8.4}]
    p = Hierarchy(recs, levels=['site', 'scribe']).partition('f')
    total = p['site'] + p['scribe'] + p['residual']
    assert abs(total - 1.0) < 1e-6, f'shares do not sum to one: {total}'
    assert p['site'] > 0.4, 'the site difference here is large and should dominate'

def test_hierarchy_says_when_there_is_too_little_to_partition():
    from kuro import Hierarchy
    p = Hierarchy([{'site': 'A', 'f': 1.0}, {'site': 'A', 'f': 2.0}], levels=['site']).partition('f')
    assert 'too few' in p.get('note', '')

# ---- hierarchy and Westfall-Young ---------------------------------------------------------------

def test_hierarchy_shares_sum_to_one():
    from kuro import Hierarchy
    items = [['a'], ['a', 'b'], ['b'], ['b', 'c'], ['c'], ['c', 'a']]
    prof = lambda d: {x: d.count(x) / len(d) for x in set(d)}
    h = Hierarchy(items, {'outer': list('XXYYZZ'), 'inner': list('123456')}, prof)
    r = h.partition()
    assert abs(sum(l['share'] for l in r['levels']) - 1.0) < 1e-9
    assert r['levels'][-1]['level'].startswith('within')

def test_hierarchy_gives_a_share_where_a_paired_null_gives_only_a_verdict():
    """The point of importing this: a small share is not a confounder worth controlling."""
    from kuro import Hierarchy
    # a level that groups at random should take almost none of the variation
    items = [['a', 'a', 'b'], ['a', 'b', 'b'], ['b', 'b', 'c'], ['c', 'c', 'a']] * 4
    prof = lambda d: {x: d.count(x) / len(d) for x in set(d)}
    labels = ['g1', 'g2'] * 8
    h = Hierarchy(items, {'random_level': labels}, prof)
    share = h.partition()['levels'][0]['share']
    assert share < 0.3, 'a meaningless grouping took a large share of the variation'

def test_westfall_young_needs_comparable_statistics():
    """The first version used raw counts and came out more conservative than Bonferroni.

    With p-values, a test correlated with the family should be able to pass where Bonferroni
    fails; with raw counts of different scales, the family maximum is set by the biggest count
    and everything else is crushed.
    """
    from kuro import WestfallYoung
    world = [['A', 'B'], ['A', 'B'], ['A', 'B'], ['C', 'D'], ['C', 'D'], ['E', 'F']] * 6
    def make(a, b):
        return lambda w: sum(1 for d in w for i in range(len(d) - 1)
                             if d[i] == a and d[i + 1] == b)
    tests = {'A->B': make('A', 'B'), 'C->D': make('C', 'D'), 'E->F': make('E', 'F'),
             'B->A': make('B', 'A')}
    def permute(w, rng):
        out = []
        for d in w:
            e = list(d)
            rng.shuffle(e)
            out.append(e)
        return out
    wy = WestfallYoung(tests).run(permute, world, n=300)
    a = wy.adjusted('A->B')
    assert 0.0 <= a['adjusted_p'] <= 1.0
    assert a['adjusted_p'] >= a['raw_p'] - 1e-9, 'an adjusted p below the raw p is impossible'
    assert 'dependence between tests' in a['note']

def test_westfall_young_reports_where_it_beats_bonferroni():
    from kuro import WestfallYoung
    world = [['A', 'B'], ['A', 'B'], ['C', 'D'], ['E', 'F'], ['G', 'H']] * 8
    def make(a, b):
        return lambda w: sum(1 for d in w for i in range(len(d) - 1)
                             if d[i] == a and d[i + 1] == b)
    tests = {f'{a}->{b}': make(a, b) for a, b in
             [('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H')]}
    def permute(w, rng):
        out = []
        for d in w:
            e = list(d)
            rng.shuffle(e)
            out.append(e)
        return out
    wy = WestfallYoung(tests).run(permute, world, n=200)
    c = wy.compare_with_bonferroni('A->B')
    assert set(c) >= {'westfall_young', 'bonferroni_threshold', 'power_gained'}
    assert 'declared by Westfall-Young and not by Bonferroni' in wy.report()

# ---- predictive claims ---------------------------------------------------------------------

def test_predictive_refuses_to_run_without_being_told_about_alignment():
    """The first libation run scored 20.2% by predicting the position it aligned on."""
    import pytest
    from kuro import PredictiveTest
    with pytest.raises(ValueError):
        PredictiveTest({'a': {0: 'X', 1: 'Y'}}, exclude_positions=None)
    t = PredictiveTest({'a': {0: 'X', 1: 'Y'}}, exclude_positions=set())
    assert t.exclude == set()

def test_predictive_reports_losing_to_the_base_rate():
    """Beating a shuffled null while losing to a constant guess is not a prediction."""
    from kuro import PredictiveTest
    items = {f'i{k}': {0: 'ANCHOR', 1: 'COMMON', 2: f'rare{k}'} for k in range(8)}
    always_wrong = lambda train, pos, comp: 'NEVER'
    t = PredictiveTest(items, exclude_positions={0}, seed=1)
    r = t.run(always_wrong, n_null=100)
    assert r['hits'] == 0 and not r['beats_base']
    h = t.as_hypothesis('x predicts y', 'it not doing so', units=[])
    assert h.verdict() == 'not_supported'
    assert any('does NOT beat' in e['detail'] for e in h.log)

def test_predictive_records_which_positions_were_excluded():
    from kuro import PredictiveTest
    items = {f'i{k}': {0: 'A', 1: 'B', 2: 'C'} for k in range(6)}
    perfect = lambda train, pos, comp: {1: 'B', 2: 'C'}.get(pos)
    t = PredictiveTest(items, exclude_positions={0}, seed=2)
    r = t.run(perfect, n_null=50)
    assert r['excluded_positions'] == [0]
    h = t.as_hypothesis('claim', 'refutation', units=['B'])
    assert any(e['step'] == 'control:leakage' for e in h.log)
    assert 'baseline' in h.confounders() and 'leakage' in h.confounders()

def test_predictive_hypothesis_needs_both_its_controls():
    from kuro import Hypothesis
    h = Hypothesis('a predictive claim', 'its failure', 'predictive')
    h.test(lambda: 1.0, lambda: 0.0, n=50)
    assert set(h.unchecked_confounders()) == {'baseline', 'leakage'}
    assert h.verdict() == 'incomplete'

def test_error_rate_flags_a_rate_from_too_few_trials():
    """0.0% from seven trials looks like a perfect instrument and is the absence of a measurement."""
    from kuro import ErrorRate
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        er = ErrorRate(os.path.join(d, 'r.json'))
        er.measure('thin', 'tiny corpus', lambda rng: 0.9, n=7, seed=1)
        r = er.rate_for('thin')
        assert r['rate'] == 0.0 and r['underpowered']
        assert 'could not be measured' in er.qualify('thin', 0.01)
        assert 'NOT MEASURED' in er.report()
        er.measure('thick', 'real corpus', lambda rng: 0.9, n=200, seed=2)
        assert not er.rate_for('thick')['underpowered']

# ---- the reader ------------------------------------------------------------------------------

def test_reader_parses_a_full_answer_and_rejects_a_partial_one():
    from kuro import Reader
    good = ("UNITS: OLIV, OLIV+TU\nKIND: positional\n"
            "CLAIM: OLIV+TU always occurs immediately after OLIV\n"
            "REFUTED_BY: an attestation of OLIV+TU not preceded by OLIV\n"
            "SOURCE_SAYS: since OLIV+TU always appears just after OLIV")
    p = Reader.parse(good)
    assert p and p['units'] == ['OLIV', 'OLIV+TU'] and p['kind'] == 'positional'
    h = p.to_hypothesis()
    assert h.kind == 'positional' and h.refuted_by
    # missing the refutation: not a proposition
    assert Reader.parse("UNITS: OLIV\nKIND: positional\nCLAIM: something\n") is None
    # a refutation that is not one
    assert Reader.parse("UNITS: OLIV\nKIND: positional\nCLAIM: x\nREFUTED_BY: nothing\n") is None
    # unknown kind
    assert Reader.parse("UNITS: OLIV\nKIND: semantic\nCLAIM: x\nREFUTED_BY: a b c d e\n") is None
    assert Reader.parse("NONE: about meaning") is None

def test_reader_rejects_units_the_corpus_lacks():
    """A unit the corpus does not have is a sign the model invented one."""
    from kuro import Reader
    answer = ("UNITS: ZZ-ZZ\nKIND: distributional\nCLAIM: ZZ-ZZ co-occurs with figs\n"
              "REFUTED_BY: ZZ-ZZ never occurring with figs in any document\n")
    r = Reader(model=lambda prompt: answer, known_units={'NI', 'VIN'})
    assert r.read('some passage', units=['NI']) is None
    assert r.log[-1]['outcome'] == 'rejected'

def test_reader_yield_matches_the_hand_reading():
    """Read by hand, 26 passages gave 7 propositions. A reader must not invent more than the text has."""
    from kuro import Reader
    # a model that answers NONE for bibliography and a proposition for a real claim
    def model(prompt):
        if 'in proportion to' in prompt or 'always appears just after' in prompt:
            return ("UNITS: OLIV, *308\nKIND: distributional\n"
                    "CLAIM: *308 is measured in proportion to OLIV\n"
                    "REFUTED_BY: an attestation of *308 in a document without OLIV in whole units\n")
        return "NONE: bibliography only"
    r = Reader(model=model, known_units={'OLIV', '*308'})
    cands = [{'claim': 'Bennett 1950; Schoep 2002, 130; see also', 'units': ['OLIV']},
             {'claim': '*308 measured in proportion to OLIV, always in fractions', 'units': ['*308', 'OLIV']},
             {'claim': 'Fig. 6.13: Textile signs and their developments', 'units': ['*86']}]
    props = r.read_all(cands)
    assert len(props) == 1
    assert 'proposition 1' in r.report() and 'none 2' in r.report()

# ---- the proposer ------------------------------------------------------------------------------

def test_proposer_extrapolation_only_uses_commodity_hosts():
    """The first version reported KU as a qualifier of seventeen 'commodities' including MA-JU,
    which is a word that begins with KU-. A qualifier attaches to a commodity, not to any word."""
    from kuro import Proposer, Dictionary
    docs = [['OLE+KI', 'GRA'], ['KI-MA-RU', 'NI'], ['KU-MA-JU', 'VIN'], ['GRA+KI'], ['OLE+KI']]
    dic = Dictionary([{'form': f, 'attestations': 2, 'evidence': [], 'status': 'untouched'}
                      for f in ['OLE+KI', 'KI-MA-RU', 'KU-MA-JU', 'GRA+KI']])
    P = Proposer(dic, docs)
    props = P.extrapolate('qualifier')
    syls = {p['claim'].split()[0] for p in props}
    assert 'KI' in syls, 'KI attaches to OLE, MA-RU and GRA and should be found'
    assert 'KU' not in syls, 'KU-MA-JU is a word, not a qualified commodity'

def test_proposer_analogy_uses_quantity_magnitude():
    """Without magnitude every unit with whole numbers looked like KU-RO."""
    from kuro.propose import _dist
    small = dict(head=0, whole=1, frac=0, withlog=0, site_conc=1, median_qty=3)
    big = dict(head=0, whole=1, frac=0, withlog=0, site_conc=1, median_qty=300)
    assert _dist(small, big) > 0.5, 'a unit at 3 and one at 300 should not be near'
    assert _dist(small, dict(small)) == 0.0

def test_proposer_output_is_ready_for_the_cycle():
    from kuro import Proposer, Dictionary
    docs = [['OLE+KI', 'GRA'], ['GRA+KI'], ['OLE+KI']]
    dic = Dictionary([{'form': 'OLE+KI', 'attestations': 2, 'evidence': [], 'status': 'untouched'},
                      {'form': 'GRA+KI', 'attestations': 1, 'evidence': [], 'status': 'untouched'}])
    for p in Proposer(dic, docs).extrapolate('qualifier'):
        h = p.to_hypothesis()
        assert h.refuted_by and h.kind and h.units

# ---- the normalizer ----------------------------------------------------------------------------

def test_normalizer_makes_a_vowelless_corpus_comparable():
    """Ugaritic has no vowels; a consonantal skeleton is the one place it and Linear A meet."""
    from kuro import Normalizer
    N = Normalizer('consonantal')
    assert N.word('ku-pa-nu') == 'kpn'
    assert N.word("<bd<vtr") == "'bd'vtr"
    assert N.word('θania') == 'tn'
    assert N.word('ḫarkandu') == 'xrknd'

def test_normalizer_declares_its_loss():
    from kuro import Normalizer
    N = Normalizer('consonantal')
    rep = N.report({'a': ['ka-ta', 'ki-ta', 'ku-ta', 'pa-ta'], 'b': ['xyz', 'abc']})
    assert 'collapsed' in rep
    assert N.loss['a'] > 0, 'ka-ta, ki-ta, ku-ta collapse to kt; the loss must be recorded'
