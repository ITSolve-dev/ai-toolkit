---
title: Tests for orthogonality
category: structure
summary: "Checks to run on code: modules touched by one requirement, imports a unit test needs, spread of a bug fix, files per fix in history, and what a library demands of your objects."
tags: [method, coupling, testability, review]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The book offers several concrete questions for measuring [[orthogonality]] in an existing system. Each turns a vague worry about coupling into something that can be counted.

## Procedure

1. **Requirement test.** Pick one function of the system and ask: «если я внесу коренные изменения в требования к конкретной функции, на какое количество модулей это повлияет?» (p. 73). The answer in an orthogonal system should be one. Moving a button should not change the database schema, and adding context help should not change billing (p. 73).
2. **Real-world test.** Ask how far the design is separated from changes in the world. List the external facts the code depends on, see [[externally-controlled-identifier]] (p. 74).
3. **Toolkit test.** When adopting a library, ask what unwanted changes it forces into your code. See [[framework-intrusion]] (p. 74).
4. **Unit-test test.** Ask what it takes to write and run a unit test: «Приходится ли для этого импортировать львиную долю остального кода системы?» (p. 76). If so, that module is not decoupled enough.
5. **Bug-fix test.** After finding a bug, ask how local the fix is: one module, or scattered through the system? Does the fix remove every symptom, or do other errors mysteriously appear (p. 76)?
6. **History test.** Tag bug fixes in version control, then review monthly trends in how many source files each fix touched (p. 76).

## Reading the results

The book attaches a limit to step 1: a real requirement often touches several functions, so count per function, and treat one module as an ideal (p. 73, footnote).

This wiki reads steps 4 to 6 as the strongest for review, since they count something present: imports, files in a fix, files in a commit. Steps 1 and 2 need a scenario of change, so a finding from them should name the specific change and the modules it reaches, not assert that a design is coupled.

## Worked case

The book's exercise on p. 78 compares a splitter that opens a file, steps through lines and returns fields, with one that is constructed from a single line and returns fields. The authors' answer is that the second is more orthogonal: it keeps to its own job of splitting lines and ignores where they come from, which makes it easier to develop and more flexible, since its lines can come from a file, from another routine or from the environment (p. 349). This wiki adds that step 4 reaches the same verdict: a unit test needs a file for the first and only a string for the second. The rule drawn from the case is [[process-values-not-their-source]].

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 10, pp. 73-74, 76 and 78, and the answer to exercise 1, p. 349, via [[pragmatic-programmer]]. This wiki's own: the numbering into one procedure, the ranking under *Reading the results*, and the link from the exercise to step 4.
