#!/usr/bin/env python3
"""Targeted reading: for every unread unit with enough attestations, find the passages in the
indexed literature that mention it, and put each through the Reader and the cycle.

    python scripts/read_units.py --dry                 # count passages, no calls
    ANTHROPIC_API_KEY=... python scripts/read_units.py # real run, progress per passage

Unlike read_literature.py (claim-marker regex over everything), this starts from the gaps of
the dictionary and asks the literature about each one. It is the mechanism that paid on 10 Sep
2026: readings by parallel with Linear B (livestock, commodities, NI, TE).
"""
import json, re, sys, os, argparse, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro import Dictionary, Reference, Reader, Lessons
from kuro.propose import Proposition

ap = argparse.ArgumentParser()
ap.add_argument('--dry', action='store_true')
ap.add_argument('--min-att', type=int, default=3)
ap.add_argument('--per-unit', type=int, default=4, help='passages per unit at most')
ap.add_argument('--window', type=int, default=350)
args = ap.parse_args()

dic = Dictionary.load('data/derived/dictionary.json')
ref = Reference('docs/reference')
flat = {w: re.sub(r'\s+', ' ', t) for w, t in ref.works.items()}
unread = [f for f, e in dic.entries.items()
          if not e.get('gloss') and e.get('attestations', 0) >= args.min_att and e.get('intact', True)]
unread.sort(key=lambda f: -dic.entries[f].get('attestations', 0))

def patterns(u):
    """how editions write the unit: *301, A 301, AB 301, *303 for CYP, hyphenated groups as such."""
    ps = [re.escape(u)]
    m = re.fullmatch(r'\*(\d+)([A-Z]?)(\+.*)?', u)
    if m:
        ps.append(r'(?:AB|A)\s?' + m.group(1) + (m.group(2).lower() if m.group(2) else '') + r'(?![0-9])')
    if '-' in u:
        ps.append(re.escape(u.lower()))
    return '|'.join(ps)

cands = []
for u in unread:
    pat = re.compile(r'(?<![A-Za-z0-9*])(?:' + patterns(u) + r')(?![A-Za-z0-9])')
    n = 0
    for w, s in flat.items():
        for m in pat.finditer(s):
            seg = s[max(0, m.start() - args.window):m.start() + args.window]
            if not re.search(r'logogram|ideogram|sign|means|reading|interpret|denot|commodit|name|term|abbreviat', seg, re.I):
                continue
            cands.append({'units': [u], 'claim': seg.strip(), 'source': w, 'kind': 'from_literature',
                          'hypothesis_kind': 'distributional'})
            n += 1
            if n >= args.per_unit:
                break
        if n >= args.per_unit:
            break
print(f'{len(unread)} unread units with >= {args.min_att} attestations; {len(cands)} passages found')
if args.dry:
    from collections import Counter
    c = Counter(x['units'][0] for x in cands)
    print('units with passages:', len(c))
    for u, k in c.most_common(25):
        print(f'  {u:12s} {k}')
    sys.exit(0)

from kuro.models import anthropic_model
reader = Reader(model=anthropic_model(), known_units=set(dic.entries))
props = []
t0 = time.time()
for i, cnd in enumerate(cands, 1):
    p = reader.read(cnd['claim'], cnd['units'])
    if p:
        p['source'] = cnd['source']; props.append(p)
    print(f'[{i}/{len(cands)}] {cnd["units"][0]:12s} {"proposition" if p else "-":12s} {time.time()-t0:5.0f}s', flush=True)
print(reader.report())
out = {'units': unread, 'passages': len(cands), 'propositions': [dict(x) for x in props],
       'sources': [(c['units'][0], c['source'], c['claim'][:300]) for c in cands],
       'reader_report': reader.report()}
os.makedirs('data/derived', exist_ok=True)
json.dump(out, open('data/derived/units_run.json', 'w'), ensure_ascii=False, indent=1)
print('saved data/derived/units_run.json')
print(f'PROPOSITIONS: {len(props)}')
for p in props:
    print(f'  [{", ".join(p["units"])}] {p["claim"][:120]}')
