---
title: Event-Driven Architecture (with Domain Events)
category: event-design
summary: Systems produce, detect, consume and react to events; Domain Events published by one Bounded Context are delivered to subscribers in others over messaging, decoupling everything but the transport and the event types — commonly organized as message-based Pipes and Filters.
tags: [architecture-pattern, event-driven, domain-event, pipes-and-filters, bounded-context, messaging]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Event-Driven Architecture (EDA)** is "a software architecture promoting the production, detection,
consumption of, and reaction to events" (raw L3436). In a DDD setting the events that matter are
[[domain-event|Domain Events]], though a system may also react to infrastructure/system events (health,
logging, provisioning).

## EDA over Hexagonal, across Bounded Contexts

A [[hexagonal-architecture|Hexagonal]] system participates by receiving and sending messages on
dedicated input/output **Ports** — typically a messaging transport such as AMQP/RabbitMQ, separate from
the HTTP Ports used by other clients. Replicating this across several systems, "The Domain Events
published by one such system through the output Port would be delivered to subscribers represented in
the others through their input Port" (raw L3450). A received Domain Event "[has] a specific meaning in
each receiving Bounded Context, or possibly no meaning at all"; if of interest, its properties are
adapted to the application's API and used to execute an operation. The style's virtue is decoupling: EDA
"decouples all but the systems' dependency on the messaging mechanism itself and the Event types they
subscribe to" (raw L3448). Each [[bounded-context]] stays autonomous behind the shared event vocabulary
(see [[bounded-context-autonomy]]).

## Pipes and Filters

Message-based EDA often takes a **Pipes and Filters** shape (from Hohpe & Woolf). Each **Filter** is a
message handler that subscribes to an event, processes it, and publishes a new event; chaining
subscriptions forms a pipeline. Unlike the shell `cat | grep | wc` analogy used to introduce it, "an EDA
Filter doesn't need to actually filter anything" — it may transform or enrich while leaving message data
intact (raw L3489). Reordering or extending the pipeline is done by changing which events each Filter
subscribes to and publishes; such Domain Event pipelines change infrequently. In a real domain, step 1
publishes a Domain Event from an Aggregate's behaviour in one Bounded Context, and later steps create or
modify Aggregates in other Contexts.

## Why the events must be substantial

These are not thin technical notifications: Domain Events "explicitly model business process activity
occurrences that are useful for domain-wide subscribers to know about, and they pack unique identity and
as many knowledge-conveying properties as necessary" (raw L3525). That richness is what lets downstream
Filters act without calling back to the source.

## Extension

A synchronous step-by-step pipeline extends to parallel, distributed work via the [[long-running-process|
Long-Running Process (Saga)]] pattern, which coordinates multiple concurrent Filters to completion.

## Related

- [[domain-event]] — the unit an EDA carries.
- [[long-running-process]] — parallel/distributed extension of the pipeline.
- [[hexagonal-architecture]] — the host that exposes messaging Ports.
- [[bounded-context-autonomy]] — the autonomy EDA buys a downstream context.
- [[published-language]] — the shared vocabulary of the events on the wire.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
