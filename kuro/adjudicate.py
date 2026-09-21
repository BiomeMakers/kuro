"""A bench for decipherment claims: does a proposal survive what the corpus already fixes?

A decipherment is a pair: values for the signs, and meanings for the words. Both are usually
judged by internal coherence, which is the wrong test, because a wrong assignment applied
consistently also produces a coherent lexicon. The corpus fixes 56 functions by distribution,
independently of what language it turns out to be: what precedes a sum is a total, what is
followed by the oil logogram is the offering, what never carries a logogram is not the object.
Any proposal has to agree with those, and the measure of a proposal is how many it satisfies
and how many it contradicts.

    from kuro.adjudicate import Bench
    b = Bench.from_dictionary('data/derived/dictionary.json')
    print(b.score({'KU-RO': 'total, all'}, values={'*301': 'na'}, family_roots=['ksp','hrs']))

The three parts of the verdict are independent: agreement with the measured functions,
the phonotactic consequence of the proposed values against a control, and whether the common
roots of the claimed family recur in the corpus.
"""
import json
import math
import random
import re
from collections import Counter

CLASSES = {
    'total': r'total|sum|deficit|balance',
    'heading': r'heading|opening|transaction term|introduc',
    'offering': r'offering|libation|dedicat',
    'qualifier': r'qualifier|grade|fine|variety|quality',
    'commodity': r'grain|oil|wine|olive|fig|cyperus|wool|textile|sheep|goat|ox|barley|emmer|sesame|cumin|coriander|commodit',
    'person': r'person|man|woman|worker|people|persons',
    'place': r'place name|toponym|place',
    'name': r'personal name|name',
    'quantity': r'quantity|measure|weight|unit|allocation|ration',
}


NEGATION = re.compile(r"\b(does not|is not|not a|never|cannot be)\b")


def classify(gloss):
    """The functional class of a gloss, or None. A gloss that denies a class returns
    'not-<class>': the inventory records what a unit is NOT (JA-SA-SA-RA-ME does not designate
    the offering), and reading that as a positive would manufacture false agreement."""
    g = (gloss or '').lower()
    if NEGATION.search(g):
        for k, p in CLASSES.items():
            if re.search(p, g):
                return 'not-' + k
        return None
    # order matters: a more specific class is tested before the one that contains its words
    for k, p in CLASSES.items():
        if re.search(p, g):
            return k
    return None


class Bench:
    def __init__(self, fixed):
        """fixed: {unit: (class, gloss, status)} from the measured inventory."""
        self.fixed = fixed

    @classmethod
    def from_dictionary(cls, path):
        d = json.load(open(path, encoding='utf-8'))
        if isinstance(d, list):                      # a list of entry records
            entries = {e.get('form', e.get('unit', '')): e for e in d}
        else:
            entries = d.get('entries', d)
        fixed = {}
        for f, e in entries.items():
            g = e.get('gloss')
            if not g:
                continue
            c = classify(g)
            if c:
                fixed[f.upper()] = (c, g, e.get('status', '?'))
        return cls(fixed)

    def agreement(self, proposal):
        """proposal: {unit: proposed gloss}. Returns agreements, contradictions, untouched."""
        agree, clash, unknown = [], [], []
        for u, g in proposal.items():
            u = u.upper()
            if u not in self.fixed:
                unknown.append(u); continue
            measured, mgloss, status = self.fixed[u]
            proposed = classify(g)
            if proposed is None:
                unknown.append(u)
            elif measured.startswith('not-') and proposed == measured[4:]:
                clash.append((u, measured, proposed, mgloss, g))
            elif proposed == measured:
                agree.append((u, measured, g))
            else:
                clash.append((u, measured, proposed, mgloss, g))
        return {'agree': agree, 'clash': clash, 'unclassifiable': unknown,
                'coverage': len([u for u in proposal if u.upper() in self.fixed]),
                'of_fixed': len(self.fixed)}

    @staticmethod
    def phonotactics(units, target_words, values=None, reps=200, seed=0):
        """Distance of the corpus to a target language under the proposed sign values,
        against a control that shuffles the syllables. Returns both, so the gap is readable."""
        rng = random.Random(seed)
        values = values or {}

        def skel(u):
            out = ''
            for s in u.lower().split('-'):
                v = values.get(s.upper(), values.get(s, None))
                if v is not None:
                    s = v
                m = re.match(r'([bdgkmnpqrstwzjhl]?)', s)
                if m and m.group(1):
                    out += m.group(1)
            return out

        def prof(ws):
            c = Counter()
            for w in ws:
                s = '#' + w + '#'
                for a, b in zip(s, s[1:]):
                    c[a + b] += 1
            t = sum(c.values()) or 1
            return {k: v / t for k, v in c.items()}

        def jsd(p, q):
            ks = set(p) | set(q)
            m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in ks}
            kl = lambda a: sum(a[k] * math.log(a[k] / m[k]) for k in a if a[k] > 0)
            return 0.5 * kl(p) + 0.5 * kl(q)

        sk = [s for s in (skel(u) for u in units) if s]
        pt = prof([w for w in target_words if w])
        d = jsd(prof(sk), pt)
        nulls = []
        for _ in range(reps):
            pool = [ch for s in sk for ch in s]; rng.shuffle(pool)
            out, i = [], 0
            for s in sk:
                out.append(''.join(pool[i:i + len(s)])); i += len(s)
            nulls.append(jsd(prof(out), pt))
        mean = sum(nulls) / len(nulls)
        return {'distance': round(d, 4), 'control': round(mean, 4), 'gap': round(mean - d, 4),
                'p': round(sum(1 for x in nulls if x <= d) / len(nulls), 3)}

    @staticmethod
    def root_recurrence(units, roots, values=None):
        """Do the common roots of the claimed family recur as whole skeletons?"""
        values = values or {}

        def skel(u):
            out = ''
            for s in u.lower().split('-'):
                v = values.get(s.upper(), values.get(s, None))
                if v is not None:
                    s = v
                m = re.match(r'([bdgkmnpqrstwzjhl]?)', s)
                if m and m.group(1):
                    out += m.group(1)
            return out

        c = Counter(skel(u) for u in units)
        return {r: c.get(r, 0) for r in roots}

    def report(self, proposal, units=None, target_words=None, values=None, roots=None):
        a = self.agreement(proposal)
        L = [f"Agreement with the measured inventory: {len(a['agree'])} of {a['coverage']} units "
             f"touched ({a['of_fixed']} fixed in all)."]
        for u, m, g in a['agree']:
            L.append(f"  agrees   {u}: measured {m}, proposed '{g}'")
        for u, m, p, mg, g in a['clash']:
            L.append(f"  CLASHES  {u}: measured {m} ({mg[:40]}), proposed {p} ('{g}')")
        if units is not None and target_words:
            ph = self.phonotactics(units, target_words, values)
            L.append(f"Phonotactics under the proposed values: distance {ph['distance']}, "
                     f"control {ph['control']}, gap {ph['gap']} (p={ph['p']}).")
        if units is not None and roots:
            rr = self.root_recurrence(units, roots, values)
            L.append("Root recurrence: " + ', '.join(f"{k} {v}" for k, v in rr.items()))
        return '\n'.join(L)
