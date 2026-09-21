# One day of trying to read Linear A, accounted for

**Alberto Acedo**
Biome Makers Inc. Version 1.0, 12 September 2026. Not for circulation.

## Summary

In August 2026 a complete Semitic reading of Linear A appeared [2] as a preprint with a DOI, an auditable catalogue of 67 readings, and its phonological conversion rules declared. This paper asks two questions of it and one of ourselves. Of it: how much of the claim can be verified from the corpus, and does it survive its own controls? Of ourselves: given a measured functional inventory and a set of verification instruments, can we produce a better reading, and what exactly is missing? The answers are, in order: 59 of the 67 catalogue entries verify against the corpus and the eight that do not are transliteration discrepancies, one of them the author's own correct correction of a published error; none of the four arguments supporting the reading survives its control; and no, we cannot produce a better reading, for a reason that can now be stated as a number. The free signs of the syllabary are 94. Our inventory of 151 functional readings constrains 39 of them. **Once the constraint that units inherit from the positions the inventory fixes is counted, 69 of the 94 are reached and 25 remain** — and of the 25 that remain, eight occur only on sealing supports, which are marks and not words in the account. **Seven signs stand between this corpus and a fully constrained syllabary: 43 bits.** One of those seven, \*309, is productive across eight forms on a single tablet and has not yet been analysed.

**Keywords:** Linear A, decipherment, verification, information theory, functional inventory.

## 1. What was verified of the claim, and what it withstands

**The corpus facts hold.** Of the 67 entries of the catalogue, 57 occur in the inscription cited, 2 occur elsewhere in the corpus, and 4 do not occur at all. Of those four, one is the author's own declared correction of a mis-transcription in the standard reference work [3], and our corpus confirms it; one is a segmentation difference; two are sign-number discrepancies (\*319 against \*904). For a catalogue of 67 entries assembled outside the academy, that is a high rate of accuracy in the corpus facts, and it should be said.

**The four arguments do not.** Each was measured with its own control.

*The lexical argument.* Under the conversion rules the author declares, 89.1% of Linear A units find a Semitic comparandum; Mycenaean Greek, which is not Semitic, finds one 79.7% of the time; and Packard's [1] fictitious grids reach 97.1%. Simulated annealing over the 38 free signs finds grids scoring 183 against 75 for the standard Linear B grid, changing 37 of 38 signs. **The criterion does not merely fail to discriminate: it prefers assignments that are almost certainly wrong.**

*Prefix conjugation.* The measure calibrates (Akkadian 1.28, Ugaritic 1.20, against Etruscan 1.08, Mycenaean 0.99, Hittite 0.89) and Linear A scores lowest of six at 0.85, but with nine cases against 10.6 expected the interval runs 0.54 to 1.16. **No power.**

*The tG stem.* Six pairs of units differ by an inserted T-series syllable in second position, p = 0.033 against a shuffled null. The same test on the other series gives six pairs for R and six for S; with twelve series tested the corrected p is 0.40. **Measured, no signal.**

*Mimation.* Word-final m-syllables occur in 7.1% of Linear A units against 3.1% in Mycenaean, p = 1.5·10⁻⁷ — the one measurement of this project that favoured the hypothesis. The Cypriot syllabary writing Greek gives 6.2%. Two syllabaries writing languages without mimation give 3.1% and 6.2%; the rate is set by the orthographic convention for final consonants. **Withdrawn seven hours after being obtained.**

**And the double constraint returns nothing.** Requiring both the vocalised form and the meaning a measured function demands, over 44,855 glossed entries (28,187 Akkadian across all dialects, 2,297 Ugaritic DULAT lemmas [5], 5,599 Sumerian), gives zero exact matches under a permissive phonology and zero under a strict one. Ugaritic is the language Gordon used in 1957 and the nearest relative the current proposal invokes, so this is the most direct available test of the Semitic hypothesis.

**What this does not establish.** It does not refute the reading. A correct reading would also produce many matches; what fails is the inference from many matches to correctness. And the reading rests in part on comparative Semitic morphology, which these instruments do not do and which a Semitist must judge.

## 2. Could we do better? The accounting

The reason for building the measurement was not to referee someone else's claim but to find out whether a verified functional inventory could reduce the space of readings enough to propose one. That question now has a number.

**The universe.** Specifying a decipherment means assigning a value to each free sign. The syllabary has 110 signs; sixteen are anchored by the place names shared with Linear B; **94 are free**. At log₂(74) = 6.21 bits each, that is 584 bits, plus the choice of language. The corpus supplies at most 236 bits through lexical fit, so of the order of 2³⁵¹ assignments fit it equally well.

**What one day of measurement bought.** The functional inventory rose from 57 readings to 151: 65 fixed unit by unit, plus 86 by a class-level function (the opening position of a tablet is the label of the record and not an entry, p = 8·10⁻³⁴). Those 151 readings include 101 syllabic units.

| | syllabic units read | free signs they touch |
|---|---|---|
| start of day | 22 | 18 of 94 |
| end of day | **101** | **39 of 94 (41%)** |

The universe shrank, and by a large factor: the signs carrying no constraint at all fell from 76 to 55, which is 130 bits, a reduction of 2¹³⁰.

