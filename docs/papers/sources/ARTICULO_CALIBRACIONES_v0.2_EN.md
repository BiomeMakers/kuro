# The same instrument on four corpora with partial answers: Etruscan, Iberian, Cypro-Minoan, and the archives of Susa and Uruk

**Alberto Acedo**
Biome Makers Inc. Draft v0.2, 11 September 2026. Merges three earlier notes (Etruscan v0.1, Iberian v0.1, three archives v0.1) and adds the Ascoli-bronze anchoring, the ending profiles and Cypro-Minoan. Not for circulation.

## Abstract

An instrument applied only to an undeciphered script cannot know whether it sees anything. This paper applies one procedure (permutation nulls that preserve what the claim does not explain, measured error rates, a refutation condition per entry) to four corpora where part of the answer is known, and reports for each what it recovers of the known, what it contradicts, and at what size it stops seeing. In Etruscan, a distributional classifier learns the function of the glossed words and assigns it to the unglossed ones, with an involuntary validation on known forms. In Iberian, the null singles out the thirty onomastic formants Untermann isolated by hand (295 occurrences against 11 expected), separates two isoglosses and dismantles a third; and with the only Palaeohispanic bilingual, the Ascoli bronze, it anchors 8 of 23 elements (1.2 expected; five after correction) provided they are written in the orthography of the semi-syllabary, which does not distinguish voiced from voiceless stops (in Latin orthography, 1 of 16). In Cypro-Minoan, 183 sequences recovered from the dataset of Corazza and others (2022) show recurrent lexical units far above the null (3-grams 19 against 0.9) and a contrast between supports without power. In the Proto-Elamite archive of Susa and the proto-cuneiform archive of Uruk, compared with Haghia Triada, the accounting anatomy is the same and every instrument has a minimum size from which it sees. The transversal conclusion is the one that serves Linear A: **what separates a language with an anchor from one without is the data, not the method**, and the instrument says so with a p-value in each case. Iberian anchors on two dozen names; Minoan, on the six consonantal place names of the Egyptian lists, does not.

**Keywords:** calibration, null models, Etruscan, Iberian, Cypro-Minoan, Proto-Elamite, proto-cuneiform, Ascoli bronze, Linear A.

## 1. What calibration is for

A method for undeciphered scripts has a problem no other method has: it cannot be checked on its object. If it says that a unit of Linear A is a qualifier, nobody can tell it that it is not. The only way to know what it sees is to apply it to corpora where part of the answer is known: languages that are read but not understood (Etruscan, Iberian), accounting archives of early scripts whose logic is known by other means (Susa, Uruk), or a sister script of Linear A with more running text (Cypro-Minoan). In each case the instrument must recover what is known without being told, and where it contradicts what is known it must be able to say why.

The four calibrations below were made with the same package (kuro) without changing a line of the method between corpora. Each section reports what it recovers, what it contradicts, and at what size the instrument loses power. Section 6 says what all this means for Linear A.

## 2. Etruscan: function without meaning

### 2.1 State of the question
Etruscan is read completely and understood in part: the vocabulary with established meaning is about a thousand entries (Bonfante and Bonfante 2002; Wallace 2008; ETP), and the great majority of texts are short funerary inscriptions whose content is onomastic. The long texts (Liber Linteus, Tabula Capuana, Tabula Cortonensis, Cippus Perusinus) hold the non-onomastic vocabulary the field discusses, and it is there that editors mark their doubts. The question here is not what those words mean but what kind of word they are, which is decidable by distribution.

### 2.2 Data and method
The Larth corpus (Vico 2023): 7,139 records with city, date and translation where available, from which 26 Umbrian texts (Iguvine Tables), detected by vocabulary, are set aside; the ETP_POS lexicon (Wallace and collaborators) with 1,122 entries and part of speech. Orthographic normalisation (th → θ, ch → χ, ph → φ, ś → σ, c and q → k) raises the known words present in the texts from 316 to 349. Labels: proper name, noun or adjective, verb, particle. Features: initial and final position in the inscription, one-word inscription, neighbours by known class, suffixes (-s, -l, -si, -ke, -χe, -θ, -al, -as, -ia, -u), frequency, dispersion across cities, and adjacency to a known praenomen. Five-fold cross-validation and a shuffled-label null.

