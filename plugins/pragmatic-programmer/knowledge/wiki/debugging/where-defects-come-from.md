---
title: Where defects come from
category: debugging
summary: "Concept: defect-origin figures that rank suspects in a search: most fixes touch one routine, construction defects are the programmer's own far more than the compiler's or OS's, one-character typos are common and costly, misread design is frequent."
tags: [concept, defect-taxonomy, debugging-heuristics]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell summarises studies of error types (pp. 509-510). He warns that the data are inconclusive: studies of similar error types differ by as much as 50% (p. 509). Several findings still bear on where to look for a cause.

- **Most errors have narrow scope.** In 85% of cases a fix touched only one routine (Endres; p. 509).
- **Construction errors are the programmer's.** In two older studies 95% of errors were made by programmers, 2% by system software (compiler and OS), 2% by other software and 1% by hardware (p. 509). McConnell expects the programmer's share to be even higher now that system software is more widely used (p. 510). The margin quotes Hunt and Thomas: «Если вы видите следы копыт, думайте о лошадях, а не о зебрах» (p. 509). See [[select-isnt-broken]].
- **Typos are a surprisingly common cause.** 36% of all construction errors in one study (Weiss), and 18% of all errors in a study of an almost three-million-line flight-dynamics application (Card); the three costliest errors he cites, at 1.6 billion, 900 million and 245 million dollars, each came from a one-character change to a previously correct program (p. 510).
- **Misunderstood design is frequent.** 16% (Beizer) and 19% (Weiss) of errors (p. 510).
- **Most errors are cheap to fix.** About 85% take under a few hours; about 1% take much longer, and about 20% of errors consume about 80% of fix effort (p. 510).
- **Many errors are not construction errors.** Poor domain knowledge, changing requirements and poor communication were the top three causes in a survey of 97 developers (p. 509).

## What this changes in debugging

This wiki reads these figures as a prior for a search: suspect your own recent change and the routine it touched before the compiler, the OS or a library; read a suspicious line character by character, since a one-character slip is a common, high-cost cause; and when code looks right but behaves wrong, check whether it implements a misreading of the design. Because the studies disagree widely, this wiki uses them to rank suspects, not to exclude any. McConnell's own conclusion is that each organisation's defect profile differs and should be measured (p. 510). The method that runs the search is [[debugging-procedure]]; where defects cluster over a codebase's history is [[metric-outlier-review]].

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 509-510, via [[code-complete]]. The margin quotation on p. 509 was transcribed from the extracted text and rejoined across a line break. The debugging reading is this wiki's own.
