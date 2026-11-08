---
title: Metric outlier review
category: complexity
summary: "Use to choose which routines or classes to read first: count decision points, parameters, locals, lines, called routines, goto and I/O statements per unit, and how often each has been fixed, then open the units that stand far apart from their neighbours; an outlier is a cue to read, not a verdict."
tags: [method, metrics, code-review, complexity, hotspots]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Metric outlier review** is a way of choosing which routines and classes to read closely: compute a few simple per-unit counts across a codebase, and treat the units whose counts stand far apart from the rest as candidates for review. McConnell presents measurement this way in two places. Chapter 28 says that most of these measures are not needed for telling programs, classes and routines apart; they are needed mainly to find the routines that differ sharply from the others, and «необычные показатели измерений в каком-то методе предупреждают о том, что вам следует пересмотреть этот метод», to find out why its quality is unusually low (p. 663, citing Shepperd and Ince, 1989). Chapter 30 says the same of tools: those that report each routine's complexity «позволяют направить наиболее сложные функции на дополнительное рецензирование, тестирование или перепроектирование», others count the changes made to the software and single out the routines fixed most often, and complexity-analysis tools were found to raise maintenance productivity by about 20% (p. 699, citing Jones, 2000).

## What is counted

Among the measures McConnell lists (Table 28-2, pp. 662-663), the ones that live in the code itself, per class or per routine, are:

- number of public routines in each class;
- number of parameters passed to each routine;
- number of private routines and/or variables in each class;
- number of local variables used by each routine;
- number of routines called from each class or routine;
- number of decision points and the control-flow complexity of each routine;
- lines of code, comment lines, data declarations and blank lines in each class or routine;
- number of `goto` statements and of input/output statements in each class or routine.

The same table pairs these with defect data per class or routine: the number of defects, the attempts made to fix each, and the new errors a fix introduced (p. 663). Chapter 30 adds the count of changes made to fix defects, per routine (p. 699). Those columns need a tracker or the version history; the structural ones can be read off the code in front of the reviewer.

## Why the defect column matters

Defects are not spread evenly through code. The intuitive assumption that 10 defects per 1000 lines means one defect in a 100-line class is wrong (p. 508). McConnell cites 80% of errors in 20% of a project's classes or routines (Endres, Gremillion, Boehm, Shull et al.) and 50% of errors in 5% of classes (Jones) (p. 508). At IBM, 31 of 425 IMS classes were labelled error-prone and were repaired or redeveloped; within a year customer-reported defects fell tenfold and maintenance costs about 45% (p. 508). OS/360's error-prone routines held up to 50 defects per 1000 lines, and fixing them often cost ten times what the whole system took to develop (p. 508). The book suggests counting defects per class and per routine, sorted from worst to best and possibly normalised by size (p. 520), and its key point is «Найдите такой код, перепроектируйте его и перепишите» (p. 523). Overly complex routines are named as another frequent home of defects (p. 508), which is why step 3 below ranks by both counts.

## Procedure

1. Pick a small set of counts. McConnell warns against collecting every possible measure at once, because the data becomes too tangled to interpret (p. 663).
2. Compute them for every routine or class in the scope under review; where version history is available, count the defect fixes per routine too.
3. Look for the units that differ sharply from the rest, not for small differences between ordinary ones (p. 663). Units high on both a complexity count and the fix count come first.
4. For each outlier, choose among the three responses chapter 30 names: extra review, extra testing, or redesign (p. 699).
5. Open the outlier and decide by reading it which rule, if any, it breaks: [[routine-length]], [[limit-parameter-count]], [[tame-deep-nesting]], [[decision-point-count]], [[routine-cohesion]], or a class doing too much ([[class-size]]).

```
routine            decisions  defect-fixes
applyDiscounts         27          14     <- review, then redesign
parseHeader            19           1     <- extra tests
formatAddress           3           9     <- read: simple yet often wrong
sum                     1           0
```

## Limits

The source states only the warning against over-collection and the remark that people concentrate on the work that is measured and neglect the rest (p. 662). The limits below are this wiki's own.

- An outlier is a reason to read, not a finding. A routine that is a flat dispatch table or a long but linear sequence can score high on lines or decision points and still be the clearest form of that code; the review may conclude that the code is fine as it is.
- A stable, well-tested routine that mirrors an inherently branching rule may need nothing, however high it ranks. The opposite case also appears: a low-complexity routine fixed often points at a misunderstanding or an unclear contract, which no complexity count shows.
- The counts compare units within one codebase. An absolute threshold carried from elsewhere is not what the source proposes; pages that do give a threshold own it. The threshold of 10 decision points is [[decision-point-count]]; ranking units by their counts to pick what to read is [[metric-outlier-review]]; a first scan routing a mark to its owner is [[design-warning-signs]].
- The defect column lives in history, not in the code in front of a reader. Without a record of which routines each fix touched, a code-only review should not call a routine error-prone.
- A high fix count can also reflect how much a routine is used or how much of the system's logic it legitimately holds; normalising by size, which the book suggests (p. 520), removes only part of that. The book's cost figures are from large systems of the 1960s to 2000.
- A rewrite of an error-prone routine is itself a risky change; see [[refactor-in-small-tested-steps]] and [[rewrite-a-method-you-do-not-understand]].
- This wiki reads McConnell's remark on p. 662, for code, as: once a per-routine count becomes a gate, routines get split to satisfy the count rather than to separate responsibilities, which scatters one decision across several places. A count used as a target stops being a reliable cue.

## Trade-offs

The method is cheap and directs attention, but it sees only what is countable. A routine with a misleading name, a wrong abstraction or duplicated knowledge can have perfectly average counts; outlier review does not replace reading the code.

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, section 28.4: Table 28-2 (pp. 662-663); the use of measures to find outlying routines and the warning against collecting everything (p. 663); measurement shaping what people attend to (p. 662). Section 30.2: metrics reporters, per-routine complexity, tracking the most-fixed routines, and the Jones 20% figure (p. 699). Chapter 22: defect concentration, the IMS and OS/360 cases (p. 508), per-class and per-routine defect counts (p. 520) and the key point (p. 523). See [[code-complete]].
- The quotations were transcribed from the extracted text; in the p. 663 one the hyphen in «каком-то» is restored from the print, where the raw text has `#`. Both need the page-image check.
- This wiki's own: the selection of the structural columns, the order of the procedure and its ranking by both counts, the example table, and all of *Limits* except the over-collection warning, the remark on p. 662, the size normalisation and the dating of the figures.
