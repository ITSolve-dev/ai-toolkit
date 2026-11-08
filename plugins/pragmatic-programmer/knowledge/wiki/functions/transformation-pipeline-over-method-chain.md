---
title: Prefer a transformation pipeline to a method chain
category: functions
summary: "A chain of three or more calls that convert data, each receiver being the differently typed object the previous call returned: pass each result to a free function instead."
tags: [rule, coupling, pipeline, train-wreck]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The book compares two ways of writing the same sequence of steps and prefers the one where each result is named and handed to the next function. In the other style every call returns an object that has to carry the next method, so the intermediate objects are tied to the calling code. The book notes that this is why method chaining is also called «крушением поездов» (p. 358). This wiki reads that as an [[orthogonality]] failure: a change in one place reaches objects that had nothing to do with it.

## Rule

Write a sequence of steps as functions applied to named intermediate values, rather than as methods called on whatever the previous call returned. The book's reason is concrete: in the chained form, the object returned by each step must implement the following call, so that object is bound to this code (p. 358).

The book's test is a changed requirement. Suppose lines starting with `#` must now be ignored. In the step-by-step form this is one more line, and the new step can be swapped with its neighbour. In the chained form the swap is harder, and two questions open that the pipeline never raises: which returned object should own the new method, and what other code breaks if that object changes (p. 358).

This wiki separates the page from [[train-wreck]], which says temporaries are not a repair. There each temporary is an object whose members the next line reaches into. Here each temporary is a value handed to a function that does not belong to it, so no step depends on what the previous result can do. The test is which side of the dot the next step sits on. For a chain that navigates held objects, use the repair on [[train-wreck]]. For a chain of work done on data, use this page. The concept behind it is [[programs-transform-data]].

## Sign in code

- A chain of three or more calls that convert data, in which each receiver is the object returned by the previous call, and those objects are of different types: `readFile(p).matching(x).truncated()`.
- A method that exists on an intermediate class only so the next link of one chain can be called.

This wiki adds the first sign's conditions on type and length. The floor of three links follows the book's advice to chain no more than two method calls (p. 172). The book's example does not discuss chains over a single type.

## When not to apply

The book states no limit here. The limits below are this wiki's own.

- Every call returns the same type and the chain assembles one value, as in a query builder, or the chain is an operation over a standard collection. No sequence of different classes is coupled, and a new step has one obvious owner. The limits on [[train-wreck]] draw the same line.
- The steps genuinely share private state of one receiver, so pulling them apart into functions would expose that state.
- A lookup on one object followed by a command on the result, such as `user.findPlan(id).extend(days)`. That is the repair of [[tell-dont-ask]], which owns the shape.

## Repair

1. Name each intermediate value.
2. Turn each step into a function that takes that value as an argument and returns the next one.
3. Put a new step in as one new function and one new line. No existing class changes.
4. Once no chain needs it, remove from intermediate classes any method that existed only to continue a chain.

## Before and after

Before: a new step needs a home on one of the returned classes.

```
total = loadReport(path).parsedRows().activeOnly().sumOfAmounts()
```

After: the new step, dropping header rows, is a line of its own and can move.

```
text   = readFile(path)
rows   = parseRows(text)
body   = dropHeaderRows(rows)
active = keepActive(body)
total  = sumAmounts(active)
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), answer to exercise 23, p. 358, and p. 172 for the advice on chained calls. The preference, the reasoning and the changed-requirement test are the book's. The second sign, the separation from [[train-wreck]], the limits, the repair steps and the pseudocode are this wiki's own.
