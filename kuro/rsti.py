"""The Ras Shamra Tablet Inventory as a comparandum for the Minoan archive.

Ugarit was Crete's direct trading partner in the fourteenth century, and its palace held
five physically separate archives. RSTI publishes the object catalogue of 4,528 inscribed
finds under CC BY-NC-SA, with findspot to the room, KTU series, and tablet dimensions. The
text editions are not published, so nothing here reads a word: what it measures is the shape
of the archive — where documents of each series were kept, and what size they are — which is
the same thing kuro measures in Linear A and which can be compared without a decipherment.
"""
import glob
import os
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict


SERIES = {'1': 'literary and religious', '2': 'letters', '3': 'legal',
          '4': 'administrative', '5': 'scribal exercises', '6': 'inscribed objects',
          '7': 'uncertain or fragmentary', '9': 'Akkadian'}


def parse_record(path):
    """One RSTI object record, reduced to the fields that travel."""
    root = ET.parse(path).getroot()
    unit = root.find('.//spatialUnit')
    if unit is None:
        return None
    rec = {'uuid': unit.get('uuid')}
    ctx = root.find('.//context')
    rec['findspot'] = ctx.get('displayPath') if ctx is not None else None
    for prop in root.iter('property'):
        label, value = prop.find('label'), prop.find('value')
        if label is None or value is None or not label.text:
            continue
        rec[label.text] = value.text
    ktu = rec.get('KTU reference')
    rec['series'] = ktu.split()[1].split('.')[0] if ktu and '.' in ktu else None
    rec['genre'] = SERIES.get(rec['series'])
    for field in ('Length', 'Width', 'Thickness'):
        try:
            rec[field] = float(rec[field])
        except (TypeError, ValueError):
            rec[field] = None
    return rec


def load(directory):
    out = []
    for path in sorted(glob.glob(os.path.join(directory, '*.xml'))):
        try:
            rec = parse_record(path)
        except ET.ParseError:
            continue
        if rec:
            out.append(rec)
    return out


def room(rec):
    """The last element of the findspot: the room or courtyard the tablet was kept in."""
    fs = rec.get('findspot')
    return fs.split('/')[-1] if fs else None


def archive(rec):
    """The named archive a record belongs to, where the excavators identified one."""
    fs = rec.get('findspot') or ''
    m = re.search(r'/(The [A-Za-z]+ Archives)', fs)
    return m.group(1) if m else None


def series_by_archive(records):
    """Which KTU series each palace archive held: the shape of the administration."""
    table = defaultdict(Counter)
    for rec in records:
        a, s = archive(rec), rec.get('genre')
        if a and s:
            table[a][s] += 1
    return table


def size_profile(records, genre=None):
    """Tablet dimensions, optionally for one genre. Returns the list of (l, w, t)."""
    out = []
    for rec in records:
        if genre and rec.get('genre') != genre:
            continue
        l, w, t = rec.get('Length'), rec.get('Width'), rec.get('Thickness')
        if l and w:
            out.append((l, w, t))
    return out
