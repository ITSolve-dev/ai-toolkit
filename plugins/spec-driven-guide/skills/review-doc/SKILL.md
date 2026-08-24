---
name: review-doc
description: >-
  Review a design doc, spec, ADR or agent instruction file by fanning out one reviewer per
  dimension plus a cold reader who tries to use it, then rank the findings by how far the damage
  travels. Use whenever someone asks to review, critique, check or "sanity-check" a technical
  document, when a doc is about to be handed to implementers or agents, and when a draft feels
  wrong but nobody can say where.
---

# Review a document

One pass by one reader finds the defects that reader is primed for. This skill runs several narrow
reviewers in parallel and one reader who ignores the rules entirely and just tries to use the
document — that last one finds what none of the others can, because what it finds is absent.

Base root: `${CLAUDE_PLUGIN_ROOT}/knowledge`. Every `wiki/...` path below is relative to it,
including the ones you read yourself in steps 3 and 4 — you are running in the user's project, so
they resolve nowhere else.

## Steps

1. **Establish what the document claims to be.** Its genre, its reader, and its grain. Where the
   document states them, take its word; where it does not, impute them from the content and say so
   in the report — a document reviewed against the wrong level generates findings that are all
   false.

2. **Dispatch in parallel**, in one message: one `spec-driven-guide:doc-reviewer` per dimension
   below, plus one `spec-driven-guide:reader` with a concrete task drawn from what the document is
   for. Give each reviewer the document path, the genre/reader/grain from step 1, and its dimension
   with the pages named.

   | Dimension | Pages it works from |
   |---|---|
   | Altitude | `wiki/altitude/defining-a-level.md`, `wiki/failure-modes/mixed-levels-of-abstraction.md` |
   | Ceiling | `wiki/failure-modes/over-specification.md`, `wiki/failure-modes/implementation-manual.md`, `wiki/obligation-and-mechanism/when-a-snippet-beats-prose.md` |
   | Floor | `wiki/writing-for-agents/minimal-is-not-short.md`, `wiki/writing-for-agents/sprawl.md` |
   | Statements | `wiki/statement-quality/` — the five rule pages; `rfc-2119-requirement-levels.md` is a source summary and prescribes nothing |
   | Structure | `wiki/failure-modes/processing-order-is-not-a-structure.md`, `wiki/failure-modes/comprehensible-only-as-a-whole.md`, `wiki/document-types/splitting-a-document.md` |
   | Argument | `wiki/decision-records/every-argument-carries-a-because.md`, `wiki/reviewing/a-problem-with-no-decision.md`, `wiki/reviewing/unresolvable-references.md` |
   | Pruning | `wiki/reviewing/pruning-a-document.md` |

   Drop a dimension the document cannot exhibit rather than running it for completeness — an ADR
   has no altitude drift worth a reviewer.

   Reviewing a **set** of documents rather than one adds `wiki/reviewing/consistency-across-a-set.md`
   as its own dimension; those defects exist only between files and no single-file reviewer sees
   them.

3. **Merge, and resolve collisions.** Two dimensions will sometimes fire on the same passage from
   opposite directions — ceiling says cut, floor says the obligation is load-bearing. Resolve it
   with `wiki/obligation-and-mechanism/resolving-a-scale-conflict.md` and report one finding, not
   two. Reporting both hands the author the disagreement and answers nothing.

4. **Rank by how far the damage travels**, per `wiki/reviewing/ranking-findings.md`:

   1. Damage already outside the document — a wrong artifact built on it
   2. Damage to whoever acts on it — they must guess, and will
   3. Damage to durability — correct today, wrong soon
   4. Damage to reading — drift, vocabulary, order

   Within a rank, reach beats depth: a mild defect where everyone reads outranks a severe one in an
   appendix.

5. **Report.** Ranked findings, each with its passage, its symptom, its repair and its page. Open
   with one line on what the document is and what state it is in; close with what was *not* checked
   — a dimension dropped, a claim you could not verify, the planning half of a document this base
   does not cover. A review that hides its own gaps reads as complete and is not.

## The correction this review needs

Nearly every rule in the base argues for removing something, so the merged report tilts toward
cutting. The reader agent is the counterweight and its findings are the ones most likely to be
skipped, because they are the vaguest to act on. Put them where they rank — usually second — rather
than at the end.

Where the reader completed the task with no guesses and the dimension reviewers returned a long
list, say that plainly: the document works and the findings are improvements. That distinction is
what stops a review being read as a verdict.

## Done when

- Genre, reader and grain are stated — taken from the document or imputed and marked as imputed.
- Every dimension either ran or was dropped with a reason.
- No passage carries two findings that disagree.
- Findings are ranked by damage, not by the order they arrived.
- The report says what was not checked.
