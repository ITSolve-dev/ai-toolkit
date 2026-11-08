---
title: Check loop boundaries by hand
category: debugging
summary: "A loop bug 'fixed' by flipping < to <= or adding or subtracting 1 from an index until a test passes, with no walk through the first, a middle and the last iteration."
tags: [method, loops, off-by-one, termination, mental-simulation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell describes a short procedure for convincing yourself that a loop is right, and sets it against the alternative he sees in unskilled programmers: tweaking the comparison and the index until the output looks right (p. 374). The procedure targets the two classic loop failures, off-by-one and non-termination.

## Procedure

1. **Walk three points.** Mentally run the first iteration, an arbitrary iteration in the middle and the last iteration, and confirm there is no off-by-one error (p. 374).
2. **Walk the special cases.** If the loop has cases that behave differently from the first or last iteration, check those too (p. 374).
3. **Compute by hand.** If the loop does complex arithmetic, check it with a calculator (p. 374).
4. **Confirm termination.** Simulate until you are sure the loop ends under every circumstance: the nominal cases, the endpoints and each exceptional case (p. 369). Make the termination condition obvious by keeping control in one place (p. 369, see [[loop-as-black-box]]).
5. **Check the counter type.** Loop counters should be integer or enumerated, not floating point. McConnell's example: adding 1.0 to 26,742,897.0 can give 26,742,897.0, and used as a loop index that gives an infinite loop (p. 374).

## Why

«Готовность выполнять такой вид проверки — ключевое различие» between skilled and unskilled programmers (p. 374). In McConnell's account, the unskilled one, when a loop misbehaves, «меняет знак < на <=», then adds or subtracts 1 from the index, and may stumble on a working combination or swap the original error for a subtler one (p. 374). Even when this works, the programmer does not know why. This wiki reads this as the loop-sized case of [[programming-by-coincidence]], and the adjust-by-one habit as the same shape as [[fix-the-model-not-the-offset]]. McConnell lists the benefits of the hand check: fewer errors in initial coding, faster diagnosis in debugging, and knowing rather than assuming how the code works (p. 374).

## Signs that the method was skipped

- A change history or diff on a loop that only flips `<` and `<=`, or adds `+ 1` or `- 1` to a bound or index, with no test added for the boundary.
- A loop counter of a floating-point type.
- A loop that walks a linked structure or waits on an external condition, in code that is not critical, where neither the header nor a stated invariant shows why it ends. In critical code the same loop is [[safety-counter]]'s.

A loop bound flipped or nudged by 1 until a test passes is [[check-loop-boundaries-by-hand]].

## Limits

This wiki adds that a loop with no index or bound of its own (for-each over a collection, a map or fold) has no boundary to walk; the first sign cannot apply to it, and only the termination check remains. This wiki also adds that the walk-through replaces neither a test nor proof. For any boundary it has found, it should leave a test pinning that boundary behind (see [[test-boundaries-and-realistic-use]]). Where termination cannot be argued (external data, cyclic structures), [[safety-counter]] is the book's fallback for critical code. The same three-point walk applies to range lookups over a bounds table: see [[stair-step-lookup-boundaries]]. A loop that keeps failing the walk can be rebuilt with [[inside-out-loop-construction]].

## Example

```
// sum of a[lo..hi] inclusive
// fix #88: total was short; tried <=, then hi + 1
total = 0
for k = lo; k < hi + 1; k++:
    total = total + a[k]
```

```
// walked first (k = lo), middle and last (k = hi): the range is inclusive
total = 0
for k = lo; k <= hi; k++:
    total = total + a[k]
// test: sum(a, 3, 3) == a[3]
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 16.2: termination p. 369, boundary checking and floating-point counters p. 374. The signs, the limits, the links to neighbouring pages and the example are this wiki's own.
