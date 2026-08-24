---
title: Splitting a document
category: structure
summary: When a document carries two genres, the repair is usually a split rather than a deletion — the procedural half is legitimate output that belongs in its own document, not a defect to be cut.
tags: [method, genre, repair, wiki-authored]
sources: []
created: 2026-08-06
updated: 2026-08-06
---

**Provenance: this page is this wiki's own, and no source supplies it.** The charter promises "the
rules for choosing one, combining two, or splitting one in half", and only choosing is covered by a
source. [[implementation-manual]] offers the only nearby repair and offers the wrong one for this
case — it frames procedural content solely as a defect, with the choices "edit it out" or "replace
the document with the work". Neither fits a document whose procedural half is content somebody
needs. It should be grounded when a source treating genre separation is ingested.

---

A document carrying two genres is a common and recoverable condition, distinct from the document
that has degenerated into one genre. The two look similar and need opposite repairs.

## Distinguishing the two

Run [[implementation-manual]]'s subtraction — remove every passage stating how the work is carried
out — and read the residue:

- **Nothing of substance remains.** The document *is* the manual. Its repair is the one that page
  gives: it either becomes an argument or it is replaced by doing the work.
- **A defensible argument remains** — a problem, a rejected alternative with its mechanism,
  trade-offs, risks. The document is two documents in one file. **The procedural half is not
  waste**; somebody wrote it because somebody needs it. Deleting it destroys real work and
  guarantees it will be rewritten worse.

The second case is the common one in documents written to be handed to an implementer, human or
otherwise, and it is where the split applies.

## The split

**Cut along the question, not along the section boundaries.** The argument document answers *what
will be true and why*; the execution document answers *what will be done, in what order*. A section
that answers both gets divided rather than assigned.

**The argument document keeps** the problem, the constraints, the decision with its trade-offs, the
rejected alternatives, and the obligations the result must meet. It should survive the
implementation being redone differently.

**The execution document keeps** the file inventory, the ordered steps, the tooling and verification
commands, the before-and-after transformations. It is expected to become obsolete on completion,
and that is not a defect in it.

**The link runs one way.** Execution cites the argument for *why*; the argument does not cite
execution, or it inherits execution's decay ([[design-doc]] on how a design document ages).

## Recognising it before it happens

Two signals appear while writing, both cheap:

- **The document's own headings split into two vocabularies** — "problem", "alternatives",
  "risks" alongside "files", "steps", "commands".
- **The two halves have different expiry.** One is written to outlive the change; the other is
  written to be consumed by it. That difference is the split line, and it is the same volatility
  criterion that governs what belongs in a document at all
  ([[the-changeability-test]]).

## The boundary this wiki cannot cross

This wiki covers the argument document and, by charter, not the execution document — planning,
decomposition and task breakdown are excluded. So it can say a split is needed and say what goes on
each side; it cannot say whether the execution half is any good. A reviewer working from this base
should say so rather than leave the impression that the whole document was assessed.

Related: [[the-information-hierarchy]], for the cut made when the material is one genre on two rungs
rather than two genres in one file — the placement question, not the genre question.

## No longer this wiki's own claim alone

The core of this page is now sourced. [[genre-blur]] carries the finding that decides whether a
split is worth its cost: two genres in one file do not each get served partly — the collapse makes
it "impossible to meet the needs served by either". [[the-two-axis-test]] is how to tell which genre
a given passage actually is, which is the step this page assumed rather than supplied.
