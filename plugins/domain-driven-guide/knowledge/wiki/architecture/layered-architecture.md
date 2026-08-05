---
title: Layered Architecture (applied to DDD)
category: architecture
summary: The traditional layered structure with the domain model isolated in its own layer; each layer couples only downward, Application Services stay thin, and Infrastructure-at-the-bottom creates a dependency problem that DIP later solves.
tags: [architecture-pattern, architecture, layers, application-service, infrastructure]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The **Layers Architecture** rigorously separates an application's concerns into well-defined layers,
each cohesive and depending only on the layers below. Evans' formulation, quoted in the chapter:
"Isolate the expression of the domain model and the business logic… Partition a complex program into
layers. Develop a design within each layer that is cohesive and that depends only on the layers below"
(raw L2929). In a DDD application the isolated domain model sits in the **Domain Layer**, with the
**User Interface** and **Application Layers** above it and the **Infrastructure Layer** below.

## Coupling rules

Each layer may couple only to itself and below. A **Strict Layers Architecture** allows coupling only to
the layer *directly* below; a **Relaxed Layers Architecture** allows any higher layer to couple to any
lower one. Because UI and Application Services both often need Infrastructure, "many, if not most,
systems are based on Relaxed Layers" (raw L2937). A lower layer may notify a higher one only indirectly,
via **Observer** or **Mediator** — "there is never a direct reference from lower to higher" (raw L2939).

## Responsibilities per layer

- **User Interface** — only view/request concerns; must not contain domain/business logic. UI
  validation is not the coarse-grained, deep-business validation that belongs in [[entity|Entities]]. A
  **Presentation Model** can keep the view from knowing domain objects.
- **Application Layer** — hosts [[application-service|Application Services]], the thin direct clients of
  the domain model. They coordinate operations on [[aggregate|Aggregates]] via **Repositories**, control
  transactions/security, and express use cases, but hold no business logic.
- **Domain Layer** — all business logic.
- **Infrastructure Layer** — persistence, messaging (JMS, SMTP, SMS), frameworks; the low-level
  technical facilities the higher layers reuse.

## The Infrastructure-at-the-bottom problem (failure/tension)

With Infrastructure at the bottom, a **Repository** *interface* defined in the Domain Layer needs an
*implementation* that uses persistence in Infrastructure. Implementing it in Infrastructure means
Infrastructure (below) references Domain (above), "which would violate the rules of Layers Architecture"
(raw L2982). Two awkward work-arounds: hide technical classes in an implementation **Module** (e.g.
`...domain.model.product.impl` holding `MongoProductRepository`), or implement the interfaces up in the
Application Layer (which "may seem a bit distasteful", raw L2988). The chapter notes their code "was
difficult to test" (raw L3002). The clean resolution is the [[dependency-inversion-principle]], which
leads on to [[hexagonal-architecture]].

## Failure mode

If Application Services grow beyond thin coordination "it is probably an indication that domain logic is
leaking into the Application Services, and that the model is becoming anemic" (raw L2976) — the
[[anemic-domain-model]] anti-pattern. Keep model clients very thin.

## Related

- [[application-service]] — the thin Application-Layer coordinator.
- [[dependency-inversion-principle]] — the fix for the Infrastructure-at-the-bottom problem.
- [[hexagonal-architecture]] — where the layering dissolves into inside/outside.
- [[anemic-domain-model]] — the failure a fat Application Layer signals.
- [[architecture-selection]] — how this style is one option among several.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
