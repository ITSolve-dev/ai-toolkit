---
title: Read Model Projection
category: event-design
summary: A set of domain-event subscribers that project events into a persistent, queryable read model — the CQRS query side that answers property-based questions event streams cannot, and a loosely coupled channel for sharing data across aggregates and bounded contexts.
tags: [pattern, cqrs, read-model, projection, domain-event, event-sourcing, domain-service]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

## The problem it solves

[[event-sourcing|Event sourcing]] makes an [[aggregate|Aggregate]] reconstitutable from its events, but it gives no efficient way to *query across* aggregates by property. Asking "What is the total amount of all customer orders within the last month?" would force you to "load every `Customer` instance, enumerate all of the `Order` instances within the last month for each one, and calculate their total, which would be extremely inefficient" (raw L15408). This is the query-side gap that [[cqrs|CQRS]] fills.

## What it is

A **Read Model Projection** is the query side. "Read Model Projections can be realized through a simple set of Domain Event subscribers that are used to generate and update a persistent Read Model. In other words, they *project Events to a persistent Read Model*" (raw L15410). As events arrive, subscribers compute query results and store them for later, cheap consumption.

Structurally, "a Projection is very similar to an Aggregate instance. As Events are received and handled, we use the data from them to build the Projection's state" (raw L15412). The key difference from an aggregate — and from an [[application-service|Application Service]] — is the direction of the trigger: "our Projection reacts to Events rather than Commands and updates documents using `IDocumentWriter`, rather than updating Aggregate instances" (raw L15451). A projection typically implements `When(SomeEvent e)` handlers that mutate a persisted DTO (the read model itself is "just a simple **Data Transfer Object**", raw L15453).

## Storage and disposability

Read models are commonly persisted in a document database, but may be cached in memory (memcached), pushed to a CDN, or written to relational tables (raw L15486). The defining operational property is disposability: "one of the major advantages of Projections is that they are completely disposable. They can be added, modified, or completely replaced at any time" (raw L15488). To rebuild, "discard all existing Read Model data and generate new data by running your entire Event Stream through your Projection classes" (raw L15490) — a process that can be automated with zero downtime. This is why event-sourced read models are cheap to evolve: the events are the source of truth, projections are derived and rebuildable.

## Sharing data across aggregates and contexts

Projections are not only for UIs; they are a loosely coupled integration channel. When an `Invoice` [[aggregate|Aggregate]] needs `Customer` data (name, billing address, tax ID) to compute an invoice, a `CustomerBillingProjection` maintains a `CustomerBillingView`, exposed to the `Invoice` aggregate through a [[domain-service|Domain Service]] named `IProvideCustomerBillingInformation` that queries the document store under the covers (raw L15494). "Projections also enable us to share information between Aggregate instances in a loosely coupled and more maintainable way" (raw L15496) — changing the shared data means changing the projection and replaying events, not modifying the `Customer` aggregate. Contrast this with directly coupling one aggregate to another's internals.

Projections that must join several event streams benefit strongly from [[domain-event-enrichment]] — thin events force the projection to maintain its own lookups.

## Related

[[domain-event]] · [[domain-event-enrichment]] · [[aggregate]] · [[domain-service]] · [[bounded-context]] · [[cqrs]] · [[event-sourcing]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
