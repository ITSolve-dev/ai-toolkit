---
title: Where to spend refactoring effort
category: change
summary: "Use when choosing which code to refactor: neighbours of a new routine or class, code beside a fixed defect, error-prone and high-complexity modules, code being touched anyway, and the boundary between legacy mess and clean code."
tags: [method, refactoring, legacy-code, prioritisation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

The number of worthwhile refactorings in any program is practically unlimited, so McConnell applies the 80/20 rule: spend time on the 20% that give 80% of the benefit (p. 568). This page is the procedure for finding them. Whether to act now on a finding on lines a change touches is [[refactor-early-and-often]]; which code deserves the effort is [[where-to-refactor]]; the occasions in the course of work that call for refactoring are [[when-to-refactor]].

## Procedure

The book's strategies (pp. 568-570):

1. **When adding a routine**, check that the related routines are well organised, and refactor them if not.
2. **When adding a class**, refactor the classes that work closely with it: a new class often exposes weaknesses in existing code.
3. **When fixing a defect**, use what the fix taught you to improve other code prone to similar errors ([[after-a-surprising-bug]]).
4. **Target error-prone modules.** A module everyone on the team fears is likely error-prone; treat it as a target instead of avoiding it (Jones, 2000). Where defect history is available, this wiki ranks the candidates by it on [[metric-outlier-review]].
5. **Target high-complexity modules**, ranked by a complexity measure. The book cites a study where this significantly improved quality in maintenance (Henry and Kafura, 1984).
6. **In maintenance, improve the parts you touch.** «Код, который никогда не изменяется, не требует рефакторинга» (p. 569), but code you do change should be left better than you found it.
7. **Define an interface between messy and clean code, and move messy code across it** (pp. 569-570).

## The interface between two worlds

Reality, such as complex business rules, hardware or other programs' interfaces, is often messier than one would like, and legacy systems hold bad code that must keep working. The book's caption: «Ваш код не обязан быть грязным только потому, что таков реальный мир» (p. 569). Treat the system as an idealised new world, the messy real world, and an interface between them. Each time you touch messy code, bring it to current standards and give variables clear names, which moves it across the interface. The book says that over time this can improve a codebase quickly (p. 570).

This wiki reads the interface as a seam in code whose form is the project's architecture, taken as given; the book's move is to bring touched messy code to current standards, which carries it across.

## Limits

- Code that never changes is left alone (p. 569): an ugly module nobody touches and that causes no defects is not a target.
- Steps 4 and 5 need data from outside the code (defect history, a complexity metric). This wiki notes that an inspector reading one diff can apply only steps 1, 2, 3, 6 and 7.

## Related

- [[refactoring-warning-signs]], for what to look for once the target is chosen
- [[refactor-in-small-tested-steps]]
- [[broken-windows]]

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 24.5, pp. 568-570, citing Jones (2000) and Henry and Kafura (1984). The strategies and the two-worlds picture are the book's, paraphrased except where quoted. The assignment against [[refactor-early-and-often]], the ranking by defect history on [[metric-outlier-review]], the reading of the interface as a seam and the note on which steps a diff supports are this wiki's own.
