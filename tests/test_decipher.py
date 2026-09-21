import numpy as np

from kuro import decipher


def test_a_value_has_a_feature_vector():
    v = decipher.feature_vector('ka')
    assert v is not None and v.sum() > 0
    assert decipher.feature_vector('gra') is None


def test_voicing_pairs_differ_in_one_feature():
    assert np.abs(decipher.feature_vector('ka') - decipher.feature_vector('ga')).sum() == 1


def test_the_mapping_is_a_distribution_per_sign():
    d = decipher.Decipher(['A', 'B'], ['ka-ru'], seed=0)
    P = d.mapping()
    assert np.allclose(P.sum(axis=1), 1.0)


def test_an_anchor_is_clamped_to_its_value():
    d = decipher.Decipher(['A', 'B'], ['ka-ru'], anchors={'A': 'ka'}, seed=0)
    assert d.best_values()['A'] == 'ka'


def test_the_true_mapping_scores_above_a_false_one():
    """The point of the objective: truth must beat a wrong assignment."""
    vocab = ['ka-ru', 'ru-to', 'ka-to', 'to-ru', 'ka-ru-to', 'to-ka-ru']
    units = [('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'B'), ('A', 'B', 'C')]
    truth = decipher.Decipher(['A', 'B', 'C'], vocab, anchors={'A': 'ka', 'B': 'ru', 'C': 'to'})
    false = decipher.Decipher(['A', 'B', 'C'], vocab, anchors={'A': 'mi', 'B': 'se', 'C': 'pu'})
    assert truth.quality(units) > false.quality(units)


def test_sound_loss_punishes_a_collapsed_mapping():
    spread = decipher.Decipher(['A', 'B'], ['ka-ru'], anchors={'A': 'ka', 'B': 'ru'})
    collapsed = decipher.Decipher(['A', 'B'], ['ka-ru'], anchors={'A': 'ka', 'B': 'ka'})
    assert collapsed.sound_loss() > spread.sound_loss()


def test_the_gradient_points_uphill():
    """A small step along the gradient must increase the objective."""
    vocab = ['ka-ru', 'ru-to', 'ka-to', 'to-ru', 'ka-ru-to', 'to-ka-ru']
    units = [('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'B'), ('A', 'B', 'C')]
    d = decipher.Decipher(['A', 'B', 'C'], vocab, seed=3)
    before, dW = d.objective_grad(units)
    d.W = d.W + 0.01 * dW
    after, _ = d.objective_grad(units)
    assert after > before


def test_ascent_recovers_a_toy_script():
    vocab = ['ka-ru', 'ru-to', 'ka-to', 'to-ru', 'ka-ru-to', 'to-ka-ru', 'ru-ka']
    units = [('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'B'), ('A', 'B', 'C'), ('B', 'A')]
    best = 0
    for seed in (0, 1, 2):
        d = decipher.Decipher(['A', 'B', 'C'], vocab, anchors={'A': 'ka'}, seed=seed)
        found, _ = d.ascend(units, steps=200, lr=1.0, batch=6, seed=seed)
        best = max(best, sum(1 for k, v in {'B': 'ru', 'C': 'to'}.items() if found[k] == v))
    assert best == 2
