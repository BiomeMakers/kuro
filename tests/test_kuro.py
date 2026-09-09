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
