---
title: Domain Event Publisher
category: event-design
summary: A lightweight, in-process, synchronous Publish-Subscribe (Observer) mechanism that lets aggregates notify subscribers of domain events without coupling the model to messaging middleware.
tags: [pattern, domain-event, publish-subscribe, observer, event-design, application-service, threadlocal]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The **Domain Event Publisher** is a lightweight, in-process **Publish-Subscribe** (Observer [Gamma et al.]) mechanism that lets an [[aggregate]] notify subscribers of a [[domain-event]] without coupling the model to messaging middleware. "Avoid exposing the domain model to any kind of middleware messaging infrastructure ... We'll use an approach that completely avoids the use of infrastructure" (raw L7275).

## How it works

It is lightweight because "there is no network involved ... All registered subscribers execute in the same process space with the publisher and run on the same thread. When an Event is published, each subscriber is notified synchronously, one by one" (raw L7277). This "implies that all subscribers are running within the same transaction, perhaps controlled by an [[application-service]]" (raw L7277).

The `DomainEventPublisher` holds two `ThreadLocal` variables, `subscribers` and `publishing`, "allocated per thread" because "every incoming request from users of the system is handled on a separate dedicated thread" (raw L7364).

- **`subscribe()`** adds a `DomainEventSubscriber` to the thread's list. Subscribers may register "only when the publisher is not in the process of publishing"; the `publishing` guard "prevents problems such as concurrent modification exceptions on the List" when a handler tries to add subscribers (raw L7381).
- **`publish()`** iterates registered subscribers, calling `subscribedToEventType()` to filter; a subscriber answering `DomainEvent.class` receives all Events, otherwise only its exact type, then matching subscribers get `handleEvent()`. The `publishing` boolean must be `false` to dispatch, so "publish() does not allow nested requests to publish Events" (raw L7405).
- **`reset()`** clears subscribers. Because "threads may be pooled and reused", each new request must `reset()` "to clear any previous subscribers" (raw L7366) — e.g. a web filter calls `reset()` at request start and an Application Service calls `subscribe()` later in the same request (raw L7371-7379).

## Who publishes, who subscribes

- **Publishers are Aggregates.** "the most common use of Domain Events is when an Aggregate creates an Event and publishes it" (raw L7283). When `BacklogItem.commitTo()` succeeds it calls `DomainEventPublisher.instance().publish(new BacklogItemCommitted(...))` (raw L7383-7401).
- **Subscribers are Application Services (sometimes Domain Services).** Since [[application-service]]s are the direct client of the model under [[hexagonal-architecture]], "they are in an ideal position to register a subscriber with the publisher before they execute Event-generating behavior on Aggregates" (raw L7421). [[domain-service]]s subscribe "when there would be domain-specific reasons to listen for Events" (raw L7466).

## The critical rule: one Aggregate per transaction

A subscriber "_should not_ ... get another Aggregate instance and execute modifying command behavior on it" (raw L7462). "Don't use the Event notification to modify a second Aggregate instance. That breaks a rule of thumb to modify one Aggregate instance per transaction" (raw L7460). Instead, "the consistency of all Aggregate instances other than the one used in the single transaction must be enforced by asynchronous means" (raw L7462) — forward the Event via messaging so out-of-band subscribers each modify their own Aggregate in separate transactions (see [[eventual-consistency]], [[event-driven-integration]]). Because "Events are a _domain-wide_ concept, not just a concept in a single Bounded Context" (raw L7464), the publish contract can reach the whole enterprise.

## Failure modes

- **Handler mutates a second aggregate** — violates the aggregate transaction rule; the symptom is oversized transactions and contention/inconsistency.
- **Forgetting `reset()`** on a pooled thread leaks subscribers from a prior request into the next.
- **Registering subscribers during publish** (guarded away here) would risk concurrent-modification errors on the subscriber list.

Related: [[domain-event]], [[event-store]], [[application-service]], [[hexagonal-architecture]], [[aggregate]], [[eventual-consistency]].
