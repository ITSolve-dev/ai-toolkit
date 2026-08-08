---
title: Attention budget
category: writing-for-agents
summary: A model reader's ability to use what it is given degrades as the amount grows — so for this reader, economy is a mechanical constraint rather than a stylistic preference.
tags: [concept, agent-reader, constraint, reasoning]
sources: [web-page-effective-context-engineering-for-ai-agents]
created: 2026-08-06
updated: 2026-08-06
---

Every other argument in this wiki for saying less is about the future: detail goes stale, changes
propagate, documents rot. For a model reader there is an argument about the present as well —
material that is present but excessive degrades the use of the material that matters.

> as the number of tokens in the context window increases, the model's ability to accurately recall
> information from that context decreases. […] Context, therefore, must be treated as a finite
> resource with diminishing marginal returns. Like humans, who have limited working memory
> capacity, LLMs have an "attention budget" […] Every new token introduced depletes this budget by
> some amount.
>
> — [[effective-context-engineering]], L29-L31

The stated mechanism is architectural: attention relates every element to every other, giving n²
pairwise relationships for n elements, and "as its context length increases, a model's ability to
capture these pairwise relationships gets stretched thin" (L33-L35). Models are also trained on
distributions where short sequences dominate, so they have "less experience with, and fewer
specialized parameters for, context-wide dependencies".

The post is careful about the shape of the effect: "These factors create a performance gradient
rather than a hard cliff: models remain highly capable at longer contexts but may show reduced
precision for information retrieval and long-range reasoning" (L37). A gradient, not a limit —
which means there is no length at which a document becomes safe, only a continuous cost.

## What follows for writing

**Irrelevant content is not neutral.** In a document read by a person, a paragraph that adds
nothing is skipped. For this reader it competes: it consumes budget and dilutes what surrounds it.
A section retained "just in case" has a cost paid on every read.

**The cost is paid by the whole document, not by the passage.** This is what makes it different
from ordinary verbosity. Adding a stale enumeration does not merely waste its own space; it reduces
the precision with which everything else is recalled.

**And the corrective still applies.** None of this argues for cutting obligations —
[[minimal-is-not-short]] holds, because an underspecified instruction produces wrong behaviour
immediately, which is worse than diluted attention.

## Its limit as an argument

This reasoning is specific to a model reader, and its specifics are perishable: the degradation
profile is a property of current architectures and training distributions, both of which move. The
durable part is the shape of the claim — that for this reader, added material has a cost that is
paid by the rest of the document — not the particular measurements behind it.

For a human reader, the older arguments carry the weight instead: [[information-hiding]] and
[[the-changeability-test]] say to omit the same material for entirely different reasons.
