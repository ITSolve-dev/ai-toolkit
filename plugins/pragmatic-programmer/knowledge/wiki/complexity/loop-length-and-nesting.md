---
title: Keep loops short enough to see whole, and nested no more than three deep
category: complexity
summary: "A loop whose body does not fit on one screen (the book: rarely over 15-20 lines), or loops nested inside loops more than three levels deep with no if/switch among the levels (mixed nesting is tame-deep-nesting): move the inner part into routines or simplify the control; a long loop keeps one, plainly stated exit."
tags: [rule, loops, nesting, length, extract-routine]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell measures a loop's length in lines of code or in depth of nesting, and treats both as complexity the reader has to hold at once (p. 377). The loop rules elsewhere in this wiki assume the loop can be seen whole; this page says when it cannot.

## Rule

- **Short enough to see at once.** If you usually read loops on a screen that shows 50 lines, that is your limit. Experts have proposed a page as the limit, but the book says that once you value simple code you will rarely write loops longer than 15 or 20 lines (p. 377).
- **Nesting limited to three levels.** The book cites research (Yourdon, 1986a) showing that programmers' ability to understand a loop drops sharply past three levels. If more are needed, make the loop conceptually shorter by moving part of it into a routine or simplifying the control structure (p. 377).
- **Move the inside of long loops into routines.** In a well-designed loop the code inside can often be extracted into one or more routines called from the loop (p. 377).
- **Make long loops especially clear.** Length adds complexity. A short loop can afford riskier structures, such as `break`, `continue`, multiple exits and complex termination conditions; a longer one should have one exit and an exceptionally clear exit condition (p. 377).

The book points to section 19.4 for reducing nesting in general (p. 377); see [[tame-deep-nesting]].

## Sign in code

- A loop body longer than one screen (the book's limit, p. 377). Past 15-20 lines, the length the book says simple code rarely exceeds, read the loop for extraction; length alone is not a finding there.
- Loops nested inside loops more than three levels deep, with no decision among the levels.

This wiki assigns the neighbouring cases as follows. This page decides only whether a loop is long or deeply nested. An end marker on a block that [[loop-length-and-nesting]] finds too long is that page's finding; [[end-of-line-comments]] reports an end marker only on a block below that page's limits. Nesting depth counts loops and decisions together. Where every level is a loop, [[loop-length-and-nesting]] owns it; where any level is an `if`/`switch`, [[tame-deep-nesting]] owns it. Several exits in such a loop are [[break-and-continue]]. The nameable fragment the repair extracts is [[extract-routine-to-name-a-step]]. A routine that is too long as a whole is [[routine-length]]. A nested loop whose cost grows with input sizes is [[estimate-algorithm-order]]. A loop that is long because it computes several unrelated results is [[one-loop-one-job]].

## When not to apply

The limits below are this wiki's own:

- A long loop that is one flat, uniform run, such as a sequence of field copies or a table of assignments with one intent, is long without being complex. The book's own measure is what the reader can hold, not a line count.
- Nesting that walks the dimensions of one multidimensional structure (row, column, channel) with a trivial innermost body is the shape of the data. Each level is then a plain index walk, and extracting levels into routines can hide the correspondence between loops and dimensions.
- Extraction would need many parameters that are shared, mutable loop state. This wiki's reading is that the state must be grouped into one object first, or the extracted routine trades one problem for another (see [[pass-state-dont-hoard-it]]).

## Repair

1. Name what the inner loop or the long block of the body does, and move it into a routine with that name ([[extract-routine-to-name-a-step]]).
2. Where the depth comes from conditions rather than loops, flatten them ([[tame-deep-nesting]]); inside a loop, top-of-loop `continue` guards are one way ([[break-and-continue]]).
3. If the loop stays long, reduce it to one exit and state the exit condition plainly in the header or at the single `break`.

## Before and after

```
for order in orders:
    for line in order.lines:
        for lot in stock.lotsFor(line.item):
            for reservation in lot.expiredReservationsOf(order.id):
                lot.release(reservation)
                line.reserved = line.reserved - reservation.qty
```

```
for order in orders:
    for line in order.lines:
        releaseExpiredReservations(stock, order, line)

function releaseExpiredReservations(stock, order, line):
    for lot in stock.lotsFor(line.item):
        for reservation in lot.expiredReservationsOf(order.id):
            lot.release(reservation)
            line.reserved = line.reserved - reservation.qty
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.2, "Насколько длинным может быть цикл?", p. 377: the screen and the 15-20 line remarks, the three-level limit and its citation, extraction into routines, and one exit for long loops. The reading of 15-20 lines as a prompt to read rather than a finding, the rule that counts loops and decisions together for ownership, the three limits, the assignment against the neighbouring pages, repair step 2 and the pseudocode are this wiki's own.
