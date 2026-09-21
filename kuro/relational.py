"""Alignment by relational structure: Gromov-Wasserstein between sign inventories.

Every comparison of Minoan with a candidate language so far has gone through the shape of
the signs, whether by phonotactics under the Linear B values or by edit distance between
transliterations. Both inherit the transcription. Gromov-Wasserstein does not look at the
signs at all: it compares how the distances between signs inside one inventory relate to the
distances between signs inside the other (Alvarez-Melis and Jaakkola 2018). Two inventories
align if their internal geometry has the same shape, whatever the signs are called.

The distributional profile of a sign is what precedes it, what follows it and where it stands
in the word. The coupling is found by entropic Gromov-Wasserstein with Sinkhorn projections,
implemented here so the package keeps no optimal-transport dependency.

The positive control is available for free: Linear A and Linear B are transliterated with the
same sign names, so the correct coupling is the identity on the shared names, and accuracy can
be measured without anybody supplying an answer.
"""
import numpy as np
from collections import Counter, defaultdict


def sign_profiles(words, signs=None, smoothing=0.5):
    """words: list of sign sequences. Returns (signs, matrix) with, per sign, the distribution
    of the sign before, the sign after, and three positional features."""
    signs = sorted({s for w in words for s in w}) if signs is None else list(signs)
    idx = {s: i for i, s in enumerate(signs)}
    n = len(signs)
    before = np.full((n, n + 1), smoothing)
    after = np.full((n, n + 1), smoothing)
    pos = np.zeros((n, 3))
    count = np.zeros(n)
    for w in words:
        for j, s in enumerate(w):
            if s not in idx:
                continue
            i = idx[s]
            count[i] += 1
            before[i, idx[w[j - 1]] if j > 0 and w[j - 1] in idx else n] += 1
            after[i, idx[w[j + 1]] if j + 1 < len(w) and w[j + 1] in idx else n] += 1
            pos[i, 0] += (j == 0)
            pos[i, 1] += (j == len(w) - 1)
            pos[i, 2] += j / max(len(w) - 1, 1)
    before /= before.sum(1, keepdims=True)
    after /= after.sum(1, keepdims=True)
    pos /= np.maximum(count[:, None], 1)
    return signs, np.hstack([before, after, pos]), count


def cosine_distance(M):
    N = M / np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-12)
    return np.clip(1 - N @ N.T, 0, 2)


def entropic_gw(D1, D2, p=None, q=None, epsilon=0.005, outer=200, inner=100, seed=0):
    """Entropic Gromov-Wasserstein coupling between two distance matrices."""
    n, m = len(D1), len(D2)
    p = np.ones(n) / n if p is None else p / p.sum()
    q = np.ones(m) / m if q is None else q / q.sum()
    rng = np.random.default_rng(seed)
    T = np.outer(p, q) * (1 + 0.01 * rng.standard_normal((n, m)))
    T = np.clip(T, 1e-12, None); T /= T.sum()
    cst = (D1 ** 2) @ np.outer(p, np.ones(m)) + np.outer(np.ones(n), q) @ (D2 ** 2).T
    for _ in range(outer):
        grad = cst - 2 * D1 @ T @ D2.T
        K = np.exp(-grad / epsilon)
        K = np.clip(K, 1e-300, None)
        u = np.ones(n) / n
        for _ in range(inner):
            v = q / np.maximum(K.T @ u, 1e-300)
            u = p / np.maximum(K @ v, 1e-300)
        T = u[:, None] * K * v[None, :]
    return T


def gw_cost(D1, D2, T):
    p, q = T.sum(1), T.sum(0)
    cst = (D1 ** 2) @ np.outer(p, np.ones(len(D2))) + np.outer(np.ones(len(D1)), q) @ (D2 ** 2).T
    return float(np.sum((cst - 2 * D1 @ T @ D2.T) * T))


def align(words_a, words_b, epsilon=0.005, seed=0, min_count=2):
    """Returns the coupling, the signs kept on each side and the Gromov-Wasserstein cost."""
    sa, Ma, ca = sign_profiles(words_a)
    sb, Mb, cb = sign_profiles(words_b)
    ka = [i for i, c in enumerate(ca) if c >= min_count]
    kb = [i for i, c in enumerate(cb) if c >= min_count]
    sa = [sa[i] for i in ka]; sb = [sb[i] for i in kb]
    D1 = cosine_distance(Ma[ka][:, :]); D2 = cosine_distance(Mb[kb][:, :])
    pa = ca[ka] / ca[ka].sum(); pb = cb[kb] / cb[kb].sum()
    T = entropic_gw(D1, D2, pa, pb, epsilon=epsilon, seed=seed)
    return {'coupling': T, 'signs_a': sa, 'signs_b': sb, 'cost': gw_cost(D1, D2, T)}


def accuracy_on_shared_names(result):
    """With Linear A and Linear B named alike, the correct coupling is the identity."""
    T, sa, sb = result['coupling'], result['signs_a'], result['signs_b']
    shared = [s for s in sa if s in sb]
    if not shared:
        return None
    hit = 0
    for s in shared:
        best = sb[int(np.argmax(T[sa.index(s)]))]
        hit += (best == s)
    return {'shared': len(shared), 'correct': hit, 'accuracy': hit / len(shared)}
