---
title: Combine Functions into Transform
category: functions
summary: "The same derived values are computed from a source record in several clients, and the record is not changed afterwards: one enrich/transform function deep-copies the record and adds every derived field, without altering its input; a client that later assigns to a source field of the enriched record leaves its derived fields stale."
tags: [rule, derived-data, duplication, immutability, refactoring]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Combine Functions into Transform** gathers all the derivations from a source record into one function that takes the record and returns a copy enriched with every derived value as a field (*Refactoring*, 2nd ed., ch. 6, PDF pp. 170-176). Fowler presents it as the alternative to [[combine-functions-into-class]] for the same shape: derived values repeated wherever they are used.

## Rule

Derivations repeated in several places are a change hazard: duplication "is asking for trouble when they need to change" (PDF p. 172). Extracting each into a function helps, but such functions "often end up scattered around the program making it hard for future developers to realize they are there" (PDF p. 172). A transform gives one place to look: "to examine the derivations, all I need do is look at the transform function" (PDF p. 170).

**Selecting between class and transform.** This wiki reads PDF p. 170 as follows. If the source record is updated anywhere after the derived values are computed, use a class, because its derivations are computed on demand and stay consistent; if the data is immutable or used only in a read-only context, a transform is equally good and the choice follows the style already in the code. Fowler: "Using a transform stores derived data in the new record, so if the source data changes, I will run into inconsistencies" (PDF p. 170).

The transform must not alter its input. Returning an enriched record implies the original is unchanged, so Fowler adds a test that deep-copies the input, runs the transform and asserts the input still equals the copy (PDF p. 174). Inside the transform he is content to mutate the result: he supports immutability "at boundaries, but will mutate within smaller scopes" (PDF p. 173).

Naming: `enrich…` when the output is the input plus extra information, `transform…` when it is something different (PDF p. 173).

## Sign in code

- The same derivation over a record's fields written out in two or more clients, or extracted into a free function that some clients use and others re-implement.
- The record is not changed after it is produced (it comes from input, a query or a read-only view). Whether the source record is changed anywhere after values are derived from it selects the page: if it is, [[combine-functions-into-class]]; if not, [[combine-functions-into-transform]].
- After the repair, the risk to look for: a client that assigns to a source field of the enriched record (`enriched.quantity = …`), which leaves its derived fields stale. That client is the sign that the class was the right choice.

This wiki assigns the neighbouring cases as follows. A field computable from other fields of a mutable structure is [[stored-derived-data]]; an enriched copy of data nobody changes afterwards falls under that page's own limit for fields derived from immutable data. A repeated derivation is this page's or [[combine-functions-into-class]]'s, not [[dry]]'s, when its input is one record.

## When not to apply

- **Source data updated after derivation.** Changing, say, the quantity on an enriched record "would result in data that’s inconsistent"; in a language without immutable structures Fowler uses a class instead (PDF p. 176).
- Without language-level immutability transforms still work "if the data appears in a read only context, such as deriving data to display on a web page" (PDF p. 176).
- **A transform that mutates its input** is not this refactoring. This wiki reads it as a hidden side effect ([[do-not-mutate-input-data]]): without a deep copy, callers holding the original see it change. Fowler's input-unchanged test is the guard.

## Repair

Fowler's mechanics (PDF p. 171):

1. Create a transform that takes the record and returns a deep copy with the same values; add a test that the original is not altered.
2. Pick one derivation, move its body into the transform as a new field of the result (extract it first if it is complex), and change the client to read the field.
3. Test; repeat for the other derivations.
4. Once all callers read the field, nest or hide the original helper inside the transform, so clients that need the value are steered to the enriched record (PDF p. 174).

## Before and after

```
// before: each client re-derives charges from the raw reading
// client 1
reading = acquireReading()
charge = baseRate(reading.month, reading.year) * reading.quantity

// client 2
reading = acquireReading()
base = baseRate(reading.month, reading.year) * reading.quantity
taxable = max(0, base - taxThreshold(reading.year))
```

```
// after: one transform derives everything once; its input is left untouched
function enrichReading(original)
    result = deepCopy(original)
    result.baseCharge    = baseRate(result.month, result.year) * result.quantity
    result.taxableCharge = max(0, result.baseCharge - taxThreshold(result.year))
    return result

reading = enrichReading(acquireReading())
charge = reading.baseCharge       // client 1
taxable = reading.taxableCharge   // client 2

test "enrichReading leaves its input unchanged"
    raw = {customer: "ivan", quantity: 15, month: 5, year: 2017}
    oracle = deepCopy(raw)
    enrichReading(raw)
    assertDeepEqual(raw, oracle)
```

A first phase of [[split-phase]] may itself be such a transform.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Combine Functions into Transform", PDF pp. 170-176: the rule, the scattering and single-place reasons, the class-versus-transform criterion, the read-only-context limit, the input-unchanged test, mutation in small scopes, the enrich/transform naming and the mechanics. This wiki's own: the third sign, the reading of a mutating transform as a hidden side effect, the assignments against [[stored-derived-data]] and [[dry]], and the pseudocode.
