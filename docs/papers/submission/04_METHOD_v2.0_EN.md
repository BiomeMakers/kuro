# Measuring reading proposals for undeciphered scripts

**Alberto Acedo**
Biome Makers Inc. Version 2.0, 12 September 2026. Not for circulation.

## Summary

Proposals to read undeciphered scripts rarely declare what datum would refute them, against what null they were tested, or how many tests were run before the one that gets published. This paper does three things. First, it sets out eight minimum requirements a proposal should meet to be discussable at all, and for each one shows a case where its absence produced a false positive; eleven of those cases are the author's own, and they are here on purpose, because whoever proposes a protocol should first show where he has failed it. Second, it describes the procedure that implements the requirements: permutation nulls that preserve whatever the claim does not purport to explain, calibration on Etruscan, twelve instruments with a measured error rate, a reading cycle with a novelty gate and batch correction, and two stages with a language model in the loop whose invention rate is measured. Third, it calibrates the whole on four corpora where part of the answer is known — Etruscan, Iberian, Cypro-Minoan, and the archives of Susa and Uruk — reporting in each what it recovers of what is known, what it contradicts, and at what size it stops seeing. The conclusion that bears on Linear A is the contrast: Iberian, with two dozen names from a bilingual, anchors; Minoan, with six consonantal place names, does not. Same instrument, different data.

**Keywords:** decipherment, null models, calibration, error rate, protocol, Linear A, Etruscan, Iberian, Cypro-Minoan, proto-Elamite.

# Part 1. The protocol

## 1.1 The problem

Proposed readings appear faster than the field can evaluate them, and the million-dollar prize for the Indus script (2025), a corpus whose statistical character has itself been disputed [5, 6] has quickened the pace. The problem is not a want of competence: it is that there is no common minimum of what a proposal must declare for someone else to judge it. Without that minimum, disputes are settled by authority or by exhaustion, and a refuted proposal reappears five years later under another name.

This paper proposes eight requirements, all elementary in other empirical sciences, and shows for each a case in which its absence produced a false positive.

## 1.2 The eight requirements

### 1.2.1 A null model for every distributional claim
Any claim of the form "this word occurs with that one", "this affix is productive", "these two document classes differ" needs the permutation that preserves whatever the claim does not purport to explain and destroys only what it does. The wrong null produces positives.

*Own case.* We measured the ascendency/capacity ratio of the document-word network at Haghia Triada and at Susa, and both fell inside Ulanowicz's [2] "window of vitality" — an attractive result. With a null preserving row and column sums, the null reproduces the observed value to three decimals. The index was measuring the marginals. Withdrawn.

*Own case.* We measured the compositionality of the Minoan lexicon and obtained 0.12 against 0.02 for a null of shuffled syllables, above Greek at equal size. With a null preserving syllable transitions, the observed value falls inside the null (p = 0.60): it was the phonotactics of the syllabary. Withdrawn.

The rule is that the null must preserve everything that is not the hypothesis. A second part has proved necessary: it is not enough to declare the null, one must declare **what claim it covers and what it does not**. A null over a set does not cover its members. And a coincidence null, however well built, measures how improbable the observation would be absent an effect; it does not turn a proposal into a certainty nor eliminate apophenia, which no calculation internal to the material can rule out.

### 1.2.2 A positive control on a corpus with a known answer
Before applying an instrument to the unknown, one must check that it recovers the known in a comparable corpus. If it does not, the instrument's silence is not information.

*Own use.* Calibration on Etruscan (recovers the genitive before *clan*, the chronology of syncope, the geography of the sibilants), on Eteocypriot against Cypriot Greek, on proto-Elamite (recovers Dahl's [4] classification of numerical systems, the institutional header, the names/commodities partition) and on Iberian (recovers Untermann's [3] formants and two known isoglosses).

*Own case, this year.* The triconsonantal root signature seemed the obvious typological test of a Semitic classification. Measured with equal sample sizes across nine languages, **Ugaritic — indisputably Semitic — scores lowest of all at 1.03 and Hittite highest at 1.46**, with Akkadian at 1.36. The measure does not separate what it must separate, so it says nothing about Minoan. Declared as a closed avenue with its table, so that no one repeats it blind.

### 1.2.3 A stated error rate for the instrument
An instrument that is not wrong on a known corpus has not been tested. Report where it fails, not only where it works.

### 1.2.4 A count of the tests run
The probability of a spectacular result grows with the number of tests. A proposal that reports one p-value without saying how many tests preceded it is reporting a maximum, not a measurement.

