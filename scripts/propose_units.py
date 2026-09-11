#!/usr/bin/env python3
"""The model proposes a reading for every unread unit, from its dossier; then the cycle judges.

    PYTHONPATH=. python scripts/propose_units.py --dry        # print the dossiers, no calls
    PYTHONPATH=. python scripts/propose_units.py              # one call per unit, progress line
Output: data/derived/proposals_run.json (to be cycled with scripts/cycle_proposals.py).
"""
import json, re, sys, os, argparse, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import Counter, defaultdict
from kuro import Dictionary
from kuro.profile import ProfileTest, is_logogram
from kuro.hypothesize import Hypothesizer, build_dossier

ap = argparse.ArgumentParser()
ap.add_argument('--dry', action='store_true')
ap.add_argument('--min-att', type=int, default=3)
ap.add_argument('--limit', type=int, default=0)
args = ap.parse_args()

d = json.load(open('data/raw/inscriptions.json'))
docs = [(it.get('site') or '?', it.get('support', ''), [t for t in it.get('transliteratedWords', []) if isinstance(t, str) and t != '\n']) for n, it in d]
dic = Dictionary.load('data/derived/dictionary.json'); E = dic.entries
P = ProfileTest([t for s, su, t in docs])
lex = {e['transcription'].upper(): e for e in json.load(open('data/raw/linearb/lexicon_B.json'))} if os.path.exists('data/raw/linearb/lexicon_B.json') else {}
seals = {}
if os.path.exists('data/raw/nodules_seals_younger.json'):
    for r in json.load(open('data/raw/nodules_seals_younger.json')):
        if r.get('sign') and r.get('seals'):
            seals.setdefault(r['sign'], Counter())[r['seals'][0]['code'] + ' ' + r['seals'][0]['motif'][:20]] += 1

unread = [f for f, e in E.items() if not e.get('gloss') and e.get('attestations', 0) >= args.min_att and e.get('intact', True)]
unread.sort(key=lambda f: -E[f].get('attestations', 0))
if args.limit: unread = unread[:args.limit]

# per-unit corpus facts
first = defaultdict(lambda: [0, 0]); comp = defaultdict(Counter); sites = defaultdict(Counter); sups = defaultdict(Counter)
allfirst = [0, 0]
for site, sup, toks in docs:
    units_here = [t for t in toks if t in E]
    for i, t in enumerate(toks):
        if t not in E: continue
        sites[t][site[:10]] += 1; sups[t][sup[:12] or '?'] += 1
        if 'Tablet' in sup:
            first[t][1] += 1; allfirst[1] += 1
            if i == 0: first[t][0] += 1; allfirst[0] += 1
        for o in set(units_here):
            if o != t and E[o].get('gloss'):
                comp[t][o] += 1        # companions that are already read: the anchors
base_first = allfirst[0] / allfirst[1]
after_comm = defaultdict(Counter); smaller = defaultdict(lambda: [0, 0])
isnum = lambda x: bool(re.fullmatch(r'\d+', x))
for site, sup, toks in docs:
    lastc = None; lastq = None
    for i, t in enumerate(toks):
        if t.split('+')[0] in ('GRA', 'OLE', 'OLIV', 'VIN', 'CYP', 'NI', 'VIR', 'TELA', '*304', '*188') and t in E and E[t].get('gloss'):
            lastc = t.split('+')[0]; lastq = int(toks[i + 1]) if i + 1 < len(toks) and isnum(toks[i + 1]) else None
        elif t in E and t != lastc and lastc:
            after_comm[t][lastc] += 1
            if lastq is not None and i + 1 < len(toks) and isnum(toks[i + 1]):
                smaller[t][1] += 1; smaller[t][0] += int(toks[i + 1]) < lastq
hosts_of = defaultdict(set)
for site, sup, toks in docs:
    for t in toks:
        if '+' in t:
            b, *rest = t.split('+'); hosts_of[rest[-1]].add(b)

dossiers = {}
for u in unread:
    lb = None
    if '-' in u and u.replace('₂', '2').replace('₃', '3') in {k.replace('₂', '2').replace('₃', '3') for k in lex}:
        e = lex.get(u) or next((v for k, v in lex.items() if k.replace('₂', '2') == u.replace('₂', '2')), None)
        if e: lb = f'the same sequence exists in Linear B: {e.get("greek", "")} {e.get("translation", "")}'.strip()
    elif is_logogram(u):
        lb = 'shared sign shapes are noted in the dictionary entry only when established; none given here'
    seal_note = None
    if u in seals:
        top = seals[u].most_common(3); seal_note = f'{sum(seals[u].values())} HT nodules, sealed by ' + ', '.join(f'{s} ({n})' for s, n in top)
    dossiers[u] = build_dossier(u, E[u], P.profile(u), first[u], base_first, comp[u], sites[u], sups[u],
                                seal_note=seal_note, lb_note=lb, hosts=sorted(hosts_of[u]) if u in hosts_of else None)
    if after_comm[u]:
        top = after_comm[u].most_common(2)
        line = 'position: comes after ' + ', '.join(f'{c} ({n} times)' for c, n in top)
        if smaller[u][1]:
            line += f'; its figure is smaller than the preceding commodity figure in {smaller[u][0]} of {smaller[u][1]} (a sub-quantity pattern if most)'
        dossiers[u] += '\n' + line
print(f'{len(unread)} unread units; {len(dossiers)} dossiers built')
if args.dry:
    for u in unread[:6]:
        print('\n' + dossiers[u])
    sys.exit(0)

from kuro.models import anthropic_model
H = Hypothesizer(anthropic_model(), known_units=set(E))
out = []; t0 = time.time()
for i, u in enumerate(unread, 1):
    pr = H.propose(u, dossiers[u])
    if pr: out.append(pr)
    print(f'[{i}/{len(unread)}] {u:12s} {H.log[-1]["outcome"]:10s} {H.log[-1]["why"][:50]:50s} {time.time()-t0:5.0f}s', flush=True)
print(H.report())
json.dump({'units': unread, 'dossiers': dossiers, 'proposals': out, 'log': H.log, 'report': H.report()},
          open('data/derived/proposals_run.json', 'w'), ensure_ascii=False, indent=1)
print('saved data/derived/proposals_run.json'); print(f'PROPOSALS: {len(out)}')
