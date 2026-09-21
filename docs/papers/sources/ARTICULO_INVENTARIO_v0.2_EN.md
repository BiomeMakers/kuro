# The functional inventory of Linear A: fifty-six units with a function fixed by distribution, and what the corpus cannot fix

**Alberto Acedo**
Biome Makers Inc. Draft v0.2, 11 September 2026. Not for circulation.

## Abstract

A century of proposed readings of Linear A has not produced an inventory that says, unit by unit, what is known, on what evidence, and what observation would refute it. This paper builds one for the 156 units of the corpus with three or more intact attestations. Each reading is fixed by the unit's distribution in the corpus (position, figures and fractions, company, site and seal) against a permutation null with a measured error rate, and is filed with the evidence for, the evidence against, and a refutation condition. The result is 56 units with a function: four arithmetic terms, eight headings and transaction terms, sixteen signs of commodities, livestock and persons, sixteen qualifiers and grades, eight place and personal names shared with Linear B, and four isolated functions. Fourteen have no prior source; the other 42 have prior art and carry a measurement here for the first time. None is a word with lexical meaning: the logograms are pictures, and the syllabic sign-groups have a function, not a translation. The inventory also brings three facts about the corpus that the editions do not state: 276 of the 783 syllabic units are broken in every attestation (35%), which invalidates part of the published morphological alternations; the 801 sealed nodules of Haghia Triada form two seal circuits that share no signs, and the sign does not identify the sealer; and the archive records no metal, honey or fish, all present in the material culture. The ceiling is declared: with this corpus, the internal method fixes functions and not words, and the number moves not with more runs but with new data.

**Keywords:** Linear A, Haghia Triada, inventory, null models, logograms, qualifiers, nodules, error rate.

## 1. Why an inventory and not one more reading

Whoever looks in Linear A for what is known about a particular unit finds Younger's lexicon, which collects almost everything and does not distinguish the measured from the conjectured, and a bibliography of proposals that seldom states what datum would refute them. What does not exist is a table with three columns: what is claimed, what supports it, what would bring it down. This paper is that table, built with one procedure and published with its code.

The procedure does not read. It fixes what a unit **does** in the account from how the scribe treats it: whether it opens the document, whether it carries a figure, whether that figure admits fractions, whether it follows a commodity with a smaller figure, whether a syllable is added to it or it is the added syllable, which other units share its document, and on nodules, which seal. Each of those observations has a null that preserves what the claim does not explain, and each instrument has an error rate measured on material where it should find nothing.

## 2. The corpus, and what the editions do not say about it

The corpus is GORILA through the LinearA Explorer: 1,720 documents and 1,007 distinct units, of which 156 have three or more attestations and at least one intact. That is the ceiling of the inventory: below three attestations there is no profile to measure.

**The broken units.** The `words` field of the edition keeps the break sign and the transliteration drops it. Recovered, 276 of the 783 syllabic units (35%) are broken in every attestation: ]MA-TE-RE is not MA-TE-RE. Three of the eight lexical coincidences with Linear B of a first comparison were fragments, and of Davis's stem/ending pairs, five of eight endings fall below three stems when only intact units count (-JA, -ME and -TI remain). The whole inventory is computed on intact units.

**The nodules.** Younger's commentaries give, for 801 nodules of Haghia Triada, the inscribed sign and the seal (CMS II,6 number and motif). Sign and seal are associated (mutual information 0.88 against 0.19 in 500 permutations), but not one to one: the seals form two blocks that share no signs (AT 13, 99, 45, 9, 17, 38 only with *301 and ZE; AT 125, 105, 19, 95, 79 with KU, KA, SI, RO, I and TA and never *301), and within a block one seal uses six signs. The sign does not identify the sealer; it identifies what is sealed. AT 19 uses KU on 42 of 44 nodules: one official for one type. What is missing to read those signs is the nodule type per document (Hallager 1996, vol. II), which is not in any open source.

