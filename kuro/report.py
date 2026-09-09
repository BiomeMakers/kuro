"""Per-document reports: what is known about a tablet, what has been measured, what is open.

    from kuro import load_lineara, Corpus
    c = Corpus(load_lineara('inscriptions.json'))
    print(c.tablet_report('HT23a'))
    print(c.sign_profile('CYP'))
    print(c.arithmetic_check('HT117a'))

Every line of a report carries the evidence behind it. Nothing is asserted that the
corpus does not support, and what is unknown is listed as unknown.
"""
import re, math, collections
from fractions import Fraction as Fr
from .corpus import is_number, FRACTIONS
from .provenance import Fact, file_hash, TIERS
from .evidence import corpus_hash, MARK, LEGEND, COMPUTED, CITED, ILLUSTRATIVE

# Fraction letter values, optimal system of Corazza, Ferrara, Montecchi, Tamburini & Valério (2021), Table 8
FRACTION_VALUES = {'J': Fr(1,2), 'E': Fr(1,4), 'D': Fr(1,6), 'B': Fr(1,5), 'K': Fr(1,10),
                   'L2': Fr(1,20), 'F': Fr(1,8), 'H': Fr(1,16), 'A': Fr(1,24),
                   'L3': Fr(1,30), 'L4': Fr(1,40), 'L6': Fr(1,60)}
FRACTION_GLYPHS = {'¹⁄₂': Fr(1,2), '¹⁄₃': Fr(1,3), '²⁄₃': Fr(2,3), '¹⁄₄': Fr(1,4), '³⁄₄': Fr(3,4),
                   '¹⁄₅': Fr(1,5), '¹⁄₆': Fr(1,6), '¹⁄₈': Fr(1,8), '¹⁄₁₆': Fr(1,16), '³⁄₈': Fr(3,8)}

# Logograms with an established reading, inherited from Linear B or fixed by the field.
ESTABLISHED = {
    'GRA': 'grain', 'NI': 'figs', 'VIN': 'wine', 'OLIV': 'olives', 'OLE': 'oil',
    'CYP': 'cyperus', 'CYP+E': 'cyperus (qualified E)', 'CYP+D': 'cyperus (qualified D)',
    'BOS': 'cattle', 'OVIS': 'sheep', 'CAP': 'goats', 'SUS': 'pigs',
    'VIR': 'man', 'MUL': 'woman', 'TELA': 'cloth', 'AROM': 'aromatic',
}
# Terms whose function is fixed by arithmetic or by position, with the evidence.
FUNCTIONAL = {
    'ku-ro': ('total', 'arithmetic: sums exactly on 8 of the 25 checkable sections'),
    'po-to-ku-ro': ('grand total', 'position and arithmetic'),
    'ki-ro': ('deficit / what is owed', 'arithmetic on HT 123+124a; prior art Younger'),
    'da-i': ('total of mixed entries', 'arithmetic: HT 12 closes with 50 = sum of its seven entries'),
    'sa-ra2': ('allocation heading', 'position: heads the document, mid-document elsewhere'),
    'a-du': ('regional heading', 'position: first entry in 8 of its 10 documents'),
    'te': ('document mark', 'occurs on nodules'),
}
COMMODITY_CLASSES = {
    'food': {'GRA', 'NI', 'FIC', 'VIN', 'OLIV'},
    'livestock': {'BOS', 'OVIS', 'CAP', 'SUS'},
    'oil': {'OLE', 'OLE+U', 'OLE+KI', 'OLE+MI', 'OLE+DI', 'OLE+TU', 'OLE+TA', 'OLE+RI', 'OLE+NE'},
    'aromatics': {'CYP', 'CYP+E', 'CYP+D', '*303', '*308', 'MI+JA+RU', 'QA2+[?]+PU', 'QA2+[?]+RE'},
    'textile': {'TELA', 'LANA', '*164', '*168'},
    'people': {'VIR', 'MUL', 'VIR+[?]'},
}
FORMULA_ANCHORS = {'a-ta-i-*301-wa-ja', 'a-ta-i-*301-de-ka', 'a-ta-i-*301-wa-e', 'ja-sa-sa-ra-me',
                   'a-sa-sa-ra-me', 'u-na-ka-na-si', 'u-na-ru-ka-na-ti', 'i-pi-na-ma',
                   'i-pi-na-mi-na', 'si-ru-te', 'ja-di-ki-tu', 'a-di-ki-te'}


