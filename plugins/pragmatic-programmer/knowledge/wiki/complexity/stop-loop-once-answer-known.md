---
title: Stop a loop once the answer is known
category: complexity
summary: "A search loop that sets a found-flag (or records a position) and keeps iterating to the end of the collection although nothing after the first hit can change the result, and no break, return or flag test in the condition ends it: exit at the first hit."
tags: [rule, loops, search, early-exit, control-flow]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell's first logic technique in the tuning chapter is to stop testing as soon as the answer is known (p. 596). Inside one boolean expression, short-circuit evaluation does it automatically in languages that support it. It applies equally to loops. His example scans an input array only to learn whether a negative value is present; the loop sets `negativeInputFound = true` on a hit and goes on to the end anyway (p. 597).

He lists four exits (p. 597): a `break` after the flag is set; a `goto` past the loop where the language has no `break`; a `while` loop whose condition also tests the flag; and a sentinel. The gain depends on how many values there are and how likely a hit is (p. 598). This wiki holds that the first three exits are not tuning in the sense of [[premature-code-tuning]]: they state in the code that the loop is a search, so they need no measurement. That departs from McConnell's definition on p. 596, under which everything in the chapter is tuning; the departure is ours. The sentinel variant is tuning, and that page owns it.

## Rule

A loop whose purpose is to find whether, or where, something occurs should end at the first occurrence.

## Sign in code

- A loop over a whole collection whose body only sets a boolean flag (or records a position) under a condition.
- After the flag is set, no later iteration can change the outcome: the flag is never reset, and nothing else in the body runs for later elements.
- Neither a `break` or `return` after the assignment nor a test of the flag in the loop condition ends the loop.

This wiki assigns the neighbouring case as follows. A search loop with *no* exit at the hit is [[stop-loop-once-answer-known]]. One `break` from a short `for` that searches a bounded range is accepted; [[break-and-continue]] owns it and does not report it. A loop that already exits, but through a `done` flag threaded through `if not done` guards or through several `break`s at different depths, is [[break-and-continue]].

## When not to apply

- The loop must visit every element for another reason: it also accumulates, counts, transforms, or must report the *last* occurrence. The book's example has none of these.
- The language or library offers a search primitive (an `any`- or `find`-style call). Use that instead of a hand-written loop; which primitive is right is settled at work time from the language in use.
- Code with a timing requirement where every input must take the same time, such as a constant-time comparison of secrets. An early exit leaks information there.

All three limits are this wiki's own; the book's example simply has none of these features.

## Repair

Exit at the hit: add `break`, or `return` when the loop is the whole routine, immediately after the flag is set, or fold the flag into the loop condition (p. 597). Where a search primitive exists, replace the loop with it.

## Before and after

```
negativeInputFound = false
for i in 0 .. count-1:
    if input[i] < 0:
        negativeInputFound = true
```

```
negativeInputFound = false
for i in 0 .. count-1:
    if input[i] < 0:
        negativeInputFound = true
        break
```

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, section 26.1: stopping the test once the answer is known, pp. 596-598; the four exit options, p. 597; the dependence on the data, p. 598. See [[code-complete]].
- The book's measured savings were 14% and 29% in its test languages (p. 597). They are language-specific and not part of the rule.
- This wiki's own: classing the plain exits as non-tuning, the sign's wording, the assignment against [[break-and-continue]], and all three limits.
