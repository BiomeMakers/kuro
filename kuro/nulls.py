import random, numpy as np

def shuffle_labels(labels, rng=random):
    v = list(labels.values()); rng.shuffle(v); return dict(zip(labels.keys(), v))

def shuffle_within_strata(labels, strata, rng=random):
    """Permute labels only among items that share the same stratum (e.g. type within hand)."""
    out = dict(labels); groups = {}
    for k, s in strata.items(): groups.setdefault(s, []).append(k)
    for ks in groups.values():
        v = [labels[k] for k in ks]; rng.shuffle(v)
        for k, x in zip(ks, v): out[k] = x
    return out

def curveball(M, iters=None, rng=random):
    """Fixed-margin randomisation of a binary presence matrix (Strona et al. 2014)."""
    M = M.copy(); R = [set(np.flatnonzero(M[i])) for i in range(M.shape[0])]
    iters = iters or 5 * M.shape[0]
    for _ in range(iters):
        i, j = rng.sample(range(M.shape[0]), 2); a, b = R[i], R[j]; ab, ba = a - b, b - a
        if not ab or not ba: continue
        pool = list(ab | ba); rng.shuffle(pool); k = len(ab)
        R[i] = (a & b) | set(pool[:k]); R[j] = (a & b) | set(pool[k:])
    B = np.zeros_like(M)
    for i, r in enumerate(R): B[i, list(r)] = 1
    return B

def shuffle_syllables(words, rng=random):
    """Permute syllables across words keeping each word's length (null for affix/root tests)."""
    syl = [w.split('-') for w in words]; pool = [s for ss in syl for s in ss]; rng.shuffle(pool)
    out = []; i = 0
    for ss in syl: out.append('-'.join(pool[i:i + len(ss)])); i += len(ss)
    return out