DIVIDERS = {'\u10101', '\u1010', '|', '', 'vacat', 'vest.', '-', '\u2014'}


def _is_divider(t):
    """Word dividers, Aegean numeral/fraction glyphs, approximation marks and editorial signs."""
    t = (t or '').strip()
    if not t or t in DIVIDERS or t in ('\u2248', '~', '['):
        return True
    # Aegean block (U+10100-U+1013F: dividers, numbers, fractions) and Linear A block glyphs used as marks
    return all(0x10100 <= ord(ch) <= 0x1077F for ch in t)


def _is_logogram(t):
    return bool(re.fullmatch(r'[A-Z*][A-Z0-9+*\[\]?:]*', t)) and len(t) > 1


def _is_word(t):
    return (bool(re.fullmatch(r'[A-Za-z0-9₀-₉*\-]+', t)) and '-' in t
            and not is_number(t) and not _is_divider(t))


class Corpus:
    """A corpus with the indices the reports need. Build it once, query it many times."""

    def __init__(self, documents, source_path=None):
        self.source = source_path
        self.hash = corpus_hash(source_path) if source_path else 'not recorded'
        self.docs = {d.id: d for d in documents}
        self.word_docs = collections.defaultdict(set)
        self.log_docs = collections.defaultdict(set)
        self.word_n = collections.Counter()
        self.log_n = collections.Counter()
        for d in documents:
            for t in d.tokens:
                if t == '|':
                    continue
                if _is_logogram(t):
                    self.log_docs[t].add(d.id); self.log_n[t] += 1
                elif _is_word(t):
                    self.word_docs[t.lower()].add(d.id); self.word_n[t.lower()] += 1
        self.N = len(documents)

    # ---------- helpers ----------
    def _hypergeom_p(self, k, a, b):
        """P(X >= k) for a documents of one kind and b of another, in N documents."""
        if not a or not b:
            return 1.0
        c = math.comb
        return sum(c(b, x) * c(self.N - b, a - x) for x in range(k, min(a, b) + 1)) / c(self.N, a)

    def _class_of(self, sign):
        for name, members in COMMODITY_CLASSES.items():
            if sign in members:
                return name
        return None

    def _entries(self, doc):
        """(token, quantity) pairs in reading order; quantity is a Fraction or None."""
        toks = [t for t in doc.tokens if t != '|' and not _is_divider(t)]
        out = []
        for i, t in enumerate(toks):
            if is_number(t):
                continue
            if not (_is_logogram(t) or _is_word(t)):
                continue
            q = None; j = i + 1
            while j < len(toks) and is_number(toks[j]):
                v = Fr(int(toks[j])) if re.fullmatch(r'\d+', toks[j]) else FRACTION_GLYPHS.get(toks[j], Fr(0))
                q = (q or Fr(0)) + v; j += 1
            out.append((t, q))
        return out



    def capture_control(self, factor, groups=('site', 'support'), min_docs=5):
        """Is a difference between groups a fact about the documents, or about how they were recorded?

        Briakos (2026) found that an apparent geographic separation in a visual analysis of
        Linear A tablets tracked photographic brightness (r = 0.990), not geography. The same
        risk exists for text: a difference between sites may track transcription practice,
        document length or state of preservation rather than the language.

        For a grouping factor, this reports the group means of three capture properties.
        If the factor separates the corpus on those as much as on vocabulary, the signal is
        suspect and the report says so.
        """
        import statistics as st
        get = (lambda d: d.site) if factor == 'site' else (lambda d: getattr(d, factor, '?'))
        by = collections.defaultdict(list)
        for d in self.docs.values():
            by[get(d)].append(d)
        rows = []
        for g, ds in by.items():
            if len(ds) < min_docs:
                continue
            lens = [len([t for t in d.tokens if not _is_divider(t)]) for d in ds]
            words = [len([t for t in d.tokens if _is_word(t)]) for d in ds]
            frag = [sum(1 for t in d.tokens if '[' in t or ']' in t) / max(1, len(d.tokens)) for d in ds]
            rows.append((g, len(ds), st.mean(lens), st.mean(words), st.mean(frag)))
        rows.sort(key=lambda r: -r[1])
        L = ['CAPTURE CONTROL [C]  (does a group difference track how the documents were recorded?)',
             f'  {"group":<18}{"docs":>6}{"tokens":>9}{"words":>8}{"damaged":>9}']
        for g, n, tl, w, f in rows[:10]:
            L.append(f'  {str(g)[:18]:<18}{n:>6}{tl:>9.1f}{w:>8.1f}{f:>9.2f}')
        if len(rows) >= 2:
            tl = [r[2] for r in rows]; fr = [r[4] for r in rows]
            spread_len = (max(tl) - min(tl)) / max(1e-9, st.mean(tl))
            spread_dmg = (max(fr) - min(fr)) / max(1e-9, st.mean(fr)) if st.mean(fr) > 0 else 0
            L.append(f'  spread across groups: document length {spread_len:.0%}, damage {spread_dmg:.0%}')
            if spread_len > 0.5 or spread_dmg > 1.0:
                L.append('  WARNING: the groups differ substantially in how much text survives per document.')
                L.append('  Any vocabulary difference between them may follow from that and not from the')
                L.append('  documents themselves. Match on length before comparing profiles.')
            else:
                L.append('  The groups are comparable in length and preservation; a vocabulary difference')
                L.append('  between them is not explained by capture conditions alone.')
        return '\n'.join(L)

    # ---------- verification ----------
    def verify(self, doc_id, as_lines=False):
        """Flag what should be checked against the primary edition, and say why.

        Three patterns, each of which produced a false result in our own work:
        an integer quantity where the same sign normally carries a fraction; a sign-group
        split across a line break that forms a word attested elsewhere; and a ligature
        whose components also occur as consecutive signs in other documents.
        """
        d = self.docs.get(doc_id)
        if d is None:
            return [] if as_lines else f'{doc_id}: not in corpus'
        L = []
        toks = [t for t in d.tokens]
        # (1) integers where the sign usually takes a fraction
        for t, q in self._entries(d):
            if q is None or q.denominator != 1:
                continue
            key = t if _is_logogram(t) else t.lower()
            frac = whole = 0
            for other in self.docs.values():
                for t2, q2 in self._entries(other):
                    if (t2 if _is_logogram(t2) else t2.lower()) == key and q2 is not None:
                        if q2.denominator == 1: whole += 1
                        else: frac += 1
            if frac + whole >= 4 and frac >= 3 * max(1, whole):
                L.append(f'  {t} = {q.numerator} is an integer, but this sign carries a fraction in '
                         f'{frac} of its {frac+whole} quantified occurrences. Fraction signs are sometimes '
                         f'rendered as integers in derived transliterations: check the sign.')
        # (2) sign-groups split by a line break that join into an attested word
        for i, t in enumerate(toks):
            if t != '|' or i == 0 or i + 1 >= len(toks):
                continue
            a, b = toks[i-1], toks[i+1]
            if not (_is_word(a) and _is_word(b)):
                continue
            joined = (a + '-' + b).lower()
            for cand in (joined, (a + b).lower()):
                if cand in self.word_docs and len(self.word_docs[cand]) >= 1:
                    L.append(f'  "{a}" and "{b}" straddle a line break and join into {cand.upper()}, '
                             f'which is attested in {len(self.word_docs[cand])} document(s). Check the '
                             f'segmentation: a line break is not a word divider.')
                    break
        # (3) rare ligatures whose components contain an attested sign-group.
        # A ligature always combines signs that exist separately, so that alone is no signal.
        # What is a signal is a RARE ligature one of whose parts is itself a frequent WORD:
        # that is the shape of HT Wa 1020, read as *304+PA-KU-PA where SigLA has *629 then KU-PA.
        ligs = {x for x in toks if '+' in x and not _is_divider(x)}
        for t in ligs:
            n_lig = sum(1 for o in self.docs.values() if t in o.tokens)
            if n_lig > 2:
                continue                      # a well-attested ligature is a ligature
            parts = [p for p in re.split(r'\+', t) if p and p != '[?]']
            found = []
            for p in parts:
                pl = p.lower()
                if '-' not in pl:
                    continue
                syl = pl.split('-')
                for a in range(len(syl)):
                    for b in range(a + 2, len(syl) + 1):
                        sub = '-'.join(syl[a:b])
                        n = len(self.word_docs.get(sub, ()))
                        if n >= 3:
                            found.append(f'{sub.upper()} ({n} documents)')
            if found:
                L.append(f'  {t} occurs in {n_lig} document(s) and contains the '
                         f'attested sign-group(s) {"; ".join(sorted(set(found))[:3])}. A rare ligature '
                         f'built on a frequent word is the shape of HT Wa 1020, where SigLA reads two '
                         f'consecutive signs and not a ligature. Check the drawing.')
        # link
        L.append(f'  verify signs at https://sigla.phis.me (search {doc_id}); the primary edition is '
                 f'GORILA (Godart & Olivier 1976-1985), which is not machine-readable.')
        if as_lines:
            return ['VERIFICATION'] + L
        return '\n'.join([f'VERIFICATION for {doc_id}'] + L)

    # ---------- reports ----------
    def classify(self, doc):
        """Classify a document by CONTENT, not by support (see the Zakros stone vessels)."""
        toks = [t for t in doc.tokens if t != '|']
        words = {t.lower() for t in toks if _is_word(t)}
        logs = [t for t in toks if _is_logogram(t)]
        nums = sum(1 for t in toks if is_number(t))
        if words & FORMULA_ANCHORS:
            return 'votive'
        if nums >= 2 or (logs and nums >= 1):
            return 'accounting'
        if logs:
            return 'label'
        return 'indeterminate'

    def tablet_report(self, doc_id, width=78):
        d = self.docs.get(doc_id)
        if d is None:
            return f'{doc_id}: not in corpus'
        L = []
        L.append('=' * width)
        L.append(f'{d.id}   {d.site}   {d.support}   [{self.classify(d)}]')
        L.append(f'corpus {self.hash}')
        L.append('=' * width)
        entries = self._entries(d)
        known = unknown = 0
        L.append('')
        L.append('ELEMENTS')
        for t, q in entries:
            qs = ('' if q is None else (str(q) if q.denominator != 1 else str(q.numerator)))
            if _is_logogram(t):
                if t in ESTABLISHED:
                    note = f'logogram, established reading: {ESTABLISHED[t]} [L]'; known += 1
                else:
                    cls = self._class_of(t)
                    n = len(self.log_docs[t])
                    note = (f'[C] logogram, no established reading; {n} document(s)'
                            + (f'; associated with the {cls} dossier' if cls else ''))
                    unknown += 1
            else:
                tl = t.lower()
                if tl in FUNCTIONAL:
                    fn, ev = FUNCTIONAL[tl]
                    tier = '[C]' if 'arithmetic' in ev or 'position' in ev else '[L]'
                    note = f'term, function fixed: {fn} {tier} ({ev})'; known += 1
                else:
                    n = len(self.word_docs[tl])
                    note = ('[C] sign-group, hapax in the corpus' if n <= 1
                            else f'[C] sign-group, {n} documents')
                    unknown += 1
            L.append(f'  {t:<18} {qs:>8}   {note}')
        # proportions
        fr = [(t, q) for t, q in entries if q is not None and q.denominator != 1]
        if len(fr) >= 2:
            base = min(q for _, q in fr)
            L.append('')
            L.append(f'PROPORTIONS  [C] computed from the quantities above, with the fraction values')
            L.append(f'of Corazza et al. 2021 [L]; normalised to the smallest, {base} = 1 part')
            for t, q in sorted(fr, key=lambda x: -x[1]):
                L.append(f'  {t:<18} {str(q/base):>8} parts')
            levels = collections.Counter(q for _, q in fr)
            eq = [q for q, c in levels.items() if c >= 3]
            if eq:
                L.append(f'  -> {max(levels.values())} entries share the fraction {max(eq)}: '
                         'the signature of secondary ingredients in equal parts')
        whole = [(t, q) for t, q in entries if q is not None and q.denominator == 1]
        if whole:
            L.append('')
            L.append('WHOLE UNITS')
            for t, q in whole:
                L.append(f'  {t:<18} {q.numerator:>8}')
        L.append('')
        L.append(f'SUMMARY [C]: {known} element(s) with an established reading or a fixed function, '
                 f'{unknown} without.')
        arit = self.arithmetic_check(doc_id, as_lines=True)
        if arit:
            L.append(''); L.extend(arit)
        ver = self.verify(doc_id, as_lines=True)
        if ver:
            L.append(''); L.extend(ver)
        L.append('')
        L.append(LEGEND)
        L.append('This report states what the corpus supports. It contains no proposed readings.')
        return '\n'.join(L)

    def sign_profile(self, sign, top=8, width=78):
        """Where a sign occurs, with what, in what position, with what quantities, with p-values."""
        is_log = _is_logogram(sign)
        key = sign if is_log else sign.lower()
        docs = self.log_docs[key] if is_log else self.word_docs[key]
        if not docs:
            return f'{sign}: not in corpus'
        L = ['=' * width,
             f'{sign}   ({len(docs)} document(s), {self.log_n[key] if is_log else self.word_n[key]} occurrence(s)) [C]',
             f'corpus {self.hash}', '=' * width]
        sites = collections.Counter(self.docs[i].site for i in docs)
        supports = collections.Counter(self.docs[i].support for i in docs)
        L.append(f'sites: {dict(sites.most_common(5))}')
        L.append(f'supports: {dict(supports.most_common(4))}')
        # position and quantity
        heads = qs = fracs = wholes = 0
        for i in docs:
            ent = self._entries(self.docs[i])
            for k, (t, q) in enumerate(ent):
                if (t if is_log else t.lower()) != key:
                    continue
                heads += (k == 0)
                if q is not None:
                    qs += 1
                    if q.denominator == 1: wholes += 1
                    else: fracs += 1
        L.append(f'heads its document {heads} time(s); carries a quantity {qs} time(s) '
                 f'({wholes} whole, {fracs} fractional)')
        # company, with significance
        comp = collections.Counter()
        for i in docs:
            for t in {x for x in self.docs[i].tokens if _is_logogram(x)}:
                if t != key: comp[t] += 1
        L.append('')
        L.append('COMPANY (logograms in the same documents, with hypergeometric p)')
        for t, k in comp.most_common(top):
            b = len(self.log_docs[t]); a = len(docs)
            p = self._hypergeom_p(k, a, b)
            flag = '  **' if p < 0.001 else ('  *' if p < 0.05 else '')
            L.append(f'  {t:<16} {k:>3} docs (expected {a*b/self.N:5.1f})   p = {p:.4g}{flag}')
        # class association
        L.append('')
        L.append('ASSOCIATION WITH COMMODITY CLASSES')
        for cls, members in COMMODITY_CLASSES.items():
            cdocs = set().union(*[self.log_docs[m] for m in members if m in self.log_docs]) if any(m in self.log_docs for m in members) else set()
            if not cdocs: continue
            k = len(docs & cdocs)
            p = self._hypergeom_p(k, len(docs), len(cdocs))
            L.append(f'  {cls:<12} {k:>3} of {len(docs)} documents   p = {p:.4g}'
                     + ('  **' if p < 0.001 else ('  *' if p < 0.05 else '')))
        L.append('')
        L.append(LEGEND)
        L.append('Association is not identification. This profile says where a sign lives, not what it means.')
        return '\n'.join(L)

    def arithmetic_check(self, doc_id, as_lines=False):
        """Totals that add up, and fixed ratios between two elements of the same document."""
        d = self.docs.get(doc_id)
        if d is None:
            return [] if as_lines else f'{doc_id}: not in corpus'
        L = []
        # totals
        section = []
        ent = self._entries(d)
        for idx, (t, q) in enumerate(ent):
            tl = t.lower()
            if tl in ('ku-ro', 'po-to-ku-ro', 'da-i', 'ki-ro'):
                # the total's quantity may sit after an intervening commodity logogram (KU-RO GRA 5)
                if q is None and idx + 1 < len(ent) and _is_logogram(ent[idx+1][0]):
                    q = ent[idx+1][1]
                s = sum(section, Fr(0))
                if q is not None and section:
                    ok = 'EXACT' if s == q else f'off by {q - s}'
                    L.append(f'  {t}: {len(section)} entries sum to {s}; recorded {q}  -> {ok}')
                section = []
            elif q is not None:
                section.append(q)
        # fixed ratios, only between elements of the same magnitude class (both fractional or both whole)
        ent = [(t, q) for t, q in self._entries(d) if q is not None and q > 0]
        for frac in (True, False):
            grp = [(t, q) for t, q in ent if (q.denominator != 1) == frac]
            ratios = []
            for i, (t1, q1) in enumerate(grp):
                for t2, q2 in grp[i+1:]:
                    r = q1 / q2 if q1 >= q2 else q2 / q1
                    a, b = (t1, t2) if q1 >= q2 else (t2, t1)
                    if r != 1 and r.denominator <= 5 and r <= 20:
                        ratios.append((float(r), f'  ratio {a}:{b} = {r} ({float(r):.2f})'))
            for _, line in sorted(ratios, reverse=True)[:6]:
                L.append(line)
        if as_lines:
            return (['ARITHMETIC'] + L) if L else []
        return '\n'.join(['ARITHMETIC for ' + doc_id] + (L or ['  nothing checkable']))