### 2.3 Results
**The classifier learns function.** Accuracy 0.70 (0.26 with shuffled labels); recall by class 0.78 (name), 0.54 (noun), 0.67 (verb), 0.83 (particle). The heaviest features are position in the onomastic formula and the verbal suffixes in -ke/-χe.

**Involuntary validation on known words.** The working file omits common words, so that terms whose meaning the field does have appear as "unknown". The classifier, unknowingly, is right on eight of ten checkable ones: teke (verb, 0.98), larke and fulnike (verbs, pasts in -ke), ein (particle, 0.75), θui (particle), suθi and zilaθ (nouns), mlaχ (noun or adjective); it fails on mulu "gave" and lupu "died", participles in -u, whose suffix was not among the features. That is the model's most immediate correction.

**The candidates.** Of 154 words unknown to the field with frequency ≥ 3, nine are not names. Three deserve examination: θapikun (Populonia, Po 4.4), in predicate position after the relative particle inpa and with a derivative in the same inscription, θapintaś, which meets two of the three conditions of the procedure; fanu (Cippus Perusinus), between the particle eθ "thus" and the subject lautn "family", with the classical comparison to Latin fanum "sanctuary" but without derivative and without a bilingual to test it, one condition and a half; and aknanasa, which examination withdraws: it is the participle acnanasa "having begotten" of the Alethnas inscription, translated in the corpus itself, and its classification as a noun is an error of the model for the same reason as mulu and lupu.

**Where the editors' doubts are.** Mining the translations locates the doubts of content in the long texts: θelu and parχ (Alethnas), munis (dedication to Hercle), θlu, θup and sela (Volterra), iluku and cuieskhu (Tabula Capuana). Each has between one and three attestations in the available corpus, too few for the procedure; they are the natural target when the full edition is available.

### 2.4 Discussion and limits
The result is one of method: in a corpus with enough glossed vocabulary, the function of an unglossed word is predictable by distribution with measurable accuracy, and the model itself points to the morphological feature it lacks when it fails. The limit is one of data: the open corpus is noisy (OCR, Umbrian, name glosses instead of translations) and the reference edition is not available in tabular form. With it, the same procedure would be applied to the editors' doubts in the long texts, which is where the non-onomastic vocabulary of Etruscan waits.

## 3. Iberian: formants, isoglosses, and the anchor

### 3.1 State of the question
The Iberian semi-syllabary has been read since Gómez-Moreno, and the language remains ununderstood. What is established is a set of regularities: a repertoire of formants that combine in pairs to form personal names (Untermann 1990), a handful of recurrent suffixes (-en, -ar, -ka, -te), a numeral system recognised by comparison with Basque (Orduña 2005; Ferrer i Jané 2009), and graphic differences between north-eastern, Levantine and southern Iberian that Hesperia records in its isogloss maps. These regularities were obtained by inspection of a large corpus and by internal comparison, not against null models, so neither their effect size nor their probability under chance is known.

### 3.2 Data and method
Corpus: 2,094 Iberian texts derived from the Hesperia database (UCM) in the version published by Luo et al. (2021), each with its Hesperia reference, which carries the province code. Of these, 1,919 have usable text after setting aside fragments and doubtful readings: 2,677 words, 2,359 types. Zones: north-eastern (Catalonia, Aragon, Castellón, southern France), 1,644 texts; Levantine-southern (Valencia, Alicante, Albacete, Murcia, Andalusia), 269. Chronology and support are missing, held by Hesperia and not by this copy; their absence prevents separating register from period, and is declared as such.

Method: as in Acedo (2026c). For the formants, a null of letters shuffled among words preserving lengths; for the endings by zone, Fisher's exact test with Bonferroni correction over the sixty endings tested (threshold p < 8·10⁻⁴).

### 3.3 Results
**Untermann's formants are the repertoire the null singles out.** The thirty formants, searched as substrings, occur 295 times; the null gives 11.1 on average (maximum 20 in 100 permutations). The most frequent are taŕ (62), biuŕ (37), atin (33), iltiŕ (31), śalir (26), bilos and beleś (24 each), unin (15), aŕbi (13), baise (12). The result is not trivial: it says that the sequences Untermann isolated are not arbitrary with respect to the phonotactics of the corpus.

