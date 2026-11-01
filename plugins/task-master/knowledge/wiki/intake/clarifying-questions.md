---
title: Clarifying Questions
category: intake
summary: Read the repository first, then ask only what it cannot answer, about behaviour and failure, in terms the asker can answer; a question whose answer was in the code, or that the person cannot answer, is the sign it was wrong.
tags: [rule, intake, agents, clarification, evidence]
sources: [ambig-swe]
created: 2026-11-01
updated: 2026-11-01
---

# Clarifying Questions

When a request is missing something, the question sent back should be one that only the requester can answer and that the requester can actually answer. This rule comes from the Ambig-SWE analysis of what agents asked a simulated user. Applying it to the questions the plugin sends a person during intake is this wiki's transfer. The study observed coding agents during a run.

## The rule

Before asking, read the repository. Then ask only what it cannot answer, phrased around expected behaviour and concrete failure, and not around implementation.

## Sign of violation

- **The answer was in the repository.** The authors found that "Deepseek and Qwen ask immediately, including questions about implementation details recoverable from code." (L240).
- **The person cannot answer.** The reply amounts to not knowing, because the question went below what the requester knows. The authors found that "Deepseek’s highly specific implementation questions often exceed user knowledge, wasting interaction turns." (L242).
- **The question is general and yields nothing.** The authors' example is "Are there any existing workarounds?" (L238). In the sampled exchanges the matching question, "Any known workarounds or temporary fixes?", was answered "I don’t have that information." (L539).

## Why

The authors report a comparison of strategies on the same benchmark:

> Claude Sonnet models (3.80-4.03 questions) achieve information gain comparable to Deepseek and Qwen (4.57-6.02 questions) by exploring the codebase first, then asking only what cannot be independently discovered.
>
> — [[ambig-swe]], L240

The authors also describe what the better questions were about:

> Claude targets behavioral aspects and concrete failure modes instead, better matching realistic user knowledge.
>
> — [[ambig-swe]], L242

This wiki reads those as two independent filters on a question: is the answer unavailable elsewhere, and is the person able to give it. A question failing either wastes a turn. The authors draw the same three-way conclusion: "Effective clarification balances question quantity (avoiding user overwhelm), exploration efficiency (discovering what can be inferred before asking), and answerability (matching specificity to user knowledge)." (L244).

## Numbers and their conditions

Information gain is cosine distance between embeddings, which the authors concede weighs all information equally (L264). Claude Sonnet 4 scored 0.171 with 4.03 questions on average and Qwen 3 Coder 0.179 with 6.02 (L230, L244). More questions did not produce more resolved issues for Qwen 3 Coder: "this high volume does not translate to better performance" (L238). Do not quote the paper's "50% fewer" for this pair, because the figures it gives come to about 33% fewer (see [[ambig-swe]]). All of this uses a simulated user who answers only from the issue, is possibly more cooperative than a real one (L264), and is an LLM.

## Cost

Exploring first spends steps. The study found no efficiency gain from interaction at all (L159), so this wiki expects the rule to buy better answers and fewer interruptions, and not a shorter run. There is also a cost in not asking: a task-only fact has to come from somewhere, and [[recoverable-versus-task-only-facts]] says which facts must be obtained.

## Agent executor note

The evidence is about agents asking. Whether the rule fits a person sending questions was not tested. It also applies to the plugin's own intake, because the plugin is an agent asking a person, and the person's time is the budget it spends.

## Related

The questions are about a task that may be underspecified: [[underspecified-task]]. A requester who cannot say how to test a result is a related sign: [[testable-acceptance]].
