---
title: "Rule: Design Small Aggregates"
category: aggregate-design
summary: Limit an Aggregate to its Root plus the minimum attributes and value-typed properties a true invariant requires; small Aggregates perform, scale, and commit better.
tags: [rule, rule-of-thumb, aggregate, aggregate-design, value-object, performance, scalability]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The second [[aggregate]] rule of thumb. Once invariants no longer force a large cluster (see [[model-true-invariants-in-consistency-boundaries]]), keep every Aggregate as small as it can be.

## Why small

Even if you could *guarantee* every transaction succeeded, a large cluster still "limits performance and scalability" (raw L8934). The concrete cost: adding one backlog item to a years-old `Product` with thousands of existing ones can force thousands of objects into memory just to append one element — and worse without lazy loading, since operations like scheduling for release load whole collections at once (raw L8936). "Don't let the 0..* fool you; the number of associations will almost never be zero and will keep growing over time." (raw L8938) Multiplied across many tenants, teams, and products, "This large-cluster Aggregate will never perform or scale well." (raw L8944)

A third benefit is transactional: "Smaller Aggregates not only perform and scale better, they are also biased toward transactional success, meaning that conflicts preventing a commit are rare." (raw L8958)

## What "small" means

Not an absurd Root-plus-one-attribute minimum, but: "limit the Aggregate to just the Root Entity and a minimal number of attributes and/or Value-typed properties... The correct minimum is however many are necessary, and no more." (raw L8946)

Which attributes are *necessary*? Those that must stay consistent with the others — including **implicit** invariants domain experts never state as rules. A `Product`'s `name` and `description` belong together not by decree but because you'd never sensibly keep them in separate Aggregates (raw L8948).

## Favor value-object parts

When tempted to model a contained part as an [[entity]], first ask whether it must change over time or can simply be **replaced** wholesale. Replaceable parts point to [[value-object|Value Objects]] (raw L8950). Advantages of value parts:

- They can often be serialized with the Root; Entity parts may need separately tracked storage and SQL joins (higher overhead — reading one table row is faster) (raw L8952).
- They are smaller, safer, and easier to unit-test for correctness thanks to immutability.
- Favoring value parts does **not** make the Aggregate immutable — the Root mutates when one of its value-typed properties is replaced.

Evidence: on a financial-derivatives project Niclas Hedhman's team modeled roughly 70% of Aggregates as a Root plus value-typed properties, the remaining 30% with just two–three total Entities (raw L8954). Evans' purchase-order example (line-item total must not exceed a limit, tricky under concurrent additions) shows that multi-Entity Aggregates are sometimes genuinely needed — but such cases are the exception (raw L8956).

## Case study: Back-of-the-envelope cost estimation

Before committing to a boundary, estimate its cost. For `BacklogItem` composing `Task`s that each hold `EstimationLogEntry` value objects, the team ran BOTE numbers: a ~12-day sprint, ~12 tasks per backlog item, ~12 estimation logs per task ≈ 144 total collected objects — but they then asked how many load *per request* (raw L8245-8277). Because estimates are logged by date as Value Objects (a same-day re-estimate replaces the prior value, not appends), and lazy loading pulls only one task's log collection at a time, a single re-estimation touches at most **one backlog item + 12 tasks + 12 log entries ≈ 25 objects** — "That's not very many; it's a small Aggregate." (raw L9277) The invariant (status auto-transitions to *done* only when the final task hits zero hours) held with only the last of 144 estimates ever modifying the Root. The exercise, "30 minutes, and perhaps as much as 60 minutes at worst" (raw L9375), is presented as well worth it for the insight it yields.

## Related

[[aggregate]] · [[value-object]] · [[model-true-invariants-in-consistency-boundaries]] · [[reference-other-aggregates-by-identity]] · [[large-cluster-aggregate]]
