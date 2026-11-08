---
title: Name a routine for everything it does
category: naming
summary: "A routine name built on a vague verb (Handle, Process, Perform, DealWith, Do), told apart from its siblings only by a number (OutputUser1, Part2), omitting an output or side effect the body has, or repeating the receiver in an object method (document.PrintDocument)."
tags: [rule, routine-names, side-effects, naming-conventions]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

In McConnell's account, a routine's name is a diagnostic of its design as well as a label. The chapter's key points say a bad but accurate name often points to a badly designed routine, and a bad, inaccurate name fails to describe it. Either way the program should change: «Плохое, но точное имя часто указывает на плохое проектирование метода.» (*Code Complete*, p. 181).

## Rule

The book's advice on routine names (pp. 167-169):

- **Describe everything the routine does,** including all outputs and side effects. A routine that computes report totals and opens an output file is not `ComputeReportTotals()`. `ComputeReportTotalsAndOpenOutputFile()` is adequate but clumsy. The cure for a clumsy name is not a vaguer one: «Выход из этого положения — не использование менее описательных имен» (p. 167). The cure is routines without side effects.
- **Avoid vague, ambiguous verbs.** `HandleCalculation()`, `PerformServices()`, `OutputUser()`, `ProcessInput()` and `DealWithOutput()` say almost nothing. Sometimes the name is the only defect, and `HandleOutput()` becomes `FormatAndPrintOutput()`. Sometimes the vagueness reflects the routine: «Неясная цель — невыразительное имя.» (p. 167). Then the book's repair is to restructure the routine and its relatives so that each has a clear purpose.
- **Do not tell routines apart only by numbers.** `OutputUser`, `OutputUser1` and `OutputUser2` say nothing about how their abstractions differ (p. 167).
- **No artificial length limit.** The book cites research putting the best variable-name length at 9-15 characters on average. Routine names are usually longer, though an object's name supplies part of the name for free. The name may be as long as clarity requires (p. 167).
- **A function is named for what it returns:** `cos()`, `customerId.Next()`, `printer.IsReady()`, `pen.CurrentColor()` (p. 168).
- **A procedure is named verb + object:** `PrintDocument()`, `CalcMonthlyRevenues()`, `CheckOrderInfo()`. In an object-oriented language the object is the receiver, so it drops out of the name: `document.Print()`. The redundant `document.PrintDocument()` can also become wrong in a subclass. If `Check` derives from `Document`, `check.Print()` plainly prints a cheque, while `check.PrintDocument()` suggests a chequebook entry or a statement (p. 168).
- **Use antonyms precisely.** Pairs such as add/remove, open/close, begin/end, create/destroy, lock/unlock and first/last keep names consistent. An asymmetric pair like `FileOpen()` and `_lclose()` confuses the reader (p. 168).
- **Set naming conventions for common operations.** In one of the author's projects, getting an object's id was spelled `employee.id.Get()`, `dependent.GetId()`, `supervisor()` and `candidate.id()`. By mid-project no one could remember which applied where, and too much code had been written to go back (pp. 168-169).

Fowler's **Mysterious Name** smell (*Refactoring*, 2nd ed., ch. 3, PDF p. 86) puts naming first among the smells, for functions, modules, variables and classes alike: names should say what an element does and how to use it, so that the code reads as mundane and clear. He gives the same diagnostic reading as McConnell: "When you can’t think of a good name for something, it’s often a sign of a deeper design malaise", and puzzling over a tricky name has often led the authors to significant simplifications (PDF p. 86). He adds that people are afraid to rename, thinking it not worth the trouble, though a good name can save hours of puzzled incomprehension later (PDF p. 86). The renames are Change Function Declaration, Rename Variable and Rename Field. This wiki reads his remark as a repair rule: where no honest, specific name fits, the finding is about the element and not only its name, so the element is restructured before it is named.

## Sign in code

