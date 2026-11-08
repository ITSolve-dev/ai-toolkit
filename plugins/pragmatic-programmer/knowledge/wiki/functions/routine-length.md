---
title: Let complexity, not a line count, limit routine length
category: functions
summary: "A routine over 200 non-blank, non-comment lines, or code split into Part1/Part2 pieces only to meet a fixed line limit: judge the length by cohesion, nesting depth, variable count and decision points, not by a quota."
tags: [decision-rule, routine-length, complexity, research]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell surveys the research on routine size and concludes that a fixed line limit is the wrong control (*Code Complete*, pp. 169-170). Textbooks often advise a screen or one to two pages, roughly 50-150 lines. IBM once capped routines at 50 lines, and TRW at two pages. Meanwhile he met routines of about 4,000 and more than 12,000 lines at two clients (p. 169).

## Rule

The evidence the book cites (pp. 169-170):

- Basili and Perricone (1984): errors per line *fell* as routines grew, up to 200 lines.
- Shen et al. (1985): errors correlated with structural complexity and amount of data, not with size.
- Card, Church and Agresti (1986), and Card and Glass (1990): small routines (32 lines or fewer) were not cheaper or less defective. Large routines (65 lines or more) were cheaper to develop per line.
- Selby and Basili (1991): routines under 143 source statements had 23% more errors per line than larger ones, but were 2.4 times cheaper to fix.
- Lind and Vairavan (1989): code needed the fewest changes when routines averaged 100-150 lines.
- Jones (1986): error rates peaked for routines over 500 lines and rose in proportion to size beyond that.

From this the book allows a routine implementing a complex algorithm to grow to 100-200 lines, counting non-blank, non-comment source lines. It notes that many routines in object-oriented code are short accessors. Length should follow from cohesion, nesting depth, number of variables, number of decision points, the number of comments needed to explain the routine, and other complexity factors. Above 200 lines it advises caution: «Что касается методов, включающих более 200 строк, то к ним следует относиться настороженно.» (p. 170). None of the studies found the benefit of size growing past 200, and beyond that, routines inevitably become harder to understand.

The checklist asks whether a routine's length is set by its role and logic rather than by an artificial coding standard (p. 181).

Beck and Fowler's **Long Function** smell argues from experience rather than from studies: "the programs that live best and longest are those with short functions" (*Refactoring*, 2nd ed., ch. 3, Long Function, PDF p. 87). They too reject the count as the criterion: "The key here is not function length but the semantic distance between what the method does and how it does it" (PDF p. 87). Their heuristic is to write a function whenever they feel the need to comment something, named after the intention of the code and not after how it works, even for a single line (PDF p. 87). The cost they name falls on the reader, who has to switch context to see what a called function does, and their answer is naming: "If you have a good name for a function, you mostly don’t need to look at its body" (PDF p. 87). They list where to look for pieces to extract: comments, conditionals, switches and loops (PDF p. 88).

This wiki resolves the two books as follows. Fowler's remark that any function over about half a dozen lines starts to smell to him (ch. 6, PDF p. 123) describes his habit; the criterion both books name is not the count, so neither makes a 60-line routine a finding by length. Fowler's guidance is applied through the pages that own a nameable step: a commented block or an inline step with a nameable result is [[extract-routine-to-name-a-step]], a complex condition is [[name-complex-conditions]], a long case arm is [[keep-case-arms-short]], and a loop doing two things is [[one-loop-one-job]]. This page keeps the threshold at which length alone calls for a review.

## Sign in code

- A routine of more than 200 non-blank, non-comment lines. That count alone triggers a review against the factors above; it is not a verdict.
- Routines named or numbered by position (`Part1`, `Part2`, `Step3`) or cut at a regular line interval, each continuing state left by the previous one. The cut was made to satisfy a length quota, not along the problem's seams. The book's example is a developer who cut one huge routine into 15-line pieces called `Part1`, `Part2` and so on (p. 167).

This wiki assigns the neighbouring case as follows. A class too long in lines is [[class-size]]; this page owns the length of one routine. State handed between the pieces through fields is also [[pass-state-dont-hoard-it]]. Numbered pieces cut from one routine that continue each other's state are [[routine-length]]; numbered siblings with distinct jobs are [[routine-names]]. A function whose name says *what* where its body says *how* is an explanation and stays, however short; a function whose name only restates its body is [[lazy-element]].

## When not to apply

- **Below 200 lines, length is not the finding.** This wiki reads the book this way: a 120-line routine that is cohesive, shallowly nested and has few decision points meets this rule. A finding against it has to name one of the complexity factors, which pages such as [[routine-cohesion]] and [[extract-routine-to-name-a-step]] own.
- **A project standard sets a limit.** This wiki adds a limit. A project's configured length check is the project's convention, and the expert follows it. The research above argues against tightening it on its own authority, not for ignoring it.
- **The research is old.** The studies date from 1984 to 1991; the book itself says some are outdated and others still hold (p. 169), without saying which. This wiki adds that they predate most object-oriented code, so a finding resting on a study's number should say so.

## Repair

For a routine over the threshold, find which complexity factor is high and fix that: split by cohesion ([[routine-cohesion]]), extract the nested or nameable steps ([[extract-routine-to-name-a-step]]), or reduce the number of live variables. For pieces cut to a quota, merge them back and split along steps that have names. Beck and Fowler's repairs for a long function (PDF pp. 87-88): Extract Function, which they say suffices nearly every time; where temps and parameters get in the way, Replace Temp with Query ([[replace-temp-with-query]]) and Introduce Parameter Object ([[group-related-data-into-a-structure]]) or Preserve Whole Object ([[pass-what-the-routine-uses]]); where they still do, Replace Function with Command, which they call the heavy artillery ([[function-or-command-object]]). The mechanics are [[extract-function]]. Where extracting a fragment would need most of the routine's locals as parameters or results, the temps are removed first ([[replace-temp-with-query]]); where they still tangle, [[function-or-command-object]] owns the choice of a command object; where the routine is to stay whole, the intent comment is split into finer steps ([[extract-routine-to-name-a-step]]).

## Before and after

```
routine BuildReport()
    Part1()
    Part2()
    Part3()

routine Part1()
    ... first 15 lines, leaves rows in a field ...
routine Part2()
    ... next 15 lines, reads the field, leaves totals ...
routine Part3()
    ... last lines, reads totals, prints ...
```

```
routine BuildReport()
    rows = LoadRows()
    totals = Summarise(rows)
    Print(rows, totals)
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.4, pp. 169-170; the `Part1`/`Part2` example, p. 167; the checklist, p. 181 ([[code-complete]]). The studies, the 100-200-line allowance, the factors and the caution above 200 lines are the book's.
- The signs as stated, the owner split, the three limits (except the book's remark that some studies are outdated, p. 169) and the pseudocode are this wiki's own.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Long Function", PDF pp. 87-88: short functions living longest, semantic distance, the comment heuristic, the reader's cost and naming, where to look, and the repairs. This wiki's own for that part: the resolution against *Code Complete* (with Fowler's half-dozen-lines remark, ch. 6, PDF p. 123, read as his habit) and the routing of Fowler's places to look to their owner pages.
