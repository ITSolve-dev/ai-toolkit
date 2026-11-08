---
title: Recover only at entry points
category: errors
summary: "A catch below an entry point does not rethrow: it returns 0, -1 or a default, assigns a fallback value, or only logs, for a failure a correct program can meet (I/O, network, parsing external text); or the reverse, an entry point or main loop with no handler around the unit of work while the user's unsaved data lives in memory."
tags: [rule, exceptions, fail-fast, recovery, retry, graceful-termination]
paradigm: any
sources: [elegant-objects, object-oriented-thought-process, against-railway-oriented-programming]
created: 2026-11-03
updated: 2026-11-07
---

The book sets two approaches to failure against each other: fail as fast as possible, or fail as safely as possible (p. 206). Fail-safe code tries to keep running whatever happens, so it returns null, zero or a default where it could not do its job. Fail-fast code stops and throws the moment it meets a problem, so its points of failure are visible and each one can be reproduced in a unit test (pp. 206-207). The book chooses fail-fast and turns it into a rule about where an exception may be caught and not rethrown.

## Rule

Let exceptions travel up, and recover only at the application's entry points, where a user or a caller from outside talks to the program: «Верхний уровень приложения — единственное законное место восстановления.» (p. 221). Everywhere else, a method either does not catch, or catches, wraps and rethrows ([[chain-exceptions]]). «Для существования каждого блока catch должна быть веская причина.» (p. 214).

The book gives these reasons:

- **A hidden failure surfaces far from its cause.** A size method that returns 0 when the file system fails lets the program run on with a wrong size. The program fails later, far from the call, and it takes hours of debugging to learn that the 0 was an I/O error (p. 215).
- **Exceptions are not branches.** Catching in order to pick the next step is using exceptions for control flow: «Исключения сделаны не для того, чтобы заменять условные операторы.» (p. 216). Recovering from a parse failure by assigning -1 is the same pattern, and as bad as returning null (pp. 220-221).
- **Catch-and-log is the same fault.** The book calls it an awful anti-pattern (p. 217).
- **The entry point exists anyway.** A command-line program's `main` catches everything and tells the user what went wrong. Without that catch, the runtime prints a stack trace instead (pp. 220-221). The book counts few entry points even in a complex system (p. 221).

Weisfeld's *The Object-Oriented Thought Process* states the entry-point side as a general rule: «приложение никогда не должно завершаться аварийно» (p. 104). On finding an error the system must «либо «починить» себя и продолжить функционировать, либо корректно завершить свою работу без потери каких-либо данных, важных для пользователя» (p. 104), and a good class anticipates errors and includes code to handle them (p. 104). Read literally this opposes [[crash-early]]. This wiki resolves the two by setting: inside a component, code that meets a failure it cannot correct stops the current operation and raises, as above; at the outermost boundary (the main loop, a request handler, a UI event) one handler keeps the user's data intact (save, roll back, keep the draft), reports, and then carries on with the next unit of work or shuts down cleanly. "Never crash" then governs how the program ends, and does not license a component to run on in a broken state. His chapter 3 example catches the `ArithmeticException` of a division the code in view makes by zero, prints, assigns `count = 1` and continues (p. 77); only a bug produces that failure, so [[crash-early]] owns it.

Wlaschin's *Against Railway-Oriented Programming* reaches the same place from code that carries failures as values: «No matter how many exceptions you convert into `Result`s, some will always leak out. You will always need to handle exceptions appropriately in the highest parts of the system.» Panics, which leave the system in an unknown state, are «best handled by abandoning the workflow and raising an exception which is then caught and logged at the highest appropriate level (e.g. the main function of the application or equivalent)» ([[against-railway-oriented-programming]]). This wiki reads that as the top-level handler holding in a project whose convention is a result type, too; which failures reach it is decided on [[crash-early]] and [[wrap-values-between-transformations]].

This wiki applies the rule outside Java; the author restricts the practical value of section 4.2 to Java (p. 211). The transfer rests on the book's language-free reason, a hidden failure surfacing far from its cause (p. 215), and is this wiki's own.

## Sign in code

- A `catch` block in a method that is not an entry point ends without a `throw`. It returns 0, -1, an empty value or a default, assigns a fallback to a variable, or only writes to a log.
- A call site compares a result with an in-band failure value (`== -1`, `== 0`) that a catch further down produced.
- A retry loop inside a domain method, which catches the failure, counts attempts and rethrows only after the last one (pp. 221-222).
- The reverse shape at the boundary: an entry point or long-running loop with no handler around the unit of work, while the user's unsaved input or an open transaction lives in memory, so one exception ends the process and loses it (after Weisfeld, p. 104).

This wiki assigns the neighbouring cases as follows. This page owns a non-rethrowing catch for a failure a correct program can meet, such as I/O, the network or parsing text from outside. A catch whose type admits a failure a correct program can meet, a catch-all included, that ends in a sentinel, a default, a fallback or only a log, is [[recover-only-at-entry-points]]; [[crash-early]] owns a catch, branch or sentinel only where the code in view shows that only a bug can produce the failure. [[log-and-rethrow]] owns a handler that logs and then rethrows the same exception. Where the project carries failures as values (a result or option type), [[wrap-values-between-transformations]] owns a sentinel or marker returned for a failure; where it carries them as exceptions, [[recover-only-at-entry-points]] owns a sentinel returned from a catch; a null or marker returned for an absence, rather than a failure, is [[never-return-null]]. A sentinel returned from a catch below an entry point, for a failure a correct program can meet, is [[recover-only-at-entry-points]]; [[never-return-null]] owns a null or sentinel returned with no catch, for an absence such as a lookup that finds nothing. The condition that selects [[exceptions-for-the-exceptional]], in the words both pages use: whether the catch around the call turns the exception into ordinary flow, for an outcome the callee throws though a correct program meets it as a normal result. Then that page owns it and its repair replaces the throw; otherwise this page's repair (rethrow) applies. A catch that turns an exception into a failure value of a result type, rather than into a sentinel or a default, is [[wrap-values-between-transformations]], which decides whether that failure belongs in the result at all.

