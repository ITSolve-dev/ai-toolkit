---
title: Domain Model
category: building-blocks
summary: A software model of one specific business domain — usually an object model whose objects carry both data and behaviour with accurate business meaning; kept small, focused, and useful rather than realistic.
tags: [concept, domain-model, building-blocks, core-domain, ubiquitous-language]
sources: [book-implementing-ddd-vaughn-vernon, web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

A **domain model** is a software model of one very specific business domain — the artifact at the heart
of practicing DDD. It is usually realized as an object model:

> "Often it's implemented as an object model, where those objects have both data and behavior with
> literal and accurate business meaning." (raw L826)

The *data-and-behaviour* clause is the whole point: an object model that is only data (only accessors)
is not a domain model but a data model — see [[anemic-domain-model]].

## Small, focused, and per-context

DDD does not build one enterprise-spanning model. "With DDD your domain models will tend to be
smallish, very focused" and "you never try to model the whole business enterprise with a single, large
domain model" (raw L828). Each model lives inside one [[bounded-context]], where its terms carry a
single agreed meaning drawn from that context's [[ubiquitous-language]]. Creating "a unique, carefully
crafted domain model at the heart of a core, strategic application or subsystem is essential to
practicing DDD" (raw L828) — so the biggest modeling investment goes to the [[core-domain]].

## Useful, not realistic

A domain model is not an attempt to mirror the real world:

> "this does not mean that effort is spent on modeling the 'real world.' Rather, DDD delivers a model
> that is the most useful to the business. Sometimes useful and realistic models happen to intersect,
> but to the degree that they diverge, DDD chooses useful." (raw L904)

Elsewhere: "It is not about creating a real-world model, as in trying to mimic reality" (raw L1337).
The goal is a faithful codification of the domain experts' *mental model*, refined continuously by an
agile, iterative process for as long as the business needs it.

## The design is the code

A recurring DDD tenet: "the design is the code and the code is the design" (raw L1132); "whiteboard
diagrams aren't the design, just a way to discuss the challenges of the model" (raw L1132).
Consequently the model is built test-first and behaviour-first — write a client-style test that shows
how a domain object should be used, create just enough of the object to compile, then refactor until
the behaviour and its naming express the [[ubiquitous-language]] (raw L1556–L1568). This keeps design
and implementation from diverging and lets nontechnical domain experts read the demonstrative tests to
confirm the model matches their meaning.

## Building blocks

Inside one Bounded Context the model is composed from DDD's tactical building blocks — [[aggregate]]s,
[[entity]]s, [[value-object]]s, domain **Services**, [[domain-event]]s, and others (raw L1343).
Tactical modeling is "generally more complex than strategic modeling" and warrants the extra investment
mainly for the Core Domain — see [[when-to-use-ddd]] for the decision criteria.

## The Cosmic Python view — behavior-first, isolated from infrastructure

*Architecture Patterns with Python* frames the same building block through the lens of *isolation*.
Its precise definitions are worth keeping: "The *domain* is a fancy way of saying *the problem you're
trying to solve*" (raw L551) and "A *model* is a map of a process or phenomenon that captures a useful
property" (raw L558). Because a model is a deliberately partial map, predictions outside its intended
cases aren't "wrong," just out of its domain — the same *useful, not realistic* stance Vernon takes
above. And it already exists before any code: "The domain model is the mental map that business owners
have of their businesses" (raw L567); the programmer's job is to surface it in the experts' own words
(the [[ubiquitous-language]]) and encode it — "Understanding the domain model takes time, and patience,
and Post-it notes" (raw L599).

**Behavior first, storage second.** The defining stance is that modeling drives persistence, not the
reverse. Many developers "immediately start to build a database schema, with the object model treated as
an afterthought. This is where it all starts to go wrong. Instead, *behavior should come first and drive
our storage requirements*" (raw L485-488), because "our customers don't care about the data model. They
care about what the system *does*" (raw L488). "Most developers have never seen a domain model, only a
data model" (raw L478) names exactly the gap — a data model records shape, a domain model encodes
behavior. Starting from the schema is the road to the [[anemic-domain-model]].

**The model is the "high-level modules."** Held against the [[dependency-inversion-principle]], the domain
model *is* the high-level modules: "the code that your organization really cares about," the "functions,
classes, and packages that deal with our real-world concepts" (raw L418, L422) — patients and trials, or
trades and exchanges. Everything the business does not care about (filesystems, sockets, SMTP/HTTP, cron
vs. Kubernetes) is low-level detail that must stay *out*. Isolation is the whole game: the book's aim is
to "build an architecture for which specific technology choices become minor implementation details"
(raw L147), so the model can be exercised by fast unit tests with no external dependencies. The
supporting patterns exist to protect that isolation — [[repository]], the [[application-service|service
layer]], and Unit of Work are "three closely related and mutually reinforcing patterns that support our
ambition to keep the model free of extraneous dependencies" (raw L159).

**The worked model (allocation).** An `OrderLine` (a [[value-object]]) is allocated against a `Batch`
(an [[entity]]) of stock in the warehouse or in transit; allocation reduces available quantity; the
coordinating operation that picks a batch is a [[domain-service]]; "out of stock" is a
[[domain-exception]]. The book concedes the toy example "is too trivial to bother with DDD" (raw L763),
but the precision pays off as real complexity accrues (future-dated deliveries, on-demand SKUs,
region-restricted allocation): "A real business in the real world knows how to pile on complexity faster
than we can show on the page!" (raw L763). Modeling precisely — plus the encapsulation and layering
around the model — is "what will help us to avoid a ball of mud" (raw L765); see [[big-ball-of-mud]].

## Related

- [[bounded-context]] — the boundary one domain model lives inside.
- [[ubiquitous-language]] — the Language the model expresses.
- [[anemic-domain-model]] — a data model masquerading as a domain model.
- [[core-domain]] — where the biggest modeling investment goes.
- [[when-to-use-ddd]] — when a behavioural domain model is worth building.
- [[dependency-inversion-principle]] — the principle that keeps the model free of infrastructure.
- [[big-ball-of-mud]] — what you get when business logic spreads across the layers.
- [[entity]] · [[value-object]] · [[domain-service]] · [[domain-exception]] — the tactical building blocks that compose it.
- [[book-implementing-ddd-vaughn-vernon]], [[web-page-cosmic-python-book]] — source summaries.
