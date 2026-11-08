---
title: Test boundaries and realistic use
category: testing
summary: "Every test of an operation with a direction, order or sign in its arguments uses the same direction, order or sign, so real usage along that axis never runs."
tags: [rule, testing, boundary-conditions]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A test passes only for what it runs. A single synthetic case leaves untested exactly the variations users will produce.

## Rule

The book draws this from a debugging story. Testers reported that a graphics application crashed on every stroke with a particular brush, while the responsible programmer insisted nothing was wrong, because his own stroke worked (p. 127). The dispute ran for days until they sat in one room: the tester stroked from top right to bottom left and the application crashed, while the programmer had only ever stroked from bottom left to top right (p. 127). The lesson the book states is that artificial tests such as that single stroke are not enough, and that both boundary conditions and realistic patterns of use must be tested ruthlessly and systematically: «граничные условия, так и реалистичные образцы его употребления конечным пользователем» (p. 127).

## Sign in code

- A test covers an operation with a direction, order or sign in its arguments, and every case uses the same direction, order or sign.

This wiki assigns the three neighbouring shapes by where the missing case comes from. This page owns an axis that no declared limit names. A limit the code declares belongs to [[test-the-contract]]. A divisor, index or length derived from the arguments belongs to [[test-state-coverage-not-line-coverage]].

## When not to apply

The limits are this wiki's own.

- The operation normalises its arguments on entry, for example by ordering the two ends of a stroke, and that step has its own test. Every direction then reaches the same code, so one case is enough.
- Values beyond a range fixed by a type cannot be constructed, so out-of-range cases are dropped. The ends of the range are still required.
- The cost of a realistic scenario is high enough that it belongs at a higher test level. The rule then requires it somewhere in the suite and not in this test.

## Repair

1. List the axes of the input: direction, order, sign, size, emptiness.
2. Add the extremes of each axis.
3. When a defect report shows a real user action, copy that action exactly into a test, per [[failing-test-before-the-fix]].

## Before and after

```
// before: one stroke, in the only direction the author ever tried
test "brush draws":
    stroke(canvas, from = bottomLeft, to = topRight)
    assert canvas.isPainted
```

```
// after: the axis is covered, including the reported direction
for (from, to) in [(bottomLeft, topRight), (topRight, bottomLeft),
                   (topLeft, bottomRight), (bottomRight, topLeft)]:
    test "brush draws from {from} to {to}":
        stroke(canvas, from, to)
        assert canvas.isPainted
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], p. 127. The story and the rule are the book's. The sign and its assignment against the two neighbouring pages, the limits, the repair and the pseudocode are this wiki's own, and the pseudocode is derived from the story.
