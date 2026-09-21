"""Clasificación distribucional de los signos del Lineal A en logogramas y silabogramas.

El corpus no distingue los dos usos por la forma: NI es el ideograma del higo y la sílaba
/ni/, y lo mismo pasa con KA, KU, SI, TE, RO, E, O y con los signos numerados *86, *188 y
*305. Una regla basada en mayúsculas los confunde, y esa confusión invalidó dos medidas de
sintaxis el 15 de septiembre de 2026, dando 77% y 2% para el mismo dato según cómo se
clasificara.

El criterio es distribucional, no formal:

    logograma    al menos el 70% de sus apariciones son sueltas, y de esas
                 al menos el 40% van seguidas de cifra o al menos el 30% llevan ligadura
    silabograma  al menos el 70% de sus apariciones están dentro de una unidad con guiones
    ambiguo      uso real en los dos papeles, al menos el 35% de cada

Validado contra los logogramas que el campo reconoce: once aciertos, cero fallos, ningún
falso positivo. NI, *188 y *305 salen ambiguos, que es lo que son.
"""
import json
import re
from collections import Counter

NUMERAL = re.compile(r'^[\d¹²³⁴⁵⁶⁷⁸⁹⁰⁄½¼¾⅓⅕⅙⅛\s≈—𐝫]+$')
SIGNO = re.compile(r'^[A-Z*0-9]{1,6}$')
DIVISOR = '𐄁'


def clasificar(inscripciones, minimo=8):
    """Devuelve {'logogramas': [...], 'silabogramas': [...], 'ambiguos': [...]}."""
    total, suelto, ligado, con_cifra, en_unidad = Counter(), Counter(), Counter(), Counter(), Counter()
    for _, doc in inscripciones:
        toks = [t for t in doc.get('transliteratedWords', [])
                if isinstance(t, str) and t.strip() and t not in ('\n', DIVISOR)]
        for i, t in enumerate(toks):
            if '-' in t:
                for s in t.split('-'):
                    if SIGNO.match(s):
                        en_unidad[s] += 1
                        total[s] += 1
            else:
                base = t.split('+')[0]
                if not SIGNO.match(base) or NUMERAL.match(base):
                    continue
                total[base] += 1
                suelto[base] += 1
                if '+' in t:
                    ligado[base] += 1
                if i + 1 < len(toks) and NUMERAL.match(toks[i + 1]):
                    con_cifra[base] += 1
    logo, sil, amb = [], [], []
    for s, n in total.items():
        if n < minimo:
            continue
        p_suelto = suelto[s] / n
        p_unidad = en_unidad[s] / n
        p_cifra = con_cifra[s] / max(suelto[s], 1)
        p_ligado = ligado[s] / max(suelto[s], 1)
        if p_suelto >= 0.70 and (p_cifra >= 0.40 or p_ligado >= 0.30):
            logo.append(s)
        elif p_unidad >= 0.70:
            sil.append(s)
        elif p_suelto >= 0.35 and p_unidad >= 0.35:
            amb.append(s)
    return {'logogramas': sorted(logo), 'silabogramas': sorted(sil), 'ambiguos': sorted(amb)}


def cargar(path='data/derived/logogramas.json'):
    with open(path, encoding='utf-8') as f:
        return json.load(f)
