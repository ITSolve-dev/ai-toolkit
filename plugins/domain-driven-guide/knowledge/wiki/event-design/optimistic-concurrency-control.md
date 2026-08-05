---
title: Optimistic Concurrency Control for Event-Sourced Aggregates
category: event-design
summary: Guarding an Aggregate's Event Stream against concurrent writers with an expected-version check, and the escalating responses to a conflict — propagate, automatic retry (replay-and-reexecute), and type-based Event conflict resolution.
tags: [technique, event-sourcing, concurrency, optimistic-concurrency, aggregate, conflict-resolution, consistency]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Because an [[aggregate|Aggregate]] is the transactional consistency boundary, concurrent modifications to one instance must be serialized. In [[event-sourcing|A+ES]] the Aggregate's Event Stream can be read by many threads at once, so two threads can each load version N, decide, and try to append — the classic lost-update race.

> "Aggregate Event Streams can be accessed and read by multiple threads simultaneously. This opens up the real potential for concurrency conflicts that, if left unchecked, could result in a random number of invalid Aggregate states." (raw L14845)

The mechanism is **optimistic** concurrency control: no locks are held while the Aggregate is in use. Instead the stream version observed at load time is passed to [[event-store|AppendToStream]] as `expectedVersion`; the store appends only if the stream head is still at that version, otherwise it throws:

```
public class EventStoreConcurrencyException : Exception {
    public List<IEvent> StoreEvents { get; set; }
    public long StoreVersion { get; set; }
}
```

The exception carries the events that were committed by the other writer and the store's actual version — enough information to recover intelligently. There are three escalating responses.

## 1. Propagate to the client

The simplest resolution: let `EventStoreConcurrencyException` propagate to the ultimate client, which then instructs the user to retry manually. Correct but user-hostile and rarely what you want by default.

## 2. Automatic retry (replay and re-execute)

Better: catch the exception and retry the whole load-decide-append cycle in a loop. On conflict the Aggregate is reloaded from the *now-longer* stream and the behavior delegate is re-executed against fresh state, producing new events that append cleanly after the events that won the race.

```
void Update(CustomerId id, Action<Customer> execute) {
  while (true) {
    EventStream eventStream = _eventStore.LoadEventStream(id);
    var customer = new Customer(eventStream.Events);
    try {
      execute(customer);
      _eventStore.AppendToStream(id, eventStream.Version, customer.Changes);
      return;
    } catch (EventStoreConcurrencyException) {
      // fall through and retry, with optional brief delay
    }
  }
}
```

Expressing the behavior as a lambda (`Action<Customer>`) is what makes automatic retry possible: the captured behavior can be replayed against a different, freshly-loaded `Customer` instance. This is the practical payoff of the lambda helper introduced for A+ES Application Services.

**Limit:** retry is unsafe or too costly when re-executing the behavior has external side effects — placing an order, charging a credit card, or other expensive third-party integration would be repeated on each retry.

## 3. Event conflict resolution

When re-execution is infeasible, reduce the number of *real* conflicts by asking whether the concurrently-appended events actually conflict with the ones this operation produced. On the concurrency exception, compare each staged event against each event that succeeded; only a genuine clash escalates to a `RealConcurrencyException`, otherwise the changes are appended at the store's actual version.

```
foreach (var failedEvent in customer.Changes)
  foreach (var succeededEvent in ex.ActualEvents)
    if (ConflictsWith(failedEvent, succeededEvent))
      throw new RealConcurrencyException(...);
// no conflicts -> append at the store's actual version
_eventStore.AppendToStream(id, ex.ActualVersion, customer.Changes);
```

The conflict predicate is usually defined **per Aggregate Root**, tuned to the behaviors it supports. A default that works for most Aggregates uses event type as the proxy for conflict:

```
bool ConflictsWith(IEvent event1, IEvent event2) {
  return event1.GetType() == event2.GetType();
}
```

> "Events of the same type always conflict with each other, but Events of different types do not." (raw L14973)

The reasoning: two writers appending the *same kind* of change genuinely contend, but unrelated changes (e.g. a lock and an address update) can safely coexist in the stream.

## Failure modes

- Applying blind automatic retry to behaviors with non-idempotent external side effects — the side effect fires on every attempt.
- Omitting `expectedVersion` on append (or backing the store with an eventually-consistent store), which silently permits lost updates and "a random number of invalid Aggregate states."
- Over-broad conflict rules that treat everything as conflicting, negating the whole point of conflict resolution and pushing avoidable failures onto users.

## Related

[[event-sourcing]] · [[event-store]] · [[aggregate]] · [[command-handler]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
