---
title: Do not live with broken windows
category: change
summary: "A defect the code itself admits (FIXME, HACK, error dropped 'for now') stays in the region under review, neither fixed nor boarded up, or new code builds on it."
tags: [rule, entropy, technical-debt, stub, fixme]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A **broken window** is a bad design, a wrong decision or a piece of poor code left unrepaired where others can see it. The book holds that one such defect is enough to start a project's decay, see [[software-entropy]]. The rule is about what is already there; for what a change adds, see [[first-do-no-harm]].

## Rule

«Нельзя жить с разбитыми окнами» (p. 35). A found defect is not left as it stands: «Исправляйте их, как только обнаружите.» (p. 35). If there is no time for the fix, the window is boarded up: «закомментируйте неисправный код, выведите сообщение "Не реализовано" или же подставьте вместо него фиктивные данные» (p. 35). The point of the board, in the book's terms, is to stop further damage and to show that the situation is under control (p. 35).

## Sign in code

The book defines a window only as bad code, which could be said of nearly any code. This wiki therefore narrows the sign to what a reader can point at in the region under review:

- a comment admits a defect (`FIXME`, `HACK`, `temporary`, `wrong for ...`) and the admitted path still runs;
- an error is caught and dropped next to a note that this is for now;
- new code in the diff calls or copies one of the above instead of stopping at it;
- another page of this wiki reports a defect on a line the change touches, and the change leaves it with neither a fix nor a board.

This page has no sign of its own for a defect nobody admitted. Finding one is the work of the other groups; this rule decides only what must happen once it is found.

This wiki assigns the neighbouring cases as follows. A test that is switched off is [[all-tests-pass-always]], and a test left with no assertion is [[test-that-verifies-nothing]]. Each owns its sign and its repair, because a board of the kind below would turn a recorded skip into a failing build. A marker admitting a defect on a path that runs is [[broken-windows]]; [[marker-comments]] owns the choice of marker notation and a marker beside a stub that has not been written. A comment admitting a defect (`HACK`, `FIXME`) is [[broken-windows]]. A dropped error with no note beside it is [[crash-early]].

## When not to apply

The book states no limit. Everything below is this wiki's own.

- The same change deletes the code. Fixing it first is wasted work.
- The fix would change behaviour with nothing pinning it. Pin the behaviour first, see [[refactoring]]. A board is no way round this: it turns a wrong result into a failure, which also changes behaviour, so it suits a path nothing depends on yet.
- The complaint names no defect and is only that the code could be nicer. That is the other side of [[good-enough-versus-broken-window]].
- A board that can pass as real output is not a board. Dummy data that looks plausible hides the window, so the book's third option applies only where the data is visibly fake.

## Repair

1. Fix the defect if the fix fits the change at hand.
2. Otherwise board it up. This wiki prefers an explicit failure on the admitted path over commenting the code out, because commented-out code removes behaviour silently, while a failure says what is missing each time it is reached.
3. Stop new code at the board. Nothing new may depend on the broken path.

Where the defect is structural and sits beside a change on other lines, [[refactor-early-and-often]] rules on when to act.

The cost is real: a fix or board enlarges a change that was about something else. This wiki reads the book as accepting this cost, because it ranks neglect as the fastest cause of rot.

## Before and after

```
// before: the comment admits the defect and new code builds on it
function tax(amount):
    // FIXME wrong for negative amounts (refunds)
    return amount * 0.2

function refund(order):
    return -order.total + tax(-order.total)
```

```
// after: no time to fix refunds, so the path is boarded up and fails visibly
function tax(amount):
    if amount < 0:
        fail("tax on refunds: not implemented")
    return amount * 0.2

// refund stays out of this change until tax handles refunds
```

## Source

[[pragmatic-programmer]], Topic 3, pp. 34-36. The rule, the definition of a window and the three ways of boarding one up are the book's. The list of signs, the narrowing to the region under review, the assignment of neighbouring cases, every limit, the preference for a visible failure over commented-out code, the condition on dummy data, the third repair step, the reading of the cost and the pseudocode are this wiki's own.
