---
title: "Rule: Model True Invariants in Consistency Boundaries"
category: aggregate-design
summary: Cluster objects into an Aggregate only when a real business invariant forces them to stay transactionally consistent; artificial constraints produce broken boundaries.
tags: [rule, rule-of-thumb, aggregate, invariant, consistency-boundary, transactional-consistency, aggregate-design]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The first and most fundamental [[aggregate]] rule of thumb: to discover Aggregates in a [[bounded-context]] you must first identify the model's **true invariants**, because "Only with that knowledge can we determine which objects should be clustered into a given Aggregate." (raw L8890)

## What an invariant is

> An invariant is a business rule that must always be consistent. (raw L8892)

Consistency comes in two kinds — **transactional consistency** (immediate and atomic) and **eventual consistency** — and this rule is strictly about the former: "When discussing invariants, we are referring to transactional consistency." (raw L8892) The canonical illustration is `c = a + b`: if the rule holds, then with `a=2` and `b=3`, `c` must be `5`; any other value violates the invariant. You enforce it by drawing a consistency boundary around exactly those attributes (raw L8898-8912). This is why *Aggregate* is synonymous with *transactional consistency boundary*.

## One Aggregate instance per transaction

With a typical persistence mechanism a single transaction manages consistency, so when it commits everything inside one boundary must be consistent. The rule of thumb that follows: "a properly designed Bounded Context modifies only one Aggregate instance per transaction in all cases" (raw L8914). Vernon concedes this "may sound overly strict" but it "should be the goal in most cases" because it addresses the very reason Aggregates exist. Legitimate exceptions are in [[reasons-to-break-aggregate-rules]].

A design consequence reaches the UI: each user request should execute a single command on a single Aggregate instance. "If user requests try to accomplish too much, the application will be forced to modify multiple instances at once." (raw L8928)

## True vs. false invariants

The SaaSOvation team's first design (see [[large-cluster-aggregate]]) failed because it clustered on *false* invariants:

> the large-cluster Aggregate was designed with false invariants in mind, not real business rules. These false invariants are artificial constraints imposed by developers. (raw L8781)

Rules like "if a backlog item is committed to a sprint, it must not be removed" felt like invariants but were arbitrary restrictions dressed up as consistency requirements; they could be enforced without clustering everything into one Aggregate. The lesson: "Aggregates are chiefly about consistency boundaries and not driven by a desire to design object graphs." (raw L8930) Because real invariants are usually simple, this frees you to [[design-small-aggregates]].

## Failure mode: don't trust every use case

A use case that calls for modifying **multiple** Aggregate instances within one transaction should be treated with skepticism (raw L8962). It may mean:

- A missing concept in the [[ubiquitous-language]] — an unrecognized invariant "waving its hands and shouting at you." Folding the instances into one new named Aggregate may be the answer (raw L8964).
- ...but if that new concept becomes a [[large-cluster-aggregate]], you've traded one problem for another.
- Often the goal is really achievable with [[eventual-consistency-between-aggregates]] and an acceptable update delay; you may need to rewrite the use case to specify that delay (raw L8972).

> Just because you are given a use case that calls for maintaining consistency in a single transaction doesn't mean you should do that. (raw L8972)

## Related

[[aggregate]] · [[design-small-aggregates]] · [[eventual-consistency-between-aggregates]] · [[large-cluster-aggregate]] · [[bounded-context]]
