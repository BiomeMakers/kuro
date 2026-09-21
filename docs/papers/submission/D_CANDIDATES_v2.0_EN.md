# Thirteen candidate languages for Minoan, measured

Alberto Acedo
Independent researcher Version 1.0, 16 September 2026.

## Summary

For a century, proposals have assigned Linear A to a language family — Semitic, Luwian, Hittite, Hurrian, Indo-European — and each has exhibited lexical matches in support. None has measured how many matches chance produces. This paper supplies the missing measurement, and the result is not a ranking of candidates but a verdict on the criterion. Five findings. First, under an anchored search over sign values calibrated against a control corpus, no candidate exceeds z = 2.3, and that one is Luwian, the proposal the field abandoned sixty years ago on archaeological grounds; the Semitic candidates sit at chance (Ugaritic 0.1, Akkadian 0.4) and Hurrian and Etruscan fall below the control (−2.3 and −3.2). Second, under the phonological conversion rules that a CV syllabary imposes and that recent proposals declare explicitly, 89.1% of Linear A units find a Semitic comparandum, Mycenaean Greek finds one 79.7% of the time, and Packard's fictitious grids [1] reach 97.1%: finding a comparandum carries no information. Third, simulated annealing over the 38 free signs finds grids scoring 183 against 75 for the standard Linear B grid [9], changing 37 of 38 signs: optimising for lexical fit actively prefers grids that are almost certainly wrong. Fourth, a screening that requires both the vocalised form and the meaning a measured function demands returns zero candidates over 44,855 glossed entries of Akkadian, Ugaritic and Sumerian, under both a permissive and a strict phonology. Fifth, searching with the functional constraint as the sole objective satisfies 1 of 20 constraints against 0 for the standard grid: with lexical fit alone there are too many solutions and the best are false, with the functional constraint added there are none. Sixth, the phonological profile, measured here for the first time against a null, yields the one hard constraint this work produces — Minoan barely uses the vowel o, 4.7% against 26.7% in Mycenaean — but three structural features give three different answers as to which candidate it favours, which is the result reported for structural phylogenetics generally. Seventh, an information count explains all of the above: specifying a decipherment costs 587 bits and the corpus supplies at most 236, so of the order of 2³⁵¹ assignments fit it equally well. Linear A is not thereby undecipherable but that this corpus cannot decide, and that any proposal resting on the number of translations achieved is using a measure that rewards the opposite of what it seeks.

Keywords: Linear A, decipherment, null models, Packard test, information theory, language classification.

## 1. A century of proposals and no common test

The proposals are well known and mutually exclusive. Gordon [2] (1957, 1966) read Minoan as Northwest Semitic; Palmer [3] (1958-61) as Luwian; Davis (1960s) as Hittite; Best (1970s-80s) as Semitic again; Owens (2004) as Indo-European; van Soesbergen [5] (2022) as Hurrian across eight volumes and 4,100 pages; and in August 2026 a new Semitic reading [14] appeared as a preprint with a DOI and an auditable catalogue of readings.

Quantitative work on the corpus exists and is careful where it stays within the archive: the values of the fraction signs were fixed by Corazza and colleagues [6], and Tamburini [7] has surveyed the computational methods applied to undeciphered scripts. What has not been done is the control.

Each exhibits matches. None reports how many matches an incorrect assignment would produce. That control was invented for this very corpus: Packard [1] (1974) built nine fictitious decipherments by redistributing the Linear B values so that no sign kept its own, and compared their matches with those of the correct assignment. No proposal in the list above includes it.

This paper applies it, and three further tests that follow from it.

## 2. Where each candidate lands

The anchored value search optimises the values of the unanchored signs and compares the fit against a control corpus with no language. Thirteen candidates, sixteen signs anchored by the place names shared with Linear B.

| Proposal | Language | Why it did not prevail | z |
|---|---|---|---|
| Palmer 1958 | Luwian | No archaeological evidence for the Luwian invasions of Crete the theory required (Mylonas [4] 1962) | **2.3** |
| Davis 1960s | Hittite | Did not prosper | 1.5 |
| Facchetti & Negri 2003 | Indo-European | Comparison through an already read language | 1.3 |
| Gordon 1957-66 | Semitic | Lexical matches without grammatical grounding | 0.1 (Ugaritic) |
| Di Mino 2026 | Central Semitic | Under review | 0.1 / 0.4 (Akkadian) |
| Finkelberg [11] 2001 | Anatolian, with Lycian its descendant | A fourteen-point morphological profile rather than an etymological argument; not taken up | (Luwian **2.3**, Hittite 1.5) |
| Van Soesbergen 2022 [5] | Hurrian | Not taken up by the field | **−2.3** |
| (not proposed) | Etruscan | — | **−3.2** |


