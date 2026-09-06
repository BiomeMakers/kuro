import json, re, csv
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Document:
    id: str
    site: str = "?"
    support: str = "?"
    date: str = "?"
    hand: str = ""
    tokens: List[str] = field(default_factory=list)   # reading order, '|' marks a line break

    def words(self, pattern=r'^[A-Za-z₀-₉*\-]+$', min_syll=1):
        return [t.lower() for t in self.tokens if re.match(pattern, t) and t.count('-') >= min_syll - 1 and t != '|']
    def logograms(self):
        return [t for t in self.tokens if re.fullmatch(r'[A-Z][A-Z0-9+*\[\]?]*', t) and len(t) > 1]

FRACTIONS = {'¹⁄₂','¹⁄₃','²⁄₃','¹⁄₄','³⁄₄','¹⁄₅','¹⁄₆','¹⁄₈','¹⁄₁₆','³⁄₈','⁵⁄₈','⁷⁄₈','²⁄₅','³⁄₅','⁴⁄₅','⁵⁄₆'}
def is_number(t): return bool(re.fullmatch(r'\d+', t)) or t in FRACTIONS

def load_lineara(path):
    """LinearA Explorer (Hogan) items_analysis/inscriptions.json -> list of Document."""
    data = json.load(open(path, encoding='utf-8'))
    docs = []
    for name, it in data:
        toks = [w if w != '\n' else '|' for w in it.get('transliteratedWords', []) if isinstance(w, str)]
        docs.append(Document(id=name, site=it.get('site') or '?', support=it.get('support') or '?',
                             date=it.get('period') or '?', hand=(it.get('scribe') or '').strip(), tokens=toks))
    return docs

def load_cdli_atf(path, catalogue_csv=None, sign_side='before_comma'):
    """CDLI ATF export -> Documents; each numbered line becomes tokens: sign-strings then numerals.
    sign_side: 'before_comma' (Proto-Elamite) or 'after_comma' (proto-cuneiform)."""
    cat = {}
    if catalogue_csv:
        csv.field_size_limit(10**8)
        for r in csv.DictReader(open(catalogue_csv, encoding='utf-8', errors='ignore')):
            cat[str(r.get('artifact_id') or r.get('id_text') or '').zfill(6)] = r
    txt = open(path, encoding='utf-8', errors='ignore').read()
    docs = []
    for b in [b for b in re.split(r'\n(?=&P\d+)', txt) if b.startswith('&P')]:
        pid = re.match(r'&P(\d+)', b).group(1); toks = []
        for l in b.split('\n'):
            m = re.match(r'^\s*(\d+[a-zA-Z\']*)\.\s+(.*)$', l)
            if not m: continue
            body = m.group(2)
            left, right = (body.split(',', 1) + [''])[:2] if ',' in body else (body, '')
            signs_src = left if sign_side == 'before_comma' else right
            signs = [re.sub(r'[#?!\[\]]', '', re.sub(r'[~@][a-z0-9]+', '', t)) for t in signs_src.split()
                     if re.match(r'^\|?[A-Za-z]', t) and not re.match(r'^\d', t) and t not in ('x', '...')]
            nums = re.findall(r'(\d+)\((N\d+[A-Z]?)\)', body)
            if signs: toks.append(' '.join(signs))
            for k, n in nums: toks.append(f'{k}({n})')
            toks.append('|')
        r = cat.get(pid, {})
        docs.append(Document(id='P' + pid, site=(r.get('provenience') or '?').split(' (')[0],
                             support=r.get('artifact_type') or '?', date=r.get('period') or '?', tokens=toks))
    return docs

def load_csv_texts(path, id_col, text_col, site_col=None, date_col=None, splitter=r'[\s:·]+'):
    csv.field_size_limit(10**8)
    docs = []
    for r in csv.DictReader(open(path, encoding='utf-8', errors='ignore')):
        toks = [w for w in re.split(splitter, r.get(text_col) or '') if w]
        docs.append(Document(id=str(r.get(id_col)), site=(r.get(site_col) or '?') if site_col else '?',
                             date=(r.get(date_col) or '?') if date_col else '?', tokens=toks))
    return docs
