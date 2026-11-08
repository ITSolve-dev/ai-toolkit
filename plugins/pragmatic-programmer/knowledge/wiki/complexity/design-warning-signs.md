---
title: Design warning signs
category: complexity
summary: "Use as a scan before judging code: a class with more than seven members, a method with more than 10 decision points or more than three levels of nesting, code its author calls clever, or a fragment the reader has to decode rather than read; each mark is a cue to read, routed to the page that owns it."
tags: [method, warning-signs, metrics, complexity, coupling, cohesion]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell's closing chapter gathers a set of **warning signs**: subtle hints of a problem in a program, which unlike a road sign about falling rocks are not obvious (p. 828). He offers them as a reason to doubt the code, not as a verdict. Programming is partly craft and not pure science, so a warning sign has no well-defined fix attached. It only points at something to examine, and the book says outright that clever code or an error-prone class does not always have to be rewritten (p. 828).

## The signs, as the source lists them

**Thresholds** (design metrics used as heuristics, p. 828). The book reads each of these as a reason to look skeptically, not as proof of a fault:

- «Если класс содержит более семи членов, это не всегда означает, что он плохо спроектирован, но предупреждает о том, что класс сложен.» (p. 828)
- more than 10 decision points in one method;
- more than three levels of logical nesting;
- an unusually large number of variables;
- high coupling of one class to others, or low cohesion inside a class or method.

**Code that has to be explained.** The book calls clever code just another name for bad code (p. 828, paraphrased). If code looks clever to its author, the book suggests rewriting it so it stops being clever. Its closing test: «Если вы разгадываете код, а не читаете его, он слишком сложен.» (p. 829). The book follows it with the claim that complex code is wrong code and should be made simpler.

**Defect history.** A class with an above-average defect count is a warning sign. A few error-prone classes are usually the most expensive part of a program, and an above-average count tends to persist, so the book suggests considering a rewrite (p. 828). The ranking by defect history is [[metric-outlier-review]].

**Friction while working** (p. 829):

- Repeated code, or similar changes made in several places, raises the question of whether control is properly centralised in classes or methods. See [[dry]].
- A class you cannot easily put into a test scaffold suggests it is too tightly coupled to other classes. See [[coupling]].
- Code you cannot reuse in another program because some classes depend too much on each other signals the same thing.
- Trouble writing comments, naming variables, or splitting the problem into cohesive classes with clear interfaces means the design was not finished before coding started. Inexpressive names, and parts that resist a short description, are further signs of the same problem.

## Procedure

This wiki reads the list as a scan to run over a piece of code before judging it:

1. Count: members per class, decision points (`if`, `while`, `for`, `case`, `and`, `or`) per method, depth of nesting, local variables.
2. Mark every count over its threshold. A mark starts a closer reading; it is not a finding by itself.
3. Apply the reading test to each marked fragment: can it be read from top to bottom, or does it have to be decoded?
4. Only then open the page that owns the repair: [[decision-point-count]] for decision points, [[tame-deep-nesting]] for nesting, [[class-size]] or [[class-interface-coherent-abstraction]] for an oversized class, [[routine-cohesion]] for a method doing several jobs, [[dry]] for duplicated control, [[coupling]] or [[global-data]] for coupling, and [[rewrite-tricky-code]] for clever code.

The numbered order and the hand-off to owning pages are this wiki's own. The source gives the signs and says they call for doubt.

This wiki assigns the neighbouring methods as follows. Choosing *which* units of a codebase to open first, by comparing counts across all of them, is [[metric-outlier-review]]. Reading one routine or class for what to refactor is [[refactoring-warning-signs]]. This page is the scan of the code already in front of the reader, against fixed thresholds. The threshold of 10 decision points is [[decision-point-count]]; ranking units by their counts to pick what to read is [[metric-outlier-review]]; a first scan routing a mark to its owner is [[design-warning-signs]].

## Limits

- The source says each threshold "does not always mean" poor design (p. 828). A class of eight well-chosen value fields, or a method with 11 decision points that is a flat dispatch table, may need no change; these examples are this wiki's own. A count over its threshold tells you where to look; the verdict still needs a named problem.
- The code may turn out fine as it is, and saying so is a valid outcome of this method.
- The defect-history sign and the reuse-in-another-program sign need knowledge outside the code in view (a defect log, a second program). A reviewer without it cannot apply them. This limit is this wiki's own.

## Source

[[code-complete]], ch. 34.7, pp. 828-829. The book's parts: the thresholds, the clever-code and decoding tests, the defect-history and friction signs, and the claim that a sign does not always require a rewrite. This wiki's own parts: the step-by-step procedure, its hand-off to owning pages, the assignment against neighbouring methods, the examples in the first limit, and the remark that defect history and reuse in another program are not visible in code. The quotations were transcribed from the extracted text and should be checked against the page image.
