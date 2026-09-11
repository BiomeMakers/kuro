#!/usr/bin/env python3
"""Put the propositions of a units run (data/derived/units_run.json) through the cycle.

Routing by what the proposition says:
  one logogram + a commodity class  -> ProfileTest (fraction rate against the base, size)
  two units, positional             -> adjacency null
  two units, other                  -> site-stratified co-occurrence null
Then the novelty gate (already published -> kept aside as prior art to file, not discarded),
correction over the whole batch, and a verdict per proposition. Nothing is written to the
dictionary here: the output lists what to file, with the two evidences each entry would carry.
"""
import json, sys, os, re, argparse
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro import Dictionary, Reference, Lessons, Efficiency, BipartiteNull, Orders
from kuro.generate import is_unit
from kuro.propose import Proposition
from kuro.profile import ProfileTest, is_logogram

ap = argparse.ArgumentParser()
ap.add_argument('run', nargs='?', default='data/derived/units_run.json')
args = ap.parse_args()

CLASS_WORDS = [
    ('persons',   r'\b(person|persons|man|men|people|worker|personnel)\b'),
    ('livestock', r'\b(sheep|goat|ox|oxen|cattle|bull|cow|pig|swine|ram|ewe|livestock|animal)\b'),
    ('fine',      r'\b(saffron|crocus|spice|aromatic|condiment|perfume|unguent|bronze|copper|gold|silver|metal|ingot|sesame|coriander|cumin)\b'),
    ('textile',   r'\b(cloth|textile|garment|wool|fleece|tunic|linen)\b'),
    ('liquid',    r'\b(oil|wine|honey|must|liquid|vinegar)\b'),
    ('bulk',      r'\b(grain|wheat|barley|cereal|emmer|flour|corn)\b'),
    ('staple',    r'\b(fig|figs|olive|olives|fruit|cyperus|legume|pulse)\b'),
]

def klass(claim):
    for k, pat in CLASS_WORDS:
        if re.search(pat, claim, re.I):
            return k
    return None

run = json.load(open(args.run))
props = [Proposition(**{k: v for k, v in p.items() if k in ('units', 'kind', 'claim', 'refuted_by', 'source_says', 'mechanism', 'score', 'klass', 'confidence')}) for p in run['propositions']]
for p, raw in zip(props, run['propositions']):
    p['source'] = raw.get('source')
print(f'{len(props)} propositions from {run["passages"]} passages')

d = json.load(open('data/raw/inscriptions.json'))
docs = [[t for t in it.get('transliteratedWords', []) if isinstance(t, str) and t != '\n'] for n, it in d]
sites = [it.get('site') or '?' for n, it in d]
dic = Dictionary.load('data/derived/dictionary.json')
ref = Reference('docs/reference')
L = Lessons.from_manifest('manifest.json')
P = ProfileTest(docs)
from collections import Counter
from math import comb
FIRST, N_ON_TABLETS = Counter(), Counter()
for (n_, it_), doc in zip(d, docs):
    if 'Tablet' not in (it_.get('support') or ''):
        continue
    for i, t in enumerate(doc):
        if len(t) > 1:
            N_ON_TABLETS[t] += 1; FIRST[t] += (i == 0)