The anchored value search, rerun after two faults were found in its construction. The first table of this search used five control runs and, more seriously, two targets that were not comparable: the Minoan consonant skeletons carried editorial marks the shuffled control could not reproduce, and the eleven candidate lexicons ranged from a deduplicated lemma list (Ugaritic, one entry per word) to raw token dumps carrying Sumerograms, cuneiform signs and clitics (Hattian repeats one form 113 times; the commonest Hurrian entry is a cuneiform sign occurring 1,194 times). Normalising the targets removes more than 90% of what was being used as the Akkadian and Sumerian lexicons. Rerun at 6,000 steps with twenty controls and normalised targets:

| Language | z | | Language | z |
|---|---|---|---|---|
| Etruscan | **+1.75** | | Mycenaean | −0.90 |
| Luwian | +1.30 | | Akkadian | −1.15 |
| Ugaritic | +1.28 | | Sumerian | −2.59 |
| Iberian | +0.99 | | Hattian | −3.32 |
| Hittite | +0.22 | | Hurrian | −4.04 |
| Palaic | −0.19 | | | |

No candidate reaches z = 3 and the highest is +1.75. Under any assignment of values compatible with the shared place names, Minoan resembles none of the eleven more than a Minoan stripped of its sequences can be made to resemble them.

The implicit control holds. Mycenaean returns −0.90: Linear A is known not to be Greek, and the instrument places Greek in the group with no signal. Had it fired, the rest of the table would be worthless.

And the reason the lexical criterion cannot discriminate is visible in the same run. Optimisation improves the distance to every target by between a third and two thirds — Hittite from 0.296 to 0.193, Iberian from 0.365 to 0.209, Etruscan from 0.297 to 0.101. With 59 free values, any corpus can be brought close to any target.

Two limitations are declared with the result. The seven cuneiform-transmitted languages average −1.40 against +0.78 for the other four, a bias no normalisation on our side corrects; and the two most negative values, Hurrian and Hattian, are the two isolates of the set, known only from Hittite archives and from a single genre, whose vocabularies are not general lexicons. A negative z is not evidence about kinship: it says the shuffled corpus suits that target better than the real one, which points to a mismatch of profiles.

No candidate reaches significance, and the highest is +1.75. The first pass of this search was worthless for reasons that are the reasons this paper exists: it used five controls, its Minoan skeletons carried editorial marks the control could not reproduce, and its eleven targets ranged from a deduplicated lemma list to raw token dumps of a different kind of object. Corrected, the instrument returns what a calibrated instrument returns when there is nothing to find. Nothing reaches significance, so nothing is established; but it should be recorded that the two candidates the measurement ranks highest are those of the one proposal in this list that rejects the etymological method. Finkelberg [11] (2001) builds a morphological profile of fourteen features and compares it against five Anatolian languages, having first dismantled the Semitic and Luwian proposals for the same methodological failure this paper measures. Her features rest for the most part on the votive formula rather than on the archive, so her profile and the functional inventory used here describe different genres and do not meet except at *a-du*, where the distributional reading holds (12 of 17 attestations of her verbal paradigm occupy first position, base rate 0.405, p = 0.012). The Semitic candidates are indistinguishable from a corpus with no language. Hurrian and Etruscan sit *below* the control: the real corpus resembles them less than a shuffled corpus does.

## 3. Finding a comparandum carries no information

A CV syllabary cannot write voicing or emphasis; sibilants merge into one series; laryngeals often go unwritten; neither consonantal nor vocalic length is marked. Recent proposals declare these rules explicitly, which is a merit and makes them testable. Under them, a Linear A sign group corresponds not to a word but to a *class* of words, and the size of that class is measurable.

Reducing the 615 intact syllabic units to their skeleton under those rules, and the complete Ugaritic lexicon plus 60,000 Akkadian forms likewise:

| | Fraction finding a Semitic comparandum |
|---|---|
| **Linear A with the Linear B grid** | **89.1%** |
| Mycenaean, which is Greek | 79.7% |
| **Linear A with a fictitious grid (Packard)** | **97.1%** (min 91.0, max 99.5, 40 grids) |

