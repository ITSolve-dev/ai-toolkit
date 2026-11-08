---
title: Assert, then handle the error anyway
category: errors
summary: "A routine both asserts a condition on its arguments and, right after, handles the same violation at run time (clamps, rejects); decide whether that double check is warranted or whether one of the two should go."
tags: [decision-rule, assertions, contracts, robustness]
paradigm: any
sources: [code-complete, pragmatic-programmer]
created: 2026-11-06
updated: 2026-11-06
---

Usually each potential error is checked either by an assertion or by error-handling code, not by both, and some experts hold that only one kind is needed (Meyer, 1997, as cited on p. 188). McConnell argues for both in a particular kind of system.

## Rule

In large, long-lived systems, assert the condition and then also handle its violation. Such systems are built over 5-10 years or more by several designers, in different versions and technologies, sometimes in different places or bought from other companies, to differing coding standards and with uneven care, and low-level testing cannot be relied on to be complete (p. 188). The book's example is Microsoft Word, whose source first asserts conditions that must be true and then handles the case where the assertion is false, because with millions of lines and many changes not every error will be found before shipping (p. 188).

The book's own Velocity example asserts the ranges of latitude, longitude and elevation, and then clamps each to the nearest legal value (pp. 188-189).

### Disagreement with [[caller-owns-the-precondition]], resolved per setting

[[caller-owns-the-precondition]] (from *The Pragmatic Programmer*, p. 147) treats a routine that clamps an out-of-domain argument as taking the caller's decision. This wiki resolves the two as follows:

- Inside a [[barricade]], in code whose callers are in the same codebase and under tests that can be relied on, the precondition is the caller's: assert only. A clamp there hides the caller's bug.
- At a boundary between parts with separate owners, release cycles or vendors, or in a large, long-lived codebase whose low-level tests cannot be relied on to be complete (the book's Word case), assert and then handle. The assertion surfaces the bug during development; the handler protects the release.
- The handler's reaction is chosen by [[robustness-versus-correctness]]. A clamp is acceptable only at the robustness end; at the correctness end the handler refuses.

The condition that selects the page, in the words both pages use: whether the caller is held to the contract by shared code ownership and tests.

## Sign in code

- An assertion on an argument followed, in the same routine, by run-time handling of the same condition.

This page fires only to decide whether that pair is warranted. A clamp or default at entry with no assertion is [[caller-owns-the-precondition]]; an assertion on freshly read external data is [[assertion-or-error-handling]].

## When not to apply

- Data from outside the program: there the check is error handling, not an assertion (p. 188). This wiki adds that an assertion beside that handler then adds nothing.
- This wiki adds: small or single-owner code with a complete test suite, where one kind of check suffices, read from the book's own conditions for the double check.

## Repair

Where the pair is not warranted, keep the assertion and delete the handler (inside) or keep the handler and delete the assertion (external data). Where it is warranted, make the handler follow the module's robustness or correctness choice and log the violation so that the bug the assertion would have caught in development is visible in production.

## Before and after

```
# before (inside one component, callers share its tests)
function velocity(latitude, longitude, elevation):
    assert -90 <= latitude <= 90
    if latitude < -90: latitude = -90
    if latitude > 90: latitude = 90
    ...
```

```
# after, inside: the precondition is the caller's
function velocity(latitude, longitude, elevation):
    assert -90 <= latitude <= 90
    ...

# after, at a boundary: caller is the navigation module,
# maintained by another team on a separate release; no external data
function velocity(latitude, longitude, elevation):
    assert -90 <= latitude <= 90
    if not (-90 <= latitude <= 90):
        log_error("latitude out of range from navigation", latitude)
        latitude = clamp(latitude, -90, 90)    # robustness end only
    ...
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 188 for the rule, its conditions and the Word example, pp. 188-189 for the Velocity example. The raw extraction drops the minus signs from the bounds in the book's listing (it prints `90 <= latitude`); the bounds in the pseudocode here are this wiki's. Thomas, Hunt, *The Pragmatic Programmer*, [[pragmatic-programmer]], p. 147 for the opposing view. The resolution against [[caller-owns-the-precondition]], the sign, the remark that an assertion beside an external-data handler adds nothing, the second limit, the repair and the example are this wiki's own.
