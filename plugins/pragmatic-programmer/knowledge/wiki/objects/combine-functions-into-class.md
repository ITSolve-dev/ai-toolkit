---
title: Combine Functions into Class
category: objects
summary: "Several free functions or client fragments take the same bare record as their main input and compute derived values from it (base charge, taxable charge), the same formula is repeated or extracted far from the data, and the record is updated somewhere after the values are derived: make the record a class whose methods compute the values on demand."
tags: [rule, cohesion, derived-data, duplication, refactoring]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Combine Functions into Class** turns a record that several functions work on into a class and moves those functions in as methods, so the shared environment becomes explicit (*Refactoring*, 2nd ed., ch. 6, PDF pp. 164-169). Fowler pairs it with [[combine-functions-into-transform]]: both repair the same shape, and the choice depends on whether the source data changes.

## Rule

"When I see a group of functions that operate closely together on a common body of data (usually passed as arguments to the function call), I see an opportunity to form a class" (PDF p. 164). The class makes the shared environment explicit, removes the common data from each call's arguments, and gives one object to pass to the rest of the system. Fowler's reason for not stopping at Extract Function is discoverability: free top-level functions computing from a record "are often easy to miss", so he prefers to "give the function a closer connection to the data it processes" (PDF p. 166).

Derived values become accessors computed on demand. Clients cannot tell a stored field from a derived value, which Fowler calls the Uniform Access Principle (PDF p. 168; see [[uniform-access]]).

**Selecting between class and transform.** This wiki reads PDF p. 170 as follows. If the source record is updated anywhere after the derived values are computed, use a class, because its derivations are computed on demand and stay consistent; if the data is immutable or used only in a read-only context, a transform is equally good and the choice follows the style already in the code. Fowler: "Using a class is much better if the source data gets updated within the code" (PDF p. 170).

He prefers a class to a nested function, because nested functions are hard to test and because a class is needed when more than one function of the group must be exposed (PDF p. 165).

## Sign in code

- Three or more free functions or client fragments that take the same bare record as their main input and compute values from its fields.
- The same derivation written out in more than one client (`baseRate(r.month, r.year) * r.quantity` twice), or one copy extracted as a free function far from the record while other clients do not use it.
- That record is changed somewhere after values are derived from it. Whether the source record is changed anywhere after values are derived from it selects the page: if it is, [[combine-functions-into-class]]; if not, [[combine-functions-into-transform]].

This wiki assigns the neighbouring cases as follows. A method in class X that computes from data class Y already holds is [[information-expert]]. Free functions or client code deriving values from a record that is not yet a class are [[combine-functions-into-class]]; fields of a structure with no routines of its own written from several call sites are [[replace-direct-data-manipulation-with-adt]]. For the split pair: a field-less class whose methods all take the same one record and read or write only its fields, while the record has only fields or accessors, is [[class-with-only-data-or-only-behaviour]]. A class that already exists with getters and setters and no behaviour is [[no-getters-and-setters]], whose repair moves this behaviour in the same way. A repeated block that is not a derivation from one record is [[dry]].

## When not to apply

- **Immutable or read-only data.** If the record is never changed after derivation, a transform serves equally well, and in code written in a functional style it is the better fit (PDF pp. 170, 176). Fowler's choice "will often depend on the style of programming already in the software" (PDF p. 170).
- **A language without first-class classes.** Fowler notes that such languages use a function-as-object closure for the same purpose (PDF p. 165); the project's idiom decides the form.
- **One derivation, one caller.** This limit is this wiki's own: a single derivation used by one caller does not form a group yet, and extracting the function is enough ([[extract-routine-to-name-a-step]]).

## Repair

Fowler's mechanics (PDF p. 165):

1. Encapsulate the common record ([[replace-direct-data-manipulation-with-adt]]). If the data is not grouped yet, group it first ([[group-related-data-into-a-structure]]).
2. Wrap the raw data in the new class as soon as it is acquired.
3. Move each function that uses the record into the class ([[move-function]]); arguments that are now members drop out of its parameter list.
4. Extract each further piece of logic over the data and move it in too, renaming for the reader (Fowler turns `calculateBaseCharge` into `baseCharge`).
5. Point every client at the method instead of its own copy of the formula.

## Before and after

```
// before: the same derivation from a reading, in two clients; the reading is later updated
reading = acquireReading()
base = baseRate(reading.month, reading.year) * reading.quantity

reading = acquireReading()
base = baseRate(reading.month, reading.year) * reading.quantity
taxable = max(0, base - taxThreshold(reading.year))

reading.quantity = corrected(reading.quantity)
```

```
// after: one class owns the data and derives values on demand
class Reading
    constructor(raw)
    quantity(), month(), year()
    correctQuantity(): quantity = corrected(quantity)
    baseCharge():    return baseRate(month(), year()) * quantity()
    taxableCharge(): return max(0, baseCharge() - taxThreshold(year()))

reading = Reading(acquireReading())
base    = reading.baseCharge()
taxable = reading.taxableCharge()
reading.correctQuantity()
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Combine Functions into Class", PDF pp. 164-169, and the comparison in "Combine Functions into Transform", PDF p. 170: the rule, the discoverability reason, uniform access, the class-versus-transform criterion, the preference over nested functions, closures in languages without classes and the mechanics. This wiki's own: the count in the first sign, the one-derivation limit, the assignments against neighbouring pages, and the pseudocode.
