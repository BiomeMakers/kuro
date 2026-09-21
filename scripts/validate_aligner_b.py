"""Validate the syllabic aligner on Linear B with the values hidden.

The one test that decides whether kuro/aligner.py is a decipherment instrument: Linear B's
values are known, so hide them, give the aligner the Greek vocabulary and five anchors as
Ventris had his place names, and count how many of the remaining values it recovers.
Chance is one in 85 per sign. Run: PYTHONPATH=. python3 scripts/validate_aligner_b.py
"""
import json
import sys
import time
from collections import Counter

from kuro import aligner, mixed


def run_one(steps, sample, n_signs, n_anchors, seed):
    """One validation run; returns (recovered, free, aligned, found, truth)."""
    data = json.load(open('data/raw/linearb/inscriptions_B.json'))
    docs = [(n, it.get('transliteratedWords') or []) for n, it in data]
    corpus = mixed.MixedCorpus(docs)
    units = [u for u in corpus.units if all(mixed.split_syllable(s) for s in u)]
    freq = Counter(s for u in units for s in u)
    top = [s for s, _ in freq.most_common(n_signs)]
    units = [u for u in units if all(s in top for s in u)]
    code = {s: 'S%02d' % i for i, s in enumerate(top)}
    hidden = [tuple(code[s] for s in u) for u in units]
    truth = {code[s]: s for s in top}
    anchors = {code[s]: s for s in top[:n_anchors]}
    vocab = [e['transcription'].lower()
             for e in json.load(open('data/raw/linearb/lexicon_B.json'))]
    al = aligner.Aligner(hidden, vocab, fixed=anchors, threshold=1.0, seed=seed)
    found, score = al.anneal(steps=steps, sample=sample)
    recovered = aligner.Aligner.recovered(found, truth) - n_anchors
    return recovered, n_signs - n_anchors, score, found, truth


def main(steps=3000, sample=200, n_signs=30, anchor_counts=(3, 5, 8, 12), seed=1):
    """The curve: how many anchors the aligner needs before it recovers the rest.

    Linear A has 16 anchored signs of 110 (15%), 23 with the Wanderwoerter (21%). On the 30
    signs tested here those proportions are 4.5 and 6.3 anchors. The curve says whether
    Linear A's anchors sit above or below the threshold at which the method takes off.
    """
    print(f'Linear B, {n_signs} signs, {steps} steps, {sample} units per step, seed {seed}')
    print(f'{"anchors":>8} {"free":>5} {"recovered":>10} {"aligned":>8} {"chance":>7}  {"seconds":>8}')
    results = []
    for n_anchors in anchor_counts:
        started = time.time()
        rec, free, aligned, found, truth = run_one(steps, sample, n_signs, n_anchors, seed)
        secs = time.time() - started
        print(f'{n_anchors:>8} {free:>5} {rec:>10} {aligned:>8} {free / 85:>7.1f}  {secs:>8.0f}', flush=True)
        results.append({'anchors': n_anchors, 'free': free, 'recovered': rec,
                        'aligned': aligned, 'found': found, 'truth': truth})
    json.dump({'steps': steps, 'sample': sample, 'signs': n_signs, 'seed': seed,
               'runs': results}, open('data/derived/aligner_b_curve.json', 'w'), indent=1)
    print('\nwritten to data/derived/aligner_b_curve.json')
    print('Linear A sits at 4.5 anchors on this scale (16 of 110), 6.3 with the Wanderwoerter.')


if __name__ == '__main__':
    steps = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    sample = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    anchors = tuple(int(x) for x in sys.argv[3].split(',')) if len(sys.argv) > 3 else (3, 5, 8, 12)
    main(steps=steps, sample=sample, anchor_counts=anchors)
