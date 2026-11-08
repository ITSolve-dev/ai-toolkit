---
title: Assertion conditions have no side effects
category: errors
summary: "The condition inside an assert advances an iterator, pops, increments, assigns or writes, so the check changes what the program does."
tags: [rule, assertions, side-effects]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Code added to detect errors must not create new ones, and an assertion does exactly that when testing its condition has an effect (p. 153).

## Rule

The condition of an assertion only observes. Perform the effect first, then assert on the result (p. 153).

The book's example calls the iterator's next-element operation inside the assertion, so the loop skips an element on each pass and handles only half the collection (p. 153). It calls this a form of Heisenbug: a bug that changes the behaviour of the system being debugged (p. 154). Since assertions can be disabled in some environments (p. 145), this wiki adds that the program can also behave differently depending on the setting.

*Code Complete* states that risk directly: «Старайтесь не помещать выполняемый код в утверждения» (p. 186). If an assertion contains code, the compiler may remove that code when assertions are switched off: not compiling the assertion means not compiling the action either (pp. 186-187). Its example is an assertion whose whole condition is the call that performs the work, `assert(PerformAction())`, and its repair is the one below (p. 187).

## Sign in code

- An `assert` condition calls something that consumes or advances: next, pop, read, dequeue.
- It contains an assignment, an increment or a write.
- The whole condition is a call that performs the routine's work, as in `assert(perform_action())`.
- Removing the assertion line would change what the following lines see.

This wiki assigns the neighbouring cases as follows. A side effect inside an assertion's condition is this page's; side effects inside an ordinary expression are [[one-side-effect-per-statement]].

## When not to apply

The book gives no exception. This wiki allows a call whose effect is invisible to program logic, such as filling a cache behind a read. The fourth sign is the test: if removing the line changes nothing that follows, the rule is not broken.

## Repair

Move the effectful call to its own statement, store the result in a local, and assert on the local (the repair both books give: pp. 153 and 187).

## Before and after

```
# before
while stack is not empty:
    assert stack.pop().is_valid()
    frame = stack.pop()
    handle(frame)
```

```
# after
while stack is not empty:
    frame = stack.pop()
    assert frame.is_valid()
    handle(frame)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 145, 153-154 for the rule and the failure. McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: pp. 186-187 for the rule, the compiled-out reason, the perform-action shape and the repair. The signs other than the perform-action one, the split with [[one-side-effect-per-statement]], the limit, the point about differing settings and the example are this wiki's own.
