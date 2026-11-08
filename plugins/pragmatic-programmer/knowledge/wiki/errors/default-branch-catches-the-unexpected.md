---
title: The default branch catches the unexpected
category: errors
summary: "A multi-way branch over a closed set with no final else or no default, so an unplanned value falls through silently; or a switch/chain whose default or last else does the work of one nameable value (the last enum member, the last command letter): list every expected case and make default/else report an internal error."
tags: [rule, conditionals, switch, default, defensive-programming, error-detection]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The last `else` of a chain and the `default` of a `case` are where values nobody planned for end up. McConnell makes them the place that reports such values, and advises against using them to handle the last ordinary case (pp. 352, 355-356). The chapter's key points repeat it: use the `default` of a `case` or the last `else` of an `if`-`then`-`else` chain to catch errors (p. 358).

## Rule

- Make sure all cases are covered: put an error message or an assertion in the final `else` to catch cases you did not plan for. The message is for you more than for the user, so word it accordingly (p. 352).
- Use the `default` clause only for a real default. Coding the last remaining case as the default loses the self-documentation that `case` labels give and loses the ability to detect errors with the default (p. 355).
- Use the `default` clause to detect errors when it is not needed for anything else (p. 355). If it serves some other purpose, every possible input is implicitly valid: double-check that, and if any input turns out invalid, rewrite the statement so that the default checks for errors (p. 356).

The book's reasoning for the user side: most users prefer «Внутренняя ошибка: Пожалуйста, позвоните в службу поддержки» to a crash or, worse, to slightly wrong results that look fine until someone checks them (p. 356).

It also gives the change-cost reason against a fake default: with a real default, adding a case is just a new label; with an artificial one, you must add the new case, maybe make it the new default, and turn the old default into an ordinary label (p. 355).

## Sign in code

- An `if`-`else if` chain over a closed set of categories that ends in `else if` with no final `else`, or a `switch` over such a set with no `default`, so a value outside every category falls through silently.
- A `switch` whose `default`, or a chain whose last `else`, does the work of one specific, nameable value (the last enum member, the last command letter) instead of having its own label or test.
- A case that needs no action handled by omission rather than by its own label: the book's example lists such a case explicitly with a comment that no action is required (p. 355).

This wiki assigns the neighbouring cases as follows. This page owns whether a multi-way branch over a closed set has a final `else` or `default` reserved for the unexpected, including a missing one; [[assert-the-impossible]] sends that shape here. How the reserved branch reacts is owned elsewhere: a `default` whose body is a comment or a log line, quiet in every build, is [[offensive-programming]]; an empty one is [[assert-the-impossible]]; and an impossible branch that logs and carries on where the module's production reaction must also be a stop is [[crash-early]]. A single `if` without an `else` is [[document-the-missing-else]]. A path that leaves a function's result unset by any other route (an early exit, a loop exit, nested conditions not over one key) is [[every-path-sets-the-return-value]]. A `switch` on a state machine's state variable with no `default` is [[default-branch-catches-the-unexpected]]; a state whose guards leave some input with no transition is [[transition-conditions-consistent-and-complete]].

## When not to apply

The book gives one condition: a `default` that handles a real default, where every input is valid, is correct (p. 356). This wiki's own limits:

- Where the language or the compiler checks exhaustiveness over a closed type (an enum or a sum type matched exhaustively), a catch-all `default` can turn that check off: adding a new member no longer fails to compile. There, list every member and leave out the catch-all, so the compiler is the error detector the book wants the default to be.
- Open sets with a meaningful fallback (an unknown HTTP header ignored by design, an unknown field skipped by a tolerant reader) have a real default. Say so in a comment.
- Where the unexpected value comes from outside the program, reporting it as an internal error is wrong: it is an input error, and [[distrust-external-input]] owns how to answer it.

## Repair

1. Give every expected value its own label or `else if`, including values that need no action (with a comment).
2. Make the final `else` / `default` report an internal error or fail an assertion; see [[assert-the-impossible]].
3. If a fallback is genuinely meant, keep it as `default` and state in a comment that every other value is valid here.

## Before and after

```
# c comes from this module's own buffer, already decoded
if isLetter(c):        type = LETTER
else if isPunct(c):    type = PUNCTUATION
else if isDigit(c):    type = DIGIT
else:                  type = CONTROL
```

```
# c comes from this module's own buffer, already decoded
if isLetter(c):        type = LETTER
else if isPunct(c):    type = PUNCTUATION
else if isDigit(c):    type = DIGIT
else if isControl(c):  type = CONTROL
else:                  internalError("unexpected character type")
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.1, p. 352 (final `else`); section 15.2, pp. 355-356 (real defaults, the default for error detection); key points, p. 358. The exhaustiveness-check limit, the open-set limit, the hand-off to external input handling and the assignment against the neighbouring pages are this wiki's own. The pseudocode is this wiki's own, modelled on the book's character classification.
