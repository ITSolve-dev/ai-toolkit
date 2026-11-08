---
title: Stabilize the error
category: debugging
summary: "Use when a failure appears only sometimes, or the only reproduction is a large scenario with many inputs: make it occur reliably, then strip the test until every remaining factor changes the outcome."
tags: [method, debugging, reproduction, intermittent]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A defect that does not occur every time is nearly impossible to diagnose, so the first step of McConnell's procedure ([[debugging-procedure]]) is to make it predictable. McConnell: «Диагностика дефекта облегчается, если его стабилизировать, т. е. обеспечить его надежное возникновение» (p. 530). He calls turning an intermittent defect into a predictable one one of the hardest parts of debugging (p. 530).

## Where intermittent defects usually come from

«Непредсказуемые ошибки обычно связаны с инициализацией, расчетом времени или зависшими указателями» (p. 530). A sum that is sometimes right and sometimes wrong probably involves a variable that is not initialised and happens to be zero most of the time; a strange pointer problem is almost certainly an uninitialised pointer or a use after release (p. 530). For failures that move between runs in concurrent code, see [[random-failures-suspect-concurrency]].

When a failure is intermittent on identical input, [[perturb-state-to-expose-uninitialized-data]] makes it occur every time; once it occurs every time, [[stabilize-the-error]] reduces the failing test.

## Steps

1. **Find a test that fails.** The book says this is not the end of stabilising (pp. 530-531).
2. **Reduce it.** Simplify until you reach the simplest test that still fails: the test should be so simple that changing any aspect of it changes the behaviour of the error (pp. 530-531).
3. **Reduce by hypothesis, not by chance.** Suppose 10 factors combine to cause the error. Form a hypothesis about which are irrelevant, change them, and rerun. If the error remains, drop those factors. If it disappears, you have refuted a specific hypothesis and learned one change that makes the error go away (p. 531).
4. **Vary the test carefully under controlled conditions** to diagnose the problem (p. 531).
5. **Keep the reduced test.** This step is this wiki's own: the reduced test is the reproduction that [[failing-test-before-the-fix]] asks for, and halving a large failing input is done by [[binary-search-debugging]].

The book notes that an independent test group can sometimes do the reduction, but usually it is the programmer's job (p. 531).

## The book's worked example

A payroll listing printed some employees out of alphabetical order on one run and in order on the next (pp. 530-533). Observations, in order: the misplaced records had been entered singly rather than in a batch; a new single record sorted correctly, refuting the first hypothesis; the misplaced names were the ones containing hyphens. The code had two sort routines: one at entry that only places a record approximately, one at save that sorts fully. The refined hypothesis that survived: names containing punctuation sort correctly only on save, and the list was printed before the save (p. 532).

This wiki reads the example as showing step 3 at work: each run either removed a factor or refuted a hypothesis, and the final hypothesis explained all the observations, including the correct second run.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 23.2, pp. 530-533. The steps, causes and example are the book's, paraphrased except where quoted; quotations were transcribed from the extracted text with line-break hyphens joined. Step 5, the reading of the example and the order against [[perturb-state-to-expose-uninitialized-data]] are this wiki's own.
