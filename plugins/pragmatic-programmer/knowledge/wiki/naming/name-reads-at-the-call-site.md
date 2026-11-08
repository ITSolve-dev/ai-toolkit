---
title: A name reads at the call site
category: naming
summary: "A function name repeats its module's name when called with the qualifier, as in Fib.fib(n), so the call stutters and says nothing more."
tags: [rule, naming, modules]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A name is read in the place it is used, along with whatever qualifies it. Judging it in isolation at the definition misses what the reader sees.

## Rule

Name a function for how it reads when called in its context. The book's example is a Fibonacci module with a function returning the n-th number. Most developers would call it `fib`, which looks reasonable, but it will be called in the module's context as `Fib.fib(n)`. Calling it `of` or `nth` gives `Fib.of(0)` or `Fib.nth(20)` (p. 293).

## Sign in code

- The call site repeats the module, class or namespace name in the member name: `Invoice.invoice_total`, `Stack.stack_push`.
- A member name carries its type's name, while every call goes through an instance of that type.

## When not to apply

This wiki's limits: where callers import a function unqualified, the bare name has to stand alone, and `of` would say nothing. The rule also yields to what the language's community does, which is taken at work time. See [[follow-local-naming-culture]].

## Repair

Read three real call sites aloud. Remove from the member name whatever the qualifier already says, and keep what distinguishes it from its siblings.

## Before and after

Before:

```
price = Tax.calculate_tax(order)
```

After:

```
price = Tax.for_order(order)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 293. This wiki's own: the signs, the limits, the repair and the pseudocode. Related: [[name-by-role]].
