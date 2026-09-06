import math, random, re, collections, statistics as st
import numpy as np
from .nulls import shuffle_labels, shuffle_within_strata, curveball, shuffle_syllables
from .corpus import is_number, FRACTIONS

def _jsd(a, b):
    ca, cb = collections.Counter(a), collections.Counter(b); keys = set(ca) | set(cb)
    p = [ca[k] / len(a) for k in keys]; q = [cb[k] / len(b) for k in keys]; m = [(x + y) / 2 for x, y in zip(p, q)]
    kl = lambda u, v: sum(x * math.log2(x / y) for x, y in zip(u, v) if x > 0)
    return 0.5 * kl(p, m) + 0.5 * kl(q, m)

def profile_distance(groupA, groupB, unit='syllable', size=None, n_null=200, rng=random):
    """Jensen-Shannon distance between two groups of documents at matched size, with (1) the floor
    (two samples of A) and (2) a document-level label-shuffle null. Returns dict."""
    def units(docs):
        out = []
        for d in docs:
            for w in d.words():
                out += (w.split('-') if unit == 'syllable' else [w])
        return out
    ua, ub = units(groupA), units(groupB); k = min(size or 10**9, len(ua), len(ub))
    obs = st.mean(_jsd(rng.sample(ua, k), rng.sample(ub, k)) for _ in range(30))
    floor = st.mean(_jsd(rng.sample(ua, k), rng.sample(ua, k)) for _ in range(30)) if len(ua) >= 2 * k else None
    alld = list(groupA) + list(groupB); labs = ['A'] * len(groupA) + ['B'] * len(groupB); null = []
    for _ in range(n_null):
        rng.shuffle(labs)
        a = units([d for d, l in zip(alld, labs) if l == 'A']); b = units([d for d, l in zip(alld, labs) if l == 'B'])
        kk = min(k, len(a), len(b))
        if kk >= 20: null.append(_jsd(rng.sample(a, kk), rng.sample(b, kk)))
    return dict(observed=obs, floor=floor, null_mean=st.mean(null), null_max=max(null),
                p=sum(1 for x in null if x >= obs) / len(null), units=k)

def affix_pairs(vocab, affix, kind='prefix', n_null=300, rng=random):
    """Root/derivative pairs for an affix (e.g. 'ka' prefix, 'ja' suffix) against a shuffled-syllable null."""
    vs = set(vocab)
    def pairs(vset):
        if kind == 'prefix':
            return [(w, w[len(affix) + 1:]) for w in vset if w.startswith(affix + '-') and w[len(affix) + 1:] in vset and '-' in w[len(affix) + 1:]]
        return [(w, w[:-len(affix) - 1]) for w in vset if w.endswith('-' + affix) and w[:-len(affix) - 1] in vset and '-' in w[:-len(affix) - 1]]
    obs = pairs(vs); null = [len(pairs(set(shuffle_syllables(list(vocab), rng)))) for _ in range(n_null)]
    return dict(pairs=obs, observed=len(obs), null_mean=st.mean(null), null_max=max(null),
                p=sum(1 for x in null if x >= len(obs)) / n_null)

def family_positions(strings, min_len=3, min_count=15, lift=1.8, p_max=1e-6):
    """Signs concentrated in initial / final position of long sign-strings (Proto-Elamite frame test)."""
    from math import comb
    long = [s for s in strings if len(s) >= min_len]
    allpos = collections.Counter(x for s in long for x in s); totall = sum(allpos.values())
    out = {}
    for label, cnt in (('final', collections.Counter(s[-1] for s in long)), ('initial', collections.Counter(s[0] for s in long))):
        tot = sum(cnt.values()); res = []
        for s, k in cnt.most_common(80):
            exp = allpos[s] * tot / totall
            p = sum(comb(allpos[s], x) * comb(totall - allpos[s], tot - x) for x in range(k, min(tot, allpos[s]) + 1)) / comb(totall, tot)
            if k >= min_count and k / exp >= lift and p < p_max: res.append((s, k, round(k / exp, 1), p))
        out[label] = res
    return out

def metacommunity(docs, min_docs=8, n_null=150, z_pos=4, rng=random):
    """Document x string presence matrix; co-occurrence and co-exclusion against a curveball null."""
    present = collections.Counter(t for d in docs for t in set(d.words()))
    cols = [t for t, c in present.items() if c >= min_docs]; idx = {t: i for i, t in enumerate(cols)}
    M = np.zeros((len(docs), len(cols)), dtype=np.int8)
    for i, d in enumerate(docs):
        for t in set(d.words()):
            if t in idx: M[i, idx[t]] = 1
    M = M[M.sum(1) >= 2]
    obs = M.T.astype(int) @ M.astype(int)
    nulls = np.array([(lambda B: B.T.astype(int) @ B.astype(int))(curveball(M, rng=rng)) for _ in range(n_null)])
    mean, sd = nulls.mean(0), nulls.std(0) + 1e-9; z = (obs - mean) / sd; n = len(cols)
    pos = [(cols[i], cols[j], int(obs[i, j]), float(mean[i, j])) for i in range(n) for j in range(i + 1, n) if z[i, j] > z_pos and obs[i, j] >= 5]
    neg = [(cols[i], cols[j], float(mean[i, j])) for i in range(n) for j in range(i + 1, n) if obs[i, j] == 0 and mean[i, j] >= 3 and (nulls[:, i, j] == 0).mean() < 0.01]
    return dict(shape=M.shape, cooccurrence=pos, coexclusion=neg)

