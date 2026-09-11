#!/usr/bin/env python3
"""From Younger's commentary pages (data/fetch.py younger_commentary -> data/raw/younger_commentary/),
extract per sealed document (W-series) the sign and the seal impression (AT/CMS number, motif).
Writes data/raw/nodules_seals_younger.json (with the commentary text, not redistributed) and
data/derived/nodules_sign_seal.json (facts only)."""
import re, html, os, json
src = 'data/raw/younger_commentary'; rows = []
for f in sorted(os.listdir(src)):
    if not re.match(r'(HT|KH|ZA|KN|PH|MA|GO|PYR|TY|AR)W[abcde]', f): continue
    t = html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', open(os.path.join(src, f), encoding='utf-8').read())))
    name = f.replace('.html', '')
    seals = re.findall(r'(AT|KH|ZA|KN|PH|MA)\s?(\d+)\s*\(=\s*CMS ([^:)]*?)(?::\s*([^)]*))?\)', t)
    sign = re.search(r'(?:Scribe \d+\s+)?([A-Z*][A-Z0-9*₂₃+\-]*)\s+[abcd]?:?\s*seal', t)
    rows.append({'doc': name, 'site': name[:2], 'text': t[:400], 'sign': sign.group(1) if sign else None,
                 'seals': [{'code': a + ' ' + b, 'cms': c.strip(), 'motif': (d or '').strip()} for a, b, c, d in seals]})
json.dump(rows, open('data/raw/nodules_seals_younger.json', 'w'), ensure_ascii=False)
json.dump([{k: r[k] for k in ('doc', 'site', 'sign', 'seals')} for r in rows if r['sign'] or r['seals']],
          open('data/derived/nodules_sign_seal.json', 'w'), ensure_ascii=False, indent=0)
print(len(rows), 'W documents')