FIRST_BASE = sum(FIRST.values()) / max(1, sum(N_ON_TABLETS.values()))
clean = [[t for t in doc if is_unit(t)] for doc in docs]
keep = [i for i, x in enumerate(clean) if x]
nb = BipartiteNull([clean[i] for i in keep], seed=3, strata=[sites[i] for i in keep])
o = Orders([clean[i] for i in keep], seed=5)
eff = Efficiency()
prior_art, survivors, unsupported, failed = [], [], [], []
tested = []
for p in props:
    h = p.to_hypothesis(); L.advise(h); h.check_literature(ref)
    units = [u for u in p['units'] if u in dic.entries]
    if h.status == 'published_already':
        if p.get('source') == 'model':
            p['prior_art'] = True; h.status = 'proposed'   # the model's reading has prior art: test it anyway, file with both
        else:
            prior_art.append(p); eff.record(h.claim, 'published_already'); continue
    k = p.get('klass') or klass(p['claim'])
    if len(units) == 1 and k == 'heading':
        m_, k_ = FIRST[units[0]], N_ON_TABLETS[units[0]]
        if k_ == 0:
            unsupported.append((p, 'not on tablets')); eff.record(h.claim, 'not_supported'); continue
        pv = sum(comb(k_, i) * FIRST_BASE ** i * (1 - FIRST_BASE) ** (k_ - i) for i in range(m_, k_ + 1))
        h.p = pv; h.observed = m_; h.null_mean = FIRST_BASE * k_
        h.log.append({'step': 'null', 'outcome': 'pass' if pv < 0.05 else 'fail', 'detail': f'first position {m_}/{k_} vs base {FIRST_BASE:.3f}, p={pv:.4f}'})
        tested.append((p, h, 'heading', {'direction': 'above'}))
    elif len(units) == 1 and k == 'qualifier' and '+' in units[0]:
        q = units[0].split('+', 1)[1]
        hosts = {t.split('+')[0] for doc in docs for t in doc if t.endswith('+' + q)}
        ok = len(hosts) >= 2
        h.p = 0.0 if ok else 1.0; h.observed = len(hosts); h.null_mean = 1
        h.log.append({'step': 'null', 'outcome': 'pass' if ok else 'fail', 'detail': f'+{q} attached to {len(hosts)} commodities: {sorted(hosts)} (rule: two or more)'})
        tested.append((p, h, 'qualifier', {'direction': 'rule'}))
    elif len(units) == 1 and is_logogram(units[0]) and k in ('persons', 'livestock', 'bulk', 'fine', 'liquid', 'staple', 'textile'):
        r = P.test(units[0], k)
        if r['p'] is None:
            unsupported.append((p, 'no quantified attestation')); eff.record(h.claim, 'not_supported'); continue
        h.p = r['p']; h.observed = r['profile']['frac']; h.null_mean = r['profile']['base'] * r['n']
        h.log.append({'step': 'null', 'outcome': 'pass' if r['compatible'] else 'fail',
                      'detail': f'profile as {k}: {r["profile"]["frac"]}/{r["n"]} fractional, base {r["profile"]["base"]:.2f}, max {r["profile"]["max"]}, p={r["p"]:.4f}, size_ok={r["size_ok"]}'})
        for c in ('scribe', 'site', 'support'):
            h.control(c, note='profile pools all sites; not stratified in this pass')
        tested.append((p, h, 'profile', r))
    elif len(units) >= 2 and p['kind'] == 'positional':
        r = o.adjacency(units[0], units[1], n=500)
        h.p = r['p']; h.observed = r['observed']; h.null_mean = r['null_mean']
        h.log.append({'step': 'null', 'outcome': 'pass' if h.p < 0.05 else 'fail', 'detail': f'adjacency {r["observed"]} vs {r["null_mean"]:.1f}, p={h.p:.4f}'})
        for c in ('scribe', 'site', 'support'):
            h.control(c, note='not run in this pass')
        tested.append((p, h, 'adjacency', r))
    elif len(units) >= 2:
        r = nb.cooccurrence(units[0], units[1], n=2000)
        h.p = r['p']; h.observed = r['observed']; h.null_mean = r['null_mean']
        h.log.append({'step': 'null', 'outcome': 'pass' if h.p < 0.05 else 'fail', 'detail': f'co-occurrence {r["observed"]} vs {r["null_mean"]:.1f}, p={h.p:.4f}'})
        for c in ('scribe', 'site', 'support'):
            h.control(c, note='site preserved by the stratified null; scribe and support not run in this pass')
        tested.append((p, h, 'cooccurrence', r))
    else:
        unsupported.append((p, 'no instrument for this claim')); eff.record(h.claim, 'not_supported'); continue

NOTES = {'baseline': 'the permutation null is the baseline for this instrument',
         'leakage': 'the claim comes from the literature, not from a split of the corpus it is tested on',
         'genre': 'pooled across supports and sites in this pass; not stratified',
         'scribe': 'not run in this pass', 'site': 'preserved by the stratified null where used', 'support': 'not run in this pass'}
for p, h, inst, r in tested:
    for c in list(h.unchecked_confounders()):
        h.control(c, note=NOTES.get(c, 'not run in this pass'))
    if inst == 'qualifier':
        v = 'survives' if h.p == 0.0 else 'fails'; eff.record(h.claim, v, p=h.p)
    elif inst == 'profile' and r['direction'] == 'base':
        v = 'survives' if r['compatible'] else 'fails'     # compatibility, not significance
        eff.record(h.claim, v, p=h.p)
    else:
        h.correct(len(tested)); v = h.verdict(); eff.record(h.claim, v, p=h.p)
    (survivors if v == 'survives' else failed).append((p, h, inst, r))

print(eff.report()); print()
print(f'PRIOR ART (published, to file with the citation): {len(prior_art)}')
for p in prior_art: print(f'  [{", ".join(p["units"])}] {p["claim"][:110]}  <- {p.get("source")}')
print(f'\nSURVIVE (our test agrees): {len(survivors)}')
for p, h, inst, r in survivors: print(f'  [{", ".join(p["units"])}] {p["claim"][:100]}  | {inst} p={h.p:.4f}')
print(f'\nFAIL (our test disagrees): {len(failed)}')
for p, h, inst, r in failed: print(f'  [{", ".join(p["units"])}] {p["claim"][:100]}  | {inst} p={h.p:.4f} status={h.status} unchecked={h.unchecked_confounders()}')
print(f'\nUNSUPPORTED (no instrument): {len(unsupported)}')
for p, why in unsupported[:15]: print(f'  [{", ".join(p["units"])}] {p["claim"][:90]}  | {why}')
out = {'prior_art': [dict(p) for p in prior_art], 'survivors': [dict(p) | {'p': h.p, 'instrument': inst} for p, h, inst, r in survivors],
       'failed': [dict(p) | {'p': h.p, 'instrument': inst} for p, h, inst, r in failed],
       'unsupported': [dict(p) | {'why': w} for p, w in unsupported], 'efficiency': eff.report()}
json.dump(out, open('data/derived/units_cycle.json', 'w'), ensure_ascii=False, indent=1)
print('\nsaved data/derived/units_cycle.json')
