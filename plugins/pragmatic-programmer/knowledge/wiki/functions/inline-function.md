---
title: "Inline Function: the mechanics"
category: functions
summary: "Procedure for putting a function's body back into its callers and deleting it: check it is not polymorphic, replace one call at a time and test, move statement by statement when the body does not paste in cleanly; do not attempt it on recursion, several returns or another object's internals. Also the first step of re-factoring a badly split group of functions or a chain of pure delegations."
tags: [method, refactoring, inline-function, indirection]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Inline Function** (formerly Inline Method) replaces calls to a function with its body and then deletes the function. It is the inverse of [[extract-function]]. Fowler favours short functions named for their intent, and this refactoring is the limit he sets on that preference: "Indirection can be helpful, but needless indirection is irritating" (*Refactoring*, 2nd ed., ch. 6, "Inline Function", PDF p. 132).

When a function should go is decided elsewhere. A function whose name only restates its body, or a class reduced to one simple function, is [[lazy-element]], which owns the sign. A function whose name says *what* where its body says *how* stays however short ([[extract-routine-to-name-a-step]]). A class whose methods mostly forward to one field is [[hide-delegate-or-remove-middle-man]], whose repair may use this procedure. This page is the procedure.

## When to run it

Fowler gives three occasions (PDF p. 132):

1. The body is as clear as the name, or a refactoring has made it so.
2. A group of functions is badly factored. He inlines them all into one large function and then extracts again along better lines.
3. Too much indirection: "every function does simple delegation to another function, and I get lost in all the delegation" (PDF p. 132). Inlining shows which hops earn their place; the rest go.

This wiki reads the second occasion as a step, not a finding: the large function it produces is temporary and is not reported under [[routine-length]] while the re-extraction is under way.

## Procedure

Fowler's mechanics (PDF pp. 132-133):

1. Check that the function is not polymorphic. If subclasses override it, it cannot be inlined.
2. Find all callers.
3. Replace each call with the body, fitting parameter names to the caller's arguments, and test after each replacement. The callers need not all be done at once.
4. Remove the definition.

When the body does not paste in cleanly, for example a helper that pushes lines into an output collection it receives, Fowler moves one statement at a time to the callers (Move Statements to Callers, [[move-statements-across-call-boundary]]). His principle: "always be ready to take smaller steps", and if a quick attempt breaks the tests he prefers "to revert back to my last green code and repeat the refactoring with smaller steps" (PDF p. 135). See [[refactor-in-small-tested-steps]].

## Where it stops

- **Polymorphic methods** cannot be inlined (PDF p. 132).
- **Recursion, several return points, inlining into another object that has no accessors.** Fowler deliberately gives no mechanics for these: "if you encounter these complexities, you shouldn’t do this refactoring" (PDF p. 133).
- **A seam.** A function that tests or other implementations substitute provides variation and stays; [[lazy-element]]'s limits keep it. This cross-reference is this wiki's own.

## Example

```
function rating(driver)
    return moreThanFiveLateDeliveries(driver) ? 2 : 1

function moreThanFiveLateDeliveries(d)
    return d.lateDeliveries > 5
```

```
function rating(driver)
    return driver.lateDeliveries > 5 ? 2 : 1
```

The statement-by-statement case. It shows the mechanics only: `gatherCustomerData` names a step, and whether to inline it is decided on [[lazy-element]].

```
function reportLines(customer)
    lines = []
    gatherCustomerData(lines, customer)
    return lines

function gatherCustomerData(out, customer)
    out.add(["name", customer.name])
    out.add(["location", customer.location])
```

```
function reportLines(customer)
    lines = []
    lines.add(["name", customer.name])
    lines.add(["location", customer.location])
    return lines
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Inline Function", PDF pp. 131-135: the irritating-indirection remark, the three occasions, the polymorphism and complexity limits, the mechanics, moving statements to callers and the revert-to-green advice. This wiki's own: the assignment of the sign to [[lazy-element]] and [[extract-routine-to-name-a-step]], the reading of the second occasion as a step, the seam limit, and the pseudocode.
