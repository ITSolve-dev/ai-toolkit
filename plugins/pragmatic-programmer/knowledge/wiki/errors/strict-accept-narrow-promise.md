---
title: Accept strictly, promise little
category: errors
summary: "A routine opens by normalising several shapes of the same argument, or returns success values of different kinds on different paths, such as one item or a list. A declared success-or-failure result is not this sign."
tags: [rule, contracts, lazy-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The book calls this lazy code, as a companion to the humble code of its topic on orthogonality (p. 143). A wide contract is paid for in code.

## Rule

A routine should «строго относиться к тому, что принимается, прежде чем начинать что-нибудь делать, а также обещать как можно меньше» (p. 143). The reasoning is direct: if a contract accepts anything and promises the world, honouring it takes a lot of code (p. 143).

## Sign in code

- The first lines of a routine branch on the type or shape of one parameter and convert each form to a common one. This page owns that shape, where every form is inside the domain. A routine that overwrites a value outside its domain belongs to [[caller-owns-the-precondition]].
- A routine returns success values of different kinds on different paths, such as one item on one and a list on another, so every caller must branch on the kind. A null for nothing found on a routine returning a collection is this sign, unless the caller in view cannot go on with an empty result, which is [[wrap-values-between-transformations]]. A declared result that holds a value or a failure is one shape and not this sign: [[wrap-values-between-transformations]] owns it.

## When not to apply

- The outer edge of a program that reads external data. Tolerance has to live somewhere, and this wiki places it in one adapter at that edge.
- A convenience interface that is deliberately overloaded. It is acceptable as a thin layer over a strict core, so the strict routine still exists.
- A wider promise that callers already need. Narrowing it there breaks them, so the promise stands until they change.

## Repair

Narrow the parameter to one shape and move conversion to the caller or a single adapter. Return one kind of success value on every path, with an empty collection for nothing found. Delete the promises nothing needs, then delete the branches that served them. Write down what remains ([[state-the-contract]]).

## Before and after

```
# before
function schedule(when):
    if is_string(when): when = parse_date(when)
    if is_number(when): when = from_epoch(when)
    enqueue(when)
```

```
# after
function schedule(when):
    # requires: when is a timestamp
    # ensures: a job is queued for when
    enqueue(when)
```

```
# before
function find_users(name):
    matches = search(name)
    if length(matches) == 1: return first(matches)
    return matches
```

```
# after
function find_users(name):
    # ensures: a list of every match, possibly empty
    return search(name)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: p. 143 for the rule and its reasoning. The signs, limits, repair and example are this wiki's own.
