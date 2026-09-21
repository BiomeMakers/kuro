from kuro import aligner


def test_identical_sequences_align_at_zero_cost():
    assert aligner.align_cost(['ku', 'pa', 'ro'], ['ku', 'pa', 'ro']) == 0


def test_a_voicing_change_costs_one():
    assert aligner.align_cost(['ku', 'pa'], ['gu', 'pa']) == 1


def test_a_missing_syllable_costs_an_insertion():
    assert aligner.align_cost(['ku', 'ro'], ['ku', 'pa', 'ro']) == aligner.INSERT


def test_the_aligner_recovers_a_toy_script():
    # a toy script of three signs whose true values are ka, ru, to
    truth = {'A': 'ka', 'B': 'ru', 'C': 'to'}
    vocab = ['ka-ru', 'ru-to', 'ka-to', 'to-ru', 'ka-ru-to']
    units = [('A', 'B'), ('B', 'C'), ('A', 'C'), ('C', 'B'), ('A', 'B', 'C')] * 4
    best = 0
    for seed in (1, 2, 3):
        al = aligner.Aligner(units, vocab, seed=seed, threshold=0.0)
        found, score = al.anneal(steps=1500, sample=None)
        if score == len(units):
            best = max(best, aligner.Aligner.recovered(found, truth))
    assert best == 3
