#!/usr/bin/env python3
"""Judge the model's proposals (data/derived/proposals_run.json) with the instruments of the cycle.

  persons/livestock/bulk/fine/liquid/staple/textile -> ProfileTest against the base rate
  heading   -> first-position rate on tablets against the base, binomial
  total     -> the figure after the unit equals the sum of the figures before it (summand)
  qualifier -> the syllable attaches to two or more distinct commodities (the rule of this work)
  name      -> no instrument yet (cross-commodity does not discriminate): recorded, not measured
Correction over the whole batch (Bonferroni). Nothing is written to the dictionary.
"""
import json, re, sys, os, argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import Counter, defaultdict
from math import comb
from kuro import Dictionary
from kuro.profile import ProfileTest, is_logogram

ap = argparse.ArgumentParser(); ap.add_argument('run', nargs='?', default='data/derived/proposals_run.json'); args = ap.parse_args()
run = json.load(open(args.run)); props = run['proposals']
d = json.load(open('data/raw/inscriptions.json'))
docs = [(it.get('support', ''), [t for t in it.get('transliteratedWords', []) if isinstance(t, str) and t != '\n']) for n, it in d]
dic = Dictionary.load('data/derived/dictionary.json'); E = dic.entries
P = ProfileTest([t for s, t in docs])
isnum = lambda x: bool(re.fullmatch(r'\d+', x))
first = defaultdict(lambda: [0, 0]); allf = [0, 0]
for sup, toks in docs:
    if 'Tablet' not in sup: continue
    for i, t in enumerate(toks):
        if t in E:
            first[t][1] += 1; allf[1] += 1
            if i == 0: first[t][0] += 1; allf[0] += 1
base_first = allf[0] / allf[1]
COMMODITY = {'GRA', 'NI', 'VIN', 'OLIV', '*OLIV', 'OLE', 'CYP', 'FIC', 'AROM', 'TELA', 'LANA', 'MA-RU', '*303', '*304',
             '*308', '*316', '*188', 'BOS', 'OVIS', 'CAP', 'CAPm', 'CAPf', 'OVISm', 'OVISf', 'SUS', 'VIR', '*21F', '*21M', '*22F', '*22M', '*23M'}
hosts = defaultdict(set)      # a qualifier attaches to COMMODITY signs; a syllable on a syllable is a monogram
for sup, toks in docs:
    for t in toks:
        if '+' in t and t.split('+')[0] in COMMODITY: hosts[t.split('+')[-1]].add(t.split('+')[0].lstrip('*'))

def test_heading(u):
    k, n = first[u]
    if n == 0: return None
    p = sum(comb(n, i) * base_first ** i * (1 - base_first) ** (n - i) for i in range(k, n + 1))
    return {'p': p, 'detail': f'first position {k}/{n} vs base {base_first:.2f}'}

def test_total(u):
    eq = n = 0
    for sup, toks in docs:
        for i, t in enumerate(toks):
            if t != u or i + 1 >= len(toks) or not isnum(toks[i + 1]): continue
            before = [int(x) for x in toks[:i] if isnum(x)]
            if len(before) >= 2:
                n += 1; eq += (sum(before) == int(toks[i + 1]))
    if n == 0: return None
    # null: chance that a figure equals the running sum is tiny; binomial with 2% base as a floor
    b = 0.02; p = sum(comb(n, i) * b ** i * (1 - b) ** (n - i) for i in range(eq, n + 1))
    return {'p': p, 'detail': f'sum matches {eq}/{n} (floor base 2%)'}

