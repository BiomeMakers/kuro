#!/usr/bin/env python3
"""Turn the linearb.xyz JS bundles (data/fetch.py linearb_js) into JSON:
data/raw/linearb/inscriptions_B.json, lexicon_B.json, forms_B.json (form -> count)."""
import json, re, os
from collections import Counter
D = 'data/raw/linearb/'
def load(fn):
    s = open(fn, encoding='utf-8').read(); s = s[s.index('new Map(') + 8:]; s = s[:s.rstrip().rstrip(';').rfind(')')]
    return json.loads(s)
ins = load(D + 'LinearBInscriptions.js'); lex = load(D + 'lexicon.js')
words = Counter()
for n, it in ins:
    for w in it.get('transliteratedWords', []):
        if isinstance(w, str) and '-' in w and re.fullmatch(r'[a-z0-9\-₀-₉]+', w):
            words[w] += 1
L = [{'transcription': e.get('transcription') or re.sub(r'[^a-z0-9\-₀-₉]', '', k), 'greek': e.get('greek', ''), 'translation': e.get('translation', '')} for k, e in lex]
json.dump(ins, open(D + 'inscriptions_B.json', 'w'), ensure_ascii=False)
json.dump(L, open(D + 'lexicon_B.json', 'w'), ensure_ascii=False)
json.dump(words, open(D + 'forms_B.json', 'w'), ensure_ascii=False)
print(f'{len(ins)} inscriptions, {len(L)} lexicon entries, {len(words)} forms')
