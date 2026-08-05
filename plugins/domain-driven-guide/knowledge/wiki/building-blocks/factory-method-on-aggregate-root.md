---
title: Factory Method on Aggregate Root
category: building-blocks
summary: A behavioral method on an Aggregate Root that creates another Aggregate (or inner part) in a valid state, expressing the Ubiquitous Language and guaranteeing correct sensitive identities like TenantId.
tags: [pattern, factory, aggregate, building-blocks, ubiquitous-language, multitenancy, invariants]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The most common way Vernon applies the [[factory|Factory]] pattern is as a **Factory Method placed directly on an [[aggregate|Aggregate Root]]** (an [[entity|Entity]]), which produces a new instance of *another* Aggregate type — or of the root's inner parts — and returns it to the client. The host Aggregate keeps its normal domain responsibilities; the Factory Method is simply one of its behaviors.

Three forces make this placement attractive: it **expresses the [[ubiquitous-language|Ubiquitous Language]]**, it **reduces the client's construction burden**, and it **guarantees correct sensitive state** that a public constructor could not enforce.

## Expressing the Ubiquitous Language

A constructor can only ever be named after its class. A Factory Method can be named after what the domain experts actually say. Vernon's Collaboration Context examples were designed straight from domain-expert scenarios:

- *Calendars schedule calendar entries* → `Calendar.scheduleCalendarEntry(...)` (raw L9745)
- *Authors start discussions on forums* → `Forum.startDiscussion(...)` (raw L9812)

> If our design were to support only a public constructor on `CalendarEntry`, it would reduce the expressiveness of the model and we would not be able to explicitly model that part of the Language of the domain. (raw L9747)

## Forcing the Factory: hide the constructor

To make the Factory Method the only path, the target Aggregate's full constructor is hidden. `CalendarEntry`'s constructor is declared `protected`, "which forces clients to make use of the `scheduleCalendarEntry()` Factory Method on `Calendar`" (raw L9747). The client can no longer bypass the language-expressing, invariant-protecting entry point.

## Guaranteeing sensitive state (the real payoff)

The decisive benefit is that the Factory Method — not the client — supplies the parameters that must never be wrong. `CalendarEntry`'s constructor takes 11 parameters; `scheduleCalendarEntry()` asks the client for only nine, injecting the other two itself:

> Still, the `Tenant` and associated `CalendarId` are strictly provided only by the Factory Method. This is where we guarantee that `CalendarEntry` instances are created only for the correct `Tenant` and in association with the correct `Calendar`. (raw L9770)

This is the concrete defense against the multitenancy disaster of a mis-assigned `TenantId`. The same shape recurs in `Forum.startDiscussion()`: the `Forum` supplies `Tenant` and `ForumId`, so "only three of five parameters required to instantiate a new `Discussion` must be supplied by the client" (raw L9808). Clients typically pass only basic parameters and [[value-object|Value Objects]].

## Enforcing invariants during creation

Beyond identity injection, the Factory Method can guard domain rules at creation time. `startDiscussion()` refuses to create a `Discussion` when the forum is closed:

```java
public Discussion startDiscussion(DiscussionId aDiscussionId, Author anAuthor, String aSubject) {
    if (this.isClosed()) {
        throw new IllegalStateException("Forum is closed.");
    }
    Discussion discussion = new Discussion(this.tenant(), this.forumId(), aDiscussionId, anAuthor, aSubject);
    DomainEventPublisher.instance().publish(new DiscussionStarted(...));
    return discussion;
}
```

The method also publishes a [[domain-event|Domain Event]] (`CalendarEntryScheduled`, `DiscussionStarted`) as part of the create.

## Guards and self-delegation

Vernon points out that `scheduleCalendarEntry()` has no guard clauses at the top, and that this is fine: "the constructors of each of the Value parameters and the `CalendarEntry` constructor, as well as the setter methods that the constructor self-delegates to, provide all the needed guards" (raw L9739). Adding guards on the Factory Method is optional belt-and-suspenders. See [[entity]] for self-delegation and guards.

## Client responsibility: add to the Repository

A Factory Method only creates; it does not persist. After creation the client "must add it to its Repository. Failing to do so will release the new instance to be swept by the garbage collector." (raw L9693) See [[repository]].

## Trade-off: you must load the host Aggregate first

The cost of putting the Factory Method on an Aggregate Root is that the root must already be in memory:

> As is the case with any such Aggregate Factory Method, the `Calendar` will have to be acquired from its persistence store before it can be used to create the `CalendarEntry`. This extra hit may be well worth it, but as the traffic in this Bounded Context increases, the team will have to weigh the consequences carefully. (raw L9766)

## Failure mode: an awkward parameter is a hint

If one of the still-required client parameters is itself hard to build (Vernon's `Set<Invitee>`), that is "not the fault of the Factory Method" but a signal to build a dedicated facility — "which may be pointing toward the creation of a dedicated Factory" for that piece (raw L9768).

## Related

[[factory]] · [[factory-on-service]] · [[aggregate]] · [[ubiquitous-language]] · [[value-object]] · [[domain-event]] · [[entity]] · [[repository]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
