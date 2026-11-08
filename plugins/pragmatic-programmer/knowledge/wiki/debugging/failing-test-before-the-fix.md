---
title: Failing test before the fix
category: debugging
summary: "A test added with a bug fix also passes against the unfixed code, or the reproduction exists only as manual steps in a ticket. A bug-fix diff with no test at all is find-bugs-once."
tags: [rule, debugging, testing, reproduction]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A defect is fixed only when something can show that it was there and is now gone. This rule makes that evidence a test written first.

## Rule

The book's tip is «Вылавливающий ошибку тест должен предшествовать ее исправлению» (p. 128), and it calls this the most important rule of debugging (p. 127). «Чтобы приступить к устранению программной ошибки, ее нужно сделать воспроизводимой» (p. 127), since otherwise there is no way to learn whether the defect was ever removed (p. 127). A long manual sequence is not enough: the goal is to reproduce the defect «с помощью единственной команды» (p. 127), because a fix is far harder when reaching the failure takes 15 steps (p. 127). Isolating the conditions can itself reveal the fix, and writing the test suggests the solution (p. 128).

## Sign in code

- A regression test added with a fix passes against the unfixed code when the fix is reverted.
- The only reproduction is a numbered list of manual steps in a ticket or a comment.

The order of writing cannot be read from a diff, so this wiki takes a test that cannot fail on the old code as the visible trace of a test not run first.

This wiki assigns the two neighbouring shapes by whether a test exists. This page owns a test or reproduction that exists and proves nothing. A bug-fix diff with no test at all belongs to [[find-bugs-once]].

## When not to apply

The book states no limit. The following limits are this wiki's own.

- The failure depends on timing, hardware or production data that a test cannot yet hold still. Capture the evidence first, for example with [[trace-statements]], and state that no reproduction exists.
- The compiler or type checker already fails on the defect. That failing check is the reproduction.
- The change is a text correction with no behaviour, such as a typo in a user-facing message, and a test would pin only the literal string.

## Repair

1. Reduce the failure to the smallest input or action, using [[binary-search-debugging]] if needed.
2. Write a test asserting the correct behaviour.
3. Run it and confirm it fails for the reported reason, not for a setup error.
4. Fix the code and confirm the test passes.
5. Keep the test in the suite.

## Before and after

```
// before: the test never reaches the fixed line, so it passes on the old code too
// commit: "fix crash on empty order"
function total(order):
    if order.lines is empty:
        return 0
    return sum(order.lines.price)

test "order total":
    assert total(orderWithLines([line(10)])) == 10
```

```
// after: the test uses the reported input, and it fails on the old code
function total(order):
    if order.lines is empty:
        return 0
    return sum(order.lines.price)

test "an empty order totals zero":
    assert total(orderWithLines([])) == 0
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 127-128. The rule, the single command and the reasoning are the book's. The signs and their assignment against [[find-bugs-once]], the limits, the repair steps and the example are this wiki's own.
