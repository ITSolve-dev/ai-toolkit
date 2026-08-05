---
title: Event Sourcing
category: event-design
summary: Persist an Aggregate as the ordered, append-only stream of Domain Events its commands produced, reconstituting state by replaying them (with snapshots to bound cost); Repositories reduce to identity lookup and Aggregates lose getters, so it pairs hand-in-glove with CQRS. The specific practice of sourcing Aggregate state this way is A+ES.
tags: [pattern, event-design, event-sourcing, domain-event, aggregate, event-store, cqrs, a-plus-es]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Event Sourcing** persists a domain model as the full history of what happened to it, rather than a snapshot of current field values. In the DDD form Vernon describes, "every operational command executed on any given Aggregate instance in the domain model will publish at least one Domain Event that describes the execution outcome. Each of the events is saved to an Event Store in the order in which it occurred" (raw L3629). The analogy is a source-control system (Git, Subversion) that lets you walk an artifact revision by revision — applied to every [[aggregate|Aggregate]] in the model. Appendix A (contributed by Rinat Abdullin) names the specific practice of using Event Sourcing to maintain and persist Aggregate state **A+ES** — Aggregates plus Event Sourcing.

> "Event Sourcing can be used to represent the entire state of an Aggregate ... as a sequence of Events ... The Events are used to rebuild the state of the Aggregate by replaying them in the same order in which they occurred." (raw L14334)

Each Aggregate's events form an **append-only Event Stream**; state is mutated only by appending new events to the end of that stream, never by overwriting prior state. The stream is persisted in an [[event-store|Event Store]], keyed by the identity of the root [[entity|Entity]].

## Reconstitution and snapshots

When a [[repository|Repository]] retrieves an Aggregate, it is rebuilt by replaying its [[domain-event|Domain Events]] oldest-first, each event applied to mutate state, until the Aggregate reaches its most recent state. Because replaying thousands or millions of events would be a bottleneck, an optimization stores periodic **snapshots**: the Aggregate is loaded to a point in history, serialized, and saved; thereafter it is instantiated from the latest snapshot and only newer events are replayed. Snapshots are taken at intervals (e.g. every 50–100 events), tuned by domain heuristics (raw L3639). See [[aggregate-snapshot]] for the full mechanics, including the critical replay-only path.

## A+ES mechanics — reconstitute by replaying, produce by Apply()

An A+ES Aggregate is rebuilt from history by feeding its event stream through the constructor, which applies each event via a `Mutate()` method. `Mutate()` dispatches (here via .NET dynamics) to an overloaded `When()` handler matched to the event's concrete type; each `When()` sets fields:

```
public Customer(IEnumerable<IEvent> events) {
  foreach (var @event in events) Mutate(@event);
}
public void Mutate(IEvent e) { ((dynamic)this).When((dynamic)e); }
public void When(CustomerLocked e)   { ConsumptionLocked = true; }
public void When(CustomerUnlocked e) { ConsumptionLocked = false; }
```

> "After Mutate() has completed, the Customer instance has a completely reconstituted state." (raw L14510)

The crucial discipline: `When()` handlers only mutate in-memory state. They contain **no business decisions and no validation** — decisions were already made when the event was first produced. Replay must be a pure state fold.

A behavior does *not* mutate fields directly. It decides what happened, constructs the corresponding event, and passes it to `Apply()`, which appends the event to a `Changes` collection (for later persistence) and immediately calls `Mutate()` so in-memory state is current for any subsequent step of the same behavior:

```
void Apply(IEvent event) {
  Changes.Add(event);   // stage for persistence
  Mutate(event);        // update current state now
}
public void LockCustomer(string reason) {
  if (!ConsumptionLocked)
    Apply(new CustomerLocked(_state.Id, reason));
}
```

> "All Events added to the Changes collection will be persisted as newly appended. Since each Event is also used to immediately mutate the Aggregate's state, if a behavior has multiple steps, each subsequent step has up-to-date state to operate on." (raw L14552)

Guarding with `if (!ConsumptionLocked)` shows how [[aggregate|invariants]] are still enforced: no event is emitted if the operation would be a no-op or violate a rule. For clarity the implementation can be split into a state object and a behavior object collaborating *only* through `Apply()` — this "ensures that state is mutated only by means of Events" (raw L14596).

