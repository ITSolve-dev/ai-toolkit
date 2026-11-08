---
title: Assertion or error handling
category: errors
summary: "An assert or precondition guards a value just read from a user, file, network or config; this page also decides whether a soft error return covers a state only a bug can produce."
tags: [decision-rule, assertions, validation]
paradigm: any
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Assertions and error handling look alike because both test a condition. They differ in what a failure means.

## Rule

Ask whether the condition can fail in a correct program. If it can, write real error handling. If only a bug can fail it, use an assertion or a contract. «Утверждения позволяют проверить то, что никогда не должно случиться.» and «Ни в коем случае не пользуйтесь утверждениями вместо реальной обработки ошибок.» (p. 153). The same holds for contracts: since a breach is a bug that nothing guarantees will not occur, preconditions must not be used to validate user input (p. 142). The book orders the two: checking for every possible error is the first line of defence, and assertions are the second, for what slipped past (p. 154).

*Code Complete* states the same test: «Используйте процедуры обработки ошибок для ожидаемых событий и утверждения для событий, которые происходить не должны» (p. 186). An error handler checks for unusual events that the programmer foresaw and that must be handled in production too; it usually checks bad input data, while assertions catch «ошибки в программе» (p. 186). The consequence differs: a handler lets the program react, while a failed assertion means the source must be changed, recompiled and released (p. 186).

McConnell adds what assertions are for. They document assumptions more actively than comments, as «выполняемую документацию» (p. 186), and they state preconditions and postconditions in the sense of [[design-by-contract]] (p. 187). Typical uses: a parameter in its expected range; a file or stream open or closed, at its start or end, read-only or writable, when a routine starts or ends; an input not changed by the routine; a non-null pointer; a container able to hold at least X elements; a table initialised; a container empty or full; a fast optimised routine agreeing with a slow clear one (p. 185).

His position test matches this page's first limit: if latitude, longitude and elevation came from an external source, they must be checked by error handling; if they came from a trusted internal source and the routine is designed on the assumption that they are in range, assertions are appropriate (p. 188). [[barricade]] turns that into a design: handlers outside, assertions inside (p. 200).

Fowler's *Refactoring* states the same line: "I only use assertions for things that are programmer errors. If I'm reading data from an external source, any value checking should be a first-class part of the program, not an assertion—unless I'm really confident in the external source." (2nd ed., ch. 10, Introduce Assertion, PDF p. 341). He adds that "Assertion failures should never be checked by other parts of the system" (p. 339): an assertion is not control flow.

## Sign in code

- An `assert` or precondition tests a value on the lines right after it was read from a user, file, socket, environment variable or config.
- A failed read, a bad reply or a malformed record reaches an assertion instead of a handler.
- Code that catches or inspects an assertion failure to decide what to do next: the condition is being used as error handling (Fowler, p. 339).
- The reverse: code returns a friendly error or null for a state that only a bug in this program could produce. [[crash-early]] owns that shape and its repair, and this page supplies the test of whether the state is such a case.

## When not to apply

- The test depends on position, not on the value. Once a value has passed validation at the boundary, asserting the same condition further in is correct, because a failure there is a bug.
- A throwaway script where abort is the wanted reaction to any bad input.
- Fowler allows an assertion on external data only where he is really confident in the source (PDF p. 341). This wiki reads that as data this program itself wrote, not user input or another system's output.
- One condition both asserted and handled in the same routine, which McConnell recommends for large, long-lived systems (p. 188): [[assert-then-handle-anyway]] decides that case, not this page.

## Repair

For an expected failure, replace the assertion with a branch that reacts: reject, ask again, retry or report. For an impossible state, replace the soft return with a failing check ([[assert-the-impossible]], [[crash-early]]). When the same condition matters on both sides, keep both: handling at the boundary, assertion inside. This wiki does not read that as the repeated check of [[caller-owns-the-precondition]], which repeats the reaction as well.

## Before and after

```
# before
function read_port(config):
    port = to_number(config.get("port"))
    assert port > 0 and port < 65536
    return port
```

```
# after
function read_port(config):
    port = to_number(config.get("port"))
    if not is_port(port):
        return failure("port must be a number from 1 to 65535")
    return success(port)

function is_port(value):
    return value is valid and value > 0 and value < 65536

function open_listener(port):
    # requires: port came through read_port
    assert is_port(port)
    bind(port)
```

Pre- and postconditions on a routine called only from internal code, after McConnell's Velocity routine:

```
# before
function velocity(latitude, longitude, elevation):   # called only from internal code
    if latitude < -90 or latitude > 90:
        return ERROR_BAD_LATITUDE
    ...
```

```
# after
function velocity(latitude, longitude, elevation):
    # preconditions
    assert -90 <= latitude <= 90
    assert 0 <= longitude < 360
    assert 500 <= elevation <= 75000
    ...
    # postcondition
    assert 0 <= result <= 600
    return result
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 142, 153, 154 for the rule. McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: pp. 184-185 for what an assertion is and its uses, p. 186 for the rule, p. 187 for pre- and postconditions, p. 188 for the position test and the double check, p. 200 for barricades. The test as worded, the signs, the limits other than the double-check case, the repair and both examples are this wiki's own; the second is pseudocode after the book's Velocity routine, whose bounds lose their minus signs in the raw extraction.

Fowler, *Refactoring*, 2nd ed., ch. 10, "Introduce Assertion", PDF pp. 339 and 341, via [[fowler-refactoring]]: assertions for programmer errors only, external data checked as a first-class part of the program, no checking of assertion failures, and the confident-source exception. This wiki's own: the sign on caught assertion failures as worded, and reading a confident source as data this program wrote.
