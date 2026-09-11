#!/usr/bin/env python3
"""Download the candidate-language corpora that CDLI holds, into data/raw/candidates/.

    python scripts/fetch_candidates.py            # all four
    python scripts/fetch_candidates.py sumerian   # one

CDLI (cdli.earth) publishes its transliterations as bulk files under CC BY. The four languages
below are the ones proposed for, or plausibly related to, Minoan and held there in quantity:
Sumerian (isolate, huge corpus), Akkadian (East Semitic), Elamite (isolate), Hurrian (Hurro-Urartian,
the candidate of van Soesbergen). Each is filtered by CDLI's language field from the full ATF dump.

Nothing downloaded here is redistributed with the package: data/raw/ is in .gitignore. The
provenance and licence are written next to each file.
"""
import os, sys, re, json, urllib.request, gzip, io

OUT = 'data/raw/candidates'
# CDLI's bulk ATF: a single large file with a #atf: lang tag per text. This URL is the documented
# bulk export; if it moves, cdli.earth/downloads lists the current one.
BULK = 'https://github.com/cdli-gh/data/raw/master/cdliatf_unblocked.atf'
LANGS = {'sumerian': 'sux', 'akkadian': 'akk', 'elamite': 'elx', 'hurrian': 'xhu'}


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'kuro/1.0'})
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    if url.endswith('.gz'):
        data = gzip.decompress(data)
    return data.decode('utf-8', errors='replace')


def split_texts(atf):
    """CDLI ATF: each text begins with '&P' and carries '#atf: lang xxx'."""
    texts = re.split(r'(?m)^&', atf)
    out = []
    for t in texts:
        if not t.strip():
            continue
        m = re.search(r'#atf:\s*lang\s+(\w+)', t)
        lang = m.group(1) if m else None
        # transliteration lines: numbered, e.g. "1. a-na dumu ..."
        lines = [ln for ln in t.splitlines() if re.match(r'^\s*\d+[\'a-z]*\.\s', ln)]
        words = []
        for ln in lines:
            body = re.sub(r'^\s*\d+[\'a-z]*\.\s*', '', ln)
            body = re.sub(r'[\[\]#!?<>{}*]', '', body)      # editorial marks
            words += [w for w in body.split() if w and not w.startswith('$')]
        out.append({'id': t.split('\n', 1)[0].strip(), 'lang': lang, 'words': words})
    return out


def main(which):
    os.makedirs(OUT, exist_ok=True)
    print('fetching the CDLI bulk ATF (large; a minute or two)...')
    atf = fetch(BULK)
    texts = split_texts(atf)
    print(f'{len(texts)} texts in the dump')
    for name in which:
        code = LANGS[name]
        sel = [t for t in texts if t['lang'] == code and len(t['words']) >= 2]
        words = [w for t in sel for w in t['words']]
        path = os.path.join(OUT, f'{name}.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({'language': name, 'cdli_code': code, 'texts': len(sel),
                       'words': words,
                       'source': 'CDLI bulk ATF, github.com/cdli-gh/data, CC BY 4.0',
                       'note': 'transliteration only; editorial marks stripped; not redistributed'},
                      f, ensure_ascii=False)
        print(f'  {name:<10} {len(sel):>7} texts  {len(words):>9} words  -> {path}')


if __name__ == '__main__':
    args = [a.lower() for a in sys.argv[1:]] or list(LANGS)
    bad = [a for a in args if a not in LANGS]
    if bad:
        sys.exit(f'unknown: {bad}; choose from {list(LANGS)}')
    main(args)
