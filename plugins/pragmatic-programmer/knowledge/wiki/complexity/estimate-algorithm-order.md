---
title: Estimate algorithm order
category: complexity
summary: "A nested loop or a linear search inside a loop whose bounds come from input sizes set outside the code: batch record counts, user lists, rows returned."
tags: [rule, algorithms, big-o, performance, scaling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Most non-trivial code processes input of variable size, and the size of that input decides whether it stays usable. Big-O notation describes how time, memory or another resource changes as input grows. It gives no absolute figures: one O(n²) algorithm can be 1000 times faster than another, and the notation cannot show this (p. 253).

## Rule

Know the order of code with loops or recursion, estimate it deliberately where input can grow, and then check the estimate. The book says this check is usually quick and informal, and that a more detailed analysis is needed only sometimes (p. 253). The book's two tips are «Оценивайте порядок производительности своих алгоритмов» (p. 256) and «Проверяйте свои оценки» (p. 257).

The deciding question in the book is about bounds. Faced with a loop inside a loop, ask how large the data can get. If it is bounded, you can work out how long the code takes. If its size depends on external factors, such as records in a nightly batch or names in a list of people, stop and consider what large inputs do to run time and memory (p. 256).

The book's common-sense shapes (pp. 255-256):

| Shape in code | Order |
|---|---|
| Simple loop from 1 to n | O(n) |
| Nested loops with limits m and n | O(m × n) |
| Halves the set at each step | O(lg n) |
| Splits input into two independent halves, processes each, then combines | O(n lg n) |
| Considers permutations | factorial, can run out of control |

Big-O is not only for time: it can describe any resource, and modelling memory is often useful (p. 254). The book says an algorithm gets out of hand once it passes O(n²) (p. 254). Permutations show why: six elements take six times as long as five, and seven take 42 times as long (p. 256).

## Sign in code

- A loop nested in a loop, where both limits are the sizes of collections that arrive as input.
- A linear search, or a call that performs one, inside a loop over the same or another input.
- Recursion that enumerates orderings or subsets.
- A loop whose hidden cost sits in a call, where the called routine itself iterates.

The sign shows the shape. Whether the input can grow large depends on where the bound comes from, which the reader must trace to its source. Where that source is out of view, the page says so and gives no verdict.

This wiki assigns the neighbouring case as follows. Where the same path also carries statement-level tweaks for speed, the mismatch is [[fix-performance-at-the-right-level]]; a plain linear search or nested loop over input-sized data is [[estimate-algorithm-order]].

## When not to apply

- The bound is fixed and small. Then the book says simply estimate the run time (p. 256).
- Input is small enough that constants decide. A simple O(n²) loop can beat a complex O(n lg n) loop for small n, especially if the latter has an expensive inner loop (p. 257). See [[fastest-algorithm-is-not-always-best]].
- The worst case is unrepresentative. Quicksort is formally O(n²) with average time O(n lg n) (p. 256).

## Repair

1. For an O(n²) algorithm, the book suggests looking for a divide-and-conquer approach that reaches O(n lg n) (p. 257).
2. When the inner loop is only a search, this wiki's usual repair is to build a keyed lookup once.
3. If you do not know the behaviour, measure it. Run the code on small inputs and plot the results. Three or four points are usually enough to see whether the curve bends upward, stays straight or flattens (p. 257).
4. If timings are hard to obtain, use a profiler to count operations and plot those against input size (p. 257).
5. Try realistic input shapes. A sort tested on random data can surprise you on ordered data, and input that looks linear when small may not stay so at millions of records (p. 257). The book holds that in the end only timing in real production with real data counts (p. 257).
6. For intractable problems (travelling salesman, bin packing, set partition), the book says domain heuristics are often used to cut the run time (p. 256).

## Before and after

```
// before: O(orders × customers)
for order in orders:
    for customer in customers:
        if customer.id == order.customerId:
            order.owner = customer
```

```
// after: O(orders + customers), at the cost of memory for the map
byId = mapBy(customers, "id")
for order in orders:
    order.owner = byId[order.customerId]
```

## Source

[[pragmatic-programmer]], Topic 39, pp. 252-258. The signs beyond nested loops, the split with [[fix-performance-at-the-right-level]], repair step 2 and the example are this wiki's own.

This wiki omits two of the book's worked figures. For a routine taking 1 s on 100 records, the book gives about 3 s for O(lg n) and 33 s for O(n lg n) at 1000 records (p. 254); scaling from that baseline gives 1.5 s and 15 s. The book also lists binary tree traversal as O(lg n) (p. 255). This wiki reads that as a descent from root to leaf, because visiting every node is O(n). The extracted text of the table on p. 255 has lost the O(n²) row to recognition noise; the row's description survives.
