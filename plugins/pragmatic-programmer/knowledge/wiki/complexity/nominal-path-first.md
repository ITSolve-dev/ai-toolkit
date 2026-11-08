---
title: Put the nominal path first
category: complexity
summary: "A sequence of step-then-check-status blocks whose test polarity alternates, so the normal case sits in the if at one level and in the else at the next, or a single if/else whose error branch comes first while the normal path waits in the else: put the normal case after each if and stack the error handling at the bottom."
tags: [rule, conditionals, if-else, readability, error-handling]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

When a routine checks a status after each step, the order of the `if` and `else` branches decides whether a reader can follow the normal run of the code. McConnell asks for the nominal path to be written first and the exceptional cases after it, and for the normal case to sit after the `if`, not after the `else` (pp. 346-347).

## Rule

Write the code so that the normal path of execution is obvious, and so that unusual circumstances do not obscure the main algorithm (p. 346). Within each `if`/`else`, handle the normal case in the `if` branch. The book ties this to its general principle of placing the actions that result from a decision as close as possible to the decision (p. 347).

Its verdict on the rewritten example: «Стек ошибочных условий, расположенный внизу вложения, — признак хорошо написанного кода обработки ошибок» (p. 349).

## Sign in code

- A sequence of step-then-check-status blocks in which the test polarity alternates: at one level the `if` tests for failure (`status == Error`) and the success path continues in `else`; at the next level the `if` tests for success. The book names exactly this: because errors are sometimes handled in the `if` and sometimes in the `else`, it is hard to find which branches carry the normal case (p. 348). It is often visible as a one-line success branch next to a long failure branch, then the reverse one level down.
- A single `if`/`else` whose `if` handles an error and whose `else` holds the normal path. The book's rule covers every `if`/`else` (p. 347), and its key point stresses it most where many errors are handled (p. 358).

This wiki assigns the neighbouring cases as follows. Where the polarity of the tests alternates, so that the normal case sits in the `if` at one level and in the `else` at the next, [[nominal-path-first]] owns the order of the branches; apply it first. Where every test checks success and the nominal work sits three or more levels deep, [[guard-clauses]] owns the sign. Other deep nesting is [[tame-deep-nesting]]. In a single `if`/`else` where one branch is the normal path and the other handles an error, the normal path goes first ([[nominal-path-first]]); where the branches are peers, prefer the positive test ([[prefer-positive-conditions]]). An empty then-branch at one level of a step-then-check chain whose polarity alternates is [[nominal-path-first]], applied first; a lone empty then-branch is [[no-empty-then-branch]]. The order of arms in a multi-way `if`-`else if` chain or a `case` is [[order-branches-by-frequency]].

## When not to apply

The book states no limits on this rule. The limits below are this wiki's own.

- Guard clauses. Code that checks each failure first and returns or throws at once puts the error *before* the normal path on purpose, and keeps the normal path flat and unindented. That shape does not hide the nominal path, and this page does not fire on it. The book itself lists guard clauses among the other solutions to the same problem (p. 349).
- A single `if`/`else` whose branches are peers, neither of them an error: which branch comes first matters little, and [[prefer-positive-conditions]] decides the test.
- The book also claims the order matters for performance (p. 346). This wiki does not apply that half without a measurement: branch order in a two-way `if` rarely shows in a profile.

## Repair

1. Mark each branch as normal or exceptional.
2. Invert the test wherever the normal case sits in the `else`, so every `if` tests for success and continues the main path.
3. Leave the error branches as a stack of `else` blocks at the bottom of the nesting, in reverse order of the steps.
4. If every test now checks success and the nominal work is still three or more levels deep, apply [[guard-clauses]]; other deep nesting is [[tame-deep-nesting]]. That is a second repair, not part of this rule.

## Before and after

```
open(file, status)
if status == ERROR:
    err = OPEN_FAILED
else:
    read(file, data, status)
    if status == OK:
        save(data)
        err = NONE
    else:
        err = READ_FAILED
```

```
open(file, status)
if status == OK:
    read(file, data, status)
    if status == OK:
        save(data)
        err = NONE
    else:
        err = READ_FAILED
else:
    err = OPEN_FAILED
```

The "after" is two levels deep, below the three levels at which [[guard-clauses]] fires. The book's own example has four steps; once every test checks success there, the nominal work sits three or more levels deep and [[guard-clauses]] applies next.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.1, pp. 346-349: the rule, the example and its rewrite, and the list of alternative solutions; key points, p. 358. The guard-clause limit, the single-if sign and its resolution against [[prefer-positive-conditions]], the peer-branch limit, the caution on the performance claim and the assignment against the neighbouring pages are this wiki's own. The pseudocode is this wiki's own, modelled on the book's example.
