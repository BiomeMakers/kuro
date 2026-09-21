from kuro.adjudicate import Bench, classify


def test_glosses_are_classified_by_function():
    assert classify('the total of an account') == 'total'
    assert classify('a heading term') == 'heading'
    assert classify('fine grade of oil') == 'qualifier'
    assert classify('something else entirely') is None


def test_a_proposal_that_matches_the_measured_function_agrees():
    b = Bench({'KU-RO': ('total', 'the total', 'established')})
    r = b.agreement({'ku-ro': 'all, the sum'})
    assert len(r['agree']) == 1 and not r['clash']


def test_a_proposal_that_contradicts_it_clashes():
    b = Bench({'KU-RO': ('total', 'the total', 'established')})
    r = b.agreement({'ku-ro': 'a personal name'})
    assert len(r['clash']) == 1 and not r['agree']


def test_phonotactics_reports_distance_and_control():
    out = Bench.phonotactics(['ka-ro', 'ma-ru', 'ti-na'], ['krb', 'mlk', 'ksp'], reps=20)
    assert set(out) == {'distance', 'control', 'gap', 'p'}


def test_a_gloss_that_denies_a_class_is_not_read_as_asserting_it():
    b = Bench({'X': ('not-offering', 'does not designate the offering', 'proposed')})
    r = b.agreement({'X': 'the offering itself'})
    assert len(r['clash']) == 1 and not r['agree']