*Own case, this year.* Six pairs of Linear A units differ by a T-series syllable inserted in second position (A-TA-DE ~ A-DE, DA-TA-RE ~ DA-RE and four more), which is what an infixed -t- stem predicts, at p = 0.033 against a shuffled null. But the same test on the other consonant series gives **six pairs for R and six for S**. With twelve series tested, the corrected p is 0.40.

### 1.2.5 Site and support confounders
Archives differ by site, by support and by scribe. A pattern concentrated in one site may be a pattern of that site.

*Own case.* List entries appeared to concentrate by site: 87% in a single site against 32% expected. The list is headed by the two total terms, which occur everywhere, and within Haghia Triada none of the twenty entries concentrates on a scribe (p = 1.00). The effect was the size of the archive, not a property of the class.

### 1.2.6 A refutation condition
Every reading must state what finding would overturn it, in the form of a datum someone could go and look for.

### 1.2.7 Prior art with its measurement
A proposal must locate itself against what exists and say by how much it improves on it, measured on the same data.

### 1.2.8 Separation of function and meaning
What a unit *does* in a document is fixed by distribution; what it *means* is not. Conflating them is the commonest failure in this field, and it is what allows a functional result to be presented as a reading.

## 1.3 A ninth requirement, added this year

**When one script is compared with another, the control must be a script of the same kind, and more than one.**

*The case that forced it.* Word-final m-syllables occur in 7.1% of Linear A units against 3.1% in Mycenaean, p = 1.5·10⁻⁷ — a strong result consistent with Semitic mimation, and the only measurement in this project that ever favoured the Semitic hypothesis. The Cypriot syllabary writing Greek gives **6.2%** over 693 words. Two syllabaries writing languages without mimation give 3.1% and 6.2%: the rate is set by the orthographic convention for final consonants, not by the language. Linear A at 7.1% is indistinguishable from the Cypriot rate. Withdrawn seven hours after being obtained.

## 1.4 Two failure modes that no null catches

**Circularity in the test's construction.** "The unit preceding a logogram never takes a figure" gives 0 of 100 and p = 3·10⁻⁴⁰. It means nothing: if the next token is a logogram then by construction it is not a figure. A p-value of that size should prompt a search for the construction that produced it.

**Artefacts of the edition.** Looking for sealing batches produced 225 consecutive nodules marked \*301, 151 with KU, 149 with KA. Of the 854 single-sign nodules of Haghia Triada, **825 consecutive pairs share a sign where 135 would be expected if mixed**: GORILA orders them by their mark. Any analysis of sequence over that material inherits the ordering. The edition does not flag it.

Both failure modes share a signature: **an effect much larger than the phenomenon could plausibly produce**. Treat that as a reason to look for the artefact, not as a result.

# Part 2. The procedure

## 2.1 Data and instruments

The corpus is the 1,720 documents of Linear A in the SigLA/LinearA Explorer transcription, checked against GORILA I-V [10]. Every unit carries a breakage status, because 276 of 783 syllabic units are broken in all their attestations and treating them as words inflates every count.

Twelve instruments, each with a measured error rate, implement the requirements: permutation nulls preserving marginals, transitions or both; a motif-discovery routine against a Markov null; a name-matching routine against a bigram null; a bench that classifies a claim against 53 functional constraints; and a reading cycle with a novelty gate and Bonferroni correction by batch.

## 2.2 Calibration on Etruscan

The instrument recovers the genitive before *clan*, the chronology of syncope and the geography of the sibilants, and fails at exactly the size where the Etruscan corpus falls below Linear A's — which is what makes its silence on Linear A informative rather than empty.

## 2.3 Method negatives

Reported in full because they bound the instrument: Gromov-Wasserstein alignment (2 of 50 correct with the same language split in halves at 455 words), the triconsonantal signature (§1.2.2), free-value search with control (no candidate below control), and cognate-based alignment with published tools that proved not to reproduce their own reported figures.

## 2.4 A case: how the procedure produced, then corrected, a reading

U-NA-KA-NA-SI was filed as the term naming the offering in the libation formula. Re-examined under requirement 1.2.1, the claim rested on a single hyphenated token in one inscription, SY Za 2, not present in the machine-readable transcription, with five attested variant forms. The hyphen is an editorial convention and was shown to be invertible. The entry now stands as disputed, with its refutation condition: the GORILA IV page for SY Za 2.

# Part 3. What the instrument sees where the answer is known

Four calibrations on corpora where part of the answer is known. Each reports what is recovered, what is contradicted, and the size at which the instrument stops seeing.

