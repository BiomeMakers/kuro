# The Linear A libation formula: an Egyptian architecture, an offering term fixed by a logogram, and a 14% ceiling on prediction

**Alberto Acedo**
Biome Makers Inc. Draft v0.2, 9 September 2026. The segmentation of the opening is credited to Finkelberg 1990-91.

## Abstract

The votive inscriptions of Linear A share a formula that recurs at six Cretan sanctuaries over more than two centuries and remains unread. We propose three things about it, fixed by its distribution and not by a borrowed language: that its architecture is that of the Egyptian votive formula; that u-na-ka-na-si is the term for the offering; and that what can be predicted of a new vessel has a ceiling of 14% that belongs to the corpus. Over the eighteen non-accounting inscriptions preserving at least one anchor it establishes that the formula opens with a fixed word whose root is invariant and whose ending varies by sanctuary; that the fillers of the variable slots are hapax in 32 of 32 cases (probability 10⁻⁴), so that the slots hold the open class of names and the anchors the closed class; that the one inscription with logograms, SY Za 2, fixes u-na-ka-na-si as the term for the offering without etymology, since it is followed by the oil logogram. Compared as a structure with the contemporary votive formulae that are read, the Minoan template places its central invariant element between the names and the offering, as the Egyptian does. Two structural readings survive for the central anchor and two for the next; the datum that would separate them is absent from the corpus, and where it might appear is stated. A held-out test with baselines closes the paper: reconstructing each inscription's slots from the others recovers 8 of 57 elements (14.0%); an n-gram baseline does better at Top-1 (17.5%); both are bounded by the same fact, that the true filler is among the candidates in only 14.0% of slots. All converge near 23%, a ceiling of the corpus and not of any model.

**Keywords:** Linear A, libation formula, votive inscriptions, null models, textual restoration.

## 1. A text that repeats, and that nobody reads

Around 1600 BC, at six mountain and cave sanctuaries of Crete, one and the same statement was cut on stone vessels, libation tables and ladles. It is recognisable at a glance: it opens with a-ta-i-\*301-wa-ja, goes on with a word that changes from vessel to vessel, and continues with ja-sa-sa-ra-me, u-na-ka-na-si, i-pi-na-ma and si-ru-te, almost always in that order and almost always the same. It is the only text of Linear A that repeats, and therefore the only one with something like a visible grammar. A century after its identification (Evans; Duhoux 1992; Finkelberg 1990-91; Davis 2013, 2014; Karnava 2016; Petrakis and Steele 2025), nobody knows what it says.

What has been tried is to read it with a borrowed language. The most cited proposal equates ja-sa-sa-ra-me with Luwian *ishassaras*, "lady", and hence a deity; others read it from Semitic or from Greek. None of those readings can be compared with the others, because each starts from a different language and none says what observation in the corpus would refute it. For a century the formula has been the place where every hypothesis about Minoan is put to the test, and where none has been able to lose.

This paper asks the question the other way round: **not what the formula says in another language, but what it says by itself.** A text that repeats with slots fixes, by its distribution alone, what each position does: which is fixed and which open, which carries names, which carries the offering, which varies with the place. That can be established without reading a word, against a null that says how much of it chance would produce, and it can be compared with the votive formulae of the same period that are read. It can be taken further: a fixed template predicts, and one can measure how much of a new vessel it recovers from the others, and why not more.

Three things result. First, the Minoan formula has the **architecture of the Egyptian votive formula**, not that of the Semitic or the Greek: a central invariant element between the names and the offering, and a fixed formula before the dedicant. Second, **u-na-ka-na-si is the term for the offering**, fixed by a logogram and not by an etymology: on the one vessel that carries logograms it is followed by the sign for oil. Third, the template has a **prediction ceiling of 14%**, and that ceiling belongs not to the method but to the corpus: 72% of the fillers occur on no other vessel, and no procedure, ours or the reference n-gram, recovers what is not there.

With that, of the dozen readings in circulation two remain per position for the two central anchors, and one can say which inscription would be needed to decide between them: a datum that is not in the corpus, and that an excavator would recognise if it appeared. That is what this paper offers the field: not one more reading, but the exact shape of the one that is missing.

## 2. Data and method

