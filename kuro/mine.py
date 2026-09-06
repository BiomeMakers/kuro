import re, html, glob, collections
DOUBT = re.compile(r'(problematic|uncertain|unclear|not clear|does not (?:add|total|work)|is (?:in)?correct|should (?:total|be)|cannot|impossible|perhaps|possibly|may be|might be|difficult|puzzling|odd|\?)', re.I)
def doubts(paths_glob, kinds=None):
    """Mine an expert's commentaries (HTML or text files) for sentences expressing doubt; classify."""
    kinds = kinds or {'arithmetic': r'total|add|sum|fraction|correct', 'function': r'name|term|place|heading|transaction|person|word', 'reading': r'read|sign|trace|erased|damaged|restor'}
    out = []
    for f in sorted(glob.glob(paths_glob)):
        t = html.unescape(re.sub(r'<[^>]*>', ' ', open(f, encoding='utf-8', errors='ignore').read())); t = re.sub(r'\s+', ' ', t)
        for s in re.split(r'(?<=[.;])\s+', t):
            if DOUBT.search(s) and 25 < len(s) < 400:
                k = next((name for name, pat in kinds.items() if re.search(pat, s, re.I)), 'other')
                out.append(dict(source=f.split('/')[-1], kind=k, sentence=s.strip()))
    return out
