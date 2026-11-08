---
title: Loop indexes get descriptive names once the loop is long, nested, or the index outlives it
category: naming
summary: "i, j, k in nested loops or loop bodies longer than a few lines (score[i][j], transaction[j][i][k]); an inner loop reusing an index name an enclosing loop already uses (index cross-talk); a counter read after the loop under a single-letter name; or i/j/k used for anything other than a simple loop index."
tags: [rule, naming, loops, loop-index, nesting]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

`i`, `j` and `k` are the conventional loop indexes, and McConnell accepts them for a simple loop of a few lines (*Code Complete*, Russian edition, pp. 257–258). He names three cases that call for a real name, plus one prohibition, and returns to the subject in the chapter on loops (pp. 375–376).

## Rule

- **The variable is used after the loop.** Give it a name for what it ends up holding. In the book's example, the number of records read becomes `recordCount` (p. 258).
- **The loop is longer than a few lines.** McConnell says the meaning of `i` is easily forgotten in a long loop. Since code is often changed, extended and copied into other programs, he notes that many experienced programmers avoid names like `i` altogether (p. 258).
- **Loops are nested.** Longer index names prevent swapping `i` for `j`, and `score[teamIndex][eventIndex]` says more than `score[i][j]` (p. 258). In chapter 16 he sums `transaction[j][i][k]` under loops named `i`, `j`, `k` and asks whether a reader who knows the declaration can tell the subscripts are in the right order; renamed, the subscript reads `transaction[month][payCodeIdx][divisionIdx]`. The computer reads both versions equally well, but the primary audience is people (p. 375).
- **Meaningful names prevent index cross-talk.** Habitual `i`, `j`, `k` raise the risk of «пересечения индексов»: one index name used for two purposes, as when an inner `for` reuses the `i` of the loop two levels up (pp. 375–376). His threshold there: avoid `i`, `j` and `k` if the loop body has more than a couple of lines, might grow, or is part of a group of nested loops (p. 376).
- **i, j, k for loop indexes only.** Using these names for anything else confuses other programmers (p. 258).

## Sign in code

- Two or more nested loops whose indexes are single letters, especially where an expression subscripts more than one dimension (`grid[i][j]`, `rows[j][i]`).
- An inner loop that assigns to an index variable already used by an enclosing loop.
- A counter the loop body maintains, read after the loop under a single-letter name.
- A loop body longer than a couple of lines that still refers to `i`.
- `i`, `j` or `k` declared for something that is not a loop index: a count, a flag, a temporary value.

This wiki assigns the neighbouring cases as follows. This page owns `i`, `j`, `k` and other single-letter loop indexes, and an inner loop reusing an index name an enclosing loop already uses. `i`, `j` or `k` bound to anything other than a loop index is [[loop-index-names]]; another conventional short name bound against its convention (an error name holding a count) is [[follow-local-naming-culture]]. Any other short name on a wide scope is [[name-length-matches-scope]]. An index that is crossed or reversed between accesses (`sales[j][i]` where `sales[i][j]` was meant) is [[array-index-discipline]], and a bound variable whose name hides whether it is inclusive is [[range-bound-names]].

The two chapters meet on reading an index after its loop, and this wiki resolves them by who sets the final value. A counter that the loop body itself increments, as in the book's `while (moreScores())` example on p. 258, holds a count by construction: it may be read after the loop, and this page asks only that it be named for what it holds. A `for` loop's own control index, whose final value depends on the language and on how the loop ended, must not be read after the loop at all: that is [[do-not-use-loop-index-after-loop]], whatever its name.

## When not to apply

- A single loop of a few lines whose index is used only to subscript one collection: `i` is fine, per the book (pp. 258, 375–376).
- Iteration that has no index at all (for-each over elements, map/filter) needs a name for the element, not for an index. The element name follows [[name-describes-what-the-variable-represents]]. This wiki's addition.
- Mathematical code where `i`, `j` are the indexes of the formula being implemented. This wiki's reading.

## Repair

1. Rename each index after the collection or dimension it walks (`teamIndex`, `month`, `divisionIdx`), and check each subscript expression against the array's declared dimension order.
2. Rename a counter that survives the loop after the value it ends up holding (`recordCount`).
3. Rename a non-index `i` after its role.
4. Declare each index in its own loop header where the language allows it, so that reusing an enclosing loop's index becomes a redeclaration the reader, and often the compiler, can see. This is the book's advice to limit a loop index's visibility to its loop (p. 376); see [[do-not-use-loop-index-after-loop]] for why the compiler's handling is not to be relied on.

## Before and after

```
for i from 0 to teamCount - 1
    for j from 0 to eventCount[i] - 1
        score[i][j] = 0
```

```
for teamIndex from 0 to teamCount - 1
    for eventIndex from 0 to eventCount[teamIndex] - 1
        score[teamIndex][eventIndex] = 0
```

Cross-talk, in the shape of the book's p. 376 example:

```
for i in 0..payCodes:
    for j in 0..12:
        for i in 0..divisions:          // i reused by the inner loop
            sum = sum + t[j][i][k]
```

```
for payCode in 0..payCodes:
    for month in 0..12:
        for division in 0..divisions:
            sum = sum + t[month][payCode][division]
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition ([[code-complete]]): ch. 11.2, pp. 257–258, for the four rules; ch. 16.2, "Использование переменных цикла", pp. 375–376, for the `transaction` example, the people-first reason, index cross-talk, the couple-of-lines threshold and limiting an index's visibility to its loop (repair step 4). The limits for for-each iteration and mathematical code, the assignment against [[name-length-matches-scope]] and [[follow-local-naming-culture]], the resolution between the two chapters on reading an index after its loop, and the pseudocode are this wiki's own. The first pair is close to the book's nested-loop example because that example is the sign itself; the second merges the book's two chapter 16 examples.
