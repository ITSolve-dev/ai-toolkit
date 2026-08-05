---
title: Internal vs. External Events
category: event-design
summary: Extending domain events outward to integrate systems asynchronously, while keeping a deliberate line between internal events (dispatched in-process) and external events (explicitly upgraded and published to a message broker).
tags: [pattern, domain-event, event-driven, integration, eventual-consistency, message-broker, command, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Internal vs. External Events

Once a domain model raises [[domain-event|domain events]] internally, the same metaphor can be extended outward to integrate with other systems: incoming external messages are translated into commands/events the model handles, and results are published back out as events for downstream services to consume. The discipline that keeps this clean is a deliberate line between **internal** events (handled in-process) and **external** events (published to the outside world).

## The application as a message processor, inside and out

> "Internally, the core of our application is now a message processor. Let's follow through on that so it becomes a message processor *externally* as well." (raw L5116)

The application "will receive events from external sources via an external message bus... and publish its outputs, in the form of events, back there as well." (raw L5118) Concretely: a `BatchQuantityChanged` message arrives from an upstream system, and an `Allocated` event is published for downstream systems.

## Commands in, events out

The integration contract for a verb-service (see [[verbs-not-nouns]]) is: "Each service accepts commands from the outside world and raises events to record the result. Other services can listen to those events to trigger the next steps in the workflow." (raw L5203) An inbound adapter deserializes an external message and converts it to a `Command` for the service layer — "much as the Flask adapter does" (raw L5314) — while an outbound adapter converts a domain event into a message on a channel.

## The message broker

Getting events from one system into another needs infrastructure "often called a *message broker*. The role of a message broker is to take messages from publishers and deliver them to subscribers." (raw L5220) The book uses Redis pub/sub for familiarity; "Kafka or RabbitMQ are valid alternatives" (raw L5224). The choice is not trivial — "message ordering, failure handling, and idempotency all need to be thought through." (raw L5231)

## Keep internal and external events distinct

> "It's a good idea to keep the distinction between internal and external events clear. Some events may come from the outside, and some events may get upgraded and published externally, but not all of them will." (raw L5379)

An event stays internal (dispatched in-process to its handlers) unless it is deliberately *upgraded* into a public event and published. The `Allocated` event, for instance, is appended by the model inside `allocate()`, and then a dedicated handler (`publish_allocated_event`) pushes it to the `line_allocated` channel — publication is an explicit, separate step, not an automatic consequence of raising the event. Outbound events are also "one of the places it's important to apply validation." (raw L5386) Blurring this line is how a private domain event accidentally becomes part of a public contract other services depend on — the same coupling hazard as treating a domain event as an integration event (see [[domain-events-vs-integration-events]]).

## Trade-offs

Temporal decoupling "buys us a lot of flexibility in our application integrations, but as always, it comes at a cost." (raw L5392) Martin Fowler's caution on event notification:

> "Event notification is nice because it implies a low level of coupling, and is pretty simple to set up. It can become problematic, however, if there really is a logical flow that runs over various event notifications...It can be hard to see such a flow as it's not explicit in any program text....This can make it hard to debug and modify." (raw L5396)

And moving from synchronous to async "you also open up a whole host of problems having to do with message reliability and eventual consistency." (raw L5410)

## See also

[[domain-event]] · [[verbs-not-nouns]] · [[distributed-ball-of-mud]] · [[aggregate]] · [[message-bus]] · [[domain-events-vs-integration-events]] · [[event-driven-integration]]
