---
title: Standard Type
category: building-blocks
summary: A descriptive Value Object (a.k.a. type code, lookup, or power type) that indicates the type of a thing; best modeled as an immutable Value, often as an enum-as-State.
tags: [pattern, tactical-pattern, standard-type, enum, state-pattern, integration]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Standard Type** is a descriptive object that indicates the *type* of a thing — what the industry
variously calls a *type code* or *lookup*, and sometimes a **Power Type**. "There is the thing (Entity)
or description (Value) itself, and there are also the Standard Types to distinguish them from other
types of the same thing" (raw L5529). Vernon prefers "Standard Type" because "type code doesn't say
much" and "a lookup is a lookup of what?" (raw L5529).

Examples: the type of a `PhoneNumber` (`Home`, `Mobile`, `Work`, `Other`); a `Currency` constraining a
`MonetaryValue` (AUD, CAD, EUR, GBP, JPY, USD…); a medication's administration route (IV, Oral,
Topical) (raw L5531, L5535).

## Why model them as Values

Standard Types "measure and describe the types of things, and measures and descriptions are best modeled
as Values" (raw L5541). They also satisfy every Value characteristic (see [[value-object]]): "one
instance of {IV}… is just the same as any other instance of {IV}. They are clearly interchangeable,
which also means that they are replaceable and can employ Value equality" (raw L5541). The rule: "if
there is no need to maintain a continuity of change over the life cycle of descriptive types in *your*
Bounded Context, model them as Values" (raw L5541).

## Failure mode they prevent: invalid states

A Standard Type constrains a Value to a valid finite set. Modeling `currency` as a raw `String` lets you
"place the model into an invalid state. Consider the misspelled *doolars* and the problems it would
cause" (raw L5533). A `Currency` Standard Type cannot be a nonexistent currency.

## The enum-as-State implementation

Vernon's preferred implementation is a **Java enum**, which he shows doubling as an elegant,
clutter-free **State** object. His `GroupMemberType` enum declares default behaviors (`isGroup()`,
`isUser()` returning `false`) at the bottom, overridden per constant (raw L5592). "The state changes by
replacing the current enum value with a different one" (raw L5594). Advantages: a well-defined finite set
of values, very lightweight, and side-effect-free by convention (raw L5592). Textual descriptions are
often unnecessary in the model — they "are generally valid only in the User Interface Layer" and are
frequently localized, so "often the name of the Standard Type alone is the best attribute to use in the
model" (raw L5592). A widely used example is `BacklogItemStatusType` with `PLANNED`, `SCHEDULED`,
`COMMITTED`, `DONE`, `REMOVED` (raw L5596).

## Alternatives and their trade-offs

- **Classical Value instances** — one immutable Value per type; use a **Domain Service** or **Factory**
  to statically create them. Downside: statically created instances are not auto-synced with the system
  of record (raw L5620).
- **Shared immutable Value from a hidden persistence store** — served by a Standard Type
  Service/Factory (one provider per set: phone types, currency types…), enabling safe caching because
  the values are read-only and immutable (raw L5612).
- **An [[aggregate]] per type** — Vernon says "think twice." "Standard types should generally not be
  maintained inside the [[bounded-context]] that consumes them," and an *immutable Entity* is a
  contradiction: "ask yourself if an immutable Entity is by definition really an Entity. If you think
  not, you should consider modeling it as a shared immutable Value Object instead" (raw L5610).

## Integration and maintenance

Standard Types commonly live natively in a **separate [[bounded-context]]**, where they are Entities
with `identity`, `name`, `description`. A consuming context should "strive to treat them as Values,"
pulling in as few attributes as possible "in adherence to the goal to integrate with minimalism" (raw
L5543) — see [[value-objects-for-integration]]. Vernon's net advice: "be biased toward enum for Standard
Types whether or not you actually think of it as a State," and for large sets consider code-generating
the enum from the system of record (raw L5618).

## Related

- [[value-object]] — the parent characteristic set a Standard Type satisfies.
- [[value-objects-for-integration]] — minimalism when consuming remote types.
- [[bounded-context]] — where Standard Types are natively maintained.
- [[value-object-persistence]] — persisting enum Standard Types with a custom user type.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
