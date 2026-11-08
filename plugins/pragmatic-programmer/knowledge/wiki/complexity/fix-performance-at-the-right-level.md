---
title: Fix performance at the level that causes it
category: complexity
summary: "A slow path patched with statement-level tweaks (cached locals, unrolled loops) while its cost comes from a linear lookup or a file, network or database read inside the loop, a system call per object whose result is unused, or tracing left on in a release path."
tags: [decision-rule, performance, code-tuning, algorithms, design]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Code tuning is only one of several levels at which a program can be made faster, and McConnell says it is usually not the most effective, the easiest or the cheapest one (p. 576). He lists the levels as requirements, program design, class and routine design, interaction with the operating system, compilation, hardware and code tuning (p. 574). This test decides, for a slow piece of code in front of the reader, whether its repair is a tuning change or a change at a higher level. It is step 2.3 of [[code-tuning-procedure]].

## Rule

Before tuning statements, check whether the cost comes from a choice above them: the algorithm or data type, the program's interaction with I/O and the OS, or work the program does not need at all. Fix it there if so. The book's key point: speed and size depend more on architecture, detailed design and the choice of data structures and algorithms than on code efficiency (p. 593). If tuning after completion cannot reach the target, the book's diagnosis is the design, not the code: «Проблема в таких ситуациях объясняется не низким качеством кода, а неадекватной архитектурой программы» (p. 580).

This wiki orders the test as follows:

1. **Is the work needed at all?** Calls whose result the program never uses, such as a constructor reading the system clock for a field the program ignores (p. 585), or debug tracing left in a release path (p. 586). Remove them.
2. **Is it I/O or a system call inside a hot path?** Move the data into memory or batch the calls (pp. 583-585).
3. **Is it the algorithm or data type?** Quicksort for bubble sort, binary for linear search: the class and routine level is where the book places this choice (p. 575). Owned by [[estimate-algorithm-order]] and [[fastest-algorithm-is-not-always-best]].
4. Only if none of these holds is the change a code-tuning change, done under [[code-tuning-procedure]].

## Sign in code

- A slow path that contains statement-level tweaks (a length cached 'for speed', an unrolled loop, shifted indexes) while the same path contains a linear search inside a loop, a file, network or database read per iteration, or a nested loop over the same collection.
- An object created in large numbers whose constructor or base constructor makes a system call or I/O whose result is not used.
- Diagnostic logging or tracing that writes on every iteration of a loop in a release path.

This wiki assigns the neighbouring cases as follows. This page owns the mismatch between where the effort went and where the cost is. A slow path whose cost lies in I/O, a lookup or a system call rather than in the statements is [[fix-performance-at-the-right-level]]. Where the same path also carries statement-level tweaks for speed, the mismatch is [[fix-performance-at-the-right-level]]; a plain linear search or nested loop over input-sized data is [[estimate-algorithm-order]]. Statement tricks with no measured slowness at all are [[premature-code-tuning]]; an elaborate algorithm on a small input is [[fastest-algorithm-is-not-always-best]].

## When not to apply

- The higher-level choice has already been measured and ruled out, and a profile still points at the statements.
- The collection is small and bounded, so the order of the algorithm does not decide the cost ([[fastest-algorithm-is-not-always-best]]).
- The higher-level change is a requirement, hardware, or the program's architecture (how it is split into classes or subsystems). Then the finding is reported, not repaired in the code; architecture is taken as given by this charter. This limit is this wiki's own.

## Repair

Make the change at the level the test identified: delete unneeded work, move I/O out of the loop, replace the algorithm or data structure. Revert the statement-level tweaks that were standing in for it, unless a measurement keeps them.

## Before and after

```
// before: tuned statements, cost is the lookup in the loop
function attachPrices(orders, priceFile):
    for order in orders:
        n = length(order.items)            // cached 'for speed'
        for i in 0 .. n - 1:
            item = order.items[i]
            item.price = readPriceFromFile(priceFile, item.sku)
```

```
// after
function attachPrices(orders, priceFile):
    prices = loadPrices(priceFile)          // one read, a map by sku
    for order in orders:
        for item in order.items:
            item.price = prices[item.sku]
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], chapter 25: levels of performance work pp. 574-576; why code tuning is not the first choice p. 576; inadequate architecture p. 580; common sources of inefficiency pp. 583-586; key points p. 593. The levels, the examples and the key point are the book's. The ordered test, the signs, the assignments against neighbouring pages (including [[estimate-algorithm-order]]), the third limit with its reading of architecture as a setting, and the example are this wiki's own.
