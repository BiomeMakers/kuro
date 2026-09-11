from kuro.profile import ProfileTest, is_logogram


def test_persons_count_in_whole_numbers():
    docs = [['VIR', '10'], ['VIR', '3'], ['VIR', '7'], ['VIR', '2'], ['VIR', '5'], ['VIR', '8'], ['VIR', '4'], ['VIR', '6'],
            ['CYP', '1', 'J'], ['CYP', 'E'], ['CYP', '2', 'J'], ['CYP', '1', 'E']]
    P = ProfileTest(docs)
    assert P.test('VIR', 'persons')['compatible']
    assert P.test('CYP', 'fine')['compatible']
    assert not P.test('VIR', 'fine')['compatible']


def test_ligature_counts_for_its_base():
    docs = [['OLE+KI', '2', 'J'], ['OLE', '4'], ['OLE+U', '1']]
    P = ProfileTest(docs)
    assert P.profile('OLE')['n'] == 3 and P.profile('OLE+KI')['n'] == 1


def test_is_logogram():
    assert is_logogram('*304') and is_logogram('OLE+KI') and is_logogram('*22F')
    assert not is_logogram('KU-RO') and not is_logogram('12')
