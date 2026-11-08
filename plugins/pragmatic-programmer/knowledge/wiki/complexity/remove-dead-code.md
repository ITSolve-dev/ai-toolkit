---
title: Remove dead code
category: complexity
summary: "Commented-out code, a private or file-local function or constant with no callers, a branch whose condition can never hold, or code after an unconditional return: delete it and rely on version control to bring it back."
tags: [rule, dead-code, comments, version-control]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's Remove Dead Code deletes code that is no longer used. The cost of dead code is not runtime, since "we aren't charged by weight" (*Refactoring*, 2nd ed., ch. 8, PDF p. 267). The cost is understanding: unused code "doesn't carry any warning signs telling programmers that they can ignore this function" (p. 267). So readers spend time working out what it does, and why changing it does not change the output they expected.

## Rule

"Once code isn't used any more, we should delete it" (p. 267). Fear of needing it later is not a reason to keep it, because version control can bring it back (p. 267). If he really expects to need it, Fowler might leave a comment that names the removed code and the revision that removed it, but he says he cannot remember the last time he did that or regretted not doing it (p. 267).

Commenting code out instead of deleting it was useful before version control was common or convenient. That is "no longer needed" (p. 267).

## Sign in code

- A block of commented-out code.
- A function, method or constant with no callers, where every possible caller is visible to a search: private members, file-local or module-private functions.
- This wiki adds: a branch whose condition the types or the control flow of the routine make impossible.

This wiki assigns the neighbouring cases as follows. A private or file-local member with no callers, or commented-out code, is [[remove-dead-code]]; a public operation with no caller anywhere is [[minimal-but-complete-functionality]]. A function or class whose only callers are tests is [[minimal-but-complete-functionality]], whose repair ends in this page's deletion; a hook built for a future need is routed by [[speculative-generality]]. A parameter the routine never reads is [[remove-unused-parameters]]. A call that runs but whose purpose no one can state is [[remove-calls-you-cannot-justify]]. A check that a type already makes impossible is the dead-code limit on [[assert-the-impossible]]. A branch that the types or the control flow of the routine prove unreachable is [[remove-dead-code]]; a branch that is impossible only because of an assumption about run-time values is [[assert-the-impossible]].

## When not to apply

- **The code can be reached from outside what a search covers.** Fowler's mechanics require a search for callers when the dead code "can be referenced from outside, e.g., when it's a full function" (p. 267). This wiki reads that as follows: for a public function of a published library, or one reached by reflection, configuration or a framework by name, a search of this repository does not prove it dead. Such a case needs knowledge of external callers, which code alone does not show; report it as a candidate and do not delete it.
- **No version control.** This wiki reads the book's reason as a limit: the argument for deleting rests on version control being able to restore the code (p. 267).
- This wiki adds: a deliberately disabled path that the code states as such, with a failure in place (the boarded-up window of [[broken-windows]]), is not commented-out code; it runs and reports what is missing.

## Repair

If the code could be referenced from outside, search for callers. Remove the code, then test (p. 267).

## Before and after

```
class Invoice
  total(): return sum(lines.map(l -> l.amount))

  // oldTotal():
  //   t = 0
  //   for l in lines: t = t + l.amount * 1.2
  //   return t

  private legacyRound(x): return floor(x * 100) / 100   // no callers
```

```
class Invoice
  total(): return sum(lines.map(l -> l.amount))
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 8, Remove Dead Code, PDF p. 267 ([[fowler-refactoring]]): the cost to readers, the rule, version control as the reason, the comment naming the revision, commented-out code and the caller search. This wiki's own parts are the restriction of the sign to code whose callers can all be searched, the unreachable-branch instance and its split with [[assert-the-impossible]], the reading of the version-control reason as a limit, the reflection/framework limit, the boarded-up-window limit, the assignment against neighbouring pages and the pseudocode.
