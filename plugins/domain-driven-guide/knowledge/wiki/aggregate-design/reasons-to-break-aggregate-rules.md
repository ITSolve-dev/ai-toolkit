---
title: Reasons to Break the Aggregate Rules
category: aggregate-design
summary: Four justified exceptions to one-Aggregate-per-transaction and reference-by-identity — UI batch convenience, missing async infrastructure, global transactions, and query performance.
tags: [heuristic, aggregate, aggregate-design, trade-offs, user-aggregate-affinity]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The [[aggregate]] rules — one instance modified per transaction, and [[reference-other-aggregates-by-identity]] — are *rules of thumb*. An experienced practitioner may break them, "but only with good reason." Vernon lists four (raw L9141). "Certainly we don't go in search of excuses to break the Aggregate Rules of Thumb" (raw L9209).

## Reason 1: User-interface convenience

A UI may let a user batch-create many things at once (e.g. several backlog items sharing common properties). Persisting the whole batch in one transaction is fine here, because each object created is a *full Aggregate maintaining its own invariants*: "if creating a batch of Aggregate instances all at once is semantically no different from creating one at a time repeatedly, it represents one reason to break the rule of thumb with impunity." (raw L9179) Note this creates independent Aggregates in one transaction — it does not modify several interdependent ones.

## Reason 2: Lack of technical mechanisms

[[eventual-consistency-between-aggregates|Eventual consistency]] needs out-of-band processing — messaging, timers, or background threads. A project with none of these has no way to converge separate Aggregates asynchronously (raw L9183). The wrong response is to regress to a [[large-cluster-aggregate]]; sometimes the only remaining option is to modify two or more instances in one transaction — but "such a decision should not be made too hastily."

**Mitigant — user-aggregate affinity:** if business workflow means only one user focuses on a given set of instances at a time, multi-instance transactions are safer, tending to prevent invariant violations and collisions. Each Aggregate is still protected by optimistic concurrency, and rare conflicts are straightforward to recover from (raw L9193).

## Reason 3: Global transactions

Legacy tech or enterprise policy may mandate global, two-phase-commit transactions you can't push back on short-term. Even then, you can often still avoid modifying multiple Aggregate instances within your *local* [[bounded-context]], preserving the rules where you're able. The cost: "your system will probably never scale as it could if you were able to avoid two-phase commits and the immediate consistency that goes along with them." (raw L9201)

## Reason 4: Query performance

Sometimes holding a direct object reference to another Aggregate (instead of by identity) eases [[repository]] query performance — weighed carefully against the size and performance trade-offs (raw L9205). See the read-side discussion in [[reference-other-aggregates-by-identity]] (theta joins, CQRS).

## Bottom line

UI decisions, technical limits, and stiff policies may force compromises, but "In the long run, adhering to the rules will benefit our projects" — consistency where necessary, plus optimal performance and scalability (raw L9209).

## Related

[[aggregate]] · [[eventual-consistency-between-aggregates]] · [[reference-other-aggregates-by-identity]] · [[large-cluster-aggregate]] · [[aggregate-optimistic-concurrency]]
