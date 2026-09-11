from kuro.hypothesize import Hypothesizer
from kuro.models import stub_model


def test_invented_unit_is_dropped_before_the_cycle():
    ans = 'UNIT: KU\nCLASS: name\nREADING: KU is the party KA-RU-PA-ZO\nWHY: x\nREFUTED_BY: y\nCONFIDENCE: low'
    H = Hypothesizer(stub_model(ans), known_units={'KU', 'KA-PA'})
    assert H.propose('KU', 'UNIT: KU') is None
    assert H.log[-1]['outcome'] == 'invented'


def test_wrong_unit_and_unknown_class_are_dropped():
    H = Hypothesizer(stub_model('UNIT: KA-PA\nCLASS: heading\nREADING: x\nREFUTED_BY: y'), known_units={'KU', 'KA-PA'})
    assert H.propose('KU', 'UNIT: KU') is None and H.log[-1]['outcome'] == 'wrong_unit'
    H2 = Hypothesizer(stub_model('UNIT: KU\nCLASS: unknown\nREADING: x\nREFUTED_BY: y'), known_units={'KU'})
    assert H2.propose('KU', 'UNIT: KU') is None and H2.log[-1]['outcome'] == 'unknown'


def test_good_proposal_passes():
    H = Hypothesizer(stub_model('UNIT: KU\nCLASS: qualifier\nREADING: KU marks a grade\nWHY: attached to GRA, TELA\nREFUTED_BY: KU with a total\nCONFIDENCE: medium'), known_units={'KU', 'GRA', 'TELA'})
    pr = H.propose('KU', 'UNIT: KU')
    assert pr and pr['class'] == 'qualifier'
