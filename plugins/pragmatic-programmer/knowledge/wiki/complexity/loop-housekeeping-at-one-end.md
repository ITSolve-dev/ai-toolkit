---
title: Keep loop housekeeping at one end of the body
category: complexity
summary: "The per-pass updates of a loop's counters and accumulators (count++, total += ...) are scattered through the middle of its body, interleaved with the work, instead of gathered at the start or the end."
tags: [rule, loops, proximity, housekeeping]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A loop has three kinds of code: the setup it needs before the first pass, the work it does, and its housekeeping, the statements that prepare the next pass, such as `count++`. McConnell asks that the housekeeping sit together at one end of the body (p. 368). He grounds the placement of the setup in the principle of proximity: related statements kept together are not missed when the code changes (p. 366). This wiki reads the housekeeping advice the same way.

## Rule

- «Располагайте служебные операции либо в начале, либо в конце цикла» (p. 368). As a rule, the variables initialized before the loop are the ones the housekeeping manipulates (p. 369), so the setup above the loop and the housekeeping at one end of it point at the same variables.

Where the setup belongs, directly before the loop, is [[initialize-close-to-first-use]], which owns that half of the book's advice.

## Sign in code

- Increments of loop counters or accumulators appear at several places in the middle of the body, interleaved with the work.

This wiki assigns the neighbouring cases as follows. A counter or accumulator initialized far above its loop, or not reset when an outer loop is added, is [[initialize-close-to-first-use]]. A counter updated in the `for` header without controlling the loop is [[loop-header-holds-only-control]]. A jump into a loop body other than through its top is [[loop-with-exit-in-the-middle]], which owns it with the book's "enter only from the top" advice (p. 366).

## When not to apply

- An accumulator that is the work itself, as when the only purpose of the body is to add to a total, has no separate housekeeping to move. This limit is this wiki's own.

## Repair

1. Gather the per-pass updates into one block at the end of the body, after the work, or at the start. If the body has a top-of-loop `continue`, put the housekeeping at the start, before the guard, or the `continue` skips it.
2. Check that each variable updated there is initialized directly above the loop ([[initialize-close-to-first-use]]).

## Before and after

```
count = 0
total = 0
while not input.atEnd():
    name = input.next()
    count = count + 1
    names.append(name)
    total = total + length(name)
    log(name)
```

```
count = 0
total = 0
while not input.atEnd():
    name = input.next()
    names.append(name)
    log(name)
    // prepare next pass
    count = count + 1
    total = total + length(name)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.2: housekeeping, pp. 368-369; proximity as the reason for placing the setup, p. 366. The reading of the housekeeping advice through proximity, the limit, the `continue` note in repair step 1, the assignment against the neighbouring pages, repair step 2 and the pseudocode are this wiki's own. Entry from the top (p. 366) is owned by [[loop-with-exit-in-the-middle]]. The initialization half of the same advice (p. 366) is merged into [[initialize-close-to-first-use]].
