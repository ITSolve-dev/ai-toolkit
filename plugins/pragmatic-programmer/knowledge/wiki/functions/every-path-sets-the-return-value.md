---
title: Make every path of a function set its return value
category: functions
summary: "A function with several branches or early exits where one path reaches the end without assigning or returning a value, relying on an implicit default or a left-over variable."
tags: [rule, return-values, control-flow, defensive-code]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell names the risk of using a function: it may return a wrong value. Usually that is because the function has several execution paths and one of them does not set the return value (*Code Complete*, p. 178).

## Rule

After writing a function, walk through each possible path in your head and confirm that the function returns a value on every one. The book recommends initialising the return value to a default at the start of the function, as insurance if a path fails to set the correct value (p. 178). The checklist asks whether the function returns a correct value in every possible case (p. 181).

## Sign in code

- A loop that returns from inside when it finds its answer, with no `return` or assignment after the loop for the case where it finds nothing.
- A function in a language that returns an implicit empty value (none, undefined, nil) where some branch falls off the end with no `return`.
- A result variable declared without an initial value and returned after conditional assignments.

This wiki assigns the neighbouring case as follows. Whether a multi-way branch over a closed set has a final `else` or `default` reserved for the unexpected, including a missing one, is [[default-branch-catches-the-unexpected]]'s. A path that leaves a function's result unset by any other route (an early exit, a loop exit, nested conditions not over one key) is [[every-path-sets-the-return-value]].

## When not to apply

- **The compiler enforces it.** Where the language rejects a non-void function with a path that returns nothing, the check is mechanical and out of this wiki's scope. The conditional-assignment shape above still applies there when the variable has a default the compiler accepts.
- **A default that hides a bug.** This wiki adds this limit, and it qualifies the book's insurance advice. If no correct value exists for an unhandled path, a silent default turns a failure into a wrong answer. Ending that path with a failure ([[crash-early]]) is better than returning the default. Use the default only when it really is the right answer for the unlisted cases.

## Repair

Give the path that falls through an explicit value or an explicit failure. Alternatively, initialise the result at the top with a value that is correct for every unlisted case. Restructure the function so that each branch ends in its own `return` where that is clearer.

## Before and after

```
routine HasOverdue(invoices)
    for each invoice in invoices
        if invoice.dueDate < today and not invoice.paid
            return true
    // nothing overdue: falls off the end, returns nothing
```

```
routine HasOverdue(invoices)
    for each invoice in invoices
        if invoice.dueDate < today and not invoice.paid
            return true
    return false
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.6, p. 178; the checklist, p. 181 ([[code-complete]]). The rule and the advice to initialise a default are the book's.
- The signs, the split with [[default-branch-catches-the-unexpected]], both limits (including the qualification of the default advice) and the pseudocode are this wiki's own.

Related: [[function-or-procedure]].
