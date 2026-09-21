# How much information a script carries about its own decipherment

**Alberto Acedo**
Biome Makers Inc. Version 1.0, 13 September 2026. Not for circulation.

## Summary

Whether an undeciphered script can be read is argued qualitatively. It need not be. A decipherment is an assignment of phonetic values to signs; the cost of specifying one follows from the size of the sign inventory; and what the corpus can supply toward that cost follows from how often a candidate reading succeeds by chance. The difference is a deficit in bits, and it is a property of the corpus rather than of the method or of the investigator. This paper states the count, calibrates it on three scripts whose answer is known, applies it to three that are open, and prices what each of the open ones would need. Linear B before 1952, Iberian and Etruscan come out decipherable; **Linear A shows a deficit of 345 bits**, which converts into two currencies a field can act on: either 56 further signs anchored from outside, or some 788 further intact units of text. For the other undeciphered scripts three of the four inputs are published and the fourth, the match rate, has never been measured for any of them; the paper sets out what measuring it would require rather than supplying it from judgement. The estimate is deliberately generous to the corpus, so a script that shows a deficit under these assumptions shows one under any.

**Keywords:** undeciphered scripts, decipherment, information theory, Linear A, Cypro-Minoan, proto-Elamite.

## 1. The question nobody puts as a number

The million-dollar prize offered for the Indus script in 2025 has a premise: that the corpus contains the answer and what is missing is ingenuity. For some scripts that premise is true and for others it is not, and the distinction is not a matter of opinion. It can be computed from four quantities that any corpus can report about itself.

The field does argue the point, but in words. Whether Linear A is readable, whether the Indus texts are language at all [9], whether proto-Elamite will ever yield: the arguments turn on the size of the corpus and the absence of a bilingual, and they are correct as far as they go. What they do not do is say how much is missing, which is what a field needs in order to know whether to keep computing or to start digging.

## 2. The count

A decipherment assigns a value to each sign that is not already fixed. Its cost in bits is

> **cost = free signs × log₂(possible values) + log₂(candidate languages)**

What the corpus supplies is the improbability of its units coming out as words. If a unit matches something in a candidate lexicon a fraction *m* of the time by chance, each successful match carries −log₂(*m*) bits, so

> **supply = independent units × −log₂(match rate)**

and

> **deficit = cost − supply.**

Each sign fixed from outside — by a bilingual, by a shared place name, by a loanword whose source is known — removes **log₂(possible values)** bits, which prices the deficit in a currency a field can act on.

**Three assumptions, all generous to the corpus.** Every unit is counted as independent evidence, when in fact units share signs and their constraints are redundant. A match is counted as success when a real decipherment also requires the match to be contextually and morphologically right. And the candidate language is counted as one choice among a handful, when in practice it is an open set. A corpus that shows a deficit under these assumptions shows one under any.

## 3. Calibration: three scripts with a known answer

| script | signs | free | cost | supply | deficit | verdict |
|---|---|---|---|---|---|---|
| **Linear B (as of 1952) [1]** | 87 | 75 | 485 | 9,966 | **−9,481** | decipherable |
| **Iberian** | 28 | 5 | 26 | 5,048 | **−5,021** | decipherable |
| **Etruscan** | 26 | 0 | 3 | 6,110 | **−6,107** | decipherable |

All three are read, and all three come out decipherable with room to spare. The reasons differ and the count shows which is which. **Linear B** had a large corpus — three thousand units — and a strict match rate, since Greek either fits a sign group or does not; the twelve signs Ventris had from Cretan place names were enough because the supply was enormous. **Iberian** has few signs and almost all of them anchored by the Ascoli bronze [2]. **Etruscan** has an alphabet borrowed from Greek, so the values were never in question and the cost is near zero, which is precisely why Etruscan is read and not understood: the count measures the cost of the values, not of the meanings.

## 4. Three scripts that are open

| script | signs | free | cost | supply | deficit | anchors needed |
|---|---|---|---|---|---|---|
| **Linear A** | 110 | 94 | 587 | 242 | **345** | 56 |

**Only Linear A is reported, and the reason matters.** Its four quantities are measured: 110 signs and 94 free from the sign list, 552 intact units from the corpus, and a match rate of 0.738 measured directly against the candidate lexicons. For every other undeciphered script, three of the four are published — the sign inventory, the corpus size and the count of externally anchored signs — but **the match rate has never been measured for any of them**, because no one has run the test. Supplying it from judgement would make the table a report on the author's estimates rather than on the corpora, and the estimates move the verdict.

**Linear A** is the near case: 56 anchored signs would close it, against the 16 it has. Its supply is small because its corpus is small and because a CV syllabary matches a candidate lexicon 74% of the time by chance, which is nearly free.

**Cypro-Minoan** [4] is worse than Linear A despite being the nearest relative in script and period: 183 usable units supply 59 bits against a cost of 504. Any project proposing to read Cypro-Minoan by internal method is working with an eighth of the information Linear A has.