Eighteen non-accounting inscriptions preserve at least one anchor: IO Za 2, 6, 9, 14, 15, 16 (Iouktas); KN Za 10 (Knossos); KO Za 1 (Kophinas); PK Za 11, 12, 27 (Palaikastro); PL Zf 1 (Platanos); PS Za 2 (Psychro); SY Za 2, 3 (Syme); TL Za 1 (Tylissos); VRY Za 1 (Vrysinas); AP Za 2 (Apodoulou). Corpus: GORILA (Godart and Olivier 1976-1985) in the form of the LinearA Explorer, with sign verification in SigLA.

A caveat about the real votive corpus. Classification by support induces error: of the 107 stone vessels of Linear A, 33 are accounting documents and only 15 carry the formula, and those 33 concentrate at Zakros, with up to twelve quantities on a single piece. **The votive corpus of Linear A is seventeen documents and not a hundred and seven**, and that is the limit of power for everything that follows (Acedo 2026c).

The measures are distributional: position of each anchor, hapax rate of the fillers, co-occurrence with logograms, and variation of the endings crossed with site. Nulls, where needed, are label permutation within strata.

## 3. The template, fixed by distribution

### 3.1 The opening is a root with a paradigm
The derived transliteration splits the sign \*301 as a separate unit, which conceals the opening anchor. A note on notation. The sign \*301 is left here without a phonetic value, following GORILA and the edition consulted. Part of the decipherment literature assigns it the value JO and therefore writes a-ta-i-jo-wa-ja where this paper reads a-ta-i-\*301-wa-ja. The difference is not one of reading the tablets but of assigning a value to a sign, and it affects equally all sixteen inscriptions in which the opening occurs. Nothing that follows depends on that assignment, since \*301 is constant across all variants and what is measured is the variation of the endings. Restored, **A occurs in sixteen inscriptions and always in first position**, with an invariant root (a-)ta-i-\*301 and six endings: -wa-ja (eleven times), -wa-e, -u-ja, -u-ti-nu, -ti and -de-ka.

The endings group by sanctuary: Syme five of five with -wa-ja; Iouktas three with -wa-ja and one with ta-na-i-\*301-u-ti-nu; Palaikastro one -wa-e and one -wa-ja; Apodoulou and Psychro with forms of their own. And they do not covary with the ending of the toponym that follows (-wa-ja occurs with -tu, -te, -a and -mi), so **the variation is one of local convention and not of grammatical agreement** (p from 0.011 to 0.16 once site is controlled).

This is the corpus's best candidate for an inflectional or derivational paradigm on a single root, and it is stated as such without proposing what distinguishes each ending. The internal structure of this opening was analysed by Finkelberg (1990-91), and priority belongs to her: she observes that while the beginning and the end of the formula vary, its middle, the sequence -i-\*301-, is stable, and concludes that it cannot be a single word but two semantic units, the first ending in -i, which she proposes to read as an element of nominal or verbal inflection. She further shows that the three endings are neither forms of one word (the element u/wa is absent from -ti, the element ti from -wa-ja) nor three distinct words, and describes them as conglomerates of elements. What is added here is the measurement of what the variation depends on: the endings group by sanctuary and do not covary with the ending of the toponym that follows, so that the variation is one of local convention and not of grammatical agreement.

### 3.2 The slots hold the open class
The slot preceding the central anchor has ten fillers at six sites, and holds toponyms identifiable through Linear B (ja-di-ki-tu and a-di-ki-te = Dikte; i-da-a and i-da-mi = Ida) sometimes followed by two further words. The following slots have fourteen fillers.

**All thirty-two fillers are hapax: they occur once in the whole corpus.** Under the corpus hapax rate (0.76), the probability of thirty-two consecutive hapax is of the order of 10⁻⁴. The conclusion is structural and depends on no reading: **the variable slots hold names and places, and the anchors the closed class.**

### 3.3 SY Za 2 fixes the term for the offering
A single inscription of the series carries logograms, and it decides one position. SY Za 2 writes "ja-su-ma-tu OLIV | u-na-ka-na-si OLE": anchor D is followed by the logogram for oil, and the word preceding it carries that for olives.

**That fixes D as the term for the offering, with no recourse to etymology.** It is, so far as I can tell, the only point of the formula whose function is established by internal evidence rather than by comparison with a candidate language. The observation about this inscription is due to Petrakis and Steele (2025); what is added here is its distributional consequence.

