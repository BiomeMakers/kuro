#!/usr/bin/env python3
"""Run the whole procedure over a corpus and print the report.

    python scripts/survey.py linear_a
    python scripts/survey.py iberian
    python scripts/survey.py etruscan

Adding a corpus is one entry in CORPORA below: a loader and its CorpusProfile.
"""
import sys, os, json, csv, ast, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro.corpus import Document, load_lineara
from kuro.survey import Survey, CorpusProfile


def linear_a():
    from kuro.names import broken_status, syls
    docs = load_lineara('data/raw/inscriptions.json')
    raw = json.load(open('data/raw/inscriptions.json'))
    st = broken_status(raw)
    cand = {}
    c = json.load(open('data/derived/corpus_all.json'))
    for k, v in (('mycenaean', c['LinB']), ('hittite', c['Hittite']), ('ugaritic', c['Ugaritic'])):
        cand[k] = v
    p = CorpusProfile(
        commodities={'GRA', 'NI', 'VIN', 'OLIV', 'OLE', 'CYP', 'VIR', 'TELA', 'MA-RU', '*304', '*303', '*188', '*316'},
        totals={'KU-RO', 'KI-RO', 'PO-TO-KU-RO', 'DA-I'}, separator='𐄁',
        broken={k: v for k, v in st.items()}, candidates=cand)
    return docs, p


def iberian():
    d = json.load(open('data/derived/iberian_corpus.json'))
    docs = [Document(id=n, site=n.split('.')[0], support='?', tokens=[t for t in toks if t])
            for n, toks in d['docs']]
    ascoli = ['sani', 'belser', 'atin', 'kibas', 'bilos', 'tibas', 'sosin', 'urki', 'uŕke', 'biuŕ',
              'biur', 'akir', 'umar', 'basti', 'balke', 'ilun', 'aŕan', 'elan', 'tautin', 'albe',
              'belen', 'ordin', 'taker']
    c = json.load(open('data/derived/corpus_all.json'))
    p = CorpusProfile(separator=':', name_elements=ascoli, unit_sep='-',
                      candidates={'mycenaean': c['LinB'], 'etruscan': [], 'hittite': c['Hittite']})
    p.candidates = {k: v for k, v in p.candidates.items() if v}
    return docs, p


def etruscan():
    rows = list(csv.DictReader(open('data/derived/openetruscan_clean.csv')))
    col = [k for k in rows[0] if 'word' in k.lower() or 'form' in k.lower()][0]
    idc = [k for k in rows[0] if 'id' in k.lower()] or [col]
    docs = [Document(id=r.get(idc[0], str(i)), tokens=[r[col]]) for i, r in enumerate(rows) if r.get(col)]
    return docs, CorpusProfile()


CORPORA = {'linear_a': linear_a, 'iberian': iberian, 'etruscan': etruscan}

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'linear_a'
    if name not in CORPORA:
        print('corpora:', ', '.join(CORPORA)); sys.exit(1)
    docs, profile = CORPORA[name]()
    s = Survey(docs, profile, seed=1)
    print(s.report())
    os.makedirs('data/derived/surveys', exist_ok=True)
    json.dump(s.out, open(f'data/derived/surveys/{name}.json', 'w'), ensure_ascii=False, default=str, indent=1)
    print(f'\n[saved data/derived/surveys/{name}.json]', file=sys.stderr)
