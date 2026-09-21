#!/usr/bin/env python3
"""Run the three decipherment attempts and score them on the same scale.

    python scripts/attempt.py uga           # Ugaritic
    python scripts/attempt.py akk --steps 40000
"""
import sys, os, json, re, csv, argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import defaultdict
from kuro.attempt import Attempt
from kuro.names import broken_status, syls
from kuro import Dictionary

ap = argparse.ArgumentParser()
ap.add_argument('lang', nargs='?', default='uga')
ap.add_argument('--steps', type=int, default=20000)
ap.add_argument('--controls', type=int, default=40)
a = ap.parse_args()

LOGO = re.compile(r'^(gra|ole|vin|oliv|cyp|ni|vir|arom|tela|lana|hide|fic)$')
def syllabic(u):
    ss = u.lower().split('-')
    return len(ss) >= 2 and all(re.fullmatch(r'(\*\d{3}|[a-z]{1,3}[23]?)', x) and not LOGO.fullmatch(x) for x in ss)

d = json.load(open('data/raw/inscriptions.json')); st = broken_status(d)
units = sorted(t for t in {'-'.join(syls(x)).lower() for n, it in d
                           for x in it.get('transliteratedWords', []) if isinstance(x, str) and '-' in x}
               if st.get(t) == 'intact' and syllabic(t))

lex = {}
for path in ('data/raw/lexicons/oracc_gloss.csv', 'data/raw/lexicons/ugaritic_dulat.csv'):
    if not os.path.exists(path): continue
    for r in csv.DictReader(open(path, encoding='utf-8')):
        if r['lang'].split('-')[0] != a.lang: continue
        lex[r['form']] = r['meaning']

CLASSES = {'total': r'\b(all|total|sum|entirety|whole|complete|deficit|remainder|balance|rest|amount)\b',
           'heading': r'\b(heading|record|account|list|document|register)\b',
           'offering': r'\b(offering|libation|gift|donation|sacrifice|votive)\b',
           'person': r'\b(man|woman|person|worker|servant|official|scribe)\b',
           'place': r'\b(city|town|place|land|country|settlement)\b',
           'commodity': r'\b(grain|barley|oil|wine|olive|fig|wool|cloth|sheep|goat|ox|cyperus|sesame|cumin|coriander|emmer|flour|cattle)\b'}
E = Dictionary.load('data/derived/dictionary.json').entries
functions = {}
for f, e in E.items():
    g = (e.get('gloss') or '').lower()
    for k, p in CLASSES.items():
        if re.search(p, g):
            functions[f.upper()] = CLASSES[k]; break

ANCH = {'pa': 'pa', 'i': 'i', 'to': 'to', 'su': 'su', 'ki': 'ki', 'ri': 'ri', 'ta': 'ta',
        'se': 'se', 'ja': 'ja', 'da': 'da', 'pi': 'pi', 'ro': 'ro', 'a': 'a', 'e': 'e',
        'o': 'o', 'u': 'u'}
VALUES = sorted({c + v for c in ['', 'p', 'b', 't', 'd', 'k', 'g', 'q', 's', 'z', 'r', 'l',
                                 'm', 'n', 'w', 'y', 'h'] for v in 'aeiou'})

print(f'unidades: {len(units)}  lexico {a.lang}: {len(lex)}  funciones: '
      f'{len([u for u in functions if u.lower() in units])}  valores posibles: {len(VALUES)}')
out = {}
for perm in (True, False):
    label = 'permisiva' if perm else 'estricta'
    at = Attempt(units, lex, functions=functions, values=VALUES, anchored=ANCH,
                 permissive=perm, seed=7)
    base = at.score(ANCH | {s: s for s in at.free})          # the Linear B grid itself
    ctrl = at.fictitious(a.controls)
    res = at.anneal(steps=a.steps)
    ml = sum(c['lexical'] for c in ctrl) / len(ctrl)
    mf = sum(c['functional'] for c in ctrl) / len(ctrl)
    sd = (sum((c['lexical'] - ml) ** 2 for c in ctrl) / len(ctrl)) ** 0.5
    print(f"\n== fonologia {label}")
    print(f"  rejilla del Lineal B tal cual : lexico {base['lexical']:4d}  funcional {base['functional']}")
    print(f"  rejillas ficticias (Packard)  : lexico {ml:7.1f}  funcional {mf:.2f}  (sd {sd:.1f}, n={len(ctrl)})")
    print(f"  mejor asignacion hallada      : lexico {res['score']['lexical']:4d}  funcional {res['score']['functional']}")
    print(f"  z de la rejilla del B frente al control: {(base['lexical'] - ml) / max(sd, 1e-9):.2f}")
    print(f"  z de la mejor hallada        : {(res['score']['lexical'] - ml) / max(sd, 1e-9):.2f}")
    out[label] = {'linear_b_grid': base, 'controls_mean_lexical': ml, 'controls_sd': sd,
                  'controls_mean_functional': mf, 'best': res['score'],
                  'best_grid': res['grid']}
os.makedirs('data/derived/attempts', exist_ok=True)
json.dump(out, open(f'data/derived/attempts/{a.lang}.json', 'w'), ensure_ascii=False, indent=1)
print(f"\n[guardado data/derived/attempts/{a.lang}.json]")
