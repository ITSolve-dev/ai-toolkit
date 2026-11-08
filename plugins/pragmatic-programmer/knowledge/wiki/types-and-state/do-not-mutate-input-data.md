---
title: Do not mutate data passed into a function
category: types-and-state
summary: "A function whose job is to compute or prepare data writes fields of a plain record or element it received as an argument (perf.amount = ..., item.play = ...), including inside a map or loop over an input collection; build a copy and enrich the copy instead."
tags: [rule, immutability, side-effects, copying]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

When a function needs to return an enriched version of a record it was given, it builds a copy and adds the new fields to the copy, leaving the caller's record unchanged. Fowler does this in the statement example: "I take a copy because I don't want to modify the data passed into the function. I prefer to treat data as immutable as much as I can—mutable state quickly becomes something rotten" (ch. 1, PDF p. 35).

This wiki assigns the neighbouring case as follows. A function that writes fields of a plain record or element it received as an argument is [[do-not-mutate-input-data]]; a method that calls a mutator on an object it received, or a class whose fields are reassigned after construction, is [[immutable-objects]].

## Rule

Do not write to the fields of an argument to produce a function's result. Copy it, then set the derived fields on the copy and return that.

## Sign in code

- An assignment to a field of a parameter (`perf.amount = ...`, `item.total = ...`) inside a function whose job is to compute or prepare data.
- A `map` or loop over an input collection whose callback assigns to the element it was handed rather than returning a new one.

## When not to apply

- The function's stated purpose is to modify its argument, for example an explicit in-place update the caller asked for, named as such. This limit is this wiki's own.
- This wiki's limit: the argument was created by the caller for this call alone and is never read again by it (a builder or accumulator passed in by design); the convention of the project decides there.

## Repair

Replace the in-place writes with: make a (shallow) copy of the argument, assign the derived fields on the copy, return the copy. Fowler would prefer a named function for the copy over a cryptic idiom, unless the idiom is so standard in the language that a wrapper would look out of place (PDF p. 35).

A shallow copy is not enough when the derived fields are written into nested objects shared with the original. Fowler's copy is shallow and he names it so (PDF p. 35); his enrichment only adds top-level fields. Checking that the writes stay at the copied level is this wiki's addition; deeper copies are [[prefer-deep-copy]].

## Before and after

```
function enrich(perf)
    perf.play = plays[perf.playId]
    perf.amount = amountFor(perf)
    return perf
```

```
function enrich(perf)
    copy = shallowCopy(perf)
    copy.play = plays[perf.playId]
    copy.amount = amountFor(copy)
    return copy
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Splitting the Phases of Calculation and Formatting", PDF p. 35. The rule, its reason, the shallow copy and the preference for a named copy function are Fowler's. This wiki's own: the signs, both limits, the check that writes stay at the copied level, the selecting sentence against [[immutable-objects]], and the pseudocode. Related: [[split-phase]].
