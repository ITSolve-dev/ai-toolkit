---
title: Rename extracted code for its new role
category: naming
summary: "A freshly extracted function still carries the caller's names for its locals and parameters (thisAmount, perf), a function name too general for what it does (format for a function used only to format US-dollar amounts), or a placeholder left from a name collision (appleSauce)."
tags: [rule, naming, refactoring, extract-function]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Most of Fowler's renames in the first chapter follow an extraction. The reason is in his remark that "Breaking a large function into smaller ones only adds value if the names are good." With good names he does not have to read a function's body to see what it does (ch. 1, PDF p. 24). Names are hard to get right first time, so he uses the best name he has and does not hesitate to rename later; often it takes a second pass to see the best name (PDF p. 24). He judges renaming worth the work because variable names are a key to clear code (PDF p. 15).

This wiki assigns the neighbouring cases as follows. Names an extraction carried over from the caller are [[rename-extracted-code-for-clarity]]; a name that a later change made untrue is [[rename-when-meaning-drifts]]. `result` as the returned value of a short function that computes one value names a role and is [[rename-extracted-code-for-clarity]]'s convention; `result`-style names on one of several intermediates in a longer routine are [[temporary-variable-names]].

## Rule

Right after an extraction, rename the new function's locals and parameters for their role inside it, and give the function a name that says what it does at the level its callers need.

## Sign in code

- A function whose parameter or local names describe the caller's context (a loop variable `perf`, `thisAmount`) rather than their role inside the function (PDF pp. 14-15); most visible in a diff that has just extracted it.
- A function name too general for what it does: `format`, used only to format US-dollar amounts, renamed `usd` (PDF pp. 23-24).
- A placeholder name left from a name collision (`appleSauce`) after the collision is gone (PDF pp. 28-29).

## When not to apply

- Fowler's two conventions are his own coding standard, not a requirement: the return value of a function is always `result`, and a parameter is named after its type with an indefinite article (`aPerformance`) unless a role is worth naming (PDF pp. 14-15). He ties the second to dynamically typed languages. This wiki treats both as project conventions that the project's own style overrides.
- Fowler on the length of a name: `formatAsUSD` was too long-winded for its use inside a string template and a small scope (PDF p. 23). This wiki reads that as length following scope ([[name-length-matches-scope]]).
- This wiki's limit: the extraction is an intermediate step in a sequence whose next step renames anyway (the placeholder during [[remove-loop-accumulator]]); the sign holds only once the sequence is finished.

## Repair

Rename one name at a time, each followed by compile and test (PDF p. 22). Where the right function name is still taken by a variable, extract under a placeholder, remove the variable, then rename.

## Before and after

```
// before: extracted, names unchanged
function amountFor(perf, play):
    thisAmount = 0
    ...
    return thisAmount

format = currencyFormatter("USD")
text += format(amount / 100)
```

```
// after
function amountFor(performance, play):
    result = 0
    ...
    return result

function usd(cents): return currencyFormatter("USD")(cents / 100)
text += usd(amount)
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, PDF pp. 14-15, 22-24, 28-29. The reasoning, the example renames and the two naming conventions are the book's. This wiki's own: treating the conventions as overridable by the project, the selecting sentences against [[temporary-variable-names]] and [[rename-when-meaning-drifts]], the intermediate-step limit, and the pseudocode.
