---
title: State the commitment, not the means
category: obligation-and-mechanism
summary: The rule several unrelated sources arrive at, the two grounds it rests on, and the tests each ground supplies — held apart from the method that first produced it.
tags: [concept, criterion, convergence]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules, web-page-design-docs-at-google, c4-model, web-page-rfc-2119-key-words-for-use-in-rfcs-to-indicate-requirement-levels-rfc-editor]
created: 2026-08-07
updated: 2026-08-07
---

> State what the subject commits to. Do not state the means of meeting it.

This is the conclusion several sources here reach, and it is not the same thing as
[[information-hiding]], which is Parnas's *method* for reaching it. The distinction matters because
the two are cited for different purposes: the method tells you how to organise a description, the
conclusion tells you what a sentence may contain. Pages arguing the second should cite this page.

## The two grounds

**Volatility — one argument, confirmed at three scales.** A commitment changes slowly; the means of
meeting it changes fast, and everything that named the means must be revised with it.

| Scale | Source | Its form of the argument |
|---|---|---|
| A module | Parnas | A revealed decision must be revised everywhere it was revealed ([[information-hiding]]) |
| A document | design-doc practice | Pasted definitions "quickly get out of date", making the document wrong rather than detailed ([[what-a-design-doc-omits]]) |
| A level | C4 | Deployment is excluded because it "will likely vary across different environments" ([[defining-a-level]]) |

These are not independent confirmations; they are the same criterion applied to three different
units. That is still worth something — a criterion that holds at three scales is more likely to be
about the underlying thing than about the unit it was first noticed in — but it is one reason, not
three.

**Interoperation and harm — genuinely independent.** RFC 2119 restricts binding statements to where
something must work together, or where the prescribed method is itself hazardous
([[imperatives-constrain-outcomes-not-methods]]). Volatility plays no part, and the harm ground has
no counterpart in the other three: it licenses constraining a method when the method is the danger,
which the volatility argument alone would forbid.

## The tests, and why you need more than one

Each ground supplies a different check, and they disagree on borderline cases:

- **Enumerate likely changes and count the passages each would touch** — [[the-changeability-test]].
- **Delete the passage and ask whether the argument survives** — [[what-a-design-doc-omits]].
- **Name a valid alternative the statement excludes** — [[over-specification]].
- **Ask what would fail to work together if this were free** —
  [[imperatives-constrain-outcomes-not-methods]].

Where they disagree, the disagreement is usually about *grain* rather than about the rule:
[[resolving-a-scale-conflict]].

## The floor

The rule reads as licence to cut and must not be applied alone. What a document commits to has to
survive the cutting, and a document that has removed its obligations along with its mechanism has
failed differently but no less completely — [[minimal-is-not-short]],
[[the-right-altitude-for-an-agent]]. The asymmetry is real: this wiki's sources are preoccupied
with saying too much and nearly silent about saying too little.

## Two applications worth reaching separately

[[when-a-snippet-beats-prose]] applies the rule to content that looks like implementation and is
not — the schema, the state machine, the type shape. [[pruning-a-document]] applies it to content
the surrounding environment already states, where the ground is discoverability rather than
volatility, and the check is therefore cheap to run.
