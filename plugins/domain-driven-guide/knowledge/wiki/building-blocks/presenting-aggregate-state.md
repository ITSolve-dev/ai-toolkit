---
title: Presenting Aggregate State to the UI
category: building-blocks
summary: How to read domain data out to a view without coupling clients to Aggregate internals — DTO Assemblers, Mediator/double-dispatch, Domain Payload Objects, and use-case-shaped representations rather than Aggregate-shaped ones.
tags: [guidance, aggregate, dto, presentation, view-model, mediator, use-case, coupling]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A view usually needs "views of data richer than is required to accomplish the direct task," so it renders properties of **multiple** [[aggregate|Aggregate]] instances even though the user typically mutates just one (raw L13627). The design question is how to expose that state **without coupling presentation clients to the internal structure of your Aggregates**. Several techniques exist; the DDD-relevant lessons are the coupling rule and the use-case-orientation rule, not the plumbing.

## The coupling rule

Whatever technique reads Aggregate state, "Think carefully about how to reveal state without revealing too much about the internal shape or structure of the Aggregates. Try to eliminate a client's coupling to all internal parts of an Aggregate. Should you allow clients... to navigate deeply into Aggregates? That can be a bad idea since it tightly couples each client to a specific Aggregate implementation" (raw L13641). This is the same reasoning behind small aggregate boundaries — see [[aggregate]].

## Techniques (in order of DDD-friendliness)

- **DTO + DTO Assembler** [Fowler, P of EAA]. The [[application-service|Application Service]] uses [[repository|Repositories]] to load the needed Aggregates and a DTO Assembler maps their attributes into one flat DTO the view reads. It resolves lazy loads (the Assembler touches every part it needs) and serializes cleanly across a physical tier boundary. But the DTO was "originally designed to deal with a remote presentation tier"; if your presentation tier is **not** remote, "this pattern many times leads to accidental complexity... as in YAGNI" — extra classes that resemble but don't match domain objects, plus GC pressure from large short-lived objects in a single-VM app (raw L13639).
- **Mediator / Double-Dispatch / Callback** [Gamma]. Instead of exposing structure, the Aggregate *publishes* its state to a client-supplied interface: the client passes a `BacklogItemInterest` and the Aggregate calls `anInterest.informSummary(...)`, `informStory(...)`, etc. (raw L13645-13675). "The trick is to not wed the Mediator's interface to any sort of view specification, but to keep it focused on rendering Aggregate states of interest." Some consider this outside an Aggregate's responsibility, others a natural extension — "such trade-offs must be discussed by your technical team members" (raw L13675).
- **Domain Payload Object (DPO)** [Vernon]. When the presentation tier is *not* remote, hold references to whole Aggregate instances in a lightweight container rather than copying attributes into a DTO. Smaller memory footprint and easier to design, "[s]ince the Aggregate instances must be read into memory anyway" (raw L13687). Caveat: because it holds whole Aggregates, lazy-loaded collections are unresolved when the read-only transaction commits — accessing them later throws. Fix with eager loading or a **Domain Dependency Resolver** [Vernon] (a [[factory|Strategy]] per use-case flow that forces the needed lazy loads before commit) (raw L13691-13693).

## The use-case-orientation rule

For REST or any representation: "It is very important to create representations that are based on use case, not on Aggregate instances" (raw L13697). Think of a set of RESTful resources as a separate **View Model / Presentation Model** [Fowler]. "Resist the temptation to produce representations that are a one-to-one reflection of your domain model Aggregate states... Otherwise your clients will have to understand your domain model... and you will lose all benefits of abstraction" (raw L13697). The [[use-case-optimal-query]] technique and [[cqrs|CQRS]] follow directly from this rule.

## Adapting the Ubiquitous Language to view frameworks

A **Presentation Model** (a GoF Adapter) is worth a mention because of one DDD-specific benefit: the domain model favors fluent names that reflect the [[ubiquitous-language|Ubiquitous Language]] (`summary()`, `story()`), while many UI frameworks require JavaBean getters (`getSummary()`, `getStory()`). The Presentation Model "can adapt Aggregates that don't support a JavaBean interface of getters to user interface frameworks that require getters," eliminating that impedance mismatch (raw L13759). It must not become "a heavy-lifting **Facade** around the Application Services or the domain model" (raw L13785) — it delegates to the Application Service, it does not become one.

## Disparate clients: Data Transformers

When one Application Service serves an RIA, a thick client, REST, and messaging, pass a **Data Transformer** whose concrete type the client chooses (`CalendarWeekXMLDataTransformer`, `...JSON...`, `...CSV...`); the service double-dispatches to produce the format (raw L13707-13743). The alternative is a Ports-and-Adapters output port — see the decoupled-output section of [[application-service]].

## Related

[[aggregate]] · [[application-service]] · [[use-case-optimal-query]] · [[cqrs]] · [[repository]] · [[factory]] · [[ubiquitous-language]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
