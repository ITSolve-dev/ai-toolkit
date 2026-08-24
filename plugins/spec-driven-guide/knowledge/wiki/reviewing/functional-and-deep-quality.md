---
title: Functional and deep quality
category: reviewing
summary: Two kinds of quality — one measured against the world, one judged against a reader — with a one-way dependency between them that gives this wiki its only sourced argument for ranking findings.
tags: [concept, review, severity]
sources: [web-page-diataxis]
created: 2026-08-24
updated: 2026-08-24
---

[[diataxis]] separates two things a review usually confuses (L1155). **Functional quality** is
accuracy, completeness, consistency, precision. **Deep quality** is the harder-named set — whether
the document has flow, whether it anticipates its reader.

Three differences are stated, and the third is what this wiki uses.

**They are not the same kind of property.** "Documentation can meet all the demands of functional
quality, and still fail to exhibit deep quality. There are many examples of documentation that is
accurate and consistent (and even very useful) but which is also awkward and unpleasant to use"
(L1192).

**One is measured, the other judged.** Functional aspects "can be measured - literally, with
numbers, in some cases"; deep ones "can only be enquired into, interrogated. Instead of taking
**measurements**, we must make **judgements**" (L1200-L1204). The source adds that functional
aspects are independent of each other while deep ones are "interdependent" — flow and anticipating
the reader "are aspects of each other" (L1194-L1198).

**And the dependency runs one way:**

> And, deep quality is **conditional** upon functional quality. Documentation can be accurate and
> complete and consistent without being truly excellent - but it will never have deep quality
> without being accurate and complete and consistent.
>
> — L1212-L1214

## Why this matters to this wiki

[[ranking-findings]] states plainly that no source supplies a severity order, and that it is kept
only because a review that cannot rank is unusable. The conditional above is the first sourced
fragment of one: **a functional defect outranks a deep one, because fixing the deep one while the
functional one stands cannot succeed.** That is an ordering with a reason under it, not a
preference.

It grounds part of the existing axis rather than replacing it. The damage ranks in
[[ranking-findings]] are about how far a defect travels; this is about which repairs are even
possible in what order. Where the two disagree, the damage axis governs — a functional defect in an
appendix still ranks below a deep one in the section everyone reads.

## What it also settles

A reviewer who reports only what can be counted — a broken reference, a missing section, an
inconsistent term — is reporting functional quality alone, and the source's first claim is that a
document can pass all of it and still fail its reader. This wiki's counterpart is
[[the-use-test]]: the only check here that produces a judgement rather than a measurement, and
therefore the only one that reaches deep quality at all.

The corollary is uncomfortable and worth stating. Every textual symptom in this wiki is a functional
check. They are cheap, they are reproducible, and by this source's argument they are necessary and
insufficient — which is the reason the reader agent exists rather than being an optimisation.

## Its limit here

The source is describing end-user documentation, where "unpleasant to use" is a cost paid by many
readers repeatedly. Whether deep quality carries the same weight for a decision record read twice in
five years, this wiki does not know and the source does not say. The conditional relation is what
transfers safely; the *importance* of deep quality relative to functional is a claim about a
readership, and this wiki's readership is not the source's.