**Two isoglosses separate under a null; a third is an artefact.** With two- and three-sign endings, over 2,090 northern and 574 southern words: -kí (sign S56 in final position) 28.6‰ in the south against 1.2‰ in the north (p = 3·10⁻⁸), and 30.9‰ against 0 in three-sign endings (p = 3·10⁻⁹); -ḿi 40.5‰ in the north against 7.6‰ in the south (p = 3·10⁻⁵). Both are the isoglosses Hesperia describes in its map 2. The third difference detected, the ending -n (21‰ south against 2.3‰ north), corresponds to a transcription convention for the separator and not to a fact of the language; it is reported so that it is not counted as a result.

**What cannot be done yet.** Without chronology, change in time cannot be separated from change in space, which is precisely the confounder the Etruscan calibration knows how to separate when dates exist. Without support, the register of the lead sheets cannot be compared with that of pottery and coins. Both analyses are ready and will be run when the database supplies those fields.

### 3.4 The bilingual anchor, measured: the Ascoli bronze
The Latinised names of the Turma Salluitana (Ascoli bronze, 89 BC) are the only real bilingual of a Palaeohispanic language. The test: for each onomastic element, how many forms of the Hesperia corpus (2,906 intact) contain it, against 1,000 strings of the same length generated by the letter-bigram model of the corpus itself. In Latin orthography (adin, gibas, bilus, balci, urgi), 1 of 16 beats the null: the Iberian script does not distinguish voiced from voiceless stops, and Adingibas is written atin-kibas. In Iberian orthography, with the field's established correspondence, 8 of 23 beat the null (1.2 expected; binomial p 10⁻⁵) and five survive Bonferroni: bilos, sosin, biuŕ, balke, tautin. Of Untermann's formant list, 15 of 24. The onomastic system the bilingual reveals is in the corpus, with a p per element, and it coincides with what Untermann isolated by hand.

### 3.5 The ending profile, with the unit declared
Stems attested bare and with an ending shared by three or more stems, against a null that shuffles endings among forms. By letter, Iberian gives 46 endings against 10 expected (4.5 times), and the most shared are those the field reads: -te, -ka/-ke, -ḿi, -ar, -en. With a semi-syllabic unit (stop + vowel as one unit), 24 against 17 (1.4 times). Linear A by syllable, all units, 14 against 6 (2.3 times); intact units only, 3 against 1 (-JA, -ME, -TI). Two lessons: the ratio depends on the unit, which must be declared; and part of the published Linear A alternations rests on broken units.

### 3.6 Four claims of the Iberian field against a null
The Basque-like numerals (Orduña 2005; Ferrer 2009: ban, bin, irur, laur, borste, śei, sisbi, sorse, abaŕ, oŕkei) should compound as in Basque: forms containing two distinct numerals, 7 observed against 0.7 expected with ten random forms of the same lengths (p = 0.014; oŕkei-irur, oŕkei-abaŕ-ban, oŕkei-ke-laur). Śalir as silver (Orduña): with metrological marks in 7 of 13 inscriptions against a 28% base (p = 0.046). Ekiar as an artisan's signature after a name: 1 of 8 as a separate token and 1 of 13 inside the same form; not supported by this corpus. The funerary formula aŕe take: two inscriptions, no null possible. The proportion (one holds, two borderline, one falls) is the same the procedure returns on Younger's readings of Linear A.

## 4. Cypro-Minoan: recurrent lexical units in 183 sequences
From the dataset published by Corazza, Tamburini, Valério and Ferrara (2022; repository sign2vec_d), 183 inscriptions are recovered with their sign sequence, site and support: 1,386 signs, 155 types. Against a unigram null (same signs, shuffled order), repeated sequences lie far above chance: 2-grams 83 against 43.9; 3-grams 19 against 0.9; 4-grams 6 against 0. The corpus has recurrent lexical units, the minimum condition for any matching method to have something to work with. The contrast between tablets and other supports has no power (6 tablets, all from Ugarit). It is the calibration closest to Linear A in size, script and date, and the one most like it in what it cannot do.

## 5.1 Why compare three archives that cannot be read

The three corpora share the condition that makes them difficult and the one that makes them comparable. None has a bilingual: Linear A is not read; Proto-Elamite is not read and its language is unknown; proto-cuneiform is half read, through the continuity of its logograms and numerals into Sumerian cuneiform (Nissen, Damerow and Englund 1993; Englund 1998). All three are, on the other hand, accounting archives of a palace or institution, with the same document type: the tablet that records entries of a quantity of something associated with someone, with a heading and sometimes a total. The literature of each has described that anatomy separately (Schoep 2002 and Montecchi 2010 for Haghia Triada; Dahl 2005, 2019 and Damerow and Englund 1989 for Susa; Englund 1998 for Uruk), but it has not been measured with the same instrument in all three, and so it is not known which features belong to early bookkeeping in general and which to each tradition.

