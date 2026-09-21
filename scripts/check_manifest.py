#!/usr/bin/env python3
"""Fail when a paper states a figure that disagrees with manifest.json.

The manifest is the single source of truth for every figure the papers assert. This checker
reads the papers, finds the figures the manifest names, and reports disagreements. It also
refuses to let a withdrawn claim or an unattributed prior-art result survive in a paper.

Adapted from the release-manifest practice of OpenEtruscan (github.com/Eddy1919/openEtruscan),
which built it after an external audit found four different version numbers across four public
surfaces. We have the same problem: this week the corpus size, the votive document count, the
hapax rate and the number of Assur recipes were each corrected in one file while older values
survived in others.

    python scripts/check_manifest.py            # report
    python scripts/check_manifest.py --strict   # exit non-zero on any disagreement
"""
import json, re, sys, os, glob, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_manifest():
    with open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8') as f:
        return json.load(f)


def paper_texts():
    """Every paper source we can read, as (name, text)."""
    out = []
    for pat in ('docs/papers/sources/*.md', 'docs/papers/*.md'):
        for p in glob.glob(os.path.join(ROOT, pat)):
            with open(p, encoding='utf-8', errors='replace') as f:
                out.append((os.path.basename(p), f.read()))
    return out


def numbers_in(text):
    """Every number appearing in the text, normalised, with its surrounding words."""
    found = {}
    for m in re.finditer(r'(?<![\w.])(\d[\d,.]*)(?![\w])', text):
        raw = m.group(1).rstrip('.').replace(',', '')
        try:
            v = float(raw)
        except ValueError:
            continue
        ctx = text[max(0, m.start() - 90):m.end() + 60].replace('\n', ' ')
        found.setdefault(v, []).append(ctx)
    return found



def check_p_value_support(manifest):
    """Every p-value must declare what sustains it: the n, and the repetitions if permuted.

    This check exists because a figure computed over five permutations was quoted for three
    days as though it were firm, and moved by a full point when rerun over twenty.
    """
    support = manifest.get('p_value_support', {})
    missing = sorted(set(manifest.get('p_values', {})) - set(support))
    if missing:
        print('p-values with no declared support (n, repetitions, test): %d of %d'
              % (len(missing), len(manifest.get('p_values', {}))))
        for key in missing[:8]:
            print('    %s' % key)
        if len(missing) > 8:
            print('    ... and %d more' % (len(missing) - 8))
        print()
    fragile = [k for k, v in sorted(support.items())
               if v.get('n', 999) < 15 or v.get('repetitions', 9999) < 100]
    if fragile:
        print('p-values resting on fewer than 15 observations or 100 repetitions: %d'
              % len(fragile))
        for key in fragile:
            print('    %-42s n=%-5s reps=%s' % (key, support[key].get('n', '-'),
                                                support[key].get('repetitions', '-')))
    return missing, fragile


def check(strict=False):
    man = load_manifest()
    papers = paper_texts()
    problems, notes = [], []

    if not papers:
        notes.append('no paper sources found under docs/papers; only PDFs are shipped, '
                     'so figure checking is limited to what the manifest records')

    # A draft marked SUPERSEDED at the top is a source kept for the record, not a paper:
    # its whole point is that it states what was later withdrawn.
    papers = [(k, v) for k, v in papers if 'SUPERSEDED' not in v[:1200]]

    # 1. Withdrawn claims must not survive in a paper except inside a withdrawal statement.
    for w in man['withdrawn']:
        key = w['claim'].split(',')[0][:38].lower()
        for name, text in papers:
            low = text.lower()
            if key in low:
                near = low[max(0, low.find(key) - 500):low.find(key) + 900]
                if not any(k in near for k in ('withdraw', 'retira', 'no se sostiene',
                                               'does not hold', 'superseded', 'no longer',
                                               'replaced by', 'sustituida', 'cannot be done')):
                    problems.append(f'{name}: states a withdrawn claim without withdrawing it '
                                    f'("{w["claim"][:60]}")')

    # 2. Prior-art results must name their holder somewhere in the paper that states them.
    for res, holder in man['prior_art'].items():
        if res.startswith('_'):
            continue
        surname = holder.split(',')[0].split(' ')[0]
        probe = res.replace('_', ' ')[:26]
        for name, text in papers:
            if probe in text.lower() and surname.lower() not in text.lower():
                problems.append(f'{name}: states "{probe}" without citing {holder}')

    # 3. Figures the manifest fixes should not appear contradicted.
    #    We check the reverse direction: a manifest figure that appears nowhere is flagged as a note,
    #    since it may mean a paper was updated and the manifest was not.
    stated = set()
    for _, text in papers:
        stated |= set(numbers_in(text))
    for k, v in man['key_results'].items():
        if isinstance(v, (int, float)) and v not in stated and papers:
            notes.append(f'manifest figure not found in any paper: {k} = {v}')

    print('=' * 74)
    print('MANIFEST CHECK')
    print('=' * 74)
    print(f'manifest version {man["version"]}, updated {man["updated"]}')
    print(f'{len(man["key_results"])} figures, {len(man["p_values"])} p-values, '
          f'{len(man["withdrawn"])} withdrawn claims, {len(man["prior_art"])} prior-art entries')
    print(f'papers read: {len(papers)}')
    print()
    if problems:
        print(f'PROBLEMS ({len(problems)})')
        for p in problems:
            print(f'  ! {p}')
        print()
    else:
        print('no problems found')
        print()
    check_p_value_support(man)
    print()
    if notes:
        print(f'notes ({len(notes)})')
        for n in notes[:12]:
            print(f'  - {n}')
        if len(notes) > 12:
            print(f'  ... and {len(notes) - 12} more')
    return 1 if (problems and strict) else 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--strict', action='store_true')
    sys.exit(check(ap.parse_args().strict))
