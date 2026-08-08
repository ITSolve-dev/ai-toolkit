---
title: Mixed levels of abstraction
category: failure-modes
summary: A description that moves between levels without saying so — listed among the recurring defects of ad hoc architecture description, alongside the vagueness that usually accompanies it.
tags: [failure-mode, altitude, symptom]
sources: [c4-model]
created: 2026-08-06
updated: 2026-08-06
---

[[the-c4-model]] opens by cataloguing what goes wrong in descriptions produced without a discipline
of levels. The list is worth having whole, because the entries co-occur:

> - Notation […] is not explained or is inconsistent.
> - The purpose and meaning of elements is ambiguous.
> - Relationships between elements are missing.
> - Relationships between elements are unlabelled.
> - Generic terms such as "business logic" are used.
> - Acronyms and abbreviations are not explained.
> - Technology choices are missing.
> - **Levels of abstraction are mixed.**
>
> — L121-L130

## Why the entries travel together

The source gives a flat list and asserts no ordering among the entries. It does state a causal
direction once, and it runs from vocabulary to levels: ad hoc abstractions are "**caused by an
impreciseness of terminology**" (L437). This wiki treats generic vocabulary as the surface signal
of level confusion for that reason — see [[imprecise-terminology]], where the source's own argument
is set out.

**A hypothesis of this wiki's, offered as such and unsourced:** the entries co-occur because a
description that has not fixed its level cannot decide what its elements are, so their meaning goes
ambiguous, and cannot decide how much to say about relationships, so they go unlabelled. Whether
that reads the causation backwards from the source is open; nothing here settles it, and a reviewer
who finds vague vocabulary should reach for the source's direction first and define the word.

## The check

Mixing can only be shown against a level the document has claimed. **Most documents never declare
one**, which does not make the check inert — the claim can be imputed. Read the document's opening
as its claim of subject: "multiple places in the system need X" claims the system; "this module
provides X" claims the component. A reviewer is entitled to hold a document to the scope its own
first paragraph asserts. The procedure and its limits are in [[resolving-a-scale-conflict]];
[[defining-a-level]] is the author-side version, for someone who can still declare it outright.

Where the opening asserts no scope at all, there is nothing to hold the document to, and the honest
finding is the missing claim rather than a drift.

Once the level is claimed or imputed:

1. **Take each section and ask what its elements are.** Are they the level's primary elements, or
   the elements of a level above or below?
2. **Take each generic term and ask what it denotes at this level.** If the answer requires
   descending a level to give, the term is doing the descending.

The second test is the one that catches the drift early, because a section that has slipped
usually announces itself in vocabulary before it announces itself in structure.

## Its relation to the neighbouring failures

- [[processing-order-is-not-a-structure]] is what a description organises itself by when it has no
  level to organise by. Steps are always available; levels have to be chosen.
- [[implementation-manual]] is the endpoint of unchecked downward drift: not a document that mixes
  levels, but one that has arrived at the bottom and stayed.
- [[imprecise-terminology]] carries the source's own position: vague vocabulary is the cause, and
  the repair is to define the word rather than to add a level. Read it before acting on anything
  here — this page's contribution is the level check, not a competing account of causation.
