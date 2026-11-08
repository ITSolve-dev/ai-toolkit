---
title: Hoist code repeated in every branch
category: complexity
summary: "The same statement at the start or end of every branch of an if/else or every arm of a switch: move one copy out before or after the conditional."
tags: [rule, conditionals, duplication]
paradigm: any
sources: [fowler-refactoring, code-complete]
created: 2026-11-07
updated: 2026-11-07
---

When every branch of a conditional ends (or starts) with the same statements, those statements do not depend on the condition. Fowler's Slide Statements, under its old name Consolidate Duplicate Conditional Fragments, moves them out so that they appear once (*Refactoring*, 2nd ed., ch. 8, PDF p. 255). McConnell lists the same refactoring: a fragment repeated at the end of both the `if` and the `else` block is moved out of the `if-then-else` (*Code Complete*, section 24.3, Russian edition, p. 560).

## Rule

Slide identical statements out of the branches of a conditional, so that they turn into "a single statement outside of the conditional block" (p. 255).

## Sign in code

An `if/else` (or every arm of a `switch`) in which each branch starts or ends with the same statement on the same variables. In Fowler's example, both branches end with `allocatedResources.push(result)` (p. 255).

This wiki assigns the neighbouring cases as follows. Identical statements at the same end of every branch of one conditional are [[identical-code-in-every-branch]]; a copy-pasted branch or block that differs from another by one operand is [[dry]].

## When not to apply

- **Interference.** The statement can leave the branches only if the hoist passes the interference checks in [[slide-statements]]. A trailing statement that reads a variable which only some branches set, or that must run before something else in a branch, cannot move. The checks are the source's; applying them per branch is this wiki's.
- **One branch exits early.** This wiki adds: if a branch returns or throws before the shared statement, hoisting the statement below the conditional changes which paths run it.
- **The copies are meant to diverge.** This wiki's reading is that a forecast is not a sign: hoist, and slide the statement back in when a branch actually differs. Fowler describes sliding in as repeating the fragment in every leg (p. 256).

## Repair

Cut the identical statements from every branch and put one copy after the conditional (for trailing statements) or before it (for leading ones). Then test.

## Before and after

```
if available.isEmpty():
  result = createResource()
  allocated.add(result)
else:
  result = available.pop()
  allocated.add(result)
return result
```

```
if available.isEmpty():
  result = createResource()
else:
  result = available.pop()
allocated.add(result)
return result
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 8, Slide Statements, example "Sliding with Conditionals", PDF pp. 255-256 ([[fowler-refactoring]]). The pair follows the book's example in this wiki's pseudocode. McConnell, *Code Complete*, 2nd ed., Russian edition, section 24.3, p. 560 ([[code-complete]]): the same refactoring for the `if`/`else` case. The early-exit limit, the treatment of expected divergence and the assignment against [[dry]] are this wiki's own.
