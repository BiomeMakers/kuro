"""The decipherment objective of Luo et al. (2021), for a segmented CV syllabary.

Their model and mine differed in more than a detail, and the difference is why mine
recovered nothing on Linear B. Theirs:

  - learns a *soft* distribution over character mappings, Pr(x|y) ∝ exp(E(x)·E(y)/T),
    optimised by gradient descent (their §3.2.1). Mine searched discrete permutations.
  - scores a span by the likelihood **summed over the whole known vocabulary**,
    Pr(x|z) = Σ_y max_a Π_τ Pr(x_{a_τ}|y_τ), normalised by span length (their eq. 2 and 7).
    Mine counted how many units found *some* word below a threshold, which is maximised
    by false assignments because almost any mapping aligns something.
  - adds Ω_loss = Σ_{c_L} (Σ_{c_K} Pr(c_L|c_K) − 1)², discouraging the disappearance of a
    sound (their §3.3). Mine had no such term.

One part of their model is not needed here. Linear A and Linear B mark word division, so
the latent segmentation variable Z is observed and the coverage term Ω_cov with it. What
remains is the mapping, the length-normalised summed likelihood, and sound preservation.

The lost side is a CV syllabary, so a lost sign's embedding is the concatenation of a
consonant and a vowel embedding, and the known side is likewise decomposed. This is the
extension their note 3 leaves open.
"""
import numpy as np

from kuro.mixed import CONSONANTS, VOWELS, split_syllable

TEMPERATURE = 0.2       # their T
LAMBDA_LOSS = 1.0       # their λ_loss
INSERTION = 0.05        # their α, the penalty on insertions


def feature_vector(value):
    """A CV value as a binary feature vector: consonant features then vowel features."""
    parts = split_syllable(value)
    if parts is None:
        return None
    c, v = CONSONANTS[parts[0]], VOWELS[parts[1]]
    vec = [c['voice']]
    for place in ('labial', 'alveolar', 'velar', 'labiovelar', 'palatal', 'glottal', 'none'):
        vec.append(1 if c['place'] == place else 0)
    for manner in ('stop', 'nasal', 'liquid', 'fricative', 'glide', 'none'):
        vec.append(1 if c['manner'] == manner else 0)
    for height in ('high', 'mid', 'low'):
        vec.append(1 if v['height'] == height else 0)
    for back in ('front', 'central', 'back'):
        vec.append(1 if v['back'] == back else 0)
    vec.append(v['round'])
    return np.array(vec, dtype=float)


VALUES = [c + v for c in CONSONANTS for v in VOWELS if split_syllable(c + v)]
FEATURES = np.stack([feature_vector(v) for v in VALUES])
VALUE_INDEX = {v: i for i, v in enumerate(VALUES)}


