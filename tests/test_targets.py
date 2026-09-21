from kuro import targets


def test_cuneiform_signs_are_not_words():
    assert not targets.is_usable('𒀹')


def test_sumerograms_are_not_words():
    assert not targets.is_usable('KI.MIN')
    assert not targets.is_usable('DINGIRMEŠ-na')


def test_clitics_and_fragments_are_dropped():
    assert not targets.is_usable('nu')
    assert not targets.is_usable('-na')
    assert targets.is_usable('ta-ba-ar-na')


def test_long_vowels_count_as_vowels():
    assert targets.skeleton('šarrātu') == 'šrrt'
    assert targets.skeleton('i-ta-a') == 't'


def test_a_target_is_deduplicated():
    forms = ['pa-la'] * 113 + ['ta-ba-ar-na'] * 80 + ['𒀹', 'nu', 'KI.MIN']
    assert targets.normalise(forms) == sorted({'pl', 'tbrn'})


def test_an_already_clean_lexicon_is_left_alone():
    forms = ['baal', 'malku', 'rapiu']
    assert len(targets.normalise(forms)) == 3


def test_skeletons_longer_than_minoan_produces_are_dropped():
    forms = ['ba-la-ka', 'bddndsbsnls', 'ka-ru']
    out = targets.normalise(forms)
    assert 'blk' in out
    assert 'kr' in out
    assert not any(len(s) > targets.MAX_SKELETON for s in out)


def test_the_bound_is_a_parameter():
    assert len(targets.normalise(['bddndsbsnls'], max_skeleton=20)) == 1
