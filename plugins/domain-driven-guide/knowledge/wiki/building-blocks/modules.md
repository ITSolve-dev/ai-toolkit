---
title: Modules
category: building-blocks
summary: Named containers for highly cohesive domain classes with low coupling between them; a first-class modeling element whose names belong to the Ubiquitous Language, designed by domain meaning rather than mechanically.
tags: [pattern, tactical-pattern, modules, cohesion, coupling, ubiquitous-language, packaging]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Module** is a named container for domain object classes that are highly cohesive with one another, chosen so that coupling between classes in *different* Modules stays low. It is the DDD name for what your language already gives you: Java calls them packages, C# calls them namespaces, and Ruby's `module` construct effects namespaces for classes. The DDD point is not the language mechanism (which you already know) but that Modules are a **modeling** decision, not a filing decision.

> "In a DDD context, Modules in your model serve as named containers for domain object classes that are highly cohesive with one another. The goal should be low coupling between the classes that are in different Modules." (raw L8348)

## Modules as first-class citizens

Because Modules are not "bland or generic storage compartments," their names carry design intent and belong to the [[ubiquitous-language]]. Evans' guidance, quoted in the chapter:

> "Choose Modules that tell the story of the system and contain a cohesive set of concepts. ... Give Modules names that become part of the Ubiquitous Language[;] Modules and their names should reflect insight into the domain." (raw L8350)

Treat them with the same care as any other model element:

> "View Modules as first-class citizens of the model, and strive to create ones with as much meaning and naming consideration as is given to Entities, Value Objects, Services, and Events." (raw L8360)

This first-class status has a corollary: **rename and re-home aggressively**. Be as bold about renaming an existing Module as about creating a new one, and move freshened domain concepts into whatever Module today's insight calls for. The chapter frames Module refactoring as ongoing due diligence — the SaaSOvation team, "having an agile mentality, was committed to refactoring Modules with due diligence" as the context evolved (raw L8608).

## Design by meaning, not by mechanics (the kitchen analogy)

The central design rule: group by what things *mean in the domain*, not by incidental physical or technical attributes. The chapter's kitchen analogy makes this concrete. A well-organized kitchen groups forks, knives, and spoons into a `placesettings` set — and you would even put `Serviette` there, "proving that it's not only being made of metal that qualifies an object to be a part of the `placesettings` Module" (raw L8368). What you would *not* do is organize mechanically — putting all fragile things together (vases with fine teacups) or all sturdy things together (a steel meat tenderizer with fine cutlery) — because then you must *remember* arbitrary groupings.

> "it would be less helpful to modeling place settings if we had separate Modules named `pronged`, `scooping`, and `blunt`." (raw L8368)

**Failure mode:** designing Modules mechanically stifles modeling creativity. A mechanical scheme (group by lifecycle, by base type, by "is it fragile") produces containers that carry no domain insight and force readers to memorize placement rules. The symptom is Module names that describe a *technical* trait rather than a domain concept.

## Traditional Modules vs. deployment modularity

DDD Modules are distinct from — but complementary to — the newer *deployment* modularity: packaging loosely coupled, logically cohesive software into a versioned deployment unit (in the Java world, JAR files assembled by version via OSGi bundles or Java 8 Jigsaw modules).

> "These kinds of modules/bundles are a bit different from DDD Modules, but they can complement each other. ... it's the loosely coupled design of your DDD Modules that will contribute to your ability to bundle with OSGi or modularize to Jigsaw." (raw L8370)

So the low-coupling discipline of DDD Modules is what later makes coarse-grained deployment bundling feasible; get the model-level modularity right and the packaging follows.

## Worked example: the Agile PM Context

SaaSOvation's [[core-domain]], the *Agile Project Management Context*, uses three top-level Modules under `domain.model`: `tenant`, `team`, and `product`.

- **`tenant`** holds a single [[value-object]], `TenantId`, identifying a tenant that originates in the *Identity and Access Context*. Nearly every other Module depends on it (it segregates one tenant's objects from another's), yet **the dependency is acyclic** — `tenant` depends on nothing.
- **`team`** holds three [[aggregate]] roots — `ProductOwner`, `Team`, `TeamMember` — plus a [[domain-service]] interface, `MemberService`, which is a front end for an [[anticorruption-layer]] that synchronizes team members (eventually consistent, out of band) with identities and roles in the *Identity and Access Context*. All three roots reference `TenantId`.
- **`product`** is a parent Module with three children — `backlogitem`, `release`, `sprint` — each holding one aggregate root (`BacklogItem`, `Release`, `Sprint`) alongside the parent's `Product` root. This is where Scrum's core lives, and the Modules read naturally as Ubiquitous Language: "product," "product backlog item," "product release," "product sprint" (raw L8549).

### The trade-off: organization vs. cross-Module coupling

Why split only four closely related Aggregates across four Modules? Because each Aggregate drags along many more classes — contained Entities (`Task` under `BacklogItem`), Value Objects, and Domain Events — roughly **60 classes and interfaces** total. Cramming all of them into one `product` Module would look disorganized.

> "The team opted for organization over crossModule coupling concerns." (raw L8551)

The coupling cost is real and named: `BacklogItem` references `ProductId`, and because each `Product` acts as a [[factory]] for `BacklogItem`, `Release`, and `Sprint` instances, the `product`↔`backlogitem` dependency is actually **bidirectional**, not acyclic. The team accepts this because the sub-Modules are *children* of `product`, where dependency rules can be relaxed:

> "Here the trade-off is organizational strengths over coupling." (raw L8590)

They rejected the alternative of loosening coupling with a generic `Identity` type for every id (`backlogItemId`, `productId`, `teamId`, `tenantId` all typed `Identity`). It would have achieved looser coupling but "opened up the potential for bugs in code where each `Identity` type could not be distinguished from the others" (raw L8606) — a concrete argument for typed identity Value Objects over a generic id.

## Related

For how Modules are *named* (hierarchy, Bounded Context segment, the `domain.model` qualifier, layers outside the model), see [[module-naming-conventions]]. For choosing the thin boundary of a Module over the thick boundary of a Bounded Context, see [[module-before-bounded-context]].
