---
title: Several error exits that share one cleanup
category: errors
summary: "A routine that acquires something, runs several steps that can each fail, and must release it on every exit: shown as goto to a cleanup label, deep nested ifs, repeated 'if status == OK' checks, or the release copied before each early return."
tags: [decision-rule, error-handling, cleanup, goto, status-variable, try-finally]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A routine that allocates a resource, performs several steps that can each fail, and must free the resource on every path is McConnell's typical case for a goto (pp. 393-394 of [[code-complete]]). The alternative to the goto is usually duplicated cleanup code. He rewrites one routine four ways, which deletes a list of files and frees the list at the end, and compares them (pp. 393-398).

## Rule

The four courses, with the book's verdict on each (p. 398):

| Approach | Gains | Costs |
|---|---|---|
| goto to a single cleanup label | no deep nesting, no extra tests | it is a goto |
| nested ifs | no goto | its deep nesting «преувеличивает картину логической сложности метода» |
| status variable, rechecked before each step | no goto, no deep nesting | extra tests, and the idiom is uncommon, so document it |
| try-finally | simplest, no goto, no nesting | not available in every language; every call must signal failure by exception |

Prefer try-finally in languages that provide it, unless the system has already standardised another approach. Otherwise the status variable is slightly preferable to goto and nested ifs, because it reads better and models the problem more closely, though that does not make it best in every situation (p. 398). Whichever approach is chosen, make it a project-level decision. All of them work well only «если последовательно применяются ко всему коду проекта» (p. 398).

## Sign in code

- A cleanup label reached by `goto` from several failure branches.
- A ladder of nested success checks in which an error assignment sits far below its test. McConnell's nested version puts one 13 lines from its `if` (p. 395). In the goto version no statement sits more than four lines from the condition that triggers it (p. 395).
- The same release call copied before each early `return`.
- A try-finally routine in a codebase that also signals failure through error codes, so the routine has to translate every code. The book says this makes it about as complex as the other versions (p. 398).

This wiki assigns ownership as follows. [[exception-safe-release]] owns a release that sits after its use with no finally or scope binding. This page owns the choice between ways of routing several failure exits through one cleanup. When a failure needs cleanup that the routine itself must perform, this page owns the shape, whether written as goto, nested ifs or a status variable; otherwise [[guard-clauses]] owns it. A lock is the special case [[release-lock-on-every-path]]. Other uses of goto are [[goto-as-last-resort]].

## When not to apply

- Where no failure needs cleanup, plain early returns are enough: [[guard-clauses]].
- Where the project already has a settled convention for this shape, follow it. The book's preference for try-finally gives way to a system that has already standardised another approach (p. 398).
- This wiki adds that a language scope construct which releases on exit (a using, with or defer block, or a destructor) does the job of try-finally with less code. The book does not discuss such constructs here.

## Repair

Where exceptions are the project's failure channel, put the steps in `try` and the release in `finally`. Where error codes are the channel, keep one status variable, test it in the loop condition and before each step, and release once after the loop. Name the status values with a well-named enumeration, which the book says helps a great deal (p. 397).

## Before and after

```
build list
for each file in list:
    if not find(file):      status = FIND_ERROR;      goto cleanup
    if not open(file):      status = OPEN_ERROR;      goto cleanup
    if not overwrite(file): status = OVERWRITE_ERROR; goto cleanup
    if not erase(file):     status = ERASE_ERROR;     goto cleanup
cleanup:
free list
```

```
build list
try:
    for each file in list:
        find(file); open(file); overwrite(file); erase(file)   -- each throws on failure
finally:
    free list
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 17.3, "Error processing and gotos", pp. 393-398: [[code-complete]]. The four approaches, their trade-offs, the order of preference and the project-level consistency rule are the book's. The ownership split with neighbouring pages, the remark on scope constructs, and the pseudocode are this wiki's own.
