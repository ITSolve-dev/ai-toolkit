---
title: No empty then-branch
category: complexity
summary: "An if whose then-branch is empty (`;`, `pass`, `{}`) or holds only a comment, with all the work in else: negate the test, move the else body into the if, drop the else."
tags: [rule, conditionals, if-else, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

An `if` whose own branch does nothing makes the reader invert the test in their head to learn when the real work happens. McConnell calls the form silly and gives its mechanical repair (p. 349).

## Rule

Put meaningful statements after the `if`. The book's repair is to negate the predicate, move the code from the `else` into the `if`, and delete the `else`; the unrepaired form «выглядит глупо» (p. 349).

## Sign in code

- `if (test) ; else { ... }`, `if test: pass else: ...`, or `if (test) {} else { ... }`: the then-branch is empty or holds only a comment, and all the work is in `else`.

This wiki assigns the neighbouring case as follows. An empty `else` written on purpose with a comment saying why nothing happens is the opposite shape, and [[document-the-missing-else]] recommends it. This page owns an empty *then*-branch. An empty then-branch at one level of a step-then-check chain whose polarity alternates is [[nominal-path-first]], applied first; a lone empty then-branch is [[no-empty-then-branch]].

## When not to apply

The book states no limits. The limit below is this wiki's own:

- An empty then-branch that carries a comment explaining why this case needs no action, in a chain where every case is listed on purpose, documents a decision. It is the same intent as the commented empty `else`, and this page does not fire on it.

## Repair

1. Negate the test. If the negation of a compound test is hard to read, for example one that would need De Morgan's law across several terms, name the test first ([[name-complex-conditions]]) and negate the call. This step's second half is this wiki's own.
2. Move the body of the `else` into the `if`.
3. Delete the `else`.

## Before and after

```
if someTest:
    pass
else:
    doSomething()
```

```
if not someTest:
    doSomething()
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.1, p. 349: the shape and the three-step repair. The limit, the naming step in repair step 1, the assignment against [[nominal-path-first]] and the pseudocode are this wiki's own.
