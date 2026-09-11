#!/usr/bin/env python3
"""Read NeuroDecipher checkpoints (log/<date>/<run>/saved.latest) and write the matched pairs.
Run inside the NeuroDecipher folder on the Mac, with its venv active:
    python nd_extract.py log/09-11 > pairs.json
For each run: the best known word per lost word from the flow tensor, plus plain edit distance.
"""
import sys, os, glob, json, torch, editdistance
out = {}
for ck in sorted(glob.glob(os.path.join(sys.argv[1], '*', 'saved.latest'))):
    run = os.path.basename(os.path.dirname(ck))
    try:
        st = torch.load(ck, map_location='cpu', weights_only=False)
    except Exception as e:
        out[run] = {'error': str(e)[:100]}; continue
    fl = st['flow']
    flow = fl['flow'] if isinstance(fl, dict) and 'flow' in fl else fl
    try:
        lost = flow.names[0] if hasattr(flow, 'names') else fl['lost_words']
        known = flow.names[1] if hasattr(flow, 'names') else fl['known_words']
        T = flow.tensor if hasattr(flow, 'tensor') else flow
    except Exception as e:
        out[run] = {'error': 'unexpected flow structure: ' + str(list(fl.keys()) if isinstance(fl, dict) else type(fl))}; continue
    T = T.to_dense() if T.is_sparse else T
    K = 5
    vals, idx = T.topk(min(K, T.shape[1]), dim=1)
    pairs = []
    for i, w in enumerate(lost):
        top = [{'known': known[int(j)], 'flow': float(v), 'edit': editdistance.eval(w, known[int(j)])}
               for v, j in zip(vals[i], idx[i]) if float(v) > 0]
        if top:
            pairs.append({'lost': w, 'top': top})
    out[run] = {'pairs': pairs, 'n': len(pairs),
                'mean_edit_best': (sum(p['top'][0]['edit'] for p in pairs) / len(pairs)) if pairs else None}
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
