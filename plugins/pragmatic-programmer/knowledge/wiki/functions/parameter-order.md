---
title: Order parameters input, modified, output
category: functions
summary: "A parameter list mixing read-only inputs, in-out parameters and outputs in no order, a status or error output that is not last, or related routines taking the same parameters in different positions."
tags: [rule, parameters, interfaces, consistency]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell opens his advice on parameters with a study: Basili and Perricone (1984) found that 39% of all errors were internal interface errors, meaning errors in communication between routines (*Code Complete*, p. 170). The ordering rules below are meant to make that interface harder to misuse.

## Rule

- **Input, then modify, then output.** List read-only parameters first, then in-out parameters, then output-only parameters, rather than at random or alphabetically. The order matches what the routine does: take input, change it, return results. The book notes that this contradicts the C library convention of putting the modified parameter first. It prefers its own order, but says any order applied consistently helps the reader (pp. 170-171).
- **Status or error variables last.** They are output-only, and «Они второстепенны по отношению к главной цели метода» (p. 172).
- **Similar routines take similar parameters in the same order.** In C, `fprintf()` takes the file first and `fputs()` takes it last, which makes both harder to remember. `strncpy()` and `memcpy()` share one order (destination, source, maximum bytes), which helps (p. 172).

The book also suggests marking roles with home-made `in`/`out` keywords or name prefixes (pp. 171-172, 175). Marking which parameters are input only is [[mark-input-only-parameters]]; the order of the list is [[parameter-order]].

## Sign in code

- An output or in-out parameter (passed by reference, pointer or mutable container and written by the body) placed before a read-only input.
- A status, error-code or success flag output that is not the last parameter.
- Two or more routines in one module sharing a parameter (a file, a buffer, a context) at different positions.

## When not to apply

- **The language or ecosystem fixes an order.** Examples are the receiver first, a callback last, or a context object first. This wiki adds this limit: the book's own fallback is any consistent order, and a fixed convention is that consistent order.
- **No out-parameters.** This wiki reads the rule so that, in code that returns results instead of writing through parameters, only the consistency rule among similar routines applies.

## Repair

Reorder the declaration (inputs, then in-out, then outputs, then status) and update every call site in the same change. Bring sibling routines' shared parameters into one position. Where a routine returns several outputs through parameters, this wiki suggests asking first whether they should be one returned value.

## Before and after

```
routine CopyRecords(out status, out target, maxCount, in out log, source)
routine MoveRecords(source, out target, maxCount)
```

```
routine CopyRecords(source, maxCount, in out log, out target, out status)
routine MoveRecords(source, maxCount, out target)
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.5, pp. 170-172 and p. 175 ([[code-complete]]). The ordering rules, the C library examples and the suggestion of role markers are the book's.
- The signs, the limits as worded, the split with [[mark-input-only-parameters]], the suggestion about returning a value, and the pseudocode are this wiki's own.

Related: [[limit-parameter-count]], [[remove-unused-parameters]], [[do-not-reuse-parameters-as-working-variables]], [[match-arguments-to-parameters]].
