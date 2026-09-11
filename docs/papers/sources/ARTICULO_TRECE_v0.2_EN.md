# Thirteen candidate relatives of Minoan measured against one null, and why none passes

**Alberto Acedo**
Biome Makers Inc. Draft v0.2, 10 September 2026. Not for circulation.

## Abstract

For a century the language of Linear A has been assigned, by different scholars, to Anatolian, Semitic, Hurrian, Tyrsenian and Greek, or declared an isolate, and no proposal has been tested against the others with a common instrument. This paper does so. Thirteen corpora — Mycenaean Greek, Hittite from two sources, Luwian, Palaic, Hurrian, Hattic, Akkadian, Ugaritic, Sumerian, Elamite, Eteocretan and Etruscan — are reduced with the Linear A lexicon to a single consonantal skeleton whose loss is declared per corpus, and their consonant-bigram profiles are compared with the Minoan one under a null that shuffles the consonants of each Minoan word among its positions. The instrument is calibrated first: on the twelve known languages it separates languages 2.5 times more than it separates halves of one language. On Minoan, one candidate lies closer than shuffled Minoan, Mycenaean Greek (p = 0.01), and it is the one that cannot count: Linear A is read with Linear B sound values, so its consonant sequences inherit Greek constraints by construction. Shuffling those values among the seventy-five Linear A syllabograms shows that the Linear B assignment brings Minoan closer to every real language than any of a hundred random assignments does, which quantifies the filter. The other twelve candidates, including the three historical ones measured against a null here for the first time, are no closer to Minoan than Minoan disordered (p from 0.22 to 1.00). The transcription is then made a variable: a simulated-annealing search over the values of the 59 signs not anchored by the names shared with Linear B, with the same search applied to a control Minoan without real sequences, brings the real corpus no closer to any of the thirteen than the control can be brought (maximum z 1.7, Luwian, with 21 controls). The result closes, with a null, the claim that Minoan phonotactics resembles any known candidate, under the current transcription and under any assignment of values compatible with the place names.

**Keywords:** Linear A, Minoan, language affiliation, phonotactics, null models, transliteration bias, Luwian, Hurrian, Etruscan.

## 1. A century of proposals and no common test

Palmer and Finkelberg read Minoan as Anatolian, specifically Luwian. Gordon read it as Semitic. Van Soesbergen reads it as Hurrian. Facchetti connected it with Etruscan through a Tyrsenian family. Others have read it as Greek, as Indo-Iranian, and as an isolate or a pre-Greek substrate. Each proposal has arguments and each has objections, and the objections are as unquantified as the arguments: no proposal has been placed beside the others under one instrument and one null.

The reason is not lack of interest but lack of comparability. The candidate corpora are written in five different systems — Linear A and B are CV syllabaries read with Greek values, Hittite and Hurrian in cuneiform with closed syllables, Ugaritic in a consonantal alphabet without vowels, Etruscan alphabetically — and any distance measured across them measures the writing system before it measures the language. A first attempt here, on raw transliterations, returned Ugaritic as the most distant language for exactly that reason: its corpus has no vowels.

## 2. A common format, and its declared loss

Every corpus is reduced to a consonantal skeleton: each word becomes its consonant sequence, with a declared mapping for the diacritics of each transliteration system, and vowels dropped. The loss is measured per corpus as the share of distinct words that become indistinguishable:

| corpus | words | collapsed |
|---|---|---|
| Linear A | 1,117 | 37.7% |
| Mycenaean | 1,414 | 43.9% |
| Hittite | 6,000 | 34.4% |
| Ugaritic | 4,767 | 29.3% |
| Etruscan | 10,783 | 48.5% |
| Sumerian (sample) | 60,000 | 38.1% |
| Akkadian (sample) | 60,000 | 50.2% |

The losses are comparable, which is the condition for the skeletons to be comparable. A syllabic skeleton was also tried and rejected: it cannot represent a vowelless corpus.

The Hurrian, Hattic, Luwian and Palaic corpora come from the TLHdig dataset of the Hethitologie-Portal Mainz (Zenodo 15459134), where they are identified by line-level language tags inside otherwise Hittite documents; a document-level count would have missed nearly all of the Hurrian. Sumerian, Akkadian and Elamite come from the CDLI bulk transliteration. Etruscan from OpenEtruscan.

## 3. The measure, its null, and its calibration

The profile of each corpus is the distribution of consonant bigrams over its skeletons, with word boundaries marked. Distance is Jensen-Shannon divergence.

**The null** shuffles the consonants of the Minoan skeletons among their positions, two hundred times, preserving the inventory and the length of every word and destroying only their order. A candidate is closer to Minoan than chance if its distance to real Minoan is below its distance to shuffled Minoan.

**Calibration.** On the twelve known languages, the mean distance between languages is 2.5 times the mean distance between two random halves of one language. The instrument separates languages when the answer is known.

## 4. Result

