---
title: "Optimistic Concurrency in Aggregates: Where to Place the Version"
category: aggregate-design
summary: How to position the optimistic-concurrency version so that changes anywhere inside an Aggregate protect its invariants, without leaking infrastructure into the model.
tags: [technique, aggregate, optimistic-concurrency, versioning, invariant, implementation, aggregate-design]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Optimistic concurrency protects [[aggregate|Aggregate]] persistent state without database locks: each instance carries a `version` that is incremented on change and checked at save; a stale client's update is rejected (see the failure cascade in [[large-cluster-aggregate]]). The design question is *where* the version lives (raw L9506-9548).

## The ideal, and why it's hard

Safest in theory is to version **only the Root** and bump it on any state-altering command anywhere inside the boundary, no matter how deep — this blocks any concurrent modification of the same Aggregate. But with Hibernate this isn't automatic: modifying a `ProductBacklogItem` part is not seen as modifying the `Product` Root (raw L9508-9510). Manually incrementing the Root's version inside `reorderFrom()` works but "always dirties the `Product`, even when a reordering command actually has no effect" and "leaks infrastructural concerns into the model" (raw L9530).

## Three better approaches

1. **Version the Entity parts individually.** If interior parts are themselves [[entity|Entities]], let each carry its own version. Two clients reordering the same `ProductBacklogItem` — the later commit fails. This is often enough (overlapping reorders are rare, usually only the product owner reorders) (raw L9540). It does not cover every case: "Sometimes the only way to protect an invariant is to modify the Root version."
2. **Modify a legitimate Root property in response to a deep change.** When a part change must bump the Root, arrange for it to change a real Root property, so Hibernate increments the version naturally. This is exactly the `BacklogItem` status trick: the Root's `status` transitions to *done* (bumping its version) only when all `Task` instances reach zero hours (raw L9542). Because only the *final* estimate changes the Root, task edits stay independent.
3. **Persist the whole Aggregate as one value.** With MongoDB, Riak, Oracle Coherence, or GemFire the entire Aggregate is one stored value, so the value itself prevents concurrency conflict — e.g. a Root implementing Coherence's `Versionable` with a `VersionedPut` entry processor is the single object used for conflict detection (raw L9548).

## What to avoid

Resorting to persistence-mechanism life-cycle hooks to manually dirty the Root "becomes problematic": it usually requires **bidirectional associations** from child parts back to the Root purely to service optimistic concurrency — and Evans generally discourages bidirectional associations, especially when kept only for an infrastructural concern (raw L9544).

## The design signal

> When modifying the Root becomes very difficult and costly, it could be a strong indication that we need to break down our Aggregates to just a Root Entity, containing only simple attributes and Value-typed properties. When our Aggregates consist of only a Root Entity, the Root is always modified when any part is modified. (raw L9546)

So concurrency pain is itself an argument for [[design-small-aggregates]] and favoring [[value-object]] parts.

## Related

[[aggregate]] · [[design-small-aggregates]] · [[large-cluster-aggregate]] · [[aggregate-information-hiding]] · [[entity]]
