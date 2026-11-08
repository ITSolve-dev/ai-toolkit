---
title: One loop, one job
category: complexity
summary: "A single loop body that computes two or more unrelated results from the same iteration (e.g. totals and a validation report and a rewrite of the items), whose statement groups share only the loop variable."
tags: [rule, loops, cohesion, premature-optimization]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell applies routine cohesion to loops: «Заставьте каждый цикл выполнять только одну функцию» (p. 369). The fact that a loop can do two things at once is not enough to justify combining them.

## Rule

Loops should be like routines: each does one thing and does it well (p. 369). If two loops where one would do seems inefficient, McConnell's procedure is: write the two loops, comment that they could be combined for efficiency, and wait until benchmarks show a problem in that spot. Only then combine them (p. 369).

The tuning chapter names the fused form as a technique, loop jamming: merging two loops that run over the same set of elements to save the loop overhead (pp. 603-604). It usually requires the two loops to have the same bounds; its measured savings were 28% in C++, 32% in PHP and 4% in Visual Basic (pp. 603-604). McConnell names two main risks: the indices of the two jammed loops may later change and stop being compatible, and jamming is sometimes hard, so check first that it does not break other code (p. 604). Like every technique in that chapter it is kept only with a measurement; see [[premature-code-tuning]], which routes the jammed-loop shape to this page.

Fowler's Split Loop agrees: programmers write a loop that does two things "just because they can do that with one pass", and anyone who modifies it then has to understand both (*Refactoring*, 2nd ed., ch. 8, PDF p. 257). Split, each loop can be understood, and later extracted, alone. He adds a second gain: "A loop that calculates a single value can just return that value", whereas a loop that does many things must return a structure or fill local variables (p. 257). He usually follows Split Loop with Extract Function, and then often with [[replace-loop-with-pipeline]] or [[substitute-algorithm]] (pp. 257, 260); the point of the split "isn't what it does on its own but what it sets up for the next move" (p. 259). On the cost of the second pass his answer matches McConnell's: separate refactoring from optimisation, and "if the loop traversal is a bottleneck, it's easy to slam the loops back together" (p. 258). He adds that iteration itself is rarely the bottleneck, and that the split often enables more powerful optimisations (p. 258).

This wiki adds the reasoning. A fused loop ties together two computations that have different reasons to change, and the index, the termination test and the early exits now serve both. A `break` added for one job silently truncates the other.

## Sign in code

- One loop body whose statements fall into two or more groups that share only the iteration variable: each group reads its own inputs and writes its own outputs, and neither reads what the other writes.
- An early exit (`break`, `return`) inside such a loop that is correct for one group and cuts the other group short.

This wiki assigns the neighbours as follows. A loop that is too long or too deep, whatever it computes, is [[loop-length-and-nesting]]. Several exits in a loop that does one job are [[break-and-continue]]. Where the interleaved independent statements sit in one loop body and each group could run as its own loop, [[one-loop-one-job]] owns it; interleaving in straight-line code is [[keep-variable-live-time-short]]. A loop whose body only filters, maps or accumulates one collection is [[replace-loop-with-pipeline]]. A loop that does that alongside other work is split first under [[one-loop-one-job]], and an accumulator taken out of such a loop follows the procedure in [[remove-loop-accumulator]].

A loop body computing unrelated results is [[one-loop-one-job]], which owns the shape; where speed is the stated reason for keeping it fused and no measurement backs that, [[refactor-first-tune-afterwards]] answers the reason. The procedure that splits such a loop without breaking it is [[remove-loop-accumulator]].

## When not to apply

- The jobs share an intermediate value per element that is expensive to recompute, or the sequence can be traversed only once (a stream, a network read). This wiki's own limit: fuse them then, and say why in a comment. McConnell's own condition is a benchmark showing the problem (p. 369), which the next bullet carries.
- A profile has shown the double pass to be a problem (p. 369; Fowler, p. 258).
- The groups are steps of one computation, where the second consumes what the first produces for the same element. This wiki reads that as one job.

## Repair

1. Split the body by output: one loop per result.
2. Give each loop its own early exit, if it needs one.
3. Where splitting is rejected for performance, leave the fused loop with a comment naming the measurement that justified it.
4. Where the language allows, express each job as its own pass (filter, map, reduce). This step is this wiki's addition (see [[decompose-into-transformations]]).

Fowler's mechanics for step 1 (pp. 258-259): copy the loop; in each copy remove the side effects that belong to the other computation (statements without side effects can stay in both for now); test; then slide each accumulator's initialisation next to its loop ([[slide-statements]]) and consider Extract Function on each.

## Before and after

```
// before
total = 0
errors = []
for item in items:
    total = total + item.price
    if item.qty < 0:
        errors.add(item.id)
        break                 // meant for validation, also stops the total
```

```
// after
total = 0
for item in items:
    total = total + item.price

firstBad = none
for item in items:
    if item.qty < 0:
        firstBad = item.id
        break
// could be fused for speed; not needed per profile
```

Fowler's example, split and then extracted:

```
// before
youngest = people.isEmpty() ? INFINITY : people[0].age
totalSalary = 0
for p in people:
  if p.age < youngest: youngest = p.age
  totalSalary = totalSalary + p.salary
return format(youngest, totalSalary)
```

```
// after
return format(youngestAge(people), totalSalary(people))

totalSalary(people): return sum(people.map(p -> p.salary))
youngestAge(people): return min(people.map(p -> p.age), default: INFINITY)
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 16.2, p. 369; ch. 26.2, pp. 603-604, for loop jamming and its risk. [[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 8, Split Loop, PDF pp. 256-260: the reader's cost, the single-value gain, the follow-up refactorings, the bottleneck answer and the mechanics; the second pair follows the book's example in this wiki's pseudocode. The reasoning about shared exits, the signs, the neighbour assignment, the first and third limits, repair step 4 and the pseudocode are this wiki's own.
