---
title: Separate Ways
category: context-mapping
summary: Declaring that a Bounded Context has no connection to others, so its team can find simple, specialized solutions in a small scope — chosen when integration's cost outweighs its small benefit.
tags: [pattern, context-mapping, integration, decision-rule, separate-ways]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Separate Ways** is the decision *not* to integrate. "We must be ruthless when it comes to defining
requirements. If two sets of functionality have no significant relationship, they can be completely cut
loose from each other." (raw L2493)

## Definition

"Declare a bounded context to have no connection to the others at all, enabling developers to find
simple, specialized solutions within this small scope." (raw L2493) The governing economic argument:
"Integration is always expensive, and sometimes the benefit is small." (raw L2493) *(Definition largely
quoted from Evans, raw L2473.)*

## When to use it

Use Separate Ways when two capabilities genuinely have no significant relationship and forcing an
integration would cost more than the value it delivers. It can be applied context-wide for a whole
system, or **case-by-case**: "one team could refuse to use a centralized security system but may still
choose to integrate with some other corporate standard facilities." (raw L2497)

## SaaSOvation's counter-example

Separate Ways is defined partly by what teams choose *not* to do. By integrating with the *Identity and
Access Context*, "both the *Collaboration Context* and the *Agile Project Management Context* avoid going
their Separate Ways with respect to security and permissions." (raw L2497) Security was worth
integrating; had it not been, cutting it loose would have been the ruthless-requirements move.

## Trade-offs

What you gain is simplicity and autonomy: a small, specialized solution free of any integration burden
or [[anticorruption-layer]]. What you give up is any sharing or reuse across the boundary — which is
exactly the point when the shared benefit is small. The risk is applying it too readily and duplicating
capability that would have been cheaper to integrate; the discipline is to weigh integration cost
against real, not imagined, benefit.

## Related

- [[context-map]] — where the (absence of a) relationship is recorded.
- [[anticorruption-layer]] — the alternative when the two contexts *should* integrate.
- [[partnership]], [[customer-supplier-development]] — the cooperative alternatives.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