- A routine name whose verb is one of handle, process, perform, deal with, do, manage or output, with no more specific word naming the result.
- Sibling routines distinguished only by a trailing digit or by `Part`/`Step` numbering.
- A routine named for an action (a procedure name such as `PrintReport`) whose body also performs a second action or returns a second result through an out-parameter, while its name mentions only the first.
- An object method whose name repeats its class's noun (`order.ValidateOrder()`, `document.PrintDocument()`).
- A pair of complementary routines whose names are not antonyms of each other (`Open` / `Release`, `Begin` / `Close`). Unconventional antonyms in routine names are [[routine-names]]; in variable names, [[computed-value-qualifier-at-end]].

This wiki assigns the neighbouring cases as follows:

- A method whose name promises a read or a result and which also writes as a side job belongs to [[rename-when-meaning-drifts]].
- Sibling operations using different verbs for one action, which is the id-getter case, are [[one-name-per-concept]].
- A name whose part of speech contradicts whether the routine returns (a verb on a returning method, `isX` on a query) is [[builder-and-manipulator-names]], which resolves the disagreement between its source and this one per setting. A vague verb (`process`, `handle`) is [[routine-names]] whatever the return.
- A missing complementary operation, as opposed to a misnamed one, is [[provide-opposite-operations]].
- Names an extraction carried over from the caller are [[rename-extracted-code-for-clarity]]; a name that a later change made untrue is [[rename-when-meaning-drifts]].

This page owns vague verbs, numbering, receiver repetition, unpaired antonyms in routine names, and action names that omit a second action or output. Numbered pieces cut from one routine that continue each other's state are [[routine-length]]; numbered siblings with distinct jobs are [[routine-names]].

## When not to apply

- **"Handle" as an event handler.** The book exempts `handle` when it is used in its technical sense of handling an event (p. 167). This wiki extends that to a project's established names for event handlers.
- **A long name that is accurate.** Length is not the defect; the book allows any length that serves clarity. This wiki reads a long `...And...` name joining two purposes as a finding about cohesion ([[routine-cohesion]]), not about naming; formatting and printing one report is one purpose, as in the book's `FormatAndPrintOutput()` (p. 167).
- **Procedural code.** The rule against repeating the object applies only where the object is the receiver. A free procedure keeps verb + object (`PrintDocument(doc)`).
- **A project convention.** This wiki adds: a project's own convention for verbs and antonym pairs overrides the book's list.

## Repair

- If the routine has one clear purpose, rename it to state that purpose and every output.
- If the name needs "And" to join two results that are not one purpose, or no specific verb fits, split the routine first (see [[routine-cohesion]]), then name each part. Fowler's tools for the split are Extract Function, Split Loop and Split Variable ([[extract-routine-to-name-a-step]], [[one-loop-one-job]], [[one-variable-one-purpose]]).
- Replace numbered siblings with names that state what differs between them.
- Drop the receiver's noun from object methods.
- Rename the second routine of a complementary pair to the antonym of the first.

## Before and after

```
routine HandleOutput(report)
    lines = format report as text lines
    send lines to printer

routine OutputUser1(user)
    print user as a short line
routine OutputUser2(user)
    print user as a full card
```

```
routine FormatAndPrintReport(report)
    lines = format report as text lines
    send lines to printer

routine PrintUserSummaryLine(user)
    print user as a short line
routine PrintUserCard(user)
    print user as a full card
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.3, pp. 167-169, and the key points on p. 181 ([[code-complete]]). The guidelines, their examples and the event-handler exemption are the book's.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Mysterious Name", PDF p. 86: names for every kind of element, the hard name as a sign of a design problem, the fear of renaming and the three renames. This wiki's own for that part: the reading as a repair rule.
- The signs as listed, the owner split with neighbouring naming pages and with [[routine-length]], the limits other than the event-handler exemption, and the pseudocode are this wiki's own.

Related: [[name-by-role]], [[command-query-separation]], [[function-or-procedure]].
