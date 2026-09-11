"""Look a sign-group up in the published reference works before measuring it.

Six times in one week this project measured something, concluded something, and then found the
conclusion already published — twice in Younger's Lexicon, which catalogues the corpus word by
word and is freely available. The cost each time was a wasted afternoon; the cure is one lookup.

    from kuro import Reference
    ref = Reference('docs/reference')       # folder of extracted reference texts
    print(ref.lookup('KU-NI-SU'))           # what the literature already says
    print(ref.unread(['KU-NI-SU','SA-RU'])) # which of these have no entry

The folder holds plain-text extractions of the reference works, one file per work, with a header
line naming the work. Nothing is redistributed: the extractions are made locally from PDFs the
user obtains, and `docs/reference/README.md` says which and where from.
"""
import os, re, glob


class Reference:
    """An index over the reference works, queried by sign-group."""

    def __init__(self, path='docs/reference'):
        self.path = path
        self.works = {}
        if os.path.isdir(path):
            for p in sorted(glob.glob(os.path.join(path, '*.txt'))):
                name = os.path.basename(p)[:-4]
                with open(p, encoding='utf-8', errors='replace') as f:
                    self.works[name] = f.read()

    def __len__(self):
        return len(self.works)

    def lookup(self, word, window=260, max_hits=3):
        """Every passage in every work that mentions this sign-group.

        Matching is case-insensitive and tolerates the variants the editions use (subscript two
        written as 2, the asterisk of unread signs). Returns a printable report.
        """
        if not self.works:
            return (f'No reference texts in {self.path}. See its README for what to put there; '
                    'the works are not redistributed with this package.')
        pats = self._variants(word)
        out = [f'=== {word} ===']
        found = False
        for name, text in self.works.items():
            hits = []
            for p in pats:
                for m in re.finditer(re.escape(p), text):
                    seg = re.sub(r'\s+', ' ', text[max(0, m.start() - 40):m.start() + window])
                    if seg not in hits:
                        hits.append(seg)
                    if len(hits) >= max_hits:
                        break
                if len(hits) >= max_hits:
                    break
            if hits:
                found = True
                out.append(f'\n-- {name}')
                for h in hits:
                    out.append(f'   {h}')
        if not found:
            out.append('  not mentioned in any indexed work. That is worth knowing, but it is not'
                       ' proof of novelty: the index covers only what is in the folder.')
        return '\n'.join(out)

    # Editions write the same sign several ways: CYP for A*303, subscript two as 2, ligatures
    # with or without the plus. A lookup that misses these reports a gap where there is none,
    # which is the error this whole class exists to prevent.
    LABELS = {'CYP': '*303', 'OLE': '*302', 'GRA': '*120', 'NI': '*30',
              'VIN': '*131', 'OLIV': '*122', 'AROM': '*304'}

    SUBS = str.maketrans('₀₁₂₃₄₅₆₇₈₉', '0123456789')

    def _variants(self, word):
        plain = word.translate(self.SUBS)          # subscript digits written flat
        v = {word, plain, word.upper(), plain.upper(), word.lower(), plain.lower(),
             word.replace('+', ''), plain.replace('+', ''),
             word.replace('*', ''), plain.replace('*', '')}
        for label, num in self.LABELS.items():
            if label in plain:
                w2 = plain.replace(label, num)
                v |= {w2, w2.replace('+', '')}
        # Editions pad sign numbers to three digits and lowercase the form letter: *22F is
        # written *022f. Without this the lookup reports a gap for every low-numbered sign.
        import re as _re
        for x in list(v):
            m = _re.match(r'^\*(\d{1,3})([A-Za-z]?)(.*)$', x)
            if m:
                num, letter, rest = m.groups()
                v |= {f'*{int(num):03d}{letter}{rest}', f'*{int(num):03d}{letter.lower()}{rest}',
                      f'*{num}{letter.lower()}{rest}'}
        return {x for x in v if len(x) > 1}

    def mentioned(self, word):
        """True if any indexed work mentions this sign-group, under any of its written forms."""
        return any(any(p in t for p in self._variants(word)) for t in self.works.values())

    def unread(self, words):
        """Of these sign-groups, which the indexed works do not mention.

        Use it before a screen: the ones that are mentioned need reading first, the ones that are
        not are where a new measurement can be claimed as new.
        """
        seen, unseen = [], []
        for w in words:
            (seen if self.mentioned(w) else unseen).append(w)
        return {'mentioned': seen, 'not_mentioned': unseen,
                'works_indexed': sorted(self.works)}
