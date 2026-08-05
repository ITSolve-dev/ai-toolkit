---
title: Strangler Fig Pattern (via event interception)
category: refactoring-toward-ddd
summary: A legacy-replacement strategy — grow a new system around the edges of an old one and gradually intercept its functionality; in DDD it is realized through event interception, where a new bounded context builds its own domain model from events emitted by the old system.
tags: [pattern, strangler-fig, event-interception, legacy, bounded-context, domain-event, walking-skeleton, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Strangler Fig Pattern (via event interception)

Where [[refactoring-toward-ddd]] cleans a system *in place*, the **Strangler Fig pattern** *replaces* a subsystem by growing a new one alongside it: "The Strangler Fig pattern involves creating a new system around the edges of an old system, while keeping it running. Bits of old functionality are gradually intercepted and replaced, until the old system is left doing nothing at all and can be switched off." (raw L6807) It is the drastic-measures option for systems "suffering problems with reliability, performance, maintainability, or all three" (raw L6843).

## Event interception (three steps)

Cosmic Python's mechanism for the interception is **event interception**, "a three-step process" (raw L6813):

1. "Raise events to represent the changes happening in a system you want to replace." (raw L6817)
2. "Build a second system that consumes those events and uses them to build its own domain model." (raw L6819)
3. "Replace the older system with the new." (raw L6821)

The DDD significance is step 2: the new system does not share the old model — it constructs *its own* [[domain-event|event]]-fed domain model, i.e. a new [[bounded-context]] with its own [[ubiquitous-language]], integrated with the legacy system through published events rather than shared tables or synchronous calls. The case study moved from "strong, bidirectional coupling based on XML-RPC" (ecommerce ↔ fulfillment) to an event-based topology where fulfillment "Publishes batch_created" and the new Availability Service "Publishes out_of_stock" (raw L6823..6827).

## Start with a walking skeleton

Rather than build the whole thing before deploying, start end-to-end but trivial: "When deploying an event-driven system, start with a 'walking skeleton.' Deploying a system that just logs its input forces us to tackle all the infrastructural questions and start working in production." (raw L6831) The first production deployment of the availability service was "a tiny system that could receive a `batch_created` event and log its JSON representation" — "the 'Hello World' of event-driven architecture" — which forced deploying a message bus, wiring a producer and consumer, building a pipeline, and writing a handler (raw L6836). Only then was the real domain model (batches, shipments, products, built TDD-first around one question) filled in.

## Trade-offs

- **Gained:** the old system keeps running throughout; risk is incremental; the new bounded context is clean and independently deployable.
- **Cost:** it is a substantial effort — the case study was "a several month-long project" (raw L6829) — and it depends on event/messaging infrastructure whose reliability concerns (delivery guarantees, idempotency, schema evolution) the book explicitly notes as hard and out of its own scope.

## Related

- [[refactoring-toward-ddd]] — the in-place alternative.
- [[collaborative-domain-modeling]] — how to build the new context's model before growing it.
- [[domain-event]] · [[bounded-context]] · [[ubiquitous-language]] — the mechanism and the clean context event interception produces.
- [[event-driven-integration]] — the messaging integration the intercepted events flow over.
