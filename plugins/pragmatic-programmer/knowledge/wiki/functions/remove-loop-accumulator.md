---
title: Remove a loop accumulator in four steps
category: functions
summary: "Procedure for a variable initialised before a loop and added to on each pass (volumeCredits += ..., total += ...) alongside other work in the same body: split the loop, slide the initialisation down, extract the total into a function, inline the variable."
tags: [method, refactoring, loops, accumulator, temporary-variables]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

An accumulator is the harder case of a temporary variable, because it is built up across the iterations of a loop and cannot be replaced by a single query ([[replace-temp-with-query]]). Fowler removes two of them, `volumeCredits` and `totalAmount`, from `statement` with the same four-step sequence (ch. 1, PDF pp. 25-29).

A loop body computing unrelated results is [[one-loop-one-job]], which owns the shape; this page is the procedure that takes such a loop apart without breaking it.

## Procedure

Each step is followed by compile, test and a local commit (PDF pp. 27-28):

1. **Split Loop (227)** to isolate the accumulation: copy the loop, keep only the accumulation in the copy, remove it from the original.
2. **Slide Statements (223)** to move the accumulator's declaration and initialisation next to the loop that now uses it ([[initialize-close-to-first-use]]).
3. **Extract Function (106)** on the initialisation, loop and accumulator together, returning the total ([[extract-function]]).
4. **Inline Variable (123)**: replace the temp with a call to the new function.

Then rename inside the new function (`totalAmount` becomes `result`; [[rename-extracted-code-for-clarity]]).

**Name collision.** The best name for the new function is often the accumulator's own name, and both cannot exist at once. Fowler gives the function a throwaway name (`appleSauce`) at step 3, inlines the variable, and only then renames the function to `totalAmount` with its own commit (PDF pp. 28-29).

**Performance.** The split repeats the loop. Fowler's answer is that rerunning a loop like this usually has a negligible effect and that the decision belongs after the refactoring (PDF p. 27; [[refactor-first-tune-afterwards]]).

## Example

```
// before
function statement(invoice):
    text = ""
    total = 0
    credits = 0
    for perf in invoice.performances:
        credits += creditsFor(perf)
        text += line(perf)
        total += amountFor(perf)
    return text + footer(total, credits)
```

```
// after steps 1-4, applied twice
function totalCredits(invoice):
    result = 0
    for perf in invoice.performances: result += creditsFor(perf)
    return result

function totalAmount(invoice):
    result = 0
    for perf in invoice.performances: result += amountFor(perf)
    return result

function statement(invoice):
    text = ""
    for perf in invoice.performances: text += line(perf)
    return text + footer(totalAmount(invoice), totalCredits(invoice))
```

The result in Fowler's example is a top-level `statement` of seven lines that only lays out the printing, with all calculation in supporting functions (PDF p. 31).

The remaining sum loops are the next step, [[replace-loop-with-pipeline]], not a sign of this page.

This wiki marks where the procedure does not fit: the limits of [[one-loop-one-job]] (a sequence that can be traversed only once, an expensive per-element value shared by the jobs) hold here too, because step 1 traverses the sequence again.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Removing Total Volume Credits" and "Removing Total Amount", PDF pp. 25-31; catalogue entries Split Loop (227), Slide Statements (223), Extract Function (106), Inline Variable (123). The four steps, the throwaway-name trick and the result are the book's. This wiki's own: the framing as a general procedure for any accumulator (the book shows it on two variables), the links to the limits of [[one-loop-one-job]], and the pseudocode.
