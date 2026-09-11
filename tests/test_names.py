from kuro.names import NameMatcher, syls, broken_status, BREAK


def test_syls_and_exact_and_stem():
    M = NameMatcher(['PA-I-TO', 'A-KA-TA', 'ZU-ZU-ZU'], ['pa-i-to', 'a-ka-ta-jo', 'ko-no-so'])
    m = M.match()
    assert ('pa-i-to', 'pa-i-to') in m['exact']
    assert ('a-ka-ta', 'a-ka-ta-jo') in m['stem']
    assert not any(u == 'zu-zu-zu' for u, _ in m['exact'] + m['stem'])


def test_null_preserves_lengths():
    M = NameMatcher(['A-B-C', 'D-E'], ['x-y'], seed=1)
    for w in M.shuffled_units():
        assert len(syls(w)) in (2, 3)


def test_broken_status_uses_words_field():
    recs = [('X1', {'words': ['ab' + BREAK], 'transliteratedWords': ['A-B']}),
            ('X2', {'words': ['cd'], 'transliteratedWords': ['C-D']}),
            ('X3', {'words': ['ab'], 'transliteratedWords': ['A-B']})]
    st = broken_status(recs)
    assert st['a-b'] == 'intact' and st['c-d'] == 'intact'
    assert broken_status(recs[:1])['a-b'] == 'broken'
