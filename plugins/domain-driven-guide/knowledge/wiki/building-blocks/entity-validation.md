---
title: Entity Validation
category: building-blocks
summary: Three levels of validation for entities — attribute guards, whole-object validators, and composition-level deferred validation — kept out of the entity itself.
tags: [technique, tactical-pattern, entity, validation, design-by-contract, self-encapsulation]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Validating an [[entity]] happens at **three levels**, because validity does not compose upward: valid
attributes don't guarantee a valid object, and valid objects don't guarantee a valid composition (raw
L4836).

## Level 1 — Attribute/property validation (guards)

Protect each attribute through **self-encapsulation** — all access, even internal, goes through
accessors [Fowler, Self Encap] (raw L4842) — and apply **design-by-contract** preconditions as
**guards** in the setter (raw L4846). Vernon frames these as *assertions*, not "validation" (a separate
concern): design by contract "enable[s] us to specify the preconditions, postconditions, and invariants
of the components we design" (raw L4846).

The `EmailAddress` [[value-object]] setter shows four escalating preconditions — not null, not empty,
≤100 chars, matches an email regex — each throwing `IllegalArgumentException` (raw L4851). The same
guards apply to simple Entity attribute setters; a Whole Value assigned to an Entity is only as safe as
the guards inside it: "there is no way to guard against setting insane state unless the smaller
attributes within the Value are guarded" (raw L4897). See [[whole-value]].

**Trade-off (the defensive-programming debate):** some developers accept null/empty checks but resist
length/range/format checks, arguing size limits belong to the database (raw L4905). Vernon's counter:
translating `ORA-01401: inserted value too large for column` into a meaningful domain error is
impractical — you can't even tell which column overflowed — so guard text widths in setters; and the
constraint may be a genuine domain rule (e.g. legacy-system integration), not merely a column width
(raw L4933).

## Level 2 — Whole-object validation

Use a **Specification** [Evans & Fowler] or **Strategy** [Gamma et al.], and prefer **Deferred
Validation** — Ward Cunningham's Checks pattern for "a class of checking that should be deferred until
the last possible moment" (raw L4941).

Do **not** embed validation in the Entity:

> "Many times the validation of a domain object changes more often than the domain object itself.
> Embedding validation inside an Entity also gives it too many responsibilities." (raw L4943)

Put a separate `Validator` class in the same **Module**/package (so it can read protected accessors),
and have it **collect a full set of results rather than throw on the first error**, via a
`ValidationNotificationHandler` (raw L4947). The Entity may expose `validate(handler)` that instantiates
its `Validator` — the Entity decides *what* validates it without performing validation itself, so
validation can evolve at its own pace and be tested independently (raw L5083).

## Level 3 — Object-composition validation

When a *cluster* of Entities / [[aggregate]] instances must be valid **together**, Deferred Validation
is best coordinated by a **Domain Service** that uses **Repositories** to read the instances it needs
(raw L5104). Validate only when appropriate: an Aggregate may sit in a temporary intermediate state, so
model a status and publish a [[domain-event]] (e.g. `WarbleTransitioned`) to signal that validation is
now due (raw L5106).

## Related

- [[entity]] — the object being validated; it decides *what* validates it, not *how*.
- [[value-object]], [[whole-value]] — attribute guards live inside the Values an Entity holds.
- [[aggregate]] — level-3 composition validation spans an Aggregate cluster.
- [[domain-event]] — signals when a deferred validation becomes due.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
