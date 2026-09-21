from kuro.formats import FormatModel, category


def test_category_assigns_the_functional_class():
    assert category('KU-RO') == 'T' and category('GRA') == 'C' and category('12') == 'N'
    assert category('¹⁄₂') == 'f' and category('A-DU') == 'W' and category('𐄁') == '|'


def test_a_planted_motif_beats_the_markov_null():
    docs = [(f'x{i}', ['A-BC', 'GRA', '5', 'A-BC', 'GRA', '7']) for i in range(20)]
    docs += [(f'y{i}', ['GRA', '5', 'A-BC', '7', 'GRA', 'A-BC']) for i in range(20)]
    m = FormatModel(docs, seed=1)
    top = m.motifs(3, reps=20, min_count=5)
    assert top and top[0]['ratio'] >= 1.0
    assert m.documents_with('WCN')


def test_short_documents_are_dropped():
    m = FormatModel([('a', ['GRA', '1']), ('b', ['GRA', '1', 'NI', '2'])], seed=0)
    assert len(m.docs) == 1
