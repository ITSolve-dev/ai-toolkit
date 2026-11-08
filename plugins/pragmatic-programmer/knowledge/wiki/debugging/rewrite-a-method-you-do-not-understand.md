---
title: Rewrite an erratic method instead of patching it
category: debugging
summary: "Two or more special-case branches in one method, keyed to particular input values, that correct the result its general path already computed (often with comments naming bugs); decide rewrite from pseudocode over another patch."
tags: [decision-rule, debugging, change, rewrite]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

At the error-removal step of the [[pseudocode-programming-process]], McConnell argues that a method still behaving unstably at that point will likely stay that way, and that on finding behaviour you cannot explain you should start over: «Не пытайтесь доводить его до ума — перепишите его.» (*Code Complete*, Russian edition, p. 224). His reasoning, paraphrased: elaborate patching usually signals incomplete understanding and guarantees errors now and later; completely redesigning an unstable method is justified, and few things are as effective as rewriting a problem method (p. 224). The same chapter's checklist ends by asking whether you fully understand your code (p. 226), and the check step holds that working is not enough without knowing why it works (p. 223; see [[programming-by-coincidence]]).

This page decides between two courses at one point: another local fix, or a rewrite of the method from its pseudocode.

## Rule

When a method behaves in ways you cannot explain, rewrite it rather than refine it (p. 224).

This wiki extends the rule from a method just written, at the error-removal step where the book places it, to a standing method whose fixes so far are local corrections of its output, and that extension is what the signs below detect.

## Sign in code

The source gives no sign in code; these are this wiki's own:

- Two or more conditionals keyed to particular literal input values that adjust a result already computed by the general path (`if id == 17 then total = total - 1`).
- Two or more corrections applied after the main computation ("clamp", "fix up", "adjust") whose comments name a bug or a case, not a rule of the problem.
- The same variable reassigned in several late branches to undo or offset earlier assignments.

A reader can point at each of these in the method in front of them; the history of how it got that way is not needed.

This wiki assigns the neighbouring cases as follows. This page owns two or more input-keyed corrections accreted in one method on its own computed result. A single offset applied to a value received from elsewhere is [[fix-the-model-not-the-offset]]. A guard a fix adds at the failing line, absorbing the value by returning, defaulting or catching, and a single input-keyed correction of a computed result added by a fix, are [[fix-the-root-cause]]. Two or more input-keyed corrections accreted in one method on its own computed result are [[rewrite-a-method-you-do-not-understand]]. A routine chosen by its fix history rather than by the shape in front of the reader is [[metric-outlier-review]].

## When not to apply

- The cause has been found and is understood: then the right repair is the targeted fix for that cause, however small, and a rewrite only adds risk. The source's trigger is behaviour you do not understand (p. 224).
- The special case is a real rule of the problem (a documented exception in the domain) rather than a compensation for wrong output; it then belongs in the design and does not count as a sign.
- The method is large and widely used, and no tests pin its current behaviour: rewriting first needs tests that capture what callers rely on. This limit is this wiki's own; see [[refactor-in-small-tested-steps]].

## Repair

1. Stop patching. Write down, as intent-level pseudocode, what the method must do, including the cases the patches were compensating for.
2. Rebuild the method from that pseudocode, keeping the pseudocode as its comments (see [[pseudocode-programming-process]] and [[comment-why-not-how]]).
3. Run the tests planned for it, adding a test for each case a removed patch was handling ([[failing-test-before-the-fix]]).

## Before and after

```
function shippingDays(order)
    days = order.distanceKm / 500 + 1
    if order.region == "north" then days = days + 2
    // bug 412: orders exactly at 1000 km came out one day short
    if order.distanceKm == 1000 then days = days + 1
    // bug 431: weekend orders too optimistic
    if order.placedOn == SATURDAY then days = days + 1
    if order.placedOn == SUNDAY and days < 3 then days = 3
    return days
```

```
function shippingDays(order)
    // Transit: one day per started 500 km, never less than one
    transit = max(1, ceil(order.distanceKm / 500))
    // Northern region: documented two extra days
    if order.region == "north" then transit = transit + 2
    // Shipping starts on the next working day
    return daysUntilNextWorkingDay(order.placedOn) + transit
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, p. 224 for the rule and its reasoning; p. 223 and p. 226 for understanding as the requirement. The book places the rule at the error-removal step for a method just written; its extension to a standing method whose fixes are local corrections of its output is this wiki's own. The signs in code, the assignment against the neighbouring pages, the limits other than the source's trigger, the repair steps and the pair are this wiki's own.