### 3.4 What ja-sa-sa-ra-me cannot be
The central anchor occurs thirteen times at six sanctuaries, with variants of prefix (ja-, a-, none) and of ending (-me, -ma, -ma-na), and **never carries a logogram or a quantity**. That absence, over thirteen occasions and with SY Za 2 demonstrating that the formula does admit logograms, rules out two possible functions: it does not designate the offering or the object. And its invariance across sanctuaries rules out two more: it is not the dedicant's name (which would be hapax) nor the sanctuary's (which would vary by site).

### 3.5 The resulting template
> **[A: fixed root + local ending] [place, and up to two names: hapax] [C: ja-sa-sa-ra-me, no logogram] [D: u-na-ka-na-si, admits a logogram of offering] [E: i-pi-na-ma] [F: si-ru-te] [name or second form of the opening: hapax, optional]**

With a variant Younger called "abbreviated", at Syme: opening, word with OLIV, D with OLE, and logograms in place of anchors E and F.

## 4. Separable morphology

Three elements separate by distribution and not by etymology.

**i-na-**: two root/prefixed pairs in the whole corpus, both in formula context and both on a place name: i-na-i-da against i-da (Ida), and i-na-ja-pa-qa against ja-pa-qa, these two at the same sanctuary (PK Za 11 and 12). A candidate for a marker of place, situated and not read. Younger discusses the prefix I- as a case marker; i-na- is a longer form with the same distribution.

**ja- / a-**: eleven pairs with a- in the whole corpus (a-ri-ja / ri-ja, a-ki-ro / ki-ro, a-mi-ta / mi-ta), and the alternation ja-sa-sa-ra-me / a-sa-sa-ra-me / sa-sa-ra-me. Its frequency is 7 per thousand at Haghia Triada against 140-240 per thousand at the sanctuaries: **it is a feature of genre, not of grammar**.

**u-ti-nu**: occurs only on IO Za 11, and as the ending of ta-na-i-\*301-u-ti-nu (IO Za 6) and of ta-na-ra-te-u-ti-nu (IO Za 2). The two Iouktas compounds share the frame ta-na-[X]-u-ti-nu. It is a separable element that the script joins to the preceding word without a divider, and it has a consequence for the template: **the tail filler of IO Za 2 is not a name but a second form of the opening**, so that at Iouktas the formula closes as it opens.

## 4 bis. What the template predicts, and what nothing can predict

Everything above describes the corpus. This section predicts material that was set aside, following
the evaluation practice of textual restoration (Sommerschield et al. 2023): a held-out test, several
baselines including the field's standard n-gram, and accuracy reported at several ranks rather than
at the first alone.

**Design.** The eighteen inscriptions in which the opening anchor can be located are indexed by
position relative to that anchor. For each slot, the whole inscription containing it is withheld and
the element is predicted from the seventeen others by what occupies that relative position, weighting
a candidate by how many other elements its source inscription shares with the one being reconstructed.
**The anchor position is excluded from scoring**, since it is what the alignment uses; an early run
that did not exclude it scored 20.2% and owed eleven of its seventeen hits to that position alone.

**Result, with baselines and at several ranks.**

| | Top-1 | Top-3 | Top-5 | Top-10 | Top-20 |
|---|---|---|---|---|---|
| this predictor | *\*14.0%** | 14.0% | 14.0% | 14.0% | 14.0% |
| n-gram baseline (predict from the preceding element) | *\*17.5%** | 19.3% | 21.1% | 22.8% | 22.8% |
| always guess the commonest element | 8.8% | 19.3% | 21.1% | 22.8% | 24.6% |

**Two things must be said plainly, and the second explains the first.**

**The n-gram baseline beats this predictor at Top-1**, 17.5% against 14.0%. The standard baseline of
the field is better than the method proposed here, and reporting otherwise would require omitting it.

**And this predictor's accuracy does not improve with rank at all**, which is not how a predictor
behaves unless it has run out of candidates. It has:

| | |
|---|---|
| slots evaluated | 57 |
| the true element is available among the candidates for that position | 8 (*\*14.0%**) |
| the true element occurs in **no other inscription of the formula** | 41 (*\*71.9%**) |

**The ceiling of this method is 14.0%, and its accuracy is 14.0%.** It recovers every slot the
structure allows it to recover. In the remaining 86% the true element is not available to be
proposed, and in nearly three quarters of cases because it is a hapax.

