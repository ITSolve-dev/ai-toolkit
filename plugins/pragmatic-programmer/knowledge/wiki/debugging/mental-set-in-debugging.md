---
title: Mental set in debugging
category: debugging
summary: "Concept: why a reader overlooks a defect in plain sight (mental set) and why a region set aside early can be the one holding it; the code shapes it explains are owned by layout-must-tell-the-same-story-as-the-logic and names-differ-by-more-than-a-character."
tags: [concept, debugging, mental-set, blindness]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell borrows the psychological term *mental set*: you see what you expect to see (p. 543). When reading your own code to debug it, the aim is to forget that you know it and to see what is written rather than what you expect (p. 543).

## How it shows in code

The book's examples (pp. 543-544):

- Students expect a `while` loop to end the moment its condition becomes false, as the natural-language word suggests, rather than when the condition is next tested (Curtis et al., 1986).
- A programmer used both `SYSTSTS` and `SYSSTSTS` believing them one variable, and did not notice until the program had run hundreds of times and a book of wrong results was written (Weinberg, 1998).
- Three indented statements under an `if` with no braces are read as if they were all inside the block, though only the first is.

## Psychological distance

The book's measure for the second example is psychological distance: how easily two items are told apart (p. 544). A difference in the first letter stands out more than one in the middle, so `Tuack` is harder to confuse with `Quack` than `Queck` is, though each differs by one letter (p. 544). The naming rule that follows is owned by [[names-differ-by-more-than-a-character]].

## What it means for debugging

The book draws two consequences (p. 544). First, good formatting, comments and names structure the background so that likely defects stand out. Second, mental set decides which parts of a program you examine. Effective debuggers mentally set aside irrelevant parts to narrow the search (Basili, Selby and Hutchens, 1986), but the part set aside may be the one holding the defect, and then the search continues in the wrong place. The book says some of its search tips help overcome this blindness (p. 544); this wiki takes widening the suspect region as the one that answers it: see [[binary-search-debugging]] and [[debugging-procedure]]. It echoes the surprise step of the procedure, [[prove-dont-assume]].

This wiki assigns the code shapes the examples show to their owners: indentation that implies a block the language does not apply is [[layout-must-tell-the-same-story-as-the-logic]]; two names a single letter apart are [[names-differ-by-more-than-a-character]].

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 23.3, pp. 543-544. The concept, the examples, psychological distance and both consequences are the book's, paraphrased. The link to [[prove-dont-assume]], the choice of widening the region as the remedy and the assignment of the code shapes in the last paragraph are this wiki's own.
