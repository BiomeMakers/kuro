"""Proposing from what we have measured, not from what others have written.

The bibliographic reader reproduces: every proposition it yields is one someone already made. What
produced a new unit today was an analogy over our own measurements — MA-RU-ME entered because its
structure matched OLE+KI, which we had measured days earlier. Nobody wrote that; it came from
comparing two of our own numbers.

This module makes that systematic. Three mechanisms over the dictionary and the corpus, and a fourth
over the literature that asks not what it claims but what it says it could not do.

  analogy        for each unread unit, the read unit whose measured behaviour it most resembles
  anomaly        units that behave unlike the category they are placed in
  extrapolation  a structure found in one place, searched for everywhere
  gaps           what the literature declares it could not measure, check, or decide

    from kuro import Proposer
    P = Proposer(dictionary, docs)
    P.analogies()          # candidates by resemblance to a read unit
    P.anomalies()          # read units that break their own category's pattern
    P.extrapolate('qualifier')   # e.g. syllables attached to several commodities

Every candidate comes out as a Proposition with a refutation condition, ready for the cycle. What
this does not do is decide: it proposes, and the judge disposes.
"""
import re, math
from collections import Counter, defaultdict
from .reader import Proposition

FR = {'¹⁄₂', '¹⁄₃', '²⁄₃', '¹⁄₄', '³⁄₄', '¹⁄₅', '¹⁄₆', '¹⁄₈', '¹⁄₁₆', '³⁄₈'}


