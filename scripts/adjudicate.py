#!/usr/bin/env python3
"""Put a proposed decipherment on the bench.

    python scripts/adjudicate.py proposal.json

proposal.json: {"glosses": {"KU-RO": "all, the total"},
                "values": {"*301": "na"},
                "language": "ugaritic",
                "roots": ["ksp", "hrs", "mlk"]}

Prints: agreement with the measured functions, the phonotactic consequence of the values
against a control, and whether the claimed family's roots recur.
"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from kuro.adjudicate import Bench
from kuro.names import broken_status, syls

p = json.load(open(sys.argv[1], encoding='utf-8'))
b = Bench.from_dictionary('data/derived/dictionary.json')
d = json.load(open('data/raw/inscriptions.json')); st = broken_status(d)
units = [u for u in {'-'.join(syls(t)).lower() for n, it in d
                     for t in it.get('transliteratedWords', []) if isinstance(t, str) and '-' in t}
         if st.get(u) == 'intact']
target = None
if p.get('language'):
    c = json.load(open('data/derived/corpus_all.json'))
    MAP = {'ʾ': '', 'ʿ': '', 'ḥ': 'h', 'ḫ': 'k', 'š': 's', 'ṯ': 't', 'ḏ': 'd', 'ṣ': 's', 'ṭ': 't'}
    raw = c.get(p['language'].capitalize(), c.get(p['language'], []))
    target = [''.join(MAP.get(ch, ch) for ch in w.lower() if ch in MAP or ch in 'bdgkmnpqrstwzjhl') for w in raw]
print(b.report(p.get('glosses', {}), units=units, target_words=target,
               values=p.get('values'), roots=p.get('roots')))
