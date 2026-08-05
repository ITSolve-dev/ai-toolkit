---
title: Event-Driven Integration (Autonomous Services)
category: context-mapping
summary: Propagating domain events across bounded contexts via asynchronous messaging so systems become autonomous services — avoiding in-band RPC, carrying meaning rather than whole objects, and keeping the model and messaging stores consistent.
tags: [pattern, event-driven-integration, context-mapping, autonomous-services, messaging, domain-event, eventual-consistency, rpc, bounded-context, idempotency]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Event-driven integration** propagates [[domain-event]]s from one [[bounded-context]] to remote contexts through enterprise messaging, so that systems become **autonomous services** — "any coarse-grained business service ... that operates largely independent of other such 'services' in the enterprise" (raw L7494). It is the mechanism that "takes over where the lightweight" [[domain-event-publisher]] "leaves off" (raw L7470). Because "Events are a _domain-wide_ concept" (raw L7464), the publish contract can span the whole enterprise.

## Autonomy by avoiding in-band RPC

"A high degree of independence from other systems is achieved by avoiding in-band remote procedure calls (RPCs), where a user request is satisfied only by successful completion of an API request to a remote system" (raw L7494). RPC couples availability: "avoiding in-band RPC greatly eases dependency and related instances of complete failure and/or unacceptable performance caused by unavailable or low-throughput remote systems" (raw L7496). Instead, "use asynchronous messaging to achieve a greater degree of independence between systems—autonomy" (raw L7498). RPC cannot always be avoided (legacy systems, or when translating a foreign model is very difficult), but Vernon suggests "not giving in to RPC too easily" (raw L7502).

## Events carry meaning, not whole objects

A subscribing context executes behavior on its own model reflecting the Event's meaning — it does not replicate foreign objects. "if Domain Events are correctly designed, they will rarely if ever carry entire objects as part of their state" (raw L7498); "The Event will hold some limited amount of command parameters and/or Aggregate state" plus foreign Aggregate identities (raw L7500). Copying whole objects across contexts is a modeling error — see [[bounded-context]] and [[context-map]], and use an [[anticorruption-layer]] to translate. If an Event lacks what a subscriber needs, the "_domain-wide_ contract of the Event must be altered", likely a new Event version (raw L7500).

## Messaging-infrastructure consistency

A commitment to [[eventual-consistency]] "can't be fought" (raw L7474), yet two stores must stay in lockstep: "the persistence store used by the domain model, and the persistence store backing the messaging infrastructure" (raw L7478) — otherwise a delivered Event might not reflect a committed model change. Three ways to guarantee this (raw L7482-7488):

1. **Shared persistence store** — model change and message insertion "commit under the same local transaction." Good performance; requires the messaging store to live in the same database/schema, and both must be shareable.
2. **Global XA (two-phase commit)** — keeps the stores separate, but "Global transactions tend to be expensive and perform poorly" and require XA support on both sides.
3. **[[event-store]] as an out-of-band queue** — a dedicated Event table in the *model's* store (owned by the Bounded Context, not the messaging product); a custom forwarder publishes unpublished Events through messaging. Guarantees model+Events consistency in one local transaction and enables REST feeds, at the cost of building the forwarder and requiring clients to de-duplicate. This is the approach Vernon uses.

## Forwarding styles

Once the [[event-store]] is populated, two styles forward its Events: pull-based [[notification-log]]s (RESTful Atom-style resources) and push-based messaging middleware (e.g. RabbitMQ **fanout exchange**). With middleware, a `NotificationService.publishNotifications()` queries unpublished Events ordered by `eventId`, sends each to the exchange, and records progress in a `PublishedMessageTracker`; "We do not wait to see if subscribers confirm receipt" (raw L7791) — the broker guarantees delivery, and a timer (JMX `TimerMBean` or Quartz) drives publishing on a recurring interval (raw L8230-8254). Because duplicate delivery is possible, subscribers must handle [[event-de-duplication]].

## How it works, end to end (Ch. 13 worked example)

When a domain operation completes, the [[aggregate]] publishes an event as its last responsibility. In the SaaSOvation example the *Identity and Access Context* publishes `UserAssignedToRole` at the end of `Role.assignUser()` (raw L12234). Every event is appended to the context's [[event-store]] and then forwarded to subscribers by the messaging mechanism (raw L12739). Consumers register a listener per exchange; SaaSOvation factors the boilerplate into an abstract `ExchangeListener` base class whose subclasses implement only `exchangeName()`, `listensToEvents()`, and `filteredDispatch()` (raw L12326). The listener adapts the notification into a command on an [[application-service]] (e.g. `TeamService.enableTeamMember(...)`), which then loads or creates the local aggregate.

## Enriching and naming events

Events should carry **enough data for consumers to act** without a synchronous callback. `UserAssignedToRole` is "enriched with `User` name and e-mail address properties" (raw L12257) so the Agile PM context can build a `TeamMember`/`ProductOwner` directly. This is a deliberate design lever, not an anti-pattern: "it is possible for Event data to be used to perform calculations and derive state in consuming foreign Bounded Contexts while not actually holding on to and assuming the responsibility for keeping it synchronized" (raw L12590). Enrichment is in tension with duplication — see [[duplicating-information-across-bounded-contexts]]. (This is consistent with the "carry meaning, not whole objects" rule above: enrich with the limited data a subscriber needs, never a whole foreign object.)

Name events with **fully qualified class names** (module + class): "publishers and subscribers should consider the use of fully qualified class names... This removes all possible collision or ambiguity that could exist with same or similarly named Events from different Bounded Contexts" (raw L12398). See [[published-language]] for how the qualified `typeName` appears in the exchanged media type.

## The core trade-off: autonomy for eventual consistency

What you gain is decoupling and availability; what you give up is immediate consistency. Consumers see facts *after* they happened, so cross-context state is only ever [[eventual-consistency|eventually consistent]]. Because the transport (RabbitMQ) guarantees **at-least-once, possibly out-of-order** delivery, every consumer must be written to tolerate duplicate and reordered messages — see [[idempotency]] and [[event-de-duplication]]. Workflows that span several messages need a coordinator — see [[long-running-process]].

## Failure modes

- **Messaging offline (publisher side):** publishers cannot send. Back off aggressively ("back off as much as 30 seconds or a minute between retries", raw L13547) rather than hammering the broker. An [[event-store]] saves you: "your Events will continue to be queued in your live system and can be sent as soon as messaging is available again" (raw L13547).
- **Silent dead consumers:** after the broker recovers, a consumer may not auto-resubscribe. "If automatic recovery of consumers is not supported, you will need to be certain that your consumers are reregistered. Otherwise... your Bounded Context isn't receiving the notifications... That's one kind of eventual consistency that you want to avoid" (raw L13549). This is a leaky-integration failure that is invisible until data silently drifts.
- **Downtime catch-up:** if a whole context is down, durable queues accumulate a backlog it must grind through on restart (raw L13551). Mitigate with limited-downtime goals, live deployment, and redundant clustered nodes.

## Related

[[domain-event]] · [[event-store]] · [[notification-log]] · [[event-de-duplication]] · [[idempotency]] · [[long-running-process]] · [[duplicating-information-across-bounded-contexts]] · [[eventual-consistency]] · [[bounded-context]] · [[integrating-bounded-contexts]] · [[anticorruption-layer]] · [[published-language]] · [[context-map]] · [[event-driven-architecture]] (the broader architectural style these mechanics realize)
