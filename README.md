<p align="center"><img src="docs/img/kuro_logo.png" width="520"></p>

# kuro

**KU-RO** (𐙂𐘜, AB 81 + AB 02) is the Linear A word for "total": the one word everyone reads, and the one proven by arithmetic. kuro is a Python package that does for small epigraphic corpora what KU-RO does for a tablet: it adds things up and says what the total supports.

It does not decipher. It answers, with a permutation null behind every claim, what a corpus can and cannot support: whether two groups of documents differ in register beyond the sampling floor; whether an affix forms root/derivative pairs above chance; whether sign-strings co-occur or exclude one another against a fixed-margin null; whether a vocabulary is compartmented by document type or by scribal hand; whether totals add up; and whether form matches with an external lexicon exceed what shuffled syllables produce. It also mines expert commentaries for expressions of doubt, so that tests can be aimed where specialists stopped.

## Install

```
pip install pykuro        # the distribution is called pykuro; the module is kuro
```

## Quickstart (Linear A, LinearA Explorer JSON)

```python
from kuro import load_lineara, profile_distance, affix_pairs, metacommunity, confounder_jaccard, totals_check
docs = load_lineara('inscriptions.json')
tablets = [d for d in docs if d.support == 'Tablet' and d.site == 'Haghia Triada']
vocab = sorted(set(w for d in docs for w in d.words()))
affix_pairs(vocab, 'ka', 'prefix')      # {'observed': 5, 'null_mean': 1.4, 'p': 0.01, ...}
totals_check(next(d for d in docs if d.id == 'HT117a'))   # KU-RO 10 = ten names with 1
```

See `examples/linear_a_quickstart.py`. The corpora themselves are fetched with `python3 data/fetch.py` (see `data/README.md` for sources and licences); `data/derived/` holds the tables produced by this project. Loaders also exist for CDLI ATF exports (Proto-Elamite, proto-cuneiform) and CSV text tables (Iberian, Etruscan).

## What it has been calibrated on

Etruscan (genitive before *clan*, syncope by period, sibilants by city), Eteocypriot vs Cypriot Greek (word-final syllables), Proto-Elamite (Dahl's numeral systems by object class, the M157 header, the name/commodity partition), Uruk vs Susa (inheritance of the sexagesimal system, adaptation of the capacity system, invention of the decimal), Iberian (Untermann's onomastic formants, the southern S56 and north-eastern -mi isoglosses). Its use on Linear A is reported in the papers under `docs/papers/`.

## Tests

```
pip install -e ".[test]"
pytest -q          # 11 tests on synthetic data with known answers
```

Each test plants a structure (a register difference, a prefix, mutually exclusive blocks, a vocabulary that depends on the hand, a tablet whose total adds up) and checks that the instrument sees it and that the nulls preserve what they must: margins, word lengths, strata.

## Function reference

| function | question it answers |
|---|---|
| `profile_distance(A, B)` | do two groups of documents differ in register beyond the sampling floor? |
| `affix_pairs(vocab, affix, kind)` | does an affix form root/derivative pairs above chance? |
| `family_positions(strings)` | do particular signs concentrate at the start or end of long strings? |
| `metacommunity(docs)` | which strings co-occur or exclude each other against a fixed-margin null? |
| `monopolies(docs, type_of)` | which vocabulary is exclusive to one document type? |
| `confounder_jaccard(docs, a, b)` | is shared vocabulary explained by factor a or by factor b? |
| `totals_check(doc)` | do the quantities of a section add up to its total? |
| `form_screen(vocab, catalogue, match)` | do form matches with an external lexicon exceed shuffled syllables? |
| `hapax_by_length(docs)` | how does the singleton rate vary with string length? |
| `doubts(glob)` | where does an expert commentary express doubt? |

## Rules of use

Function before form. Verify signs in the primary edition, not in a derived transliteration. Report negatives with their numbers. Stop where the corpus stops.

## Citation

Acedo, A. (2026). kuro: null models, calibration and confounder tests for small epigraphic corpora (v0.1.0). Biome Makers Inc. See `CITATION.cff`.

## Data acknowledgements

LinearA Explorer (R. Hogan), SigLA (E. Salgarella and S. Castellan), CDLI, Hesperia (via Luo et al. 2021), Larth (G. Vico), ETP (R. Wallace et al.). Corpora are not redistributed here; the loaders read the formats those projects publish.

## License

MIT.
