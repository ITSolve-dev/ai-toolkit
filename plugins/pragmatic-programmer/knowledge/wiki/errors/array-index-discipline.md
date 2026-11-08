---
title: "Keep array indexes in bounds, in order and uncrossed"
category: errors
summary: "An index computed by arithmetic with no length check, a loop over an array compared with <= against its length or bounded by a hard-coded number, a multidimensional access a[i][j] where a[j][i] was meant, or nested loops where one index leaks into the other's position."
tags: [rule, arrays, off-by-one, indexes, loops]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* traces every array problem to random access: an element can be reached by any index, and the most common failure is an index outside the array, which some languages report and others answer with strange results (Russian edition, pp. 301-302). Its advice narrows that freedom and checks the places where it fails.

## Rule

- **Keep every index within bounds** (p. 301).
- **Consider sequential access instead.** The book reports the argument of Mills and Linger that «произвольный доступ к массиву похож на случайные операторы goto» (p. 302), and their finding that a design using sets, stacks and queues needed fewer variables and fewer references to them. Its advice is to consider sequential containers before choosing an array.
- **Check the endpoints.** Ask whether the code reaches the first element or the one before or after it, whether the last element is off by one, and whether the middle is reached correctly (p. 302). The same applies to substrings indexed like arrays (p. 289).
- **Check index order in multidimensional arrays.** `Array[i][j]` is easy to write for `Array[j][i]` (p. 302).
- **Watch for index cross-talk.** In nested loops it is easy to write `Array[j]` for `Array[i]` (p. 302).
- For the last two the book's repair is the same: index names more meaningful than i and j where the purpose is not obvious (p. 302).
- **Take the upper bound from the array**, not from a separate constant, so adding or removing elements cannot leave the bound stale. The book gives this for C, through a macro (pp. 302-303); this wiki extends it to any language that can report an array's length.

## Sign in code

- An index computed by arithmetic (`a[i + offset - 1]`) rather than produced by iteration, with no check against the length.
- A loop over an array with `<=` against the length, a start at 1 in a zero-based language, or a hard-coded upper bound beside an array whose size is set elsewhere.
- Nested loops over a two-dimensional array where the inner body indexes with the outer variable, or swaps the order of indexes between accesses.
- A loop bound taken from a constant while the array is initialised from a literal list whose length can change.

This wiki assigns neighbouring cases as follows. This page owns the index expression and a loop compared directly against the array's length or a hard-coded number. Where a literal bounds a loop that indexes an array, this page owns it and the repair takes the bound from the array; a literal elsewhere is [[named-constants-over-literals]]. An index walked only to read each element in order is [[for-or-while]]. Where the bound is a variable whose name hides whether it is inclusive, [[range-bound-names]] owns the sign. The single-letter names themselves (`i`, `j` in nested loops) are [[loop-index-names]], and so is an inner loop reusing an index name an enclosing loop already uses; this page owns an index that is crossed or reversed between accesses. Boundary cases as test design are [[test-boundaries-and-realistic-use]].

## When not to apply

The book states no limits here. The limits below are this wiki's own:

- **Iteration without indexes** (for-each, map, fold) removes the endpoint, order and cross-talk signs altogether; it is the preferred repair, not an exception.
- **Algorithms that need random access** (binary search, matrix arithmetic, dynamic programming tables) cannot be made sequential; there the rule is the endpoint and order checks, not the container advice.
- **i and j are conventional** for short loops over a matrix whose rows and columns are obvious; the naming repair fires when the dimensions have meanings (row and seat, month and region).

## Repair

1. Where the code only walks the collection, replace indexing with iteration or a sequential container; [[for-or-while]] owns that choice of loop form.
2. Where indexing stays, take bounds from the array itself and write the loop in the half-open form the language uses.
3. Check the first, last and a middle element by hand, or with a test at each.
4. In nested loops over multidimensional data, name indexes after their dimension and keep their order the same at every access.

## Before and after

```
for i = 0 to 11
  for j = 0 to REGIONS - 1
    total[j] = total[j] + sales[j][i]

for k = 0 to 15
  use(ratios[k])
```

```
for month in 0 ..< length(sales)
  for region in 0 ..< length(sales[month])
    total[region] = total[region] + sales[month][region]

for ratio in ratios
  use(ratio)
```

In the before, `sales[j][i]` reverses the order used where `sales` is filled by month first; the after names the dimensions so the order can be checked by reading.

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: off-by-one in substrings, p. 289; arrays, bounds and the source of array errors, pp. 301-302; Mills and Linger on sequential access, p. 302; endpoints, multidimensional order and index cross-talk, p. 302; deriving the bound from the array, given by the book only as a C macro, pp. 302-303. The quotation of p. 302 is transcribed from `raw/` and needs the page-image check. This wiki's own: the extension of that bound rule beyond C, the signs as worded, all limits, the iteration repair, the split with neighbouring pages, and the pseudocode. The book's C-specific macro is not carried.
