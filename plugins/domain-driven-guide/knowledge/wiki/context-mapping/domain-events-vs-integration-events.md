---
title: Domain Events vs. Integration Events
category: context-mapping
summary: Domain events belong inside a single bounded context; integrating contexts by sharing them turns them into a coupling contract — use explicit integration events or an API instead.
tags: [comparison, domain-events, integration-events, bounded-context, coupling]
sources: [web-page-event-sourcing-guide]
created: 2026-07-25
updated: 2026-07-25
---

A recurring temptation is to integrate services by having one service consume another's
[[domain-event]]s directly. [[web-page-event-sourcing-guide]] argues this is a mistake, and the
distinction is a strategic-design boundary worth stating precisely.

| | **Domain event** | **Integration event** |
|---|---|---|
| Where it lives | Inside one bounded context | Crosses bounded-context boundaries |
| Purpose | Reconstitute aggregate state; drive internal projections/background work | Notify *other* contexts that something happened |
| Contract | Free to change with the service's internals | A published contract other teams depend on |
| Effect of sharing widely | — | Couples consumers to your internal model |

## The argument

If a service's domain events are consumed by other services, they *become* integration events:
they now imply a contract that must be maintained, which constrains how the owning service may
change its own code. The result is excessive coupling and fragility. (raw L222–L230)

The recommended discipline: **apply event sourcing (and keep domain events) within a limited
scope — e.g. a single [[bounded-context]].** A payments service and an orders service may each be
event-sourced internally, but they remain separate services and integrate the standard way —
through explicit integration events or an API — not by leaking each other's domain events.
(raw L226)

## Recorded counterpoint

Reader **powerman** challenged the sharpness of the distinction in the discussion: in his view
domain and integration events share the same hard problems — *both* need versioning, *both*
need long-lived format support, and *both* face incomplete-data issues — so the line between
them is less principled than the author implies.
— discussion on [[web-page-event-sourcing-guide]]

This is a fair caution: the categories differ by *contract scope and coupling*, not by any
technical property of the message itself. The practical guidance (keep the coupling boundary at
the bounded context) still holds even if the two event kinds look identical on the wire.