z of the real corpus against the fictitious grids: −4.71. A deliberately false assignment finds Semitic comparanda *better* than the correct one, and Greek finds them four times in five. This does not refute any reading: it fixes where the weight of a reading must lie, which is not in the existence of a comparandum.

The same holds across languages. Under permissive phonology, the fraction of units finding a match runs from 53.7% (Palaic) to 88.6% (Hurrian), mean 73.8%. The language that matches best is the one that scores worst under the anchored search.

## 4. Optimising for lexical fit prefers false grids

Scoring one grid is one thing; searching for the best is another, and no proposal has done it. Simulated annealing over the 38 free signs, with the objective any decipherment pursues — how many units become real words of the target language, plus ten times how many of those also mean what a measured function requires:

| | Permissive phonology | Strict phonology |
|---|---|---|
| **Linear B grid** | Lexical **75**, functional 0 | Lexical **40**, functional 0 |
| Best found by search | **183** | **131** |
| Signs changed from Linear B | **37 of 38** | **38 of 38** |

Three runs from independent seeds converge. The search finds grids 2.4 to 3.3 times better than the standard grid, and to reach them it changes every free sign. This is Packard's 1974 result redone with a modern optimiser and a real lexicon, and it is stronger than his: fictitious grids do not merely tie, they win.

The criterion is therefore not weak but counterproductive. Any proposal resting on the number of translations achieved is using a measure that rewards the opposite of what it seeks.

## 5. Requiring form and meaning together returns nothing

The one criterion that survives optimisation is the functional one, because it is the only one no grid satisfies. It can be applied where an independent inventory fixes what a unit does in the account [8].

For each Linear A unit with a measured function, the glossed lexicons of ORACC and the Copenhagen Ugaritic Corpus [12] (44,855 entries: 28,187 Akkadian across all dialects, 2,297 Ugaritic lemmas with DULAT glosses over 278 KTU tablets, 5,599 Sumerian) were searched for words that both sound like the unit under the grid and mean what its function demands.

| Phonology | Units tested | With a candidate | With an **exact** match |
|---|---|---|---|
| Permissive | 15 | 1 (KU-RO against Sumerian *gu* "entirety", by prefix) | **0** |
| Strict | 15 | **0** | **0** |

Both phonologies were run and both are reported, because the severity of the phonology is not a free choice but a hypothesis about the script, and 243 bits of discrimination ride on it. The result is reliable to the assumption that weighs most.

A methodological note. With consonantal skeletons alone, four candidates appeared, two of them attractive: KU-RO and KI-RO both matched Akkadian *kalû* "all" with the meanings the distribution requires, total and deficit. They are spurious. KU-RO and KI-RO share a consonantal skeleton and have distinct meanings fixed by distribution, so they cannot be the same word. Linear A writes its vowels, and discarding them is discarding information the corpus has. No screening that fails to distinguish KU-RO from KI-RO is worth running, and none published so far makes that distinction.


## 5 bis. And no grid satisfies them either

The screening above ran on one grid, the standard Linear B values. That leaves the obvious defence open: perhaps the values are wrong rather than the language. The defence can be tested, not by enumerating the space, which is impossible, but by searching it with the functional constraint as the sole objective.

Twenty units whose measured function fixes a semantic class (five headers, three totals, one deficit, one offering, three place names, five parties, two textiles) are touched by thirty signs, seventeen of them free. The lexicon is the glossed entries of ORACC and the Copenhagen Ugaritic Corpus sorted by class: 45 words meaning totality, 35 deficit, 52 record, 127 offering, 275 person, 140 place, 152 textile. Objective: how many of the twenty become a word of their class. Simulated annealing over the seventeen free signs, eight independent seeds, 6,000 steps each.

| | Functions satisfied of 20 |
|---|---|
| The Linear B grid | **0** |
| Best found by annealing | **1**, and it is spurious |

No assignment of values in the space searched makes two of the measured functions come out at once as words of Akkadian, Ugaritic or Sumerian meaning what their position requires.

Set beside §4, that completes a figure worth stating plainly. With lexical fit alone as the criterion there are far too many solutions and the best of them are certainly false; with the functional constraint added there are none. The criterion the field uses yields too many answers, and the criterion that measures what the archive does yields no answer at all. Between the two there is no reading.

