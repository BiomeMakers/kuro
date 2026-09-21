from kuro.corpus import Document
from kuro.survey import Survey, CorpusProfile


def _docs():
    return [Document(id=f'd{i}', site='S', support='tablet',
                     tokens=['A-DU', 'GRA', '10', 'X-Y', '2', 'KU-RO', '12']) for i in range(6)] + \
           [Document(id=f'e{i}', site='T', support='label', tokens=['Z-W']) for i in range(4)]


def test_inventory_counts_and_skips_edition_marks():
    s = Survey(_docs(), CorpusProfile(commodities={'GRA'}, totals={'KU-RO'}))
    inv = s.inventory()
    assert inv['documents'] == 10 and 'A-DU' not in s.EDITION_MARKS
    assert inv['units_3plus'] >= 3


def test_one_sign_documents_do_not_manufacture_headings():
    s = Survey(_docs(), CorpusProfile(commodities={'GRA'}, totals={'KU-RO'}))
    f = s.functions()
    assert all(r['unit'] != 'Z-W' for r in f['heading_candidates'])


def test_steps_needing_outside_material_say_so():
    s = Survey(_docs(), CorpusProfile())
    assert 'skipped' in s.anchoring() and 'skipped' in s.affiliation()