def monopolies(docs, type_of, min_count=4):
    """Strings attested >= min_count times and only in documents of one type."""
    bytype = collections.defaultdict(collections.Counter); allc = collections.Counter()
    for d in docs:
        t = type_of(d)
        for w in d.words(): bytype[t][w] += 1; allc[w] += 1
    return {t: [w for w, c in cnt.items() if c >= min_count and allc[w] == c] for t, cnt in bytype.items()}

def confounder_jaccard(docs, factor_a, factor_b, n_null=300, rng=random):
    """Vocabulary Jaccard between document pairs, split by same/different factor_a and factor_b;
    effect of each factor within strata of the other, with within-stratum permutation nulls."""
    docs = [d for d in docs if factor_a(d) and factor_b(d) and len(set(d.words())) >= 2]
    names = list(range(len(docs))); W = [set(d.words()) for d in docs]
    A = {i: factor_a(docs[i]) for i in names}; B = {i: factor_b(docs[i]) for i in names}
    pairs = [(i, j) for i in names for j in names if i < j]
    def cells(la, lb):
        c = collections.defaultdict(list)
        for i, j in pairs: c[(la[i] == la[j], lb[i] == lb[j])].append(len(W[i] & W[j]) / len(W[i] | W[j]))
        return {k: st.mean(v) for k, v in c.items() if v}
    m = cells(A, B); g = lambda k: m.get(k, 0)
    eff_a_within_b = g((True, True)) - g((False, True)); eff_b_within_a = g((True, True)) - g((True, False))
    na, nb = [], []
    for _ in range(n_null):
        mm = cells(shuffle_within_strata(A, B, rng), B); na.append(mm.get((True, True), 0) - mm.get((False, True), 0))
        mm = cells(A, shuffle_within_strata(B, A, rng)); nb.append(mm.get((True, True), 0) - mm.get((True, False), 0))
    return dict(cells=m, effect_a_within_b=(eff_a_within_b, sum(1 for x in na if x >= eff_a_within_b) / n_null),
                effect_b_within_a=(eff_b_within_a, sum(1 for x in nb if x >= eff_b_within_a) / n_null), n_docs=len(docs))

def totals_check(doc, total_word='ku-ro'):
    """Sum quantities in each section before a total word and compare (fractions as Fractions)."""
    from fractions import Fraction as Fr
    FR = {'¹⁄₂': Fr(1, 2), '¹⁄₃': Fr(1, 3), '²⁄₃': Fr(2, 3), '¹⁄₄': Fr(1, 4), '³⁄₄': Fr(3, 4), '¹⁄₅': Fr(1, 5), '¹⁄₆': Fr(1, 6), '¹⁄₈': Fr(1, 8), '¹⁄₁₆': Fr(1, 16), '³⁄₈': Fr(3, 8)}
    toks = [t for t in doc.tokens if t not in ('|', '𐄁')]; sec = []; out = []; i = 0
    while i < len(toks):
        t = toks[i]
        if t.lower() == total_word:
            q = None; j = i + 1
            while j < len(toks) and (re.fullmatch(r'\d+', toks[j]) or toks[j] in FR):
                q = (q or Fr(0)) + (int(toks[j]) if re.fullmatch(r'\d+', toks[j]) else FR[toks[j]]); j += 1
            out.append(dict(section_sum=sum(sec, Fr(0)), total=q, n=len(sec), exact=(q is not None and sum(sec, Fr(0)) == q))); sec = []; i = j
        else:
            if re.fullmatch(r'\d+', t): sec.append(Fr(int(t)))
            elif t in FR: sec.append(FR[t])
            i += 1
    return out

def form_screen(vocab, catalogue, match_fn, n_null=200, rng=random):
    """Form matches between a vocabulary and an external catalogue against a shuffled-syllable null."""
    hits = [(w, p) for w in vocab for p in catalogue if match_fn(w, p)]
    null = [sum(1 for w in shuffle_syllables(list(vocab), rng) for p in catalogue if match_fn(w, p)) for _ in range(n_null)]
    return dict(hits=hits, observed=len(hits), null_mean=st.mean(null), null_max=max(null), p=sum(1 for x in null if x >= len(hits)) / n_null)

def hapax_by_length(docs, counted_only=True):
    """Singleton rate of sign-strings by number of signs (name / commodity partition)."""
    strings = collections.Counter(); bylen = collections.defaultdict(list)
    for d in docs:
        for w in d.words(): strings[w] += 1
    for d in docs:
        for w in d.words(): bylen[min(len(w.split()), 5) if ' ' in w else min(w.count('-') + 1, 5)].append(strings[w] == 1)
    return {L: (round(st.mean(v), 2), len(v)) for L, v in sorted(bylen.items())}