Three limits are declared with the result. The lexicon per class is small, between 35 and 275 words, where the real vocabulary of each language is larger and the English glosses do not cover every synonym. Three languages of the thirteen candidates, the only ones with a glossed lexicon available. And seventeen signs, not ninety-four, because only those touch units with a measured function.

## 5 ter. What this does not decide, and it is not the language

There is a premise under all of the above that this result brings into view and does not settle. We have assumed that a unit whose function is fixed is a word meaning that function: that KU-RO, which sums, is the word for "total". It need not be. It could be an abbreviation, as Linear B writes its commodities; a logogram spelled out; a technical term inherited from another administration; or a name. If the Minoan archive writes its functional vocabulary the way Linear B writes *ku-pa-ro* as CYP+KU, then no language would return those units as words, and the negative above would be a fact about Minoan orthography rather than about Minoan language.

That possibility is opened by this measurement and closed by none. It is the first alternative a reader should raise, and we have no test for it.

## 6. Three morphological tests, and a retraction

The recent Semitic proposal rests on three morphological features rather than on the lexicon alone. All three are measurable without any etymology, and all three can be calibrated on languages whose answer is known.

Prefix conjugation. Stems appearing with two or more distinct first units, and how many of those alternations use the Semitic prefix set. The measure calibrates: Akkadian 1.28 and Ugaritic 1.20 against Etruscan 1.08, Mycenaean 0.99 and Hittite 0.89. Linear A scores 0.85, the lowest of the six, but with nine observed against 10.6 expected the interval runs from 0.54 to 1.16. No power: 72 alternating stems do not decide.

The tG stem. An infixed -t- after the first root consonant predicts pairs of units differing by an inserted T-series syllable in second position. Six such pairs exist, and they are the ones one would wish to see: A-TA-DE ~ A-DE, DA-TA-RE ~ DA-RE, I-TA-JA ~ I-JA, A-TI-RU ~ A-RU. Against a shuffled null, p = 0.033. But the same test on the other consonant series gives 6 pairs for R and 6 for S; the T series does not stand out, and with twelve series tested the corrected p is 0.40. Measured, and no signal.

Mimation, and its retraction. Word-final m-syllables occur in 7.1% of Linear A units against 3.1% in Mycenaean, p = 1.5·10⁻⁷ — the only measurement in this work that favoured the Semitic hypothesis. A second syllabic control annuls it. The Cypriot syllabary writing Greek gives 6.2% over 693 words. Two syllabaries writing languages without mimation give 3.1% and 6.2%: the rate is set by the orthographic convention for final consonants, not by the language, and Linear A at 7.1% is indistinguishable from the Cypriot rate.

This retraction carries a general lesson worth more than the result: when one script is compared with another, the control must be a script of the same kind, and more than one. A single witness produced a p of 1.5·10⁻⁷ that meant nothing.


# 6 bis. The phonological profile, and why three features give three answers

The tests above all concern the lexicon. A second criterion has been available to the field since Lejeune [10] (1956) and has never been measured: the phonological profile of Minoan, and its comparison with the candidates. It is measured here, and it fails in a different way from the lexicon, which is what makes it worth reporting.

## 6 bis.1 The o-series, and what it excludes

A caution on the o-series. The scarcity of o-series signs in Linear A is measured here and is not in dispute. What it means is. Four readings stand in the literature and none is ours: that Minoan lacked /o/, in a three-vowel system (the traditional reading, treated by Packard 1974 and by Palaima and Sikkenga 1999); that Minoan had *more* than five vowels (Duhoux 1989, 72-73); that e and o are secondary developments from an original three-vowel system by contraction of i-diphthongs (Davis 2014, 240-241); and, most recently, that the scarcity is due to chances of attestation given how few o-series correspondences are known at all (Meissner and Steele, a position Judson calls persuasive).

Two measurements of our own bear on it, and the second corrects the first. Screened against PHOIBLE, which holds living languages, 112 of 3,020 inventories have a, e, i and u and lack /o/ — 7.8% of those with all four — and none is in the eastern Mediterranean. That suggested a Minoan without /o/ would be typologically exceptional.

