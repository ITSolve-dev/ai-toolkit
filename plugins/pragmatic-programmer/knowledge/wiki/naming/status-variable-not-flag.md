---
title: 'Name a status variable for the state it records, not "flag"'
category: naming
summary: "A variable whose name is or contains 'flag' (flag, statusFlag, printFlag), especially when it is set or tested against bare numbers like 16 or 0x80."
tags: [rule, naming, state]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell asks that flags be treated as status variables. He says the fragment `flag` in a name tells nothing about what the flag means (*Code Complete*, Russian edition, p. 259). In his examples, `statusFlag = 0x80` cannot be understood until someone explains in a comment or in documentation what `statusFlag` and `0x80` are. The rewrite makes both the variable and its values speak: `characterType = CONTROL_CHARACTER`, and `reportType == ReportType_Annual` instead of `printFlag == 16` (pp. 259–260). His conclusion: if a piece of code is hard to understand, consider renaming its variables. «Его нужно просто читать.» (p. 260).

## Rule

- Name the variable for the state it records (`dataReady`, `recalcNeeded`, `characterType`, `reportType`). Do not include `flag`.
- Give its values meaningful names too: compare and assign against enumeration members or named constants, not against bare numbers (pp. 259–260).

## Sign in code

- An identifier that is `flag` or contains it: `flag`, `statusFlag`, `printFlag`, `computeFlag`, `isFlagSet`.
- Such a variable set to, tested against, or masked with a bare literal (`== 16`, `& 0x0F`, `= 0x80`).

This wiki assigns the neighbouring cases as follows. This page owns the *variable's name* when it contains `flag`. A boolean named for a thing or a dimension other than `flag` (`status`, `file`) is [[boolean-variable-names]]. A status held as a boolean and tested directly by functions outside its owner is [[status-variable-as-enumeration]], which also decides between a boolean and an enumeration where the status is read from outside. A bare literal that encodes a decision is [[named-constants-over-literals]], and a closed set of integer codes the status takes is [[enum-instead-of-codes-and-flags]]. Where these appear on one line, each page fires for its own part.

## When not to apply

- Where "flag" is the domain's own word for the thing (a country's flag, a feature flag in a feature-flag system, a CPU flag register in an emulator), the name is a problem name. This wiki's own limit.
- A boolean already named for its state (`dataReady`) needs nothing further.

## Repair

1. Find what states the variable distinguishes, by reading where it is set.
2. Two states, used inside one owner: rename it as a boolean for the true state ([[boolean-variable-names]]). More than two, or read from outside its owner: make it an enumeration named for the dimension (`reportType`), with one member per state ([[status-variable-as-enumeration]]).
3. Replace each literal it is set to or compared with by the corresponding member or constant.

## Before and after

```
if printFlag == 16
    printAnnual()
printFlag = 16
```

```
enum ReportType { Daily, Monthly, Quarterly, Annual, All }

if reportType == ReportType.Annual
    printAnnual()
reportType = ReportType.Annual
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.2, pp. 258–260 ([[code-complete]]): the rule against `flag`, meaningful values through enumerations and constants, and the advice to rename when code is hard to understand. The assignment against the neighbouring pages, the two-states condition in repair step 2 and the limit for domain uses of "flag" are this wiki's own. The pseudocode is this wiki's own, after the book's `ReportType` example.