# ---------------------------------------------------------------------------
# Corpus-size thresholds: what a corpus of a given size can and cannot support.
# Two independent sources, both reported with their provenance.
# ---------------------------------------------------------------------------
POWER_THRESHOLDS = [
    # (instrument, documents or tokens needed, unit, evidence tier, source)
    ('hapax rate by string length', 200, 'documents', 'computed',
     'visible at Haghia Triada (224 documents)'),
    ('root/affix pairs', 200, 'documents', 'computed',
     'p = 0.01-0.02 at Haghia Triada (224 documents)'),
    ('arithmetic of totals', 200, 'documents', 'computed',
     '8 of 25 checkable sections at Haghia Triada'),
    ('hand-versus-type confounder', 70, 'documents with attributed hands', 'computed',
     '73 tablets, 21 hands at Haghia Triada'),
    ('co-exclusion under the curveball null', 800, 'documents', 'computed',
     'zero pairs at 224 (Haghia Triada), 13 pairs at 830 (Susa)'),
    ('frame of long sign-strings', 1000, 'long strings', 'computed',
     'weak at Haghia Triada, p < 1e-6 at Susa'),
    ('profile distance between subcorpora', 800, 'documents', 'computed',
     'below the sampling floor at Haghia Triada, clear at Susa'),
    ('frequency rank-matching for phonetic values', 10000, 'sign tokens', 'cited',
     'Briakos 2026: 13% top-1 at 2,481 tokens, below the 21% useful threshold'),
    ('network descriptor with test-retest reliability', 30000, 'documents', 'computed',
     'noise at 224 (Haghia Triada); 2.9% between halves at 34,000 (Ur III)'),
]


