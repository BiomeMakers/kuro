import numpy as np
from kuro.relational import sign_profiles, cosine_distance, entropic_gw, align, accuracy_on_shared_names


def test_profiles_have_the_expected_shape():
    signs, M, c = sign_profiles([['a', 'b'], ['a', 'c', 'b']])
    assert signs == ['a', 'b', 'c']
    assert M.shape == (3, 2 * (3 + 1) + 3)


def test_coupling_is_a_valid_transport_plan():
    D1 = np.array([[0., 1, 2], [1, 0, 1], [2, 1, 0]])
    T = entropic_gw(D1, D1.copy(), epsilon=0.05, outer=30, inner=30)
    assert abs(T.sum() - 1) < 1e-6 and (T >= 0).all()


def test_identical_corpora_align_to_themselves():
    words = [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['a', 'c'], ['b', 'a']] * 6
    r = align(words, words, epsilon=0.02)
    acc = accuracy_on_shared_names(r)
    assert acc['shared'] == 3 and acc['accuracy'] >= 0.66
