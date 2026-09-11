#!/usr/bin/env python3
"""The model proposes: one reading per unread unit from its counts, guarded, then the cycle.

    PYTHONPATH=. python scripts/hypothesize_units.py --dry      # prints the cards, no calls
    PYTHONPATH=. python scripts/hypothesize_units.py            # one call per unit, progress line each
Output: data/derived/hypotheses_run.json (run scripts/cycle_units.py on it afterwards).
"""
import json, sys, os, argparse, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro import Dictionary
from kuro.hypothesize import Hypothesizer

ap = argparse.ArgumentParser()
ap.add_argument('--dry', action='store_true')
ap.add_argument('--min-att', type=int, default=3)
ap.add_argument('--limit', type=int, default=0)
args = ap.parse_args()

d = json.load(open('data/raw/inscriptions.json'))
dic = Dictionary.load('data/derived/dictionary.json')
lexb = json.load(open('data/raw/linearb/lexicon_B.json')) if os.path.exists('data/raw/linearb/lexicon_B.json') else []
seals = json.load(open('data/raw/nodules_seals_younger.json')) if os.path.exists('data/raw/nodules_seals_younger.json') else []
unread = [f for f, e in dic.entries.items() if not e.get('gloss') and e.get('attestations', 0) >= args.min_att and e.get('intact', True)]
unread.sort(key=lambda f: -dic.entries[f].get('attestations', 0))
if args.limit:
    unread = unread[:args.limit]
print(f'{len(unread)} unread units with >= {args.min_att} attestations')

if args.dry:
    H = Hypothesizer(model=lambda p: 'NONE: dry', dictionary=dic, inscriptions=d, lexicon_b=lexb, nodule_seals=seals)
    for u in unread[:6]:
        print(f'\n== {u}\n{H.card(u)}')
    sys.exit(0)

from kuro.models import anthropic_model
H = Hypothesizer(model=anthropic_model(), dictionary=dic, inscriptions=d, lexicon_b=lexb, nodule_seals=seals)
props, t0 = [], time.time()
for i, u in enumerate(unread, 1):
    p = H.propose(u)
    if p:
        p['source'] = 'model'; props.append(p)
    print(f'[{i}/{len(unread)}] {u:12s} {(p["klass"] if p else "-"):12s} {time.time()-t0:5.0f}s', flush=True)
print(H.report())
out = {'passages': len(unread), 'propositions': [dict(x) for x in props], 'reader_report': H.report(), 'log': H.log}
json.dump(out, open('data/derived/hypotheses_run.json', 'w'), ensure_ascii=False, indent=1)
print('saved data/derived/hypotheses_run.json')
for p in props:
    print(f'  [{", ".join(p["units"])}] {p["klass"]:10s} {p["claim"][:100]}')
