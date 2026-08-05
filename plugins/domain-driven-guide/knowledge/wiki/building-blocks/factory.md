---
title: Factory
category: building-blocks
summary: A domain object whose job is to encapsulate the complex, invariant-enforcing creation of an Aggregate or complex object, hiding concrete classes and assembly detail from clients.
tags: [pattern, factory, building-blocks, tactical-design, creation, invariants]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Factory** in Domain-Driven Design is the model element responsible for encapsulating the creation of complex objects and [[aggregate|Aggregates]]. It exists so that clients never have to reference the concrete classes being instantiated or reproduce the assembly logic needed to build a valid whole. Factory is one of the better-known DDD patterns and overlaps with the GoF patterns **Abstract Factory**, **Factory Method**, and **Builder**; DDD's contribution is not new mechanics but a focus on using them to keep the model expressive and its invariants protected.

## Primary motivations

Vernon quotes Evans on the three reasons to introduce a Factory:

> Shift the responsibility for creating instances of complex objects and AGGREGATES to a separate object, which may itself have no responsibility in the domain model but is still part of the domain design. Provide an interface that encapsulates all complex assembly and does not require the client to reference the concrete classes of the objects being instantiated. Create entire AGGREGATES as a piece, enforcing their invariants. (raw L9604)

The throughline: **create the whole thing at once, in a valid state, without leaking construction details.** A Factory lets a client pass only basic parameters — often [[value-object|Value Objects]] — and receive a correctly assembled Aggregate back.

## Two forms

Vernon distinguishes two structural placements, which matter for how the Factory shows up in the model:

- **A pure Factory** — a dedicated object whose only purpose is to instantiate a specific Aggregate type. It "will have no other responsibilities and will not even be considered a first-class citizen of the model. It is only a Factory." (raw L9606)
- **A Factory Method on an existing model object** — e.g. an [[aggregate|Aggregate Root]] that exposes a method producing another Aggregate type. Here the host's primary responsibility is still its own Aggregate behavior; the Factory Method is just one of those behaviors. Vernon notes this "is what tends to occur more frequently in my examples" (raw L9606). See [[factory-method-on-aggregate-root]].

A third form places the Factory on a [[domain-service|Service]], used mostly when [[bounded-context|integrating Bounded Contexts]] — see [[factory-on-service]].

## When to reach for one

- **Non-trivial assembly.** Building a valid instance requires wiring several objects together or enforcing invariants across them.
- **Sensitive construction state.** Even Aggregates with otherwise simple construction can need a Factory to protect details that must never be wrong. Vernon's canonical example is multitenancy: "If an Aggregate instance were created under the wrong tenant, giving it the wrong `TenantId`, it could be disastrous." (raw L9608) A carefully designed Factory Method guarantees tenancy and association identities are set correctly.
- **Ubiquitous Language expressiveness.** A well-named behavioral method expresses the [[ubiquitous-language|Ubiquitous Language]] "in ways not possible through constructors alone" (raw L9610). When the name reads like the domain (e.g. *Calendars schedule calendar entries*), that is itself a strong case for a Factory Method.

## Abstract Factory and class hierarchies

The classic Abstract Factory use is creating objects of different concrete types within a class hierarchy from a few basic client-supplied parameters. Vernon does not demonstrate it (his sample domains have no such hierarchies) and issues a pointed caution: if you plan to model class hierarchies, review the discussion under [[repository|Repositories]] first and "be prepared for the potential for pain that could result" (raw L9620).

## Trade-offs and failure modes

- **Not every construction needs a Factory.** If construction is simple and carries no sensitive or invariant-laden state, a plain constructor is fine; a Factory adds indirection for no gain.
- **A Factory that hides too little.** If a required collaborator remains awkward to build (Vernon's `Set<Invitee>` example), the client burden isn't really removed — that awkwardness "may be pointing toward the creation of a dedicated Factory" for that part (raw L9768).
- **Performance cost when the Factory is a method on a loaded Aggregate** — see the trade-off detailed in [[factory-method-on-aggregate-root]].

## Related

[[aggregate]] · [[value-object]] · [[ubiquitous-language]] · [[domain-service]] · [[entity]] · [[factory-method-on-aggregate-root]] · [[factory-on-service]] · [[repository]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
