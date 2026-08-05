---
title: Verbs, Not Nouns
category: context-mapping
summary: A strategic-decomposition heuristic — carve a system into services / bounded contexts by business process (verbs) rather than by data entity (nouns), so each resulting context is a consistency boundary integrated via events.
tags: [heuristic, strategic-design, bounded-context, decomposition, consistency-boundary, event-driven, microservices, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Verbs, Not Nouns

**Verbs, not nouns** is a strategic-decomposition heuristic for carving a large system into services or [[bounded-context|bounded contexts]]: split by *business process* — a verb such as *ordering* or *allocating* — rather than by *data entity* — a noun such as Orders, Batches, Products, or Customers. Cosmic Python offers it as the antidote to the noun-based split that reliably produces a [[distributed-ball-of-mud]].

## The naive noun-based split

Engineers migrating a monolith to microservices have a "first instinct... to split their system into *nouns*" (raw L5129) — one service per business thing, each exposing a CRUD HTTP API. In the book's example this even names the system after a noun, *Batches*, "instead of *Allocation*" (raw L5135). It "works *fine* for systems that are very simple, but it can quickly degrade into a distributed ball of mud." (raw L5155)

The tell that the axis is wrong: business logic has no natural home. When water-damaged stock must be discarded, restocked, and possibly reallocated, the question "Where does this logic go?" (raw L5160) has no clean answer — whichever noun-service you bolt it onto, the dependency graph tangles.

## Model the verb

> "We should think in terms of verbs, not nouns. Our domain model is about modeling a business process. It's not a static data model about a thing; it's a model of a verb." (raw L5188)

So "instead of thinking about a system for orders and a system for batches, we think about a system for *ordering* and a system for *allocating*" (raw L5190). Framed this way "it's a little easier to see which system should be responsible for what." (raw L5194) The *ordering* system's job is only that "when we place an order, the order is placed. Everything else can happen *later*, so long as it happens." (raw L5196)

## Services as consistency boundaries

The move is the same segregation-of-responsibilities process used to design [[aggregate|aggregates]] and commands (raw L5199):

> "Like aggregates, microservices should be *consistency boundaries*. Between two services, we can accept eventual consistency, and that means we don't need to rely on synchronous calls. Each service accepts commands from the outside world and raises events to record the result. Other services can listen to those events to trigger the next steps in the workflow." (raw L5201)

Each verb-system is thus internally consistent and integrated with its neighbours through [[internal-vs-external-events|events]], not synchronous HTTP calls. This is why the heuristic sits at the boundary between tactical and strategic design: the same instinct that keeps an [[aggregate]] a transactional consistency boundary keeps a service one.

## Trade-offs

Why the verb-split plus asynchronous messaging beats noun-services wired by HTTP:

- **Independent failure** — "we can still take orders if the allocation system is having a bad day." (raw L5213)
- **Local change** — "If we need to change the order of operations or to introduce new steps in the process, we can do that locally." (raw L5215)

The cost is eventual consistency and the messaging problems that ride along with it (ordering, idempotency, reliability) — see [[internal-vs-external-events]].

## See also

[[distributed-ball-of-mud]] · [[aggregate]] · [[bounded-context]] · [[internal-vs-external-events]] · [[consistency-boundary]] · [[event-driven-integration]]
