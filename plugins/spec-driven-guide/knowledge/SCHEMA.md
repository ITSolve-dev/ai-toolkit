# Writing Documents That Drive Development — SCHEMA

<!--
This file is the CHARTER and the ROOT MARKER: its presence marks this directory as a wiki
root, and its contents are the lens ingest uses to decide what to keep.

Per Karpathy, the schema is "what makes the LLM a disciplined wiki maintainer rather than a
generic chatbot" — and it is a LIVING document you and the LLM co-evolve as you learn what
works for this domain. The generic structure/conventions/workflows live in the llm-wiki
plugin; this file holds the DOMAIN-SPECIFIC charter and any local overrides. Fill every
section, then keep refining it.
-->

## Purpose

A working reference for writing documents that drive development — how to state what a thing
must do and why, at a level that survives the implementation changing underneath it.

It serves two readers. The team, when authoring or reviewing a design document, a decision
record, or an instruction written for an agent. And the skills of the plugin that bundles this
wiki, which consult it instead of reasoning from general knowledge — an uncited answer about
where a boundary falls is indistinguishable from a cited one, and that is precisely why the base
exists.

The charter is deliberately about **writing in general**, not about any one genre. Genres are
served by the skills; the knowledge under them is shared.

## Scope — the ingestion lens

Ingest judges every candidate fact from a source against this. Be specific — this is what
separates signal from noise for THIS wiki.

**In scope (keep):**
- Levels of abstraction: choosing an altitude, holding it across a document, and the genre
  ceiling below which a document stops being what it claims to be and becomes an execution plan.
- Separating obligation from mechanism: information hiding applied to prose, black-box
  description, what an interface commits to versus how it is realised.
- Volatility as a criterion — which elements change faster than the document naming them, and
  how that decides whether an element belongs in it.
- Document types, and the rules for choosing one, combining two, or splitting one in half.
- Quality of a statement: unambiguity, verifiability, atomicity, the language of obligation.
- Observable behaviour, acceptance criteria, and what counts as failure.
- Structure and order of exposition; keeping genres apart inside one document.
- Recording a decision: its context, the alternatives, the consequences, and why the rejected
  options were rejected.
- Writing for an agent reader: what must be exact so that it does not guess, and where that
  requirement conflicts with abstraction.
- Reviewing documents: internal contradictions, unresolvable references, terminology drift,
  and testing a document by trying to use it.
- Failure modes of writing, each recorded with the symptom that reveals it **in the text**.

**Out of scope (drop):**
- Templates of particular organisations presented as a form to copy. Their reasoning is in
  scope; their section list is not.
- Tooling for storing, publishing or collaborating on documents.
- Planning, decomposition, estimation, task breakdown — the execution half of the practice.
- Grammar and style beyond what affects unambiguity or altitude.
- Product and marketing writing; end-user documentation as a craft of its own.
- Codegen workflows in which a document is compiled into an implementation.

## Domain extraction schema

From each source, extract these kinds of knowledge (tailor to the domain — this overrides
the generic default):

- **Rules**, each stated so that a violation of it is detectable in a text.
- **The reasoning under a rule** — what specifically breaks when it is ignored. A rule without
  its reasoning cannot be applied to a case its author did not foresee.
- **Discriminating criteria** — what separates two neighbouring cases: obligation from
  mechanism, one document type from another, essential detail from incidental.
- **Trade-offs** — what a rule costs when it is followed, not only what it buys.
- **Failure modes**, with the symptom that reveals each one in the text.
- **Before/after pairs**, wherever a source shows a passage rewritten. These are the most
  valuable artifact this domain produces and the hardest to reconstruct later.

## Grouping principle

Pages live in subdirectories of `wiki/`, named by this domain's own topics, so the folder tree
is self-documenting (e.g. `strategic-design/`, not `concepts/`). Rather than enumerate every
group, state the **principle** by which this wiki splits pages into groups; new groups are
created as topics appear, and the emerging tree shows what exists. A page's `category`
frontmatter equals its folder name.

Group by the **question a writer arrives with**, not by source and not by document genre — the
same rule usually serves several genres, and duplicating it per genre is how this wiki would
rot. A page goes where someone stuck on that specific question would look: how high to write and
how to stay there, what to keep and what to drop, which document this even is, how to phrase
something so it can be checked, how to record a decision, how to write for a machine reader, how
to review, and what goes wrong.

## Languages

- **Wiki language:** English — pages, summaries, and synthesis are written in English.
- **Communication language:** Russian — the LLM converses in Russian (questions, surfaced
  takeaways, reports).

## Conventions

- Pages, frontmatter, and `[[wikilinks]]` follow the `llm-wiki` plugin's page conventions.
- Link style: `[[slug]]` (Obsidian-style).

### Page kinds

The first entry in `tags` is the page's kind. Eight are in use here, beyond the generic set:

| Kind | What it holds |
|---|---|
| `summary` | One per ingested source |
| `concept` | An idea, defined and situated |
| `rule` | A prescription, with the symptom that reveals its violation in a text |
| `method` | A procedure to run against a document |
| `decision-rule` | A test deciding between two courses |
| `mechanism` | A device that makes something else work |
| `position` | A stance a source takes, where the wiki records it as contested |
| `failure-mode` | A defect, with its symptom |

