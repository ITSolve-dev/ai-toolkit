---
title: A cache must earn its complexity
category: complexity
summary: "A function or object keeps remembered results (cachedX or lastX fields, a memo map, a lazily filled table) in front of a computation no costlier than the lookup, or with no comment, test or benchmark showing that the same inputs recur, or keyed on fewer inputs than the result depends on."
tags: [rule, caching, memoization, optimization, state]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Caching keeps some values so that the ones used most often are cheaper to get than the rest (p. 614). McConnell shows a hypotenuse function that remembers its last arguments and result, and states the cost plainly: the second version is more complex and larger than the first, so it «должна обосновать свое право на жизнь быстродействием» (p. 615). He ends the subsection with the warning that caching, like other optimizations, complicates code and «часто оказывается источником ошибок» (p. 615).

## Rule

Add a cache only where it pays, and judge that by the factors McConnell lists (p. 615):

- the more expensive it is to produce a new item, the more a cache pays;
- the more often the same information is requested, the more it pays;
- the cheaper it is to look up a cached item and to store a new one, the more it pays.

Caches that keep more than one item cost more again (p. 615). Like any tuning, the gain must be measured ([[premature-code-tuning]]); his own figures for the hypotenuse cache assume that the same values recur (p. 615).

## Sign in code

A function or object holds remembered inputs and outputs next to the computation: fields named `cached…` or `last…`, a map from arguments to results, or a table initialised empty and filled on first request (McConnell describes that lazy variant of a precomputed table as one form of caching, p. 622). One of the following also holds:

- the computation it guards costs no more than the cache check and store themselves (a field read, a constant, a single comparison);
- no comment, test, benchmark or call site beside the cache shows the repetition it relies on;
- the cache key omits an input the result depends on, so a call with that input changed returns a stale result.

This wiki assigns the neighbouring shapes as follows. This page owns the cache shape. Every other speed-motivated indirection is [[premature-code-tuning]]. A stored value derived from other fields of an object, kept in step by hand, is [[stored-derived-data]]. A memo over a call whose result can change between calls with the same arguments is [[immutable-versus-constant-object]]; this page owns a memo whose key omits an argument.

## When not to apply

- The guarded computation is expensive (disk or network access, a heavy formula) and requests repeat. McConnell's examples are records read randomly from disk, and character widths in a font renderer, where caching the last width roughly doubled display speed (p. 614).
- A measurement in the real setting shows the gain.
- The cache comes from a library or runtime that owns invalidation, and is used as documented. This wiki's reading is that the bug risk the source warns about lies in hand-written cache state.

## Repair

1. Remove the cache and measure the plain version.
2. If the cache stays, keep its state in one place with one responsibility, so the computation stays readable without it. That separation is this wiki's suggestion, not McConnell's. Where the project follows *Elegant Objects*, the one place is a caching decorator ([[constructors-without-code]]).
3. Check what the cache keys on, and add every input the result depends on. This failure is this wiki's example of the bugs the source warns about.

## Before and after

Before: the book's own hypotenuse cache paid 2-4x when inputs repeated (p. 615); here it is a violation only because nothing beside it shows that they do.

```
class Geometry:
    cachedResult = 0
    cachedA = 0
    cachedB = 0

    hypotenuse(a, b):
        if a == cachedA and b == cachedB:
            return cachedResult
        cachedResult = sqrt(a*a + b*b)
        cachedA = a
        cachedB = b
        return cachedResult
```

After:

```
function hypotenuse(a, b):
    return sqrt(a*a + b*b)
```

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, section 26.3: definition and examples of caching, p. 614; the hypotenuse cache, the factors that make caching pay, its complexity and bug risk, p. 615; section 26.4: lazy table filling as caching, p. 622. See [[code-complete]].
- Quotations were transcribed from the extracted text with line-break hyphens joined, and need the page-image check.
- This wiki's own: the sign and its three conditions, the assignment against neighbouring pages, the library-cache limit, repairs 2 and 3 (the decorator setting from [[elegant-objects]] included), and the pseudocode pair. In the book the cached version is the optimized "after", measured faster when inputs repeat (p. 615); this page reverses the direction for the case with no such evidence.
