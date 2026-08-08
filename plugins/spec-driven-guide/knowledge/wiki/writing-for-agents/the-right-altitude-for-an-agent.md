---
title: The right altitude for an agent
category: writing-for-agents
summary: Instructions fail at both ends — hardcoded brittle logic at one, vague guidance assuming shared context at the other — and the target is the band between them.
tags: [concept, altitude, agent-reader, failure-mode]
sources: [web-page-effective-context-engineering-for-ai-agents]
created: 2026-08-06
updated: 2026-08-06
---

Instructions written for a model reader have an altitude problem, and
[[effective-context-engineering]] names it outright:

> **System prompts** should be extremely clear and use simple, direct language that presents ideas
> at the *right altitude* for the agent. The right altitude is the Goldilocks zone between two
> common failure modes.
>
> — L43

**Too low.** "Engineers hardcoding complex, brittle logic in their prompts to elicit exact agentic
behavior. This approach creates fragility and increases maintenance complexity over time." The
instruction enumerates conditions and responses, and every situation the enumeration did not
anticipate is handled badly or not at all.

**Too high.** "Vague, high-level guidance that fails to give the LLM concrete signals for desired
outputs or falsely assumes shared context." The instruction sounds correct and decides nothing.

**The target.** "Specific enough to guide behavior effectively, yet flexible enough to provide the
model with strong heuristics to guide behavior."

## Why this matters beyond the agent genre

Most writing advice names one failure and treats its opposite as safety. This source names both,
and they map exactly onto the two ways a document about a decision goes wrong:

| Failure for an agent reader | Same failure in any document |
|---|---|
| Hardcoded brittle logic | Mechanism stated where an obligation belongs — [[processing-order-is-not-a-structure]] |
| Vague guidance assuming shared context | Obligation dissolved into generality; the reader cannot act |

The second column's second row has no page of its own in this wiki's other sources, and that is
telling: the tradition this wiki draws on is preoccupied with saying too much, and comparatively
silent about saying too little. The agent-reader literature is where the opposite failure is taken
seriously, because with a model reader it produces immediate, visible, wrong behaviour rather than
a slow misunderstanding.

## The phrase that makes it checkable

"Falsely assumes shared context" is the operative part. Vagueness is hard to judge; a *false
assumption of shared context* is not — it is a specific claim about a specific reader, and it can
be tested by giving the text to a reader who genuinely lacks that context and seeing what they do.

That test is the same one described in [[comprehensible-only-as-a-whole]], arrived at from the
opposite direction: there, a reader who needs outside knowledge reveals a leak between sections;
here, a reader who needs outside knowledge reveals an obligation the document failed to state.

Related: [[minimal-is-not-short]], which prevents this rule from being read as licence to cut.
