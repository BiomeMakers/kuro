# How much template each part of the Linear A corpus has, and why only one genre has any

**Alberto Acedo**
Biome Makers Inc. Draft v0.1, 10 September 2026. Not for circulation.

## Abstract

Linear A documents are classified in several ways: by ideogram, by commodity combination, by
transaction type, by support. None of these classifications measures how rigid the format of each
group actually is, and the question has an answer that can be obtained without reading anything.
This note proposes a measure of format rigidity: hold out each document in turn, predict each of its
positions from the others, and record how much that prediction gains over always guessing the group's
commonest element. Applied to twelve groups of the corpus, the measure separates them sharply. The
libation formula gains 12.4 points over its base rate (22.4% against 10.0%, permutation null 6.6%,
p = 0.003); no other group reaches 3, seven of the eleven remaining gain nothing at all, and five
gain less than nothing — a constant guess beats prediction. Stone vessels, the only group besides the
formula with a positive gain worth naming, owe it to containing the formula: their hits are the same
fixed elements. The conclusion is that **Linear A has one genre with a rigid format, the votive, and
that its administration does not have one**: accounting tablets repeat a short repertoire of
commodities, but their order is not predictable beyond what that repetition already supplies. The
measure is calibrated on material where no template exists, and reports a false positive in 5.0% of
trials at the 5% threshold.

**Keywords:** Linear A, document classification, format, prediction, null models, Haghia Triada,
libation formula.

## 1. The question, and why it has not been asked

The Linear A corpus is classified in at least four ways. Bennett's system, inherited by Younger,
groups tablets by the ideogram they carry. Uchitel and Montecchi group them by combination of
commodities. Hogan groups them by transaction type. And every edition groups them by support: tablet,
roundel, nodule, stone vessel.

Each classification asserts, implicitly, that its groups are coherent. **None of them measures how
coherent**, and the reason is that coherence of content is easy to see and coherence of *format* is
not: whether a group's documents follow a shared order cannot be judged by inspection when the
documents are three elements long.

The question matters beyond bookkeeping. A group with a rigid format is a group whose documents were
written to a template, which is a fact about the administration that produced them; a group without
one is a group whose coherence lies elsewhere.

## 2. The measure

Each document is a sequence of elements. Align every document of a group on its first element, hold
out one document entirely, and predict each of its positions from the remaining documents: a
candidate is weighted by how often it occupies that relative position elsewhere, and by how many
other elements its source document shares with the one being reconstructed.

**Three things are reported, and the third is the measure.**

The **accuracy** is the share of held-out positions predicted correctly. The **base rate** is what
always guessing the group's commonest element achieves. And the **gain** is the difference. A
permutation null, shuffling elements within each document two thousand times, gives the accuracy
obtainable when order carries no information at all.

**The alignment position is excluded from scoring.** It must be: it is what the alignment uses, and
predicting it would be circular. In an early run of this measure on the libation formula, eleven of
seventeen apparent hits were that position alone.

**Why the gain and not the accuracy.** A group in which one element dominates yields a high accuracy
for a trivial reason, and the base rate absorbs exactly that. The gain isolates what position
contributes.

## 3. Result

| group | n | positions | accuracy | base rate | null | **gain** | p |
|---|---|---|---|---|---|---|---|
| **libation formula** | 16 | 49 | 22.4% | 10.0% | 6.6% | **+12.4** | 0.003 |
| stone vessels | 43 | 204 | 5.9% | 3.4% | 3.2% | +2.5 | 0.060 |
| class family A | 8 | 85 | 9.4% | 8.0% | 3.4% | +1.5 | 0.023 |
| tablets | 209 | 1,277 | 5.2% | 3.9% | 4.0% | +1.3 | 0.032 |
| tablets, Haghia Triada | 141 | 947 | 5.1% | 4.0% | 3.8% | +1.1 | 0.057 |
| class family U | 41 | 289 | 9.0% | 9.2% | 6.8% | −0.2 | 0.152 |
| class family E | 16 | 100 | 4.0% | 6.7% | 4.9% | −2.7 | 0.675 |
| tablets, Khania | 35 | 167 | 10.2% | 13.2% | 8.1% | −3.0 | 0.250 |
| class family V | 20 | 105 | 1.0% | 4.5% | 0.7% | −3.6 | 0.425 |
| tablets, Phaistos | 11 | 48 | 4.2% | 8.0% | 2.5% | −3.8 | 0.482 |
| class family B | 14 | 99 | 4.0% | 10.0% | 3.3% | −6.0 | 0.405 |
| tablets, Arkhalkhori | 8 | 35 | 5.7% | 12.8% | 2.2% | −7.1 | 0.162 |

