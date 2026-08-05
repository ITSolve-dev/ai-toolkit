---
title: Idempotency and Out-of-Order Tolerance for Message Consumers
category: context-mapping
summary: Design message-handling operations so that duplicate and reordered deliveries are harmless — required whenever messaging guarantees at-least-once, possibly out-of-order delivery.
tags: [technique, idempotency, messaging, out-of-order, at-least-once, change-tracker, eventual-consistency]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Message-based integration transports such as RabbitMQ guarantee **delivery at least once** and give **no ordering guarantee**. A consumer therefore must assume it will sometimes see the *same* message twice and sometimes see messages in the *wrong order*. **Idempotency** is the property that applying a message more than once has the same effect as applying it once; **ordering tolerance** is the property that a stale (older) message cannot overwrite newer state. Both are mandatory for correct [[event-driven-integration]] and [[long-running-process]]es — they are not optional polish.

The receiver-side machinery that tracks handled message ids is treated in depth under [[event-de-duplication]]; this page covers the domain-modeling techniques that make the *operation* itself idempotent and order-tolerant.

## Why it is unavoidable

"Remember that RabbitMQ guarantees _delivery at least once_ and thus may deliver the same command message multiple times, even if it is sent only once" (raw L13333). Retries in a long-running process compound this: a single logical request can produce many physical deliveries. The wrong fix is to disable retries; the right fix is to make the operation idempotent so redundant deliveries "end up being benign" instead of creating duplicates.

## Technique 1 — state-check idempotency

Guard the operation with the aggregate's own state. `Product.initiateDiscussion()` transitions `REQUESTED -> READY`; if already `READY` it does nothing: "if the state is currently `READY`, the Long-Running Process has already completed" (raw L13003). No extra machinery is needed when the [[aggregate]]'s state itself records that the step happened.

## Technique 2 — find-or-create

Make creation idempotent by looking up the target before creating it. Collaboration's `startExclusiveForumWithDiscussion` searches for an existing `Forum`/`Discussion` by its unique exclusive-owner key and only creates when absent: "By trying to find the `Forum` and `Discussion` from their unique exclusive owner attribute, we prevent attempting to create two Aggregate instances that may already exist" (raw L13394). Vernon notes this small change makes "Event-Driven processing so much better" — before it, retried commands produced benign-but-noisy duplicate-key errors that looked like bugs in the logs (raw L13331).

## Technique 3 — a change tracker (idempotency + ordering together)

When you keep a synced copy of foreign data (see [[duplicating-information-across-bounded-contexts]]), you need both properties. SaaSOvation's `MemberChangeTracker` [[value-object]] stamps each mutable field with the timestamp of the last change it applied (`enablingOn`, `nameChangedOn`, `emailAddressChangedOn`). Every command carries the event's `occurredOn` as an `asOfDate`, and the operation only proceeds if the incoming change is newer:

> `canToggleEnabling(asOfDate)` returns `this.enablingOn().before(asOfDate)` (raw L12523).

This single mechanism does two jobs. It gives **ordering tolerance** — a reversed pair (`UserUnassignedFromRole` arriving after a later `UserAssignedToRole`) can no longer strand a member in the wrong state (raw L12457). And it gives **idempotency** — "The `MemberChangeTracker` also serves to make `Member` subclass command operations idempotent, such that when the same notification is delivered multiple times by the messaging infrastructure, redundant deliveries are ignored" (raw L12562).

A subtlety: for a coarse event like `PersonContactInformationChanged` (which may or may not actually change the email), check whether the value really changed before recording it as changed — otherwise "an out-of-order Event of the same type that did in fact carry a changed e-mail address would be ignored" (raw L12560).

The tracker is not part of the [[ubiquitous-language]] and that is acceptable: "we never expose the `MemberChangeTracker` outside the Aggregate boundary. It is an implementation detail" (raw L12564). Clients only owe the operation an `occurredOn` value.

## Failure mode this prevents

Without these techniques you get, variously: stuck aggregates (an out-of-order disable that never re-enables), silent duplicate aggregates or duplicate-key error spam, and compensation logic firing on stale data. All of them surface only under real message reordering/redelivery — "it seems to always happen when we overlook the fact that it could happen" (raw L12457).

## Related

[[event-driven-integration]] · [[event-de-duplication]] · [[long-running-process]] · [[duplicating-information-across-bounded-contexts]] · [[value-object]] · [[aggregate]] · [[eventual-consistency]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