The comparison also has a methodological value. The apparatus used here (Acedo 2026c) produces on Linear A a series of negative results that were attributed to the size of the corpus: no measurable co-exclusion, no reliability of network descriptors, no power to separate document types. Applied to sister corpora five and twenty times larger, it allows one to say for each instrument at what size it begins to see, and thus to turn those negatives into a power curve.

## 5.1 bis. The three archives

Haghia Triada, c. 1450 BC. A villa of the Mesara plain in Neopalatial Crete; its archive, some 150 tablets and 150 nodules and roundels, survives because the building burned in the Late Minoan IB destructions, and records the last year of an administration that allocated grain, oil, wine, figs, livestock and aromatics, with twenty-one scribes working at the same time (Schoep 2002; Montecchi 2010). There is no temporal stratification: it is a still photograph.

Susa, c. 3100-2900 BC. Capital of the Khuzestan plain, in contact with Uruk and at the same time independent of it; its 1,500 Proto-Elamite tablets are accounts of grain, livestock, personnel and derived products, with numeral systems of its own and a recurrent institutional header, and they are nearly all that survives of that administration; the periphery (Malyan, Tepe Yahya, Sialk, Sofalin) adds some fifty more (Damerow and Englund 1989; Dahl 2005, 2019).

Uruk IV-III, c. 3350-3000 BC. The earliest known written administration, in Lower Mesopotamia; some 5,000 tablets from the city and its surroundings, with the numeral systems from which those of Susa derive, and with a repertoire of logograms whose meaning is partly known from their continuity into Sumerian cuneiform (Nissen, Damerow and Englund 1993; Englund 1998). It is the only one of the three whose content is half understood.

## 5.2 Data and instruments

Linear A: GORILA (Godart and Olivier 1976-1985) in the form of the LinearA Explorer (Hogan 2022), with the hands of GORILA V and Younger's commentaries (2024); verification in SigLA (Salgarella and Castellan 2020). Proto-Elamite and proto-cuneiform: the transliterations and catalogue of CDLI (export of September 2026), with the numeral systems according to Damerow and Englund (1989) and Dahl (2019). In all three, the unit is the entry (a numbered line with a sign-string and a quantity); the sign-string of Linear A is the syllabic sign-group, that of Proto-Elamite and proto-cuneiform the sequence of non-numerical signs of the entry.

Instruments, in the same order in the three corpora: (1) size and singleton rate of the strings; (2) singletons by string length; (3) recurrence within a document with different quantities by length class; (4) headings (first entry) and totals; (5) vocabulary monopolies by document type or by numeral system; (6) co-occurrence and co-exclusion with the curveball null (Strona et al. 2014) on the documents × frequent strings matrix; (7) numeral systems by object class; (8) hands, where they exist. Nulls and thresholds are those described in Acedo (2026c): permutation preserving margins or lengths, p < 0.01 with one thousand permutations for new claims.

## 5.3 Results

### 5.3.1 The anatomy is the same

The three archives write the entry as sign-string plus quantity, open with a heading (SA-RA₂ and the toponyms at Haghia Triada; M157, the institution sign, on 278 tablets at Susa; the institution and office signs at Uruk) and close with a total on part of the tablets (KU-RO at Haghia Triada; the totals of Susa and Uruk marked by position). The proportion of entries with a quantity differs among the three (0.60, 0.75 and 0.80; χ² = 121, p < 10⁻²⁶ on 8,282 and 23,272 entries), but the order of magnitude is the same and the difference is explained by the proportion of headings and broken lines in each corpus; what is comparable is the anatomy, not the rate.

### 5.3.1 bis Comparative table