`comparison` is available for a page whose subject is a disagreement between sources, and is
currently unused.

### Pages this wiki authored itself

Some pages carry `sources: []` and an explicit provenance note. They exist where the charter names
something in scope, no ingested source treats it, and leaving the gap open made the base unusable
for review. They are marked so a reader can tell a distilled claim from an invented one, and each
says what would have to be found to ground it. Their number should go down, not up.

## Workflow customizations

Per-wiki overrides to the plugin's default ingest / query / lint behavior. Leave empty to
use the defaults; add rules here as you and the LLM discover what this domain needs.

- **Ingest: a rule is kept only with a detectable symptom.** A prescription that cannot be
  checked against a piece of text — "write clearly", "be concise" — is commentary, not knowledge
  for this wiki. Either find the symptom the source implies, or drop the claim.
- **Ingest: record where each source puts the ceiling.** Sources disagree about how much
  implementation detail a design document may carry, and some tolerate a great deal. The
  disagreement is itself the knowledge; flattening it into one house rule destroys the ability to
  answer a boundary question with reasoning instead of assertion.
- **Query: when an answer draws a boundary, give a case on each side of it.** Boundary questions
  are the hard ones in this domain, and a criterion stated without a near-miss on either side is
  not usable by a reviewer.
- **Writing: any sentence extending a quotation opens with an explicit subject.** "This wiki reads
  that as…", "the transfer here is ours…", "a hypothesis of this wiki's…". Nearly every source this
  base draws on argues about code, or about diagrams, or about one organisation's practice, so
  almost every page must extend its source to reach a claim about writing. A block quote followed
  by unbroken declarative prose makes that extension read as the source's — the single failure mode
  most damaging to a base whose whole value is that a reader can go and check.
- **Symptom rule, applied strictly.** A rule page keeps its rule only with a symptom checkable
  **against a piece of text**. A check that requires observing a reader, forecasting the future, or
  knowing current practice is not a textual symptom; such a page must say so in the check itself
  rather than claiming detectability. Source-summary pages are exempt — they describe a source
  rather than prescribe anything.

## Notes

Starting sources are open-access; book material is added later, and only against a gap observed
after the first pass. Candidates, in rough order of directness:

- Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (1972) — hide what is
  likely to change. The reasoning under the central rule of this wiki.
- Parnas & Clements, *A Rational Design Process: How and Why to Fake It* — why a document
  describes the decision, not the path taken to it.
- Diátaxis — genre separation, and what mixing genres does to a document.
- The C4 model — levels of description and the rule against mixing them.
- Architecture decision records: Nygard's original write-up and the community collection.
- RFC 2119 — the language of obligation.
- Published accounts of design-document practice at scale, and of request-for-discussion
  processes, for what such a document contains and what it deliberately omits.
- A developer documentation style guide under a permissive licence, for unambiguity of phrasing.
- Vendor documentation on writing instructions for agents, for the machine-reader genre.

Deferred, pending a demonstrated gap: Cockburn on goal levels (the most direct source on
altitude), Wiegers on requirement quality, Brooks on essence versus accident.

<!-- Co-evolution log: record decisions about how THIS wiki is run as they emerge. -->

- 2026-08-06 — Charter written to be genre-neutral on purpose. The discipline is expected to
  serve a second consumer outside this plugin; keeping the charter free of any one genre is what
  makes moving it later cost a directory move rather than a rewrite.

- 2026-08-07 — Six read-only reviewers audited the base after its first nine sources. Three rules
  above were added as a result: the explicit-subject rule after a quotation, the strict reading of
  the symptom requirement, and the exemption for source summaries. The audit's own conclusion is
  worth keeping: **a base built for review is judged differently from a base built for reference.**
  Recording a disagreement between sources and telling the reader to hold both is honest for a
  reference and useless for review — it returns exactly the hard cases and answers only the easy
  ones. Where two rules here collide on the same passage, a page must resolve the collision rather
  than name it.

- 2026-08-07 — Known and open, so the next pass does not rediscover them: `failure-modes/` groups
  by page kind rather than by question and should be dissolved into the question groups, with the
  kind kept in tags; there are no before/after rewrite pairs anywhere, though the extraction schema
  above calls them this domain's most valuable artifact; Diátaxis is uningested, which leaves
  "combining two documents, or splitting one in half" covered only by a page this wiki wrote
  itself; and no source on requirement quality or on altitude proper has been obtained, so both
  rest on thin material.

