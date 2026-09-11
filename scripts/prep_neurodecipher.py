#!/usr/bin/env python3
"""Build .cog files for j-luo93/NeuroDecipher: Linear A (lost) against each candidate (known),
plus a control column of Minoan with syllable order destroyed. The model matches the two
vocabularies by minimum-cost flow over learned character embeddings; the cognate pairs in a
.cog file are only used for evaluation, so for an undeciphered pair the rows are unpaired
('_' in the known column) and the quantity to compare is the matching cost the model reports,
real Minoan against control Minoan, for each candidate.

    PYTHONPATH=. python scripts/prep_neurodecipher.py   -> data/derived/nd/<candidate>.cog and control.cog
"""
import json, csv, os, sys, random, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro.normalize import _clean
c = json.load(open('data/derived/corpus_all.json'))
la = sorted({w.lower() for w in c['LinA'] if '-' in w})
t = json.load(open('data/raw/candidates/tlhdig_by_language.json'))
cand = {'mycenaean': c['LinB'], 'hittite': c['Hittite'], 'ugaritic': c['Ugaritic'], 'eteocretan': c['Eteocretan'],
        'luwian': t['Luw'], 'hattic': t['Hat'], 'hurrian': t['Hur'], 'palaic': t['Pal']}
et = list(csv.DictReader(open('data/derived/openetruscan_clean.csv')))
col = [k for k in et[0] if 'word' in k.lower() or 'form' in k.lower()][0]; cand['etruscan'] = [r[col] for r in et if r.get(col)]
if os.path.exists('data/derived/iberian_corpus.json'):
    cand['iberian'] = list(json.load(open('data/derived/iberian_corpus.json'))['intact'])
os.makedirs('data/derived/nd', exist_ok=True)
def flat(w): return re.sub(r'[^a-zšśḫṣṭ₂₃]', '', _clean(w).lower().replace('-', ''))
rng = random.Random(7)
pool = [s for w in la for s in w.split('-')]; rng.shuffle(pool)
ctrl, i = [], 0
for w in la:
    n = len(w.split('-')); ctrl.append('-'.join(pool[i:i + n])); i += n
for name, words in cand.items():
    known = sorted({flat(w) for w in words if flat(w)})[:20000]
    for lost_name, lost in (('linear_a', la), ('control', ctrl)):
        rows = max(len(lost), len(known))
        with open(f'data/derived/nd/{lost_name}-{name}.cog', 'w', encoding='utf-8') as f:
            f.write(f'{lost_name}\t{name}\n')
            for j in range(rows):
                f.write(f'{flat(lost[j]) if j < len(lost) else "_"}\t{known[j] if j < len(known) else "_"}\n')
    print(f'{name:11s} known {len(known):6d}  -> linear_a-{name}.cog, control-{name}.cog')
print(f'\nlost: {len(la)} Linear A words (and {len(ctrl)} control words)')