## When not to apply

- **Retry.** The book concedes that a local retry is bad practice with no better alternative inside the method (p. 222). Its answer is to move the retry out of the method into an aspect, a wrapper that intercepts the call (pp. 222-223). The recovery still happens below the entry point, but it is now one reusable mechanism rather than a loop in each class. This wiki reads a decorator around the object as the equivalent of the aspect in a language without AOP; see [[composable-decorators]].
- **Several entry points.** Every place the outside world enters is an entry point: each request handler of a server, each job of a worker, each callback a framework invokes. The book admits that its ideal, one catch per entry point and none elsewhere, is nearly impossible because languages and frameworks are built otherwise (p. 214). This wiki adds that the size of the unit failed is the request or the job, not the process, as in the limit on [[crash-early]].
- **Input from a person, parsed where it is read.** A reader's objection in the book is that a form must tell "not a number" from "too big", and may substitute a default for an empty field (pp. 226-227). The author does not answer it in print; to a related question he allows that an error must sometimes be caught earlier and says such places are to be avoided (p. 225). This wiki resolves the two by setting: the code reading user input is itself at the boundary, so handling a parse failure there is recovery at the entry point. It is not the same as a catch deep inside a domain method. See [[assertion-or-error-handling]] and [[distrust-external-input]].
- **Specified degradation.** A routine may catch below an entry point and fall back, as a cache read that falls back to the source, or optional enrichment or telemetry that the work goes on without, provided the fallback is stated in the routine's contract and the failure is logged once. Whether the fallback is acceptable is decided on [[robustness-versus-correctness]]. This limit is this wiki's own.
- **No user data at stake.** A short-lived tool or batch job that holds no user data terminates cleanly by exiting with an error code; a process whose supervisor restarts it, with state already persisted, recovers by dying. The boundary sign above does not fire there. This limit is this wiki's own.
- **Releasing a resource.** A `finally` or scoped release is not recovery and is required: [[exception-safe-release]].

## Repair

1. Delete the catch, or replace its fallback with a wrap and rethrow that keeps the cause ([[chain-exceptions]]).
2. Make sure the entry point has the one catch that reports the failure to the user or the caller. Where the user's data is in memory, that handler preserves it first (a recovery copy, a rollback), then reports, then continues with the next unit of work or exits cleanly (after Weisfeld, p. 104).
3. Move a retry loop out of the domain method into a wrapper configured with the attempt count and back-off. The book notes that a proper retry also logs the failure and increases the interval between attempts (p. 222).
4. Remove the `== -1` checks at the call sites. They now cannot fire.

## Before and after

```
# before
function length(file):
    try:
        return size_of(read_all(file))
    catch IoFailure:
        return 0

function main(args):
    print(length(file_from(args)))
```

```
# after
function length(file):
    try:
        return size_of(read_all(file))
    catch IoFailure as cause:
        throw StorageFailure("cannot compute size of " + file.path, cause = cause)

function main(args):
    try:
        print(length(file_from(args)))
    catch any failure as problem:
        print_error("Sorry, something went wrong: " + problem.message)
```

```
# before: retry inside the domain method
class PageSource:
    field url
    method page():
        attempt = 0
        loop:
            try:
                return http_get(this.url)
            catch IoFailure as cause:
                attempt = attempt + 1
                if attempt >= 3:
                    throw cause

# after: the method fails at once, a wrapper retries
class PageSource:
    field url
    method page():
        return http_get(this.url)

source = Retrying(PageSource(url), attempts = 3, backoff = doubling)
```

## Source

- Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018: section 4.1, pp. 206-208 (fail fast against fail safe), and section 4.2, pp. 214-223 (unneeded catches, control flow, -1, catch-and-log, recovering once, AOP). The scope of section 4.2 is on p. 211; the reader's objection is on pp. 226-227 and the author's answer to a related question on p. 225. Summary page: [[elegant-objects]].
- The quotations from pp. 214, 216 and 221 were checked against the page image.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 77 (the handler assigning `count = 1`), p. 104 (never crash, repair or terminate without losing user data, anticipate errors). The quotations were checked against `raw/`. This wiki's own for that part: the per-setting resolution against [[crash-early]], assigning the p. 77 handler to [[crash-early]], the boundary sign, the no-user-data limit and the data-first order in repair step 2.
- Wlaschin, "Against Railway-Oriented Programming", fsharpforfunandprofit.com, 2019, [[against-railway-oriented-programming]]: the two quotations on exceptions handled at the top; reading them as the rule holding under a result-type convention is this wiki's own, as is the assignment of a catch that returns a failure value to [[wrap-values-between-transformations]].
- This wiki's own parts are: the signs as worded; the conditions that divide this page from [[crash-early]], [[log-and-rethrow]], [[wrap-values-between-transformations]], [[never-return-null]] and [[exceptions-for-the-exceptional]]; the link of the degradation limit to [[robustness-versus-correctness]]; the decorator as a substitute for the aspect; requests, jobs and callbacks counted as entry points; the resolution of the user-input objection; the transfer of the rule outside Java; and the limit for specified degradation.
