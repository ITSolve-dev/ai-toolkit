---
title: State the contract of a routine
category: documentation
summary: "The body indexes, divides or dereferences an argument under a condition (non-empty, positive, open) that its comment and signature never state."
tags: [rule, contracts, comments, parameters]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

A routine's contract can exist on paper before any tool enforces it. The book calls listing it a huge step forward and a good start, and says that having the compiler check the contract gives more (p. 145). See [[design-by-contract]].

## Rule

Before writing the code, list the limits of the input domain, the boundary conditions, what the routine promises and, more importantly, what it does not promise (p. 145). Where a language has no contract support, put this in comments or unit tests; it is still a real benefit (p. 145). The authors say that leaving these conditions unstated returns you to programming by coincidence (p. 145).

McConnell adds when and what (*Code Complete*, p. 174). Document an assumption about the data passed in when you make it, not after the routine is finished, when much will have been forgotten; documenting it both in the routine and at the call sites is time well spent, and an assertion, which builds the assumption into the code, is better still. His list of parameter assumptions worth stating:

- whether each parameter is input-only, modified or output-only;
- units of measure (inches, feet, metres);
- the meaning of status and error codes, when they are not enumerations;
- ranges of allowed values;
- specific values that must never be passed in.

## Sign in code

- The body indexes, divides or dereferences a parameter in a way that fails unless a condition holds (non-empty, non-zero, open), the type does not rule that failure out, and nothing above it states the condition: `items[0]` under a comment that only says it returns the first item. This wiki counts "not null" only where a caller or a path in view can pass null, because a plain dereference of a reference parameter would otherwise fit nearly any routine.
- The comment restates the routine's name and is silent on empty input, on range, and on what comes back when nothing matches.
- A runtime check in the body such as `if amount <= 0: fail` is the only place the domain is written down, so a caller must read the implementation to learn it.
- An integer status or error parameter, or return value, whose possible values are not stated anywhere near the signature. This sign is this wiki's reading of McConnell's list.

This page owns a missing precondition or boundary result on any routine, exported or not. Whether an export carries a doc comment at all belongs to [[documentation-in-the-source]]. This wiki reads a contract as a fact no name or signature carries, so a comment stating one on non-exported code with distant callers is the kind [[comment-why-not-how]] allows. A comment restating the name over a body that fails or returns a special value unless a condition holds that neither its name nor its signature states is this page's, and the repair replaces it. With no such condition, or within the limits below, the comment is only a duplicate, which [[comment-why-not-how]] owns. A measure with no unit is judged by where it is declared: a parameter is [[name-by-role]], a stored field or constant is [[representation-that-fits-by-coincidence]], a local is [[comment-data-declarations]]. A parameter the routine writes to, declared like the read-only ones with nothing marking it as an output, is [[routine-header-comment]]; their order is [[parameter-order]].

## When not to apply

- The parameter's type already states the condition, such as a non-empty list, a positive-amount type, a `Duration` that carries its unit, an enumeration of status codes or a read-only marker. Repeating it in a comment adds a second copy that can drift.
- A private helper whose few callers sit next to it and whose domain is plain from the code around it.
- Absence of a runtime check is not itself a violation where the language has no contract support: the book accepts a contract held only in comments or tests there, as a real benefit though a smaller one than a check (p. 145). This wiki extends that to a check the cost rules out.

## Repair

Write the precondition, the postcondition and the non-promise next to the signature, which is also where [[documentation-in-the-source]] puts the contract of an export. Use the strongest form the language offers: a type, then an assertion, then a comment. Make them executable where the cost allows ([[assert-the-impossible]]; which of assertion and error handling fits is decided on [[assertion-or-error-handling]]), and otherwise keep them as a comment or a test. If the promise is hard to word, report that as a finding: the book's point is that a contract forces you to think (p. 143).

## Before and after

```
# before
function median(values):
    # Returns the median.
    ordered = sort(values)
    return ordered[length(ordered) / 2]
```

```
# after
function median(values):
    requires not is_empty(values)    # a checked clause, so the condition is stated once
    # ensures: result is an element of values; for an even length, the upper middle one
    # does not promise: interpolation between the two middle elements
    ordered = sort(values)
    return ordered[length(ordered) / 2]
```

A domain written down only in a runtime check:

```
# before
function wait_ms(timeout_ms):
    if timeout_ms <= 0 or timeout_ms > 60000: fail("bad timeout")
    sleep_ms(timeout_ms)
```

```
# after
# requires: 0 < timeout_ms <= 60000; otherwise fails with "timeout_ms out of range"
function wait_ms(timeout_ms):
    if timeout_ms <= 0 or timeout_ms > 60000: fail("timeout_ms out of range")
    sleep_ms(timeout_ms)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 143, 145 for the rule and the third limit. The signs, the splits with [[documentation-in-the-source]] and [[comment-why-not-how]], the reading of a contract as a fact a comment may carry, the first two limits, the extension of the third to a check the cost rules out, the repair apart from its closing remark, and the example are this wiki's own.

McConnell, *Code Complete*, 2nd ed., Russian edition, section 7.5, [[code-complete]]: p. 174 for the list of assumptions to document, the timing, and the preference for assertions. The status-code sign, the splits with [[name-by-role]] and [[routine-header-comment]], the extension of the first limit to units, status enumerations and modes, the order of forms in the repair and the second pair are this wiki's own.
