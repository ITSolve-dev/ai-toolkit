---
title: Use existing components before writing your own
category: complexity
summary: "A hand-written container, sort, search, or date/number/format routine duplicates what the standard library or a dependency already in the project provides, with no stated speed, precision or interface need."
tags: [rule, reuse, accidental-complexity, libraries, build-vs-buy]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

**Using existing components** means taking a general-purpose part from the language or a library already in the project (a container, a sort, mathematical functions, user-interface or database classes) instead of writing it again. McConnell makes the point through the building metaphor: nobody building a house designs their own washing machine, refrigerator, cabinets, windows and doors when they can buy them, and software is built the same way (p. 17). His conclusion: «Обычно невыгодно писать компоненты, которые можно купить готовыми» (p. 17).

## Rule

The source says to make full use of the high-level language rather than write your own operating-system-level code, and adds that you may also use built-in libraries of container classes, scientific functions, UI classes and database classes (p. 17). In its account of the writing metaphor it adds that, in construction, an original approach often works worse than reusing ideas, code and tests from earlier projects (p. 12).

This wiki reads what breaks when the rule is ignored as accidental complexity. A hand-rolled general component is code the project now has to test, debug and maintain; it usually handles fewer edge cases than the library version, and a reader has to study it instead of recognising a known name. The source does not spell out this reasoning. See [[managing-complexity]].

## Sign in code

- A class or module whose job is a general data structure (list, map, set, queue, heap, tree) or a general algorithm (sort, binary search, shuffle, hashing), when the language or a dependency already in the project provides the same operation.
- Hand-written parsing or formatting of a standard format (dates, numbers, URLs, CSV, JSON) beside an available library routine for it.
- No comment, test or benchmark near it that names a requirement the existing component fails to meet.

All three can be checked against the code and its dependency list. Whether a library exists for the project's language is settled at work time from the project's tooling and documentation, not from this page.

This wiki assigns the neighbouring cases as follows. This page owns a general-purpose part re-implemented. Vendor calls spread across modules are [[hide-third-party-apis]]. Hand-written cryptography is [[do-not-implement-cryptography]], whose reason is security, not complexity. Where a hand-written component that the library already offers claims speed, [[fastest-algorithm-is-not-always-best]] owns it; where no reason is stated, [[use-existing-components-before-writing-your-own]] owns it. A hand-written parser for a configuration or data language the project defines is [[internal-vs-external-dsl]]; re-parsing an existing standard format that a library already reads is [[use-existing-components-before-writing-your-own]]. A block of statements inside a routine that computes what one existing function already computes is [[replace-inline-code-with-function-call]]; a hand-written general-purpose part (its own routine or class) that the library already provides is [[use-existing-components-before-writing-your-own]]. Swapping such a part for the library once the decision is made follows [[substitute-algorithm]].

## When not to apply

- The source's own exception: high-end applications sometimes need their own scientific functions, container classes and other components, for higher speed, more precise calculation or an unusual interface, like furniture or windows made to order for a non-standard house (p. 17). If the code states such a need (a benchmark, a precision requirement, an interface the library cannot give), the custom component is the rule applied correctly.
- This wiki adds three exceptions of its own. Taking on a new dependency only for a trivial routine can cost more than the routine. A library the project cannot accept (licence, size, target platform) is not available. Code written to teach or to test an algorithm is not a violation.

## Repair

This wiki's own: replace the hand-written component with the standard or library one, keeping the call sites' intent. If the custom version exists for a real need, keep it and write that need next to it, as a comment naming the requirement plus a test or benchmark showing the library version failing it, so the next reader does not have to rediscover why.

## Before and after

```
// before: a general sorted collection written by hand
class SortedIntList
    items = []
    add(x)
        i = 0
        while i < length(items) and items[i] < x
            i = i + 1
        insert(items, i, x)
    contains(x)
        // hand-written binary search, off-by-one prone
        ...

scores = new SortedIntList()
for s in results: scores.add(s)
```

```
// after: the platform's sort and search routines
scores = sorted(results)
if binarySearch(scores, target) found then ...
```

The "after" contains no general-purpose part written by hand. The "before" states no speed, precision or interface requirement, so it falls outside the page's limits.

## Source

[[code-complete]], ch. 2, section 2.3, Russian edition: the building metaphor, p. 17 (buy rather than build, and the exception for high-end applications), and the writing metaphor, p. 12 (reuse beats originality in construction). The source presents this as a parallel drawn from a metaphor, not as a stated rule. The sign, the assignment of neighbouring cases, the repair, the reasoning in terms of accidental complexity, the three added exceptions and the pseudocode are this wiki's own.
