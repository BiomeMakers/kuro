import os
import textwrap

import pytest

from kuro import rsti

XML = textwrap.dedent("""\
    <result><ochre><spatialUnit uuid="u-1">
      <context displayPath="Projects/RSTI/Ugarit/Ras Shamra/Royal Palace/The Eastern Archives/Room 56"/>
      <identification><label>RS 16.001</label></identification>
      <observations><observation><properties>
        <property><label>KTU reference</label><value>KTU 4.269</value></property>
        <property><label>Length</label><value>163</value></property>
        <property><label>Width</label><value>112</value></property>
        <property><label>Thickness</label><value>27</value></property>
      </properties></observation></observations>
    </spatialUnit></ochre></result>
    """)


@pytest.fixture
def one(tmp_path):
    (tmp_path / 'a.xml').write_text(XML)
    return str(tmp_path)


def test_a_record_yields_its_series_and_genre(one):
    rec = rsti.load(one)[0]
    assert rec['series'] == '4'
    assert rec['genre'] == 'administrative'


def test_the_findspot_gives_room_and_named_archive(one):
    rec = rsti.load(one)[0]
    assert rsti.room(rec) == 'Room 56'
    assert rsti.archive(rec) == 'The Eastern Archives'


def test_dimensions_are_numbers(one):
    rec = rsti.load(one)[0]
    assert rsti.size_profile([rec]) == [(163.0, 112.0, 27.0)]


def test_series_by_archive_counts_genres(one):
    table = rsti.series_by_archive(rsti.load(one))
    assert table['The Eastern Archives']['administrative'] == 1


def test_a_record_with_no_ktu_has_no_genre(tmp_path):
    (tmp_path / 'b.xml').write_text(XML.replace('<property><label>KTU reference</label><value>KTU 4.269</value></property>', ''))
    rec = rsti.load(str(tmp_path))[0]
    assert rec['genre'] is None
