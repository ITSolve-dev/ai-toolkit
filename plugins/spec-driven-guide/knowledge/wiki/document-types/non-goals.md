---
title: Non-goals
category: document-types
summary: Things that could reasonably have been goals and were deliberately chosen not to be — not negated goals, which is the distinction that makes the section checkable.
tags: [rule, design-doc, scope, symptom]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

A **non-goal** is an outcome that could plausibly have been a goal of this work and was
deliberately excluded. [[design-docs-at-google]] draws the line sharply, and the sharpness is what
makes the section verifiable rather than decorative:

> Note, that non-goals aren't negated goals like "The system shouldn't crash", but rather things
> that could reasonably be goals, but are explicitly chosen not to be goals. A good example would
> be "ACID compliance"; when designing a database, you'd certainly want to know whether that is a
> goal or non-goal.
>
> — L57

## The symptom

**A non-goal that nobody would have proposed as a goal is not a non-goal.** "The system shouldn't
crash", "we won't introduce security holes", "performance won't be terrible" — each states a
universal expectation and excludes nothing. The test is direct: could a reasonable person have
argued for this as a goal of this work? If not, the line is filler and its presence hides the
absence of real ones.

The inverse symptom is subtler and costlier: an obvious candidate goal that appears in neither
list. A reader who wonders "is X in scope here?" and finds no answer has found a defect, because
the ambiguity will be resolved by whoever implements, silently and at their discretion.

## Why the section carries weight

The example given is instructive: a database design that says nothing about ACID compliance leaves
the single most consequential question about it open. And the post notes that excluding something
does not forbid it — "if it is a non-goal you might still select a solution that provides it, if it
doesn't introduce trade-offs that prevent achieving the goals" (L57). A non-goal constrains what
the design will be *judged* on, not what it may deliver.

That is what makes non-goals part of the obligation rather than commentary: they bound the claim
the document is making. A design evaluated against goals it never accepted is being evaluated
against the wrong document.

Related: [[alternatives-considered]] performs the same function for solutions that
non-goals perform for outcomes — both record what was deliberately not chosen, so a later reader
can tell a decision from an oversight.
