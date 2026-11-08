---
title: Remove parameters the routine does not use
category: functions
summary: "A declared parameter the body never reads (screenX, screenY passed and ignored), or an output parameter the body never assigns."
tags: [rule, parameters, interfaces, dead-code]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell asks that every parameter a routine receives be used, and that any other parameter be removed from the interface (*Code Complete*, p. 172). His opening example of a bad routine has two such defects. It takes `screenX` and `screenY` and never uses them, and it passes `prevColor` by reference without ever assigning it (p. 159).

## Rule

If a parameter is passed in, the routine uses it. Otherwise the parameter goes. The book links unused parameters to higher error rates. In Card, Church and Agresti (1986), 46% of routines with no unused variables were error-free, against 17-29% of routines with more than one unused variable (p. 172). The checklist asks the question both ways: are all input parameters used, and are all output parameters used (p. 181).

## Sign in code

- A parameter name that does not appear in the body.
- A parameter that appears only in a comment, a log line or an assertion and does not affect the result. This wiki reads that as unused.
- A parameter passed by reference or pointer, or marked as output, that the body never writes. If it is only read, it is really an input, and its mode misleads.

This wiki assigns the neighbouring case as follows. A parameter every caller passes with the same value is [[minimal-but-complete-functionality]]; a parameter the body ignores is [[remove-unused-parameters]].

## When not to apply

- **Conditional compilation.** The book allows one exception: parts of the routine that use the parameter may be compiled out. It asks for caution but accepts it when the author is sure. More broadly, it keeps a parameter when there is a serious reason not to use it (p. 172).
- **A fixed signature.** This wiki adds a limit. A routine that implements an interface method, an override, a callback or an event-handler type must accept what the contract passes, whether or not this implementation reads it. A project or language convention for marking such a parameter as deliberately unused belongs to the project's tooling.
- **A published interface.** This wiki also adds that removing a parameter from an API other code calls is an interface change, governed by [[break-the-build-on-interface-change]], not just a cleanup.

## Repair

Delete the parameter and the arguments at every call site. Change an output-mode parameter that is only read into an input. If a caller was computing an argument only to pass it, delete that computation too.

## Before and after

```
routine DrawLabel(text, x, y, screenWidth, screenHeight, in out previousColor)
    move cursor to x, y
    write text
```

```
routine DrawLabel(text, x, y)
    move cursor to x, y
    write text
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.5, p. 172; the opening example, p. 159; the checklist, p. 181 ([[code-complete]]). The rule, the study and the conditional-compilation exception are the book's; section 24.3, p. 561, repeats the rule as a refactoring.
- The second sign, the owner split, the fixed-signature and published-interface limits, and the pseudocode are this wiki's own.

Related: [[parameter-order]], [[routine-review-checklist]].
