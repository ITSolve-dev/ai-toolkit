---
title: Limit a routine to about seven parameters
category: functions
summary: "A routine (not a constructor) declares clearly more than seven parameters: the routine is too tightly coupled to its callers."
tags: [rule, parameters, coupling, interfaces]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell bases the limit on Miller (1956), who found that people generally cannot track more than about seven chunks of information at once: «7 — магическое число.» (*Code Complete*, p. 174). He reasons that most people therefore cannot hold more than seven of a routine's parameters in mind at once. His opening bad example takes 11 and lays them out so that most developers would not even try to count them (p. 159).

## Rule

Keep a routine's parameter list to about seven. A long list is a symptom, and the book states what it is a symptom of: «Если вам постоянно приходится передавать в методы слишком большое число аргументов, ваши методы имеют слишком сильное сопряжение.» (p. 174). Its repair is to design routines, or groups of routines, for loose coupling. If the same data goes to many routines, gather the routines and the data into a class (p. 174).

What counts as one item depends on the language. Where structured data is available, a composite of 13 fields passes as one item (p. 174).

Beck and Fowler's **Long Parameter List** smell gives the history of the trade-off. Passing everything a function needs as parameters was taught as the alternative to global data, which "quickly becomes evil", but "long parameter lists are often confusing in their own right" (*Refactoring*, 2nd ed., ch. 3, Long Parameter List, PDF p. 88). This wiki reads that as a limit on every repair below: a list is never shortened by moving parameters into global state ([[global-data]]).

## Sign in code

- A routine declaration with more than seven parameters.

This wiki assigns the neighbouring cases as follows. The same run of three or more loose variables or parameters passed field by field at several sites is [[group-related-data-into-a-structure]]. A parameter list too long whatever its contents is [[limit-parameter-count]]. Constructor parameter counts, and a class needing many fields, are [[keep-objects-small]]; this page owns parameter lists of ordinary routines. Whether a routine takes an object or the fields it reads is [[pass-what-the-routine-uses]]. A value the callee could derive from another of its parameters or from its own object is [[parameter-or-query]]; several values unpacked from one record and passed instead of the record is [[pass-what-the-routine-uses]].

## When not to apply

- **Grouping only to hit the number.** This wiki adds, drawing on [[pass-what-the-routine-uses]]: packing unrelated parameters into a struct to meet the count hides the coupling rather than removing it. If the caller fills a record only so the routine can unpack it, the group is not a value.
- **Seven is a guideline.** The book says "about seven". This wiki reads that so a routine with eight cohesive, distinct, named parameters is not a finding just for being eight; cite this page for lists that clearly exceed the number.
- **Named or keyword arguments** make long lists easier to call correctly ([[match-arguments-to-parameters]]), but this wiki notes they do not reduce the coupling the book is pointing at.

## Repair

1. Find parameters that always travel together and mean one thing. Make them one value (a record or a small object).
2. Where several routines all receive the same data, make the data the state of a class and the routines its methods.
3. Remove parameters the routine does not use ([[remove-unused-parameters]]).
4. If the routine needs many unrelated inputs because it does several jobs, split it ([[routine-cohesion]]).

Fowler pairs each way of shortening a list with its own case (PDF p. 88):

- A parameter the routine could get by asking another parameter for it: Replace Parameter with Query, decided on [[parameter-or-query]]. Fowler's limit there: the query must not add an unwanted dependency to the function body (ch. 11, PDF p. 363).
- Several values pulled out of one existing structure and passed separately: Preserve Whole Object. Whether to pass the object or the values is decided on [[pass-what-the-routine-uses]].
- Parameters that always travel together: Introduce Parameter Object ([[group-related-data-into-a-structure]]).
- A parameter used as a flag to dispatch different behaviour: Remove Flag Argument. A flag that selects unrelated jobs is [[routine-cohesion]].
- Several functions sharing several parameter values: Combine Functions into Class, which captures the common values as fields. Fowler notes that in functional terms this creates a set of partially applied functions. It is the same repair as step 2 above.

## Before and after

```
routine DrawBox(x, y, width, height, borderColor, fillColor, borderWidth,
               shadow, cornerRadius, opacity, label)
```

```
record Rect(x, y, width, height)
record BoxStyle(borderColor, fillColor, borderWidth, shadow, cornerRadius, opacity)

routine DrawBox(rect, style, label)
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.5, p. 174; the opening example, p. 159 ([[code-complete]]). The limit, Miller's study, the coupling diagnosis and the repair by grouping into a class are the book's.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Long Parameter List", PDF p. 88: the history against global data and the five repairs with their cases. Ch. 11, "Replace Parameter with Query", PDF p. 363: the dependency limit. This wiki's own for that part: the reading as a limit against global state and the routing to owner pages.
- The sign, the owner split with [[keep-objects-small]], [[pass-what-the-routine-uses]] and [[group-related-data-into-a-structure]], the limits and the pseudocode are this wiki's own.

Related: [[coupling]], [[parameter-order]].