## 3.1 Etruscan: function is predictable where meaning is not

Etruscan is read and only partly understood: the vocabulary with established meaning runs to about a thousand entries, and the overwhelming majority of texts are short funerary inscriptions whose content is onomastic. The question posed here is not what the disputed words mean but what class of word they are, which distribution can decide.

**Data.** The Larth corpus (Vico 2023), 7,139 records with city, date and translation where one exists, setting aside 26 Umbrian texts detected by vocabulary; the ETP_POS lexicon with 1,122 entries and part of speech. Orthographic normalisation raises the known words present in the texts from 316 to 349. Features: initial and final position, single-word inscription, neighbours by known class, ten suffixes, frequency, dispersion by city, and adjacency to a known praenomen. Five-fold cross-validation and a shuffled-label null.

**The classifier learns function.** Accuracy 0.70 against 0.26 with shuffled labels; recall by class 0.78 (name), 0.54 (noun), 0.67 (verb), 0.83 (particle). The heaviest features are position in the onomastic formula and the verbal suffixes in -ke/-χe.

**An unintended validation.** The working file omits common words, so terms whose meaning the field does have appear as "unknown". Without knowing it, the classifier is right on eight of ten checkable cases: *teke* (verb, 0.98), *larke* and *fulnike* (verbs, past in -ke), *ein* (particle, 0.75), *θui* (particle), *suθi* and *zilaθ* (nouns), *mlaχ* (noun or adjective). It fails on *mulu* "gave" and *lupu* "died", participles in -u, whose suffix was not among the features. That is the model's own indication of what it lacks.

**The candidates.** Of 154 words unknown to the field with frequency ≥ 3, nine are not names. Three merit examination: *θapikun* (Populonia, Po 4.4), in predicate position after the relative particle *inpa* and with a derivative in the same inscription, *θapintaś*, which satisfies two of the three conditions of the procedure; *fanu* (Cippus Perusinus), between the particle *eθ* "thus" and the subject *lautn* "family", with the classical comparison to Latin *fanum* but no derivative and no bilingual, one condition and a half; and *aknanasa*, which examination withdraws: it is the participle *acnanasa* "having begotten", translated in the corpus itself, and its classification as a noun is a model error of the same kind as *mulu* and *lupu*.

**Limit.** The open corpus is noisy (OCR, Umbrian, name glosses in place of translations) and the reference edition is not available in tabulated form. The editors' own doubts sit in the long texts (*θelu*, *parχ*, *munis*, *θlu*, *θup*, *sela*, *iluku*, *cuieskhu*), each with one to three attestations: insufficient for the procedure, and the natural target when the full edition is available.

## 3.2 Iberian: the corpus that anchors

The Iberian semi-syllabary has been read since Gómez-Moreno and the language is still not understood. What is established is a set of regularities: a repertoire of formants combining in pairs to make anthroponyms (Untermann 1990), recurrent suffixes, a numeral system recognised by comparison with Basque (Orduña 2005; Ferrer i Jané 2009), and graphic differences between the north-eastern, Levantine and southern varieties. These were obtained by inspection and internal comparison, not against null models, so neither their effect size nor their probability under chance is known.

**Data.** 2,094 Iberian texts derived from the Hesperia database (UCM) in the version published by Luo et al. (2021), of which 1,919 have usable text: 2,677 words, 2,359 types. Zones: north-eastern 1,644 texts, Levantine-southern 269. Chronology and support are in Hesperia but not in this copy; their absence prevents separating register and period, and is declared.

**Untermann's formants are the repertoire the null points to.** The thirty formants sought as substrings occur 295 times; the null gives 11.1 on average (maximum 20 over 100 permutations). The most frequent are *taŕ* (62), *biuŕ* (37), *atin* (33), *iltiŕ* (31), *śalir* (26). The result is not trivial: it says the sequences Untermann isolated are not arbitrary with respect to the phonotactics of the corpus.

**Two isoglosses separate under a null, a third is an artefact.** Over 2,090 northern and 574 southern words: final -kí at 28.6‰ in the south against 1.2‰ in the north (p = 3·10⁻⁸), and 30.9‰ against 0 in three-sign endings (p = 3·10⁻⁹); -ḿi at 40.5‰ in the north against 7.6‰ in the south (p = 3·10⁻⁵). Both are the isoglosses Hesperia describes. The third difference detected, final -n (21‰ south against 2.3‰ north), corresponds to a transcription convention for the separator and not to a fact of the language; it is reported so that it is not counted as a result.

