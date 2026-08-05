---
title: Duplicating Information Across Bounded Contexts
category: context-mapping
summary: When and how to copy data owned by another Bounded Context — the immutable-snapshot vs. kept-in-sync trade-off, the minimalist rule, and why identity duplication is safe.
tags: [heuristic, integration, data-duplication, value-object, aggregate, eventual-consistency, trade-offs, anti-patterns]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

When one [[bounded-context]] integrates with another, it frequently needs some of the other's data locally (an SLA may make fetching it on every use impractical). Copying that foreign data into your own model is legitimate, but it hands you a synchronization responsibility, and *how much* you take on is a design decision with sharp trade-offs. This page captures Vernon's guidance from the SaaSOvation messaging-integration example.

## Two strategies, opposite trade-offs

**Immutable snapshot (Value Object copy).** The *Collaboration Context* chose to "create immutable [[value-object]]s that hold similar information." Upside: "Because the Values are immutable, the team will never have to worry about keeping the shared information up-to-date." Downside: staleness — "if some of the shared information is updated, the *Collaboration Context* will never update the related objects that it created in the past" (raw L12451). Good when a point-in-time fact is what you actually need (who authored this post, as of then).

**Kept-in-sync copy (mutable Aggregate).** The *Agile Project Management Context* took "the opposite trade-off": `ProductOwner`/`TeamMember` [[aggregate]]s hold live copies of `User` name and email, updated by listening for change events. Upside: the local copy stays current. Downside: you must now consume and correctly apply a stream of change events, tolerating [[idempotency|duplicate and out-of-order delivery]].

## The hidden responsibility

The cost of the synced-copy choice is easy to underestimate. Keeping just a name and email correct means reacting to *every* foreign event that could touch them (raw L12570-L12584):

- `PersonContactInformationChanged`, `PersonNameChanged`
- `UserAssignedToRole`, `UserUnassignedFromRole`
- `UserEnablementChanged`, `TenantActivated`, `TenantDeactivated`

Each must be applied in a time-aware, idempotent way (SaaSOvation's `MemberChangeTracker`, covered in [[idempotency]]). Taking on more foreign fields multiplies this surface — the failure mode is a local model that silently drifts out of sync, or gets stuck (e.g. a member left disabled because two events arrived reversed).

## Rule of thumb: be a minimalist

Vernon's summarizing heuristic: "if at all possible, it is best to minimize or even completely eliminate information duplication across Bounded Contexts" (raw L12586). It may be unavoidable, but "having the goal to reduce the amount of foreign information we take responsibility for will make our jobs much easier. It's integrating with a minimalist's mindset." A related move is to **derive** state from event data transiently rather than storing it: use event payloads "to perform calculations and derive state... while not actually holding on to and assuming the responsibility for keeping it synchronized with its official state located in the system of record" (raw L12590). See [[value-objects-for-integration]].

## Identity is the exception — and it is safe

One kind of duplication is always necessary and always fine: identity. "there is no way to avoid duplication of tenant and user identity, and identity duplication across Bounded Contexts is necessary in general. That is one of the primary ways that Bounded Contexts can integrate at all. Besides, identity is safe to share because it is immutable" (raw L12588). Combine it with soft-deletes/disabling so that referenced objects (`Tenant`, `User`, `ProductOwner`, `TeamMember`) never vanish out from under a foreign reference.

## Related

[[event-driven-integration]] · [[value-object]] · [[value-objects-for-integration]] · [[aggregate]] · [[idempotency]] · [[eventual-consistency]] · [[bounded-context]] · [[anticorruption-layer]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
