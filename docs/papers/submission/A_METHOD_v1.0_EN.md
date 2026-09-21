# Reading undeciphered scripts: what to declare, how to measure it, and how much information a corpus holds

Alberto Acedo
Independent researcher Version 1.0, 16 September 2026.

## Summary

Proposals to read undeciphered scripts are numerous and are not comparable with one another. None states how many tests it ran before the one it publishes, and the field has no shared criterion by which one proposal can be preferred to another. This paper offers four pieces of that criterion, developed on Linear A and calibrated wherever the answer is known.

Part I sets out the instrument: what a proposed reading must declare to be assessable, how each claim is measured against an explicit null, and what the instrument returns on scripts that are already read.

Part II gives a protocol of ten minimum requirements, calibrated on four corpora. No published proposal for Linear A meets the fourth: state how many hypotheses were tested before the one that is published.

Part III turns "we do not know whether this can be read" into a number. The decipherability function calibrates on three deciphered scripts and returns, for Linear A, a deficit of 345 bits — 56 signs to anchor from outside, or some 788 further units of text.

Part IV is the accounting of one day spent trying to produce a better reading with the whole instrument, and of what it produced: nothing. It is published because the field's difficulty is not a shortage of proposals but the absence of records of what did not work.

Keywords: undeciphered scripts, decipherment, Linear A, null models, statistical protocol, information theory.

---


# Part I. Measuring a reading proposal

### Summary

Proposals to read undeciphered scripts rarely declare what datum would refute them, against what null they were tested, or how many tests were run before the one that gets published. This paper does three things. First, it sets out ten minimum requirements a proposal should meet to be discussable at all, and for each one shows a case where its absence produced a false positive; eleven of those cases are the author's own, and they are here on purpose, because whoever proposes a protocol should first show where he has failed it. Second, it describes the procedure that implements the requirements: permutation nulls that preserve whatever the claim does not purport to explain, calibration on Etruscan, twelve instruments with a measured error rate, a reading cycle with a novelty gate and batch correction, and two stages with a language model in the loop whose invention rate is measured. Third, it calibrates the whole on four corpora where part of the answer is known — Etruscan, Iberian, Cypro-Minoan, and the archives of Susa and Uruk — reporting in each what it recovers of what is known, what it contradicts, and at what size it stops seeing. The conclusion that bears on Linear A is the contrast: Iberian, with two dozen names from a bilingual, anchors; Minoan, with six consonantal place names, does not. Same instrument, different data.

Keywords: decipherment, null models, calibration, error rate, protocol, Linear A, Etruscan, Iberian, Cypro-Minoan, proto-Elamite.

## Part 1. The protocol

### 1.1 The problem

Proposed readings appear faster than the field can evaluate them, and the million-dollar prize for the Indus script (2025), a corpus whose statistical character has itself been disputed [5, 6] has quickened the pace. The problem is not a want of competence: it is that there is no common minimum of what a proposal must declare for someone else to judge it. Without that minimum, disputes are settled by authority or by exhaustion, and a refuted proposal reappears five years later under another name.

This paper proposes ten requirements, all elementary in other empirical sciences, and shows for each a case in which its absence produced a false positive.

### 1.2 The ten requirements

### 1.2.1 A null model for every distributional claim
Any claim of the form "this word occurs with that one", "this affix is productive", "these two document classes differ" needs the permutation that preserves whatever the claim does not purport to explain and destroys only what it does. The wrong null produces positives.

*Own case.* We measured the ascendency/capacity ratio of the document-word network at Haghia Triada and at Susa, and both fell inside Ulanowicz's [2] "window of vitality" — an attractive result. With a null preserving row and column sums, the null reproduces the observed value to three decimals. The index was measuring the marginals. Withdrawn.

*Own case.* We measured the compositionality of the Minoan lexicon and obtained 0.12 against 0.02 for a null of shuffled syllables, above Greek at equal size. With a null preserving syllable transitions, the observed value falls inside the null (p = 0.60): it was the phonotactics of the syllabary. Withdrawn.

The rule is that the null must preserve everything that is not the hypothesis. A second part has proved necessary: it is not enough to declare the null, one must declare what claim it covers and what it does not. A null over a set does not cover its members. And a coincidence null, however well built, measures how improbable the observation would be absent an effect; it does not turn a proposal into a certainty nor eliminate apophenia, which no calculation internal to the material can rule out.

### 1.2.2 A positive control on a corpus with a known answer
Before applying an instrument to the unknown, one must check that it recovers the known in a comparable corpus. If it does not, the instrument's silence is not information.

*Own use.* Calibration on Etruscan (recovers the genitive before *clan*, the chronology of syncope, the geography of the sibilants), on Eteocypriot against Cypriot Greek, on proto-Elamite (recovers Dahl's [4] classification of numerical systems, the institutional header, the names/commodities partition) and on Iberian (recovers Untermann's [3] formants and two known isoglosses).

*Own case, this year.* The triconsonantal root signature seemed the obvious typological test of a Semitic classification. Measured with equal sample sizes across nine languages, Ugaritic — indisputably Semitic — scores lowest of all at 1.03 and Hittite highest at 1.46, with Akkadian at 1.36. The measure does not separate what it must separate, so it says nothing about Minoan. Declared as a closed avenue with its table, so that no one repeats it blind.

### 1.2.3 A stated error rate for the instrument
An instrument that is not wrong on a known corpus has not been tested. Report where it fails, not only where it works.

### 1.2.4 A count of the tests run
The probability of a spectacular result grows with the number of tests. A proposal that reports one p-value without saying how many tests preceded it is reporting a maximum, not a measurement.

*Own case, this year.* Six pairs of Linear A units differ by a T-series syllable inserted in second position (A-TA-DE ~ A-DE, DA-TA-RE ~ DA-RE and four more), which is what an infixed -t- stem predicts, at p = 0.033 against a shuffled null. But the same test on the other consonant series gives six pairs for R and six for S. With twelve series tested, the corrected p is 0.40.

### 1.2.5 Site and support confounders
Archives differ by site, by support and by scribe. A pattern concentrated in one site may be a pattern of that site.

*Own case.* List entries appeared to concentrate by site: 87% in a single site against 32% expected. The list is headed by the two total terms, which occur everywhere, and within Haghia Triada none of the twenty entries concentrates on a scribe (p = 1.00). The effect was the size of the archive, not a property of the class.

### 1.2.6 A refutation condition
Every reading must state what finding would overturn it, in the form of a datum someone could go and look for.

### 1.2.7 Prior art with its measurement
A proposal must locate itself against what exists and say by how much it improves on it, measured on the same data.

### 1.2.8 Separation of function and meaning
What a unit *does* in a document is fixed by distribution; what it *means* is not. Conflating them is the commonest failure in this field, and it is what allows a functional result to be presented as a reading.

### 1.3 A ninth requirement, added this year

When one script is compared with another, the control must be a script of the same kind, and more than one.

*The case that forced it.* Word-final m-syllables occur in 7.1% of Linear A units against 3.1% in Mycenaean, p = 1.5·10⁻⁷ — a strong result consistent with Semitic mimation, and the only measurement in this project that ever favoured the Semitic hypothesis. The Cypriot syllabary writing Greek gives 6.2% over 693 words. Two syllabaries writing languages without mimation give 3.1% and 6.2%: the rate is set by the orthographic convention for final consonants, not by the language. Linear A at 7.1% is indistinguishable from the Cypriot rate. Withdrawn seven hours after being obtained.

### 1.4 Two failure modes that no null catches

Circularity in the test's construction. "The unit preceding a logogram never takes a figure" gives 0 of 100 and p = 3·10⁻⁴⁰. It means nothing: if the next token is a logogram then by construction it is not a figure. A p-value of that size should prompt a search for the construction that produced it.