class Decipher:
    """Soft character mapping between lost signs and known syllable values.

    W[i, j] is the unnormalised affinity of lost sign i for known value j. The mapping
    distribution is the row-wise softmax at temperature T. Signs whose value is known
    (anchors) have their row clamped.
    """

    def __init__(self, signs, vocabulary, anchors=None, seed=0, temperature=TEMPERATURE):
        self.signs = list(signs)
        self.index = {s: i for i, s in enumerate(self.signs)}
        self.T = temperature
        self.anchors = dict(anchors or {})
        rng = np.random.default_rng(seed)
        # initialise each lost sign in the phonetic space, as their eq. 4 does with a
        # weighted sum of known embeddings
        self.W = rng.normal(0, 0.3, size=(len(self.signs), len(VALUES)))
        for s, v in self.anchors.items():
            if s in self.index and v in VALUE_INDEX:
                self.W[self.index[s]] = -20.0
                self.W[self.index[s], VALUE_INDEX[v]] = 20.0
        self.vocab = []
        for word in vocabulary:
            syls = [s for s in word.lower().split('-') if s in VALUE_INDEX]
            if len(syls) == len(word.split('-')) and 2 <= len(syls) <= 6:
                self.vocab.append([VALUE_INDEX[s] for s in syls])
        # Index by length: a word can only align to a unit of nearly its length, so the
        # sum over the vocabulary need not touch words that cannot contribute.
        self.by_len = {}
        for w in self.vocab:
            self.by_len.setdefault(len(w), []).append(w)

    def mapping(self):
        """Pr(known value | lost sign): row-wise softmax of W/T."""
        z = self.W / self.T
        z = z - z.max(axis=1, keepdims=True)
        e = np.exp(z)
        return e / e.sum(axis=1, keepdims=True)

    def span_likelihood(self, unit, P):
        """Pr(x|z) = Σ_y max_a Π_τ Pr(x_{a_τ}|y_τ), their eq. 2, length-normalised.

        max_a over monotonic alignments is a Viterbi edit-distance recursion in log space.
        """
        rows = [P[self.index[s]] for s in unit]
        n = len(rows)
        total = 0.0
        candidates = []
        for L in (n - 1, n, n + 1):
            candidates.extend(self.by_len.get(L, ()))
        for word in candidates:
            m = len(word)
            NEG = -1e9
            # a word whose first syllable is improbable under every sign of the unit
            # cannot contribute meaningfully; skip it before running the recursion
            if max(rows[k][word[0]] for k in range(n)) < 1e-4:
                continue
            prev = [0.0 if j == 0 else NEG for j in range(n + 1)]
            for t in range(m):
                cur = [NEG] * (n + 1)
                for k in range(1, n + 1):
                    sub = prev[k - 1] + np.log(rows[k - 1][word[t]] + 1e-12)
                    ins = (cur[k - 1] + np.log(rows[k - 1][word[t]] + 1e-12)
                           + np.log(INSERTION)) if k > 1 else NEG
                    cur[k] = max(sub, ins)
                prev = cur
            if prev[n] > NEG / 2:
                total += np.exp(prev[n] / n)      # their φ, normalised by span length
        return total

    def quality(self, units, P=None):
        """Σ_x φ(x): their Q, with segmentation observed."""
        P = self.mapping() if P is None else P
        return float(sum(self.span_likelihood(u, P) for u in units))

    def sound_loss(self, P=None):
        """Ω_loss = Σ_{c_L} (Σ_{c_K} Pr(c_L|c_K) − 1)², their sound-preservation term."""
        P = self.mapping() if P is None else P
        column_mass = P.sum(axis=0)
        return float(((column_mass - 1.0) ** 2).sum())

    def objective(self, units, P=None):
        P = self.mapping() if P is None else P
        return self.quality(units, P) - LAMBDA_LOSS * self.sound_loss(P)

    def best_values(self, P=None):
        P = self.mapping() if P is None else P
        return {s: VALUES[int(P[i].argmax())] for s, i in self.index.items()}


    def span_likelihood_grad(self, unit, P):
        """Pr(x|z) and its gradient with respect to P, for one unit.

        The Viterbi recursion picks, for each known word, one monotonic alignment. Along
        that alignment the span probability is a product of entries of P, so the gradient
        of its length-normalised value is that value times the reciprocal of each entry
        used. This is backpropagation through the dynamic program, done by hand.
        """
        rows = [self.index[s] for s in unit]
        n = len(rows)
        total = 0.0
        grad = np.zeros_like(P)
        candidates = []
        for L in (n - 1, n, n + 1):
            candidates.extend(self.by_len.get(L, ()))
        for word in candidates:
            m = len(word)
            if max(P[rows[k], word[0]] for k in range(n)) < 1e-4:
                continue
            NEG = -1e9
            prev = [0.0 if j == 0 else NEG for j in range(n + 1)]
            back = [[None] * (n + 1) for _ in range(m)]
            for t in range(m):
                cur = [NEG] * (n + 1)
                for k in range(1, n + 1):
                    lp = np.log(P[rows[k - 1], word[t]] + 1e-12)
                    sub = prev[k - 1] + lp
                    ins = (cur[k - 1] + lp + np.log(INSERTION)) if k > 1 else NEG
                    if sub >= ins:
                        cur[k], back[t][k] = sub, ('sub', k - 1)
                    else:
                        cur[k], back[t][k] = ins, ('ins', k - 1)
                prev = cur
            if prev[n] <= NEG / 2:
                continue
            phi = np.exp(prev[n] / n)
            total += phi
            # walk the chosen alignment back, accumulating 1/P for each entry used
            k, t = n, m - 1
            while t >= 0 and k >= 1:
                grad[rows[k - 1], word[t]] += phi / (n * (P[rows[k - 1], word[t]] + 1e-12))
                kind, k_prev = back[t][k]
                k = k_prev
                if kind == 'sub':
                    t -= 1
                if k == 0:
                    break
        return total, grad

    def objective_grad(self, units, P=None):
        """The objective and its gradient with respect to W, through the softmax."""
        P = self.mapping() if P is None else P
        total = 0.0
        dP = np.zeros_like(P)
        for u in units:
            q, g = self.span_likelihood_grad(u, P)
            total += q
            dP += g
        # sound preservation: d/dP of Σ_j (Σ_i P[i,j] − 1)²
        column_mass = P.sum(axis=0)
        loss = float(((column_mass - 1.0) ** 2).sum())
        dP -= LAMBDA_LOSS * 2.0 * (column_mass - 1.0)[None, :]
        # softmax Jacobian: dW = (dP * P − P * (dP * P).sum(axis=1, keepdims=True)) / T
        dPP = dP * P
        dW = (dPP - P * dPP.sum(axis=1, keepdims=True)) / self.T
        for s in self.anchors:
            if s in self.index:
                dW[self.index[s]] = 0.0
        return total - LAMBDA_LOSS * loss, dW

    def ascend(self, units, steps=150, lr=0.5, batch=40, seed=0, verbose=False):
        """Gradient ascent on the objective, the way the paper trains its model."""
        rng = np.random.default_rng(seed)
        momentum = np.zeros_like(self.W)
        best, best_W = -np.inf, self.W.copy()
        for step in range(steps):
            idx = rng.choice(len(units), min(batch, len(units)), replace=False)
            sample = [units[i] for i in idx]
            value, dW = self.objective_grad(sample)
            momentum = 0.9 * momentum + dW
            self.W += lr * momentum
            self.W = np.clip(self.W, -20.0, 20.0)
            if value > best:
                best, best_W = value, self.W.copy()
            if verbose and step % 25 == 0:
                print('    step %3d  objective %.3f' % (step, value), flush=True)
        self.W = best_W
        return self.best_values(), best

    def fit(self, units, steps=200, lr=2.0, batch=60, seed=0):
        """Gradient ascent on the objective, by finite differences on W.

        Their training is backpropagation through the dynamic program; without a
        differentiable framework the same objective is optimised by sampling coordinate
        perturbations, which is slower but optimises the same quantity.
        """
        rng = np.random.default_rng(seed)
        free = [i for i, s in enumerate(self.signs) if s not in self.anchors]
        sample = units if len(units) <= batch else list(rng.choice(len(units), batch))
        def score(idx=None):
            us = units if idx is None else [units[i] for i in idx]
            return self.objective(us)
        idx = rng.choice(len(units), min(batch, len(units)), replace=False)
        cur = score(idx)
        for step in range(steps):
            i = int(rng.choice(free))
            j = int(rng.integers(len(VALUES)))
            delta = rng.normal(0, lr)
            self.W[i, j] += delta
            new = score(idx)
            if new >= cur:
                cur = new
            else:
                self.W[i, j] -= delta
            if step % 25 == 24:
                idx = rng.choice(len(units), min(batch, len(units)), replace=False)
                cur = score(idx)
        return self.best_values(), cur
