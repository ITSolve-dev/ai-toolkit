---
title: Do not use the loop index after the loop
category: complexity
summary: "Code after a for loop reads that loop's own control index (if i < MAX ...) to learn whether or where the loop stopped; set a variable named for the fact inside the loop instead."
tags: [rule, loops, loop-index, scope, off-by-one]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The final value of a loop index depends on how the loop ended and, in some languages, on the implementation. McConnell treats reading it after the loop as a defect waiting for a maintainer: «Использование значения индекса цикла после его завершения — дурной тон» (p. 370).

## Rule

- Do not write code that depends on the index's last value. That value varies between languages and implementations, and between normal and abnormal exit. Even if you know it, the next reader has to work it out (p. 370). Instead, inside the loop at the right moment, assign whatever the later code needs to a variable of its own (p. 370).
- Limit the visibility of loop indexes to the loop itself, by declaring the index in the loop header where the language allows (p. 376). McConnell notes that Ada made a `for` index unusable outside its loop because cross-talk and use outside the loop were such important problems (p. 376). McConnell adds that compilers of his time disagreed on header-declared scope (p. 377); where the language definition does not settle it, see [[rely-only-on-documented-behaviour]].

McConnell's example is a search over records followed, much later, by `if (recordCount < MAX_RECORDS) return true`. That test looks as if it checks the whole range, and it is easy to get wrong by one, because it is hard to remember whether the index was incremented after the last pass (p. 370). The rewrite sets `found = true` before `break` and returns `found`, and he adds that, as often happens with a helper boolean, the result is clearer (pp. 370-371).

## Sign in code

- An expression after a `for` loop that compares or uses that loop's control index, typically against the loop bound, to decide whether the loop found something or exited early.

This wiki assigns the neighbouring cases as follows. A `for` index declared outside its loop and not read after it is [[smallest-scope-first]]; one read after the loop is [[do-not-use-loop-index-after-loop]]. This page owns a `for` loop's own control index, whose final value depends on the language and on how the loop ended, read after the loop. A counter that the loop body itself increments holds a count by construction and may be read after the loop; its name is [[loop-index-names]].

## When not to apply

- The language or a documented API defines the final value and the index is the natural result, such as a search routine that returns the found position directly. The return then names it. This limit is this wiki's own.

## Repair

1. Introduce a variable named for the fact the later code needs (`found`, `foundAt`, `firstInvalid`).
2. Set it inside the loop at the moment the fact becomes true, before any `break`.
3. Replace the post-loop index test with that variable.
4. If the index is then declared wider than the loop, narrowing it is [[smallest-scope-first]]'s repair.

## Before and after

```
for i = 0; i < MAX; i++:
    if entry[i] == wanted: break
...                               // much code
return i < MAX
```

```
found = false
for i = 0; i < MAX; i++:          // i scoped to the loop
    if entry[i] == wanted:
        found = true
        break
...
return found
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.2: the final index value, pp. 370-371; the scope of the index, pp. 376-377. The limit, the assignments against [[loop-index-names]] and [[smallest-scope-first]], and the pseudocode are this wiki's own; the pseudocode condenses the book's example.
