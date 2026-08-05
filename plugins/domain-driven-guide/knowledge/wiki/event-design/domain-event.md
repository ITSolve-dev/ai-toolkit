---
title: Domain Event
category: event-design
summary: A domain-model object capturing something that already happened and that domain experts care about; named in past tense, immutable, and the backbone of event-driven, eventually consistent DDD.
tags: [concept, tactical-pattern, domain-events, domain-event, event-design, event-sourcing, immutability, ubiquitous-language, aggregates, message-bus, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-event-sourcing-guide, web-page-cosmic-python-book]
created: 2026-07-25
updated: 2026-07-26
---

A **domain event** is a domain-model object that records the occurrence of something meaningful that *has already happened* in the domain. Because the event describes the past, it cannot be changed after the fact, exactly as a real-world occurrence cannot be undone. Vernon adopts the contemporary definition "Something happened that domain experts care about" (IDDD raw L7009), quoting Evans: "Model information about activity in the domain as a series of discrete events. Represent each event as a domain object. . . . A domain event is a full-fledged part of the domain model, a representation of something that happened in the domain." (IDDD raw L7011). Events are "an extremely powerful modeling tool" (IDDD raw L6989).

> "Событие в эвент-сорсинге это набор данных описывающий некоторый факт реального мира, когда
> событие уже произошло, как и в реальном мире, оно уже не может измениться."
> — [[web-page-event-sourcing-guide]] (raw L86)

Domain events are the unit an [[aggregate]] emits. A time-ordered sequence of the events belonging to one aggregate is its **event stream**, and replaying that stream in order reconstitutes the aggregate's current state.

## When and why to model an Event

Listen to domain experts for verbal cues that an occurrence matters: phrases like "When . . .", "If that happens . . .", "Inform me if . . ." and "Notify me if . . .", "An occurrence of . . ." (IDDD raw L7015-7021). The notification itself is not the Event; it signals that "someone in the domain _wants to be notified_ as a result of an important occurrence, and that _likely means_ the need to model an explicit Event" (IDDD raw L7023). Once agreed, "new Events become a formal part of the [[ubiquitous-language]]" (IDDD raw L7035).

Not every command produces an Event: "Just as important as recognizing the _need_ for an Event is knowing _when to disregard_ extraneous happenings in the domain that experts or the business as a whole don't care about" (IDDD raw L7049). (Under [[event-sourcing]], Events may be more prolific than domain experts directly require.)

Events most often serve [[eventual-consistency]]: one aggregate publishes an Event and other aggregates or remote [[bounded-context]]s react in separate transactions, eliminating two-phase commits (IDDD raw L7037).

## Modeling an Event

- **Name in past tense, derived from the command.** "If an Event is the result of executing a command operation on an Aggregate, the name is usually derived from the command that was executed" (IDDD raw L7061). The command `BacklogItem#commitTo(Sprint)` yields the Event `BacklogItemCommitted`. "It is not occurring now. It occurred previously. The best name to choose is the one that reflects that fact" (IDDD raw L7069). Name Events and their properties per the Ubiquitous Language of the originating [[bounded-context]].
- **Properties.** Include a timestamp — the minimal `DomainEvent` interface guarantees an `occurredOn()` accessor (IDDD raw L7086) — plus "whatever would be necessary to trigger the Event again ... normally includes the identity of the Aggregate instance on which it took place, or any Aggregate instances involved" (IDDD raw L7101). `BacklogItemCommitted` carries `backlogItemId`, `committedToSprintId`, and `tenantId`: the SprintId because a subscriber must notify the Sprint, and "in the multitenancy environment, recording the TenantId is always necessary" (IDDD raw L7122).
- **Immutability.** "an Event is usually designed as immutable" (IDDD raw L7124) — a full-state constructor plus read accessors, no exposed setters. Any derived-state operations must be **Side-Effect Free** (see [[value-object]]) to protect immutability (IDDD raw L7243).
- **Enrichment.** Add extra state or derived operations only when subscribers need more than the Event's cause, so they "avoid querying back on the Aggregate from which the Event was published" (IDDD raw L7231). Enrichment is more common with [[event-sourcing]].

