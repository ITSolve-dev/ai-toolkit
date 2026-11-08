---
title: Lazy element
category: complexity
summary: "A function whose name says no more than its body reads (lateCount(d) returning d.lateDeliveries), or a class with state whose only behaviour is one simple function used from one place: structure that adds no explanation, variation or reuse."
tags: [rule, lazy-element, inline, needless-indirection]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's **Lazy Element**: program elements are welcome when they add structure, "providing opportunities for variation, reuse, or just having more helpful names" (ch. 3, Lazy Element, PDF p. 94). Sometimes the structure is not needed: "a function that’s named the same as its body code reads, or a class that is essentially one simple function" (PDF p. 94). Fowler says it may be a function that was expected to grow and never did, or a class that refactoring has shrunk.

## Rule

Remove a program element that adds no explanation, no variation and no reuse.

The catalogue entries give the two sides. Inline Function's first occasion is a body "as clear as the name" (ch. 6, PDF p. 132), and its third is a chain in which every function only delegates to the next (PDF p. 132); the procedure is [[inline-function]]. Inline Class applies to a class that "is no longer pulling its weight", typically after refactoring has moved its responsibilities out, and folds it into the class that uses it most (ch. 7, "Inline Class", PDF p. 213).

## Sign in code

- A function whose name restates its body. `lateCount(d)` returning `d.lateDeliveries` qualifies. `isAdult(p)` returning `p.age >= adultAge` does not, because it names a rule.
- A class with fields whose only behaviour is one method of a few lines, called from one place, where the caller could hold the fields and the lines.
- A call chain in which each function's whole body is a call to the next, with the arguments unchanged or only renamed (Fowler's third occasion, PDF p. 132).

This wiki assigns the neighbouring cases as follows. A function whose name says *what* where its body says *how* is an explanation and stays, however short; a function whose name only restates its body is [[lazy-element]]. A missing extraction of the first kind is [[extract-routine-to-name-a-step]]. A class with no fields, created only to call one method on another object's data, is [[class-with-only-data-or-only-behaviour]]. A class whose methods mostly forward to one field is [[hide-delegate-or-remove-middle-man]]. A subclass that overrides nothing but constants is [[subclass-that-differs-only-in-data]], and an abstract parent with one subclass is [[base-class-with-one-subclass]]. A parameter, hook or layer added for a future need is [[speculative-generality]], which routes it to its owner.

## When not to apply

- A short element whose name explains its purpose. Fowler extracts even single lines when the name explains purpose (Long Function, PDF p. 87).
- An element at an interface that other code implements or substitutes, such as a seam used by tests. It provides variation, which is one of the purposes in Fowler's list. This reading is this wiki's own.
- A function that is reused from several call sites. Reuse is the second purpose in the list.
- **A polymorphic method.** If subclasses override it, it cannot be inlined (ch. 6, PDF p. 132).
- **A small class several classes use, or one exposed to clients as a value** (a telephone number handed out). This limit is this wiki's own: folding it into one user would duplicate it or take a type away from the others.
- **Inline as a step.** To reallocate features between two classes, Fowler sometimes inlines one into the other and then extracts the new split (ch. 7, PDF p. 213); the same holds for a badly factored group of functions (ch. 6, PDF p. 132). The intermediate large element is then a step, not a finding. See [[keep-objects-small]] for the extraction.

## Repair

Inline Function ([[inline-function]]) or Inline Class. For inheritance, Collapse Hierarchy (PDF p. 94).

Inline Class mechanics (ch. 7, PDF pp. 213-214): in the target class, create a delegating method for each public method of the source; switch every reference to them, testing after each change; move the functions and data over until the source is empty; delete it.

## Before and after

```
function rating(driver)
    return isAboveLimit(lateCount(driver), driver.allowedLate) ? POOR : GOOD

function lateCount(driver)
    return driver.lateDeliveries

function isAboveLimit(value, limit)
    return value > limit
```

```
function rating(driver)
    return driver.lateDeliveries > driver.allowedLate ? POOR : GOOD
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 3, "Lazy Element", PDF p. 94, with "Long Function", PDF p. 87, for extracting single lines. Ch. 6, "Inline Function", PDF p. 132: the occasions, the delegation chain and the polymorphism limit. Ch. 7, "Inline Class", PDF pp. 213-214: the class not pulling its weight, inline-then-extract and the mechanics. This wiki's own: the signs as worded (the delegation chain included), the assignments against neighbouring pages, the seam and reuse limits as worded, the limit for a shared or exposed small class, and the pseudocode.
