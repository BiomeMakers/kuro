"""The model as proposer, not as reader.

The Reader turns a scholar's paragraph into a proposition; it cannot say more than the paragraph.
The Hypothesizer is given the DATA of one unread unit — a dossier built from the corpus and the
Linear B parallels — and asked for a reading with its refutation condition. The reading then enters
the same cycle as everything else. Two guards sit in front of the cycle:

  1. every unit the model names must exist in the corpus (on 10 Sep 2026 the reading prompt
     invented a unit in 22% of passages); a proposition naming an unknown unit is dropped before
     any null is spent on it;
  2. the reading must name a CLASS the profile test can check (persons, livestock, bulk, fine,
     liquid, staple, textile, qualifier, heading, total, name) — a reading that names none is
     recorded as untestable, not measured.
"""
import re
from collections import Counter

CLASSES = ('persons', 'livestock', 'bulk', 'fine', 'liquid', 'staple', 'textile',
           'qualifier', 'heading', 'total', 'name', 'unknown')

PROMPT = """You are proposing a reading for ONE unit of Linear A, an undeciphered Bronze Age script used
for accounts. You cannot know what the word means. You CAN say what kind of thing the unit is,
from how the administration counted it, and what would prove that wrong.

The dossier below is everything the corpus records about the unit, plus what its sign looks like
in Linear B if the sign is shared. Read it as an accountant reads a ledger.

Dossier:
{dossier}

Classes you may propose (one only):
  persons    counted in whole units, often large, listed with VIR
  livestock  whole units, sheep/goat/ox signs, species-by-sex lists
  bulk       a staple counted in large whole figures, fractions rare (grain)
  fine       a valued commodity in small fractional amounts (spice, saffron, metal)
  liquid     oil or wine: fractions at the ordinary rate, grades marked by an added sign
  staple     figs, olives, cyperus: fractions at the ordinary rate, medium figures
  textile    whole units, with an added sign for type
  qualifier  a bare syllable that is ADDED to commodity signs (KU in GRA+KU). A ligature such as
             OLE+U is NOT a qualifier: it is a graded commodity (class liquid/staple/fine); the
             qualifier there is U. Propose 'qualifier' only for the bare syllable.
  heading    a word that opens the document (a record or transaction label)
  total      a word before a figure that sums the entries above it
  name       a party (person or place) entered in a list with a figure. Note: the corpus cannot
             tell a party from a commodity written in syllables; 'name' is judged as a category
             (list entry), never as a reading. Prefer another class if the dossier allows one.
  unknown    when the dossier does not support any of the above

Answer with EXACTLY this form and nothing else:
UNIT: <the unit, exactly as written in the dossier>
CLASS: <one class from the list>
READING: <one sentence: what the unit is, in the terms of the class>
WHY: <the two or three facts of the dossier that support it>
REFUTED_BY: <one concrete observation in the corpus that would show the reading false>
CONFIDENCE: <low | medium | high>
"""


def build_dossier(unit, entry, profile, first_rate, base_first, companions, sites, supports,
                  seal_note=None, lb_note=None, hosts=None):
    """A plain-text ledger view of one unit."""
    lines = [f'UNIT: {unit}',
             f'kind: {"logogram" if "-" not in unit else "syllabic sign-group"}'
             + (' (ligature: base sign + added syllable)' if '+' in unit else ''),
             f'attestations: {entry.get("attestations", 0)} in {entry.get("documents", 0)} documents',
             f'sites: {", ".join(f"{s} {n}" for s, n in sites.most_common(4))}',
             f'supports: {", ".join(f"{s} {n}" for s, n in supports.most_common(3))}']
    if profile:
        lines.append(f'with a figure: {profile["n"]} times; fractions in {profile["frac"]} of them '
                     f'({100*profile["frac_rate"]:.0f}%; corpus base rate for commodity signs 27%); '
                     f'largest figure {profile["max"]}')
    else:
        lines.append('with a figure: never')
    lines.append(f'in first position of a tablet: {first_rate[0]} of {first_rate[1]} '
                 f'(base rate for all units {100*base_first:.0f}%)')
    if companions:
        lines.append('other units in the same documents: '
                     + ', '.join(f'{u} ({n})' for u, n in companions.most_common(6)))
    if hosts:
        lines.append(f'as an added syllable, attached to: {", ".join(hosts)}')
    if seal_note:
        lines.append(f'on nodules: {seal_note}')
    if lb_note:
        lines.append(f'Linear B: {lb_note}')
    return '\n'.join(lines)


class Hypothesizer:
    def __init__(self, model, known_units):
        self.model = model
        self.known = set(known_units)
        self.log = []

    def parse(self, text):
        f = {}
        for line in text.strip().splitlines():
            m = re.match(r'\s*(UNIT|CLASS|READING|WHY|REFUTED_BY|CONFIDENCE):\s*(.*)', line)
            if m:
                f[m.group(1)] = m.group(2).strip()
        if not all(k in f for k in ('UNIT', 'CLASS', 'READING', 'REFUTED_BY')):
            return None
        f['CLASS'] = f['CLASS'].lower().strip('. ')
        if f['CLASS'] not in CLASSES:
            return None
        return f

    def propose(self, unit, dossier):
        try:
            answer = self.model(PROMPT.format(dossier=dossier))
        except Exception as e:
            self.log.append({'unit': unit, 'outcome': 'error', 'why': str(e)[:80]}); return None
        f = self.parse(answer)
        if f is None:
            self.log.append({'unit': unit, 'outcome': 'unparsed', 'why': answer[:80]}); return None
        # guard 1: the unit it names must be the one asked and must exist
        named = re.findall(r'[A-Z*][A-Z0-9*₂₃+\-\[\]?]{1,}', f['UNIT'] + ' ' + f['READING'])
        unknown = [u for u in named if len(u) > 1 and u not in self.known and not re.fullmatch(r'[A-Z]{1,2}', u)]
        if f['UNIT'] != unit:
            self.log.append({'unit': unit, 'outcome': 'wrong_unit', 'why': f['UNIT']}); return None
        if unknown:
            self.log.append({'unit': unit, 'outcome': 'invented', 'why': ', '.join(unknown)[:80]}); return None
        if f['CLASS'] == 'unknown':
            self.log.append({'unit': unit, 'outcome': 'unknown', 'why': f.get('WHY', '')[:80]}); return None
        self.log.append({'unit': unit, 'outcome': 'proposal', 'why': f['CLASS'] + ': ' + f['READING'][:70]})
        return {'unit': unit, 'class': f['CLASS'], 'reading': f['READING'], 'why': f.get('WHY', ''),
                'refuted_by': f['REFUTED_BY'], 'confidence': f.get('CONFIDENCE', '')}

    def report(self):
        c = Counter(e['outcome'] for e in self.log)
        return f'{len(self.log)} units proposed on: ' + ', '.join(f'{k} {v}' for k, v in c.items())
