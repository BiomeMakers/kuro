# Ideas parked for later

Things worth doing that are not worth doing now. Each entry says what it is, why it
would help, and what would have to be true for it to be worth the work.

---

## Annotate kuro's operations with the Workflow Motif Ontology

**What it is.** The Workflow Motif Ontology (Garijo, Alper and Belhajjame 2013,
http://purl.org/net/wf-motifs, https://vocab.linkeddata.es/motifs/) is a vocabulary for
annotating the steps of a scientific workflow with the kind of data operation each performs:
`DataPreparation` (with `Combine`, `Filter`, `Sort`, `Split`, `Group`, `FormatTransformation`,
`InputAugmentation`, `OutputExtraction`), `DataAnalysis`, `DataCleaning`, `DataRetrieval`,
`DataVisualization`, `DataMovement`. It was built from an empirical analysis of 260 workflows
in Taverna, Wings, Galaxy and Vistrails.

**Why it would help us, and this is the specific reason.** We already label every figure by
provenance (`[C]` computed, `[L]` cited, `[~]` illustrative). What we do not label is *which
kind of operation produced it*, and that is exactly where two of our errors came from. The
claim about -so and the zero for animal names were both failures in a **preparation** step
(what the corpus made available to be counted), not in the **analysis** step, and nothing in
the output distinguished the two. A figure tagged `DataAnalysis` and a figure tagged `Filter`
carry different risks, and saying so in the output would have made both errors visible.

**The second use: making the procedure citable.** The minimum protocol asks a proposal to
declare what it did. If kuro's functions carried these annotations, the whole workflow could be
described in a standard format, and a reader could see that the null runs after the filter and
before the analysis without reading the code.

**Caveats.** The ontology is from 2013 and aimed at workflow systems, not at analysis packages;
the mapping is not exact. And this is infrastructure work, worth doing when kuro is published
with a DOI, not while there are sources unread and letters unsent.

**Condition for doing it.** When the repository goes public and the software paper is submitted.


---

## A release manifest that CI verifies

**What it is.** OpenEtruscan (github.com/Eddy1919/openEtruscan) keeps a single
`release-manifest.json` holding every version, corpus count, licence, DOI and model status the
project asserts publicly, and a checker (`scripts/ops/check_release_truth.py`) that fails CI when
any surface drifts from it. They built it after an external audit found four different version
numbers across four public surfaces and three corpus totals with no machine-readable
reconciliation.

**Why we need it.** We have that problem now. The figures in the papers, in this README, in
`biblio/claims.json` and in the analysis notes are reconciled by memory alone. When a number is
corrected in one place, nothing checks the others. This week alone: the corpus size, the number
of votive documents, the hapax rate and the count of Assur recipes were each corrected in one
file while older values survived elsewhere.

**Minimum useful version.** A JSON file with the figures the papers assert (corpus counts, key
p-values, the number of documents in each dossier) and a test that reads the papers and fails when
a stated figure does not match. It does not need to cover licences or DOIs to be worth having.

**Condition for doing it.** Before the papers are submitted, not after. A corrected figure that
survives in one paper is exactly the error that costs credibility.