Screened against BDPROTO, which holds 212 ancient and reconstructed languages, the conclusion reverses: 21% of ancient languages with three or more vowels lack a vowel of o quality, nearly three times the living rate, and seven are of the Near East and Aegean — Hittite (a, e, i, u), Akkadian (a, e, i, u), Palaic, Cuneiform Luwian, Urartian, Hattic and Aramaic — against Hurrian, Sumerian, Elamite, Phoenician, Ugaritic, Phrygian and Greek, which have it. A four-vowel Minoan would be ordinary for its area. The first screen compared a Bronze Age language with living ones, which is the temporal bias the authors of BDPROTO themselves flag.

And a measurement on the open question. If Minoan had four vowels, the Mycenaeans would have added the o-series when adapting the script, and its signs would show fewer Linear A correspondences than the other series. Over the 82 Linear B syllabograms: the i-series has a known correspondence in 100% of cases, the u-series in 90%, the e-series in 69%, the a-series in 67%, and the o-series in 35%, 6 of 17, p = 0.017 against the overall rate of 63%. The shortfall is specific to the o-series and is not explained by the average rate, which makes those eleven signs candidates for Mycenaean innovation.

Accordingly, no argument in this paper rests on Minoan lacking /o/. The measurement is reported as a fact about the script's attested signs, and the question of the language's vowel system is left where the field has it.


Over 3,085 syllabic positions of the intact corpus, eight signs of the o-series have zero occurrences (jo, mo, no, qo, so, wo, do, zo); o, po and to are rare (8, 7 and 14); ro is frequent (86) and ko is not (11). The series as a whole is 4.7% of the vowels of Minoan against 26.7% of Mycenaean, and 0.9% if ro and ko are set aside as Finkelberg (2001) suggests they may be. The reverse holds for u: 17.4% against 7.7%.

The doublets Lejeune observed also survive a null for the first time. Of the ninety intact units ending in -u, sixteen have an exact -o counterpart in the Linear B lexicon (a-ru/a-ro, di-de-ru/di-de-ro, ka-ru/ka-ro, qa-qa-ru/qa-qa-ro, si-tu/si-to and eleven more), against 8.0 expected when the final vowel is replaced at random by a, e or i (500 repetitions, maximum 14, p < 0.002).

This is the first hard phonological constraint the work produces, and unlike everything else in this paper it constrains rather than closes: any language proposed for Linear A must account for a vowel system that barely uses o.

## 6 bis.2 The profile across ten languages

The constraint can only be applied to languages written in a system that distinguishes o, which excludes the seven cuneiform candidates [12]: their transliterations return 0.0% as a property of the script. Distance is total variation against Minoan.

| | a | e | i | **o** | u | Distance | Vowels |
|---|---|---|---|---|---|---|---|
| **Minoan** | 40.5% | 13.2% | 24.2% | **4.7%** | 17.4% | — | 2,677 |
| Lydian | 46.4% | 12.8% | 25.7% | 7.5% | 7.6% | **0.102** | 2,955 |
| Etruscan | 37.6% | 19.4% | 29.1% | 2.3% | 11.6% | 0.111 | 22,849 |
| Iberian | 29.5% | 22.1% | 29.5% | 8.2% | 10.7% | 0.177 | 9,397 |
| Sidetic | 43.1% | 16.8% | 13.2% | 17.4% | 9.6% | 0.189 | 167 |
| Carian | 24.3% | 10.7% | 22.3% | 19.4% | 23.3% | 0.205 | 1,578 |
| Pisidian | 24.9% | 19.3% | 20.8% | 24.3% | 10.7% | 0.257 | 711 |
| Lycian B | 24.2% | 34.9% | 29.0% | 0.0% | 11.8% | 0.266 | 1,821 |
| Lycian | 24.7% | **39.0%** | 28.9% | **0.2%** | 7.2% | **0.304** | 11,957 |
| Mycenaean | 27.7% | 22.3% | 15.8% | **26.3%** | 7.9% | 0.307 | 18,380 |

The poverty of o excludes Greek, as Lejeune concluded in 1956 [10]: Mycenaean has the highest o in the table. But it does not place Minoan in Anatolia. Within that family the o runs from 0.0% in Lycian and Lycian B to 24.3% in Pisidian: it is a feature of individual languages and not of the branch. Sharing it with Lycian brings Minoan no closer to Anatolia than to Etruscan, which shares it and is not Anatolian.

## 6 bis.3 Reduplication points the other way

Lejeune's second observation [10] also holds. Minoan repeats adjacent syllables in 4.4% of its intact units against 2.3% in Mycenaean, p = 0.0038. Measured the same way across the Anatolian corpora: Lycian 6.3%, Minoan 4.8%, Lydian 1.2%, Carian 1.2%.

