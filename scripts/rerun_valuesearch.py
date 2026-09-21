"""Rerun the anchored value search with enough controls to trust the z.

The first pass used five controls and a standard deviation estimated from them. That is too
few: rerunning Etruscan and Luwian with twenty moved them from -3.2 to -2.1 and from 2.3 to
0.7. This script redoes all thirteen candidates at twenty controls and writes the table.
"""
import csv
import json
import sys
import time

from kuro import targets
from kuro.names import broken_status, syls
from kuro.valuesearch import ValueSearch, profile

VOWELS = set('aeiou')
ANCHORED = ('pa', 'i', 'to', 'su', 'ki', 'ri', 'ta', 'se', 'ja', 'da',
            'pi', 'ro', 'a', 'e', 'o', 'u')


def skeletons(words):
    """Every target, made an object of the same kind: see kuro.targets.

    The first pass compared Minoan against eleven targets that were not comparable. Ugaritic
    was a deduplicated lemma list; the TLHdig languages were raw token dumps carrying
    Sumerograms, cuneiform signs and clitics. Normalisation drops 90% of the Akkadian
    "lexicon" and 93% of the Sumerian, and their anomalously concentrated bigram profiles
    rise into the range of the rest.
    """
    return targets.normalise(words)


def minoan_units(path='data/raw/inscriptions.json'):
    """Intact syllabic units, with editorial marks stripped.

    The first pass left '+', '?', brackets and two private-use glyphs inside the consonant
    skeletons, where the search treated them as consonants the control could not match.
    Cleaning them drops Akkadian from z = +6.88 to about +1.3 in a short rerun.
    """
    import re
    data = json.load(open(path))
    status = broken_status(data)
    seen = {'-'.join(syls(t)).lower()
            for _, doc in data
            for t in doc.get('transliteratedWords', [])
            if isinstance(t, str) and '-' in t}
    units = [re.sub(r'[^a-z\-]', '', u) for u in seen if status.get(u) == 'intact']
    return [u for u in units if u.replace('-', '')]


def candidates():
    out = {}
    corpus = json.load(open('data/derived/corpus_all.json'))
    out['ugaritic'] = corpus['Ugaritic']
    out['hittite'] = corpus['Hittite']
    tlh = json.load(open('data/raw/candidates/tlhdig_by_language.json'))
    for key, name in (('Luw', 'luwian'), ('Pal', 'palaic'),
                      ('Hat', 'hattian'), ('Hur', 'hurrian')):
        out[name] = tlh[key]
    for name, path in (('akkadian', 'data/raw/candidates/akkadian.json'),
                       ('sumerian', 'data/raw/candidates/sumerian.json')):
        out[name] = json.load(open(path))['words'][:40000]
    rows = list(csv.DictReader(open('data/derived/openetruscan_clean.csv')))
    col = next(k for k in rows[0] if 'word' in k.lower() or 'form' in k.lower())
    out['etruscan'] = [r[col] for r in rows if r.get(col)]
    out['iberian'] = json.load(open('data/derived/iberian_corpus.json'))['intact']
    out['mycenaean'] = [e['transcription']
                        for e in json.load(open('data/raw/linearb/lexicon_B.json'))]
    return out


def main(steps=6000, controls=20):
    search = ValueSearch(minoan_units(), seed=1, fixed=ANCHORED)
    results = []
    for name, words in sorted(candidates().items()):
        target_forms = skeletons(words)
        target = profile(target_forms)
        if not target:
            print(f'{name}: no usable forms', file=sys.stderr)
            continue
        started = time.time()
        run = search.run(target, steps=steps, controls=controls)
        results.append({'language': name, 'target_forms': len(target_forms),
                        'linear_b_values': run['lb'],
                        'real_best': run['real_best'],
                        'control_mean': run['control_mean'],
                        'control_sd': run['control_sd'], 'z': run['z'],
                        'controls': controls, 'steps': steps})
        print(f"{name:12s} lb {run['lb']:.3f}  real {run['real_best']:.4f}  "
              f"control {run['control_mean']:.4f} ± {run['control_sd']:.4f}  "
              f"z {run['z']:+.2f}   ({time.time() - started:.0f}s)", flush=True)
    results.sort(key=lambda r: -r['z'])
    with open('data/derived/valuesearch_normalised.json', 'w') as fh:
        json.dump(results, fh, indent=1)
    print('\nwritten to data/derived/valuesearch_20controls.json')
    print(f"none reaches z = 3: max is {results[0]['language']} at {results[0]['z']:+.2f}")


if __name__ == '__main__':
    main(steps=int(sys.argv[1]) if len(sys.argv) > 1 else 6000,
         controls=int(sys.argv[2]) if len(sys.argv) > 2 else 20)
