---
title: Stored derived data
category: types-and-state
summary: "A field whose value is computable from other fields of the same structure, a setter that must recompute a second field to keep the two in step, or one method that both records a fact and adjusts a stored summary of the facts (adjustments.add(a); production += a.amount)."
tags: [rule, state, duplication, caching, derived-data]
paradigm: any
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Data structures represent knowledge, so they can violate [[dry]] too. A field that can be computed from its neighbours states one fact twice, and the structure can then hold a contradiction.

## Rule

Make a value computed when it is determined by other data in the same structure. The book's example is a line with a start point, an end point and a stored length. The class looks reasonable, but the length is defined by the two points, so changing either one changes it (pp. 65-66).

Fowler's *Refactoring* reaches the same rule from the **Mutable Data** smell: "Mutable data that can be calculated elsewhere is particularly pungent" (2nd ed., ch. 3, Mutable Data, PDF p. 90). He calls it not only a rich source of confusion and bugs but also unnecessary (PDF p. 90). The wider smell, and the other shapes of mutation it covers, are on [[mutable-data]].

The catalogue entry, **Replace Derived Variable with Query** (ch. 9, PDF pp. 277-281), gives the reasons. Fowler names mutable data "One of the biggest sources of problems in software" (PDF p. 277). A calculation "often makes it clearer what the meaning of the data is, and it is protected from being corrupted when you fail to update the variable as the source data changes" (p. 277). He calls the shape duplication, "not the common duplication of code but duplication of data" (p. 278).

## Sign in code

- A field computable from other fields of the same type.
- A constructor or setter that writes a second field in order to keep it consistent with the first.
- A constructor accepting both the inputs and the value derived from them.
- One method that both records a fact and adjusts a stored summary of the facts: `adjustments.add(a); production = production + a.amount`, where the summary equals a fold, count, sum or lookup over the collection. This wording is this wiki's, after Fowler's `ProductionPlan` (p. 278).

This wiki assigns the neighbouring case as follows. This page owns a field that can be computed from its neighbours, because removing the field removes the need to keep it in step. A rule between fields that cannot be computed from each other, such as `min <= max`, is [[class-invariant]], and so is the agreement between a cache that survives here and its sources.

## When not to apply

The book allows a violation later in development for performance, usually to cache a costly result (p. 66). The condition is that the damage stays local, in its words: «локализовать отрицательное влияние, чтобы оно не распространялось наружу» (p. 66). The difference must be visible only inside the class's methods.

Fowler allows a field derived from immutable data: information derived from an immutable record can be represented as fields rather than getters (*Refactoring*, Data Class, PDF p. 98); this wiki's reason is that such a field cannot drift. Chapter 9 repeats the exception: where the source data is immutable and the result can be forced immutable too, transformations that build a new data structure are "reasonable to keep even if they could be replaced with calculations" (PDF p. 277); where the source changes and the lifetime of derived structures would have to be managed, the object with calculated properties wins (p. 277). This wiki reads that as a limit: the sign needs a mutable source field, or a setter on one. A constructor that accepts the derived value from its caller is still reported: immutability does not stop the two disagreeing. An enriched copy produced by a transform over data that nothing changes afterwards is this limit's case ([[combine-functions-into-transform]]); where the source is updated after derivation, [[combine-functions-into-class]] owns the repair.

This wiki adds a frozen value. A total or a price recorded at the moment of a transaction is a fact about that moment, and later changes to its inputs must not alter it, so it is not derived from them.

## Repair

- Default: remove the field and expose a computed function. Fowler's name for this is Replace Derived Variable with Query (PDF p. 90). His mechanics (PDF p. 278):
  1. Identify every point of update. If the variable mixes sources, split it first ([[one-variable-one-purpose]]).
  2. Write a function that calculates the value.
  3. Assert that the stored variable and the calculation agree wherever the variable is read ([[assert-the-impossible]]); encapsulate the variable if the assertion needs a home. Test. Fowler treats the replacement as a hypothesis the assertion tests (p. 278).
  4. Replace readers with the calculation. Test.
  5. Remove the declaration and the updates as dead code ([[remove-dead-code]]).
- More than one source: when the accumulator starts from a constructor argument, the assertion fails for any non-zero start. Split the field into the initial value and the accumulated part, then replace only the accumulated part; the result is the sum of the two (PDF pp. 280-281).
- If a measured cost justifies a cache: make the field private, recompute it in every mutator through one private function, and keep the public read identical to the computed form.

The word measured is this wiki's: the source says only that performance may require it. Keeping one public read for both forms is what [[uniform-access]] asks for.

## Before and after

Before:

```
record Interval          // fields writable after construction
    start: Time
    end: Time
    duration: Span

interval.end = interval.end + extension   // duration now wrong
```

After:

```
record Interval
    start: Time
    end: Time
    function duration()
        return end - start
```

A summary kept in step with a collection, after Fowler's example:

```
class ProductionPlan
  production()  -> return this.production
  applyAdjustment(a)
    this.adjustments.add(a)
    this.production = this.production + a.amount
```

```
class ProductionPlan
  constructor(initial)
    this.initialProduction = initial
    this.adjustments = []
  production() -> return this.initialProduction + sum of a.amount over this.adjustments
  applyAdjustment(a)
    this.adjustments.add(a)
```

After, where a cache is justified:

```
class Interval
    private start, end, duration

    constructor(start, end)
        this.start = start
        this.end = end
        recompute()

    function set_start(time)
        this.start = time
        recompute()

    function set_end(time)
        this.end = time
        recompute()

    function duration()
        return this.duration

    private function recompute()
        this.duration = this.end - this.start
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 9, pp. 65-66, via [[pragmatic-programmer]]. This wiki's own: the wording of the signs, the assignment of the neighbouring case, the frozen-value limit, the requirement that the cost be measured, and the pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Mutable Data", PDF p. 90, and "Data Class", PDF p. 98: the rule as a smell, its repair, and derived fields on immutable data. This wiki's own for that part: the reading of p. 98 as a limit on the sign, the reason that such a field cannot drift, and keeping the constructor that accepts a derived value as a sign.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 9, "Replace Derived Variable with Query", PDF pp. 277-281: the reasons, duplication of data, the immutable-source exception, the mechanics with the assertion, the split for an initial value and the `ProductionPlan` example. This wiki's own for that part: the paired-writes sign as worded and the pseudocode.
