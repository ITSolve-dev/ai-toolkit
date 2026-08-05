---
title: Whole Value (Conceptual Whole)
category: building-blocks
summary: The characteristic that a Value Object's related attributes form one indivisible measure or description, constructed atomically — the antidote to primitive obsession and leaked domain logic.
tags: [pattern, tactical-pattern, whole-value, conceptual-whole, primitive-obsession, ubiquitous-language]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Whole Value** — Ward Cunningham's pattern, and the "conceptual whole" characteristic of a
[[value-object]] — is the principle that a Value's attributes are meaningful only *together*, as a
single integral measure or description, and must be created in one atomic operation. "Each attribute
contributes an important part to a whole that collectively the attributes describe. Taken apart from the
others, each of the attributes fails to provide a cohesive meaning" (raw L5278). Merely grouping
attributes into an object is not enough — the grouping earns its keep only when the whole describes
another thing in the model.

## The canonical example: {50,000,000 dollars}

Cunningham's illustration: the Value `{50,000,000 dollars}` has two attributes, `50,000,000` and
`dollars`, and "separately these attributes describe something else or nothing special… Together these
attributes are a conceptual whole that describes a monetary measure" (raw L5280). So a thing worth that
amount should not carry two loose attributes `amount` and `currency`; it should carry one
`MonetaryValue` property, because "the thing's worth is not just 50,000,000, and not just dollars" (raw
L5280).

## Attribute vs property

Vernon draws a precise vocabulary distinction. The `MonetaryValue` type *has* attributes (`amount`,
`currency`). But the parent thing that holds a reference to a `MonetaryValue` instance has a
**property** — e.g. `ThingOfWorth.worth` — not an attribute. "To the thing that holds the reference to
the Value Object instance, it is a property" (raw L5317). The property name (`worth`) and the Value type
name (`MonetaryValue`) can be settled only after establishing the [[bounded-context]] and its
[[ubiquitous-language]].

## Atomic construction

Wholeness constrains construction: "You must not allow the attributes of a Value instance to be
populated after construction, as if to build up the Whole Value piece by piece. Instead, the final state
must be guaranteed to initialize all at once, atomically" (raw L5346). This is why every [[value-object]]
initializes its full state in its constructor.

## Failure mode: primitive obsession and leaked logic

The symptom that a Whole Value is missing is domain logic *leaking* out of the model into clients.
Vernon's example: typing a name as a plain `String` allows capitalization logic to escape into client
code — `name.substring(0,1).toUpperCase() + name.substring(1).toLowerCase()` scattered wherever the name
is used (raw L5332). Introducing a `ThingName` type centralizes all naming concerns (formatting on
construction) so clients are relieved of the burden. "This emphasizes the need to proliferate Values
throughout the model as opposed to minimizing their significance and use" (raw L5344).

A related smell is **basic-type overuse** — reaching for `String`, `Integer`, or `Double` where a
domain Value belongs. Vernon's three-strikes case against patching `Double` with `convertToCurrency()`:
the currency behavior is "lost in a sea of general-purpose floating-point responsibilities" (strike
one), `Double` has no built-in understanding of currencies (strike two), and "class `Double` says
nothing explicit about your domain. You lose track of your domain concerns by not applying the
Ubiquitous Language" (strike three) (raw L5348).

## Decision heuristic

"If you are tempted to place multiple attributes on an Entity that as a result manifests a weakened
relationship to all other attributes, the attributes should very likely be gathered into a single Value
type, or multiple Value types" — each forming a cohesive whole named from the Ubiquitous Language. And
"if one or more of the attributes must change over time, consider Whole Value replacement over
maintaining an Entity through a long life cycle" (raw L5352).

## Related

- [[value-object]] — the building block this characteristic defines.
- [[side-effect-free-function]] — the behavioral counterpart characteristic.
- [[entity]] — what a weakened attribute cluster is often mistakenly modeled as.
- [[ubiquitous-language]] — the source of the Whole Value's name.
- [[data-model-leakage]] — the anti-pattern that pushes designers away from Whole Values.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
