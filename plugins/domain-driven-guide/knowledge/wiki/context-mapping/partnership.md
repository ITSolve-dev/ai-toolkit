---
title: Partnership
category: context-mapping
summary: An organizational relationship where two contexts' teams succeed or fail together, so they coordinate planning and jointly manage integration.
tags: [pattern, context-mapping, team-relationship, integration, partnership]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Partnership** is one of the DDD organizational relationships between two [[bounded-context]]s. "When
teams in two Contexts will succeed or fail together, a cooperative relationship needs to emerge." (raw
L2475)

## Definition

The teams institute a process for coordinated planning of development and joint management of
integration. They must cooperate on the evolution of their interfaces to accommodate the development
needs of both systems, and interdependent features should be scheduled so they are completed for the
same release (raw L2475). *(Definition largely quoted from Evans, raw L2473.)*

## When to use it

Apply Partnership when the mutual dependency is genuine and symmetric — neither side can ship
successfully without the other. It sits at the high-coordination end of the spectrum, distinct from the
asymmetric [[upstream-downstream]] arrangements of [[customer-supplier-development]] and [[conformist]].

## Trade-offs

What you gain is aligned delivery and interfaces that evolve together. What you pay is a continuous
coordination cost: joint planning, synchronized release scheduling, and shared integration management.
Partnership is worth that overhead only when the two contexts truly rise or fall together; imposing it
where dependencies are one-directional wastes coordination effort that a lighter relationship
(Customer-Supplier, or even [[separate-ways]]) would avoid.

## Related

- [[context-map]] — where the relationship is labelled.
- [[upstream-downstream]] — the asymmetric alternative axis.
- [[customer-supplier-development]], [[conformist]], [[separate-ways]] — the other organizational
  relationships.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
