from kuro import mixed


def test_a_cv_sign_splits_into_consonant_and_vowel():
    assert mixed.split_syllable('ka') == ('k', 'a')
    assert mixed.split_syllable('a') == ('', 'a')
    assert mixed.split_syllable('gra') is None


def test_phonetic_distance_is_small_between_voicing_pairs():
    assert mixed.phonetic_distance('ka', 'ga') == 1
    assert mixed.phonetic_distance('ka', 'ma') > mixed.phonetic_distance('ka', 'ga')
    assert mixed.phonetic_distance('ka', 'ka') == 0


def test_a_corpus_classifies_the_four_kinds():
    docs = [('HT1', ['KU-RO', 'GRA', '12', 'GRA+PA', '½', 'OLE+KI', 'A-DU'])]
    c = mixed.MixedCorpus(docs)
    s = c.summary()
    assert s['units'] == 2
    assert s['ligatures'] == 2
    assert s['logogram_tokens'] == 3
    assert s['fractions'] == 2


def test_the_ligature_constraint_allows_first_syllables_of_the_field():
    docs = [('HT1', ['GRA+PA', 'OLE+KI'])]
    c = mixed.MixedCorpus(docs)
    lex = {'GRA': {'paros', 'kupa'}, 'OLE': {'kiriwa'}}
    allowed = mixed.ligature_constraint(c, lex)
    assert allowed['pa'] == {'pa', 'ku'}
    assert allowed['ki'] == {'ki'}


def test_a_sign_bound_to_two_logograms_is_not_constrained():
    docs = [('HT1', ['GRA+KU', 'TELA+KU'])]
    c = mixed.MixedCorpus(docs)
    assert 'ku' not in mixed.ligature_constraint(c, {'GRA': {'ka'}, 'TELA': {'ki'}})


def test_bits_removed_is_log_of_the_ratio():
    assert abs(mixed.bits_removed({'pa': {'pa', 'ku'}}, 64) - 5.0) < 1e-9
