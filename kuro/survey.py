"""One pass over an undeciphered corpus: the whole procedure, in the order that matters.

Weeks of work on Linear A reduce to a sequence that any corpus of the same kind can take, in
minutes. Each step measures something against a null, and each step that cannot be measured
says so instead of guessing. Nothing here reads a reading: the output is what the corpus can
support, with its numbers.

    from kuro.survey import Survey, CorpusProfile
    s = Survey(documents, CorpusProfile(commodities={'GRA', ...}, totals={'KU-RO'}))
    print(s.report())

The order is the one the Linear A work arrived at the hard way:
  1 inventory and integrity   what is there, and how much of it is broken
  2 genres                    which support carries a rigid template, against its own base rate
  3 formats                   recurrent motifs of functional categories, against a Markov null
  4 functions                 headings, qualifiers, totals, sub-counts, quantity profiles
  5 morphology                endings shared by several stems, against a shuffled-endings null
  6 anchoring                 a bilingual or external name list, against a bigram null
  7 affiliation               phonotactics against candidate languages, with a shuffled control

Steps 6 and 7 need material from outside the corpus and are skipped when it is not supplied.
"""
import random
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from math import comb


@dataclass
class CorpusProfile:
    """The language-specific facts. Everything optional; a missing one skips its test."""
    commodities: set = field(default_factory=set)     # logograms of goods
    totals: set = field(default_factory=set)          # terms of summation
    separator: str = ''                               # token that separates entries
    broken: dict = field(default_factory=dict)        # unit -> 'intact' | 'broken'
    name_elements: list = field(default_factory=list)  # from a bilingual, for step 6
    candidates: dict = field(default_factory=dict)    # language -> word list, for step 7
    unit_sep: str = '-'                               # inside a word