**The bilingual anchor, measured.** The Latinised names of the Turma Salluitana (Ascoli bronze, 89 BC) are the only real bilingual of a Palaeohispanic language. For each onomastic element, how many forms of the Hesperia corpus (2,906 intact) contain it, against 1,000 strings of the same length generated by the corpus's own letter-bigram model. In Latin orthography (*adin*, *gibas*, *bilus*, *balci*, *urgi*) it beats the null 1 of 16, because Iberian writing does not distinguish voiced from voiceless and *Adingibas* is written *atin-kibas*. In Iberian orthography, with the correspondence established by the field, **8 of 23 beat the null** (1.2 expected; binomial p = 10⁻⁵) and five survive Bonferroni: *bilos*, *sosin*, *biuŕ*, *balke*, *tautin*. Of Untermann's formant list, 15 of 24. **The onomastic system the bilingual reveals is present in the corpus, with a p-value per element, and it agrees with what Untermann isolated by hand.**

**Four claims of the Iberian field against a null.** The Basque-like numerals should compose with one another as in Basque: forms with two distinct numerals, 7 observed against 0.7 expected with ten random forms of the same lengths (p = 0.014). *Śalir* as "silver" (Orduña): with metrological marks in 7 of 13 inscriptions against a base rate of 28% (p = 0.046). *Ekiar* as a craftsman's signature after a name: 1 of 8 as a separate token and 1 of 13 within the same form; it does not hold with this corpus. The funerary formula *aŕe take*: two inscriptions, no null possible. **One holds, two are borderline, one falls** — the same proportion the procedure yields over Younger's readings in Linear A.

## 3.3 Cypro-Minoan: the nearest neighbour

From the dataset published by Corazza [7], Tamburini [8], Valério and Ferrara (2022), 183 inscriptions are reconstructed with their sign sequence, site and support: 1,386 signs, 155 types. Against a unigram null (same signs, shuffled order), repeated sequences are well above chance: 2-grams 83 against 43.9; 3-grams 19 against 0.9; 4-grams 6 against 0. The corpus has recurrent lexical units, which is the minimum condition for any matching method to have something to work with. The contrast between tablets and other supports has no power (6 tablets, all from Ugarit). This is the calibration closest to Linear A in size, script and period, and the one that most resembles it in what it cannot do.

## 3.4 Susa and Uruk: the same instrument on larger archives

The three archives share what makes them hard and what makes them comparable. None has a bilingual: Linear A is not read; proto-Elamite is not read and its language is unknown; proto-cuneiform is read in part, through the continuity of its logograms and numerals into Sumerian cuneiform. All three are accounting archives of a palace or institution, with the same document type: a tablet recording entries of a quantity of something associated with someone, with a header and sometimes a total. The literature has described that anatomy separately for each, but it has not been measured with one instrument across the three, so it is not known which features belong to early accounting in general and which to each tradition.

The comparison also has a methodological value. The apparatus used here produces in Linear A a series of negative results that were attributed to corpus size: no measurable co-exclusion, no reliability in the network descriptors, no power to separate document types. Applied to sibling corpora five and twenty times larger, it allows one to say for each instrument at what size it begins to see, and so turn those negatives into a power curve.

**Haghia Triada**, around 1450 BC: some 150 tablets and 150 nodules and roundels, preserved because the building burned in the Late Minoan IB destructions, recording the last year of an administration that allocated grain, oil, wine, figs, livestock and aromatics, with twenty-one scribes working at once. There is no temporal stratification: it is a still photograph.

## 3.5 What the four calibrations say about Linear A

**The contrast is the result.** Iberian anchors: two dozen names from a bilingual fix values, and the instrument then recovers Untermann's formants and two known isoglosses, with p-values. Minoan does not: six consonantal place names shared with Linear B fix sixteen signs of 110. Same instrument, different data.

That contrast can now be priced. Specifying a decipherment costs 587 bits (94 free signs × log₂ 74, plus the choice of language); the corpus supplies at most 236; **each sign anchored from outside removes 6.2 bits**, so closing the deficit would take some 57 anchored signs. Iberian has its bilingual. Minoan has sixteen signs.

And Cypro-Minoan gives the size at which the instruments fall silent: at 1,386 signs the recurrent lexical units are still visible, but every contrast between document classes loses power. Linear A sits just above that line on the first count and just below it on the second, which is why its functional inventory grows while its lexical one does not.

# Part 4. Why this matters now