**One group stands apart, and the distance is not marginal.** The libation formula gains 12.4 points;
the next gains 2.5. Five groups gain less than nothing.

## 4. What the result says

**The votive genre has a template and the administration does not.** This is the finding, and it is
worth stating in the form that can be attacked: in eleven groups of the corpus other than the
libation formula, knowing a position contributes at most 2.5 points over knowing which element is
commonest, and usually contributes nothing.

**Stone vessels are the apparent exception and are not one.** Their gain comes from containing the
formula: their correctly predicted elements are I-PI-NA-MA and SI-RU-TE, the same fixed elements that
drive the formula's own result. Remove the formula and the group joins the tablets.

**Negative gains are informative, not failures.** A group where prediction loses to a constant guess
is a group with a dominant element. The tablets of Khania have a base rate of 13.2% and those of
Arkhalkhori 12.8%, the two highest in the corpus. That is not template but dominance, and it is worth
distinguishing: a classification that groups documents by a shared ideogram will produce groups with
high base rates and no format, which is what class families B and V show.

**And this does not contradict the reported standard sequences.** Uchitel and Hogan describe
recurring orders of commodities, and a companion study finds one such order on four tablets of four.
Both are true. Subgroups with fixed order exist; the classification-level groups that contain them do
not share a template, and the signal of the subgroups dissolves in them. **The measure operates at the
level of the classification, and what it says is that the classifications do not capture format.**

## 5. Calibration and limits

**Calibration.** The instrument was run on groups of accounting documents drawn at random, where no
template exists to be found: it reports a false positive in 5.0% of 120 trials at the 5% threshold
and 0.83% at 1%. It behaves as it should.

**Limits, three.** The measure requires at least eight documents of three or more elements, which
excludes most classes of the fine classification. The alignment on the first element is crude, and a
group whose template begins at different points would be penalised by it; the formula was aligned
that way here for comparability and its gain is, if anything, understated. And **the p-values are not
corrected for the twelve comparisons**: at a Bonferroni threshold of 0.004 only the formula survives,
which is the conclusion in any case.

## 6. Discussion

The measure is not specific to Linear A. Any corpus of short documents with repeated elements can be
profiled this way, and the interesting quantity is the same everywhere: how much position contributes
over frequency. Applied to a corpus with known answers it should separate a formulaic genre from an
inventory genre, and here it does exactly that on the one Linear A group whose formulaic character is
not in dispute.

What it adds to the study of Linear A is a fact that four classifications had left unstated: **the
administration of Neopalatial Crete did not write its accounts to a form.** It repeated commodities,
it repeated transaction terms, and on some tablets it repeated an order; but the order is not a
property of any group large enough to be called a genre. The one place where the form is fixed is the
one place where nothing is being counted.

## Data

Linear A texts from the LinearA Explorer transcription of GORILA. Classification by Montecchi 2019.
The measure, its null and its calibration are implemented in the kuro package; the code and the
per-group figures are available with it.

## Declaration of assistance

The corpus processing, the tests and the drafting of this text were produced with the assistance of a
language model (Claude, Anthropic) under the direction of the author, who is responsible for all
claims made here.

## References

Bennett, E. L. 1950. Fractional quantities in Minoan bookkeeping. American Journal of Archaeology 54, 204-222.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A. Études Crétoises 21. Paris: Geuthner.

Hogan, R. 2026. Transaction types in the Linear A corpus. In E. Salgarella and V. Petrakis (eds), The Wor(l)ds of Linear A, AURA Supplement 15, Athens.

Montecchi, B. 2019. Contare, misurare e valutare nella Creta minoica. Rome: Quasar.

Schoep, I. 2002. The Administration of Neopalatial Crete. Suplementos a Minos 17. Salamanca.

Uchitel, A. 2002-2003. HT 94 and the standard sequences of Linear A. Minos 37-38.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos and N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Younger, J. G. 2024. Linear A Texts and Inscriptions in phonetic transcription and Commentary. Academia.edu.