## Where it sits — the Application Service loop

A+ES is driven from an [[application-service|Application Service]] that loads the stream, reconstitutes the Aggregate, invokes a command method (double-dispatching any needed [[domain-service|Domain Services]]), and appends the resulting `Changes` back to the store guarded by the stream version:

1. Client invokes an Application Service method (or a [[command-handler|Command Handler]]).
2. Obtain any Domain Services needed.
3. From the supplied identity, retrieve the Event Stream.
4. Reconstitute the Aggregate by applying all events.
5. Execute a business operation.
6. The Aggregate may double-dispatch to Domain Services / other Aggregates and generates new Events.
7. Append the new Events to the stream, using the stream version to guard against conflicts (see [[optimistic-concurrency-control]]).
8. Publish the newly appended Events to subscribers via messaging infrastructure.

## Consequences for the tactical model — why it pairs with CQRS

Event Sourcing "leans heavily in the direction of technical solution" and "replaces and is far different from using an ORM tool" (raw L3645). Because events are stored as (often binary) representations, they cannot be queried well; Repositories reduce to a single get/find by Aggregate identity, and the Aggregates have no query methods (getters). "As a result, we need another way to query, which generally leads to employing CQRS… hand-in-glove with Event Sourcing" (raw L3645). The [[cqrs|CQRS]] query model is projected from the same event stream via a [[read-model-projection|Read Model Projection]]. You can publish Domain Events without adopting Event Sourcing, and use CQRS without it; the two simply reinforce each other.

## Benefits

- **The reason for every change is never lost.** "Event Sourcing guarantees that the reason for each change to an Aggregate instance will not be lost" (raw L14348) — enabling audit logs, business intelligence, analytics, and time-travel debugging that current-state persistence overwrites.
- **Append-only performance and replication.** Appending to a single stream is extremely fast and supports replication (the appendix cites LMAX's low-latency trading).
- **Structural freedom.** "No matter how complex the structure of a given Aggregate is, it can always be represented with a sequence of serialized Events that can be used to reconstitute it" (raw L14977) — the internal implementation can be restructured with lower risk, a major advantage for long-lived [[bounded-context|Bounded Contexts]].
- **Business wins that sell it:** patch the Event Store with corrective events (with a built-in audit trail); undo/redo by replaying different event sets; answer "what if?" by replaying real history against experimentally enhanced Aggregates — "an alternative way to approach business intelligence" (raw L3655).

## Trade-offs and drawbacks

> "make no mistake: A+ES is not a silver bullet." (raw L14354)

- **High domain-understanding cost.** Defining the right events demands deep domain knowledge — justified mainly for complex, competitively advantageous models; use must be deliberately justified (see [[architecture-selection]]). A common concrete driver is a regulatory requirement to track every change.
- **Immature tooling / scarce expertise** raise cost and risk for inexperienced teams.
- **Forces CQRS.** "since Event Streams are hard to query" (raw L14362), A+ES almost always drags in CQRS to build read models — extra cognitive load and learning curve.

## Failure modes

- Putting business decisions or validation inside `When()`/`Mutate()` handlers — replay must be a pure fold; any decision there re-runs on every reconstitution and corrupts history semantics.
- Adding already-persisted events to `Changes` during replay (reusing `Apply()` instead of a replay-only path), re-appending historic events — see [[aggregate-snapshot]].
- Reaching for A+ES on a CRUD-shaped or generic subdomain where the event history yields no business value but all the CQRS cost still applies.

## Related

- [[event-store]] — the append-only persistence mechanism; [[aggregate-snapshot]] — bounding replay cost.
- [[optimistic-concurrency-control]] — guarding the stream against concurrent writers.
- [[command-handler]], [[command-object]] — how A+ES Aggregates are invoked.
- [[read-model-projection]], [[cqrs]] — the query side Event Sourcing all but requires.
- [[focused-aggregates]], [[given-when-then-specification]], [[functional-event-sourcing]] — aggregate design, testing, and functional restatement under A+ES.
- [[domain-event]] — the stored unit; [[domain-event-enrichment]], [[domain-event-contract-design]], [[value-objects-in-contracts]] — designing durable event contracts.
- [[architecture-selection]] — the risk-driven test that justifies it. [[book-implementing-ddd-vaughn-vernon]] — source summary.