In August 2026 a complete Semitic reading of Linear A appeared as a preprint with a DOI, an auditable catalogue of 67 readings, and its phonological conversion rules declared explicitly. That last point is a merit and is rare: declaring the rules makes the space of solutions measurable, which is precisely what the companion paper does with it.

The result there is instructive for this protocol. Under the declared rules, 89.1% of Linear A units find a Semitic comparandum, Mycenaean Greek finds one 79.7% of the time, and Packard's [1] fictitious grids reach 97.1%. Simulated annealing over the free signs finds grids scoring 183 against 75 for the standard grid, changing 37 of 38 signs. The criterion by which such proposals are judged does not merely fail to discriminate: it prefers assignments that are almost certainly wrong.

None of that refutes the reading. It fixes where the weight of a reading must lie, which is the whole purpose of a protocol.

**Works this protocol leans on.** The fictitious-grid control is Packard [1]; the entropy dispute over the Indus script, which is the clearest recent case of a statistic without a control, is Rao [5] against Sproat [6]; the fraction values are Corazza and colleagues [7]; and the limits of palaeography as a criterion are set out by Salgarella and Judson [9].

## Data and reproducibility
Corpus, code, null models, the manifest of every figure, the closed avenues with their measurements and the withdrawn claims with their reasons, at github.com/BiomeMakers/kuro.

## References

[1] Godart, L. and Olivier, J.-P. 1976-1985. *Recueil des inscriptions en linéaire A* (GORILA), 5 vols. Paris: Geuthner.
[2] Packard, D. W. 1974. *Minoan Linear A*. Berkeley: University of California Press.
[3] Duhoux, Y. 1989. "Le linéaire A: problèmes de déchiffrement." In *Problems in Decipherment*, 59-119.
[4] Ventris, M. and Chadwick, J. 1953. "Evidence for Greek dialect in the Mycenaean archives." *Journal of Hellenic Studies* 73: 84-103.
[5] Luo, J., Hartmann, F., Santus, E., Barzilay, R. and Cao, Y. 2021. "Deciphering undersegmented ancient scripts using phonetic prior." *Transactions of the Association for Computational Linguistics* 9: 69-81.
[6] Salgarella, E. and Castellan, S. 2021. SigLA: The Signs of Linear A, a palaeographical database. sigla.phis.me.

## Acknowledgements

I am a biotechnologist by training and came to the Aegean scripts from outside the field. Several of its specialists answered a stranger's letters, and this work would be poorer or wrong without them.

**Margalit Finkelberg** (Tel Aviv) sent me her 1995 paper with Alexander Uchitel and her 2001 study of the Minoan language, and raised two objections that changed the text: one on the affiliation of Etruscan, which I had treated as settled when it is not, and one that led me to find two faults in my own value search. **Barbara Montecchi** (Bologna) sent me her 2019 monograph on counting at Haghia Triada. **José Miguel Jiménez Delgado** (Seville) corrected the reading of the *-qe* ending and offered further help. **Miguel Valério** (Murcia) agreed to read the work; I later found that a reading I had reconstructed independently was his, published in 2007. **Robert Hogan**, who maintains the Linear A Explorer, answered on the data and has collaborated since.

Letters are outstanding to **Thomas G. Palaima**, **Ilse Schoep**, **Silvia Ferrara**, **Maria Anastasiadou**, **Maurizio Del Freo**, **Miller Prosser** and **Brent Davis**. None of them is responsible for anything asserted here.

The corpus rests on the published editions of **GORILA** (Godart and Olivier), on **SigLA** (Salgarella and Castellan), on the **Linear A Explorer**, and on **NESTOR** (University of Cincinnati), whose bulletins are the bibliographical filter this work applies before claiming anything is new.

## An open invitation

Every measurement in this paper is reproducible. The corpus, the code, the null models and the manifest that holds every figure asserted here are public at **github.com/BiomeMakers/kuro**, and the manifest names, for each claim, the condition that would refute it.

**I would rather be corrected now than in print.** If a measurement here is wrong, if a claim has prior art I have missed, or if a null is badly built, I want to know — and the repository is set up so that anyone can check without taking my word for it. Twelve apparent findings of this project turned out to be already published; each was caught by a three-minute search. There will be a thirteenth, and I would like it found by someone else before it reaches a journal.

Anyone who wants to run these tests on another corpus, or to break them on this one, is welcome to write.

## Statement of artificial intelligence assistance

The measurements and the drafting of this paper were carried out with the assistance of a language model (Claude, Anthropic), under the design, verification and responsibility of the author. Every figure asserted here is recorded in the project manifest with its null model, its number of observations and its p-value, and the code that produces it is public.
