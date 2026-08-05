---
title: "Rule: Reference Other Aggregates by Identity"
category: aggregate-design
summary: Hold foreign Aggregates by their globally unique id rather than a direct object pointer; this keeps Aggregates small, enforces one-per-transaction, and enables scale.
tags: [rule, rule-of-thumb, aggregate, aggregate-design, identity-reference, scalability, disconnected-domain-model]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The third [[aggregate]] rule of thumb. An Aggregate may reference the Root of another Aggregate, but holding a reference does **not** pull the referenced Aggregate inside the referrer's consistency boundary — "There are still two (or more)" Aggregates (raw L8976).

## Prefer identity references over pointers

> Prefer references to external Aggregates only by their globally unique identity, not by holding a direct object reference (or "pointer"). (raw L9009)

So `BacklogItem` holds a `ProductId`, not a `Product` object (raw L9013-9023). The payoff: "Aggregates with inferred object references are thus automatically smaller because references are never eagerly loaded. The model can perform better because instances require less time to load and take less memory" — with knock-on benefits for allocation and garbage collection (raw L9025).

## Implications

1. The referencing Aggregate (`BacklogItem`) and the referenced one (`Product`) **must not** both be modified in one transaction — only one or the other (raw L8999).
2. If you find yourself modifying multiple instances in one transaction, your consistency boundaries are probably wrong, or a [[ubiquitous-language]] concept is undiscovered (raw L9001).
3. If fixing that would push you toward a [[large-cluster-aggregate]], that's the signal to reach for [[eventual-consistency-between-aggregates]] instead of atomic consistency (raw L9003).

## Model navigation without pointers

Reference by identity doesn't forbid navigation. Two approaches:

- **Disconnected Domain Model** — call a [[repository]] from *inside* the Aggregate to look up dependents. This is a form of lazy loading, and Vernon treats it as the *less favored* option (raw L9029, L9552).
- **Preferred**: use a [[repository]] or [[domain-service]] to look up dependent objects *ahead of* invoking the Aggregate behavior — typically the [[application-service]] resolves them and passes them in (raw L9029-9057). For complex, domain-specific resolution, pass a Domain Service into the command method and let the Aggregate *double-dispatch* to it (raw L9059).

### Corollary: avoid dependency injection into Aggregates

> Dependency injection of a Repository or Domain Service into an Aggregate should generally be viewed as harmful. (raw L9552)

Look up dependencies before the command method is called and pass them in; injecting Repositories/Domain Services into Aggregates adds object-reference overhead in high-volume domains (extra references, GC pressure) and encourages the Disconnected Domain Model. DI remains fine for [[application-service|Application Services]] (raw L9552-9558).

## Scalability and distribution

Because Aggregates hold ids rather than pointers, their persistent state can be repartitioned freely — Pat Helland's "almost-infinite scalability" via continuous repartitioning (what he calls an *entity* is Vernon's Aggregate: a unit of composition with transactional consistency) (raw L9073). Identity references also make **distribution** across [[bounded-context|Bounded Contexts]] natural: [[domain-event|Domain Events]] carrying Aggregate identities travel the enterprise, and subscribers in foreign contexts use those ids to act in their own models. Transactions across distributed systems are not atomic — the systems reach consistency eventually (raw L9075).

## Trade-off: read-side inconvenience

Identity-only references make it harder to assemble UI views — you may need several Repositories per use case. If query overhead bites, options are *theta joins* (Hibernate can assemble referentially associated Aggregates in one join query) or **CQRS**; failing those, strike a balance with some direct references (raw L9067). This is also one of the sanctioned [[reasons-to-break-aggregate-rules]].

## Related

[[aggregate]] · [[design-small-aggregates]] · [[eventual-consistency-between-aggregates]] · [[domain-event]] · [[repository]] · [[domain-service]]
