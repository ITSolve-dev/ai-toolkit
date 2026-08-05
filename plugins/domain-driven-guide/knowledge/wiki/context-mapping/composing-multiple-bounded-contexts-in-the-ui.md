---
title: Composing Multiple Bounded Contexts in the UI
category: context-mapping
summary: When one user interface must present several domain models at once — using a single Application Layer to aggregate them — and the decision of when that composition has quietly become a new Bounded Context.
tags: [guidance, bounded-context, anticorruption-layer, anemic-domain-model, application-layer, ui-composition, context-mapping]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Integrating an upstream model into a downstream one (translating its concepts into the downstream [[ubiquitous-language|language]] via an [[anticorruption-layer|Anticorruption Layer]]) is different from **composing** several models into one unified presentation. Sometimes a single user interface must show, say, a *Products Context*, a *Discussions Context*, and a *Reviews Context* together, and "[t]he user interface should not be aware that it is composing multiple models" (raw L14179).

## Prefer a single Application Layer as the composition point

Two structural options (raw L14185-L14189):

- **Multiple Application Layers** (portal–portlet style) — each with its own UI components tied to one underlying model. Harder to harmonize disparate layers along a single use-case flow.
- **A single Application Layer** that aggregates objects from each model into cohesive shapes the UI needs. "Since the Application Layer manages use cases, it may be easiest to create a single Application Layer as the actual source of model composition... Services in that single layer are devoid of business domain logic. It will only serve to aggregate objects from each model." Modules are then named for the composition's purpose, e.g. `com.consumerhive.productreviews.presentation` and `...application`.

## The hidden Bounded Context

The important DDD insight is a warning disguised as an observation. "Isn't this Application Layer really serving as a new domain model with a built-in **Anticorruption Layer**? Yes, it is basically a new bargain-basement [[bounded-context|Bounded Context]]. Here the Application Services manage a merger of various DTOs, which mimic a sort of [[anemic-domain-model|Anemic Domain Model]]. It is a bit of a **Transaction Script** approach that models the Core Domain" (raw L14203).

In other words, a composition layer that starts as "just aggregating objects" silently accretes Core Domain modeling — but as an anemic, procedural model rather than a real one. That may be an acceptable, deliberate trade-off for a minor system; it is a smell for an important one.

## The decision to draw

"Where do we draw the line between composing multiple Bounded Contexts into a single user interface, and creating a new, clean Bounded Context with a unified domain model?" (raw L14221). If the composition is really crying out for a unified object model, promote it to a genuine [[bounded-context|Bounded Context]] with proper tactical modeling (e.g. `...domain.model.product`, `...domain.model.discussion`, `...domain.model.review`). Guidance for the call:

- Apply the same criteria used to justify any [[bounded-context]] split — linguistic boundaries, team ownership, rate of change.
- "[W]e must not treat such decisions arbitrarily... In the end the best approach is the one that benefits the business the most" (raw L14221).
- A less significant system tolerates the bargain-basement composition; a Core Domain deserves a real model rather than a Transaction Script over merged DTOs.

## Related

[[bounded-context]] · [[anticorruption-layer]] · [[anemic-domain-model]] · [[application-service]] · [[core-domain]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
