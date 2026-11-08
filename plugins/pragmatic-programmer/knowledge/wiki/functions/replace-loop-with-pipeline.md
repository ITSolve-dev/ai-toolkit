---
title: Replace a loop with a collection pipeline
category: functions
summary: "A loop whose whole body selects, transforms or accumulates one collection (an accumulator declared before it, a first-time flag or continue that skips items, an if that filters, a local that reshapes the item, an append or a running total), in a language or project that has first-class functions and filter/map/reduce."
tags: [rule, loops, collection-pipeline, functional-style]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Beck and Fowler's **Loops** smell reflects a shift between the editions of *Refactoring*: first-class functions are now widely supported, so loops can be retired with Replace Loop with Pipeline (ch. 3, Loops, PDF p. 94). Their reason is readability: "pipeline operations, such as filter and map, help us quickly see the elements that are included in the processing and what is done with them" (PDF p. 94).

The catalogue entry (ch. 8, PDF pp. 261-266) defines a collection pipeline as "a series of operations, each consuming and emitting a collection" (p. 261), and restates the reason: "I can then read from top to bottom to see how objects flow through the pipeline" (p. 261). The commonest stages are map, which transforms each element, and filter, which selects a subset.

## Rule

Where a loop only selects, transforms or aggregates a collection, and the language environment provides collection pipelines, write it as a pipeline of named operations (p. 261).

## Sign in code

A loop over a collection whose body is made only of some of the following, with nothing else in it (p. 262 for the parts):

- a control flag or index check that skips the first item (a header line);
- `continue`, or an `if` wrapping the rest of the body, that drops items;
- a local that reshapes the item;
- an append into an accumulator declared before the loop, or a running total, that the function returns.

Each part maps onto one pipeline stage: slice, filter, map, and the result.

This wiki assigns the neighbouring cases as follows. A loop whose body only filters, maps or accumulates one collection is [[replace-loop-with-pipeline]]. A loop that does that alongside other work is split first under [[one-loop-one-job]], and an accumulator taken out of such a loop follows the procedure in [[remove-loop-accumulator]]. A chain of calls each made on the differently typed object the previous call returned is [[transformation-pipeline-over-method-chain]]. A collection pipeline returns the same kind of object at each step, so it is not that page's sign.

## When not to apply

Fowler motivates the refactoring by the fact that environments increasingly provide pipelines (p. 261) and states no other limit. This wiki adds:

- The language or the project has no first-class functions or pipeline idiom. The source ties the smell to their being available.
- The loop's iterations depend on each other other than through the final accumulation: a running state that each step reads and updates, several interacting accumulators, index arithmetic, or an early exit tied to state. Such a loop does not split into independent stages, and Fowler shows only stateless stages and an accumulating reduce. An early exit on the first hit is [[stop-loop-once-answer-known]].
- A hot loop where the project has measured that the pipeline costs too much. [[premature-code-tuning]] sets the burden of proof: without the measurement, the claim of cost does not keep the loop.

## Repair

Fowler's mechanics (pp. 261-262):

1. Create a new variable for the collection the loop iterates over.
2. Starting at the top of the body, replace each piece of behaviour with a pipeline operation in the derivation of that variable, testing after each. The skip becomes a slice or `filter`, the reshaping becomes `map`, the accumulator a fold or `sum`.
3. When the body only appends to the accumulator, assign the pipeline's result to the accumulator and remove the loop.
4. Tidy up: inline the accumulator, rename the lambda parameters (in his example `record` becomes `fields`) and make the layout "read more like a table" (p. 266). The control variable disappears along the way; Fowler says he particularly enjoys deleting control variables (p. 263).

Fowler kept an intermediate variable (`lines`) that he could have inlined, because "its presence explains what's happening" (p. 266). Compare [[explaining-variable]]. A loop that does two jobs is split first ([[one-loop-one-job]]); his own sequence is Split Loop, then Extract Function, then the pipeline (p. 260).

## Before and after

```
names = []
for p in people
    if p.city == homeCity
        names.add(p.name)
```

```
names = people
    .filter(p -> p.city == homeCity)
    .map(p -> p.name)
```

With a header skip and a reshape, after the book's example:

```
indiaOffices(csv):
  lines = csv.splitLines()
  first = true
  result = []
  for line in lines:
    if first: first = false; continue
    if line.trim() == "": continue
    record = line.split(",")
    if record[1].trim() == "India":
      result.append(Office(city = record[0].trim(), phone = record[2].trim()))
  return result
```

```
indiaOffices(csv):
  lines = csv.splitLines()
  return lines
    .drop(1)
    .filter(line   -> line.trim() != "")
    .map   (line   -> line.split(","))
    .filter(fields -> fields[1].trim() == "India")
    .map   (fields -> Office(city = fields[0].trim(), phone = fields[2].trim()))
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed.: ch. 3, "Loops", PDF p. 94, for the smell and its reason; ch. 8, "Replace Loop with Pipeline", PDF pp. 261-266, for the definition, the parts of the loop, the mechanics, the tidy-up and the kept intermediate variable. The sign as worded, the limits, the assignments against neighbouring pages and the pseudocode are this wiki's own; the second pair follows the book's example.