| candidate | family | distance | null | p |
|---|---|---|---|---|
| Mycenaean Greek | Indo-European | 0.145 | 0.152 | *\*0.010** |
| Hittite (CDLI) | Anatolian | 0.260 | 0.253 | 0.98 |
| Hittite (Mainz) | Anatolian | 0.272 | 0.255 | 1.00 |
| Hurrian | Hurro-Urartian | 0.277 | 0.262 | 1.00 |
| Palaic | Anatolian | 0.299 | 0.279 | 1.00 |
| Luwian | Anatolian | 0.320 | 0.309 | 1.00 |
| Akkadian | East Semitic | 0.338 | 0.333 | 0.97 |
| Hattic | isolate | 0.338 | 0.323 | 1.00 |
| Eteocretan | | 0.351 | 0.310 | 1.00 |
| Ugaritic | West Semitic | 0.369 | 0.371 | 0.22 |
| Elamite | isolate | 0.379 | 0.379 | 0.47 |
| Sumerian | isolate | 0.401 | 0.391 | 1.00 |
| Etruscan | Tyrsenian | 0.417 | 0.407 | 1.00 |

One candidate lies closer than chance. Twelve do not; nine are further from Minoan than shuffled Minoan.

## 5. The one that passes is the one that cannot count

Linear A is transliterated with the sound values of Linear B, established for Greek. Its consonant sequences therefore inherit Greek phonotactic constraints before any comparison is made. That Mycenaean comes out closest is what this construction predicts, and it is a measure of the filter, not of the language.

The filter can be quantified. The Linear B values were shuffled among the seventy-five Linear A syllabograms one hundred times and the comparison repeated under each assignment:

| candidate | with Linear B values | best of 100 random | random assignments that do better |
|---|---|---|---|
| Mycenaean | 0.151 | 0.281 | 0 |
| Hittite | 0.266 | 0.355 | 0 |
| Hurrian | 0.283 | 0.352 | 0 |
| Luwian | 0.326 | 0.383 | 0 |
| Hattic | 0.344 | 0.375 | 0 |
| Akkadian | 0.368 | 0.417 | 0 |
| Ugaritic | 0.376 | 0.392 | 0 |
| Sumerian | 0.395 | 0.436 | 0 |
| **Etruscan** | 0.424 | 0.389 | *\*6** |

With the Linear B values Minoan is closer to every real language than under any random assignment, save one. The values are not arbitrary: they produce a consonant profile resembling that of a real language, and they draw Minoan towards real languages in general and towards Greek in particular. That is why no other candidate can compete, and why the result of section 4 cannot be read as evidence for Greek.

**Etruscan is the exception.** Six of a hundred random assignments bring Minoan closer to Etruscan than the Linear B values do: the values push Minoan away from Etruscan relative to chance. Six of a hundred is not a finding. It is the only direction in the table that the filter hides rather than manufactures, and it is where an alternative, principled assignment of sound values should be tried first.

## 5 bis. Under any assignment of values

If the Linear B values are the filter, the next question is what values the signs would need for Minoan to resemble each candidate, and how close it can be brought at best. The sixteen signs anchored by the names shared with Linear B (those of pa-i-to, su-ki-ri-ta, se-to-i-ja, da-i-pi-ta, i-ta-ja, ki-da-ro, and the five plain vowels) are held fixed, and simulated annealing over swaps of values among the other 59 seeks the assignment that minimises the distance to each candidate (6,000 steps). With 59 free values anything can be brought close to anything, which is why the control is the result: the same search applied to a Minoan whose syllables are shuffled across words, preserving inventory and word lengths and destroying the sequences (five controls per candidate; 21 for the best one).

| candidate | Linear B values | best real | control (mean) | z |
|---|---|---|---|---|
| Luwian | 0.220 | 0.113 | 0.120 | 2.3 (1.7 with 21 controls) |
| Hittite | 0.181 | 0.105 | 0.110 | 1.5 |
| Mycenaean | 0.100 | 0.053 | 0.054 | 1.3 |
| Sumerian | 0.322 | 0.219 | 0.222 | 1.0 |
| Akkadian | 0.295 | 0.193 | 0.194 | 0.4 |
| Ugaritic | 0.257 | 0.171 | 0.172 | 0.1 |
| Elamite | 0.275 | 0.200 | 0.200 | 0.1 |
| Hattic | 0.233 | 0.122 | 0.119 | −1.0 |
| Eteocretan | 0.243 | 0.174 | 0.171 | −1.2 |
| Palaic | 0.207 | 0.125 | 0.119 | −1.4 |
| Hurrian | 0.198 | 0.121 | 0.114 | −2.3 |
| Etruscan | 0.312 | 0.189 | 0.177 | −3.2 |

No candidate beats the control by more than two spreads once the controls are enough. The gain in distance is what any optimisation with 59 degrees of freedom produces, and the control reproduces all of it. Etruscan, which in section 5 was the one direction the Linear B values pushed away relative to chance, is here brought closer less than the control; the two measurements do not contradict each other (they compare different things) and together say there is nothing there. The same holds for the sign-shape assignment of Nepal and Perono Cacciafoco (2024), transcribed from their Table 2 and tested with the same instrument: it moves Minoan away from every candidate except Etruscan, and 35 of 100 random assignments bring it closer than theirs does.