Artefacts of the edition. Looking for sealing batches produced 225 consecutive nodules marked \*301, 151 with KU, 149 with KA. Of the 854 single-sign nodules of Haghia Triada, 825 consecutive pairs share a sign where 135 would be expected if mixed: GORILA orders them by their mark. Any analysis of sequence over that material inherits the ordering. The edition does not flag it.

Both failure modes share a signature: an effect much larger than the phenomenon could plausibly produce. Treat that as a reason to look for the artefact, not as a result.

## Part 2. The procedure

### 2.1 Data and instruments

The corpus is the 1,720 documents of Linear A in the SigLA/LinearA Explorer transcription, checked against GORILA I-V [10]. Every unit carries a breakage status, because 276 of 783 syllabic units are broken in all their attestations and treating them as words inflates every count.

Twelve instruments, each with a measured error rate, implement the requirements: permutation nulls preserving marginals, transitions or both; a motif-discovery routine against a Markov null; a name-matching routine against a bigram null; a bench that classifies a claim against 53 functional constraints; and a reading cycle with a novelty gate and Bonferroni correction by batch.

### 2.2 Calibration on Etruscan

The instrument recovers the genitive before *clan*, the chronology of syncope and the geography of the sibilants, and fails at exactly the size where the Etruscan corpus falls below Linear A's — which is what makes its silence on Linear A informative rather than empty.

### 2.3 Method negatives

Reported in full because they bound the instrument: Gromov-Wasserstein alignment (2 of 50 correct with the same language split in halves at 455 words), the triconsonantal signature (§1.2.2), free-value search with control (no candidate below control), and cognate-based alignment with published tools that proved not to reproduce their own reported figures.

### 2.4 A case: how the procedure produced, then corrected, a reading

U-NA-KA-NA-SI was filed as the term naming the offering in the libation formula. Re-examined under requirement 1.2.1, the claim rested on a single hyphenated token in one inscription, SY Za 2, not present in the machine-readable transcription, with five attested variant forms. The hyphen is an editorial convention and was shown to be invertible. The entry is now disputed, with its refutation condition: the GORILA IV page for SY Za 2.

## Part 3. What the instrument sees where the answer is known

Four calibrations on corpora where part of the answer is known. Each reports what is recovered, what is contradicted, and the size at which the instrument stops seeing.

### 3.1 Etruscan: function is predictable where meaning is not

Etruscan is read and only partly understood: the vocabulary with established meaning runs to about a thousand entries, and the overwhelming majority of texts are short funerary inscriptions whose content is onomastic. The question posed here is not what the disputed words mean but what class of word they are, which distribution can decide.

Data. The Larth corpus (Vico 2023), 7,139 records with city, date and translation where one exists, setting aside 26 Umbrian texts detected by vocabulary; the ETP_POS lexicon with 1,122 entries and part of speech. Orthographic normalisation raises the known words present in the texts from 316 to 349. Features: initial and final position, single-word inscription, neighbours by known class, ten suffixes, frequency, dispersion by city, and adjacency to a known praenomen. Five-fold cross-validation and a shuffled-label null.

The classifier learns function. Accuracy 0.70 against 0.26 with shuffled labels; recall by class 0.78 (name), 0.54 (noun), 0.67 (verb), 0.83 (particle). The heaviest features are position in the onomastic formula and the verbal suffixes in -ke/-χe.

An unintended validation. The working file omits common words, so terms whose meaning the field does have appear as "unknown". Without knowing it, the classifier is right on eight of ten checkable cases: *teke* (verb, 0.98), *larke* and *fulnike* (verbs, past in -ke), *ein* (particle, 0.75), *θui* (particle), *suθi* and *zilaθ* (nouns), *mlaχ* (noun or adjective). It fails on *mulu* "gave" and *lupu* "died", participles in -u, whose suffix was not among the features. That is the model's own indication of what it lacks.

The candidates. Of 154 words unknown to the field with frequency ≥ 3, nine are not names. Three merit examination: *θapikun* (Populonia, Po 4.4), in predicate position after the relative particle *inpa* and with a derivative in the same inscription, *θapintaś*, which satisfies two of the three conditions of the procedure; *fanu* (Cippus Perusinus), between the particle *eθ* "thus" and the subject *lautn* "family", with the classical comparison to Latin *fanum* but no derivative and no bilingual, one condition and a half; and *aknanasa*, which examination withdraws: it is the participle *acnanasa* "having begotten", translated in the corpus itself, and its classification as a noun is a model error of the same kind as *mulu* and *lupu*.

Limit. The open corpus is noisy (OCR, Umbrian, name glosses in place of translations) and the reference edition is not available in tabulated form. The editors' own doubts sit in the long texts (*θelu*, *parχ*, *munis*, *θlu*, *θup*, *sela*, *iluku*, *cuieskhu*), each with one to three attestations: insufficient for the procedure, and the natural target when the full edition is available.

### 3.2 Iberian: the corpus that anchors

The Iberian semi-syllabary has been read since Gómez-Moreno and the language is still not understood. What is established is a set of regularities: a repertoire of formants combining in pairs to make anthroponyms (Untermann 1990), recurrent suffixes, a numeral system recognised by comparison with Basque (Orduña 2005; Ferrer i Jané 2009), and graphic differences between the north-eastern, Levantine and southern varieties. These were obtained by inspection and internal comparison, not against null models, so neither their effect size nor their probability under chance is known.

Data. 2,094 Iberian texts derived from the Hesperia database (UCM) in the version published by Luo et al. (2021), of which 1,919 have usable text: 2,677 words, 2,359 types. Zones: north-eastern 1,644 texts, Levantine-southern 269. Chronology and support are in Hesperia but not in this copy; their absence prevents separating register and period, and is declared.

Untermann's formants are the repertoire the null points to. The thirty formants sought as substrings occur 295 times; the null gives 11.1 on average (maximum 20 over 100 permutations). The most frequent are *taŕ* (62), *biuŕ* (37), *atin* (33), *iltiŕ* (31), *śalir* (26). The result is not trivial: it says the sequences Untermann isolated are not arbitrary with respect to the phonotactics of the corpus.

Two isoglosses separate under a null, a third is an artefact. Over 2,090 northern and 574 southern words: final -kí at 28.6‰ in the south against 1.2‰ in the north (p = 3·10⁻⁸), and 30.9‰ against 0 in three-sign endings (p = 3·10⁻⁹); -ḿi at 40.5‰ in the north against 7.6‰ in the south (p = 3·10⁻⁵). Both are the isoglosses Hesperia describes. The third difference detected, final -n (21‰ south against 2.3‰ north), corresponds to a transcription convention for the separator and not to a fact of the language; it is reported so that it is not counted as a result.

The bilingual anchor, measured. The Latinised names of the Turma Salluitana (Ascoli bronze, 89 BC) are the only real bilingual of a Palaeohispanic language. For each onomastic element, how many forms of the Hesperia corpus (2,906 intact) contain it, against 1,000 strings of the same length generated by the corpus's own letter-bigram model. In Latin orthography (*adin*, *gibas*, *bilus*, *balci*, *urgi*) it beats the null 1 of 16, because Iberian writing does not distinguish voiced from voiceless and *Adingibas* is written *atin-kibas*. In Iberian orthography, with the correspondence established by the field, 8 of 23 beat the null (1.2 expected; binomial p = 10⁻⁵) and five survive Bonferroni: *bilos*, *sosin*, *biuŕ*, *balke*, *tautin*. Of Untermann's formant list, 15 of 24. The onomastic system the bilingual reveals is present in the corpus, with a p-value per element, and it agrees with what Untermann isolated by hand.

