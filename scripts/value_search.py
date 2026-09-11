#!/usr/bin/env python3
"""Search the sound values of Linear A signs against each candidate language, with the control.

    PYTHONPATH=. python scripts/value_search.py --steps 20000 --controls 10          # full (Mac, minutes)
    PYTHONPATH=. python scripts/value_search.py --steps 2000 --controls 3 --only Etruscan,Hurrian
Output: data/derived/value_search.json
"""
import json, csv, sys, os, argparse, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro.valuesearch import ValueSearch, profile
from kuro.normalize import Normalizer

ap = argparse.ArgumentParser()
ap.add_argument('--steps', type=int, default=4000); ap.add_argument('--controls', type=int, default=5)
ap.add_argument('--only', default='')
ap.add_argument('--seed-offset', type=int, default=0)
ap.add_argument('--anchored', action='store_true', help='keep the toponym-anchored signs fixed')
ap.add_argument('--out', default='data/derived/value_search.json')
args = ap.parse_args()
c = json.load(open('data/derived/corpus_all.json'))
words = [[s for s in w.lower().split('-') if s] for w in c['LinA'] if '-' in w]
t = json.load(open('data/raw/candidates/tlhdig_by_language.json'))
cand = {'Mycenaean': c['LinB'], 'Hittite': c['Hittite'], 'Ugaritic': c['Ugaritic'], 'Eteocretan': c['Eteocretan'],
        'Luwian': t['Luw'], 'Hattic': t['Hat'], 'Hurrian': t['Hur'], 'Palaic': t['Pal']}
for k in ('akkadian', 'sumerian', 'elamite'):
    try:
        v = json.load(open(f'data/raw/candidates/{k}.json')); v = v if isinstance(v, list) else v.get('words', [])
        cand[k.capitalize()] = [w for w in v if isinstance(w, str)][:60000]
    except Exception: pass
et = list(csv.DictReader(open('data/derived/openetruscan_clean.csv')))
col = [k for k in et[0] if 'word' in k.lower() or 'form' in k.lower()][0]; cand['Etruscan'] = [r[col] for r in et if r.get(col)]
if os.path.exists('data/derived/iberian_corpus.json'):
    cand['Iberian'] = list(json.load(open('data/derived/iberian_corpus.json'))['intact'])
if args.only: cand = {k: v for k, v in cand.items() if k in args.only.split(',')}
N = Normalizer('consonantal'); VS = ValueSearch(words, seed=0, fixed='anchored' if args.anchored else ())
print(f'{len(VS.words)} Minoan words, {len(VS.signs)} signs ({len(VS.free)} free, {len(VS.fixed & set(VS.signs))} anchored); {args.steps} steps, {args.controls} controls per candidate\n')
print('%-12s %8s %8s %9s %8s %6s %s' % ('candidate', 'LB', 'real', 'ctrl mean', 'ctrl sd', 'z', 'signs changed'))
out = {}; t0 = time.time()
for k, v in cand.items():
    target = profile(N.words(v))
    r = VS.run(target, steps=args.steps, controls=args.controls, seed_offset=args.seed_offset)
    out[k] = r
    print('%-12s %8.3f %8.3f %9.3f %8.3f %6s %3d   %4.0fs' % (k, r['lb'], r['real_best'], r['control_mean'], r['control_sd'], ('%.1f' % r['z']) if r['z'] is not None else '-', r['changed'], time.time() - t0), flush=True)
os.makedirs('data/derived', exist_ok=True)
json.dump(out, open(args.out, 'w'), ensure_ascii=False, indent=1)
print(f'\nsaved {args.out}')
print('reading: z is how many control spreads the real corpus can be brought closer than a corpus with no real sequences; below ~3 is what optimizing 75 free values does to anything.')