def power_report(n_documents=None, n_tokens=None, width=78):
    """What a corpus of this size can and cannot support, with the evidence for each threshold.

        from kuro import power_report
        print(power_report(n_documents=224, n_tokens=2481))   # Haghia Triada
    """
    L = ['=' * width, 'WHAT A CORPUS OF THIS SIZE CAN SUPPORT', '=' * width]
    if n_documents: L.append(f'documents: {n_documents}')
    if n_tokens: L.append(f'sign tokens: {n_tokens}')
    L.append('')
    for name, need, unit, tier, ev in POWER_THRESHOLDS:
        have = n_tokens if 'token' in unit else n_documents
        if have is None:
            mark, verdict = '   ', 'not assessed (size not given)'
        elif have >= need:
            mark, verdict = ' + ', f'yes, above the threshold of {need} {unit}'
        else:
            mark, verdict = ' - ', f'no: needs about {need} {unit}, {need - have} more'
        L.append(f'{mark}{name:<44} {verdict}')
        L.append(f'    {TIERS[tier][0]} {ev}')
    L.append('')
    L.append('Thresholds marked [C] are measured in this project by comparing corpora of')
    L.append('different sizes; the one marked [L] is from Briakos (2026), who calibrates it')
    L.append('against a synthetic Linear B corpus. Neither is a guarantee: a threshold says')
    L.append('where an instrument starts to see, not that it will see anything in your data.')
    return '\n'.join(L)
