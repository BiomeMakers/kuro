#!/usr/bin/env python3
"""Download the third-party corpora that kuro reads into data/raw/.

    python3 data/fetch.py            # everything reachable without credentials
    python3 data/fetch.py lineara    # one corpus

CDLI exports are paged from cdli.earth; the others come from public git repositories.
Nothing here is redistributed: each file is fetched from the project that publishes it.
"""
import os, sys, io, zipfile, time, urllib.request

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'raw')
os.makedirs(RAW, exist_ok=True)
UA = {'User-Agent': 'kuro/0.1 (research; https://github.com/BiomeMakers/kuro)'}

def _get(url, timeout=120):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()

def from_github_zip(repo, branch, members, targets):
    """Extract selected files from a GitHub repository archive."""
    data = _get(f'https://codeload.github.com/{repo}/zip/refs/heads/{branch}')
    z = zipfile.ZipFile(io.BytesIO(data))
    root = z.namelist()[0].split('/')[0]
    for m, t in zip(members, targets):
        with z.open(f'{root}/{m}') as f, open(os.path.join(RAW, t), 'wb') as o:
            o.write(f.read())
        print('  ->', t)

def cdli(period, atf_name, cat_name, page_size=1000, pause=1.0):
    """Page the cdli.earth search export for one period."""
    base = 'https://cdli.earth/search'
    def url(fmt, page, aspect=None):
        from urllib.parse import urlencode
        q = {'simple-value[0]': period, 'simple-field[0]': 'period', 'format': fmt, 'page': page}
        if aspect: q['aspect'] = aspect
        if page == 1: q['page-size'] = page_size
        return base + '?' + urlencode(q)
    for fmt, aspect, name, is_csv in (('atf', 'inscriptions', atf_name, False), ('csv', None, cat_name, True)):
        out = open(os.path.join(RAW, name), 'w', encoding='utf-8'); seen = 0; header = False
        for page in range(1, 300):
            try: txt = _get(url(fmt, page, aspect)).decode('utf-8', 'ignore')
            except Exception: break
            if is_csv:
                lines = [l for l in txt.splitlines() if l.strip()]
                if len(lines) < 2: break
                if not header: out.write(lines[0] + '\n'); header = True
                out.write('\n'.join(lines[1:]) + '\n'); seen += len(lines) - 1
            else:
                n = txt.count('&P')
                if n == 0: break
                out.write(txt + '\n'); seen += n
            print(f'  {name}: page {page}, {seen} records')
            if page == 1 and seen >= page_size: break
            time.sleep(pause)
        out.close()

TASKS = {
 'lineara': lambda: from_github_zip('mwenge/lineara.xyz', 'master',
        ['items_analysis/inscriptions.json'], ['inscriptions.json']),
 'linearb': lambda: from_github_zip('mwenge/linearb.xyz', 'master',
        ['items_analysis/inscriptions.json'], ['linearb_inscriptions.json']),
 # the full Linear B corpus and lexicon used since 10 Sep 2026 are the JS bundles of the same repository;
 # scripts/extract_linearb.py turns them into data/raw/linearb/{inscriptions_B,lexicon_B,forms_B}.json
 'linearb_js': lambda: from_github_zip('mwenge/linearb.xyz', 'master',
        ['LinearBInscriptions.js', 'lexicon.js'], ['linearb/LinearBInscriptions.js', 'linearb/lexicon.js']),
 # Younger's per-document commentary pages (HTML), the source of the sign/seal table of the HT nodules
 # (scripts/extract_nodule_seals.py): folder commentary/ of the Explorer
 'younger_commentary': lambda: from_github_zip('mwenge/lineara.xyz', 'master',
        ['commentary/'], ['younger_commentary/']),
 # NeuroDecipher (Luo, Cao & Barzilay 2019) data: Linear B-Greek and Ugaritic-Hebrew cognate files
 'neurodecipher': lambda: from_github_zip('j-luo93/NeuroDecipher', 'master',
        ['data/linear_b-greek.cog', 'data/uga-heb.small.no_spe.cog'], ['neurodecipher/linear_b-greek.cog', 'neurodecipher/uga-heb.small.no_spe.cog']),
 'iberian': lambda: from_github_zip('j-luo93/DecipherUnsegmented', 'main',
        ['data/iberian.csv'], ['iberico_hesperia_luo2021.csv']),
 'etruscan': lambda: from_github_zip('GianlucaVico/Larth-Etruscan-NLP', 'main',
        ['Data/Etruscan.csv', 'Data/ETP_POS.csv'], ['etruscan_larth.csv', 'etruscan_etp_pos.csv']),
 'proto_elamite': lambda: cdli('Proto-Elamite (ca. 3100-2900 BC)', 'proto_elamita.atf', 'proto_elamita_cat.csv'),
 'uruk': lambda: [cdli(p, 'uruk.atf' if i == 0 else 'uruk_III.atf', 'uruk_cat.csv' if i == 0 else 'uruk_III_cat.csv')
                  for i, p in enumerate(['Uruk IV (ca. 3350-3200 BC)', 'Uruk III (ca. 3200-3000 BC)'])],
}
# Candidate-language corpora (CDLI bulk ATF, TLHdig from Zenodo 15459134) are fetched by
# scripts/fetch_candidates.py; Grambank by hand from grambank.clld.org.
# SigLA: not fetched automatically. Download the dataset from https://sigla.phis.me (CC BY-NC-SA)
# or the pyaegean release, and place sigla_corpus.json in data/raw/.

if __name__ == '__main__':
    names = sys.argv[1:] or list(TASKS)
    for n in names:
        if n not in TASKS: print('unknown:', n); continue
        print(n); TASKS[n]()
    print('done. SigLA must be downloaded by hand (see data/README.md).')