def test_entry(u):
    """A list entry, by exclusion: syllabic, followed by figures at least twice, not a heading, not a
    total, never an added syllable. Calibrated on 10 Sep 2026: all 17 known names pass and so does
    any commodity written syllabically, which is why this is a category, not a reading."""
    if '-' not in u: return None
    withnum = 0
    for sup, toks in docs:
        for i, t in enumerate(toks):
            if t == u and i + 1 < len(toks) and isnum(toks[i + 1]): withnum += 1
    if withnum < 2: return None
    h = test_heading(u); tot = test_total(u)
    added = any(t.split('+')[-1] == u for sup, toks in docs for t in toks if '+' in t)
    ok = (h is None or h['p'] > 0.05) and (tot is None or tot['p'] > 0.05) and not added
    return {'p': 0.0 if ok else 1.0, 'detail': f'{withnum} figures; heading p={h["p"] if h else "-"}; total p={tot["p"] if tot else "-"}; added={added}', 'category_only': True}

def test_qualifier(u):
    hs = hosts.get(u, set())
    return {'p': 0.0 if len(hs) >= 2 else 1.0, 'detail': f'attached to {len(hs)} commodities: {", ".join(sorted(hs))}'}

results = []
for pr in props:
    u, k = pr['unit'], pr['class']
    if u not in E: results.append((pr, 'invented', None)); continue
    if k in ('persons', 'livestock', 'bulk', 'fine', 'liquid', 'staple', 'textile'):
        if not is_logogram(u): results.append((pr, 'untestable', {'detail': 'class needs a logogram'})); continue
        r = P.test(u, k)
        if r['p'] is None: results.append((pr, 'untestable', {'detail': 'no figure'})); continue
        results.append((pr, 'measured', {'p': r['p'], 'compatible': r['compatible'], 'base_dir': r['direction'] == 'base', 'detail': f'{r["profile"]["frac"]}/{r["n"]} fractional, max {r["profile"]["max"]}'}))
    elif k == 'heading':
        r = test_heading(u); results.append((pr, 'measured' if r else 'untestable', r or {'detail': 'never on a tablet'}))
    elif k == 'total':
        r = test_total(u); results.append((pr, 'measured' if r else 'untestable', r or {'detail': 'never after two figures'}))
    elif k == 'qualifier':
        results.append((pr, 'measured', test_qualifier(u)))
    elif k == 'name':
        r = test_entry(u); results.append((pr, 'category' if r and r['p'] == 0 else 'untestable', r or {'detail': 'fewer than two figures'}))
    else:
        results.append((pr, 'untestable', {'detail': f'no instrument for class {k}'}))

measured = [x for x in results if x[1] == 'measured']
m = len([x for x in measured if not x[2].get('base_dir')]) or 1
thr = 0.05 / m
verdicts = []
for pr, st, r in results:
    if st == 'category': verdicts.append((pr, 'category', r)); continue   # list entry by exclusion: a category, never a reading
    if st != 'measured': verdicts.append((pr, st, r)); continue
    if r.get('base_dir'):
        v = 'compatible' if r['compatible'] else 'incompatible'
    else:
        v = 'survives' if r['p'] < thr else ('borderline' if r['p'] < 0.05 else 'fails')
    verdicts.append((pr, v, r))
c = Counter(v for _, v, _ in verdicts)
print(f'{len(props)} proposals; verdicts: ' + ', '.join(f'{k} {n}' for k, n in c.most_common()))
print(f'(Bonferroni over {m} directional tests, threshold {thr:.4f})\n')
for label in ('survives', 'compatible', 'borderline', 'fails', 'incompatible', 'category', 'untestable', 'invented'):
    rows = [(pr, r) for pr, v, r in verdicts if v == label]
    if not rows: continue
    print(f'== {label.upper()} ({len(rows)})')
    for pr, r in rows:
        p = f' p={r["p"]:.4f}' if r and r.get('p') is not None else ''
        print(f'  {pr["unit"]:12s} {pr["class"]:9s} {pr["reading"][:70]:70s} |{p} {r.get("detail", "") if r else ""}')
    print()
json.dump([{**pr, 'verdict': v, 'result': r} for pr, v, r in verdicts], open('data/derived/proposals_cycle.json', 'w'), ensure_ascii=False, indent=1)
print('saved data/derived/proposals_cycle.json')
