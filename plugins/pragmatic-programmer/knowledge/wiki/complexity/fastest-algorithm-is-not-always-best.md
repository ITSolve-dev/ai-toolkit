---
title: The fastest algorithm is not always the best
category: complexity
summary: "A hand-written elaborate algorithm or a structure with high setup cost over a small bounded collection, or a speed-motivated change of algorithm or structure with no measured bottleneck behind it."
tags: [decision-rule, algorithms, premature-optimization, performance, trade-offs]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Asymptotic order decides at scale, and at small scale other costs decide. This test chooses between a simple algorithm and an asymptotically faster one. It is the counterweight to [[estimate-algorithm-order]]. Its neighbour is [[premature-code-tuning]], and the two share a selection condition: if the speed-motivated change replaces one algorithm or data structure with another, this page owns it; if the algorithm stays the same and only its statements are rewritten for speed, [[premature-code-tuning]] owns it. A precomputed table standing in for a closed-form computation counts as a statement-level rewrite, because the algorithm's result and order are unchanged. Which level a measured slowness should be fixed at is [[fix-performance-at-the-right-level]].

## Rule

Pick the algorithm that fits the actual input, and spend effort on speed only where a bottleneck has been confirmed. The book's statement is that «самый быстродействующий алгоритм далеко не всегда оказывается наилучшим» (p. 257).

The test has three questions:

1. **Is the input small or bounded?** On a small input, plain insertion sort beats quicksort and takes less time to write and debug (pp. 257-258).
2. **Is setup expensive?** On small inputs, setup cost can cancel the run-time advantage and make the algorithm impractical (p. 258).
3. **Has this code been shown to be the bottleneck?** The book warns against premature optimisation and asks you to confirm the algorithm is a bottleneck before spending time on it (p. 258).

If the input is small or setup dominates, the simple option wins. If the bound is external and the code is a confirmed bottleneck, the faster option earns its cost.

## Sign in code

- A hand-written sort, search or index over a collection whose size is visibly fixed or small in the code.
- A structure that is costly to build (a tree, an index, a compiled table) created for a few elements or rebuilt on every call.
- A comment or commit message that claims speed for a choice of algorithm or structure and cites no measurement.
- A routine rewritten for speed that the library already offers. The book expects library sorts to beat what you could write without substantial effort (p. 256).

Where a hand-written component that the library already offers claims speed, [[fastest-algorithm-is-not-always-best]] owns it; where no reason is stated, [[use-existing-components-before-writing-your-own]] owns it.

## When not to apply

- The input size is set outside the code and can grow. Then the order matters first ([[estimate-algorithm-order]]).
- A profile or measurement names this code as the bottleneck.
- The simple option is not simpler here, because the library already provides the fast one at the same call cost.

## Repair

1. Replace the elaborate algorithm with the library routine, or with the simplest loop that does the job.
2. If speed is claimed to matter, measure first, on real input.
3. Keep the faster version only where the measurement supports it, and record the figure next to it.

## Before and after

```
// before: four settings, sorted once at startup
function sortSettings(items):
    tree = new BalancedTree(compareByName)
    for item in items:
        tree.insert(item)
    return tree.inOrder()
```

```
// after
function sortSettings(items):
    return sorted(items, by: "name")
```

## Source

[[pragmatic-programmer]], Topic 39, pp. 256-258, for the insertion sort case, setup cost, premature optimisation and library routines. The three-question form, the signs, the selection condition against [[premature-code-tuning]] and its reading of precomputed tables, the split with [[use-existing-components-before-writing-your-own]], the limits, the repair and the example are this wiki's own.
