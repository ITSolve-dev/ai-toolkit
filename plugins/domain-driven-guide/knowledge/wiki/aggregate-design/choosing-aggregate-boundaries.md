---
title: Choosing Aggregate Boundaries
category: aggregate-design
summary: How to pick which objects cluster into an aggregate — driven by shared invariants and the right granularity, kept as small as performance allows, and revisited over time; there is no single correct aggregate.
tags: [heuristic, aggregate-design, granularity, aggregate, consistency-boundary, performance, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Choosing Aggregate Boundaries

Choosing which objects belong together in an [[aggregate]] is "somewhat arbitrary, but it's important" (raw L3276). The boundary you pick becomes the [[consistency-boundary]] the system serializes writes over, so the decision shapes both correctness and performance. This page collects the heuristics the book uses to arrive at `Product` as the allocation aggregate.

## Drive the boundary from invariants

The cluster should contain exactly the objects that must be consistent with one another — i.e. the objects a shared [[invariants-and-constraints|invariant]] spans. Objects with no invariant between them belong in *different* aggregates so they can change concurrently. In allocation, the invariant ("don't oversell a SKU") relates only batches of the *same SKU*, which is the clue that points to a per-SKU aggregate.

## Get the granularity right

The book explicitly tries and rejects candidates that have the wrong granularity:

- **`Shipment`** — each shipment holds several batches that travel together, but we must be able to allocate across shipments.
- **`Warehouse`** — each warehouse holds many batches, but we must allocate across warehouses too.

> "We should be able to allocate `DEADLY-SPOON`s or `FLIMSY-DESK`s in one go, even if they're not in the same warehouse or the same shipment. These concepts have the wrong granularity." (raw L3288)

What we actually care about when allocating a line is *only the batches with the same SKU*. That points to `GlobalSkuStock` — a collection of all batches for a given SKU — ultimately (after bikeshedding through `SkuStock`, `Stock`, `ProductStock`) named **`Product`**, reusing the domain-language term from chapter 1. The aggregate's identifier is the `sku`.

## Prefer the smallest boundary that holds the invariant

Smaller aggregates lock fewer rows and allow more concurrency, so pick the smallest cluster that still keeps all its invariants true (see [[consistency-boundary]]). Give it a good, business-meaningful name.

## "Loading all the batches" is acceptable — know why

`Product.allocate()` loads *all* the SKU's batches to use just one, which looks inefficient. The book is comfortable for three concrete reasons (raw L3449–3453):

1. It enables **a single query to read and a single update to persist** — which outperforms systems that issue many ad hoc queries and whose transactions grow more complex over time.
2. The rows are **minimal** (a few strings and integers), so hundreds load in milliseconds.
3. There are only **~20 active batches per product**; used-up batches drop out, so the working set stays bounded.

## Escape hatches if the boundary hurts

If you *did* expect thousands of active batches per product (raw L3455–3467):

- **Lazy-loading**: SQLAlchemy pages through batches transparently; since you only need one batch with enough capacity, more but smaller queries can work well.
- **Pick a different aggregate**: split batches by region or warehouse, or redesign data access around the shipment concept.

## There is no one correct aggregate

The boundary is an engineering trade-off around consistency and performance, not a truth about the domain:

> "There isn't *one* correct aggregate, and we should feel comfortable changing our minds if we find our boundaries are causing performance woes." (raw L3466)

> "Choosing the right aggregate is key, and it's a decision you may revisit over time." (raw L3665)

The book points at Vaughn Vernon's "effective aggregate design" papers for deeper treatment — the same material distilled in this wiki under [[design-small-aggregates]] and [[model-true-invariants-in-consistency-boundaries]].

## Failure modes

- **Choosing a physical/organizational grouping** (Shipment, Warehouse) that doesn't match the invariant's scope — you end up unable to perform the core operation in one transaction.
- **Treating the choice as permanent** — refusing to revisit a boundary that is causing deadlocks or slow transactions.
- **Bloating the aggregate** with data the operation doesn't need (this `Product` deliberately has no price/description/dimensions).

## Related

[[aggregate]] · [[consistency-boundary]] · [[invariants-and-constraints]] · [[aggregate-concurrency-control]] · [[bounded-context]] · [[design-small-aggregates]] · [[model-true-invariants-in-consistency-boundaries]]
