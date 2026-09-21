import json

from kuro import signclass


def _doc(tokens):
    return ('X1', {'transliteratedWords': tokens})


def test_a_sign_that_stands_alone_with_figures_is_a_logogram():
    ins = [_doc(['GRA', '10']) for _ in range(10)]
    assert 'GRA' in signclass.clasificar(ins)['logogramas']


def test_a_sign_inside_units_is_a_syllabogram():
    ins = [_doc(['KU-RO', '5']) for _ in range(10)]
    r = signclass.clasificar(ins)
    assert 'KU' in r['silabogramas'] and 'RO' in r['silabogramas']


def test_a_sign_used_both_ways_is_ambiguous():
    ins = [_doc(['NI', '7']) for _ in range(6)] + [_doc(['NI-TA', '1']) for _ in range(6)]
    assert 'NI' in signclass.clasificar(ins)['ambiguos']


def test_rare_signs_are_left_unclassified():
    ins = [_doc(['XX', '3'])]
    r = signclass.clasificar(ins)
    assert not any('XX' in v for v in r.values())


def test_the_stored_list_recovers_the_known_logograms():
    r = signclass.cargar()
    for s in ('GRA', 'OLE', 'VIN', 'OLIV', 'CYP', 'VIR'):
        assert s in r['logogramas'], s
    assert 'NI' in r['ambiguos']
