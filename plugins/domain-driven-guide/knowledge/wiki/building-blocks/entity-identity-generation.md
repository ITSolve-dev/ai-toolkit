---
title: Entity Identity Generation
category: building-blocks
summary: Four strategies for creating an entity's unique identity, plus the timing (early vs late) and stability concerns that surround it.
tags: [technique, tactical-pattern, entity, identity, uuid, decision-rule]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Every [[entity]] needs a stable unique identity. Vernon catalogs **four strategies** for creating it
— ordered from simplest to most complex (raw L3873) — plus two orthogonal concerns: *when* identity is
generated (timing) and *how* it stays stable.

## 1. User provides identity

The user types or selects the identifying value; the application must enforce uniqueness (raw L3875).
Simple but risky: users produce identities that are "unique but incorrect," and identity usually must
be immutable so users cannot fix typos (raw L3891). Example failure: using `Forum`/`Discussion`
**titles** as identity breaks when a title is misspelled or later regretted. Mitigation is
**workflow-based identity approval** — worth the extra cycles when a human-readable identity will be
used "pervasively throughout the business for years," but not conducive to high-throughput domains (raw
L3897). Safer alternative: keep user-entered values as matchable *properties*, and obtain identity
another way (raw L3899).

## 2. Application generates identity

The application manufactures identity with no external round-trip, most commonly a **UUID/GUID** (raw
L3903). In Java, `java.util.UUID.randomUUID()` gives a type-4 (SecureRandom) value;
`nameUUIDFromBytes()` gives a type-3 name-based value (raw L3915). Properties: fast, no persistence
interaction, and **cacheable** — refill a cache in the background; lost cached UUIDs on restart leave
no gaps because values are random (raw L3960).

Cost: a 32/36-char UUID is large and not human-readable, so keep it off the UI (raw L3964). Two
refinements:

- **Local vs global identity.** UUID segments may serve as *local identity* for Entities inside an
  [[aggregate]] boundary (unique only among siblings); the Aggregate Root still needs *global*
  uniqueness. "Local identity means that Entities held inside an Aggregate need only have uniqueness
  among other Entities held inside the same Aggregate." (raw L3972)
- **Custom human-readable identity Value Object.** e.g. `APM-P-08-14-2012-F36AB21C` encodes context
  (`APM`), type (`P`=Product), creation date, and a UUID segment — human-readable, globally unique, and
  self-describing across [[bounded-context]]s (raw L3974). Wrap it in a `ProductId` [[value-object]],
  not a `String`, so clients can call `productId.creationDate()` without knowing the format (raw L3976).

The natural home for application identity generation is the Aggregate's **Repository**, via
`nextIdentity()` (raw L4016):

```java
public ProductId nextIdentity() {
    return new ProductId(java.util.UUID.randomUUID().toString().toUpperCase());
}
```

## 3. Persistence mechanism generates identity

Delegate to a database sequence or auto-increment; it is always unique and compact (2/4/8-byte, giving
up to ~9.2 quintillion values for an 8-byte long) (raw L4036). Downsides: **performance** (a round-trip
per value) and **gaps** when cached preallocated values are lost on restart (raw L4040). Preallocation
caching is impractical for small ranges or when gaps are unacceptable.

## 4. Another Bounded Context assigns identity

The identity already exists in an external system; you integrate to find, match, and assign it (see
[[context-map]], [[anticorruption-layer]]). Matching is an exact lookup, or a fuzzy search returning
multiple candidates for the user to select; the chosen identity becomes the local identity, sometimes
copying additional foreign state (raw L4188). This introduces **synchronization** — external changes
must propagate, ideally via [[domain-event]]s the local context subscribes to (raw L4196). It is "the
most complex of identity creation strategies… Use this approach as conservatively as possible." (raw
L4200)

## Timing: early vs late generation

> "Early identity generation and assignment happen before the Entity is persisted." (raw L4072)
> "Late identity generation and assignment happen when the Entity is persisted." (raw L4074)

Late is simplest — the store assigns identity on insert (raw L4206). But timing matters when identity
is needed *before* persistence. If a [[domain-event]] is published on construction, late generation
means the event carries no valid identity — so identity "must be completed early," queried from the
**Repository** and passed to the constructor (raw L4212).

### Failure mode: the add-to-Set equality bug

A concrete hazard of late generation: adding two not-yet-persisted Entities to a `java.util.Set` while
their identity is still `null`/`0`/`-1`. If `equals()` compares identity, the new instances look equal,
so only the first is retained and the rest silently vanish — "a dubious bug whose root cause is at first
difficult to understand and fix" (raw L4218). Two fixes: (a) allocate identity **early**, or (b)
implement `equals()`/`hashCode()` on other attributes as if the Entity were a Value (in multitenancy,
include `TenantId` — no two `User`s under different tenants are equal) (raw L4222). Vernon prefers early
allocation: "It is more desirable for Entities to have equals() and hashCode() methods that are based on
the object's unique identity rather than other attributes." (raw L4255)

## Identity stability

Identity "must be protected from modification, remaining stable throughout the lifetime of the Entity"
(raw L4338). Enforce with **modify-once guards** in a self-encapsulated setter: throw
`IllegalStateException` if the value is already set, `IllegalArgumentException` if null (raw L4340). The
guard does not obstruct ORM rehydration, because the object is first built with a zero-arg constructor
(attribute null), permitting the one-time assignment.

## Related

- [[entity]] — the building block being identified.
- [[surrogate-identity]] — the second, ORM-only identity carried alongside domain identity.
- [[value-object]] — the wrapper type (`ProductId`) that gives identity domain meaning.
- [[aggregate]] — local-vs-global identity is scoped by the Aggregate boundary.
- [[domain-event]] — why identity often must be generated early.
- [[bounded-context]], [[anticorruption-layer]] — strategy 4, identity assigned by another context.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
