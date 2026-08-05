---
title: Module Naming Conventions
category: building-blocks
summary: "How to name DDD Modules: a hierarchy from organization domain, to Bounded Context, to the domain / domain.model qualifiers — naming for the Ubiquitous Language, avoiding brand names, and the anemic-model risk of a separate domain.service peer."
tags: [reference, modules, naming, ubiquitous-language, packaging, layered-architecture, convention]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Because [[modules]] are a first-class part of the [[ubiquitous-language]], naming them is a modeling act, not a clerical one. The chapter lays out a hierarchical, dotted naming scheme (Java packages / C# namespaces) built up one meaningful segment at a time.

## Basic hierarchy: organization first

Module names are hierarchical, each level separated by a dot, beginning with the producing organization composed with its Internet domain name (top-level domain first):

```
com.saasovation   // Java
SaaSOvation        // C#
```

A unique top-level name "prevents namespace collision with third-party Modules ... or those caused when yours are consumed by others" (raw L8391). Most organizations have already settled on this convention; the guidance is simply to be consistent.

## Model segment: name the Bounded Context

The next segment identifies the [[bounded-context]] — basing it on the Context's name is the recommended choice:

```
com.saasovation.identityaccess
com.saasovation.collaboration
com.saasovation.agilepm
```

Two instructive rejections:

- **Over-long, literal names** (`identityandaccess`, `agileprojectmanagement`) were dropped as "unnecessary noise" — they name the Context exactly but add no value (raw L8409).
- **Brand / product names** (`idovation`, `collabovation`, `projectovation`) were rejected because brand names change (trademark, cultural fit) and often correlate poorly with the underlying Bounded Context. `idovation` "has almost no correlation to its Bounded Context" (raw L8424). The goal is to reflect the Ubiquitous Language — the name the *team* actually discusses — so name the Context, not the marketed product.

## The `domain` and `domain.model` qualifiers

A `domain` qualifier marks the Module as part of the domain, compatible with both a [[layered-architecture]] and a [[hexagonal-architecture]] (the "inside" of the application):

```
com.saasovation.identityaccess.domain
```

This level "may be devoid of interfaces/classes and serve only as a container for lower-level Modules" (raw L8436). Beneath it, `domain.model` is where model classes begin, and where reusable interfaces and abstract base classes live — SaaSOvation placed common types here such as `Entity`, `ConcurrencySafeEntity`, `IdentifiedDomainObject`, `IdentifiedValueObject`, `DomainEvent`, `DomainEventPublisher`, `DomainEventSubscriber`, and `DomainRegistry` (raw L8451-8459).

Why `domain.model` and not just `domain`? Because you model a domain, you do not build one:

> "Remember that we do not develop a domain. ... What we design and implement is a *model of a domain*. So when naming the ultimate Module of the model, `domain.model` seems most appropriate." (raw L8479)

## Optional `domain.service` peer — and its anemic-model risk

If you prefer to keep [[domain-service|domain services]] out of `domain.model`, create a peer package:

```
com.saasovation.identityaccess.domain.service
```

This is optional — it treats services as a medium-grained mini-layer or ring around the model. But it carries a warning:

> "be aware that this approach can quickly lead to Anemic Domain Model" (raw L8469)

See [[anemic-domain-model]]: pulling behavior out of Entities/Value Objects and into a service package tends to hollow out the model.

## Dropping the `model` level (and why you may regret it)

You *can* place concept Modules directly under `domain` (`com.saasovation.identityaccess.domain.conceptname`), eliminating a seemingly redundant level. The catch: if you later decide to add a `domain.service` sub-Module, you'll wish you had a matching `domain.model` for symmetry (raw L8477). Keeping `domain.model` from the start avoids that.

## Modules outside the model

Every non-model layer also needs named Modules, and the same "sub-divide only if it helps" restraint applies.

- **[[layered-architecture|Layered Architecture]]** stack: User Interface, Application, Domain, Infrastructure.
- **User Interface (REST):** separate the resource providers from pure presentation —
  ```
  com.saasovation.agilepm.resources
  com.saasovation.agilepm.resources.view
  ```
  RESTful resources produce bland representations (XML, JSON, HTML) with *no* presentation layout; layout comes from a different channel.
- **Application Layer:** optionally one Module per service type (`application.team`, `application.product`, `application.tenant`). But the Identity and Access Context had only a few Application Services and left them in one Module (`com.saasovation.identityaccess.application`). Modularize further only when you have "more than a few services, perhaps half a dozen or so" (raw L8644).

For the pattern these names serve, see [[modules]].
