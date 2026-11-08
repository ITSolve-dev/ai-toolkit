---
title: One side effect per statement
category: functions
summary: "An expression that changes a variable (++, --, an assignment, a mutating call) and also reads that same variable elsewhere in the same expression, such as print(++n, n + 2) or values[i++] + values[i], or packs several mutations into one expression; a side effect in a loop condition is loop-header-holds-only-control."
tags: [rule, side-effects, expressions, evaluation-order, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell's rule (section 31.5, pp. 743-745) is that an expression should not do several operations on one line when some of them have side effects. He defines a side effect as a consequence of evaluating an expression beyond its main result, for example an increment on a line with other operations, or an assignment whose left side is then used in a condition (p. 743). The chapter is about formatting, but the defect underneath is about meaning: the reader cannot tell what the statement computes, and sometimes neither can the language.

## Rule

Put each side effect in its own statement, before or after the expression that uses its result. This wiki reads that, for review, as: do not mutate a variable and read it again inside the same expression (pp. 743-744).

The source gives three reasons:

- **Undefined or surprising order.** In `PrintMessage( ++n, n + 2 )` with `n` equal to 4, the first argument is 5. C++ does not fix the order in which arguments are evaluated, so the second argument can be 6 or 7 depending on the compiler, and the book's answer to which it is reads «Ни то, ни другое и не третье» (p. 743).
- **Recognising instead of reading.** A compact copy loop in the shape of `strcpy` looks familiar, so experienced readers name it and move on: «вы узнали код, а не прочитали его» (p. 744). The book's version holds a bug that is plain once it is written one operation per line (p. 744). That case sits in a loop condition and is owned by [[loop-header-holds-only-control]].
- **No speed gain.** The compact copy loop was 11% slower than the plain one when profiled (p. 744); the book adds that results vary between compilers and that clarity comes first until a gain is measured (pp. 744-745). The same section adds that today's optimising compilers need no hints from layout (p. 743).

The source also argues for the reader: most programmers have to think twice to understand expressions with side effects, and that attention is better spent on what the code does as a whole (p. 745).

## Sign in code

- A variable incremented, decremented or assigned inside an expression that also reads that variable: two arguments of one call, two operands of one operator, or an index together with the value it indexes.
- An assignment embedded in a larger expression, where the assigned variable is then used again in the same expression.
- Two or more mutations in one expression, outside a loop header.

This wiki assigns the neighbouring cases as follows. This page owns side effects inside an ordinary expression. A side effect inside a loop condition, or a loop with an empty body whose condition does the work, is [[loop-header-holds-only-control]]. A side effect inside an assertion's condition is [[assertion-side-effects]]; side effects inside an ordinary expression are [[one-side-effect-per-statement]]. A method that both changes state and returns a value is [[command-query-separation]].

## When not to apply

This wiki's own limits, not stated by the source:

- A single side effect whose result is used once, with no other read of the variable in the expression (`x = next()`, then a call that uses only `x`), has no ordering problem. Splitting it changes nothing a reader needs.
- Where a language guarantees left-to-right evaluation, the order half of the reasoning does not hold; the reading half still does. How the language evaluates is decided at work time.
- In purely functional code there are no side effects to separate, and the rule has nothing to say.

## Repair

Move each mutation into its own statement next to the expression, then let the expression use the already-updated value (p. 744). Check that the order of the separated statements is the one intended; writing it out is exactly where a hidden off-by-one shows.

## Before and after

```
print_pair(++n, n + 2)          // second argument depends on evaluation order
total = values[i++] + values[i]
```

```
n = n + 1
print_pair(n, n + 2)

total = values[i] + values[i + 1]
i = i + 1
```

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, section 31.5, on one statement per line and on avoiding several operations on one line in C++, pp. 743-745. See [[code-complete]].
- The source frames the rule for C++. This wiki records it as the source states it; applying it to another language's evaluation rules is decided at work time.
- Quotations were transcribed from the extracted text and need the page-image check.
- This wiki's own: the review reading of the rule (no mutate-and-read in one expression), the signs' wording, the assignment against neighbouring pages, the limits, and the pseudocode.