That is the exact reverse of the vowel profile. On vowels Lydian is nearest and Lycian furthest; on reduplication Lycian shares the feature and Lydian does not.

A third feature was attempted and does not calibrate: the profile of endings shared by three or more roots. Its null is not comparable across writing systems, since shuffling syllables and shuffling letters generate spurious endings at very different rates (Lycian returns 0.44 and Pisidian 2.87 on 165 words). It is declared unusable for comparison between scripts.

## 6 bis.4 What the disagreement means, and it is not local

One feature points to Lydian, another to Lycian, a third to nothing. That is not a defect of these particular measurements: structural and typological features are known to carry areal signal as readily as genealogical signal, which is why almost all quantitative phylogenetics in linguistics codes lexical cognates instead.

The problem has been measured directly. A study of July 2026 in *Entropy* [13] ran 29 structural features over 28 Transeurasian languages with a pipeline first calibrated on Indo-European. At the depth involved, the signal separated broad typological profiles but did not reconstruct internal relationships: Bayesian and distance-based inference returned near-complete polytomies, no branch reached a posterior probability above 0.75, and an unrelated Indo-European control language, included precisely for the purpose, was pulled into the family.

Our own data says it in one line. Etruscan sits at 0.111 from Minoan on the vowel profile and is the worst of the thirteen candidates under the anchored lexical search, at z = −3.2. A shared phonological profile is area or typology; it is not kinship.

## 6 bis.5 The shape of the whole

The two criteria available to this field fail in mirrored ways, and both failures are now measured.

By lexicon, there is too much evidence. Under the permissive phonology a CV syllabary imposes, 89.1% of Linear A units find a Semitic comparandum, Greek finds one 79.7% of the time, and fictitious grids reach 97.1%. Optimising for lexical fit finds grids 2.4 times better than the standard one, changing 37 of 38 free signs.

By typology, there is too little. Three features give three answers, and the discipline that formalised the method reports the same result on a family with a corpus orders of magnitude larger than ours.

What is missing in both cases is not evidence but a rule for weighing it, and the information count of §7 says why no such rule can be built from this corpus alone: specifying a decipherment costs 587 bits and the corpus supplies at most 236.


## 6 ter. Two further phonological facts, and a power analysis that licenses them

Two measurements complete the phonological profile, and both are reported with the power analysis that makes their negatives readable.

Minoan has no vowel harmony. Adjacent syllables share their vowel in 27.1% of 1,094 pairs against 27.8% expected when the syllables are shuffled (p = 0.74). Linear B, the same script writing Greek, does have it: 29.3% against 24.0%, p < 0.0001. And the negative is not a want of material: subsampled to the 1,094 pairs Linear A has, Linear B's harmony is detected in 30 of 30 subsamples. The absence is real.

Adjacent syllables in Minoan predict each other less than in Greek. The mutual information between the consonants of adjacent syllables exceeds its null by 0.081 in Linear A (p < 0.005) and by 0.226 in Linear B at the same corpus size (ten samples, range 0.195 to 0.274). The dependency exists in both and is about three times weaker in Minoan.

Taken with the o-series and reduplication, four phonological facts now describe the language without naming it: a vowel system poor in o and rich in a and u, reduplication at twice the Greek rate, no harmony, and weak dependency between adjacent syllables. None requires a candidate language, each has its control, and any future reading must satisfy all four.

One methodological caution belongs with them. An earlier version of the dependency measurement compared Minoan with eight candidate languages syllabified by us from their alphabetic forms. All eight returned identical vowel dependency of exactly zero, which is what a function that assigns vowels by construction will always produce. Only corpora syllabified by their own scribes — Linear A and Linear B — are comparable here, which is why the comparison above uses no others.

## 7. Why all of this happens: an information count

Specifying a decipherment means assigning a value to each free sign. The complete syllabary has 110 signs, sixteen anchored by the place names shared with Linear B, leaving 94 free. Assigning each a value from a grid of 74 costs 94 × log₂(74) = 584 bits, plus 3.3 bits for choosing the language among ten: 587 bits.

The corpus supplies less. A unit "working" is an event that occurs 73.8% of the time by chance, so it carries −log₂(0.738) = 0.438 bits. Over 552 intact syllabic units the theoretical maximum is 242 bits, and since each sign occurs in sixteen units on average the constraints are not independent; counting only the units that fix a previously unseen sign gives 236 bits.