Four claims of the Iberian field against a null. The Basque-like numerals should compose with one another as in Basque: forms with two distinct numerals, 7 observed against 0.7 expected with ten random forms of the same lengths (p = 0.014). *Śalir* as "silver" (Orduña): with metrological marks in 7 of 13 inscriptions against a base rate of 28% (p = 0.046). *Ekiar* as a craftsman's signature after a name: 1 of 8 as a separate token and 1 of 13 within the same form; it does not hold with this corpus. The funerary formula *aŕe take*: two inscriptions, no null possible. One holds, two are borderline, one falls — the same proportion the procedure yields over Younger's readings in Linear A.

### 3.3 Cypro-Minoan: the nearest neighbour

From the dataset published by Corazza [7], Tamburini [8], Valério and Ferrara (2022), 183 inscriptions are reconstructed with their sign sequence, site and support: 1,386 signs, 155 types. Against a unigram null (same signs, shuffled order), repeated sequences are well above chance: 2-grams 83 against 43.9; 3-grams 19 against 0.9; 4-grams 6 against 0. The corpus has recurrent lexical units, which is the minimum condition for any matching method to have something to work with. The contrast between tablets and other supports has no power (6 tablets, all from Ugarit). This is the calibration closest to Linear A in size, script and period, and the one that most resembles it in what it cannot do.

### 3.4 Susa and Uruk: the same instrument on larger archives

The three archives share what makes them hard and what makes them comparable. None has a bilingual: Linear A is not read; proto-Elamite is not read and its language is unknown; proto-cuneiform is read in part, through the continuity of its logograms and numerals into Sumerian cuneiform. All three are accounting archives of a palace or institution, with the same document type: a tablet recording entries of a quantity of something associated with someone, with a header and sometimes a total. The literature has described that anatomy separately for each, but it has not been measured with one instrument across the three, so it is not known which features belong to early accounting in general and which to each tradition.

The comparison also has a methodological value. The apparatus used here produces in Linear A a series of negative results that were attributed to corpus size: no measurable co-exclusion, no reliability in the network descriptors, no power to separate document types. Applied to sibling corpora five and twenty times larger, it allows one to say for each instrument at what size it begins to see, and so turn those negatives into a power curve.

Haghia Triada, around 1450 BC: some 150 tablets and 150 nodules and roundels, preserved because the building burned in the Late Minoan IB destructions, recording the last year of an administration that allocated grain, oil, wine, figs, livestock and aromatics, with twenty-one scribes working at once. There is no temporal stratification: it is a still photograph.

### 3.5 What the four calibrations say about Linear A

The contrast is the result. Iberian anchors: two dozen names from a bilingual fix values, and the instrument then recovers Untermann's formants and two known isoglosses, with p-values. Minoan does not: six consonantal place names shared with Linear B fix sixteen signs of 110. Same instrument, different data.

That contrast can now be priced. Specifying a decipherment costs 587 bits (94 free signs × log₂ 74, plus the choice of language); the corpus supplies at most 236; each sign anchored from outside removes 6.2 bits, so closing the deficit would take some 57 anchored signs. Iberian has its bilingual. Minoan has sixteen signs.

And Cypro-Minoan gives the size at which the instruments fall silent: at 1,386 signs the recurrent lexical units are still visible, but every contrast between document classes loses power. Linear A sits just above that line on the first count and just below it on the second, which is why its functional inventory grows while its lexical one does not.

## Part 4. Why this matters now

In August 2026 a complete Semitic reading of Linear A appeared as a preprint with a DOI, an auditable catalogue of 67 readings, and its phonological conversion rules declared explicitly. That last point is a merit and is rare: declaring the rules makes the space of solutions measurable, which is precisely what the companion paper does with it.

The result there is instructive for this protocol. Under the declared rules, 89.1% of Linear A units find a Semitic comparandum, Mycenaean Greek finds one 79.7% of the time, and Packard's [1] fictitious grids reach 97.1%. Simulated annealing over the free signs finds grids scoring 183 against 75 for the standard grid, changing 37 of 38 signs. The criterion by which such proposals are judged does not merely fail to discriminate: it prefers assignments that are almost certainly wrong.

None of that refutes the reading. It fixes where the weight of a reading must lie, which is the whole purpose of a protocol.

Works this protocol leans on. The fictitious-grid control is Packard [1]; the entropy dispute over the Indus script, which is the clearest recent case of a statistic without a control, is Rao [5] against Sproat [6]; the fraction values are Corazza and colleagues [7]; and the limits of palaeography as a criterion are set out by Salgarella and Judson [9].

### Data and reproducibility
Corpus, code, null models, the manifest of every figure, the closed avenues with their measurements and the withdrawn claims with their reasons, at github.com/BiomeMakers/kuro.

# Part II. A minimum protocol

### Abstract

Proposals for reading undeciphered scripts appear faster than the field can evaluate them, and the reason is not a shortage of expertise but the absence of a shared minimum of what a proposal must state to be assessable at all. Drawing on the experience of applying a single procedure to five corpora with known or partly known answers (Etruscan, Eteocypriot, Proto-Elamite, proto-cuneiform and Iberian) and to one that has none (Linear A), and on our own withdrawn results, this paper proposes ten requirements: a null model for every distributional claim; a positive control in a corpus with a known answer; a prediction about unseen text; a declaration of how many tests were run, with correction for multiple comparisons; verification of the data in the primary edition; publication of negatives with their figures; an account of the ending of any sign-group identified with a word of another language, or an explicit statement that it is unaccounted for; and, before any absence is interpreted, a check that the instrument could have seen what is said to be missing. None of the ten requires computational methods, and none demands that a proposal be correct: they demand that it be evaluable. For each requirement a case is given in which its absence produced a false positive, and twelve of those cases are the author's own, all withdrawn with their figures. Two further failure modes are described that no null model catches, because they are properties of how a test is built or of how an edition is ordered rather than of the data.

Keywords: undeciphered scripts, method, null models, reproducibility, Linear A, Indus script.

### 1. The problem

Reading proposals appear faster than the field can evaluate them, and the million-dollar prize for the Indus script (2025) has accelerated the pace. The problem is not a lack of competence: it is that there is no common minimum of what a proposal must declare for another to judge it. Without that minimum, discussion is settled by authority or by exhaustion, and a proposal that is wrong for a demonstrable reason survives beside one that is wrong for reasons nobody can articulate.

This paper proposes no method and evaluates no one else's proposal. It proposes ten requirements, all elementary in other empirical sciences, and for each shows a case in which its absence produced a false positive. Twelve of the cases are the author's own, and they are there deliberately: whoever proposes a protocol should first show where he has failed it.

### 2. The ten requirements

### 2.1 A null model for every distributional claim
Every claim of the type "this word occurs with that one", "this affix is productive", "these two document classes differ" needs a permutation that preserves what the claim does not purport to explain and destroys only what it does. Any null will not do: the wrong null produces positives.

Own case: we measured the ascendency-to-capacity ratio of the document-word network at Haghia Triada and at Susa, and both fell within Ulanowicz's "window of vitality", an attractive result. With a null preserving row and column sums, the null reproduces the observed value to three decimal places. The index was measuring the marginal distributions. Withdrawn.

Own case 2: we measured the compositionality of the Minoan lexicon (whether long words decompose into recurrent elements) and obtained 0.12 against 0.02 for the shuffled-syllable null, above Greek at equal size. With a null preserving syllable transitions, the observed value falls within the null (p = 0.60): it was the phonotactics of the syllabary. Withdrawn.

Rule: the null must preserve everything that is not the hypothesis. A second part must be added to this requirement, which applying the protocol to someone else's proposal showed to be necessary. Declaring the null is not enough: one must declare which claim it covers and which it does not. A null over a set does not cover its members, and this is a common case: in the companion paper on toponyms, fifteen cases jointly exceed the null and none stands on its own, which is stated there expressly. And a null on coincidence, however well built, measures how improbable the observed would be were there no effect; it does not turn a proposal into a certainty, nor does it eliminate apophenia, the bias of seeing structure where there is none, which no calculation internal to the material can rule out. The gap between what a null measures and what is concluded from it is as real a failure as not running one.

