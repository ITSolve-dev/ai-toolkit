---
title: Follow the local naming culture
category: naming
summary: "A conventional short name other than a loop index is bound against its convention, such as an error name (err) holding a count or s holding a number."
tags: [rule, naming, conventions]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Whether a name is good depends partly on what its readers expect. A short name that a community reads without effort can be clearer than a long one, and the same short name used against expectation misleads.

## Rule

Most introductory literature warns against one-letter variables such as `i`, `j` or `k`, and the book says of that literature that «они не совсем правы» (p. 293). It depends on the programming culture of the language or its environment. In C, `i`, `j` and `k` are traditional loop variables and `s` a string, and working there means following those norms. Respect for tradition also rules out binding `i` to a string, as in the book's Clojure fragment (pp. 293-294). The same applies to camelCase against snake_case, and to Unicode identifiers: languages allow all of them, and the local community decides what is acceptable (p. 294).

## Sign in code

- A conventionally reserved short name holds something else: a conventional name for an error bound to a count, `s` bound to a number.

This wiki assigns the neighbouring cases as follows. `i`, `j` or `k` bound to anything other than a loop index is [[loop-index-names]]; another conventional short name bound against its convention (an error name holding a count) is [[follow-local-naming-culture]]. A short name used far from its binding is [[name-length-matches-scope]]; a conventional short name bound against its convention is [[follow-local-naming-culture]].

The convention itself is taken at work time from the project's tooling and documentation, because this wiki does not record any language's style. Mixed casing is left out as a sign: it is mechanical style, which the charter leaves to tooling.

## When not to apply

These limits are this wiki's own.

- A module is being moved on purpose from one convention to another, and the project says so. Mixed names are then the plan.
- The name is fixed from outside, as with generated bindings or a field of an external format. It keeps the outside form at that edge.
- The local habit is itself a defect under another page of this wiki. Tradition covers a short scope and does not license `i` across a long function, however common that is in the surrounding code.

## Repair

Find what the surrounding code and the community do, and match it. If a conventional letter was used for something else, give it a role name; see [[name-by-role]].

## Before and after

Before: the reader expects an error.

```
err = 0
for each line in lines
    if not valid(line)
        err = err + 1
report(err)
```

After:

```
invalidLineCount = 0
for each line in lines
    if not valid(line)
        invalidLineCount = invalidLineCount + 1
report(invalidLineCount)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 293-294. This wiki's own: the signs, the omission of casing as a sign, the assignment against [[loop-index-names]] and [[name-length-matches-scope]] (the book's own example, `i` bound to a string, is owned by [[loop-index-names]]), the limits, the repair and the pseudocode.
