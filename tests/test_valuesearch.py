from kuro.valuesearch import ValueSearch, profile, jsd, consonant_of


def test_consonants_and_skeletons():
    S = ValueSearch([['ku', 'ro'], ['pa', 'i', 'to'], ['ki', 'ro']])
    assert consonant_of('pa') == 'p' and consonant_of('i') == ''
    assert S.skeletons(S.words, S.lb) == ['kr', 'pt', 'kr']
    a = dict(S.lb); a['ku'] = 'g'
    assert S.skeletons(S.words, a) == ['gr', 'pt', 'kr']


def test_control_keeps_lengths_and_inventory():
    S = ValueSearch([['ku', 'ro', 'ta'], ['pa', 'i']], seed=3)
    cw = S.control_words(seed=1)
    assert sorted(len(w) for w in cw) == [2, 3]
    assert sorted(x for w in cw for x in w) == sorted(['ku', 'ro', 'ta', 'pa', 'i'])


def test_anneal_never_worsens_and_respects_anchors():
    words = [['ku', 'ro'], ['ki', 'ro'], ['pa', 'i', 'to'], ['sa', 'ra'], ['ta', 'na']]
    S = ValueSearch(words, seed=1, fixed='anchored')
    target = profile(['kr', 'kr', 'pt', 'sr', 'tn'])
    start = S.distance(S.words, S.lb, target)
    best, a = S.anneal(S.words, target, steps=200, seed=2)
    assert best <= start + 1e-12
    for s in S.fixed & set(S.signs):
        assert a[s] == S.lb[s]
