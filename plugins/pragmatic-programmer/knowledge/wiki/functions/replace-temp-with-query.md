---
title: Replace a temp with a query before extracting
category: functions
summary: "Inside a long function about to be split, a local assigned once from a lookup or expression on values every fragment already has (play = plays[perf.playID]) and read in the fragments to be extracted, so each extraction carries it as an extra parameter beside the value it derives from (amountFor(perf, play)); or the same derivation computed into locals in several methods of one class."
tags: [rule, refactoring, temporary-variables, extract-function, local-variables]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler removes temporary variables from a long function before he breaks it up. His reason is mechanical: "temporary variables create a lot of locally scoped names that complicate extractions" (ch. 1, PDF p. 16). More broadly, temps are only useful within their own routine, "and therefore they encourage long, complex routines" (PDF p. 23). The refactoring is Replace Temp with Query (178).

This wiki assigns the neighbouring case as follows. A local assigned once from a lookup or expression on values every fragment already has, inside a function about to be split, is [[replace-temp-with-query]]; a variable naming the participant of a dereference chain in a function that stays whole is [[explaining-variable]]. A single expression that combines several sub-calculations, none written twice, is [[extract-variable]]. A local that blocks the split of a long function, or a derivation repeated in locals of several methods, is [[replace-temp-with-query]]. Where extracting a fragment would need most of the routine's locals as parameters or results, the temps are removed first ([[replace-temp-with-query]]); where they still tangle, [[function-or-command-object]] owns the choice of a command object; where the routine is to stay whole, the intent comment is split into finer steps ([[extract-routine-to-name-a-step]]).

## Rule

When a local in a long function is computed from something else in scope and assigned once, replace it with a function that computes it, call that function where the temp was used, and drop it as a parameter from functions already extracted.

The catalogue entry (ch. 7, "Replace Temp with Query", PDF pp. 204-208) weighs the temp against the function. A temp names a value and avoids recomputing it, "But while using a variable is handy, it can often be worthwhile to go a step further and use a function instead" (PDF p. 205). Fowler's reasons: an extracted piece no longer needs the value passed in; the function forms "a stronger boundary" that "helps me spot and avoid awkward dependencies and side effects"; and one function replaces the same calculation repeated in several places (PDF p. 205). The chapter introduction adds that temps "often get in the way of refactoring", because they must be computed in the right order and be available where needed (PDF p. 183).

## Sign in code

- A local assigned once from an expression on another local or parameter (`play = plays[perf.playID]`), not reassigned, read further down in fragments that are candidates for extraction.
- An extracted function taking both a value and something derived from it as parameters (`amountFor(perf, play)` where `play` is a lookup on `perf`) (PDF p. 16).
- Two or more methods of one class compute the same expression into their own locals (PDF p. 205).
- A local holding a function value, assigned once and used as a function (`format = <number formatter>.format`); Fowler prefers a declared function (PDF p. 23).

## When not to apply

- The temp is reassigned, or it accumulates across a loop: use [[remove-loop-accumulator]] instead.
- **Snapshots.** The calculation must give the same result whenever it is used, "which rules out variables used as snapshots with names like oldAddress" (ch. 7, PDF p. 205). This wiki extends it: the expression reads state that changes between the assignment and a later use, so recomputing it gives a different value.
- **Side effects.** The query must have none (PDF p. 206); a calculation that also changes state is separated first ([[command-query-separation]]).
- **Several assignments.** A temp assigned in more than one place can become a query only if all its assignments are extracted together into it (PDF pp. 205, 208).
- **Outside a class.** The refactoring "works best if I’m inside a class": a top-level function may end up with too many parameters, which cancels much of the gain, and nested functions avoid that but cannot be shared between related functions (PDF p. 205).
- This wiki's limit: the function is short and not about to be split, and the temp names a role the expression does not say; [[explaining-variable]] owns that case.
- This wiki's limit: the expression is expensive in kind (a file, network or database read). Fowler's lookup is a cheap map access; for an expensive one the cost is decided on [[fix-performance-at-the-right-level]], outside [[refactor-first-tune-afterwards]]'s limits.

## Repair

Fowler's sequence for `play` (PDF pp. 16-19), each step followed by compile-test-commit:

First check that the variable is fully determined before its first use and yields the same value every time; make it read-only if the language allows, and test, which catches a missed reassignment (ch. 7, PDF pp. 205-206).

1. Extract the right-hand side of the assignment into a function (`playFor(aPerformance)`); if several assignments compute it, extract all of them (PDF p. 208).
2. Inline the variable: replace each read of `play` with `playFor(perf)`.
3. Change the declaration of functions that took the temp as a parameter: first use the query inside them, then delete the parameter.
4. If a caller now stores the function's result in a temp read once, inline that temp too (PDF p. 19).

Fowler notes the lookup now runs three times per iteration instead of once, judges the effect unlikely to matter, and adds that well-factored code is easier to tune (PDF p. 19).

## Before and after

```
// before
function statement(invoice):
    for perf in invoice.performances:
        play = plays[perf.playID]
        amount = amountFor(perf, play)
        if play.type == "comedy": credits += floor(perf.audience / 5)
        text += play.name + ": " + amount
```

```
// after
function playFor(perf): return plays[perf.playID]
function amountFor(perf): ... switch playFor(perf).type ...

function statement(invoice):
    for perf in invoice.performances:
        if playFor(perf).type == "comedy": credits += floor(perf.audience / 5)
        text += playFor(perf).name + ": " + amountFor(perf)
```

The "after" still accumulates `credits` in the loop; that is the next step, [[remove-loop-accumulator]], not a sign of this page.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Removing the play Variable" and "Removing the format Variable", PDF pp. 16-19, 23; the catalogue entry is Replace Temp with Query (178). The reasoning, the signs from the example and the repair sequence are the book's. Ch. 7, "Replace Temp with Query", PDF pp. 204-208, and the chapter introduction, p. 183: the variable-versus-function weighing, the boundary and duplication reasons, the snapshot, side-effect, several-assignment and outside-a-class limits, the read-only check and the duplicated-derivation sign. This wiki's own: the selection against [[explaining-variable]] and [[extract-variable]], the extension of the snapshot limit to state changed in between, the short-function and expensive-expression limits, and the pseudocode.