def _behaviour(unit, docs, sites):
    """A small vector of measured behaviour, comparable across units."""
    n = head = whole = frac = withlog = 0
    st = Counter(); qtys = []
    for toks, site in zip(docs, sites):
        for i, t in enumerate(toks):
            if t != unit:
                continue
            n += 1; st[site] += 1
            if i == 0:
                head += 1
            j = i + 1
            while j < len(toks) and (re.fullmatch(r'\d+', toks[j]) or toks[j] in FR):
                if toks[j] in FR:
                    frac += 1
                else:
                    whole += 1; qtys.append(int(toks[j]))
                j += 1
            if i + 1 < len(toks) and re.fullmatch(r'[A-Z*][A-Z0-9+*\[\]?]*', toks[i + 1]) \
                    and len(toks[i + 1]) > 1:
                withlog += 1
    if not n:
        return None
    top = st.most_common(1)[0][1] / n
    return {'n': n, 'head': head / n, 'whole': whole / n, 'frac': frac / n,
            'withlog': withlog / n, 'site_conc': top, 'sites': len(st),
            'median_qty': sorted(qtys)[len(qtys) // 2] if qtys else 0}


def _dist(a, b):
    """Distance in behaviour. Quantity magnitude is included on a log scale, because without it
    every unit that carries whole numbers and heads nothing looked like KU-RO, whose totals run
    to hundreds; a unit at 3 and a unit at 300 are not alike."""
    keys = ('head', 'whole', 'frac', 'withlog', 'site_conc')
    d2 = sum((a[k] - b[k]) ** 2 for k in keys)
    qa, qb = math.log1p(a['median_qty']), math.log1p(b['median_qty'])
    d2 += ((qa - qb) / 3.0) ** 2
    return math.sqrt(d2)


class Proposer:
    def __init__(self, dictionary, docs, sites=None):
        self.dic = dictionary
        self.docs = [list(d) for d in docs]
        self.sites = list(sites) if sites is not None else ['?'] * len(self.docs)
        self._beh = {}

    def behaviour(self, unit):
        if unit not in self._beh:
            self._beh[unit] = _behaviour(unit, self.docs, self.sites)
        return self._beh[unit]

    # ---- 1. analogy ---------------------------------------------------------------------------
    def analogies(self, min_n=3, max_dist=0.35, limit=40):
        """For each unread unit, the read unit it most resembles in measured behaviour.

        Run over the whole corpus on 10 September 2026: 36 analogies, none survived its null, one
        borderline. The p-values clustered between 0.05 and 0.12, which is the signature of an
        instrument that does not discriminate — with some twenty-five read units and a
        five-dimensional behaviour vector, "the nearest read unit" is a minimum among few options
        over coarse features, not a finding. Kept because the null that killed it is the point, and
        because a richer behaviour vector may yet make it work. What did work the same day was
        `extrapolate`, which asks for a concrete structure rather than general resemblance.
        """
        read = [(f, e) for f, e in self.dic.entries.items() if e.get('gloss')]
        out = []
        for f, e in self.dic.entries.items():
            if e.get('gloss') or e.get('attestations', 0) < min_n:
                continue
            bf = self.behaviour(f)
            if not bf:
                continue
            best = None
            for g, ge in read:
                bg = self.behaviour(g)
                if not bg or bg['n'] < min_n:
                    continue
                d = _dist(bf, bg)
                if best is None or d < best[0]:
                    best = (d, g, ge)
            if best and best[0] <= max_dist:
                d, g, ge = best
                out.append(Proposition(
                    units=[f, g], kind='distributional',
                    claim=f'{f} belongs to the same class as {g} ({ge.get("gloss", "")[:40]})',
                    refuted_by=f'{f} lacking a property {g} has beyond the ones matched here: '
                               f'a different site pattern, a different quantity range, or a '
                               f'different position in its documents',
                    source_says=f'behavioural distance {d:.3f}', mechanism='analogy', score=1 - d))
        return sorted(out, key=lambda p: -p['score'])[:limit]

    # ---- 2. anomaly ---------------------------------------------------------------------------
    def anomalies(self, limit=30):
        """Read units that break the pattern of their own category. Each is a question.

        A commodity that never carries a quantity, a person category that carries a fraction, a
        transaction term confined to one site: either the reading is wrong or the corpus has a
        story the reading does not tell. Both are worth a hypothesis.
        """
        rules = [
            ('commodity', lambda b: b['whole'] + b['frac'] == 0,
             'is glossed as a commodity but is never followed by a quantity'),
            ('person_category', lambda b: b['frac'] > 0,
             'is glossed as a category of persons but carries a fraction'),
            ('transaction_term', lambda b: b['sites'] == 1 and b['n'] >= 5,
             'is glossed as a transaction term but occurs at a single site'),
            ('party', lambda b: b['withlog'] > 0.5,
             'is glossed as a party but is usually followed by a commodity logogram'),
        ]
        out = []
        for f, e in self.dic.entries.items():
            g = (e.get('gloss') or '').lower()
            b = self.behaviour(f)
            if not b or b['n'] < 3:
                continue
            for cat, test, why in rules:
                if cat.replace('_', ' ') in g or cat in g:
                    if test(b):
                        out.append(Proposition(
                            units=[f], kind='distributional',
                            claim=f'{f} {why}; either the reading or the category is wrong',
                            refuted_by=f'the anomaly being an artefact of transcription, e.g. '
                                       f'quantities recorded on the other side of the document',
                            mechanism='anomaly', score=b['n'] / 20))
        return sorted(out, key=lambda p: -p['score'])[:limit]

    # ---- 3. extrapolation ---------------------------------------------------------------------
    def extrapolate(self, structure='qualifier', min_hosts=2, limit=30):
        """A structure found once, searched for everywhere.

        'qualifier'   a syllable attached to several distinct commodities (KI on OLE+KI, KI-MA-RU,
                      *316+KI) is a grade or type, and every unit it attaches to inherits a reading
        'alternation' a stem attested both bare and with one ending, the ending recurring on other
                      stems (the pairs Davis collects); the proposition is that the ending is an affix
        'subcount'    a unit that follows a count with a smaller figure (*86 after VIR, KI-RO after
                      KU-RO): a sub-quantity of what precedes it
        'summand'     a unit followed by a figure that equals the sum of the figures before it
                      in the document (KU-RO, DA-I): a total term
        """
        if structure == 'qualifier':
            return self._qualifiers(min_hosts, limit)
        if structure == 'alternation':
            return self._alternations(min_hosts, limit)
        if structure == 'subcount':
            return self._subcounts(limit)
        if structure == 'summand':
            return self._summands(limit)
        raise ValueError('structure must be qualifier, alternation, subcount or summand')

    COMMODITY = {'GRA', 'NI', 'VIN', 'OLIV', 'OLE', 'CYP', 'FIC', 'AROM', 'TELA', 'LANA',
                 '*303', '*304', '*308', '*316', '*188', 'MA-RU', 'BOS', 'OVIS', 'CAP', 'SUS'}

    def _qualifiers(self, min_hosts, limit):
        hosts = defaultdict(set)
        for toks in self.docs:
            for t in toks:
                m = re.fullmatch(r'([A-Z*][A-Z0-9*]*)\+([A-Z]{2})', t)
                if m and m.group(1) in self.COMMODITY:
                    hosts[m.group(2)].add(m.group(1)); continue
                m = re.fullmatch(r'([A-Z]{2})-(MA-RU)', t)
                if m:
                    hosts[m.group(1)].add(m.group(2)); continue
                m = re.fullmatch(r'(MA-RU)-([A-Z]{2})', t)
                if m:
                    hosts[m.group(2)].add(m.group(1))
        out = []
        for syl, hs in hosts.items():
            if len(hs) >= min_hosts:
                out.append(Proposition(
                    units=sorted(hs)[:4], kind='distributional',
                    claim=f'{syl} is a qualifier (a grade or type) shared by {len(hs)} commodities: '
                          f'{", ".join(sorted(hs)[:4])}',
                    refuted_by=f'{syl} heading a document on its own or carrying its own total, '
                               f'which a qualifier does not do',
                    mechanism='extrapolation', score=len(hs)))
        return sorted(out, key=lambda p: -p['score'])[:limit]

    def _alternations(self, min_stems, limit):
        """stems attested bare and with the same ending: the ending is a candidate affix."""
        words = {t.upper() for toks in self.docs for t in toks if '-' in t and re.fullmatch(r'[A-Za-z₀-₉\-]+', t)}
        by_ending = defaultdict(set)
        for w in words:
            parts = w.split('-')
            if len(parts) < 3:
                continue
            stem, end = '-'.join(parts[:-1]), parts[-1]
            if stem in words:
                by_ending[end].add(stem)
        out = []
        for end, stems in by_ending.items():
            if len(stems) >= min_stems:
                out.append(Proposition(
                    units=[f'{s}-{end}' for s in sorted(stems)[:3]], kind='lexical',
                    claim=f'-{end} is a productive ending: {len(stems)} stems occur both bare and with '
                          f'it ({", ".join(sorted(stems)[:3])})',
                    refuted_by=f'the bare and -{end} forms of the same stem showing no difference in '
                               f'position, quantity or company, so that -{end} changes nothing measurable',
                    mechanism='extrapolation', score=len(stems)))
        return sorted(out, key=lambda p: -p['score'])[:limit]

    def _subcounts(self, limit):
        """a unit that follows a count with a smaller figure, in most of its attestations."""
        hits = defaultdict(lambda: [0, 0])
        for toks in self.docs:
            for i, t in enumerate(toks):
                if not re.fullmatch(r'[A-Z*][A-Z0-9+*\[\]?]*', t) or len(t) < 2:
                    continue
                prev_q = [int(x) for x in toks[max(0, i - 3):i] if re.fullmatch(r'\d+', x)]
                next_q = [int(x) for x in toks[i + 1:i + 2] if re.fullmatch(r'\d+', x)]
                if prev_q and next_q:
                    hits[t][1] += 1
                    if next_q[0] < max(prev_q):
                        hits[t][0] += 1
        out = []
        for u, (small, n) in hits.items():
            if n >= 3 and small / n >= 0.75 and not self.dic.entries.get(u, {}).get('gloss'):
                out.append(Proposition(
                    units=[u], kind='arithmetic',
                    claim=f'{u} records a sub-quantity of the count before it: smaller figure in '
                          f'{small} of {n} attestations',
                    refuted_by=f'{u} carrying a figure larger than the count it follows, or standing '
                               f'without a preceding count',
                    mechanism='extrapolation', score=small / n * min(n, 10) / 10))
        return sorted(out, key=lambda p: -p['score'])[:limit]

    def _summands(self, limit):
        """a unit whose figure equals the sum of the figures before it in the document."""
        hits = defaultdict(lambda: [0, 0])
        for toks in self.docs:
            for i, t in enumerate(toks):
                if not re.fullmatch(r'[A-Za-z₀-₉*][A-Za-z0-9₀-₉+*\-]*', t) or len(t) < 2:
                    continue
                nxt = toks[i + 1] if i + 1 < len(toks) else ''
                if not re.fullmatch(r'\d+', nxt):
                    continue
                before = [int(x) for x in toks[:i] if re.fullmatch(r'\d+', x)]
                if len(before) >= 2:
                    hits[t][1] += 1
                    if sum(before) == int(nxt):
                        hits[t][0] += 1
        out = []
        for u, (eq, n) in hits.items():
            if eq >= 2 and not self.dic.entries.get(u.upper(), {}).get('gloss'):
                out.append(Proposition(
                    units=[u], kind='arithmetic',
                    claim=f'{u} is a total term: its figure equals the sum of the preceding figures '
                          f'in {eq} of {n} documents',
                    refuted_by=f'{u} followed by a figure unrelated to the preceding ones in most '
                               f'attestations',
                    mechanism='extrapolation', score=eq))
        return sorted(out, key=lambda p: -p['score'])[:limit]

    def report(self, props):
        by = Counter(p.get('mechanism') for p in props)
        lines = [f'{len(props)} propositions: ' + ', '.join(f'{k} {v}' for k, v in by.items()), '']
        for p in props[:15]:
            lines.append(f'  [{p.get("mechanism", "?"):<13}] {p["claim"][:90]}')
        return '\n'.join(lines)
