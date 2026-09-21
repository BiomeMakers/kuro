from kuro import measured as constraints


def test_absent_syllables_are_penalised():
    assert constraints.penaliza_ausentes({'A': 'mo', 'B': 'ka'}) == 1
    assert constraints.penaliza_ausentes({'A': 'ka', 'B': 'ta'}) == 0


def test_a_vowel_profile_far_from_the_measured_one_costs_more():
    units = [['A', 'B'], ['A', 'B']]
    bueno = {'A': 'ka', 'B': 'ta'}          # todo a, como el perfil real (40.5%)
    malo = {'A': 'ko', 'B': 'to'}           # todo o, que es el 4.7%
    assert constraints.penaliza_perfil(malo, units) > constraints.penaliza_perfil(bueno, units)


def test_harmony_is_penalised_when_created():
    units = [['A', 'B']] * 10
    armonico = {'A': 'ka', 'B': 'ta'}       # misma vocal siempre: armonía total
    variado = {'A': 'ka', 'B': 'ti'}
    assert constraints.penaliza_armonia(armonico, units) > constraints.penaliza_armonia(variado, units)


def test_the_functional_inventory_loads():
    f = constraints.carga_funciones()
    assert len(f) > 50
    assert any('total' in (v or '').lower() for v in f.values())