**What is missing, once context is counted.** Fifty-five free signs carry no constraint from a directly read unit. But they are not in a vacuum: they sit inside units that occupy positions the inventory has fixed. A unit that opens a tablet is a record label whether or not the unit itself has ever been read; a unit taking a figure in a document whose other entries are read is a list entry; a unit standing before a commodity logogram is in the commodity frame.

Counting that inheritance:

| how the constraint arrives | units | |
|---|---|---|
| list entry in a document with read units | 25 | |
| opens a tablet (label, by class) | 10 | |
| precedes a commodity | 4 | |
| **total inheriting a function from context** | **39** | |

Those 39 units touch **30 of the 55 signs**. The floor therefore is not 342 bits but **155 bits over 25 signs**, and 69 of the 94 free signs now carry some constraint, direct or inherited.

The 25 that remain do not form one class, and separating them changes the figure again.

**Eight occur only on sealing supports**: \*411 (15 occurrences, all roundels at Khania), \*408, \*333, \*328, \*417, \*905, \*351 and \*810. The sealing system has been shown to operate with twenty-eight marks and to share almost no vocabulary with the accounts (seven crossings against 34.4 expected). A sign that only marks sealings does not need a syllabic value *in the account*: it is a mark, not a word, and it does not stand between anyone and a reading of the archive.

**Seven occur on tablets or on inscriptions**: \*307 (8), \*314 (6), \*309 (6), \*805 (4), \*410, \*342 and \*350. These are the signs that genuinely remain, and at 6.21 bits each they are **43 bits**.

Two of the seven have since been attacked. **\*309 is productive**: its six occurrences are all on TY 2 from Tylissos, where twelve of the fourteen entries carry it, in three graphic variants and with nine distinct qualifying sequences. It is counted by pieces and not in bulk — none of its ten quantities takes a fraction, against 34% for the bulk commodities of the corpus, p = 0.017 — which places it with persons, livestock and discrete goods; which of those is not fixed, since all its attestations are in one document. **\*307** occupies the header frame on HT 27a and HT 89 and qualifies oil at Petras, but the frame claim rests on two tablets and does not survive correction. The other five — \*314, \*805, \*410, \*342 and \*350 — have between one and six attestations, no repeated form among them, and are beyond any method that works on recurrence.

**The answer to the question, corrected twice.** The first accounting gave a floor of 342 bits over 55 signs. Counting the constraint units inherit from fixed positions brought it to 155 over 25. Separating the sealing marks, which are not words of the account, brings it to **43 bits over seven signs**. The universe fell today from 76 unconstrained signs to seven: **429 bits**.

**We still cannot produce a reading**, and it is worth being exact about why, because the reason has changed in the course of one day. It is no longer that the corpus withholds too much: 43 bits over seven named signs is not an impassable wall. It is that constraining a sign is not the same as knowing its value. Every result in this work fixes what a unit *does*; none fixes what it *sounds like*, and the step between the two needs a judge the corpus does not contain. The seven signs are the boundary of the first kind of knowledge. The second kind has not been touched, and no quantity of the first produces it.

## 3. What would be needed, priced

**Each sign anchored from outside removes 6.21 bits.** Closing the 43 that remain would take seven anchored signs, which is a small number and a hard one: they are precisely the signs no distributional method reaches, because five of the seven occur between one and six times with no repeated form. Partial closure is proportional, and the realistic target is whichever of the seven a new document happens to attest again.

Three sources, in order of what they would buy:

1. **A bilingual, or running text in a known language naming Minoan things.** This is what Iberian has and Minoan does not, and the contrast is the whole difference between the two cases: with two dozen names from the Ascoli bronze, the same instruments recover Untermann's [4] formants and two isoglosses; with six consonantal place names, they recover functions and no words.
2. **New tablets increasing the attestation count of the rare signs.** Thirty-two signs at one occurrence need a second and a third before any distributional instrument can see them.
3. **Better readings of the existing editions.** Marginal, but real: 276 of 783 syllabic units are broken in every attestation, and some of them are the same units in different states.

All three come out of the ground or out of the archive, and none out of computation.

## 4. What the exercise leaves

The instrument works, and what it produced is worth having: a functional description of the archive of Haghia Triada that does not depend on reading a word, and a scale on which any proposal can be placed before publication. What it also produced, and this is the part that answers the question it was built for, is the boundary itself, stated as a quantity rather than as a feeling.

That boundary cuts both ways, and it should. It says the reading under review cannot be shown correct with this corpus. It says ours cannot either, and we have not attempted one. And it says that the next person to propose a decipherment of Linear A will face the same seven signs, whatever their method and however good their idea, until someone digs up a document that attests them again.

## References
[1] Packard, D. W. 1974. *Minoan Linear A*. Berkeley: University of California Press.
[2] di Mino, T. 2026. *Ya Diktu*. Preprint, doi 10.5281/zenodo.22129502.
[3] Godart, L. and Olivier, J.-P. 1976-1985. *Recueil des inscriptions en linéaire A* (GORILA), 5 vols. Paris.
[4] Untermann, J. 1990. *Monumenta Linguarum Hispanicarum III*. Wiesbaden: Reichert.
[5] Copenhagen Ugaritic Corpus (CACCHT), doi 10.5281/zenodo.10695308, CC BY-NC 4.0.

## Data and reproducibility
Corpus, code, null models, error rates, the fourteen closed avenues and the eleven withdrawn claims, each with its measurement, at github.com/BiomeMakers/kuro.

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