- 2026-08-08 — Two practitioner sources ingested (`writing-for-agents`, and the ADR/spec formats
  from the same toolkit), closing the gap the audit named first: **the base had no argument about
  volume, only about kind.** [[sprawl]] supplies it, and it turned out to need a rule of its own
  rather than a stronger cutting rule — a document can be too long while every line in it is live,
  and there the repair is relocation, not deletion. That is now stated on the floor page as well, so
  neither can be applied alone.

  Two consequences for how this wiki is run. **A practitioner source is graded on its mechanisms,
  not its magnitudes** — these two argue from observed behaviour with no study behind them, so a
  claim is kept when it names something checkable in a text and dropped when it only asserts a size
  of effect. And **a contested claim now gets resolved on the page that raises it**: the minimal-ADR
  position collides with this wiki's own rule on consequences, and per the 2026-08-07 entry the
  collision is settled there rather than reported.

  Still open from the entry above, unchanged: `failure-modes/`, before/after pairs, Diátaxis,
  Cockburn. Requirement quality is now partly served from an adjacent direction
  (`completion-criteria`, `leading-words`) but still has no source that studies it directly.

- 2026-08-24 — Diátaxis ingested **narrowly**, and the narrowness is the point worth recording. Its
  subject — end-user documentation as a craft — is named in the exclusions above, and its four
  genres are not this wiki's genres. Three claims were taken because they hold of any genre pair,
  and every page carrying one states that the transfer is this wiki's rather than the source's.
  The taxonomy, the pedagogy and the map were left.

  **A source can be mostly out of charter and still worth ingesting.** The gate is per-claim, not
  per-source; what makes this safe is the marking, not the selection. A future pass tempted to
  "finish" Diátaxis by adopting its four kinds should read this entry first — that is the version of
  this ingest that would break the wiki.

  It closes one open item: "combining two documents, or splitting one in half" no longer rests on a
  page this wiki wrote itself. It also gives `reviewing/` its first sourced fragment of a severity
  order, which `ranking-findings` had recorded as missing.

- 2026-08-24 — `failure-modes/` dissolved, closing the oldest open item. It grouped by page kind
  while the charter groups by the question a writer arrives with, and the kind is carried in `tags`
  anyway. Its five pages went where the question sends them: over-specification and the
  implementation manual to `obligation-and-mechanism/`, mixed levels to `altitude/`, processing
  order and comprehensibility to a new `structure/` group.

  **`structure/` is the group the charter always implied and the tree never had** — "structure and
  order of exposition; keeping genres apart inside one document" is one of its scope bullets. The
  genre pages moved there from `document-types/` for the same reason: which document this *is* and
  how one document is *shaped* are different questions, and a reader stuck on the second was being
  sent to the first.

- 2026-08-24 — Four **before/after pairs** added, closing the extraction schema's oldest unmet
  bullet. They are not from a source and say so: each was produced by running this base's own
  reviewers against a document written to carry the defect, and taking the repair the reviewer
  proposed. They live on the rule pages rather than in a group of their own, because a pair read
  apart from its rule is an anecdote.

  **The pairs were chosen for the trap, not the illustration.** The ceiling pair shows a passage
  whose naive repair — delete it as implementation detail — removes the obligation with the
  mechanism. The floor pair shows a rewrite that is four times longer and more minimal. Those are
  the two mistakes this base's own rules most invite, and neither is visible in a pair chosen to
  show a rule working.

- 2026-08-24 — The base was measured, and then the measurement was refuted. Both halves are the
  record; the first alone would be misleading.

  **What was run.** Three dimension reviewers plus a cold reader against a document written to carry
  nine defects, and three reviewers against a document written to be clean. All nine were reported
  by the dimension assigned them, and nothing was reported that could not be substantiated.

  **Why that supports much less than it appears to.** An adversarial pass took the claim apart, and
  its central finding holds up under checking: **the planted defects were transcriptions of this
  base's own example strings.** `genre-blur` lists "Files to modify" as its symptom; the test
  document has a section headed exactly that. `completion-criteria` gives "the system is robust" as
  its example of an unfalsifiable claim; the test document says "the service should be robust".
  The reviewers were then handed, per dimension, the very pages those strings came from. That
  measures retrieval under maximal cueing, not detection.

  Three further holes, all confirmed: the dimension table in force during the run differed from the
  one that shipped, and the page that governed one credited defect was in neither — it was added to
  the test prompt by hand, so the page list was curated for the document. Only step 2 of the review
  skill ran; establishing genre and grain, merging, ranking and reporting were never exercised. And
  every run was n=1 on a stochastic model with no baseline, so nothing separates "the pipeline
  works" from "the document was easy".

  **What survives.** The fan-out runs and returns findings in the required shape. And the one result
  that was not cued: the document written to be clean was not clean — three findings came back and
  all three were real defects its author had missed, including a headline commitment contradicted
  two paragraphs later. Nothing was planted there and nothing pre-registered, so that result is
  worth more than the 9/9 it sits beside. It is also an anecdote.

  **The fixture is burned.** The reviewers' own repairs were written into `over-specification` and
  `processing-order-is-not-a-structure` as before/after pairs, so any future reviewer pointed at
  that document finds the answer in the first page it reads. A real measurement needs a fresh
  document written by someone who has not read this base, a ground truth registered before the run,
  and an ungrounded baseline alongside.

  **The rule this leaves behind:** a symptom's example in this base must never be reused as a test
  case for that symptom. The base is the answer key.