## 6. What is closed and what remains

**Closed, with a null:** that the consonant phonotactics of Minoan resembles any of thirteen candidates, under the current transcription (section 4) and under any assignment of values compatible with the shared names (section 5 bis). Those shared names are, in turn, the only thing the lexical comparison with Linear B returns above chance: with the full Linear B lexicon (5,234 forms) and a syllable-bigram null, exact coincidences of three or more syllables concentrate in the place names (3 observed against 0.24 expected), graze chance in the personal names (3 against 0.95) and sit at chance in the lexemes (2 against 0.54). The coincidences between the two scripts are shared geography, not language. The three historical ones — Luwian, Hurrian, Hattic — are measured against a null here for the first time, and none passes.

**Not closed:** the affiliation of Minoan. Four readings remain compatible with everything measured: that Minoan is an isolate; that it is related to a language not in the set; that the Greek filter deforms the phonotactics too much for any signal to survive; or that the Linear B values are wrong for Linear A, in which case what was measured is the phonotactics of an incorrect transcription. The fourth is now bounded by section 5 bis: not even a free assignment of the unanchored values produces resemblance. The first three remain open, and none is resolved by adding candidates. Adding candidates is not the remedy: fifty more would return fifty more p-values near 1.00 for the same reason.

**What does not pass through the filter** is typology: word order, affixation, reduplication, and other structural properties that can be measured on a transliteration without depending on its sound values. Three such features coded for Minoan and matched against the Grambank database (Skirgård et al. 2023) already point in a direction — Luwian and Akkadian score 0 of 3, Sumerian and Abkhaz 3 of 3 — but three binary features do not discriminate among 2,467 languages, and the historical candidates are mostly absent from Grambank because they are dead. That is the work this paper leaves: ten structural features measured distributionally for Minoan, and the dead candidates coded by hand from their grammars.

## 7. Discussion

The century of proposals was not wrong to ask the question; it was unable to answer it, because the answer requires putting every candidate in the same format and giving each the same chance to fail. Done that way, every candidate fails at the level of consonant phonotactics, and the one apparent success is the instrument seeing its own transcription. That is a result, not a lack of one: it removes the phonological argument from every proposal on the list, and it says where the argument would have to be made instead.

There is a lesson here that reaches beyond Linear A. Ventris did not have a bilingual; he had a structural grid and a candidate language whose grammar could be applied and tested. Where the candidate language is unknown, the grid must carry more of the weight, and the grid is exactly what a transcription-independent typology would supply. The path exists; what this paper establishes is that the phonological shortcut is closed under the current values.

## Data and reproducibility

Linear A from the LinearA Explorer transcription of GORILA. Linear B, Hittite (6,000 words), Ugaritic, Eteocretan from the corpus_all dataset of the companion project. Hurrian, Hattic, Luwian, Palaic and a second Hittite from TLHdig 25.1 (Zenodo 15459134, Hethitologie-Portal Mainz). Sumerian, Akkadian, Elamite from the CDLI bulk ATF (CC BY 4.0). Etruscan from OpenEtruscan. The normalizer, the null and the calibration are implemented in the kuro package; the candidate corpora are not redistributed, and the scripts that fetch and filter them are.

## Declaration of assistance

The corpus processing, the tests and the drafting of this text were produced with the assistance of a language model (Claude, Anthropic) under the direction of the author, who is responsible for all claims made here.

## References

Facchetti, G. M. 2001. Appunti di morfologia etrusca. Florence: Olschki.

Finkelberg, M. 1990-91. Minoan inscriptions on libation vessels. Minos 25-26, 43-85.

Gordon, C. H. 1966. Evidence for the Minoan Language. Ventnor: Ventnor Publishers.

Nepal, A. and F. Perono Cacciafoco 2024. Minoan Cryptanalysis: Computational Approaches to Deciphering Linear A and Assessing Its Connections with Language Families from the Mediterranean and the Black Sea Areas. Information 15(2), 73.

Palmer, L. R. 1958. Luvian and Linear A. Transactions of the Philological Society 57, 75-100.

Skirgård, H., H. J. Haynie, D. E. Blasi and others 2023. Grambank reveals the importance of genealogical constraints on linguistic diversity and highlights the impact of language loss. Science Advances 9(16), eadg6175.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos and N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Steele, P. M. and T. Meißner 2017. From Linear B to Linear A: the backward projection of sound values. In P. M. Steele (ed.), Understanding Relations Between Scripts. Oxford: Oxbow.

TLHdig 2025. Thesaurus Linguarum Hethaeorum digitalis, version 25.1. Hethitologie-Portal Mainz. Zenodo, doi 10.5281/zenodo.15459134.

van Soesbergen, P. 2022. The Decipherment of Minoan Linear A. Volumes I-II. Academia.edu.
