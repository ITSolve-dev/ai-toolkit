---
title: Do not inline routines by hand for speed
category: functions
summary: "A small routine's body copied by hand into several callers, with speed given in a comment as the reason (\"inlined for performance\") and no measurement showing that the call costs anything."
tags: [rule, inlining, decomposition, optimization, duplication]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell opens the section on routines in his code-tuning chapter by calling good decomposition into routines «одним из самых эффективных способов оптимизации кода» (p. 625). Small, well-defined routines remove repeated code, make tuning easier because improving one routine improves every caller, and are easy to rewrite in a lower-level language if that becomes necessary; large, tricky routines are hard to understand, let alone rewrite (p. 625). Against that, the saving from inlining is small and unreliable: inlining a string-copy routine saved 8% in C++ and cost 10% in Java (p. 625).

## Rule

Keep small routines as routines. McConnell asks the reader to imagine how much larger programs would be if each call were replaced by the routine's code, and how much harder they would be to optimise (p. 159). He states that on the machines a programmer meets in practice a call costs almost nothing, and that inlining can improve performance or worsen it (pp. 625-626). Even the language's inline routines he tells the reader not to overuse: they expose the code in a header, always grow the code, and are to be profiled and measured like any other tuning (pp. 180-181).

This wiki reads that as: do not copy a routine's body into its callers to avoid call overhead unless a measurement shows the call matters.

## Sign in code

- The same few lines appear in several callers where one named routine would do, and a comment gives speed as the reason ("inlined for performance").
- Or a routine has been absorbed into a long loop body for speed, so the loop now holds several unnamed steps.

This wiki assigns the neighbouring shapes as follows. A small routine's body copied by hand into its callers is [[do-not-hand-inline-for-speed]], when speed is the stated reason. Copies with no stated reason are [[dry]]. Every other speed-motivated indirection is [[premature-code-tuning]].

## When not to apply

- A profile shows the call itself is a hot spot, and the inlined form measured faster in the real build. McConnell allows that inlining can save «несколько наносекунд» in some cases (p. 625).
- The language or compiler offers an inlining hint (such as C++ `inline`), or a macro that switches inlining on and off, which the book names as the means of inlining (p. 625). Either keeps the routine as a single named definition, so it is not the copied-body shape this page targets; the distinction is this wiki's. Even so, the book warns that inline routines break encapsulation and grow the code, so they too need the measurement (pp. 180-181).

## Repair

Extract the copied lines back into one named routine and call it from each site ([[extract-routine-to-name-a-step]]). Measure before and after; restore the inlining only on evidence, and then through the language's inlining hint or a macro rather than by copying.

## Before and after

Before:

```
// inlined for speed
for each order in orders:
    total = 0
    for each line in order.lines:
        total = total + line.price * line.quantity
    order.total = total

for each quote in quotes:
    total = 0
    for each line in quote.lines:
        total = total + line.price * line.quantity
    quote.total = total
```

After:

```
function sumLines(lines):
    total = 0
    for each line in lines:
        total = total + line.price * line.quantity
    return total

for each order in orders:
    order.total = sumLines(order.lines)
for each quote in quotes:
    quote.total = sumLines(quote.lines)
```

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, section 26.5: decomposition as optimization and its reasons, p. 625; the inlining measurements and the nanoseconds remark, p. 625; the near-zero cost of calls today and the two-way effect of inlining, pp. 625-626; inlining by macro, p. 625. Section 7.1, p. 159: the cost of replacing each call by the routine's code. Section 7.7, pp. 180-181: the caution on inline routines and the call to profile and measure. See [[code-complete]].
- Quotations were transcribed from the extracted text with line-break hyphens joined, and need the page-image check.
- This wiki's own: the reading of the book as a rule against copying a body by hand (the book speaks of inline routines and macros, not of hand copies), the measurement condition as worded, the sign, the assignment against neighbouring pages, the distinction between an inlining hint and copying by hand, and the pseudocode pair.
