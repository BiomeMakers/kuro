#!/usr/bin/env python3
"""Read NeuroDecipher checkpoints and write, for each lost word, its best matches.
Run inside the NeuroDecipher folder, with its venv active:
    python nd_extract.py log/09-11 > pairs13.json
The checkpoint stores {'lost_forms': [...], 'known_forms': [...], 'flow': tensor}.
"""
import sys, os, glob, json, torch

K = 5
out = {}
for ck in sorted(glob.glob(os.path.join(sys.argv[1], '*', 'saved.latest'))):
    run = os.path.basename(os.path.dirname(ck))
    try:
        st = torch.load(ck, map_location='cpu', weights_only=False)
    except Exception as e:
        out[run] = {'error': 'load: ' + str(e)[:120]}; continue
    fl = st.get('flow', st)
    try:
        lost = list(fl['lost_forms']); known = list(fl['known_forms']); T = fl['flow']
    except Exception as e:
        out[run] = {'error': 'fields: ' + str(list(fl.keys()))[:160]}; continue
    for attr in ('tensor', 'data', 't', '_t', 'value', 'values'):   # MagicTensor wraps the tensor
        if not isinstance(T, torch.Tensor) and hasattr(T, attr):
            cand = getattr(T, attr)
            if isinstance(cand, torch.Tensor): T = cand; break
    if not isinstance(T, torch.Tensor):
        out[run] = {'error': 'flow type ' + type(T).__name__ + ' attrs ' + str([a for a in dir(T) if not a.startswith('_')])[:400]}; continue
    if T.is_sparse: T = T.to_dense()
    T = T.float()
    if T.shape[0] != len(lost) and T.shape[1] == len(lost): T = T.t()
    k = min(K, T.shape[1])
    vals, idx = T.topk(k, dim=1)
    pairs = []
    for i, w in enumerate(lost):
        top = [{'known': str(known[int(j)]), 'flow': float(v)} for v, j in zip(vals[i], idx[i]) if float(v) > 0]
        if top: pairs.append({'lost': str(w), 'top': top})
    out[run] = {'n_lost': len(lost), 'n_known': len(known), 'matched': len(pairs), 'pairs': pairs}
json.dump(out, sys.stdout, ensure_ascii=False)
