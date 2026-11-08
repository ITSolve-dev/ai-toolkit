---
title: Mutable data
category: types-and-state
summary: "Concept: why updating data in place is risky in proportion to its scope, after Fowler's Mutable Data smell; routes each shape (a reused variable, a setter on a field that need not change, a stored derived value, an argument modified in place, a function that both returns and changes state) to the page that owns it."
tags: [concept, mutation, immutability, side-effects, state]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's **Mutable Data** smell: an update in one place can break another part of the software that expected something different, and the failure is especially hard to spot when it happens only under rare conditions (ch. 3, Mutable Data, PDF p. 89). An entire school, functional programming, is built on never changing data; this wiki reads Fowler as treating that as one end of a scale. In languages that allow mutation, "there are still many things we can do to limit the risks on unrestricted data updates" (PDF p. 89).

## Scope decides the risk

"Mutable data isn’t a big problem when it’s a variable whose scope is just a couple of lines—but its risk increases as its scope grows" (PDF p. 90). This wiki reads that as the limit common to every page below: a local accumulator inside a short function is not a finding of any of them.

## The shapes and their owners

Fowler pairs each risk with a refactoring (PDF pp. 89-90). This wiki routes each shape to the page that owns it:

| Shape | Fowler's repair | Owner |
|---|---|---|
| Data updated from many places with no narrow update function | Encapsulate Variable | [[global-data]] for module or static data, with the procedure on [[encapsulate-variable]]; a record manipulated field by field from many places, [[replace-direct-data-manipulation-with-adt]] |
| One variable assigned to hold different things in turn | Split Variable | [[one-variable-one-purpose]] |
| An API function that both returns a value and changes state | Separate Query from Modifier | [[command-query-separation]] |
| A setter on a field that should not change after construction | Remove Setting Method | [[immutable-objects]] |
| A mutable field whose value can be computed from other data | Replace Derived Variable with Query | [[stored-derived-data]] |
| A holder's setter that writes a field of a nested object only that holder refers to, rather than replacing the nested object whole | Change Reference to Value | [[reference-or-value]] |
| A function that writes fields of a plain record or element it received as an argument | none named in this smell; this row is this wiki's | [[do-not-mutate-input-data]] |

Two of Fowler's moves have no sign of their own here. He uses Slide Statements and Extract Function to separate side-effect-free code from the update, and Combine Functions into Class or Combine Functions into Transform to limit how much code updates a variable (PDF p. 90). This wiki treats them as repair steps inside the owners above. On Remove Setting Method, Fowler adds that looking for a setter's clients can itself show how to narrow the variable's scope (PDF p. 90).

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 3, "Mutable Data", PDF pp. 89-90. Fowler's text for Change Reference to Value is "If a variable contains some data with internal structure, it’s usually better to replace the entire structure rather than modify it in place" (PDF p. 90). The reading of the scope remark as a common limit, the "one end of a scale" reading, the argument row and the routing to owner pages are this wiki's own.
