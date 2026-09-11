"""A dictionary of the corpus in which every field says where it came from and when.

Not a lexicon: Younger's already exists and catalogues attestations with their readings. This is
the complement — for each unit, what its distribution measures, what the literature says with whom
and when, what evidence bears on it and in which direction, and what would refute it.

The design follows from what went wrong in this project's first week. Three lessons are built in:

1. **Every field carries its source and its year.** An identification made in 1955, before GORILA,
   with an incomplete corpus, is not the same kind of claim as one made in 2025 with the corpus
   catalogued and searchable. The year is not a ranking — older is often better argued — but it
   records what the author had in front of them.

2. **Evidence is typed and signed, not counted.** Three weak supports do not equal one strong one:
   the KU-PA reading had three and fell, because one of them was a ligature that does not exist.
   Each piece of evidence records its kind (distribution, arithmetic, documentary parallel,
   chemistry, archaeobotany, etymology) and its direction (for, against, neutral), because kinds
   are independent of each other and a chemical result weighs differently from an etymology.

3. **What would refute it is a field.** A unit with no refutation condition is not assessable, and
   this dictionary says so rather than letting it pass.

    from kuro import Dictionary
    d = Dictionary.load('data/derived/dictionary.json')
    d.gaps()                      # units with measured behaviour but no proposed reading
    d.contested()                 # units where evidence points both ways
    d.by_evidence('chemistry')    # units with chemical evidence
"""
import json, os
from collections import Counter, defaultdict

KINDS = ('distribution', 'arithmetic', 'documentary_parallel', 'chemistry',
         'archaeobotany', 'etymology', 'palaeography', 'context')
DIRECTIONS = ('for', 'against', 'neutral')
STATUS = ('established', 'proposed', 'disputed', 'measured_only', 'untouched')


class Entry(dict):
    """One unit of the corpus. Every claim in it names its source and its year."""

    @property
    def evidence_for(self):
        return [e for e in self.get('evidence', []) if e.get('direction') == 'for']

    @property
    def evidence_against(self):
        return [e for e in self.get('evidence', []) if e.get('direction') == 'against']

    @property
    def independent_kinds(self):
        """How many distinct kinds of evidence support it. Kinds, not pieces."""
        return len({e['kind'] for e in self.evidence_for})

    def summary(self):
        f, a = self.evidence_for, self.evidence_against
        kinds = ', '.join(sorted({e['kind'] for e in f})) or 'none'
        s = (f"{self['form']} [{self.get('status', 'untouched')}]\n"
             f"  behaviour : {self.get('behaviour', 'not measured')}\n"
             f"  gloss     : {self.get('gloss', '-')}\n"
             f"  support   : {len(f)} pieces over {self.independent_kinds} kinds ({kinds})")
        if a:
            s += f"\n  AGAINST   : {len(a)} — " + '; '.join(
                f"{e['kind']}, {e['source']} {e['year']}: {e['note']}" for e in a)
        if self.get('refuted_by'):
            s += f"\n  refuted by: {self['refuted_by']}"
        else:
            s += "\n  refuted by: NOT STATED — the claim is not assessable as it stands"
        return s


class Dictionary:
    def __init__(self, entries=None):
        self.entries = {e['form']: Entry(e) for e in (entries or [])}

    @classmethod
    def load(cls, path):
        with open(path, encoding='utf-8') as f:
            return cls(json.load(f))

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(list(self.entries.values()), f, ensure_ascii=False, indent=1)

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, form):
        return self.entries[form]

    def gaps(self):
        """Units whose behaviour is measured but for which nobody has proposed a reading.

        This is where a new claim can be made, and it is the point of the whole object.
        """
        return sorted(f for f, e in self.entries.items()
                      if e.get('behaviour') and not e.get('gloss'))

    def contested(self):
        """Units with evidence pointing both ways. A count of supports would hide these."""
        return sorted(f for f, e in self.entries.items()
                      if e.evidence_for and e.evidence_against)

    def unassessable(self):
        """Units with a proposed reading and no stated refutation condition."""
        return sorted(f for f, e in self.entries.items()
                      if e.get('gloss') and not e.get('refuted_by'))

    def by_evidence(self, kind):
        return sorted(f for f, e in self.entries.items()
                      if any(x['kind'] == kind for x in e.get('evidence', [])))

    def by_year(self):
        """Claims grouped by the year they were made, with what the author had available."""
        out = defaultdict(list)
        for f, e in self.entries.items():
            for ev in e.get('evidence', []):
                out[ev['year']].append((f, ev['source'], ev['kind'], ev['direction']))
        return dict(sorted(out.items()))

    def report(self):
        st = Counter(e.get('status', 'untouched') for e in self.entries.values())
        kinds = Counter(x['kind'] for e in self.entries.values() for x in e.get('evidence', []))
        lines = [f'{len(self)} units', '',
                 'by status: ' + ', '.join(f'{k} {v}' for k, v in st.most_common()), '',
                 'evidence by kind: ' + ', '.join(f'{k} {v}' for k, v in kinds.most_common()), '',
                 f'gaps (measured, unread): {len(self.gaps())}',
                 f'contested (evidence both ways): {len(self.contested())}',
                 f'unassessable (read, no refutation stated): {len(self.unassessable())}']
        return '\n'.join(lines)
