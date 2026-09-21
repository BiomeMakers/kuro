from kuro.attempt import Attempt, apply_grid, normalise_target


def test_a_grid_reads_a_unit():
    assert apply_grid('ku-ro', {'ku': 'ku', 'ro': 'ro'}, permissive=False) == 'kuro'
    assert apply_grid('ku-ro', {'ku': 'ka', 'ro': 'lu'}, permissive=False) == 'kalu'


def test_the_target_is_reduced_to_what_the_syllabary_can_write():
    assert normalise_target('kalû', permissive=False) == 'kalu'
    assert normalise_target('kalû', permissive=True) == 'karu'


def test_the_functional_score_separates_grids_the_lexical_one_cannot():
    # swapping the signs here still yields two real words, so the lexical count is blind;
    # only the requirement that KU-RO mean a total tells the two grids apart
    units = ['ku-ro', 'da-me']
    lex = {'kuro': 'the total', 'dame': 'a man'}
    a = Attempt(units, lex, functions={'KU-RO': r'total'}, values=['ku', 'ro', 'da', 'me'],
                anchored={}, permissive=False, seed=1)
    good = {'ku': 'ku', 'ro': 'ro', 'da': 'da', 'me': 'me'}
    swapped = {'ku': 'da', 'ro': 'me', 'da': 'ku', 'me': 'ro'}
    assert a.score(good)['lexical'] == a.score(swapped)['lexical']
    assert a.score(good)['functional'] == 1
    assert a.score(swapped)['functional'] == 0


def test_annealing_returns_a_grid_and_a_score():
    units = ['ku-ro', 'da-me', 'ku-me']
    a = Attempt(units, {'kuro': 'total', 'dame': 'man', 'kume': 'oil'},
                values=['ku', 'ro', 'da', 'me'], permissive=False, seed=2)
    r = a.anneal(steps=200)
    assert set(r) == {'score', 'grid', 'objective'} and r['score']['units'] == 3
