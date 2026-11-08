---
title: Inside-out loop construction
category: functions
summary: "A procedure for writing a hard loop correctly the first time: code one action with constants, wrap it in a loop, replace constants with indexes, add initialization last."
tags: [method, loops, stepwise-construction, pseudocode]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell offers a simple way to get a complicated loop right the first time, which he calls «кодирование изнутри наружу» (p. 378). It starts from one concrete case and generalizes outward, so that only one concern is open at any moment. He relates it to the pseudocode programming process of his chapter 9.

## Procedure

«Начните с одного действия. Закодируйте его с помощью констант.» (p. 378) Then, step by step:

1. Write the steps the loop body must perform as comments, without syntax or indexes.
2. Replace the comments with code for one concrete case, using real data and leaving array indexes empty or constant.
3. Add the indexes the data needs.
4. Wrap a loop around the existing statements, choosing an index that ranges over the cases.
5. Fix every expression that must vary with the new index.
6. Add initialization last.
7. Repeat outward for each further loop level.

McConnell's worked example totals insurance rates for a group (pp. 378-379). The steps are: "get rate from table; add to total". Then `rate = table[]`, then `table[census.Age][census.Gender]`, then the `for person` loop around it, then `census[person]`, and finally `totalRate = 0`. He says the order need not be followed rigidly. The point is to start from something concrete, think about one thing at a time, and grow the loop in small, understandable steps, which minimizes how much code must be held in mind at once (p. 379).

## When to use it

This wiki adds when to use it. It suits a nested or index-heavy loop whose subscripts are hard to get right in one pass. It also suits rebuilding a loop that failed [[check-loop-boundaries-by-hand]]. For a single loop over a collection with no index arithmetic it adds nothing.

## Example

```
// step 2: one case, constants
rate = table[42][FEMALE]
total = total + rate

// step 4-5: loop around it, constants replaced
for person in group:
    rate = table[person.age][person.gender]
    total = total + rate

// step 6: initialization last
total = 0
for person in group:
    total = total + table[person.age][person.gender]
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 16.3, pp. 378-379. The "when to use it" section and the example's concrete constants are this wiki's own. See also [[small-steps-with-feedback]].
