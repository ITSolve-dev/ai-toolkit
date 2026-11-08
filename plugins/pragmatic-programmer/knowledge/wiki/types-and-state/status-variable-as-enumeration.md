---
title: Status variable as an enumeration behind an accessor
category: types-and-state
summary: "A status or error state is a boolean (isError, ok, failed), or several booleans for one state, tested directly by several functions outside the code that sets it, so a third state or a combined condition means revisiting every test."
tags: [rule, state, boolean, enumeration, access-routine, change]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell lists status variables among the areas most likely to change, because they describe the program's state and change more often than most data (p. 95). His example: an error status declared as a boolean later turns out to need `None`, `Warning` and `Fatal` (p. 95).

## Rule

Two measures, both the book's (pp. 95-96):

- «В качестве переменных статуса примените не булевы переменные, а перечисления.» Extending an enumeration needs a recompile, not a review of every place that tests the variable.
- «Вместо непосредственной проверки переменной используйте методы доступа.» A check hidden in a routine can later combine the status with another variable (the book's example: error status together with the current functional state) in one place.

## Sign in code

- A boolean field or variable named for a status (`error`, `isOk`, `failed`, `ready`) read by several functions outside the code that sets it.
- Two or more booleans describing one state (`isLoading` and `isError`), whose combinations callers test.
- The same direct test (`if job.error`) repeated in several functions.

This wiki assigns the neighbouring cases as follows. This page owns a status read from outside its owner. Flags held as fields of one entity and tested in combination by several of its own input handlers to choose a reaction are [[replace-flags-with-explicit-states]]; flags that one loop over a sequence of events sets and tests to track its place in that sequence are [[finite-state-machine]]; a status read by functions outside its owner is [[status-variable-as-enumeration]]. Integer codes, bare boolean arguments and boolean return values that need a third outcome are [[enum-instead-of-codes-and-flags]]. Client code that reads or writes a machine's state field is [[automated-class]]; one state machine's guard reading another machine's state is [[state-machines-communicate-through-an-explicit-interface]]. A flag in shared data written by one state machine and read by another only to coordinate them is [[state-machines-communicate-through-an-explicit-interface]]. The status variable's name, where it contains `flag`, is [[status-variable-not-flag]], and a boolean's name generally is [[boolean-variable-names]]; this page decides whether it should stay a boolean.

## When not to apply

- This wiki's limit: the state is two-valued by its meaning (present or absent, an on/off switch) and tested in one place. The book's reason for the rule is likely growth of the state set (p. 95); with neither growth nor spread the boolean costs nothing.
- A status local to one routine needs no accessor. This limit is this wiki's own.
- Where the language has a sum type carrying data per state, this wiki notes the enumeration may be replaced by that type.

## Repair

Replace the boolean, or the set of booleans, with an enumeration of named states, and replace direct tests at call sites with a query on the owner that names the question being asked.

## Before and after

```
class Job
    error: bool

-- in different functions
if job.error
    retry(job)
if not job.error
    report(job)
```

```
enum ErrorType
    None, Warning, Fatal

class Job
    private errorType: ErrorType
    function needsRetry(): bool
        return errorType != None
    function isReportable(): bool
        return errorType == None

if job.needsRetry()
    retry(job)
if job.isReportable()
    report(job)
```

## Source

[[code-complete]], ch. 5, section 5.3, Russian edition, pp. 95-96. The `None/Warning/Fatal` example and the two measures are the book's. The signs, the assignment of neighbouring cases, the limits marked as such, the note on sum types and the pseudocode are this wiki's own.
