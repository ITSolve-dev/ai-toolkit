---
title: Consider the else, and say why it is absent
category: documentation
summary: "An if with no else whose false case is a real input and not obviously a no-op (input validation, range or status checks), with nothing near it saying what happens then: add an else that handles it, or a comment saying the false case is deliberately ignored."
tags: [rule, conditionals, if-else, comments, completeness]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A plain `if` silently decides that nothing should happen when its test is false. McConnell asks the writer to check that decision, because it is often wrong, and to leave a trace when it is right (pp. 349-350).

## Rule

When you think you need a plain `if`, consider whether you need an `if`-`then`-`else`. The book cites a classic General Motors analysis (Elshoff, 1976) that found an `else` should have been used in 50-80% of `if` statements (p. 349). One reason to add an `else`, even an empty one, is to show that the `else` case was considered. Coding empty `else` blocks just for that may be overdoing it, but for an `if` without an `else`, other than in obvious cases, write a comment explaining why the `else` is absent (p. 350).

The book's example keeps an `else` that holds only a comment: the color is invalid, and the command is deliberately ignored with no output (p. 350).

The checklist adds: test the `else` branch too, not only the main branch, and check that the `if` and `else` bodies are not swapped, an inversion the book calls a common error (pp. 350, 357).

## Sign in code

- An `if` with no `else` whose test is a validation, a range check or a status check, so that the false case is a real input the code will meet, and nothing near it says what happens then.
- Tests that exercise only the true side of such an `if`.

This wiki assigns the neighbouring case as follows. This page owns a single `if` without an `else`. The final `else` of an `if`-`else if` chain over a closed set, and the `default` of a `case`, are [[default-branch-catches-the-unexpected]].

## When not to apply

- The book exempts obvious cases (p. 350) without defining them. This wiki reads "obvious" as: the false case is the natural no-op of the statement, such as `if (logEnabled) log(...)`, or a guard clause that returns, where nothing follows the `if` that could run in the wrong state. A test that validates input or checks a range or status is never the natural no-op: its false case is a real input.
- The book itself warns that empty `else` blocks written only to show the case was considered may be overdoing it (p. 350). This wiki prefers a comment, the lighter form, to an empty block where the language or the team's linter flags empty blocks.

## Repair

1. Ask what must happen when the test is false.
2. If something must happen, write it in an `else` (an error, a default value, a report).
3. If nothing must happen and it is not obvious, add an `else` holding a comment, or a comment on the `if`, that states the false case is deliberately ignored and why.
4. Add a test that drives the false side.

## Before and after

```
if COLOR_MIN <= color and color <= COLOR_MAX:
    paint(color)
```

```
if COLOR_MIN <= color and color <= COLOR_MAX:
    paint(color)
else:
    # invalid color: the command is ignored on purpose, no output
    pass
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 15.1, pp. 349-350, and the checklist, p. 357. The Elshoff (1976) figure is the book's citation, not checked here. The reading of "obvious cases" and its exclusion of validation tests, the sign on tests that drive only the true side, the preference for a comment over an empty block under a linter, the assignment against [[default-branch-catches-the-unexpected]] and the pseudocode are this wiki's own.
