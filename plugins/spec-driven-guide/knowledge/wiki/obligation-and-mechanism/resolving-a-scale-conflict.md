---
title: Resolving a scale conflict
category: obligation-and-mechanism
summary: When one rule says a passage states the obligation and another says it leaks the mechanism, the two are answering at different grains — separate the grain question from the form question and both resolve.
tags: [method, criterion, boundary, review]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules, web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

Two rules in this wiki return opposite verdicts on the same passage, and the case is common rather
than exotic. A design document contains the operations of a component, with their parameters and
types.

- [[abstract-interface-vs-representation]] says this is the commitment, and "a document that omits
  them has withheld its obligation rather than its mechanism."
- [[what-a-design-doc-omits]] says "withstand the temptation to copy-paste formal interface or data
  definitions into the doc."

Both are correctly stated. The conflict is not between them; it is that a reviewer applying either
alone gets a confident wrong answer. **The passages a reader most wants adjudicated are exactly the
ones two rules disagree about**, so a base that cannot resolve this answers only the easy cases.

## The two questions are different, and only one of them is about scale

**Question one — grain. Whose commitment is this?**

An interface is an obligation *of its owner*. So the test is not "is this an interface" but "is the
document's subject the thing that owes it":

- **The subject owes it** — the document is about this component, and these operations are what it
  promises to everything outside. State them. Omitting them withholds the obligation.
- **Something inside the subject owes it** — the document is about a system, and these are one
  component's operations. Now they are an internal decision, and naming them commits the reader to
  a boundary the document's subject does not actually promise to keep.

This is what [[abstract-interface-vs-representation]] means by "the line is stable; what sits on
each side of it moves with the subject". The line does not move. The subject does.

**Question two — form. Stated, or transplanted?**

Independent of grain, and this is where the second rule bites. Even when an interface is the
subject's own commitment, there is a difference between *stating* it and *importing the artifact
that defines it*. A signature described in prose or sketched to the depth the argument needs is a
statement. A pasted definition file is a transplant: it carries syntax, ordering, annotations,
imports and defaults that no argument in the document turns on, and all of which will change on a
schedule the document does not track.

So the two rules govern different axes and never actually contradict:

| | Subject owes it | Something inside owes it |
|---|---|---|
| **Stated** | Correct | Wrong grain — the finding is the grain, not the form |
| **Transplanted** | Right content, wrong form — cite or link the definition instead | Wrong on both counts |

## Imputing the grain when the document does not declare one

Most real documents never declare a level ([[defining-a-level]] is written for the author, who
still can). A reviewer needs a way to impute one, and inventing it produces arbitrary findings.

**Read the document's own opening as its claim.** The first paragraph names a subject — "multiple
places in the system need file storage" claims the system; "this module provides X" claims the
component. That claim is the level, and the reviewer is entitled to hold the document to it because
the document made it.

Two consequences worth stating:

- **If the opening claims a system and the body specifies a component's internals, the finding is
  real** and it is a drift finding, not a taste finding — see
  [[mixed-levels-of-abstraction]].
- **If the opening claims the component, component-level operations are in scope** and a reviewer
  citing the ceiling rule against them is over-firing.

Where the opening is genuinely silent about scope, there is no claim to hold the document to, and
the honest finding is that one is missing — not a grain violation.

## What this does not settle

The grain test tells you which side a passage falls on. It does not tell you **how much** of the
subject's own interface belongs in the document — whether all operations or only those the argument
turns on. [[what-a-design-doc-omits]] answers that with the deletion test: keep what the trade-offs
turn on. The two combine cleanly, and where they still disagree the document is probably trying to
be two documents at once.
