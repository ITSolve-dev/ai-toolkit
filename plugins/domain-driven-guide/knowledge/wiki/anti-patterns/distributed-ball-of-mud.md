---
title: Distributed Ball of Mud
category: anti-patterns
summary: The failure mode where noun-based (microservice-per-table, anemic) decomposition plus synchronous HTTP integration produces a tangled, cyclic dependency graph and temporal coupling, so failures cascade across service boundaries.
tags: [anti-pattern, failure-mode, temporal-coupling, coupling, anemic-domain-model, microservices, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Distributed Ball of Mud

The **Distributed Ball of Mud** is the distributed-systems form of the [[big-ball-of-mud|Big Ball of Mud]]: a service topology with no clean boundaries, where every business workflow threads through every service and failures cascade across service lines. Cosmic Python names it as the antipattern that noun-based decomposition (see [[verbs-not-nouns]]) and synchronous HTTP integration reliably produce.

## Cause 1 — microservice-per-table over anemic models

> "This style of architecture, where we create a microservice per database table and treat our HTTP APIs as CRUD interfaces to anemic models, is the most common initial way for people to approach service-oriented design." (raw L5153)

It "works *fine* for systems that are very simple, but it can quickly degrade into a distributed ball of mud." (raw L5155) The models behind each service are [[anemic-domain-model|anemic]] — data holders whose behavior has leaked out into orchestration between services.

## Cause 2 — a tangled dependency graph

With noun-services, different workflows drive services in conflicting directions. To allocate stock, Orders drives Batches drives Warehouse; but to handle a warehouse problem "our Warehouse system drives Batches, which drives Orders." (raw L5167) The result: "now our dependency graph is a mess" (raw L5167), and "Multiply this by all the other workflows we need to provide, and you can see how services quickly get tangled up." (raw L5169)

## Mechanism — temporal coupling

> "When two things have to be changed together, we say that they are *coupled*. We can think of this failure cascade as a kind of *temporal coupling*: every part of the system has to work at the same time for any part of it to work. As the system gets bigger, there is an exponentially increasing probability that some part is degraded." (raw L5179)

Synchronous HTTP integration makes services temporally coupled. A network error right after taking an order for three `MISBEGOTTEN-RUG` forces a bad choice — place the order unallocated, or refuse it — because "The failure state of our batches service has bubbled up and is affecting the reliability of our order service." (raw L5177)

## Symptoms that reveal it

- Mutual or cyclic dependencies between services (A→B→C for one workflow, C→B→A for another).
- A single business workflow requires every service to be up simultaneously.
- A failure in one service degrades the reliability of otherwise-unrelated services.

## The fix

Decompose by [[verbs-not-nouns]] so each service is a consistency boundary, then integrate asynchronously: "To avoid the Distributed Ball of Mud antipattern, instead of temporally coupled HTTP API calls, we want to use asynchronous messaging to integrate our systems." (raw L5207) See [[internal-vs-external-events]] for the event-based integration that replaces the synchronous calls.

## See also

[[verbs-not-nouns]] · [[anemic-domain-model]] · [[internal-vs-external-events]] · [[big-ball-of-mud]] · [[coupling-and-cohesion]] · [[bounded-context-autonomy]]
