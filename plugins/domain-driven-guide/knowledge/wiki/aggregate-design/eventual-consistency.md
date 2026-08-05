---
title: Eventual Consistency
category: aggregate-design
summary: "The deliberate acceptance of latency between models: one aggregate commits in a transaction, others (local or remote) catch up asynchronously via domain events — supporting the one-aggregate-per-transaction rule and avoiding two-phase commits."
tags: [concept, eventual-consistency, aggregate-design, domain-event, transactions, latency, consistency-boundary]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Eventual consistency** is the deliberate acceptance that changes in one model which must influence other models "will not be fully consistent for some elapsed period of time" (raw L7474). In DDD it is the standard way to coordinate multiple [[aggregate]]s and multiple [[bounded-context]]s using [[domain-event]]s rather than large, global transactions. "This is purposeful and by design" (raw L7037).

This page covers the general principle as introduced in the Domain Events chapter. For its concrete form as the fourth Aggregate rule of thumb — how to *implement* cross-Aggregate consistency and the "Whose job is it?" tie-breaker — see [[eventual-consistency-between-aggregates]].

## Why it exists — the Aggregate rule

Eventual consistency directly supports the aggregate transaction rule: "only a single instance should be modified in a single transaction, and all other dependent changes must occur in separate transactions" (raw L7037). When one [[aggregate]] changes, it publishes a [[domain-event]]; other aggregates in the same context, and aggregates in remote contexts, are synchronized in *separate* transactions as they react to that Event. This "can eliminate the need for two-phase commits (global transactions)" (raw L7037) and yields "a highly scalable and peak-performing set of cooperating services ... loose coupling between systems" (raw L7037).

The corollary rule for Event handlers: never modify a second aggregate synchronously in the same transaction — "the consistency of all Aggregate instances other than the one used in the single transaction must be enforced by asynchronous means" (raw L7462) (see [[domain-event-publisher]]).

## Batch processing made redundant

Vernon frames Events as a replacement for costly nightly batch-processing catch-up: if "each of those discrete occurrences were captured by a single Event, and published to listeners", the complex reconciling queries vanish because "you would know exactly what occurred and when" — work "spread out into short spurts throughout the day" so "business situations would be in harmony much more quickly" (raw L7045-7047).

## Latency tolerances — a business question, not a technical default

The key trade-off is delay, and how much is acceptable is a domain question: "Domain experts will likely be very much in tune with what constitutes acceptable and unacceptable delays" (raw L7508). Counter-intuitively, "most times, several seconds, minutes, hours, or even days between consistent states is completely tolerable" (raw L7508). A useful heuristic: "How did the business work prior to computers, or how would it work without them now?" — since even paper systems were rarely immediately consistent, "eventual consistency makes better business sense" (raw L7510). Example: a `TeamActivityApproved` Event scheduling an activity that is weeks away tolerates minutes or even hours of delay (raw L7512-7514). Where higher throughput is required, "Maximum latency tolerances should be well understood and systems should have the architectural qualities to meet them" (raw L7524).

## Failure modes

- **Assuming near-immediate consistency is always required** — the chapter warns "we must not assume that in any given domain, near-consistent time frames are always imperative" (raw L7508).
- **Acting on stale data where the domain can't tolerate the delay** — "out-of-sync data could influence wrong and even damaging actions" (raw L7506); latency must be measured against the domain's real tolerance, not guessed at.

Related: [[domain-event]], [[aggregate]], [[eventual-consistency-between-aggregates]], [[domain-event-publisher]], [[event-driven-integration]], [[bounded-context]].