def _binom_tail(k, n, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


class Survey:
    def __init__(self, documents, profile=None, seed=0):
        self.docs = documents
        self.p = profile or CorpusProfile()
        self.rng = random.Random(seed)
        self.out = {}

    # ---------- helpers
    def _is_num(self, t):
        return bool(re.fullmatch(r'\d+', t))

    def _is_frac(self, t):
        t = t.replace('≈', '').strip()
        return t in set('JEDBKFLMXY') or bool(re.fullmatch(r'[¹²³⁴⁵⁶⁷⁸⁹][⁄/][₀-₉]+|½|⅓|¼', t))

    def _quantity(self, t):
        return self._is_num(t) or self._is_frac(t)

    EDITION_MARKS = {'\U0001076b', '𐝫', '—', '-', '…', '[', ']', '?', '+', '<', '>'}

    def _units(self, d):
        return [t for t in d.tokens if t not in ('|', self.p.separator)
                and t not in self.EDITION_MARKS and not self._quantity(t)]

    def _intact(self, u):
        return self.p.broken.get(u.lower(), 'intact') == 'intact'

    # ---------- 1 inventory
    def inventory(self):
        units = Counter(u for d in self.docs for u in self._units(d))
        att = Counter(units.values())
        broken = sum(1 for u in units if not self._intact(u))
        r = {'documents': len(self.docs), 'tokens': sum(len(d.tokens) for d in self.docs),
             'units': len(units), 'hapax': att[1],
             'units_3plus': sum(1 for u, c in units.items() if c >= 3),
             'broken_in_every_attestation': broken,
             'sites': Counter(d.site for d in self.docs).most_common(6),
             'supports': Counter(d.support for d in self.docs).most_common(6)}
        self.out['inventory'] = r
        return r

    # ---------- 2 genres
    def genres(self, min_docs=5):
        """Template rigidity: share of a genre's units that recur across its documents,
        against the same measure over the whole corpus."""
        by = defaultdict(list)
        for d in self.docs:
            by[d.support].append(d)
        base_units = Counter(u for d in self.docs for u in self._units(d))
        base = sum(1 for u, c in base_units.items() if c > 1) / max(len(base_units), 1)
        rows = []
        for g, ds in by.items():
            if len(ds) < min_docs:
                continue
            c = Counter(u for d in ds for u in self._units(d))
            if not c:
                continue
            rate = sum(1 for u, n in c.items() if n > 1) / len(c)
            rows.append({'genre': g, 'documents': len(ds), 'rigidity': round(rate, 3),
                         'over_base': round(rate - base, 3)})
        r = {'base': round(base, 3), 'genres': sorted(rows, key=lambda x: -x['over_base'])}
        self.out['genres'] = r
        return r

    # ---------- 3 formats
    def formats(self, k=5, reps=40, min_count=4):
        from .formats import FormatModel, category, COMMODITY, TOTALS
        COMMODITY.update(self.p.commodities)
        TOTALS.update(self.p.totals)
        M = FormatModel([(d.id, [t for t in d.tokens if t != '|']) for d in self.docs], seed=1)
        rows = M.motifs(k, reps=reps, min_count=min_count)[:8]
        for r in rows:
            r['documents'] = M.documents_with(r['motif'])[:8]
        self.out['formats'] = rows
        return rows

    # ---------- 4 functions
    def functions(self, min_units=3):
        """min_units: documents with fewer units are excluded from the first-position test.
        A corpus of one-sign labels (sealings, nodules) puts every unit in first position and
        manufactures headings; on Linear A this produced eight false candidates before the
        filter was added (12 September 2026)."""
        first, tot = Counter(), Counter()
        hosts = defaultdict(set)
        qty = defaultdict(list)
        for d in self.docs:
            toks = [t for t in d.tokens if t != '|']
            if len([t for t in toks if not self._quantity(t) and t != self.p.separator]) < min_units:
                for t in toks:
                    if '+' in t and t.split('+')[0] in self.p.commodities:
                        hosts[t.split('+')[-1]].add(t.split('+')[0])
                continue
            seen = False
            for i, t in enumerate(toks):
                if self._quantity(t) or t == self.p.separator:
                    continue
                if self._intact(t):
                    tot[t] += 1
                    if not seen:
                        first[t] += 1; seen = True
                if '+' in t and t.split('+')[0] in self.p.commodities:
                    hosts[t.split('+')[-1]].add(t.split('+')[0])
                if i + 1 < len(toks) and self._quantity(toks[i + 1]):
                    qty[t].append(toks[i + 1])
        base = sum(first.values()) / max(sum(tot.values()), 1)
        heads = []
        for u, n in tot.items():
            k = first[u]
            if n >= 3 and k >= 2:
                p = _binom_tail(k, n, base)
                if p < 0.05:
                    heads.append({'unit': u, 'first': k, 'of': n, 'p': round(p, 5)})
        quals = [{'syllable': s, 'commodities': sorted(h)} for s, h in hosts.items() if len(h) >= 2]
        r = {'first_position_base': round(base, 3), 'documents_used': sum(1 for d in self.docs if len([t for t in d.tokens if t != '|' and not self._quantity(t) and t != self.p.separator]) >= min_units),
             'heading_candidates': sorted(heads, key=lambda x: x['p'])[:10],
             'qualifiers': quals,
             'note': 'p values are bare; correct by the number of units tested before filing'}
        self.out['functions'] = r
        return r

    # ---------- 5 morphology
    def endings(self, min_stems=3, reps=100):
        us = [u.lower() for d in self.docs for u in self._units(d) if self._intact(u)]
        # a script that writes no separator inside the word is split into characters; the unit
        # must be declared, because the ratio depends on it (Linear A by syllable 2.3, Iberian
        # by letter 4.5 and by semi-syllabic unit 1.4, measured 10-11 September 2026)
        hyphened = [u for u in us if self.p.unit_sep in u]
        if len(hyphened) >= 0.2 * max(len(us), 1):
            words = {tuple(u.split(self.p.unit_sep)) for u in hyphened}
            unit = 'declared separator'
        else:
            words = {tuple(u) for u in us if len(u) >= 3}
            unit = 'character'
        def count(ws):
            be = defaultdict(set)
            for w in ws:
                if len(w) >= 2 and w[:-1] in ws:
                    be[w[-1]].add(w[:-1])
            return {e: s for e, s in be.items() if len(s) >= min_stems}
        obs = count(words)
        nl = []
        ws = list(words)
        for _ in range(reps):
            ends = [w[-1] for w in ws]; self.rng.shuffle(ends)
            nl.append(len(count({w[:-1] + (e,) for w, e in zip(ws, ends)})))
        mean = sum(nl) / max(len(nl), 1)
        r = {'unit': unit, 'words': len(words), 'endings': len(obs), 'null_mean': round(mean, 1),
             'ratio': round(len(obs) / mean, 1) if mean else None,
             'p': round(sum(1 for x in nl if x >= len(obs)) / max(len(nl), 1), 3),
             'top': sorted(((e, len(s)) for e, s in obs.items()), key=lambda x: -x[1])[:10]}
        self.out['endings'] = r
        return r

    # ---------- 6 anchoring
    def anchoring(self, reps=500):
        if not self.p.name_elements:
            self.out['anchoring'] = {'skipped': 'no external name list supplied'}
            return self.out['anchoring']
        forms = {u.lower().replace(self.p.unit_sep, '') for d in self.docs for u in self._units(d) if self._intact(u)}
        big = defaultdict(Counter)
        for w in forms:
            s = '<' + w + '>'
            for a, b in zip(s, s[1:]):
                big[a][b] += 1
        def gen(n):
            out, cur = [], '<'
            for _ in range(n):
                nxt = [c for c in big[cur] if c != '>']
                if not nxt:
                    break
                cur = self.rng.choices(nxt, [big[cur][c] for c in nxt])[0]; out.append(cur)
            return ''.join(out)
        by_len = defaultdict(list)
        for el in self.p.name_elements:
            by_len[len(el.lower().replace(self.p.unit_sep, ''))].append(el)
        rows = []
        for n, els in by_len.items():
            draws = sorted(sum(1 for w in forms if gen(n) in w) for _ in range(reps))
            for el in els:
                e = el.lower().replace(self.p.unit_sep, '')
                obs = sum(1 for w in forms if e in w)
                import bisect
                p = 1 - bisect.bisect_left(draws, obs) / len(draws)
                rows.append({'element': el, 'forms': obs, 'p': round(p, 3)})
        k = sum(1 for r in rows if r['p'] < 0.05)
        r = {'tested': len(rows), 'above_null': k, 'expected_by_chance': round(0.05 * len(rows), 1),
             'bonferroni': round(0.05 / max(len(rows), 1), 4),
             'elements': sorted(rows, key=lambda x: x['p'])[:15]}
        self.out['anchoring'] = r
        return r

    # ---------- 7 affiliation
    def affiliation(self, reps=200):
        if not self.p.candidates:
            self.out['affiliation'] = {'skipped': 'no candidate corpora supplied'}
            return self.out['affiliation']
        from .normalize import Normalizer
        import math
        N = Normalizer('consonantal')
        def prof(sk):
            c = Counter()
            for s in sk:
                s = '#' + s + '#'
                for a, b in zip(s, s[1:]):
                    c[a + b] += 1
            t = sum(c.values()) or 1
            return {k: v / t for k, v in c.items()}
        def jsd(p, q):
            keys = set(p) | set(q)
            m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
            kl = lambda a: sum(a[k] * math.log(a[k] / m[k]) for k in a if a[k] > 0)
            return 0.5 * kl(p) + 0.5 * kl(q)
        mine = N.words([u for d in self.docs for u in self._units(d) if self._intact(u)])
        pm = prof(mine)
        nulls = []
        for _ in range(reps):
            pool = [ch for s in mine for ch in s]; self.rng.shuffle(pool)
            out, i = [], 0
            for s in mine:
                out.append(''.join(pool[i:i + len(s)])); i += len(s)
            nulls.append(prof(out))
        rows = []
        for lang, words in self.p.candidates.items():
            pc = prof(N.words(words))
            d = jsd(pm, pc)
            nd = [jsd(n, pc) for n in nulls]
            rows.append({'language': lang, 'distance': round(d, 3),
                         'null_mean': round(sum(nd) / len(nd), 3),
                         'p': round(sum(1 for x in nd if x <= d) / len(nd), 3)})
        r = {'candidates': sorted(rows, key=lambda x: x['distance'])}
        self.out['affiliation'] = r
        return r

    # ---------- everything
    def run(self):
        self.inventory(); self.genres(); self.formats(); self.functions()
        self.endings(); self.anchoring(); self.affiliation()
        return self.out

    def report(self):
        if not self.out:
            self.run()
        o, L = self.out, []
        i = o['inventory']
        L.append(f"# Survey\n\n## 1. Inventory\n{i['documents']} documents, {i['tokens']} tokens, "
                 f"{i['units']} distinct units, {i['hapax']} of them attested once, "
                 f"{i['units_3plus']} attested three times or more.")
        if i['broken_in_every_attestation']:
            L.append(f"{i['broken_in_every_attestation']} units are broken in every attestation "
                     f"({100 * i['broken_in_every_attestation'] / max(i['units'], 1):.0f}%): they are excluded from every test below.")
        L.append(f"Sites: {', '.join(f'{a} {b}' for a, b in i['sites'])}. Supports: {', '.join(f'{a} {b}' for a, b in i['supports'])}.")
        g = o['genres']
        L.append(f"\n## 2. Genres\nBase rate of recurring units in the whole corpus: {g['base']}.\n")
        L += [f"- {r['genre']}: {r['documents']} documents, rigidity {r['rigidity']} ({r['over_base']:+} over base)" for r in g['genres'][:6]]
        L.append("\n## 3. Formats (motifs of functional categories against a Markov null)\n")
        L += [f"- `{r['motif']}` {r['observed']} times, null {r['null']}, ratio {r['ratio']}: {', '.join(r['documents'][:5])}" for r in o['formats'][:6]]
        f = o['functions']
        L.append(f"\n## 4. Functions\nFirst-position base rate {f['first_position_base']} over {f['documents_used']} documents with three or more units.\n")
        L += [f"- heading candidate {r['unit']}: {r['first']}/{r['of']}, p={r['p']}" for r in f['heading_candidates'][:8]]
        L += [f"- qualifier {r['syllable']}: on {', '.join(r['commodities'])}" for r in f['qualifiers'][:8]]
        L.append(f"({f['note']})")
        e = o['endings']
        L.append(f"\n## 5. Morphology (unit: {e['unit']})\n{e['endings']} endings shared by three or more attested bare stems, "
                 f"null {e['null_mean']}, ratio {e['ratio']}, p={e['p']}. "
                 f"Most shared: {', '.join(f'-{a} ({b})' for a, b in e['top'][:8])}.")
        a = o['anchoring']
        if 'skipped' in a:
            L.append(f"\n## 6. Anchoring\nSkipped: {a['skipped']}.")
        else:
            L.append(f"\n## 6. Anchoring\n{a['above_null']} of {a['tested']} external name elements occur above a "
                     f"bigram null ({a['expected_by_chance']} expected by chance; Bonferroni {a['bonferroni']}).\n")
            L += [f"- {r['element']}: {r['forms']} forms, p={r['p']}" for r in a['elements'][:10]]
        af = o['affiliation']
        if 'skipped' in af:
            L.append(f"\n## 7. Affiliation\nSkipped: {af['skipped']}.")
        else:
            L.append("\n## 7. Affiliation (consonant-skeleton phonotactics, shuffled control)\n")
            L += [f"- {r['language']}: {r['distance']} against null {r['null_mean']}, p={r['p']}" for r in af['candidates']]
        return '\n'.join(L)