**The gaps.** The material culture of Haghia Triada has copper ingots, honey and fish. No sign with a figure has the profile of those things (low whole numbers or weight for metal, liquid fractions for honey), *118 is the weight unit and accompanies cyperus and sesame, and Younger's lexicon does not mention them. The tablet archive does not record them.

## 3. The instruments and their error rates

Twelve instruments, each with its null and its measured rate (data/derived/error_rates.json). Those that support the inventory:

| instrument | what it measures | null | error rate at 0.05 |
|---|---|---|---|
| quantity profile | fraction rate of a logogram's figures against the base (27%), in the direction the class predicts; size of the figures | fractions at the base rate | 4.6% (worst case, direction chosen a posteriori) |
| heading | first position on a tablet against the base (11.8%) | binomial | positional: 3-5% |
| sub-count | figure smaller than the preceding commodity's against the base (52%) | binomial | (within positional) |
| qualifier | a syllable added to two or more distinct commodity signs | a rule, not a test | — |
| stratified co-occurrence | two units in the same document, preserving site and margins | bipartite by site | 5.5% |
| adjacency | two units contiguous, over eligible pairs | permutation | 2.5% |
| name matching | exact coincidence with the Linear B lexicon by length | syllable bigrams of the corpus itself | (by length; 2 syllables = chance) |
| arithmetic | the figure after the unit equals the sum of those before | permutation | 2.5% |

An instrument is calibrated on the material it is applied to: the profile rate was measured by shuffling the fractions of already-read logograms at the base rate; the co-occurrence rate, on words and logograms of the corpus itself (8.0% unstratified, 5.5% stratified by site: the site was the confounder).

## 4. The inventory

Fifty-six units: 25 established (field consensus confirmed by our test), 27 proposed (our test without prior consensus, or prior art without a test of its own until now), 4 disputed (a source against). Status, attestations, reading, prior source for, and number of pieces of evidence against:

| unit | status | attest. | reading | prior source | against |
|---|---|---|---|---|---|
| **Arithmetic** | | | | | |
| KU-RO | established | 37 | total | Godart & Olivier / field consensus, Scho |  |
| KI-RO | established | 16 | deficit | Schoep, Uchitel |  |
| DA-I | proposed | 2 | a total, of a kind distinct from KU-RO | — |  |
| PO-TO-KU-RO | established | 2 | grand total | Schoep |  |
| **Qualifiers and grades** | | | | | |
| KU | established | 170 | as an added syllable, a qualifier of four commodities (GRA+KU, TELA+KU, *188+KU, | — |  |
| KA | proposed | 169 | as an added syllable, a qualifier of wine and of persons (VIN+KA, VIR+KA); alone | — |  |
| OLE+MI | proposed | 19 | a grade of oil; listed together with OLE+DI in every document where it carries a | Younger | 1 |
| KI | established | 19 | as an added syllable, a qualifier of oil and *316 (OLE+KI, *316+KI) and of wool  | Del Freo, via Nosch and Weilhartner |  |
| CYP+D | proposed | 19 | a grade of cyperus recorded in the smallest amounts (fractions in 13 of 16, maxi | — |  |
| PA | proposed | 16 | qualifier (a grade or type) shared by grain, cyperus and *304: GRA+PA, CYP+PA, * | — |  |
| OLE+DI | proposed | 12 | a grade of oil; listed together with OLE+MI in every document where it carries a | Younger | 1 |
| TU | established | 11 | qualifier (a grade or type) restricted to the olive family: OLE+TU and OLIV+TU | Younger |  |
| RA | proposed | 9 | as an added syllable, a qualifier of oil and wine (OLE+RA, VIN+RA) | — |  |
| OLE+TA | proposed | 8 | a grade of oil recorded in small fractional amounts | Younger |  |
| GRA+KU | proposed | 7 | GRA with the qualifier KU (a grade or type) | — |  |
| VIN+RA | proposed | 4 | wine with the qualifier RA (a grade or type), parallel to OLE+RA | — |  |
| MA-RU-ME | proposed | 3 | wool with the qualifier ME (a type or grade) | Del Freo, via Nosch and Weilhartner |  |
| *188+KU | proposed | 2 | *188 with the qualifier KU (a grade or type) | — |  |
| KI-MA-RU | proposed | 1 | wool with the qualifier KI | Del Freo, via Nosch and Weilhartner |  |
| TELA+KU | proposed | 1 | TELA with the qualifier KU (a grade or type) | — |  |
| **Headings and transaction** | | | | | |
| TE | established | 58 | transaction term set between a party and the commodity ("X 𐄁 TE 𐄁 VIN"); also th | Schoep, Younger |  |
| SA-RA₂ | disputed | 20 | transaction term, Haghia Triada only; possibly the ethnic of the site | Schoep, Uchitel | 1 |
| A-DU | established | 10 | heading term (record label) of HT tablets; heads the lists of HT 86 and HT 95 am | Younger |  |
| KA-PA | established | 6 | heading term of HT tablets (HT only); KA-PA-QE is its extended form (Salgarella  | Salgarella |  |
| JE-DI | proposed | 4 | heading term (first position in 3 of 4 tablet attestations) | — |  |
| A-KA-RU | established | 3 | heading term of HT tablets (HT 2.1, HT 86a.1, HT 86b.1 as second heading) | Younger |  |
| DA-QE-RA | proposed | 3 | heading term of HT tablets (HT 6a.6 as a second heading, HT 120.1) | Younger |  |
| KI-RI-TA₂ | proposed | 2 | heading term (first position in both attestations) | — |  |
| **Commodities, livestock and persons** | | | | | |
| NI | established | 76 | figs (the logogram NI; ni- as the first syllable of the Minoan word) | Neumann; Salgarella and Petrakis (eds.), |  |
| GRA | established | 62 | grain (cereal), the bulk dry commodity | Ventris and Chadwick |  |
| VIN | established | 53 | wine, a liquid commodity | Ventris and Chadwick |  |
| CYP | established | 52 | cyperus (*303), a fine commodity measured in small fractional amounts | Ventris and Chadwick |  |
| OLIV | established | 24 | olives, the fruit as distinct from its oil | Ventris and Chadwick |  |
| OLE+U | proposed | 22 | a type of oil counted in whole units (or a counted unit of oil: whole numbers, s | — | 1 |
| OLE | established | 22 | olive oil, a liquid commodity | Ventris and Chadwick |  |
| *22F | established | 14 | goat, female; Linear B CAPf | GORILA / Ventris and Chadwick |  |
| *308 | proposed | 12 | fatty product derived from the olive | Koh & Birney, Younger |  |
| *305 | proposed | 12 | a category of persons | Younger |  |
| *21M | established | 8 | sheep, male (ram); Linear B OVISm | GORILA / Ventris and Chadwick |  |
| *23M | established | 7 | ox/bull; Linear B BOSm | GORILA / Ventris and Chadwick |  |
| *21F | established | 4 | sheep, female (ewe); Linear B OVISf | GORILA / Ventris and Chadwick |  |
| *131B | proposed | 4 | a variant of the wine sign (AB 131b), a type of wine | GORILA |  |
| *22M | established | 3 | goat, male; Linear B CAPm | GORILA / Ventris and Chadwick |  |
| VIR | established | 0 | person (man), the unit counted in personnel lists | Ventris and Chadwick |  |
| **Other functions** | | | | | |
| JA-SA-SA-RA-ME | proposed | 7 | does not designate the offering or the object | — |  |
| *306 | disputed | 7 | possibly the sign for woman | Uchitel | 2 |
| KU-NI-SU | disputed | 5 | first name in a list; the Semitic reading as emmer is proposed and contested | Younger, various, cited by Younger | 1 |
| SU-KI-RI-TE-I-JA | proposed | 1 | formed on the stem of Sybrita, or sharing its lexicon | Davis |  |
| **Place and personal names** | | | | | |
| KI-DA-RO | proposed | 2 | a personal name shared with the Linear B tablets of Knossos (Godart 1984) | Godart |  |
| PA-I-TO | established | 2 | Phaistos, the place name (Linear B pa-i-to) | Godart |  |
| DA-I-PI-TA | proposed | 2 | a personal name shared with the Linear B tablets of Knossos (Godart 1984) | Godart |  |
| I-TA-JA | proposed | 1 | a personal name shared with the Linear B tablets of Knossos (Godart 1984) | Godart |  |
| DA-MA-TE | disputed | 1 | coincides with Linear B da-ma-te; read as Demeter by some, contested | Owens | 2 |
| SU-KI-RI-TA | established | 1 | Sybrita, the place name (Linear B su-ki-ri-ta) | Godart |  |
| I-JA-TE | proposed | 1 | coincides with Linear B i-ja-te (PY Eq 146); Younger: "of/from I-JA" | Godart, Younger |  |
| SE-TO-I-JA | established | 1 | Setoia, the place name (Linear B se-to-i-ja; Archanes or Iouktas?) | Godart |  |

Four things are visible in the whole table.

**Fourteen with no prior source.** DA-I as a total of another kind; KI-RI-TA₂ and JE-DI as headings; VIN+RA parallel to OLE+RA; KU as a qualifier of four commodities and PA of three; KA of wine and of persons; CYP+D as cyperus in the smallest amounts; OLE+TA as fine oil; OLE+DI and OLE+MI as paired grades; JA-SA-SA-RA-ME as what it is not. They are functions, and several are the same finding seen in several units (KU in four ligatures).

**Forty-two with prior art, where the measurement is what is new.** VIR in whole numbers only (2 of 36 fractional, p = 0.0008); GRA in large whole numbers (12 of 90, maximum 976); CYP almost always in fractions and in small amounts (39 of 64, maximum 23); TE in the pattern separator-TE-separator-commodity in 10 of 24 against 2.5% (p = 10⁻¹⁰); the sex-marked livestock in whole numbers (2 of 28, p = 0.007) with PH 31 as a list by species and sex; A-DU in first position in 7 of 10 (p < 0.0001). And in the other direction: six of Younger's "headings" with zero first positions, KU-NI-SU as emmer disputed, and "*304 always between OLE and OLIV" false as stated (6 of 25).

**No word.** All 56 are function: what the unit does in the account. For the 16 signs of commodities, livestock and persons, the reading comes from pictographic identity with Linear B (OLE is oil because the sign is the same and in Linear B it is fixed by Greek context), and our test says the administration counted them as that kind of thing is counted. No syllabic group has a translation: KU-RO is "total" because it adds up, not because we know how "total" was said in Minoan.

**What was tested and not fixed.** List entries (the most numerous class) are judged only by exclusion: no fractions of their own, no added syllable, not a heading, not a total; and that exclusion leaves a personal name and a commodity written in syllables indistinguishable. Without an external source there is no positive judge, and the category "list entry" does not count as a reading. The nodule signs (*301, KU, KA, SI, RO, ZE) have their structure fixed (the two circuits) and not their reading. The five borderline units of two runs (VIR+[?], QA2+[?]+PU, SA-RU, A-SE, JE-DI in part) are not filed: bare p between 0.01 and 0.04 with 50-80 tests is what chance produces.

## 4 bis. The scope of the inventory: which archive fixed each function

The 56 entries were not fixed on "Linear A" but on the archives with enough material, which is almost always Haghia Triada (64% of the corpus). The distinction is not formal. The second archive, Khania (227 documents, 105 tablets), **uses no summation term on any of its tablets**, against 41 of 205 at Haghia Triada: under the Haghia Triada rate, the probability of that zero is 7·10⁻¹¹. KU-RO, KI-RO, PO-TO-KU-RO and DA-I are functions of the Haghia Triada archive, and Khania offers nothing against which to check them.

Nor is Khania the same kind of archive: its tablets carry half the units (7.4 against 13.8) and a quarter of the syllabic groups (0.8 against 3.1), its figures are smaller (median 3 against 5), 36% of them are fractional against 17%, and its dominant commodity is cyperus (65 occurrences against 14), with 68% of its records in fractions. It is fine-grained distribution of a valued product, not bulk storage.

With the instruments run on the archive's own base rates, Khania yields no headings and no qualifiers of its own, and yields one reading that Haghia Triada cannot give: **CYP+D carries the quantity ½ in 12 of its 16 quantified attestations** against a 22% base (p = 10⁻⁵), and it is issued after entries of persons (KH 7a: VIR+*313b 10 then CYP+D ½; VIR+*313b 4 then CYP+D ⅓). No commodity at Haghia Triada shows a dominant quantity at that level. It is the corpus's only candidate for a fixed-quantity allocation.

The inventory is therefore to be read with this restriction: **it is the functional inventory of the Haghia Triada archive, with additions from Khania and from the votive vessels.** The Linear A corpus does not have one accounting format but at least two.

## 5. How it was reached, and why the number stops

The inventory went from 18 to 56 in two days of work with the same procedure on the same units: the parallel with Linear B (livestock, commodities, NI, TE), the extrapolation of structures (qualifier, sub-count, heading), name matching with a null, and two stages with a language model in the loop. Those two stages were measured: reading passages of the literature, the model invents non-existent units in 22% of cases; proposing a reading from the dossier of each unit (figures, position, company, seal), in 1%. Its contribution was routing at scale, not the idea: the three new readings it brought came from mechanical rules applied to units nobody had looked at with them. A second pass of the same procedure over the remaining 117 units found nothing.

That is the ceiling, and it should be stated precisely. It is not the ceiling of the problem: it is the ceiling of what can be **verified** with this corpus. Accounts have few functions and almost all are fixed; those that remain (some twenty nodule signs) wait for an external datum; and the step from function to word requires a judge the corpus does not contain, because nothing in it can say that "KU-NI-SU means emmer" is false. That judge would be given by a bilingual or by new running text, and those come from excavation.

## 6. Discussion

What this inventory changes is not the number of readings but their status. Each of the 56 carries in writing what observation would refute it, and the dictionary refuses to file an entry without that line. Each instrument carries its error rate, and a rate that came out wrong (the uniform null for fractions, 16.5%) is kept as a record of why the null was changed and not the instrument. Each claim with prior art carries the citation and the measurement together, and those that fall are filed as fallen, with the source against. It is what the field asks of a decipherment and has not asked of a lexicon: that one can know, of each line, how much it is worth.

And what the inventory says about Linear A, read whole, is something a century of proposals had not said in this form: **we know what was counted and how the account was organised, we know three places, and we know no word**. The distance between an archive understood and a language read is exactly that, and no internal method closes it.

## Data and reproducibility

GORILA corpus via the LinearA Explorer (R. Hogan); nodule seals from the commentaries of J. Younger; Linear B from linearb.xyz. Dictionary, error rates, sign × seal table and runs in data/derived/ of the kuro package (github.com/BiomeMakers/kuro), with the scripts that rebuild every non-redistributable source.

## Declaration of assistance

The corpus processing, the tests and the drafting of this text were produced with the assistance of a language model (Claude, Anthropic) under the direction of the author, who is responsible for all claims made here. Two stages of the procedure use the model in the loop; their invention rates are declared in section 5.

## References

Davis, B. 2024. Minoan Linear A: the state of the question. AURA Supplement 15.

Godart, L. 1984. Du linéaire A au linéaire B. In Aux origines de l'hellénisme: la Crète et la Grèce. Hommage à Henri van Effenterre. Paris, 121-128.

Godart, L. and J.-P. Olivier 1976-1985. Recueil des inscriptions en linéaire A (GORILA), 5 vols. Paris: École française d'Athènes.

Hallager, E. 1996. The Minoan Roundel and Other Sealed Documents in the Neopalatial Linear A Administration. Aegaeum 14, 2 vols. Liège.

Salgarella, E. 2019. Non-administrative Linear A? SMEA NS 5.

Schoep, I. 2002. The Administration of Neopalatial Crete. Minos Suppl. 17. Salamanca.

Ventris, M. and J. Chadwick 1973. Documents in Mycenaean Greek, 2nd ed. Cambridge.

Younger, J. G. 2024. Linear A Texts and Inscriptions in Phonetic Transcription (online).
