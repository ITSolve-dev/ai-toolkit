---
title: Use a function only when returning its named value is the point
category: functions
summary: "A call to a mutating routine and the test of its returned status are fused in one condition (if report.FormatOutput(r) == Success) in a project that reports failure through return values: split the call from the test."
tags: [decision-rule, functions, procedures, status-codes, command-query-separation]
paradigm: any
sources: [code-complete, elegant-objects]
created: 2026-11-06
updated: 2026-11-06
---

McConnell separates the two kinds of routine by meaning, not by syntax. A function returns a value and a procedure does not. A C++ routine returning `void` is semantically a procedure, whatever the language calls it, and the semantics deserve the attention (*Code Complete*, p. 177).

## Rule

The book's conclusion: «используйте функцию, если основная цель метода — возврат значения, указанного в имени функции» (p. 178). Otherwise use a procedure. The chapter's key points repeat it (p. 181).

On the common case of a procedure that returns a status code, the book takes a middle position (pp. 177-178):

- Purists would have every function take only inputs and return one value named by the function (`sin()`, `CustomerID()`, `ScreenHeight()`).
- `if (report.FormatOutput(formattedReport) = Success)` is logically a procedure that technically returns a value. Defended on the grounds that the value relates neither to its purpose nor to its name, it causes no confusion *if* status is returned consistently.
- The author's own preference is to keep the call and the check of the status apart, either through a status out-parameter or as `outputStatus = report.FormatOutput(formattedReport)` followed by a separate `if`. His reason is density, not purism: «Объединение вызова и проверки в одной строке увеличивает «плотность» команды, а значит, и ее сложность.» (p. 177).

### Where this meets *Elegant Objects*

[[command-query-separation]], from *Elegant Objects*, forbids any method that manipulates and also returns something. McConnell allows a procedure to return its success or failure. This wiki resolves the conflict by setting, and the resolution is its own:

- **The project reports failure through return values** (no exceptions, or a project-wide result or status convention). A success/failure status returned from a procedure is then the error channel, applied consistently, and McConnell's form holds. The call and the test go on separate lines.
- **The project reports failure through exceptions.** A returned status alongside a mutation duplicates the error channel, and [[command-query-separation]] holds.
- **Any other returned value from a mutating routine** (a count, the previous value, a changed flag) is owned by [[command-query-separation]] in both settings.

The condition that selects the page, in the words both pages use: whether the value a mutating routine returns is a success/failure status in a project that reports failure through return values.

## Sign in code

- In a project that reports failure through return values, a call to a mutating routine placed inside an `if` or `while` condition, so the action and the test of its returned status are one expression.

A mutating routine returning any value other than a success/failure status (a count, the previous value, a changed flag) is [[command-query-separation]]'s, not this page's.

## When not to apply

- **Idioms built on the fused form.** This wiki adds this limit. Where a language's idiom fuses the call and the test (a read-loop condition, pattern matching on a returned result type), that idiom is the project's convention and overrides the density argument.
- **A pure function** returning its named value is exactly what the rule asks for. Nothing on this page applies to it.

## Repair

- Separate the call from the test: assign the status to a named variable, then test the variable.
- If the return value is neither the routine's named result nor a status, apply [[command-query-separation]]: return nothing, or split off a query.
- If the value is the routine's real purpose, rename the routine for that value ([[routine-names]]).

## Before and after

```
if report.FormatOutput(formatted) == SUCCESS
    Print(formatted)
```

```
status = report.FormatOutput(formatted)
if status == SUCCESS
    Print(formatted)
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.6, pp. 177-178, and the key points on p. 181 ([[code-complete]]). The function/procedure criterion, the acceptance of a consistently used status return and the density argument are the book's.
- The resolution against [[command-query-separation]] ([[elegant-objects]]), the signs, the limits and the pseudocode are this wiki's own.

Related: [[every-path-sets-the-return-value]].