Deficit: 351 bits. Of the order of 2³⁵¹ distinct assignments fit the corpus as well as any other.

That number is the explanation of the century described in §1. Proposals are serious enough; the difficulty is that with 351 bits of slack, any sufficiently worked hypothesis produces a coherent lexicon. Packard demonstrated in 1974 that nine fictitious decipherments could be built; this is the figure that explains why he could.

It also prices the only way out the field already knew. Each sign anchored from outside removes 6.2 bits. Closing the deficit would take some 57 anchored signs, and sixteen exist.

## 8. Discussion

The measurements above do not refute any particular reading of Linear A, and it would be the same error to claim they do as the error they document. A correct reading would also produce many matches; what fails is the inference from many matches to correctness.

What is established is narrower and firmer. The criterion by which these proposals are judged does not discriminate: fictitious grids match as well or better; optimisation prefers grids that keep none of the Linear B values; and requiring form and meaning together returns nothing across the three languages for which a glossed lexicon exists. Anyone advancing a decipherment of Linear A on lexical grounds is now obliged to place it on this scale.

Three things remain outside the reach of these instruments and should be said plainly. Whether Minoan belongs to a given family is decided by comparative morphology, which this work does not do. Whether the phonology of the script was permissive or strict is a hypothesis about the writing system on which 243 bits depend and which no measurement here settles. And what any unit means, as opposed to what it does, is not fixed by distribution at all.

## Data and reproducibility
Corpus, code, null models and the manifest of every figure at github.com/BiomeMakers/kuro. Glossed lexicons from ORACC (saao, rinap, dcclt) and from the Copenhagen Ugaritic Corpus (DT-UCPH/cuc, CACCHT project, doi 10.5281/zenodo.10695308, CC BY-NC 4.0).

## References

[1] Godart, L. and Olivier, J.-P. 1976-1985. *Recueil des inscriptions en linéaire A* (GORILA), 5 vols. Paris: Geuthner.

[2] Duhoux, Y. 1989. "Le linéaire A: problèmes de déchiffrement." In *Problems in Decipherment*, 59-119. Louvain-la-Neuve.

[3] Duhoux, Y. 2012. "¿La lengua del Lineal A es anatolia?" *Estudios Clásicos* 142: 7-32.

[4] Packard, D. W. 1974. *Minoan Linear A*. Berkeley: University of California Press.

[5] Finkelberg, M. 2001. "The language of Linear A: Greek, Semitic or Anatolian?" In *Greater Anatolia and the Indo-Hittite Language Family*, JIES Monograph 38, 81-105.

[6] Lejeune, M. 1956. "Observations sur le vocalisme du linéaire A." *Bulletin de la Société de Linguistique de Paris* 52: 40-57.

[7] Davis, B. E. 2014. *Minoan Stone Vessels with Linear A Inscriptions*. Aegaeum 36. Leuven and Liège: Peeters.

[8] Steele, P. M. and Meißner, T. 2017. "From Linear B to Linear A: the problem of the backward projection of sound values." In P. M. Steele (ed.), *Understanding Relations Between Scripts: The Aegean Writing Systems*, 93-110. Oxford: Oxbow.

[9] Meißner, T. and Steele, P. M. 2017. "Linear A and Linear B: structural and contextual concerns." In *Aegean Scripts*, Rome.

[10] Judson, A. P. 2017. "Processes of script adaptation and creation in Linear B: the evidence of the 'extra' signs." In P. M. Steele (ed.), *Understanding Relations Between Scripts*. Oxford: Oxbow.

[11] Salgarella, E. 2020. *Aegean Linear Scripts: Rethinking the Relationship Between Linear A and Linear B*. Cambridge: Cambridge University Press.

[12] Gordon, C. H. 1966. *Evidence for the Minoan Language*. Ventnor: Ventnor Publishers.

[13] Moorhouse, A. C. et al. Various proposals reviewed in Duhoux 1989 and in Younger's Linear A lexicon.

[14] Younger, J. G. 2024. *Linear A Texts in Phonetic Transcription*. Available at kansas.academia.edu/JYounger.

[15] Moran, S., McCloy, D. and Wright, R. (eds.) 2019. PHOIBLE 2.0. Jena: Max Planck Institute. And Marsico, E. et al. 2018, BDPROTO.

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