| instrument | Haghia Triada (224 docs) | Susa (1,594 tablets) | Uruk (6,387 tablets) |
|---|---|---|---|
| entries with a quantity | 0.60 | 0.75 | 0.80 |
| string singletons (1 sign / 3+ signs) | 0.03 / 0.76 | 0.03 / 0.87-0.99 | 0.03 / 0.9 |
| within-document recurrence with different quantity (short / long) | 0.13 / 0.02 | 0.13 / 0.002 | comparable to Susa |
| institutional header | SA-RA₂ (20 docs), toponyms | M157 (278 tablets) | institution and office signs |
| total | KU-RO (37), PO-TO-KU-RO, DA-I | by position | by position |
| vocabulary monopolies | 6 (accounts) + 3 (allocations) | 24 (capacity), 3 (decimal) | pending |
| co-exclusion with curveball null | 0 pairs (no power) | 13 pairs | pending |
| frame of long strings | KA- 17% on roundels; -JA 7 pairs | M288 final (lift 3.8); M124 initial | pending |
| numeral systems by class | its own fractions (Corazza et al. 2021) | 4 systems, own decimal | 5 systems, source of Susa's |
| attributed hands | 21 (73 tablets) | none in the catalogue | none |

### 5.3.2 The partition of the lexicon is the same, and is seen better with more data

In the three corpora short strings are few, frequent and repeated, and long strings are many, unique and not repeated. At Susa the gradation is clean: one-sign strings are singletons in 3% of cases and recur within the tablet with different quantities in 13%; strings of three or more signs are singletons in 87-99% and recur in 0.2%. At Haghia Triada the same partition exists (commodity and transaction terms recur, names are singletons at 76%) but is seen with less definition because the short class is mostly logographic. Uruk behaves like Susa. The partition between what is counted and who delivers or receives it is therefore a feature of early bookkeeping and not of one tradition, and the behavioural criterion (recurrence with different quantities) recovers it without reading in all three.

### 5.3.3 The compartments, and who makes them

At Haghia Triada, the accounts with a total have six monopoly words and the allocations three (p < 0.01 in both cases); at Susa, the capacity system (grain) has 24 monopoly strings, the decimal 3, the sexagesimal none. Co-exclusion, which at Haghia Triada is not measurable (zero pairs with expected ≥ 1 in 224 documents), appears at Susa with 830 tablets: 13 pairs never co-occur when they should (the header M157 with M371, M370, M373, M046, M367; the grain product M297 with M376, M124, M003, M032, M009), which separates grain accounts from those of livestock and personnel. Only Haghia Triada allows the control by hand: with 73 tablets attributed to 21 scribes, shared vocabulary is explained by the hand (effect 0.032, p = 0.002 controlling for type) and not by the document type (0.025, p = 0.21): the Minoan compartments are, at least in part, scribal portfolios. Susa and Uruk have no attributed hands in the catalogue, and their compartmentation cannot be decomposed in this way; it is stated.

### 5.3.4 Long strings have a frame

At Susa, the 1,296 strings of three or more signs with a quantity have an institution or object sign in final position above chance (M288 231 times, lift 3.8, p < 10⁻⁶; also M263, M297, M346) and a class sign in initial position (M124, M305, M157). The "names" carry a frame: classifier in front, variable core, institution or object behind. At Haghia Triada the frame exists with less power: the prefix KA- (17% of roundel groups against 4% of tablet groups) and the suffix -JA (seven root/derivative pairs against 3.1 expected). It is the same phenomenon at two scales of data.

### 5.3.5 The numerals

