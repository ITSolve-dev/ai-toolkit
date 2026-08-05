---
title: Module before Bounded Context
category: context-mapping
summary: A sizing heuristic — when domain terminology is fuzzy and a contextual boundary is unclear, first keep concepts together behind the thin boundary of a Module rather than splitting into the thick boundary of a separate Bounded Context.
tags: [heuristic, modules, bounded-context, decision-rule, strategic-design, boundaries]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Module before Bounded Context** is a decision rule for how coarsely to divide a domain model. When it is unclear whether two clusters of concepts truly belong in separate models, prefer the *thinner* boundary of a [[modules|Module]] over the *thicker* boundary of a [[bounded-context|Bounded Context]].

> "In cases where terminology is fuzzy and it is not clear if contextual boundaries should be created, first consider the possibility of keeping them together. This approach will use the thinner boundary of Module to separate, rather than the thicker one of Bounded Context." (raw L8648)

## Why the linguistics decide

The deciding signal is language. Sometimes "the linguistics of the true, actual domain will jump out at you" — the same term clearly means two different things, or two teams speak two dialects — and separate models are justified. Sometimes the terminology is merely fuzzy, and a premature split invents a boundary the domain does not actually have.

The two boundaries differ sharply in cost:
- A **Module** is a thin, in-model partition: same model, same [[ubiquitous-language]], concepts can still reference each other directly.
- A **Bounded Context** is a thick, between-models partition: its own model and Ubiquitous Language, requiring translation, integration, and often an [[anticorruption-layer]] to talk across it.

Because the Bounded Context boundary is expensive, you should not pay for it on a hunch. Reach for a Module first; promote to a Bounded Context only when the language demands it.

## Do not substitute one for the other

The rule cuts both ways — it restrains over-splitting into Contexts without discouraging legitimate multiple Contexts:

> "Bounded Contexts are not meant to be used as a substitute for Modules. Use Modules to modularize cohesive domain objects, and to separate those that are not cohesive or less cohesive." (raw L8652)

> "This does not mean that we rarely use multiple Bounded Contexts. Boundaries between models are clearly justified, as the linguistics demand." (raw L8650)

## Failure modes

- **Over-eager Bounded Contexts** (using a Context where a Module would do): every fuzzy grouping becomes its own model, forcing needless integration plumbing, translation, and anticorruption layers between concepts that actually share one language. The symptom is heavyweight boundaries around concepts the team still discusses in one vocabulary.
- **Under-splitting** (forcing genuinely distinct languages into one model behind Modules): a single model tries to serve two conflicting meanings of the same term, producing a leaky, overloaded model — the classic pressure that a true Bounded Context split relieves.

See [[modules]] for the thin boundary itself and [[bounded-context]] for the thick one.
