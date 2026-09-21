import math

import pytest

from kuro.decipherability import Corpus


def linear_b_like():
    """A script with most of its signs anchored from outside: the solved case."""
    return Corpus('Linear B-like', signs=87, anchored=70, units=3000, match_rate=0.05)


def linear_a_like():
    """A script with few anchors and a permissive match rate: the open case."""
    return Corpus('Linear A-like', signs=110, anchored=16, units=552,
                  match_rate=0.738, values=74, languages=10)


def test_an_anchored_script_with_a_strict_match_rate_comes_out_decipherable():
    assert linear_b_like().decipherable


def test_a_script_with_few_anchors_and_loose_matching_does_not():
    corpus = linear_a_like()
    assert not corpus.decipherable
    assert corpus.deficit > 300


def test_the_deficit_is_priced_in_anchors_and_in_text():
    corpus = linear_a_like()
    assert corpus.anchors_needed() > 0
    assert corpus.units_needed() > 0


def test_closing_the_deficit_with_anchors_makes_it_decipherable():
    corpus = linear_a_like()
    closed = Corpus(corpus.name, corpus.signs,
                    corpus.anchored + corpus.anchors_needed(),
                    corpus.units, corpus.match_rate,
                    values=corpus.values, languages=corpus.languages)
    assert closed.decipherable


def test_a_match_rate_at_the_bounds_is_refused():
    with pytest.raises(ValueError):
        Corpus('impossible', signs=10, anchored=0, units=10, match_rate=1.0)


def test_more_anchors_than_signs_is_refused():
    with pytest.raises(ValueError):
        Corpus('impossible', signs=10, anchored=11, units=10, match_rate=0.5)


def test_a_solved_script_needs_no_further_anchors():
    assert linear_b_like().anchors_needed() == 0
