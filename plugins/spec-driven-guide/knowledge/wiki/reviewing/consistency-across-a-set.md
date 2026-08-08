---
title: Consistency across a set
category: reviewing
summary: A collection of documents has defects no single document has — inconsistent naming, no stated reading order, and no transition from one to the next.
tags: [failure-mode, review, collection, symptom]
sources: [c4-model]
created: 2026-08-06
updated: 2026-08-06
---

[[the-c4-model]] keeps two lists of defects: one for a single artifact, and a second for what
happens when several accumulate. The second is the one a reviewer of a document *set* needs, and it
is short enough to use as a checklist:

> - The notation (shapes, colour coding, line styles, etc) is not consistent between diagrams.
> - The naming of elements is not consistent between diagrams.
> - The logical order in which to read the diagrams isn't clear.
> - There is no clear transition between one diagram and the next.
>
> — L134-L137

Stated for prose rather than diagrams, three of the four survive intact:

**Inconsistent naming.** The same thing called different names across documents, or the same name
used for different things. Each document is internally coherent; the set is not. This is
[[imprecise-terminology]] distributed across files, where it is harder to see because no single
document contains the contradiction.

**No stated reading order.** The set assumes an order that exists only in its author's head. A
reader starting from the wrong document meets forward references to material they have not seen and
concludes the writing is unclear.

**No transition between documents.** Each ends where its subject ends, with nothing saying what
comes next or which document takes over the topic. The reader is left to search — and, more often,
to assume nothing further exists.

The fourth entry, notation consistency, has a prose analogue in inconsistent conventions: what is
emphasised, what is quoted, how obligations are marked. It is the weakest of the four and rarely
worth a finding on its own.

## Why these need a separate pass

Every one of these defects is invisible from inside a single document. A reviewer reading one file
carefully cannot find them, because each file is consistent with itself — the defect exists only in
the relation between files, and only a pass that holds several at once can see it.

That is the practical argument for treating cross-document review as its own dimension rather than
as a thoroughness setting on ordinary review.

## The related failure this list omits

Consistency is not the same as agreement. A set can be perfectly consistent in naming and order and
still contain two documents that assert incompatible things — and the same reading that finds
naming drift will not find a contradiction unless it is looking for one. See
[[superseding-not-editing]] for the mechanism that keeps a *decision* set honest about its own
reversals; a document set with no such mechanism accumulates silent contradictions instead.
