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

## Reports

```
python -m kuro report HT23a          # what is known about a document, and what is not
python -m kuro sign CYP              # where a sign occurs, with what, with p-values
python -m kuro arithmetic HT117a     # totals that add up, and fixed ratios
python -m kuro verify HT23a          # what to check against the primary edition, and why
python -m kuro capture site          # does a group difference track how the data was recorded?
python -m kuro classify --out c.csv  # classify every document by content, not by support
python -m kuro power --documents 224 --tokens 2481   # what a corpus this size can support
```

A report lists each element of a document with its state — established reading, function fixed by arithmetic or position, or unidentified — its quantity, the proportions normalised to the smallest fraction, and the arithmetic that checks. It proposes no readings: it states what the corpus supports and what it leaves open. Sign profiles give company, position, quantities and hypergeometric p-values against the commodity classes; association is not identification, and the report says so.

Every report ends with a verification sec
## What is in this repository

| path | what it holds |
|---|---|
| `kuro/` | the package: corpus loaders, nulls, tests, reports, provenance, power thresholds |
| `tests/` | 32 tests on synthetic data with known answers, plus the manifest and language-pair checks |
| `manifest.json` | every figure the papers assert, the withdrawn claims, the prior art and its holders |
| `scripts/check_manifest.py` | reads the papers and fails when any of those drifts |
| `biblio/` | which work bears on which claim, and whether it has been read |
| `docs/papers/` | the papers as PDFs; `sources/` holds the Markdown they are built from |
| `docs/analysis/` | the analyses behind every claim in the papers, in the order they were made |
| `docs/state/` | where the work stands, what is unchecked, whom to write to, what to obtain |
| `docs/REGISTRO_cambios.md` | what was done each day and why |
| `data/raw/` | corpus sources, with `README.md` recording provenance and what may be redistributed |
| `data/derived/` | derived data: the content classification, the 2019 classification, the Etruscan corpus |
| `docs/IDEAS.md` | things worth doing later, each with the condition that would make it worth the work |

tion. It flags three patterns, each of which produced a false result in our own work: an integer quantity where the same sign normally carries a fraction; a sign-group split by a line break that joins into a word attested elsewhere; and a rare ligature built on a frequent word. It fires on 0.3% of the Linear A corpus, and the three documents that misled us are among them. Signs are verified at sigla.phis.me; the primary edition, GORILA, is not machine-readable.

## Where the figures come from

Every figure a report states carries its provenance: `[C]` computed from the loaded corpus in this
session (reports print the corpus SHA-256, so two runs on different files cannot be confused),
`[L]` taken from the literature and cited, `[~]` illustrative and not verified here. The practice is
adopted from Briakos (2026). It matters because a measured 26-28% yield and a recalled "olive oil
gives 15-25%" must not read alike.

And before any comparison between groups, `capture_control` asks whether the groups differ in how
much text survives per document. On Linear A the answer is yes — document length spreads 311% across
sites and 274% across supports — so profile comparisons must be matched on length. Briakos (2026)
found the corresponding trap in the visual domain, where an apparent geographic separation tracked
photographic brightness at r = 0.990.

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
| `Corpus.tablet_report(id)` | what is known about this document, and what is not? |
| `Corpus.sign_profile(sign)` | where does this sign occur, with what, with what significance? |
| `Corpus.arithmetic_check(id)` | do the totals add up, and are there fixed ratios? |
| `Corpus.classify(doc)` | is this document accounting, votive, a label, or indeterminate? |
| `Corpus.verify(id)` | what in this document should be checked against the primary edition, and why? |
| `power_report(n_documents, n_tokens)` | which instruments have power at this corpus size, and which do not? |
| `capture_artifact(docs, signal, capture)` | is this difference a property of the data or of how it was captured? |
| `group_cohesion(items, labels, features)` | does a proposed classification capture real structure, or the classifier's categories? |
| `factor_effects(items, factors, features)` | which of several confounded factors explains shared features, and which is redundant? |
| `Fact.computed / cited / illustrative` | a number with its provenance, so measured and remembered figures never mix |
| `Corpus.capture_control(factor)` | does a difference between groups track how the documents were recorded? |

## Provenance of figures

Every figure a report states carries a marker: `[C]` computed here, with the hash of the source file; `[L]` taken from the literature, with the source named; `[~]` illustrative only. The practice is adapted from Briakos (2026), who labels each statistic in his thesis the same way. A report that mixes a measured value with a remembered one is the easiest kind of work to discredit and the hardest error to see from inside.

## Corpus size

`power_report` states which instruments have power at a given size, with the evidence for each threshold: co-exclusion needs around 800 documents (zero pairs at 224, thirteen at 830), a network descriptor with test-retest reliability needs tens of thousands (noise at 224, 2.9% between halves at 34,000), and frequency rank-matching for phonetic values needs around 10,000 sign tokens — that last one from Briakos (2026), who calibrates it against a synthetic Linear B corpus.

## One source of truth for the figures

`manifest.json` holds every figure the papers assert: corpus counts, key results, p-values, the
claims that have been withdrawn and why, the results that have a published precedent and whose it
is, and the identifications the field currently disputes. `python scripts/check_manifest.py`
reads the paper sources in `docs/papers/sources/` and fails when a paper states a withdrawn claim
without withdrawing it, states a prior-art result without citing its holder, or when a figure the
manifest fixes has drifted. Two tests keep the manifest itself honest.

The practice is adapted from OpenEtruscan (github.com/Eddy1919/openEtruscan), which built it after
an external audit found four different version numbers across four of its public surfaces. The
problem it solves here is the same: in a single week, the corpus size, the votive document count,
the hapax rate and the number of Assur recipes were each corrected in one file while the older
value survived in another.

## Prior art

`biblio/works.json` lists every work known to bear on our claims, whether we hold it and whether it has been read; `biblio/claims.json` links each claim in `docs/papers/` to those works with a status. `python -m kuro biblio` prints what is unchecked.

The status CONFLICT deserves a note: Corazza et al. (2021) and Montecchi (2009) give different values for the fraction sign D (1/6 against 1/3). Where the literature disagrees, the resolution is arithmetic and not authority: the system that makes more tablets balance is the better one, and that test is in `Corpus.arithmetic_check`.

## Rules of use

Function before form. Verify signs in the primary edition, not in a derived transliteration. Check whether a difference is a property of the data or of how the data was captured. Report negatives with their numbers. Stop where the corpus stops.

## Citation

Acedo, A. (2026). kuro: null models, calibration and confounder tests for small epigraphic corpora (v0.1.0). Biome Makers Inc. See `CITATION.cff`.

## Data acknowledgements

LinearA Explorer (R. Hogan), SigLA (E. Salgarella and S. Castellan), CDLI, Hesperia (via Luo et al. 2021), Larth (G. Vico), ETP (R. Wallace et al.). Corpora are not redistributed here; the loaders read the formats those projects publish.

## License

MIT.

## Parked ideas

`docs/IDEAS.md` records things worth doing later, with the condition that would make each worth the work.
