# data/

Two kinds of file live here, and they are treated differently when this repository becomes public.

## raw/  — third-party corpora (NOT redistributed in the public repository)
Downloaded by `fetch.py` from the projects that publish them. Cite the project, not this repository.

| file | source | licence / conditions |
|---|---|---|
| `inscriptions.json` (Linear A) | LinearA Explorer, R. Hogan (github.com/mwenge/lineara.xyz), from GORILA (Godart & Olivier 1976-1985, École française d'Athènes) | repository code MIT; the transliterations are GORILA's. Cite Godart & Olivier and Hogan. Known defect: Zakros tablets labelled as stone vessels. |
| `sigla_corpus.json` (Linear A signs) | SigLA, E. Salgarella & S. Castellan (sigla.phis.me), via the pyaegean redistribution | CC BY-NC-SA 4.0. Non-commercial; ask before redistributing. |
| `linearb_inscriptions.json` | linearb.xyz (same author as the Explorer), from the standard editions | as above. |
| `proto_elamita.atf`, `proto_elamita_cat.csv` | CDLI (cdli.earth), period filter "Proto-Elamite" | CDLI transliterations CC BY-NC-SA; catalogue CC0 in part. Cite CDLI. |
| `uruk.atf`, `uruk_cat.csv` | CDLI, periods "Uruk IV" and "Uruk III" | as above. |
| `iberico_hesperia_luo2021.csv` | Luo et al. 2021 (github.com/j-luo93/DecipherUnsegmented), derived from Banco de Datos Hesperia (UCM) | Hesperia is consultation-only and supplies exports on request. Do NOT redistribute; cite Hesperia and Luo et al. |
| `linearb/` (full Linear B corpus, lexicon, form counts) | linearb.xyz JS bundles (R. Hogan) | no licence stated; transliterations from the standard editions. Not redistributed; `fetch.py linearb_js` + `scripts/extract_linearb.py`. |
| `nodules_seals_younger.json` | J. Younger's commentary pages via the Explorer | © John Younger; not redistributed. The derived table `derived/nodules_sign_seal.json` keeps only document, site, sign and seal number/motif. |
| `neurodecipher/` | Luo, Cao & Barzilay 2019 data | no licence stated; not redistributed. |
| `iberian/iberian.csv` | as `iberico_hesperia_luo2021.csv` above | Hesperia: consultation only. Not redistributed. |
| `candidates/`, `grambank/` | CDLI bulk ATF (CC BY 4.0), TLHdig 25.1 (Zenodo 15459134), Grambank (CC BY 4.0) | large; fetched by `scripts/fetch_candidates.py`, Grambank by hand. |
| Larth / ETP (Etruscan) | github.com/GianlucaVico/Larth-Etruscan-NLP; ETP (R. Wallace et al.) | see each repository. Larth contains OCR noise and some Umbrian texts; filter before use. |

## derived/ — our own tables (redistributable, CC BY 4.0)
Produced by the scripts of this project from the corpora above; they contain no third-party text beyond what a citation would quote.

| file | what it is |
|---|---|
| `entry_tables.json` | one row per accounting entry of each Haghia Triada tablet (word, logogram, quantity), with sections |
| `seals_roundels.json` | seal number, motif and number of impressions per Linear A roundel, from Younger's commentaries and SigLA |
| `hands_tab.json` | hand attributions used in the confounder test (from GORILA V via the Explorer) |
| `skeletons.json` | consonantal skeletons of the Linear A vocabulary used in the language screen |
| `metaweb_A.json` | documents × words matrix and the curveball results |
| `classifier_rank.json`, `etrusco_desconocidas_funcion.json` | classifier outputs (function per unlabelled word) |
| `dictionary.json` | the functional inventory: every unit with attestations, intact flag, status, gloss, evidence for and against, refutation condition |
| `error_rates.json` | measured error rate of each instrument on material where nothing should be found |
| `nodules_sign_seal.json` | sign × seal of 801 HT nodules (facts only) |
| `value_search_anchored.json`, `value_search_luwian_21.json` | the sound-value search against each candidate, with its control |
| `iberian_ascoli.json`, `iberian_onomastics.json`, `ending_systems.json` | the Iberian anchoring and the ending profiles |
| `literature_run.json`, `units_run.json`, `proposals_run.json`, `*_cycle.json` | the reader and hypothesizer runs and their verdicts |

## Before making this repository public
1. `git rm -r --cached data/raw` and add `data/raw/` to `.gitignore` (already listed there, commented out).
2. Keep `derived/`, `fetch.py` and this README.
3. Deposit the full working package (including `raw/`) in Zenodo under restricted access if you need a citable snapshot.
Note: files already committed remain in git history; if `raw/` has been committed and the repository is to be opened, rewrite history (`git filter-repo`) or start a clean public repository.
