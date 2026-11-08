---
title: Replace inline code with an existing function call
category: complexity
summary: "A block of statements inside a routine computes what an existing function in scope (the project's own or a library's) already computes, such as a hand-written max loop where max exists: call the function, unless its name would read wrong in that place, which shows the likeness is coincidental."
tags: [decision-rule, duplication, naming, library-reuse]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's Replace Inline Code with Function Call removes duplication between inline code and a function that already exists. Its value for this wiki is the test it gives for whether the likeness is real: whether the function's name makes sense in place of the inline code.

## Rule

If inline code does the same thing as an existing function, replace it with a call (*Refactoring*, 2nd ed., ch. 8, PDF p. 251). The named function explains purpose rather than mechanics, and a later change to its implementation does not mean hunting down look-alike code. Fowler finds this "particularly satisfying" with library functions: "that way, I don't even have to write the function body" (p. 251).

## Sign in code

A block of statements inside a routine that computes what an existing function in scope computes. Examples are a hand-written loop summing a field where a `sum` helper exists, or a hand-rolled trim, min or max where the standard library has one.

This wiki assigns the neighbouring cases as follows. A block of statements inside a routine that computes what one existing function already computes is [[replace-inline-code-with-function-call]]; a hand-written general-purpose part (its own routine or class) that the library already provides is [[use-existing-components-before-writing-your-own]]. Two existing functions with identical bodies whose names refer to different things are [[coincidental-duplication]], and the name test below is the test that page needs at the level of one block.

## When not to apply

The similarity is coincidental: "if I change the function body, I don't expect the behavior in this inline code to change" (p. 251). Fowler's guide is the name: "A good name should make sense in place of inline code I have" (p. 251). If it does not, then either:

- the name is poor, so rename the function and then call it, or
- the function's purpose differs from what this code wants, so do not call it.

This wiki reads the test as one a reader can apply to the code in front of them, by reading the candidate call aloud in place of the block. Read with [[dry]], it marks the boundary between one piece of knowledge written twice and two pieces of knowledge that happen to look alike.

## Repair

Replace the inline code with a call to the existing function, then test (p. 251). If the name was the obstacle, rename first.

## Before and after

```
shippingCost(order):
  heaviest = order.items[0].weight
  for item in order.items:
    if item.weight > heaviest: heaviest = item.weight
  return rateFor(heaviest)
```

```
shippingCost(order):
  return rateFor(max(order.items.map(i -> i.weight)))
```

A counter-case that stays inline: a function `clampPercent(x)` returns `min(max(x, 0), 100)`, and inline code clamps a volume level to 0..100. `clampPercent` reads wrong for a volume, so the two are not the same knowledge.

## Source

Fowler, *Refactoring*, 2nd ed., ch. 8, Replace Inline Code with Function Call, PDF p. 251 ([[fowler-refactoring]]): the rule, the library case, the coincidence limit and the name test. The sign as worded, the assignment against neighbouring pages, the pseudocode pair and the clamp counter-case are this wiki's own.
