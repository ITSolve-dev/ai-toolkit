---
title: Loop with the exit in the middle
category: complexity
summary: "The same statements appear just before a loop and again at the bottom of its body (a 'loop and a half'), usually producing the value the loop condition tests; or a goto jumps into the middle of a loop on its first pass: use one unconditional loop with a single exit where the test naturally falls."
tags: [rule, loops, duplication, control-flow]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A loop whose natural test falls partway through its body is often forced into a top-tested or bottom-tested shape by copying statements, which leaves two parallel copies to keep in step. McConnell recommends the *loop with exit*: one entry, a body, and the exit test where it naturally falls. He calls it «структурированная управляющая конструкция» with one entry and one exit (p. 363).

## Rule

When testing at the top or the bottom would mean coding "a loop and a half", put the exit test in the middle. In languages without a native form, write it as an unconditional loop with one `break` (pp. 361-362). McConnell attaches two conditions (p. 363):

- «Разместите все условия выхода в одном месте.» He argues that exits spread through the body make it almost certain that some exit will be missed during debugging, modification or testing.
- Comment the construct where the language has no direct form for it.

He cites a study in which students answered comprehension questions 25% better on the exit-in-the-middle form than on top- or bottom-tested variants (Soloway, Bonar and Ehrlich, 1983, p. 363). He also admits the form was not yet common in production code.

The abnormal variant is a `goto` that jumps into the middle of a loop so that the first half is skipped on the first pass. He rejects it as unusual and confusing (p. 363). The repair is the same unconditional loop with the two halves swapped around the `break` (p. 364). His general advice on loop entry points the same way: enter a loop only from the top, since the loop forms available can test at the top, middle or end (p. 366).

## Sign in code

- One or more statements just before a loop are repeated, identically, as the last statements of its body. Usually these statements produce the value the loop condition tests.
- A jump into a loop body other than through its top, which skips the part above the label on the first iteration.

This wiki assigns the neighbouring cases as follows. A jump into a loop body other than through its top is [[loop-with-exit-in-the-middle]]. A single `break` that removes a top-and-bottom duplication is this page. Several exits, or a `break` replacing flags, are [[break-and-continue]]. A fragment repeated at separate call sites rather than around one loop is [[dry]].

## When not to apply

- The duplicated statement is a single call with no further logic, and the language idiom for reading until exhausted (an iterator, or a read inside the condition) already removes the copy. This limit is this wiki's own.
- The loop is long. This wiki reads p. 365 (the exit of a `while (true)` sits inside the black box; see [[loop-as-black-box]]) and p. 377's demand for an exceptionally clear exit condition in long loops as: in a loop too long to see whole, a middle exit is easy to miss, so keep the form to short loops ([[loop-length-and-nesting]]); p. 377's "one exit" itself is satisfied by this form.
- More than one exit is needed. That is [[break-and-continue]], not this page.

## Repair

1. Replace the loop with an unconditional loop.
2. Move the duplicated statements to the top of its body and delete the copy before the loop.
3. Put the negated loop condition right after them as the single exit, with a comment marking it.
4. Leave the rest of the old body below the exit.
5. Simplify the negated condition (McConnell points to De Morgan's laws, p. 362).

## Before and after

```
score = 0
increment = nextRating()
rating = rating + increment
while score < target and increment != 0:
    score = score + nextScore()
    increment = nextRating()
    rating = rating + increment
```

```
score = 0
loop forever:
    increment = nextRating()
    rating = rating + increment
    if score >= target or increment == 0:
        break        // the only exit
    score = score + nextScore()
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.1, pp. 361-364: the rule, its two conditions, the study and the goto variant; section 16.2, p. 366: entry only from the top. Widening the goto sign to any jump into a loop body below its top is this wiki's own. The first limit, the reading of pp. 365 and 377 as a second limit, the assignment against the neighbouring pages and the pseudocode are this wiki's own; the pseudocode is adapted from the book's score/rating example.
