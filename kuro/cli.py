"""Command line for kuro reports.

    python -m kuro report HT23a --corpus data/raw/inscriptions.json
    python -m kuro sign CYP
    python -m kuro arithmetic HT117a
    python -m kuro classify --out classification.csv

The corpus path defaults to data/raw/inscriptions.json (the LinearA Explorer export);
set KURO_CORPUS in the environment to point elsewhere.
"""
import sys, os, argparse
from .corpus import load_lineara
from .report import Corpus

DEFAULT = os.environ.get('KURO_CORPUS', 'data/raw/inscriptions.json')


def _corpus(path):
    if not os.path.exists(path):
        sys.exit(f'corpus not found: {path}\nDownload it with: python3 data/fetch.py lineara')
    return Corpus(load_lineara(path), source_path=path)


def main(argv=None):
    p = argparse.ArgumentParser(prog='kuro', description='Reports on epigraphic documents.')
    p.add_argument('--corpus', default=DEFAULT, help='path to the corpus JSON')
    sub = p.add_subparsers(dest='cmd', required=True)
    r = sub.add_parser('report', help='full report for one document')
    r.add_argument('id')
    s = sub.add_parser('sign', help='distributional profile of one sign or sign-group')
    s.add_argument('sign')
    a = sub.add_parser('arithmetic', help='totals and fixed ratios in one document')
    a.add_argument('id')
    v = sub.add_parser('verify', help='what to check against the primary edition, and why')
    v.add_argument('id')
    cc = sub.add_parser('capture', help='does a group difference track how the documents were recorded?')
    cc.add_argument('factor', nargs='?', default='site', choices=['site', 'support'])
    p2 = sub.add_parser('power', help='what a corpus of a given size can support')
    p2.add_argument('--documents', type=int); p2.add_argument('--tokens', type=int)
    b = sub.add_parser('biblio', help='prior-art status of every claim')
    b.add_argument('--path', default='biblio')
    c = sub.add_parser('classify', help='classify every document by content')
    c.add_argument('--out', help='write a CSV instead of printing a summary')
    args = p.parse_args(argv)
    if args.cmd == 'biblio':
        print(biblio_report(args.path)); return
    C = _corpus(args.corpus)
    if args.cmd == 'report':
        print(C.tablet_report(args.id))
    elif args.cmd == 'sign':
        print(C.sign_profile(args.sign))
    elif args.cmd == 'arithmetic':
        print(C.arithmetic_check(args.id))
    elif args.cmd == 'power':
        from .report import power_report
        print(power_report(args.documents, args.tokens))
    elif args.cmd == 'verify':
        print(C.verify(args.id))
    elif args.cmd == 'capture':
        print(C.capture_control(args.factor))
    elif args.cmd == 'classify':
        rows = [(d.id, d.site, d.support, C.classify(d)) for d in C.docs.values()]
        if args.out:
            import csv
            with open(args.out, 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f); w.writerow(['id', 'site', 'support', 'class']); w.writerows(rows)
            print(f'{len(rows)} documents written to {args.out}')
        else:
            import collections
            t = collections.Counter((r[2], r[3]) for r in rows)
            print(f'{len(rows)} documents')
            for (sup, cls), n in t.most_common(20):
                print(f'  {sup[:20]:<20} {cls:<14} {n:>5}')


if __name__ == '__main__':
    main()


def biblio_report(path='biblio'):
    """What has been checked against the literature, and what has not."""
    import json, os, collections
    w = {x['id']: x for x in json.load(open(os.path.join(path, 'works.json')))}
    claims = json.load(open(os.path.join(path, 'claims.json')))
    by = collections.Counter(c['status'] for c in claims)
    out = ['=' * 78, 'PRIOR-ART STATUS OF EVERY CLAIM', '=' * 78, '']
    for st in ('CONFLICT', 'PRIOR ART', 'UNCHECKED', 'PARTIAL', 'CHECKED'):
        sel = [c for c in claims if c['status'] == st]
        if not sel:
            continue
        out.append(f'{st} ({len(sel)})')
        for c in sel:
            miss = [k for k in c['works'] if k in w and not w[k]['read']]
            out.append(f"  {c['id']:<22} [{c['paper']}] {c['claim'][:52]}")
            if miss:
                out.append(f"      needs: {', '.join(w[k]['title'][:44] for k in miss)}")
        out.append('')
    held = sum(1 for x in w.values() if x['held'])
    read = sum(1 for x in w.values() if x['read'])
    out.append(f'works: {len(w)} known, {held} held, {read} read')
    out.append(f'claims: {sum(by.values())} — ' + ', '.join(f'{k} {v}' for k, v in by.most_common()))
    out.append('')
    out.append('A claim with status UNCHECKED should not be published as new without either')
    out.append('reading the work listed or stating "so far as I know the literature".')
    return '\n'.join(out)
