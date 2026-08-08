---
title: Canonical examples, not edge cases
category: writing-for-agents
summary: A curated set of diverse representative examples outperforms an exhaustive list of every rule the reader should follow — and the exhaustive list is the more common instinct.
tags: [rule, agent-reader, examples, symptom]
sources: [web-page-effective-context-engineering-for-ai-agents]
created: 2026-08-06
updated: 2026-08-06
---

[[effective-context-engineering]] endorses examples and rejects the usual way of producing them:

> teams will often stuff a laundry list of edge cases into a prompt in an attempt to articulate
> every possible rule the LLM should follow for a particular task. We do not recommend this.
> Instead, we recommend working to curate a set of diverse, canonical examples that effectively
> portray the expected behavior of the agent. For an LLM, examples are the "pictures" worth a
> thousand words.
>
> — L55

Two properties are asked of the set: **diverse** — the examples differ from each other along the
dimensions that matter — and **canonical** — each is a clear case of the behaviour rather than a
corner of it.

## Why enumeration fails

An edge-case list is an attempt to specify behaviour by covering the space, and the space cannot be
covered. Each entry handles one situation and says nothing about its neighbours, so the reader
facing an unlisted case has no basis for generalising — and has been implicitly taught that
generalising is not expected, since the document's method has been to enumerate.

Canonical examples do the opposite: they demonstrate the shape of the behaviour, and the reader
extends it. This is the same reason [[processing-order-is-not-a-structure]] holds — an enumeration
of what happens in each situation is bound to the situations enumerated, exactly as a description
organised by steps is bound to one execution.

## The symptom

**A list that grows by one entry per incident.** Its history is visible in its shape: entries that
are oddly specific, mutually overlapping, and phrased as exceptions to something.

The list is a genuine signal — every entry marks a real failure someone hit — but the wrong
response to it. The trigger was right and the shape was wrong: an observed failure does earn an
edit ([[effective-context-engineering]]), and the edit should have been an example rather than an
entry. The repair is therefore not to stop responding to incidents but to read the accumulated
entries for the pattern they share and replace them with one example that demonstrates it.

## The cost side

Examples are not free: they consume the same budget as everything else
([[attention-budget]]), so a set of examples is subject to the same minimality requirement as the
prose. The rule is not "prefer examples" but "prefer few good examples to many narrow ones" — and
diversity is what makes a small set sufficient, since two examples that differ only trivially
occupy budget for the coverage of one.
