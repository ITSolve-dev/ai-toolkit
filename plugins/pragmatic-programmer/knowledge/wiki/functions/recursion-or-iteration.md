---
title: Recursion or iteration
category: functions
summary: "A routine recursing over a linear sequence where each call does one step and makes one self-call (factorial, Fibonacci, summing a list): a loop is clearer. Backtracking or branching search is where recursion pays."
tags: [decision-rule, recursion, iteration]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell holds that recursion is rarely necessary, elegant on a small class of problems and confusing on most (p. 385 of [[code-complete]]). For a small group of problems it gives simple, elegant solutions. For a slightly larger group it gives solutions that are simple, elegant and hard to understand. «Для большинства задач она создает исключительно запутанные решения» (p. 385). His closing lesson is to consider both before choosing: «Но прежде чем выбрать какой-то один, надо рассмотреть оба» (p. 389). How to make recursion safe once chosen is on [[recursion-safeguards]].

## Rule

Use recursion selectively. Choose it when a small part of the problem is easy to solve and the problem splits easily into smaller parts of the same shape (p. 385). His good examples are quicksort, which splits the range in two and recurses on each half, and a maze search, which tries every turn and backtracks; for the maze, «альтернативное решение было бы гораздо более трудоемким» (p. 387). His bad examples are factorial and Fibonacci, which he calls silly uses of recursion (p. 388). Of factorial he adds that the recursive version is slow, uses memory unpredictably, and is harder to understand than the loop (p. 389).

## Sign in code

This is the discriminating criterion that decides between the two courses. This wiki derived it from the book's two sets of examples.

- **Iteration wins:** each call makes at most one self-call over a linear sequence, so the recursion only replaces a counter (factorial, a running sum, walking a list); or its self-calls recompute overlapping subproblems (Fibonacci written as two self-calls), which a loop computes without the repeated work.
- **Recursion wins:** a call branches into self-calls over disjoint parts, as in divide-and-conquer, tree descent or backtracking search. Here the iterative version has to maintain its own stack of pending work.

## When not to apply

- In functional code where recursion is the language's way of looping, and accumulator recursion or a fold is the idiom, the linear case is not a defect. This wiki adds this limit. The book argues within imperative languages and does not address it. There, prefer a library fold or map over hand recursion, where one exists.

## Repair

Replace linear self-recursion with a loop that carries the intermediate result in a variable. Leave branching recursion in place and check it against [[recursion-safeguards]].

## Before and after

```
factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)
```

```
factorial(n):
    result = 1
    for factor from 2 to n:
        result = result * factor
    return result
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 17.2, pp. 385-389: [[code-complete]]. The Fibonacci reasoning (overlapping subproblems) is this wiki's; the book only names Fibonacci as a silly example. The verdicts on quicksort, the maze, factorial and Fibonacci, and the advice to consider both options, are the book's. The criterion of one self-call versus several, the functional-language limit, and the pseudocode are this wiki's own.
