import json

import pytest

from kuro import anatolian


@pytest.fixture
def corpus(tmp_path):
    (tmp_path / 'lycian_0.json').write_text(json.dumps(
        {'TL 44 (Xanthos)': [{'word': '· 1', 'sentence': 'ebẽñnẽ xupa'},
                             {'word': '· 2', 'sentence': '(Greek-Lycian Bilingual)'}]}))
    (tmp_path / 'lycian_1.json').write_text('[]')
    return str(tmp_path)


def test_a_text_yields_its_label_and_words(corpus):
    texts = anatolian.load_corpus(corpus, 'lycian')
    assert list(texts) == ['TL 44 (Xanthos)']
    assert 'xupa' in texts['TL 44 (Xanthos)']


def test_empty_responses_are_skipped(corpus):
    assert len(anatolian.load_corpus(corpus, 'lycian')) == 1


def test_editorial_matter_is_not_a_word():
    assert not anatolian.is_word('TRANSLATION:')
    assert not anatolian.is_word('A 12')
    assert anatolian.is_word('xupa')


def test_the_vowel_profile_sums_to_one(corpus):
    texts = anatolian.load_corpus(corpus, 'lycian')
    profile, n = anatolian.vowel_profile(texts['TL 44 (Xanthos)'])
    assert n > 0
    assert abs(sum(profile.values()) - 1.0) < 1e-9


def test_distance_is_zero_for_identical_profiles():
    p = {'a': 0.4, 'e': 0.2, 'i': 0.2, 'o': 0.05, 'u': 0.15}
    assert anatolian.distance(p, p) == 0
