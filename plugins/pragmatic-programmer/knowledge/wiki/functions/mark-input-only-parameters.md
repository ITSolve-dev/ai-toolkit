---
title: Make input-only parameters visible in the signature
category: functions
summary: "A signature leaves its input-only parameters unmarked although the language or project has a read-only marker (const, final, readonly, an agreed prefix) used elsewhere in the code, or a parameter carrying that marker or prefix appears on the left of an assignment or as the receiver of a mutating call."
tags: [rule, parameters, mutation, naming, side-effects]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Programmers sometimes change an input parameter by accident. Some languages make the author state whether changes to a parameter are visible to the caller; in others, a change to a passed object is visible whether or not it was intended. McConnell gives Java as his example, where an object passed to a method may come back changed (*Code Complete*, Russian edition, p. 267).

## Rule

McConnell's rule is that where the language does not enforce it, a naming convention should mark parameters that are input only. He suggests a `const`, `final` or `nonmodifiable` prefix. With such a convention, if you see a name with that prefix on the left of an assignment, «вы будете знать, что произошла ошибка» (p. 267). The same holds for a mutating call on it, such as `constMax.SetNewMax(...)` (p. 267). The chapter checklist repeats the rule (p. 280). This wiki reads the rule's aim as making the signature say which parameters the routine promises not to change, so that a write to one of them is visible as a defect.

## Sign in code

- A parameter that the routine only reads, declared without the read-only marker that the language offers and that the codebase uses on other signatures.
- A parameter that carries a read-only prefix or marker appearing on the left of an assignment, or as the receiver of a mutating call (the book's own check, p. 267).

This wiki assigns the neighbouring cases as follows. This page owns the signature: whether input-only is declared. Marking which parameters are input only is [[mark-input-only-parameters]]; the order of the list is [[parameter-order]]. A routine that reassigns its own parameter variable and reads it again is [[do-not-reuse-parameters-as-working-variables]]. A function that writes fields of a plain record or element it received as an argument is [[do-not-mutate-input-data]]; a method that calls a mutator on an object it received, or a class whose fields are reassigned after construction, is [[immutable-objects]].

## When not to apply

- Where a linter or compiler already reports the missing marker, it is mechanical style and left to the tooling.
- A parameter that is documented as an in/out or output parameter is supposed to change, so this page does not apply.
- In code written in a functional style over immutable values nothing can be mutated, so the sign cannot occur.

## Repair

Where the language has a read-only marker (`const`, `final`, `readonly`, an immutable type), use it rather than a prefix; this preference is this wiki's own, because a compiler enforces a marker and not a name. The book's prefix rule is for languages that lack one (p. 267).

In order of preference (this ordering is this wiki's own):

1. Declare the parameter read-only with the language's feature, or pass an immutable value.
2. If the routine needs a working copy, copy it into a local and change the local.
3. Only where neither is available, adopt a project-wide prefix for input-only parameters and treat a prefixed name on the left of an assignment as a defect.

## Before and after

```
function invoiceTotal(readonly lines, readonly taxRate): ...
function discountedTotal(order, rate):       // only reads order, unmarked
    return order.total * (1 - rate)
```

```
function invoiceTotal(readonly lines, readonly taxRate): ...
function discountedTotal(readonly order, readonly rate):
    return order.total * (1 - rate)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 267, 280 ([[code-complete]]). The rule, the const/final prefix, the 'prefix on the left of an assignment means a defect' check and the Java caveat come from the book. The first sign as worded, the ownership split, preferring the language's read-only feature to a prefix, the copy-to-local repair, the functional-style limit and the pseudocode are this wiki's own. The book places the rule in its chapter on naming; this wiki files it under functions because the problem a reader arrives with is a parameter that changed.
