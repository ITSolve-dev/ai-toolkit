---
title: Comprehensible only as a whole
category: failure-modes
summary: The reader-side symptom of a leaked decision — no part of the description can be understood without the others, because each part encodes constraints that belong elsewhere.
tags: [failure-mode, symptom, information-hiding, review]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

When a description reveals a decision it should have hidden, the damage shows up on the reader's
side before it shows up on the writer's. Parnas names the symptom precisely:

> To understand the output module in the first modularization, it will be necessary to understand
> something of the alphabetizer, the circular shifter, and the input module. There will be aspects
> of the tables used by output which will only make sense because of the way that the other modules
> work. There will be constraints on the structure of the tables due to the algorithms used in the
> other modules. **The system will only be comprehensible as a whole.**
>
> — [[parnas-criteria-for-decomposing-systems]], L201-L209

The last sentence is the diagnostic. A description whose parts cannot be read independently has
leaked something between them, whether or not any individual passage looks wrong.

## Why this is the useful symptom

The other symptoms of a leak require knowing what was leaked. This one does not: it is detectable
by trying to read a single section and noticing that you cannot, without having read others.
The reader's failure is the evidence, and it works even when the reader has no idea what the
correct boundary would have been.

Parnas is careful about the strength of the claim — he calls the contrast "my subjective judgment"
(L208). What is not subjective is the mechanism behind it: the output module's tables carry
constraints that originate in other modules' algorithms, so understanding the tables requires
understanding those algorithms.

## Where this check applies, and where it must not

**It applies to a description covering several things that are supposed to be independent** — a
system of components, a set of documents, a module boundary. There, "you cannot read this part
without that part" means the independence is fictitious, which is the finding.

**It does not apply inside a document about one coherent subject.** A design document about a
single component is *supposed* to have sections that depend on each other: the error handling
follows from the interface, the consistency argument follows from the storage decision. Applied
there, the check fires on ordinary forward and backward reference and flags well-structured
documents — which destroys a reviewer's credibility faster than missing a defect does.

Parnas is writing about modules of a program, where "another module's internal choices" is a
meaningful category. Inside one document about one thing, nearly every section's content *is*
another section's internal choice, and the category collapses.

## Using it as a review check, within that restriction

Take a section and read it alone. Then ask what you had to already know to make sense of it.

- **Knowledge of the subject** — expected, and not a defect.
- **A forward or backward reference within one subject** — expected. Not a defect.
- **Knowledge of the internal choices of something the document presents as separate** — a leak.
  The separation has been claimed and not delivered.

The check has a natural mechanisation: a reader with no other context tries to answer a question
the section should settle. What they cannot answer without reading elsewhere marks the leak. This
is the same evidence a naive reader produces in review, and it is the reason such a reader finds
defects that a knowledgeable reviewer does not — the knowledgeable one supplies the missing
context automatically and never notices it was missing.

Related: [[information-hiding]] for what should have been concealed,
[[abstract-interface-vs-representation]] for where the boundary belongs, and
[[over-specification]] for the neighbouring defect where the leak is a constraint rather than a
dependency.

Related: [[genre-blur]], for the case where the sections resist separation because they belong to
two different genres rather than because one meaning was scattered across them.