**proto-Elamite** [5] is not close to anything. With 1,900 signs, the cost of specifying an assignment is twenty thousand bits, and no corpus of the size that survives could supply it. The count says plainly what the field has concluded by experience.

## 5. What the deficit buys, stated in two currencies

The same figure converts into either of the two things that could be found.

| script | signs to anchor from outside | or further intact units of text |
|---|---|---|
| Linear A | 56 | 788 |

For Linear A the two numbers are the choice the field faces. Fifty-six anchored signs means a bilingual; 788 further units means roughly doubling the corpus, which means excavation. Neither is a computation, and that is the point: **the count says that no amount of method closes the gap, and what would.**

## 6. The case that would test this, and it has an answer

Linear Elamite was deciphered in 2022 by Desset and colleagues [6], after a century in which the field considered it out of reach. Its published quantities make it the natural test, because they run against the intuition the count is accused of merely restating. **It has less material than Linear A, not more**: 77 hypothesised signs against 110, and a corpus that stood at 25 inscriptions and 1,731 readable signs in the OCLEI supplement of 2020 [7], against the 7,147 of Linear A.

If the count measures corpus size, Linear Elamite should be further from decipherment than Linear A and it is not. What changed was not the quantity of text but three of the four inputs: the script is a closed alphasyllabary of five vowels, twelve consonants and sixty syllabic values with no logograms, so the space of assignments is smaller; the language was known, attested in cuneiform across two millennia, so the term for the choice of language vanishes; and the silver vessels from Kam-Firuz published in the 2000s supplied royal and divine names — Šilhaha, Eparti II, Napiriša — which is anchoring from outside in the strict sense.

**The test is worth running and is not run here.** Three of the four quantities are published; the fourth, the match rate, would have to be measured on the corpus, which is available through OCLEI and through the Hatamti database at Liège [8]. If the count returns a deficit for the corpus as it stood before the vessels and no deficit for the corpus after them, it will have reproduced a decipherment the field took a century to reach, and the timing of it. If it does not, the count is wrong and should be abandoned.

## 7. What the count does not do

It does not say a script is undecipherable. It says the corpus does not contain enough information to distinguish the right assignment from the many wrong ones [3], which is a different claim and a weaker one: an assignment may be correct and unprovable. It does not price the step from a phonetic value to a meaning, which is separate and which Etruscan shows to be the harder one. And its inputs are estimates: the match rate in particular depends on the target lexicon and on how permissive the phonology is assumed to be, and should be reported with the assumption that produced it.

It also inherits a limit from its own generosity. Because it counts every unit as independent when units share signs, the supply figure is an upper bound and the deficit a lower one. For Linear A the honest statement is *at least* 345 bits.

## 8. Why this is worth having

A field that cannot say how much is missing cannot tell a hard problem from an impossible one, and cannot tell whether the next decade should be spent on method or on excavation. The count is crude, its inputs are four numbers, and it can be computed for any undeciphered script in an afternoon. Its value is not precision but direction: it converts "we do not know whether this can be read" into a figure, a currency and a target.

For Linear A the direction is unambiguous and the distance is 56 anchored signs. Whether the other undeciphered scripts are at a comparable distance or two orders of magnitude away is exactly what nobody knows, and what four measurable numbers per script would settle.

## Data and reproducibility
The module and its tests are in the accompanying repository. The Linear A figures are measured in the companion papers; the figures for the calibration scripts are drawn from their standard editions and are stated as estimates.

## References

[1] Godart, L. and Olivier, J.-P. 1976-1985. *Recueil des inscriptions en linéaire A* (GORILA), 5 vols. Paris: Geuthner.
[2] Untermann, J. 1990. *Monumenta Linguarum Hispanicarum III: Die iberischen Inschriften aus Spanien*. Wiesbaden: Reichert.
[3] Shannon, C. E. 1948. "A mathematical theory of communication." *Bell System Technical Journal* 27: 379-423, 623-656.
[4] Ventris, M. and Chadwick, J. 1953. "Evidence for Greek dialect in the Mycenaean archives." *Journal of Hellenic Studies* 73: 84-103.
[5] Chadwick, J. 1958. *The Decipherment of Linear B*. Cambridge: Cambridge University Press.
[6] Rix, H. 1991. *Etruskische Texte: Editio minor*. Tübingen: Narr.
[7] Desset, F. 2020. "Nine Linear Elamite texts inscribed on silver 'gunagi' vessels." *Iran* 60: 1-29. With the OCLEI supplement.
[8] Desset, F., Tabibzadeh, K., Kervran, M., Basello, G. P. and Marchesi, G. 2022. "The decipherment of Linear Elamite writing." *Zeitschrift für Assyriologie* 112 (1): 11-60. Hatamti database, University of Liège.
[9] Farmer, S., Sproat, R. and Witzel, M. 2004. "The collapse of the Indus-script thesis: the myth of a literate Harappan civilization." *Electronic Journal of Vedic Studies* 11 (2): 19-57.
[10] Dahl, J. L. 2019. *Tablettes et fragments proto-élamites*. Paris: Éditions Khéops.

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