### 2.2 A positive control in a corpus with a known answer
Before applying an instrument to the unknown, one must check that it recovers the known in a comparable corpus. If it does not, the instrument's silence is not information.

Our use: we calibrated on Etruscan (it recovers the genitive before *clan*, the chronology of syncope and the geography of the sibilants), on Eteocypriot against Cypriot Greek (it separates the two languages by their endings), on Proto-Elamite (it recovers Dahl's classification of the numerical systems, the institutional heading and the name/commodity partition) and on Iberian (it recovers the formulaic elements).

Counterexample from the field: most reading proposals for Linear A and for the Indus script report no positive control, so it is not known whether their method would see the answer if it were in front of them.

### 2.3 A prediction about unseen text
A reading that only explains the texts already known cannot be evaluated. The proposal must say what it expects to find in the next inscription and what would refute it.

Our use: the reading of the KU-PA family predicts that its members will go on appearing with the cyperus logogram and with dry commodities, that a new roundel with KA-KU-PA will carry that logogram or a ligature of it, and that the family will not appear as the recipient of liquids. The protocol for what will be done with the Knossos sceptre when it is published is pre-registered before the text is known.

Note: the prediction does not require that the text appear; it requires that it be written down beforehand.

### 2.4 How many tests were run, with correction for multiple comparisons
A procedure that tests forty hypotheses finds two below 0.05 by chance. The proposal must declare the denominator and correct within each family of tests.

Own case: of eleven suffixes tested in Linear A, three exceed the threshold uncorrected and none survives Bonferroni; we report it as such, and the result we sustain is not "these three suffixes are productive" but "there is a positional signal of morphology that none of the suffixes individually demonstrates".

Counterexample from the field: screens for lexical coincidence between an unread script and an extensive dictionary, which are in effect thousands of simultaneous tests, almost never declare that number.

### 2.5 Verify the datum in the primary edition
Derived transliterations, including excellent ones, introduce errors that propagate.

Own case: one of our supports for reading KU-PA as a commodity was a ligature, \*304+PA-KU-PA, on a Haghia Triada nodule. The palaeographic database reads three consecutive signs there: the ligature does not exist. It sustained an argument for two days.

Own case 2: the same source transcribes some fraction signs as whole numbers, which made the arithmetic of several tablets fail.

Rule: every datum sustaining a claim is checked in the edition or in the palaeographic database, and the version used is declared.

### 2.6 Publish negatives with their figures
A negative without a number is not information: "we found no co-exclusion" may mean that there is none or that the corpus is small. With a number, the negative is a measure of power and saves the next investigator the work.

Our use: there is no measurable co-exclusion between Linear A words (zero pairs with expectation above one in 224 documents), and there is in Proto-Elamite with 830 tablets (13 pairs); a network descriptor has no test-retest reliability at these sizes; comparison by sound does not discriminate between candidate languages (all between 1.3 and 1.7 over their own null) either in Linear A or in Linear B, where the same rule produces 383 false positives.

### 2.7 Account for the ending, or state that it is unaccounted for
When a proposal identifies a sign-group with a known word of another language, the comparison usually rests on the stem and leaves the ending untreated. That is where most false positives enter, because a stem of two or three syllables coincides easily and an unexplained ending may be concealing morphology, a particle, or a misplaced word boundary.

The requirement is cheap: state what the ending is proposed to be, or state expressly that it is unaccounted for. It does not demand being right; it demands not being silent.

An own case illustrates it, which is why it is included here. In the companion paper on names formed on plant words we proposed KU-MI-NA-QE as formed on the word for cumin (Mycenaean ku-mi-no, Greek κύμινον, a Semitic loan), on the basis of the shared stem and of its distribution on a sealed roundel, where the sign-group is the party and the logogram the commodity. The vowel -a against Mycenaean -o is no objection, since it follows the correspondence rule measured over 46 pairs (the Minoan final vowel becomes -o in Greek and -a is never preserved). But the ending -QE was left untreated, and a consultation with J. M. Jiménez Delgado (University of Seville) identified it as the problem with the case.

Checked in the corpus, the objection holds. There are seven sign-groups ending in -qe among 782 types (0.9%), and only two have their stem attested separately; against the shuffled-syllable null preserving lengths, those two pairs give p = 0.086, so -qe does not hold as a productive suffix, unlike -ja, which does with seven pairs. And KA-PA-QE is telling: its stem KA-PA is a Cretan toponym (Uchitel 2002-2003) heading six Haghia Triada tablets, so that KA-PA-QE reads naturally as "and KA-PA". In Mycenaean, -qe is the copulative enclitic. If Minoan had a comparable enclitic, KU-MI-NA-QE would be the word ku-mi-na with a particle attached rather than a name, and its two contexts admit that reading.

The case is not refuted; it is left open: it satisfies two of the three conditions, with the third in dispute. Writing it that way is what this requirement asks, and it is what the original proposal did not do.

### 2.8 Before interpreting an absence, check that the instrument could have seen it
A zero is the most tempting observation in a small corpus and the easiest to misread. When something does not appear, there are two possible explanations and only one is interesting: that it is absent because the object did not have it, or that it is absent because the instrument could not see it. The requirement consists in ruling out the second before asserting the first.

Two own examples illustrate it, both detected on applying this requirement retroactively.

First. We claimed that no Linear A sign-group ends in -so, and contrasted this with the fact that Cretan toponyms end in -so in Greek (Knossos, Tylissos, Amnisos). Measuring the full distribution of syllables, it turns out that the syllable so never occurs in the corpus, in any position, and with it seven others of the -o column (do, jo, mo, no, qo, wo, zo). The word-final absence was not a phonotactic feature of Minoan: it was a gap in the transliterated syllabary. The claim was withdrawn and replaced by the comparison of each syllable with its own general frequency, which does measure a positional preference and does not depend on which signs have an assigned value.

Second. Applying by semantic field the functional criterion of a companion paper, names formed on animal words gave zero matches against nine for the plant field. The immediate reading was that Minoan onomastics did not form names on animals, which would be a cultural feature with content. But the search is necessarily made with Mycenaean stems, and in Crete livestock is always written with a logogram and never with syllables: the Minoan words for animals with which to search do not exist. The zero measured the absence of available vocabulary, not the absence of the pattern.

The check is cheap in both cases and consists of the same question: what would have to be in the corpus for the instrument to detect what I say is missing? If that prior condition is not met, the absence is not a datum about the language.

The requirement is therefore stated thus: every claim of the form "X does not occur" must be accompanied by the check that X could have occurred, that is, that the sign, word or category was available to the instrument in the material and the transliteration used. Where that check cannot be made, the absence is reported as a property of the available corpus and not of the language.


### 2.9 When one script is compared with another, the control must be a script of the same kind, and more than one

A rate measured on a script is a property of the script's orthographic conventions as much as of the language behind it. A single comparison witness cannot separate the two.

*The case that forced this requirement, obtained and withdrawn within seven hours.* Word-final m-syllables occur in 7.1% of Linear A units against 3.1% in Mycenaean Greek, p = 1.5·10⁻⁷. Mimation is a diagnostic feature of Semitic, and this was the only measurement in a long project that favoured a Semitic classification of Minoan. The Cypriot syllabary writing Greek gives 6.2% over 693 words. Two syllabaries writing languages without mimation give 3.1% and 6.2%, because Linear B usually omits a final consonant while the Cypriot syllabary writes it with a dead vowel. Linear A at 7.1% is indistinguishable from the Cypriot rate. The effect was real; the inference was not.

### 2.10 Declare the scope of a reading: which archive, which support, which site

A function fixed on one archive is a reading of that archive until it is shown to transfer.

*Our case.* An inventory of functions was built on Haghia Triada, which is 64% of the Linear A corpus, and read as a description of "the Minoan receipt". Measured against its own base rates, the second largest series is a different thing: Khania never sums (0 of 105 tablets carry a summation term against 41 of 205 at Haghia Triada, p = 7·10⁻¹¹), records in fractions, and has no headers or qualifiers of its own. The general claim had to be rewritten as a claim about one archive.

### 2 bis. Two failure modes that no null model catches

The ten requirements above concern what a proposal must declare. These two concern how a test can be wrong while satisfying all ten, and both were encountered in a single day.

Circularity in the construction of the test. "The unit preceding a logogram never takes a figure" gives 0 of 100 and p = 3·10⁻⁴⁰. It means nothing: if the next token is a logogram then by construction it is not a figure. The null model is correct, the arithmetic is correct, and the result is empty.

Artefacts of the edition's ordering. A search for sealing batches produced 225 consecutive nodules marked \*301, 151 with KU, 149 with KA — apparently the trace of large sealing operations. Of the 854 single-sign nodules of Haghia Triada, 825 consecutive pairs share a sign where 135 would be expected if they were mixed: the standard edition orders them by their mark. Any analysis of sequence, neighbourhood or batch over that material inherits the ordering, and the edition does not flag it.

Both share a signature worth stating as a rule: an effect much larger than the phenomenon could plausibly produce is a reason to look for the artefact, not a result. A p-value of 10⁻⁴⁰ in a corpus of a few hundred documents should prompt a search for the construction that produced it.

### 2 ter. What the requirements cost, measured on ourselves

A protocol that nobody applies to themselves is an exhortation. Over one project on Linear A, applying the ten requirements produced fifteen closed avenues and twelve withdrawn claims, each filed with its measurement and its reason. Three examples of what the requirements removed:

- A network index placing two Bronze Age archives inside Ulanowicz's "window of vitality": the null preserving row and column sums reproduced the observed value to three decimals. It was measuring the marginals.
- A compositionality figure for the Minoan lexicon of 0.12 against 0.02 for shuffled syllables, above Greek at equal size: with a null preserving syllable transitions, the observed value falls inside the null (p = 0.60). It was the phonotactics of the syllabary.
- The mimation result of §2.9, which survived seven hours.

None of the twelve was caught by a referee. All were caught by the requirement that the author himself had written down.

### 3. What the protocol does not require

It does not require computational methods: a proposal made by hand can satisfy all ten requirements, and many computational proposals satisfy none. It does not require giving up intuition, which is the origin of almost every good reading; it requires separating the moment of intuition from the moment of checking. And it does not require that a proposal be correct in order to be publishable: it requires that it be evaluable.

### 3 bis. The protocol applied to two proposals by others, and calibrated on a language with an anchor

The protocol has been applied to two readings of Linear A that are not ours, without naming their authors, because what matters is the pattern and not the signature.

The first is a decipherment text with seven claims. One partly meets the requirements; two are measurable and fall when measured: the power law offered as proof of "natural language" is obeyed better by the shuffled corpus (R² 0.95) than by the real one (0.81), and the word breaks presented as successes are right 88.5% of the time against a base rate of 86.5%. The other four state no null and can have none.

The second is a public repository generated with a language model that declares Linear A "solved in five minutes" with 92% confidence. Against the corpus: it gives 1,450 inscriptions with Knossos 450 and Haghia Triada 300 (the corpus has 1,720, Knossos 59, Haghia Triada 1,108); it reads "YA-NE" as wine with confidence 0.90, and the unit does not exist; it proposes "formulas" (oil + 10 + recipient) that occur four times in 89; and it assigns to bare syllables meanings such as "divine invocation". The only correct items (KU-RO total, PA-I-TO Phaistos, VIN wine) were already published. It is the extreme case of a proposal that states nothing verifiable, and it shows why two of the ten requirements, verifying the datum in the edition and counting the tests, must precede any null: a null on a unit that does not exist is a calculation without an object.

The same procedure, applied to a language that does have an anchor, is the calibration. Iberian is read and not understood, and has a partial bilingual, the Latinised names of the Turma Salluitana on the Ascoli bronze. Their elements, written in Iberian orthography (which does not distinguish voiced from voiceless stops: Adingibas is atin-kibas), occur in the Hesperia corpus above a null of strings of equal length in 8 of 23 cases (1.2 expected), five after correction; Untermann's thirty onomastic formants, in 15 of 24 tested. In Latin orthography, without the correspondence, 1 of 16. The same instrument applied to the only near-bilingual source for Minoan, the six Cretan place names of the Egyptian lists, anchors nothing (1 of 9, and that one an artefact of a frequent skeleton). The difference between the two languages is one of data, not of method: two dozen names against six, and the instrument says so with a p in each case. That is what the protocol asks of any proposal: to state how much anchor it has, measured, before saying what it reads.

### 3 bis bis. The precedent this protocol is meant to avoid

The need for these requirements is not hypothetical. Rao and colleagues (2009) argued in *Science* that the Indus Valley script encodes a natural language, because its conditional entropy resembles that of languages more closely than that of several non-linguistic systems; Lee, Jonathan and Ziman (2010) published an argument of the same kind for the Pictish symbols. Sproat (2010) refuted both with a larger set of non-linguistic and comparative corpora, showing that none of those measures reliably tells writing from non-writing, and proposed a repetition-based measure that classified the same symbols the other way.

What failed there was not the statistics but the control: the comparison was made against the non-linguistic systems the authors chose, and not against the set that could have brought the claim down. That is requirement 2 of this list, and the case shows its cost: a claim published in the most widely read journal in the world, disputed for years, which a better chosen control would have bounded from the start.

### 4. Why now, and one case in the open

Three reasons. The volume of proposals has grown with the availability of tools and of prizes. The corpora are digitised, so the ten requirements are now cheap: a null is ten lines of code. And the field has produced, in recent years, examples of how it is done well: the testing against nulls of the tripartite division of Cypro-Minoan, the validation of Ithaca with an experiment among historians, and explicit warnings about the discriminating power of coincidences in small corpora. This paper only orders what those works already practise.

In August 2026 a complete Semitic reading of Linear A appeared as a preprint with a DOI, an auditable catalogue of 67 readings, and — unusually, and to its credit — its phonological conversion rules declared explicitly. Declaring the rules is what makes a proposal testable, and the test is instructive for this protocol. Under those rules, 89.1% of Linear A units find a Semitic comparandum, Mycenaean Greek finds one 79.7% of the time, and Packard's fictitious grids (1974) reach 97.1%. Simulated annealing over the free signs finds grids scoring 183 against 75 for the standard grid, changing 37 of 38 signs.

That is requirement 2.2 in action: without a positive control, a criterion that prefers false assignments looks like evidence. The proposal is not refuted by this, and nothing here bears on the comparative Semitic morphology it also rests on. What the measurement fixes is where the weight of the argument must lie, which is the whole purpose of a protocol.


### 5. Where these requirements come from, and who else has met them

None of the ten is original. Each is standard practice in a field that has had to formalise it, and several have been met in Aegean studies already.

Positive controls and calibration. Corazza, Tamburini, Valério and Ferrara (2022) reclassified the Cypro-Minoan writing system with unsupervised deep learning and validated the method on scripts with known answers before applying it to the unknown one. Assael and colleagues (2022) built their restoration model for Greek epigraphy the same way. Tamburini (2025) surveys the computational approaches and is explicit about which reproduce and which do not.

Verification in the primary edition. Godart and Olivier (1976-1985) is the reference against which every transliteration in this work was checked, and Montecchi (2009) is the study that established how fractions and calculation errors behave in the Linear A documentation. Where the machine-readable transcriptions in circulation disagree with GORILA, this work follows GORILA and says so.

Declaring what a null covers. Duhoux (1978) analysed Linear A linguistically without claiming more than the distribution supported, and his later insistence that resemblance between isolated words proves nothing is the clearest statement in the field of requirement 1.2.8.

Scope and genre. Salgarella and Judson set out the limits of palaeography as a criterion; Davis (2025) surveys what linguistics-based work has and has not established. Steele's work on the Aegean scripts is the standing example of treating writing system and language as separable questions.

And the requirement no one has met. Not one of the decipherment proposals surveyed in the companion paper reports how many tests were run before the one that was published. That is requirement 1.2.4, it is elementary, and its absence is why a century of proposals cannot be compared with one another.

### Declaration of assistance

The analysis of the cases and the draft of this text were produced with the assistance of a language model (Claude, Anthropic) under the author's direction, who is responsible for all claims.

# Part III. How much information a script carries about its own decipherment

### Summary

Whether an undeciphered script can be read is argued qualitatively. It need not be. A decipherment is an assignment of phonetic values to signs; the cost of specifying one follows from the size of the sign inventory; and what the corpus can supply toward that cost follows from how often a candidate reading succeeds by chance. The difference is a deficit in bits, and it is a property of the corpus rather than of the method or of the investigator. This paper states the count, calibrates it on three scripts whose answer is known, applies it to three that are open, and prices what each of the open ones would need. Linear B before 1952, Iberian and Etruscan come out decipherable; Linear A shows a deficit of 345 bits, which converts into two currencies a field can act on: either 56 further signs anchored from outside, or some 788 further intact units of text. For the other undeciphered scripts three of the four inputs are published and the fourth, the match rate, has never been measured for any of them; the paper sets out what measuring it would require rather than supplying it from judgement. The estimate is deliberately generous to the corpus, so a script that shows a deficit under these assumptions shows one under any.

Keywords: undeciphered scripts, decipherment, information theory, Linear A, Cypro-Minoan, proto-Elamite.

### 1. The question nobody puts as a number

The million-dollar prize offered for the Indus script in 2025 has a premise: that the corpus contains the answer and what is missing is ingenuity. For some scripts that premise is true and for others it is not, and the distinction is not a matter of opinion. It can be computed from four quantities that any corpus can report about itself.

The field does argue the point, but in words. Whether Linear A is readable, whether the Indus texts are language at all [9], whether proto-Elamite will ever yield: the arguments turn on the size of the corpus and the absence of a bilingual, and they are correct as far as they go. What they do not do is say how much is missing, which is what a field needs in order to know whether to keep computing or to start digging.

### 2. The count

A decipherment assigns a value to each sign that is not already fixed. Its cost in bits is

> cost = free signs × log₂(possible values) + log₂(candidate languages)

What the corpus supplies is the improbability of its units coming out as words. If a unit matches something in a candidate lexicon a fraction *m* of the time by chance, each successful match carries −log₂(*m*) bits, so

> supply = independent units × −log₂(match rate)

and

> deficit = cost − supply.

Each sign fixed from outside — by a bilingual, by a shared place name, by a loanword whose source is known — removes log₂(possible values) bits, which prices the deficit in a currency a field can act on.

Three assumptions, all generous to the corpus. Every unit is counted as independent evidence, when in fact units share signs and their constraints are redundant. A match is counted as success when a real decipherment also requires the match to be contextually and morphologically right. And the candidate language is counted as one choice among a handful, when in practice it is an open set. A corpus that shows a deficit under these assumptions shows one under any.

### 3. Calibration: three scripts with a known answer

| Script | Signs | Free | Cost | Supply | Deficit | Verdict |
|---|---|---|---|---|---|---|
| **Linear B (as of 1952) [1]** | 87 | 75 | 485 | 9,966 | **−9,481** | Decipherable |
| **Iberian** | 28 | 5 | 26 | 5,048 | **−5,021** | Decipherable |
| **Etruscan** | 26 | 0 | 3 | 6,110 | **−6,107** | Decipherable |

All three are read, and all three come out decipherable with room to spare. The reasons differ and the count shows which is which. Linear B had a large corpus — three thousand units — and a strict match rate, since Greek either fits a sign group or does not; the twelve signs Ventris had from Cretan place names were enough because the supply was enormous. Iberian has few signs and almost all of them anchored by the Ascoli bronze [2]. Etruscan has an alphabet borrowed from Greek, so the values were never in question and the cost is near zero, which is precisely why Etruscan is read and not understood: the count measures the cost of the values, not of the meanings.

### 4. Three scripts that are open

| Script | Signs | Free | Cost | Supply | Deficit | Anchors needed |
|---|---|---|---|---|---|---|
| **Linear A** | 110 | 94 | 587 | 242 | **345** | 56 |

Only Linear A is reported, and the reason matters. Its four quantities are measured: 110 signs and 94 free from the sign list, 552 intact units from the corpus, and a match rate of 0.738 measured directly against the candidate lexicons. For every other undeciphered script, three of the four are published — the sign inventory, the corpus size and the count of externally anchored signs — but the match rate has never been measured for any of them, because no one has run the test. Supplying it from judgement would make the table a report on the author's estimates rather than on the corpora, and the estimates move the verdict.

Linear A is the near case: 56 anchored signs would close it, against the 16 it has. Its supply is small because its corpus is small and because a CV syllabary matches a candidate lexicon 74% of the time by chance, which is nearly free.

Cypro-Minoan [4] is worse than Linear A despite being the nearest relative in script and period: 183 usable units supply 59 bits against a cost of 504. Any project proposing to read Cypro-Minoan by internal method is working with an eighth of the information Linear A has.

proto-Elamite [5] is not close to anything. With 1,900 signs, the cost of specifying an assignment is twenty thousand bits, and no corpus of the size that survives could supply it. The count says plainly what the field has concluded by experience.

### 5. What the deficit buys, stated in two currencies

The same figure converts into either of the two things that could be found.

| Script | Signs to anchor from outside | Or further intact units of text |
|---|---|---|
| Linear A | 56 | 788 |

For Linear A the two numbers are the choice the field faces. Fifty-six anchored signs means a bilingual; 788 further units means roughly doubling the corpus, which means excavation. Neither is a computation: the count says that no amount of method closes the gap, and what would.

### 6. The case that would test this, and it has an answer

Linear Elamite was deciphered in 2022 by Desset and colleagues [6], after a century in which the field considered it out of reach. Its published quantities make it the natural test, because they run against the intuition the count is accused of merely restating. It has less material than Linear A, not more: 77 hypothesised signs against 110, and a corpus that stood at 25 inscriptions and 1,731 readable signs in the OCLEI supplement of 2020 [7], against the 7,147 of Linear A.

If the count measures corpus size, Linear Elamite should be further from decipherment than Linear A and it is not. What changed was not the quantity of text but three of the four inputs: the script is a closed alphasyllabary of five vowels, twelve consonants and sixty syllabic values with no logograms, so the space of assignments is smaller; the language was known, attested in cuneiform across two millennia, so the term for the choice of language vanishes; and the silver vessels from Kam-Firuz published in the 2000s supplied royal and divine names — Šilhaha, Eparti II, Napiriša — which is anchoring from outside in the strict sense.

The test is worth running and is not run here. Three of the four quantities are published; the fourth, the match rate, would have to be measured on the corpus, which is available through OCLEI and through the Hatamti database at Liège [8]. If the count returns a deficit for the corpus as it stood before the vessels and no deficit for the corpus after them, it will have reproduced a decipherment the field took a century to reach, and the timing of it. If it does not, the count is wrong and should be abandoned.

### 7. What the count does not do

It does not say a script is undecipherable. It says the corpus does not contain enough information to distinguish the right assignment from the many wrong ones [3], which is a different claim and a weaker one: an assignment may be correct and unprovable. It does not price the step from a phonetic value to a meaning, which is separate and which Etruscan shows to be the harder one. And its inputs are estimates: the match rate in particular depends on the target lexicon and on how permissive the phonology is assumed to be, and should be reported with the assumption that produced it.

It also inherits a limit from its own generosity. Because it counts every unit as independent when units share signs, the supply figure is an upper bound and the deficit a lower one. For Linear A the honest statement is *at least* 345 bits.

### 8. Why this is useful

A field that cannot say how much is missing cannot tell a hard problem from an impossible one, and cannot tell whether the next decade should be spent on method or on excavation. The count is crude, its inputs are four numbers, and it can be computed for any undeciphered script in an afternoon. Its value is not precision but direction: it converts "we do not know whether this can be read" into a figure, a currency and a target.

For Linear A the direction is unambiguous and the distance is 56 anchored signs. Whether the other undeciphered scripts are at a comparable distance or two orders of magnitude away is exactly what nobody knows, and what four measurable numbers per script would settle.

### Data and reproducibility
The module and its tests are in the accompanying repository. The Linear A figures are measured in the companion papers; the figures for the calibration scripts are drawn from their standard editions and are stated as estimates.

# Part IV. One day of trying, accounted for

### Summary

In August 2026 a complete Semitic reading of Linear A appeared [2] as a preprint with a DOI, an auditable catalogue of 67 readings, and its phonological conversion rules declared. This paper asks two questions of it and one of ourselves. Of it: how much of the claim can be verified from the corpus, and does it survive its own controls? Of ourselves: given a measured functional inventory and a set of verification instruments, can we produce a better reading, and what exactly is missing? The answers are, in order: 59 of the 67 catalogue entries verify against the corpus and the eight that do not are transliteration discrepancies, one of them the author's own correct correction of a published error; none of the four arguments supporting the reading survives its control; and no, we cannot produce a better reading, for a reason that can now be stated as a number. The free signs of the syllabary are 94. Our inventory of 151 functional readings constrains 39 of them. Once the constraint that units inherit from the positions the inventory fixes is counted, 69 of the 94 are reached and 25 remain — and of the 25 that remain, eight occur only on sealing supports, which are marks and not words in the account. Seven signs stand between this corpus and a fully constrained syllabary: 43 bits. One of those seven, \*309, is productive across eight forms on a single tablet and has not yet been analysed.

Keywords: Linear A, decipherment, verification, information theory, functional inventory.

### 1. What was verified of the claim, and what it withstands

The corpus facts hold. Of the 67 entries of the catalogue, 57 occur in the inscription cited, 2 occur elsewhere in the corpus, and 4 do not occur at all. Of those four, one is the author's own declared correction of a mis-transcription in the standard reference work [3], and our corpus confirms it; one is a segmentation difference; two are sign-number discrepancies (\*319 against \*904). For a catalogue of 67 entries assembled outside the academy, that is a high rate of accuracy in the corpus facts, and it should be said.

The four arguments do not. Each was measured with its own control.

*The lexical argument.* Under the conversion rules the author declares, 89.1% of Linear A units find a Semitic comparandum; Mycenaean Greek, which is not Semitic, finds one 79.7% of the time; and Packard's [1] fictitious grids reach 97.1%. Simulated annealing over the 38 free signs finds grids scoring 183 against 75 for the standard Linear B grid, changing 37 of 38 signs. The criterion does not merely fail to discriminate: it prefers assignments that are almost certainly wrong.

*Prefix conjugation.* The measure calibrates (Akkadian 1.28, Ugaritic 1.20, against Etruscan 1.08, Mycenaean 0.99, Hittite 0.89) and Linear A scores lowest of six at 0.85, but with nine cases against 10.6 expected the interval runs 0.54 to 1.16. No power.

*The tG stem.* Six pairs of units differ by an inserted T-series syllable in second position, p = 0.033 against a shuffled null. The same test on the other series gives six pairs for R and six for S; with twelve series tested the corrected p is 0.40. Measured, no signal.

*Mimation.* Word-final m-syllables occur in 7.1% of Linear A units against 3.1% in Mycenaean, p = 1.5·10⁻⁷ — the one measurement of this project that favoured the hypothesis. The Cypriot syllabary writing Greek gives 6.2%. Two syllabaries writing languages without mimation give 3.1% and 6.2%; the rate is set by the orthographic convention for final consonants. Withdrawn seven hours after being obtained.

And the double constraint returns nothing. Requiring both the vocalised form and the meaning a measured function demands, over 44,855 glossed entries (28,187 Akkadian across all dialects, 2,297 Ugaritic DULAT lemmas [5], 5,599 Sumerian), gives zero exact matches under a permissive phonology and zero under a strict one. Ugaritic is the language Gordon used in 1957 and the nearest relative the current proposal invokes, so this is the most direct available test of the Semitic hypothesis.

What this does not establish. It does not refute the reading. A correct reading would also produce many matches; what fails is the inference from many matches to correctness. And the reading rests in part on comparative Semitic morphology, which these instruments do not do and which a Semitist must judge.

### 2. Could we do better? The accounting

The reason for building the measurement was not to referee someone else's claim but to find out whether a verified functional inventory could reduce the space of readings enough to propose one. That question now has a number.

The universe. Specifying a decipherment means assigning a value to each free sign. The syllabary has 110 signs; sixteen are anchored by the place names shared with Linear B; 94 are free. At log₂(74) = 6.21 bits each, that is 584 bits, plus the choice of language. The corpus supplies at most 236 bits through lexical fit, so of the order of 2³⁵¹ assignments fit it equally well.

What one day of measurement bought. The functional inventory rose from 57 readings to 151: 65 fixed unit by unit, plus 86 by a class-level function (the opening position of a tablet is the label of the record and not an entry, p = 8·10⁻³⁴). Those 151 readings include 101 syllabic units.

| | Syllabic units read | Free signs they touch |
|---|---|---|
| Start of day | 22 | 18 of 94 |
| End of day | **101** | **39 of 94 (41%)** |

The universe shrank, and by a large factor: the signs carrying no constraint at all fell from 76 to 55, which is 130 bits, a reduction of 2¹³⁰.

What is missing, once context is counted. Fifty-five free signs carry no constraint from a directly read unit. But they are not in a vacuum: they sit inside units that occupy positions the inventory has fixed. A unit that opens a tablet is a record label whether or not the unit itself has ever been read; a unit taking a figure in a document whose other entries are read is a list entry; a unit standing before a commodity logogram is in the commodity frame.

Counting that inheritance:

| How the constraint arrives | Units | |
|---|---|---|
| List entry in a document with read units | 25 | |
| Opens a tablet (label, by class) | 10 | |
| Precedes a commodity | 4 | |
| **total inheriting a function from context** | **39** | |

Those 39 units touch 30 of the 55 signs. The floor therefore is not 342 bits but 155 bits over 25 signs, and 69 of the 94 free signs now carry some constraint, direct or inherited.

The 25 that remain do not form one class, and separating them changes the figure again.

Eight occur only on sealing supports: \*411 (15 occurrences, all roundels at Khania), \*408, \*333, \*328, \*417, \*905, \*351 and \*810. The sealing system has been shown to operate with twenty-eight marks and to share almost no vocabulary with the accounts (seven crossings against 34.4 expected). A sign that only marks sealings does not need a syllabic value *in the account*: it is a mark, not a word, and it does not stand between anyone and a reading of the archive.

Seven occur on tablets or on inscriptions: \*307 (8), \*314 (6), \*309 (6), \*805 (4), \*410, \*342 and \*350. These are the signs that genuinely remain, and at 6.21 bits each they are 43 bits.

Two of the seven have since been attacked. **\*309 is productive: its six occurrences are all on TY 2 from Tylissos, where twelve of the fourteen entries carry it, in three graphic variants and with nine distinct qualifying sequences. It is counted by pieces and not in bulk — none of its ten quantities takes a fraction, against 34% for the bulk commodities of the corpus, p = 0.017 — which places it with persons, livestock and discrete goods; which of those is not fixed, since all its attestations are in one document. \*307** occupies the header frame on HT 27a and HT 89 and qualifies oil at Petras, but the frame claim rests on two tablets and does not survive correction. The other five — \*314, \*805, \*410, \*342 and \*350 — have between one and six attestations, no repeated form among them, and are beyond any method that works on recurrence.

The answer to the question, corrected twice. The first accounting gave a floor of 342 bits over 55 signs. Counting the constraint units inherit from fixed positions brought it to 155 over 25. Separating the sealing marks, which are not words of the account, brings it to 43 bits over seven signs. The universe fell today from 76 unconstrained signs to seven: 429 bits.

We still cannot produce a reading, and the reason is exact, because the reason has changed in the course of one day. It is no longer that the corpus withholds too much: 43 bits over seven named signs is not an impassable wall. It is that constraining a sign is not the same as knowing its value. Every result in this work fixes what a unit *does*; none fixes what it *sounds like*, and the step between the two needs a judge the corpus does not contain. The seven signs are the boundary of the first kind of knowledge. The second kind has not been touched, and no quantity of the first produces it.

### 3. What would be needed, priced

Each sign anchored from outside removes 6.21 bits. Closing the 43 that remain would take seven anchored signs, which is a small number and a hard one: they are precisely the signs no distributional method reaches, because five of the seven occur between one and six times with no repeated form. Partial closure is proportional, and the realistic target is whichever of the seven a new document happens to attest again.

Three sources, in order of what they would buy:

1. A bilingual, or running text in a known language naming Minoan things. This is what Iberian has and Minoan does not, and the contrast is the whole difference between the two cases: with two dozen names from the Ascoli bronze, the same instruments recover Untermann's [4] formants and two isoglosses; with six consonantal place names, they recover functions and no words.
2. New tablets increasing the attestation count of the rare signs. Thirty-two signs at one occurrence need a second and a third before any distributional instrument can see them.
3. Better readings of the existing editions. Marginal, but real: 276 of 783 syllabic units are broken in every attestation, and some of them are the same units in different states.

All three come out of the ground or out of the archive, and none out of computation.

### 4. What the exercise leaves

The instrument works, and what it produced is useful: a functional description of the archive of Haghia Triada that does not depend on reading a word, and a scale on which any proposal can be placed before publication. What it also produced, and this is the part that answers the question it was built for, is the boundary itself, stated as a quantity rather than as a feeling.

That boundary cuts both ways, and it should. It says the reading under review cannot be shown correct with this corpus. It says ours cannot either, and we have not attempted one. And it says that the next person to propose a decipherment of Linear A will face the same seven signs, whatever their method and however good their idea, until someone digs up a document that attests them again.

### Data and reproducibility
Corpus, code, null models, error rates, the fourteen closed avenues and the eleven withdrawn claims, each with its measurement, at github.com/BiomeMakers/kuro.

---

## References

[1] Godart, L. and Olivier, J.-P. 1976-1985. *Recueil des inscriptions en linéaire A* (GORILA), 5 vols. Paris: Geuthner.

[2] Packard, D. W. 1974. *Minoan Linear A*. Berkeley: University of California Press.

[3] Duhoux, Y. 1989. "Le linéaire A: problèmes de déchiffrement." In *Problems in Decipherment*, 59-119.

[4] Ventris, M. and Chadwick, J. 1953. "Evidence for Greek dialect in the Mycenaean archives." *Journal of Hellenic Studies* 73: 84-103.

[5] Luo, J., Hartmann, F., Santus, E., Barzilay, R. and Cao, Y. 2021. "Deciphering undersegmented ancient scripts using phonetic prior." *Transactions of the Association for Computational Linguistics* 9: 69-81.

[6] Salgarella, E. and Castellan, S. 2021. SigLA: The Signs of Linear A, a palaeographical database. sigla.phis.me.

[7] Untermann, J. 1990. *Monumenta Linguarum Hispanicarum III: Die iberischen Inschriften aus Spanien*. Wiesbaden: Reichert.

[8] Shannon, C. E. 1948. "A mathematical theory of communication." *Bell System Technical Journal* 27: 379-423, 623-656.

[9] Chadwick, J. 1958. *The Decipherment of Linear B*. Cambridge: Cambridge University Press.

[10] Rix, H. 1991. *Etruskische Texte: Editio minor*. Tübingen: Narr.

[11] Desset, F. 2020. "Nine Linear Elamite texts inscribed on silver 'gunagi' vessels." *Iran* 60: 1-29. With the OCLEI supplement.

[12] Desset, F., Tabibzadeh, K., Kervran, M., Basello, G. P. and Marchesi, G. 2022. "The decipherment of Linear Elamite writing." *Zeitschrift für Assyriologie* 112 (1): 11-60. Hatamti database, University of Liège.

[13] Farmer, S., Sproat, R. and Witzel, M. 2004. "The collapse of the Indus-script thesis: the myth of a literate Harappan civilization." *Electronic Journal of Vedic Studies* 11 (2): 19-57.

[14] Dahl, J. L. 2019. *Tablettes et fragments proto-élamites*. Paris: Éditions Khéops.

[15] di Mino, T. 2026. *Ya Diktu*. Preprint, doi 10.5281/zenodo.22129502.

[16] Copenhagen Ugaritic Corpus (CACCHT), doi 10.5281/zenodo.10695308, CC BY-NC 4.0.

## Acknowledgements

I am a biotechnologist by training and came to the Aegean scripts from outside the field. Several of its specialists answered a stranger's letters, and this work would be poorer or wrong without them.

Margalit Finkelberg (Tel Aviv) sent me her 1995 paper with Alexander Uchitel and her 2001 study of the Minoan language, and raised two objections that changed the text: one on the affiliation of Etruscan, which I had treated as settled when it is not, and one that led me to find two faults in my own value search. Barbara Montecchi (Bologna) sent me her 2019 monograph on counting at Haghia Triada. José Miguel Jiménez Delgado (Seville) corrected the reading of the *-qe* ending and offered further help. Miguel Valério (Murcia) agreed to read the work; I later found that a reading I had reconstructed independently was his, published in 2007. Robert Hogan, who maintains the Linear A Explorer, answered on the data and has collaborated since.

None of them is responsible for anything asserted here.

The corpus rests on the published editions of GORILA (Godart and Olivier), on SigLA (Salgarella and Castellan), on the Linear A Explorer, and on NESTOR (University of Cincinnati), whose bulletins are the bibliographical filter this work applies before claiming anything is new.

## An open invitation

Every measurement in this paper is reproducible. The corpus, the code, the null models and the manifest that holds every figure asserted here are public at github.com/BiomeMakers/kuro, and the manifest names, for each claim, the condition that would refute it.

I would rather be corrected now than in print. If a measurement here is wrong, if a claim has prior art I have missed, or if a null is badly built, I want to know — and the repository is set up so that anyone can check without taking my word for it. Sixteen apparent findings of this project turned out to be already published; each was caught by a three-minute search. There will be a thirteenth, and I would like it found by someone else before it reaches a journal.

Anyone who wants to run these tests on another corpus, or to break them on this one, is welcome to write: acedo@biomemakers.com.

## Statement of artificial intelligence assistance

The measurements and the drafting of this paper were carried out with the assistance of a language model (Claude, Anthropic), under the design, verification and responsibility of the author. Every figure asserted here is recorded in the project manifest with its null model, its number of observations and its p-value, and the code that produces it is public.