**That is the result, and it confirms section 3.2 from the other side.** The slots hold the open
class: all thirty-two of the formula's fillers are hapax. One cannot predict the filler because the
filler is new each time; one can predict the template because the template recurs. The eight hits are
JA-SA-SA-RA-ME, I-PI-NA-MA and SI-RU-TE, which are exactly the three elements section 3 identifies as
fixed by distribution. The same conclusion is reached twice by independent routes.

**And a figure worth stating for anyone who attempts this corpus with a stronger method.** All three
approaches converge near 23% as rank grows, which is approximately the share of slots occupied by
elements that occur more than once. **The ceiling is a property of the corpus, not of the models**: no
method that works by recognising repetition will exceed it, however sophisticated, because 72% of the
material to be recovered occurs exactly once.

**What would refute this.** New formula inscriptions raising the share of repeated fillers, which
would lift the ceiling and make the comparison between methods meaningful; or the hits ceasing to
concentrate on the fixed positions, which would sever the connection with section 3.

**Calibration.** The instrument was measured on accounting documents where no template exists: it
reports a false positive in 5.0% of 120 trials at the 5% threshold and 0.83% at 1%. The permutation
null for this test, shuffling elements within each inscription, gives 3.5%.

## 5. The two readings that survive, and the datum that would separate them

For each position the functions a votive formula can have there are enumerated, following the read formulae of Egypt, Anatolia, Ugarit and Greece, and those contradicting some measured datum are discarded.

### 5.1 The central anchor (C)

| hypothesis | predicts | does it hold? |
|---|---|---|
| **C1: name or title of the receiving deity** | invariant across sites; no logogram; after the names and before the offering | **yes throughout** |
| **C2: verb of dedicating** | invariant; after the dedicant; might take an object after it | **compatible**, but then D would be the object and C-D would be verb plus object |
| C3: word for offering or object | should admit a logogram at some point | no: 0 of 13. Discarded |
| C4: dedicant's name | should be hapax | no: 13 near-identical occurrences. Discarded |
| C5: sanctuary's name | should vary by site | no: the same form at five sanctuaries. Discarded |

**The datum that would separate C1 from C2**: if C ever appeared without D and with a logogram of offering after it, it would be a verb with an object; if it appeared in a non-votive text with a name before it and nothing after, it would be the deity. **Neither occurs in the present corpus.** The place where it might is the Knossos sceptre, a ritual text without numerals.

### 5.2 The offering anchor (D)

| hypothesis | predicts | does it hold? |
|---|---|---|
| **D1: term for the offering** | admits a logogram; follows the deity | **yes**: OLE on SY Za 2; always after C |
| **D2: verb of giving or offering** | follows the recipient in the Egyptian and Anatolian formulae; may take an object | **yes as well** |
| D3: dedicant's title | should vary or be hapax | no: 9 near-identical at 5 sites. Discarded |
| D4: case marker or postposition | would not take a logogram of its own | no: OLE follows it. Discarded |

D1 and D2 are not exclusive: a verb "to libate" and a noun "libation" share a root in many languages. The alternation -si / -ti / -ja-si, if it is morphology, favours D2; if it is local orthography, it decides nothing.

### 5.3 The closings (E and F)
Both are invariable, come last and occur at six sanctuaries. Neither ever carries a logogram, which rules out their being a second object of offering; their invariance rules out their being names. Two functions remain compatible and not separable with this corpus: a fixed closing formula, or an adverb of time or place. One datum is informative: **F can occur without either C or D** (VRY Za 1, IO Za 15), so the closing depends neither on the deity nor on the offering, but on the inscription itself.

## 6. The template compared, as a structure

Comparing the Minoan template with the contemporary votive formulae that are read yields no reading, but it orders the space of possibilities.

| tradition | structure | does it match? |
|---|---|---|
| Egyptian (*ḥtp-dí-nsw*) | [fixed formula] [deity] [offerings] [beneficiary last] | **yes** in the fixed opening preceding the dedicant and in the deity before the offering; differs in that place and names precede the deity in Minoan |
| Anatolian (Hittite, Hieroglyphic Luwian) | [dedicant and title] [object] [verb] [deity in the dative], or [deity] [dedicant] [verb] | **yes** in the order names → C → D, if C is the deity |
| Semitic (Ugaritic, Phoenician) | [dedicant] [verb] [object] [to the deity] | **no**: deity last |
| later Greek | [dedicant] [verb] [deity in the dative] | **no**: deity last |

