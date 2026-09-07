# kuro (KU-RO, "total"): null models, calibration and confounder tests for small epigraphic corpora

**Alberto Acedo**, Biome Makers Inc.
Draft v0.1, 6 September 2026. Target: Journal of Open Source Software (short paper + repository review).

## Summary

kuro is a small Python package for the statistical analysis of epigraphic corpora that are too small, too fragmentary or too poorly understood to be read: Linear A, Proto-Elamite, proto-cuneiform, Iberian, Etruscan. It does not decipher. It answers, with a permutation null behind every claim, what a corpus can and cannot support: whether two groups of documents differ in register beyond the sampling floor, whether an affix forms root/derivative pairs above chance, whether sign-strings co-occur or exclude one another against a fixed-margin null, whether a vocabulary is compartmented by document type or by scribal hand, whether totals add up, and whether form matches with an external lexicon exceed what shuffled syllables produce. It also mines expert commentaries for expressions of doubt, so that tests can be aimed where specialists stopped.

## Statement of need

Statistical work on undeciphered scripts has produced readings by sound-matching that any large lexicon supplies (Duhoux 1989; Nepal and Perono Cacciafoco 2024) and, at the other extreme, the view that nothing in such corpora is testable (Petrakis and Steele 2025). What the field lacks is a common toolbox in which each distributional claim is tied to the null model that preserves what the claim does not explain, and in which instruments are calibrated on corpora with known answers before they are applied to unknown ones. kuro provides loaders for the formats the community already uses (the LinearA Explorer JSON, CDLI ATF exports, SigLA-style sign tables, CSV text tables) and the tests, so that an epigrapher can run a calibrated analysis in a few lines and report negatives with their numbers.

## Functionality

- Corpus model: documents with site, support, date, hand and tokens in reading order.
- Null models: label shuffling, shuffling within strata, the curveball fixed-margin randomisation (Strona et al. 2014), and syllable shuffling with word lengths preserved.
- Tests: profile distance (Jensen-Shannon) with sampling floor and document-level null; affix root/derivative pairs; positional frame of long sign-strings; metacommunity co-occurrence and co-exclusion; monopolies by document type; confounder analysis (hand versus type) with within-stratum permutation; totals arithmetic with fractions; form screen against an external catalogue; singleton rate by string length.
- Doubt mining over commentaries.

## Validation

The package reproduces, on Etruscan, the genitive before *clan*, the chronology of syncope and the geography of the sibilants; on Eteocypriot against Cypriot Greek, the separation by word-final syllables; on Proto-Elamite, Dahl's numeral systems by object class, the institutional header and the name/commodity partition; on Uruk against Susa, the inheritance of the sexagesimal system, the adaptation of the capacity system and the invention of the decimal; on Iberian, Untermann's onomastic formants and the southern S56 and northeastern -ḿi isoglosses. Its use on Linear A is reported in Acedo (2026a, 2026b, 2026c).

Beyond reproducing published results, three checks quantify what the package offers on a task with known answers (classifying a Linear B sign-group as a personal name or a term, from distribution alone, on 64 words whose meaning the field has established). A decision rule written from the literature reaches 0.63 balanced accuracy; the distributional model reaches 0.77, and following the model where it is confident and the rules elsewhere reaches 0.80 in raw accuracy. A learning curve shows that twenty annotated words suffice for three correct answers in four (0.74), with slow improvement afterwards. And in the task a researcher actually performs, prioritising what to inspect, ordering by the model's probability finds half the terms after 22 reviews instead of 32 at random, about a third less work. The three checks are reported with their limits: they are performed on Linear B, the rules are ours, and the labelled set is small. A study with human experts, designed after Assael et al. (2022), is planned and will be added when participants are available.

## Acknowledgements

Data: LinearA Explorer (R. Hogan), SigLA (E. Salgarella and S. Castellan), CDLI, Hesperia (via Luo et al. 2021), Larth (G. Vico), ETP (R. Wallace et al.).

## References

Acedo, A. 2026a. Nombres minoicos formados sobre fitónimos. Draft.
Acedo, A. 2026b. Qué puede afirmarse de un corpus de siete mil signos. Draft.
Acedo, A. 2026c. Tres archivos, un instrumento. Draft.
Duhoux, Y. 1989. Le linéaire A: problèmes de déchiffrement. In Problems in Decipherment, Louvain-la-Neuve, 59-119.
Nepal, A. and F. Perono Cacciafoco 2024. Minoan cryptanalysis. Information 15(2), 73.
Petrakis, V. and P. M. Steele 2025. The Wor(l)ds of Linear A: some concluding thoughts. In The Wor(l)ds of Linear A, Athens, 167-176.
Strona, G., D. Nappo, F. Boccacci, S. Fattorini and J. San-Miguel-Ayanz 2014. A fast and unbiased procedure to randomize ecological binary matrices with fixed row and column totals. Nature Communications 5, 4114.
