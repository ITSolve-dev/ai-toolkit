---
title: Tame deep nesting
category: complexity
summary: "if/switch blocks nested more than three or four levels inside one routine, alone or inside a loop, with long bodies between levels, or nested ifs whose inner test re-narrows a range the outer one already fixed (q > 10, then q > 100, then q > 1000)."
tags: [rule, nesting, control-flow, conditionals]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell calls excessive indentation one of the main culprits of confusing code and cites researchers who found that few people understand more than three levels of nested `if`, with many recommending no more than three or four levels (p. 438). He ties it to managing complexity, the book's central technical imperative (see [[managing-complexity]]), and calls that reason enough to avoid it. He also reads deep nesting as a symptom: complicated code is a sign that the programmer does not yet understand the program well enough to make it simple, and deep nesting is a warning to add a routine call or redesign that part (p. 447).

This wiki assigns the neighbouring cases as follows. This page owns the **depth of nested decisions in one routine**, including decisions nested inside a loop, when the depth does not come from a chain of precondition checks. Where the polarity of the tests alternates, so that the normal case sits in the `if` at one level and in the `else` at the next, [[nominal-path-first]] owns the order of the branches; apply it first. Where every test checks success and the nominal work sits three or more levels deep, [[guard-clauses]] owns the sign. Nesting depth counts loops and decisions together. Where every level is a loop, [[loop-length-and-nesting]] owns it; where any level is an `if`/`switch`, [[tame-deep-nesting]] owns it. A loop too long to see whole is [[loop-length-and-nesting]]. A flat `switch` on a type code whose arms call per-type routines is [[polymorphism-or-type-switch]]. A routine that is shallow but has many branches is [[decision-point-count]].

## Rule

Keep nesting inside a routine to three or four levels at most (p. 438). When it goes deeper, restructure: the book lists retesting part of a condition, converting to an `if-then-else` chain, converting to a `case`, factoring the nested body into a routine, using polymorphic dispatch, a status variable, guard clauses, exceptions, and full redesign (pp. 447-448). It says one need not rewrite the whole routine, «но у вас должна быть веская причина не делать этого» (p. 447).

## Sign in code

- More than three or four levels of `if`/`switch` blocks inside one routine, counted from the routine body; a loop level that contains them counts too.
- Nested `if`s where an inner test is implied by an outer one, e.g. `if (q > 10) { if (q > 100) { if (q > 1000) ...`: each level re-establishes a range the previous level already narrowed (pp. 440-441).
- A loop whose body holds a decision three or more levels deep with long inline actions, so that the loop and its decisions together exceed the three-to-four-level threshold (pp. 442-443).

## When not to apply

- The book's own threshold is three or four levels. This wiki reads two or three short levels that fit on one screen as no finding; the long "lots of code" bodies between levels in the book's example (p. 439) are part of what makes the depth harmful.
- Retesting a condition is not free: the book says you cannot reduce nesting «безнаказанно», because the conditions get more complex (p. 440). Where the flattened condition would be harder to read than the nesting, do not use that repair.
- The "block with exit" idiom (`do { ... break; ... } while (false)`) is unusual; the book allows it only if the whole team knows it and has approved it as a practice (p. 440).

## Repair

This wiki maps the book's repairs (pp. 439-447) to shapes:

1. **Nested ranges or implied conditions**: a flat `if / else if` chain ordered so each test relies on the previous one failing, or a `case` over ranges where the language has one. If the ranges are not ordered, write each condition in full so the order no longer matters; the book keeps the `else` form only to avoid repeated tests (p. 442).
2. **Sequential preconditions each guarding a long block**: retest the combined condition at a lower level, exit early with [[guard-clauses]], or use a status variable.
3. **Nesting built from both loops and decisions**: keep the `if`/`switch` in the loop to show the branching, and move each branch's body into its own routine (p. 442). Once extracted, the remaining dispatch often turns into a `case` (p. 444). The book names what extraction buys: two-level nesting, a loop that fits on one screen, and the ordinary benefits of modularity (p. 444).
4. **Dispatch on a type code**: see [[polymorphism-or-type-switch]]; the book's own transaction example ends there (pp. 445-447).
5. **None fits**: redesign the routine (p. 447).

## Before and after

Implied ranges, four deep:

```
if quantity > 10
    if quantity > 100
        if quantity > 1000
            if quantity > 10000
                discount = 0.15
            else
                discount = 0.10
        else
            discount = 0.05
    else
        discount = 0.025
else
    discount = 0
```

```
if quantity > 10000      discount = 0.15
else if quantity > 1000  discount = 0.10
else if quantity > 100   discount = 0.05
else if quantity > 10    discount = 0.025
else                     discount = 0
```

This page owns only the depth, and the flat chain is where it stops. Whether a chain becomes a table is [[drive-repeated-dispatch-from-a-table]]; which access scheme the table uses is [[choose-table-access-scheme]]. A chain of irregular thresholds that only assigns constants, like this one, is the next question for those pages, not a remaining finding here.

A loop with inline nested decisions:

```
for order in orders
    if order.region == DOMESTIC
        if order.weight > 20
            if order.express
                order.cost = HEAVY_RATE * order.weight * EXPRESS_FACTOR
            else
                order.cost = HEAVY_RATE * order.weight
        else
            if order.express
                order.cost = LIGHT_RATE * EXPRESS_FACTOR
            else
                order.cost = LIGHT_RATE
    else
        order.cost = foreignCost(order)
```

```
for order in orders
    order.cost = shippingCost(order)

shippingCost(order)
    if order.region != DOMESTIC  return foreignCost(order)
    base = domesticBase(order.weight)
    if order.express  return base * EXPRESS_FACTOR
    return base

domesticBase(weight)
    if weight > 20  return HEAVY_RATE * weight
    return LIGHT_RATE
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.4, pp. 438-448: see [[code-complete]]. The three-to-four-level threshold, the list of repairs and their costs, the team-approval limit on the exit block and the reading of nesting as a symptom are the book's. The sign wording, the reading that two or three short levels are no finding, the shape-to-repair mapping, the owner assignments and the hand-off of the flattened chain to the table pages are this wiki's own. The pseudocode is this wiki's; the first pair follows the book's discount example (pp. 440-442) with a fourth level added, and the second pair replaces the book's transaction example, whose "after" still dispatches on a type code. Related: [[decision-point-count]], [[structured-programming]].