**The Minoan template resembles the Egyptian and the Anatolian and not the Semitic or the Greek**, and cannot be decided between the first two on eighteen fragments. The fixed opening preceding the dedicant favours the Egyptian, since only that tradition opens so; the order dedicant → deity → offering favours the Anatolian.

That result has a consequence for the most cited proposal. Reading a-sa-sa-ra-me as Luwian *ishassaras*, "lady", **gains a condition** if the Anatolian template is preferred and **loses one** if the Egyptian is. With this corpus it cannot be decided, and it should be presented that way.

## 7. Discussion

What is established. The formula has a template of seven positions whose function is fixed by distribution in five of them; its slots hold the open class with a probability of error of the order of 10⁻⁴; its opening is a root with a paradigm whose variation is local and not grammatical; three morphological elements separate by distribution; and one position, that of the offering, is fixed by internal evidence of the corpus itself.

What is not established, and will not be with this corpus. The value of any of the four anchors. The possible functions of each have been enumerated, those contradicting some datum discarded, and two remain per position in the two central cases. The datum that would separate each pair is specified and does not exist: new inscriptions are needed, and which ones would serve is stated.

What this contributes to the debate on the language. Nothing directly, and that should be said. The comparison of templates is one of structure and not of words, so it favours no linguistic affiliation: a community can adopt the ritual structure of its neighbours while speaking another language, as indeed happens throughout the ancient Mediterranean. What it does provide is a criterion for ordering the existing proposals: **a reading proposal that requires a Semitic or Greek template has the structure measured here against it, and one requiring the Anatolian or Egyptian does not have that problem.** The criterion decides nothing, but it allows discarding.

And what it contributes to method. In a corpus without a bilingual, the function of each position of a formula is measurable and the number of possible readings is boundable. What is not measurable is the value of the words. The distinction between the two is what this paper wants to establish, because a century of proposals has treated both as if they were one task.

## Data

GORILA (Godart and Olivier 1976-1985) in the form of the LinearA Explorer (Hogan 2022), with sign verification in SigLA (Salgarella and Castellan 2020). The content-based classification of the 1,719 documents, which separates the real votive corpus from the apparent one, accompanies this work. Scripts: the kuro package (Acedo 2026d).

## Declaration of assistance

Corpus processing, the distributional tests and the first draft of this text were produced with the assistance of a language model (Claude, Anthropic) under the author's direction, who is responsible for all claims.

## References

Acedo, A. 2026c. What can be claimed about a corpus of seven thousand signs. Draft.

Acedo, A. 2026d. kuro: null models, calibration and confounder tests for small epigraphic corpora. Software.

Davis, B. 2013. Syntax in Linear A: the word-order of the "libation formula". Kadmos 52, 35-52.

Davis, B. 2014. Minoan Stone Vessels with Linear A Inscriptions. Aegaeum 36. Leuven and Liège.

Duhoux, Y. 1992. Variations, formules et texte dans les inscriptions votives en linéaire A. Cretan Studies 3, 65-88.

Finkelberg, M. 1990-91. Minoan inscriptions on libation vessels. Minos 25-26, 43-85.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A, I-V. Paris.

Hogan, R. 2022. Linear A Explorer. https://lineara.xyz

Karnava, A. 2016. On sacred vocabulary and religious dedications: the Linear A "libation formula". In E. Alram-Stern et al. (eds), Metaphysis (Aegaeum 39), Leuven and Liège, 345-355.

Petrakis, V. and P. Steele 2025. A-SA-SA(-RA-ME) 1. In E. Salgarella and V. Petrakis (eds), The Wor(l)ds of Linear A, AURA Supplement 15, Athens.

Salgarella, E. and S. Castellan 2020. SigLA: the Signs of Linear A. https://sigla.phis.me

Valério, M. 2007. "Diktaian Master": a Minoan predecessor of Diktaian Zeus in Linear A? Kadmos 46, 3-14.

Sommerschield, T., Y. Assael, J. Pavlopoulos, V. Stefanak, A. Senior, C. Dyer, J. Bodel, J. Prag, I. Androutsopoulos y N. de Freitas 2023. Machine Learning for Ancient Languages: A Survey. Computational Linguistics 49, 1-44.

Younger, J. G. 2024. Linear A texts and inscriptions in phonetic transcription. http://people.ku.edu/~jyounger/LinearA/
