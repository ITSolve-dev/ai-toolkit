---
title: Persistence-Oriented Repository
category: building-blocks
summary: A save-based Repository style (save/saveAll) used when the store does not track object changes — NoSQL key-value stores, in-memory Data Fabrics, or as a hedge against future persistence swaps.
tags: [pattern, repository, persistence, aggregate, nosql, serialization]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **persistence-oriented Repository** (also called *save-based*) is a [[repository]] whose interface exposes `save()` / `saveAll()` (plus `remove()` / `removeAll()`) instead of the `add()` / `addAll()` of a [[collection-oriented-repository]]. You reach for it when the underlying persistence mechanism does not implicitly track and persist changes to already-loaded objects.

> "For times when a collection-oriented style doesn't work, you will need to employ a persistence-oriented, save-based Repository. This will be the case when your persistence mechanism doesn't implicitly or explicitly detect and track object changes." (raw L10516)

## The defining difference: save on create AND on modify

A collection-oriented Repository mimics an in-memory collection so faithfully that a client `add()`s an [[aggregate]] only once, at creation, and later modifications are transparently persisted by the backing Unit of Work. A persistence-oriented store has no such Unit of Work, so the client must explicitly re-save every time it mutates an Aggregate:

> "We must explicitly `put()` both new and changed objects into the store, effectively replacing any value previously associated with the given key." (raw L10522)

```java
Product product = new Product(...);
productRepository.save(product);            // save on create
// later ...
product = productRepository.productOfId(tenantId, productId);
product.reprioritizeFrom(backlogItemId, orderOfPriority);
productRepository.save(product);            // must save AGAIN on modify
```

Because there is no change tracking, "each `put()` and `putAll()` represents a separate logical transaction" (raw L10526) — there is no atomic multi-write demarcation for free.

## When to use it

1. **The store has no Unit of Work / change tracking.** In-memory Data Fabrics (GemFire, Oracle Coherence) and NoSQL key-value / document stores (MongoDB, Riak) give the *illusion* of a `Map`-like collection but require an explicit `put()` of new and changed values (raw L10524). These are "sometimes called Aggregate Stores or Aggregate-Oriented Databases" (raw L10522) because they store a whole Aggregate under its identity key.
2. **As a hedge against a future persistence swap.** Even with an ORM that supports the collection-oriented style, if there is a realistic chance you will later move to a key-value store, designing save-based up front avoids ripple through the [[application-service]] layer: "You'd have a lot of ripple through your Application Layer as it would have to be changed to use `save()` in all places where Aggregate updates occur" (raw L10518). The Repository pattern then lets you "completely replace your persistence mechanism with potentially little impact on your application."

## Trade-offs

- **Simplicity of basic reads/writes.** Aggregate-oriented stores make the elementary `put()`/`get()` of a whole Aggregate trivial (raw L10522).
- **Portability at the cost of discipline.** The downside of using save-based methods over an ORM that *does* track changes: "your current object-relational mapper may cause you to leave out necessary uses of `save()` that you may catch only later when there is no longer a backing Unit of Work" (raw L10518). This is the chief **failure mode** — a forgotten `save()` after a mutation silently loses the change because nothing else flushes it.
- **Serialization becomes a modeling force.** Standard Java serialization on a Data Fabric "requires a premium of bytes ... and it performs relatively poorly" (raw L10539). High-performance domains need custom/compact serializers, so "distribution is introduced into your system. That will often bring a new force into domain model design, namely, custom or at least specialized serialization" (raw L10539). MongoDB's BSON serializer using **direct field access** frees domain objects from JavaBean getters/setters, which "tends to steer you away from an Anemic Domain Model" (raw L10787) — see [[anemic-domain-model]].
- **Batching over network stores.** `saveAll()` should collect instances into a local map and issue one `putAll()` rather than looping `save()`, because each `put()` may be a network round-trip (raw L10696). But `removeAll()` often cannot batch — `java.util.Map` offers no batch remove, so it iterates, accepting partial-failure risk that Data Fabric redundancy/high-availability is expected to offset (raw L10718).
- **Lazy schema migration.** With document stores you can register field override-mappings (e.g. map an old `description` field to `summary` on deserialize) instead of running a mass migration, but instances never re-read-and-saved keep the obsolete field names — "You'll have to weigh the trade-offs of this lazy migration approach" (raw L10806).

## Related

Contrast with [[collection-oriented-repository]]. Both are variants of the [[repository]] pattern and store whole [[aggregate]] instances by identity. See [[testing-repositories]] for the in-memory `HashMap` edition, which is naturally save-based. Related: [[application-service]] · [[anemic-domain-model]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
