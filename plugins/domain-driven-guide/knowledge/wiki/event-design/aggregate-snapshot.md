---
title: Aggregate Snapshot
category: event-design
summary: A performance optimization for event-sourced Aggregates — persist a serialized copy of full state at a stream version so reconstitution replays only the events since that version, plus the replay-only path, caching, and identity partitioning.
tags: [pattern, event-sourcing, snapshot, performance, aggregate, optimization, partitioning]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Loading an [[event-sourcing|event-sourced]] [[aggregate|Aggregate]] means replaying its whole Event Stream. When streams grow very large — the appendix cites individual streams beyond hundreds of thousands of events — reconstitution becomes a performance problem. A **snapshot** is the standard remedy.

> "snapshots are just serialized copies of an Aggregate's full state, taken at certain moments in time, that reside in the Event Stream as specific versions." (raw L14997)

Instead of replaying from event 1, you load the latest snapshot as the base state and replay only the events appended *after* the snapshot's version. Snapshots are stored separately from the [[event-store]], behind their own repository interface that records the stream version alongside the state:

```
public interface ISnapshotRepository {
  bool TryGetSnapshotById<TAggregate>(IIdentity id, out TAggregate snapshot, out int version);
  void SaveSnapshot(IIdentity id, TAggregate snapshot, int version);
}
```

The version is essential — it tells you exactly which suffix of the stream still needs replaying:

```
if (_snapshots.TryGetSnapshotById(id, out customer, out snapshotVersion)) {
  EventStream stream = _store.LoadEventStreamAfterVersion(id, snapshotVersion);
  customer.ReplayEvents(stream.Events);   // NOT Apply()
  return customer;
} else {
  return new Customer(_store.LoadEventStream(id).Events);
}
```

## The replay-only path: why not Apply()

A subtle but critical correctness rule: the events loaded after a snapshot are *already persisted*, so they must update state without being re-staged for persistence. `Apply()` is wrong here — it both mutates state and adds the event to the `Changes` collection, and re-persisting already-stored events corrupts the stream. A dedicated `ReplayEvents()` calls only `Mutate()`:

```
public void ReplayEvents(IEnumerable<IEvent> events) {
  foreach (var event in events) Mutate(event);
}
```

> "we can't just use Apply() because it not only mutates the current state with the given Event, it also saves each Event it receives to the Changes collection. Saving Events to Changes that are already in the Event Stream would cause serious bugs." (raw L15048)

## Generation, thresholds, and tuning

Snapshot creation loads the full stream once and saves the resulting state at the current version. It is delegated to a background thread and triggered only after a set number of events have accrued since the last snapshot. Because different Aggregate types have different characteristics, the snapshot threshold is tuned per type.

## Complementary performance techniques

- **Cache Event Streams in memory.** Events are immutable once written, so a cached stream can be extended by querying only for events after the last known version. Trades memory for speed.
- **Partition by identity.** Distribute Aggregate instances across processes or machines by hashing the Aggregate identity. This combines with both in-memory caching and snapshots. > "partition Aggregates among multiple processes or machines by Aggregate identity." (raw L15087)

## Failure modes

- Using `Apply()` instead of a replay-only method when loading post-snapshot events, re-appending historic events and corrupting the stream.
- Reaching for snapshots prematurely — for typical stream sizes plain replay is fine; snapshots add moving parts (a second store, staleness, thresholds) and are warranted only when reconstitution is actually slow.
- A single global snapshot threshold, ignoring that different Aggregate types have very different event volumes and cost profiles.

## Related

[[event-sourcing]] · [[event-store]] · [[aggregate]] · [[repository]] · [[functional-event-sourcing]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