Susa inherits from Uruk the sexagesimal system (identical chain N45 → N34 → N14 → N01, same carries), adapts the capacity system (same upper segment N01 → N39 → N24, its own fraction segment N30C, N30D, N39C), invents the decimal (N23 and the chain N23 → N14 → N01 do not exist at Uruk; N51 changes value, from 120 bisexagesimal to 1,000 decimal) and does not take the bisexagesimal (Uruk's chain N19 → N04, 231 cases, absent at Susa). It is the description of Damerow and Englund and of Dahl, recovered by structure, with the correction that the bisexagesimal inheritance is not confirmed. Linear A has no partner for comparison on this side: its fractions (Corazza et al. 2021) are a system of its own.

### 5.3.6 The periphery

At Susa the institutional header M157 is exclusive to the centre (278 tablets, 0 at Malyan, Yahya, Sialk or Sofalin); Yahya writes almost only grain accounts and has six signs of its own; Malyan uses the Susa inventory without a foreign sign. In Crete, Haghia Triada against Khania and Zakros shows a difference of repertoire of the same kind (the HT monopolies do not appear outside), with the same limitation of size of the periphery. In both cases the centre/periphery difference is one of administrative genre before one of script.

### 5.3.7 Note on the scope of this paper

The comparison of which administrative functions each archive puts into words (totals, transfer, sealing, date, measure), and its consequences for the question of whether the form of the Minoan receipt is native or borrowed, are treated in a separate paper (Acedo 2026g), which adds to these three archives the Middle Assyrian archival texts, the Amarna letters and the Neo-Assyrian records. The object here is different: which distributional instrument begins to see at which corpus size.

## 5.4 Discussion

What is common. The early bookkeeping of three regions without direct contact (Uruk and Susa had it; Crete with neither) has the same anatomy and the same partition of the lexicon, and in the three cases the part that records persons and places is the open class of long, unique strings, and the part that records what is counted is the closed class of short, repeated signs. That is not linguistics: it is the shape a record of deliveries takes when it is written, and it is seen in the three scripts because the three were born for that.

What is proper to each. Susa invents a decimal system for persons and animals and does not take the bisexagesimal; Crete writes the commodity almost always with a logogram and the party with syllables, and separates receipts (roundels) from lists (tablets) with a prefix; Uruk has the systems of time, rations and area that the other two do not need. Each archive shows its economy in what it decided to count and in how it decided to count it.

One negative worth recording. When the Susa tablets are ordered by the volume of commodity they record, vocabulary diversity does not change (singleton rate 0.40, 0.40, 0.36 and 0.42 by quartiles; p = 0.47): what grows with volume is repetition within the tablet (from 0.08 to 0.49), not lexical dominance. The analogy with the energy gradients of ecological systems, which predicts less diversity at higher input, does not transfer to the archive.

What it teaches about the instrument. Co-exclusion, the frame of names and the clean partition by length appear clearly at Susa and Uruk and not at Haghia Triada, whose size is a fifth and whose lexicon is mostly logographic. The control by hand, on the other hand, is possible only at Haghia Triada, because only there are scribes attributed. Each corpus answers the instruments that its size and its metadata allow, and the comparison fixes for the first time, with a number, the order of magnitude at which each instrument begins to see: co-exclusion, around eight hundred samples with mixed vocabulary; frame of names, around a thousand long strings; control by hand, with twenty hands and seventy documents.

An asymmetry that conditions all of the above. The three corpora do not offer the same metadata: only Haghia Triada has attributed hands, so that the scribal confounder can be measured there alone; only Susa and Uruk share a comparable numeral system, so that inheritance can be tested between them alone; and only Susa and Uruk have the size for co-exclusion. Every comparative claim in this paper holds for the corpora in which the corresponding instrument has data, and no further. What it does not say. Nothing about the languages, which remain three unknowns, nor about kinship between the scripts, which have none save Uruk-Susa. What it says is where each archive stands in the typology of early written administration, and that Linear A, the smallest of the three, is a normal archive of that typology, measured with the yardstick its elder siblings allow one to calibrate.



## 6. What the four calibrations say about Linear A

Read together, they say three things.

**The instrument sees.** In each corpus it recovers what is known without being told: the function of glossed Etruscan words, Untermann's formants, the compound numerals, the lexical units of Cypro-Minoan, the accounting anatomy of Susa and Uruk. Where it contradicts what is known (ekiar without a name before it; an Iberian isogloss that is a collection artefact), it says why and with what number.

**This is what "isolate" looks like.** The phonotactics of Iberian, an isolate with a reliable transcription, comes out at p ≈ 1 against the thirteen Linear A candidates, exactly as Minoan does. The instrument cannot tell "isolate" from "transcription filter", a limitation that must be declared; but it fixes what a language without relatives looks like in this instrument, and Minoan looks like that.

**This is what "anchored" looks like.** Iberian, with two dozen names in a Latin bilingual, anchors eight elements with a p for each. Linear A, with the six Cretan place names of the Egyptian lists, written in consonants only, anchors one of nine, and that one is an artefact of a frequent skeleton. Same instrument, same test, different data. The distance between the two languages is not one of method.

That is what this paper brings to the Linear A problem: not a reading, but the measure of why there is none, on four corpora where the measure can be checked to work.

## Data and reproducibility
Etruscan: OpenEtruscan and Larth/ETP. Iberian: Hesperia database via Luo et al. 2021 (consultation only; not redistributed). Cypro-Minoan: Corazza et al. 2022 (sign2vec_d). Susa and Uruk: CDLI. Code and derived tables in kuro (github.com/BiomeMakers/kuro).

## Declaration of assistance
The corpus processing, the tests and the drafting of this text were produced with the assistance of a language model (Claude, Anthropic) under the direction of the author, who is responsible for all claims made here.

## References

Corazza, M., F. Tamburini, M. Valério and S. Ferrara 2022. Unsupervised deep learning supports reclassification of Bronze Age Cypriot writing system. PLOS ONE 17(7): e0269544.

Ferrer i Jané, J. 2009. El sistema de numerales ibérico: avances en su conocimiento. Palaeohispanica 9, 451-479.

Orduña, E. 2005. Sobre algunos posibles numerales en textos ibéricos. Palaeohispanica 5, 491-506.

Acedo, A. 2026c. Qué puede afirmarse de un corpus de siete mil signos. Borrador.

Acedo, A. 2026c. What can be claimed about a corpus of seven thousand signs: null tests, calibration and confounders in Linear A, with Etruscan as control. Draft.

Acedo, A. 2026d. kuro. Software.

Acedo, A. 2026d. kuro: modelos nulos, calibración y confusores para corpus epigráficos pequeños. Software.

Acedo, A. 2026g. The Minoan receipt is native: the form of bookkeeping in six Bronze Age administrations. Draft.

Agostiniani, L. y F. Nicosia 2000. Tabula Cortonensis. Roma.

Bonfante, G. y L. Bonfante 2002. The Etruscan Language: An Introduction. 2ª ed. Manchester.

Corazza, M., S. Ferrara, B. Montecchi, F. Tamburini and M. Valério 2021. The mathematical values of fraction signs in the Linear A script. Journal of Archaeological Science 125, 105214.

Dahl, J. L. 2005. Complex graphemes in Proto-Elamite. Cuneiform Digital Library Journal 2005:3.

Dahl, J. L. 2019. Tablettes et fragments proto-élamites / Proto-Elamite Tablets and Fragments (MDP 32). Paris.

Damerow, P. and R. K. Englund 1989. The Proto-Elamite Texts from Tepe Yahya. Cambridge, MA.

Englund, R. K. 1998. Texts from the Late Uruk period. In J. Bauer, R. K. Englund and M. Krebernik, Mesopotamien: Späturuk-Zeit und Frühdynastische Zeit (OBO 160/1), Freiburg, 15-233.

Ferrer i Jané, J. 2009. El sistema de numerales ibérico: avances en su conocimiento. Palaeohispanica 9, 451-479.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A, I-V. Paris.

Hogan, R. 2022. Linear A Explorer. https://lineara.xyz

Luo, J., F. Hartmann, E. Santus, R. Barzilay and Y. Cao 2021. Deciphering undersegmented ancient scripts using phonetic prior. Transactions of the ACL 9, 69-81.

Montecchi, B. 2010. A classification proposal of Linear A tablets from Haghia Triada in classes and series. Kadmos 49, 11-38.

Nissen, H. J., P. Damerow and R. K. Englund 1993. Archaic Bookkeeping: Early Writing and Techniques of Economic Administration in the Ancient Near East. Chicago.

Orduña, E. 2005. Sobre algunos posibles numerales en textos ibéricos. Palaeohispanica 5, 491-506.

Rix, H. 1991. Etruskische Texte. Editio minor. Tübingen.

Salgarella, E. and S. Castellan 2020. SigLA. The Signs of Linear A: a palaeographical database. https://sigla.phis.me

Schoep, I. 2002. The Administration of Neopalatial Crete. Salamanca.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos and N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Strona, G., D. Nappo, F. Boccacci, S. Fattorini and J. San-Miguel-Ayanz 2014. A fast and unbiased procedure to randomize ecological binary matrices with fixed row and column totals. Nature Communications 5, 4114.

Untermann, J. 1990. Monumenta Linguarum Hispanicarum III. Die iberischen Inschriften aus Spanien. Wiesbaden.

Velaza, J. 1996. Epigrafía y lengua ibéricas. Madrid.

Vico, G. 2023. Larth: Etruscan NLP corpus. https://github.com/GianlucaVico/Larth-Etruscan-NLP

Wallace, R. E. 2008. Zikh Rasna: A Manual of the Etruscan Language and Inscriptions. Ann Arbor.

Younger, J. G. 2024. Linear A Texts in Phonetic Transcription. https://kansas.academia.edu/JYounger
