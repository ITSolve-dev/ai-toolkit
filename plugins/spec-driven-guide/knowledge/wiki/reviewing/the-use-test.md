---
title: The use test
category: reviewing
summary: Give the document to a reader with no outside context and a decision to make — what they cannot decide marks a missing obligation, and where they choose arbitrarily marks its location.
tags: [method, review, under-specification]
sources: [web-page-effective-context-engineering-for-ai-agents, web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

Three sources in this wiki reach the same method independently, from three different concerns, and
none of them names it. **Try to use the document, and treat the failure as the finding.**

- For a missing obligation: "give the document to someone — or something — with no outside context
  and a decision to make, and see whether they can make it. A reader who has to choose arbitrarily
  has found a missing obligation, and the arbitrary choice marks its location"
  ([[minimal-is-not-short]]).
- For a false assumption of shared context: "it can be tested by giving the text to a reader who
  genuinely lacks that context and seeing what they do"
  ([[the-right-altitude-for-an-agent]]).
- For a leaked dependency: "a reader with no other context tries to answer a question the section
  should settle" ([[comprehensible-only-as-a-whole]]).

Convergence from three directions is the argument for treating it as the primary review method
rather than a fallback.

## Why it finds what reading cannot

Every other check in this wiki inspects the text for something present — a leaked format, an
unearned imperative, a vague term. **Propositions that were never written leave no trace**, so no
amount of careful reading finds them. The only evidence of an absence is somebody failing to
proceed.

This is also why the method cannot be replaced by a more attentive reviewer. Someone who knows the
subject supplies the missing information automatically and never notices supplying it. The test
depends on the reader's ignorance, which means the reviewer's competence works against it.

## Running it

1. **Write the questions first, before reading with them in mind.** The document should settle
   them: what happens in case X, which of two behaviours is guaranteed, what counts as failure. A
   brief or a problem statement is the best source; where none exists, predict what a reader
   arriving at this document would need.
2. **Give a reader the document and the questions — nothing else.** No conversation, no
   surrounding repository, no access to the author.
3. **Record three outcomes per question**, not two: answered; answered *wrongly*; and could not
   answer. The middle one is the most valuable, because it means the document actively misled
   rather than merely omitted.
4. **Locate by the arbitrary choice.** Where the reader had to pick, the passage they were reading
   when they picked is where the obligation is missing.

## What the outcome distinguishes, and what it does not

The test fires on any missing information; deciding *which* defect it found needs a second step:

- The needed knowledge lives **in another section** → a leaked dependency, and the finding is
  the coupling ([[comprehensible-only-as-a-whole]], within its restriction).
- The needed knowledge lives **nowhere in the document** → a missing obligation
  ([[minimal-is-not-short]]).
- The needed knowledge lives **in the document but was not found** → a structure or ordering
  defect, not an omission.

What it produces outranks most of what textual checks produce, because a reader who could not
proceed is evidence of damage about to happen rather than of a sentence that will age — see
[[ranking-findings]].

## Its cost, stated plainly

This is the most expensive check in the wiki. It needs a second reader, isolation from context, and
prepared questions — where the textual checks need one person and the file. That cost is why the
under-specification failure is systematically under-detected, and why a base whose rules almost all
point toward cutting is dangerous without it: **the failure it catches is the one every other rule
here makes more likely.**

Its opposite number is [[pruning-a-document]]: this test finds what the document never said, that
pass finds what it said and did not need. Run them in that order — pruning first would delete lines
the use test is about to prove load-bearing.

[[functional-and-deep-quality]] says why this test cannot be replaced by cheaper ones: every textual
symptom in this wiki is a measurement, and this is the only check here that produces a judgement.
By that source's argument the measurements are necessary and insufficient — which makes this test a
requirement rather than an optimisation.
