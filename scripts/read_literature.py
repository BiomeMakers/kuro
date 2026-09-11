#!/usr/bin/env python3
"""Read the literature and put every proposition it yields through the cycle.

    ANTHROPIC_API_KEY=... python scripts/read_literature.py            # real run
    python scripts/read_literature.py --dry                             # list the passages only

The regex in Generator.from_literature() finds the passages; the Reader turns each into a
proposition or discards it; each proposition becomes a Hypothesis and goes through the novelty
gate, the null its kind requires, the confounders the lessons schedule, and the correction. What
survives is filed. Everything is logged so the run can be audited passage by passage.
"""
import json, re, sys, os, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro import (Generator, Dictionary, Reference, Lessons, Constraints, Reader,
                  Orders, BipartiteNull, Efficiency)
from kuro.generate import is_unit

ap = argparse.ArgumentParser()
ap.add_argument('--dry', action='store_true')
ap.add_argument('--limit', type=int, default=300)
args = ap.parse_args()

d = json.load(open('data/raw/inscriptions.json'))
docs = [[t for t in it.get('transliteratedWords', []) if isinstance(t, str)] for n, it in d]
sites = [it.get('site') or '?' for n, it in d]
dic = Dictionary.load('data/derived/dictionary.json')
ref = Reference('docs/reference')
L = Lessons.from_manifest('manifest.json')
g = Generator(dic, docs, reference=ref, constraints=Constraints(), lessons=L)
cands = g.from_literature(limit=args.limit)
print(f'{len(cands)} passages found by the regex in {len(ref)} works')

if args.dry:
    for c in cands[:20]:
        print(f'  [{", ".join(c["units"])}] {c["claim"][:100]}')
    sys.exit(0)

from kuro.models import anthropic_model
reader = Reader(model=anthropic_model(), known_units=set(dic.entries))
props = reader.read_all(cands)
print(reader.report())
print()

clean = [[t for t in doc if is_unit(t)] for doc in docs]
keep = [i for i, x in enumerate(clean) if x]
clean = [clean[i] for i in keep]; csites = [sites[i] for i in keep]
nb = BipartiteNull(clean, seed=3, strata=csites)
o = Orders(clean, seed=5)
eff = Efficiency()
survivors = []
for p in props:
    h = p.to_hypothesis()
    L.advise(h)
    h.check_literature(ref)
    if h.status == 'published_already':
        eff.record(h.claim, 'published_already'); continue
    units = [u for u in p['units'] if u in dic.entries]
    if p['kind'] == 'positional' and len(units) >= 2:
        r = o.adjacency(units[0], units[1], n=500)
        h.p = r['p']; h.p_floor = r.get('p_floor'); h.observed = r['observed']; h.null_mean = r['null_mean']
        h.log.append({'step': 'null', 'outcome': 'pass' if h.p < 0.05 else 'fail',
                      'detail': f'adjacency {r["observed"]} vs {r["null_mean"]:.1f}, p={h.p:.4f}'})
        h.control('scribe', note='not run in this pass'); h.control('genre', note='not run in this pass')
    elif len(units) >= 2:
        r = nb.cooccurrence(units[0], units[1], n=400)
        h.p = r['p']; h.p_floor = r.get('p_floor'); h.observed = r['observed']; h.null_mean = r['null_mean']
        h.log.append({'step': 'null', 'outcome': 'pass' if h.p < 0.05 else 'fail',
                      'detail': f'co-occurrence {r["observed"]} vs {r["null_mean"]:.1f}, site-stratified p={h.p:.4f}'})
        for c in ('scribe', 'site', 'support'):
            h.control(c, note='site preserved by the null; others not run in this pass')
    else:
        eff.record(h.claim, 'not_supported'); continue
    h.correct(len(props))
    v = h.verdict()
    eff.record(h.claim, v, p=h.p)
    if v == 'survives':
        survivors.append((h.claim, h.p, p.get('source_says', '')))
print(eff.report())
print()
out={'passages': len(cands), 'propositions': [dict(x) for x in props], 'reader_report': reader.report(),
     'efficiency': eff.report(), 'survivors': [{'claim': c, 'p': p_, 'source_says': s_} for c, p_, s_ in survivors]}
os.makedirs('data/derived', exist_ok=True)
json.dump(out, open('data/derived/literature_run.json', 'w'), ensure_ascii=False, indent=1)
print('saved data/derived/literature_run.json')
print(f'SURVIVORS: {len(survivors)}')
for c, p, s in survivors:
    print(f'  {c}  (p={p:.4f})  <- "{s}"')
