---
title: Extract the scattered code before changing it everywhere
category: change
summary: "A change would force every client to be edited at once (a new return type, a replaced sentinel such as x == \"unknown\"): first extract the fragment each client repeats into one function, move callers over one at a time, and trap unexpected values while the migration runs."
tags: [method, refactoring, small-steps, migration, extract-function]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's *Refactoring* (2nd ed., ch. 10) describes a recurring technique inside Introduce Special Case ([[introduce-special-case]]). Some changes look as if they must happen everywhere in one step. A container that starts returning an object instead of the string `"unknown"` breaks every client that compares to the string. Fowler wants to "make one small change at a time, then test" (PDF p. 324). The all-at-once version he finds "as appealing as eating liver (i.e., not at all)" (PDF p. 324). His way out: "I use Extract Function (106) on the code that I’d have to change in lots of places" (PDF p. 324).

## Procedure

1. **Find the fragment every client repeats** that the coming change would break, such as `x == "unknown"`.
2. **Extract it into one function** that keeps the current behaviour ([[extract-function]]).
3. **Add a trap for unexpected values** while the migration runs: the function throws if its argument is neither the old form nor the new one. Fowler put it in to "spot any mistakes or odd behavior as I’m doing this refactoring" (PDF p. 324).
4. **Move callers to the function one at a time**, testing after each ([[refactor-in-small-tested-steps]]).
5. **Make the structural change once** (the container returns the new form), then change the function's body to recognise the new form only. Clients that still see the old form now fail the trap or the tests, which shows that nothing depends on the old form any more (PDF pp. 325-326).
6. **When data passes through both a raw and an enriched path**, let the function accept both forms for the duration. Fowler keeps the original test "so that the test will work on both raw and enriched sites" (PDF p. 336).
7. When the migration is done, inline the function where a check is still needed, and delete it where it is not (PDF p. 329).

## Why it works

The function turns a change at N sites into a change at one site, and every step in between leaves the program working and tested. This wiki reads the trap as a cheap stand-in for a type check during the transition. The trap exists for the migration only, and Fowler's final version of the function drops the string case.

This wiki assigns the neighbouring procedures as follows. Renaming or re-parameterising a function whose callers can all be edited in this change is [[change-function-declaration]]; a change some of whose users lie outside this change (a published interface, stored data, a library used throughout) is [[parallel-change]]; a changed value that callers inspect, such as a sentinel they compare to, is [[extract-before-changing-many-callers]]; renaming a record field or a class's accessor pair is [[rename-widely-used-field]].

## Limits

This wiki's own note: when a language's type checker or an automated rename already finds every affected site and changes them together safely ([[automated-refactoring]]), the extracted function adds less. Its value is highest where clients are found only by text search, or where values are dynamically typed.

## Source

- Fowler, *Refactoring*, 2nd ed., ch. 10, "Introduce Special Case", PDF pp. 324-326, 329 and 336 ([[fowler-refactoring]]): the bind, extracting the comparison, the trap, the one-at-a-time migration, the switch of the container and the check that the old form is unused, the inline into the exceptional client and removal of the dead function, and the dual-form test during a transform.
- This wiki's own: the generalisation into a named procedure, the reading of the trap, the links to neighbouring procedures and the selecting sentence, and the limit.