## Event vs. command

The distinction is load-bearing and often confused:

- A **command** is the description of a task — a *request* to do something. It is a stateful thing (it may be pending, executing, or completed with a result) and it *may be rejected*. Executing a command can change one or more aggregates, which is what produces new events.
- A **domain event** is the *outcome* — data describing what already happened as a result of that code running. Once an event exists, it always applies to its aggregate; the only reason it would fail to apply is a bug in the code.

A direct corollary the guide stresses: **do not run domain-logic validation when replaying events to reconstitute an aggregate.** Validation belongs to command handling (before the event is produced); at reconstitution time the event is already an accepted fact, so re-validating it is a design error. (raw L154-158)

## Command sourcing (contrast)

*Command sourcing* stores the commands the system executed so they can be replayed. Replaying commands can yield a *different* resulting state (the code they run against may have changed), whereas event sourcing stores the events (the facts) and therefore always reproduces one specific state. (raw L160)

## Value-based vs. Aggregate-characteristic Events

Most Events are value-like and need no identity. But some are "created by direct request from clients ... in response to some occurrence that is not the direct result of executing behavior on an instance of an Aggregate" (IDDD raw L7247); such an Event "can be modeled as an Aggregate and retained in its own [[repository]]", whose "Repository would not permit its removal" (IDDD raw L7247). It stays immutable but may be assigned a generated unique identity.

## Identity

Often an Event needs no formal identity — "It may be enough to allow Event identity to be represented by its properties, as is the case with Value Objects": name/type + involved Aggregate identities + timestamp (IDDD raw L7261). Assign a generated unique id when Events must be compared, when modeled as an [[aggregate]], or — importantly — when published outside the local context, because "individual messages can be delivered more than once" and remote subscribers use the id for [[event-de-duplication]] (IDDD raw L7265-7269). `equals()`/`hashCode()` are needed only if the local context uses them or the Event is stored as an Aggregate (IDDD raw L7271).

## Domain events are not integration events

Emitting domain events across service boundaries turns them into a shared contract and couples the services. Keep domain events internal to a single bounded context and integrate contexts through explicit integration events or an API — see [[domain-events-vs-integration-events]]. When Events *are* deliberately propagated enterprise-wide, do it through the mechanisms of [[event-driven-integration]], not by leaking the domain contract implicitly.

## The Cosmic Python view — recorded on the aggregate, dispatched by the bus

*Architecture Patterns with Python* arrives at the same building block from the allocation example and adds a concrete Python mechanism. It agrees the event is value-like: "An *event* is a kind of *value object*. Events don't have any behavior, because they're pure data structures. We always name events in the language of the domain, and we think of them as part of our domain model." (raw L3877). Events are plain `@dataclass`es (`OutOfStock(sku)`, `Allocated`, `BatchCreated`, `AllocationRequired`, `BatchQuantityChanged`) sharing an `Event` parent that gives the [[message-bus]] a type to dispatch on.

**Recorded on the aggregate, not acted on.** When the model records a fact, it *raises* an event by appending to the aggregate's own `.events` list, and does nothing else about it — no email, no infrastructure call:

```python
class Product:
    def __init__(self, sku, batches, version_number=0):
        ...
        self.events = []  # type: List[events.Event]
    def allocate(self, line: OrderLine) -> str:
        try:
            ...
        except StopIteration:
            self.events.append(events.OutOfStock(line.sku))
            return None
```

