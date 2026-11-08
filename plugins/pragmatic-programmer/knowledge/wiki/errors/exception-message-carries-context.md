---
title: An exception carries the data that caused it
category: errors
summary: "A throw passes a fixed message (\"index out of range\", \"invalid value\") without the offending value and the bounds or state it was checked against, so whoever reads the report cannot tell why it fired."
tags: [rule, exceptions, diagnostics]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The code that throws knows the circumstances it detected; the person reading the exception later does not (p. 195).

## Rule

«Вносите в описание исключения всю информацию о его причинах» (p. 195). Make sure the message contains enough to understand why the exception was thrown; if the cause was a bad array index, include the array's upper and lower bounds and the illegal index value (p. 195). The chapter's checklist asks the same: does each exception contain all its relevant source data (p. 206).

## Sign in code

- A throw that carries no values (neither in its message nor as fields), at a point where the failing value and the limit it broke are local variables.
- A family of throws in one module with identical messages for different checks.

This wiki assigns the neighbouring case as follows. A rethrow that loses the cause is [[chain-exceptions]]; this page owns what the first throw records. An assertion whose failure reports nothing useful is [[leave-assertions-on]].

## When not to apply

- Values that must not be disclosed: secrets, personal data, or anything the audience of the message may not see. The book's security checklist asks that error messages not help an attacker (p. 207); see [[do-not-disclose-in-output]]. This wiki adds: include an identifier or a redacted form instead.
- A sentinel exception whose type alone says everything, such as cancellation.

## Repair

Put the offending value, the limits or state it was checked against, and the identity of the object involved into the exception, as fields where the language allows, so a central reporter can format them ([[consistent-error-handling-strategy]]).

## Before and after

```
# before
function item_at(items, index):
    if index < 0 or index >= items.length:
        throw IndexError("index out of range")
    return items[index]
```

```
# after
function item_at(items, index):
    if index < 0 or index >= items.length:
        throw IndexError("index out of range",
                         index = index, lower = 0, upper = items.length - 1)
    return items[index]
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 195 for the rule and the array example, p. 206 for the checklist item, p. 207 for the security question. The signs, the split with [[chain-exceptions]], the limits, the repair and the example are this wiki's own.
