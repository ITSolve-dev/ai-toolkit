---
title: The changeability test
category: obligation-and-mechanism
summary: Decide whether something belongs in a description by listing the changes likely to happen and tracing how far each one propagates.
tags: [method, criterion, information-hiding, volatility]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

A method for settling boundary arguments with evidence instead of taste: **enumerate the decisions
likely to change, then trace how far each change propagates through the description as written.**
The arrangement that confines more changes to fewer places is the better one, and an element whose
change propagates everywhere is one the description should not have named.

Parnas uses it as the entire argument of [[parnas-criteria-for-decomposing-systems]]. He describes
one system — a KWIC index — twice, once cut by processing step and once cut by hidden decision,
then lists five "design decisions which are questionable and likely to change" (L161-L178) and
walks each through both cuts.

## The trace, as he runs it

| Likely change | Cut by processing step | Cut by hidden decision |
|---|---|---|
| Input format | one module | one module |
| Whether all lines are held in core | **every module** | one module |
| Whether characters are packed four to a word | **every module** | one module |
| Whether shifts are stored or indexed | shifter, alphabetiser and output | one module |
| Whether alphabetisation happens once, on demand, or partially | output must know it finished first | one module |

> In the first decomposition the format of the line storage in core must be used by all of the
> programs. In the second decomposition the story is entirely different. Knowledge of the exact
> way that the lines are stored is entirely hidden from all but module 1.
>
> — L180

Note what makes the test necessary rather than optional. The two arrangements are indistinguishable
until a change arrives — Parnas states that they "may share all data representations and access
methods", and that a system built either way "could conceivably be identical *after assembly*"
(L147-L159). The first row of the table shows the same thing at the level of one change: input
format is confined either way. Nothing about the flowchart cut looks wrong on inspection. The
defect becomes visible only when something changes, which is why the test has to be run
deliberately rather than waited for.

## Running it on a document

1. **List what will plausibly change** about the subject within the document's expected life —
   not everything that could change, only what a reasonable person expects to.
2. **For each, find every passage that would have to be rewritten.** Search the text for the
   element by name.
3. **Judge by the count.** A change that touches one passage was hidden well. A change that
   touches many was revealed where it should not have been, and the passages naming it are the
   defect.

This turns the abstract question "is this too much detail" into a countable one. It also supplies
the discriminator behind [[information-hiding]]: *likely to change* is a claim about the subject,
open to argument and to being wrong, and therefore checkable — unlike "too concrete", which is
not.

## Its limit

The test is only as good as the list of changes. A change nobody anticipated is confined by luck,
not by design, and Parnas is candid that his own second decomposition still contained a defect he
noticed only in hindsight — see [[over-specification]]. Running the test does not certify a
description; it finds the defects the list can reach.
