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
