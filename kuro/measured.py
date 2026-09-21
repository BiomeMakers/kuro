"""Las restricciones MEDIDAS, en forma que un modelo generativo pueda usar.

Este trabajo acumuló durante un mes medidas que viven en documentos y en el diccionario, y
construyó un modelo de alineamiento que no las conocía. Corrido así, el 15 de septiembre de
2026, ese modelo ordenó las lenguas candidatas por el tamaño de su léxico — que es
exactamente el artefacto que el artículo 02 documenta en el criterio del campo.

Este módulo es el puente que faltaba. Cada función devuelve una penalización sobre una
asignación de valores, y todas descansan en una medida con su nulo y su p en manifest.json.

A diferencia de kuro.constraints, que elimina CATEGORÍAS de una unidad por lo que el género
admite, esto puntúa ASIGNACIONES DE VALOR por lo que la fonología medida permite.
"""
import json
import re
from collections import Counter

AUSENTES = {'do', 'jo', 'lo', 'mo', 'no', 'qo', 'so'}
PERFIL_VOCALICO = {'a': 0.405, 'i': 0.230, 'u': 0.174, 'e': 0.144, 'o': 0.047}
ARMONIA_NULA = 0.278


def penaliza_ausentes(asignacion):
    """Sílabas que el silabario no parece tener: seis consonantes con la serie completa
    salvo la o, p = 0.0003."""
    return sum(1 for v in asignacion.values() if v in AUSENTES)


def penaliza_perfil(asignacion, unidades):
    """Distancia entre el perfil vocálico que la asignación produce y el medido."""
    c = Counter()
    n = 0
    for u in unidades:
        for s in u:
            v = asignacion.get(s)
            if not v:
                continue
            vow = re.sub(r'[^aeiou]', '', v)
            if vow:
                c[vow] += 1
                n += 1
    if not n:
        return 0.0
    return sum(abs(c[k] / n - PERFIL_VOCALICO.get(k, 0)) for k in 'aeiou')


def penaliza_armonia(asignacion, unidades):
    """El minoico no tiene armonía vocálica (27.1% frente a 27.8% del nulo, potencia 100%
    verificada en Linear B): penaliza asignaciones que la creen."""
    pares = iguales = 0
    for u in unidades:
        for a, b in zip(u, u[1:]):
            va, vb = asignacion.get(a), asignacion.get(b)
            if not va or not vb:
                continue
            va = re.sub(r'[^aeiou]', '', va)
            vb = re.sub(r'[^aeiou]', '', vb)
            if va and vb:
                pares += 1
                iguales += (va == vb)
    return abs(iguales / pares - ARMONIA_NULA) if pares else 0.0


def carga_funciones(path='data/derived/dictionary.json'):
    with open(path, encoding='utf-8') as f:
        d = json.load(f)
    return {e['form'].lower().replace('₂', '2'): e['gloss']
            for e in d if e.get('form') and e.get('gloss')}


def penalizacion_total(asignacion, unidades, pesos=None):
    """Suma ponderada de las restricciones medidas. Menor es mejor."""
    p = pesos or {'ausentes': 1.0, 'perfil': 3.0, 'armonia': 5.0}
    return (p['ausentes'] * penaliza_ausentes(asignacion)
            + p['perfil'] * penaliza_perfil(asignacion, unidades)
            + p['armonia'] * penaliza_armonia(asignacion, unidades))