Something else (ideally the [[unit-of-work]], via the [[repository]]'s `.seen` set) collects and dispatches them later — "the UoW no longer actively puts events on the message bus; it just makes them available." (raw L4389) This keeps the domain model free of any dependency on the dispatch mechanism, and is the antidote to [[infrastructure-leaking-into-the-domain-model]].

**Events replace exceptions used for control flow.** A key refactor: the model stops *raising* an `OutOfStock` exception and *records* an `OutOfStock` event instead. "if you're implementing domain events, don't raise exceptions to describe the same domain concept... it's confusing to have to reason about events and exceptions together." (raw L3940). The recorded-not-raised style means `allocate()` returns `None` on failure, so callers inspect state/events rather than catching.

**The "When X, then Y" heuristic.** Domain experts phrase requirements causally, and that phrasing reveals a hidden event: "When we try to allocate stock but there's none available, then we should send an email to the buying team." — "The magic words 'When X, then Y' often tell us about an event that we can make concrete in our system." (raw L4138) Model X as a domain event and put Y in a handler on the [[message-bus]].

**Events are both system inputs and internal work packages.** The book stops distinguishing external API calls from internal side effects and treats both as events: `services.allocate()` becomes the *handler* for an `AllocationRequired` event, `services.add_batch()` the handler for `BatchCreated`. A `BatchQuantityChanged` handler may deallocate order lines and raise fresh `AllocationRequired` events that flow straight back into the ordinary allocation handler — "there is no conceptual difference between a brand-new allocation coming from the API and a reallocation that's internally triggered by a deallocation." (raw L4248) The aggregate records these inline:

```python
def change_batch_quantity(self, ref, qty):
    batch = next(b for b in self.batches if b.reference == ref)
    batch._purchased_quantity = qty
    while batch.available_quantity < 0:
        line = batch.deallocate_one()
        self.events.append(
            events.AllocationRequired(line.orderid, line.sku, line.qty))
```

**Handlers and the SRP.** "Handlers are the way we react to events... We can define multiple handlers for a single event... Handlers can also raise other events. This allows us to be very granular about what a handler does and really stick to the SRP." (raw L4707) Because a handler can emit further events instead of doing everything itself, each unit of work stays small; dispatch does the composition. The pay-off is extensibility at fixed conceptual cost — a complicated new requirement is added with "no cost in terms of complexity" (raw L4719), only new events, handlers, and adapters.

**Independent failure is a feature.** Because events broadcast and "senders should not care whether the receivers succeeded or failed" (raw L4773-4774), handlers may fail on their own: "By separating out these concerns, we have made it possible for things to fail in isolation, which improves the overall reliability of the system." (raw L5001) In the VIP example, a `History` aggregate raises `CustomerBecameVIP` on the third order and a handler sends the congratulations email — but a busy email server must not "stop us from taking money for orders" (raw L4996). Only the core command handler must succeed; events carry the non-essential work. This is the reliability argument behind [[aggregate-consistency-boundary]]. The cost is that you need recovery, not fire-and-forget: log every message before handling, retry transient failures with back-off (safe because the UoW + command-handler patterns "mean that each attempt starts from a consistent state", raw L5076), and accept that eventually you "give up trying to process the message" (raw L5078). See [[commands-and-events]] for the command/event distinction that governs all of this.

## Failure modes

- **Events carrying whole objects.** "if Domain Events are correctly designed, they will rarely if ever carry entire objects as part of their state" (IDDD raw L7498) — carry limited command parameters / Aggregate state plus foreign Aggregate identities.
- **Present-tense or command-shaped names** hide that the occurrence is already in the past.
- **Coupling the model to messaging.** Publish through the in-process [[domain-event-publisher]], never by referencing middleware from the model (IDDD raw L7275).

## Related

[[domain-event-publisher]] · [[event-store]] · [[eventual-consistency]] · [[event-driven-integration]] · [[event-de-duplication]] · [[event-sourcing]] · [[aggregate]] · [[domain-events-vs-integration-events]] · [[message-bus]] · [[commands-and-events]] · [[aggregate-consistency-boundary]] · [[unit-of-work]] · [[infrastructure-leaking-into-the-domain-model]]

---
Distilled from [[book-implementing-ddd-vaughn-vernon]] (Ch. 8), [[web-page-event-sourcing-guide]], and [[web-page-cosmic-python-book]] (Ch. 8–10).
