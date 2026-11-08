---
title: One change at a time
category: debugging
summary: "A bug-fix diff bundles two or more independent edits, each of which could plausibly explain the fixed symptom, so nobody can say which one fixed it or whether one introduced a look-alike defect."
tags: [rule, debugging, fix, voodoo-programming]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

This wiki reads a fix as an experiment, and an experiment with two variables changed at once answers nothing.

## Rule

Make one change at a time. The book's reasoning: single changes are treacherous enough, and two at once can introduce subtle errors that look like the original, so you cannot tell whether you face the old error, a new one that resembles it, or both. «Не осложняйте себе жизнь и вносите изменения только по одному за раз» (p. 542).

Closely related in the book: change code only for a good reason. Changing code at random until it seems to work, such as subtracting 1 and then adding 1 until a run looks right, is what the book calls «вуду-программирование» (p. 542), and the more code is changed without understanding it, the more doubtful its correctness (p. 542). «Не вносите в программу изменение, если не уверены в его правильности» (p. 542).

## Sign in code

- A commit or diff described as fixing one defect changes two or more places that do not depend on each other, and any one of them could account for the reported behaviour.
- A fix diff also carries a second, independent behaviour change (a "while I was here" fix or policy change).

This wiki assigns the neighbouring shapes as follows. This page owns the bundling of independent edits in one fix. A loop bound flipped or nudged by 1 until a test passes is [[check-loop-boundaries-by-hand]]; a lone unexplained ±1 or scale factor applied to a value is [[fix-the-model-not-the-offset]]; a change kept because it made a run pass, with no stated cause, is [[programming-by-coincidence]]; a refactoring and a behaviour change in one diff is [[do-not-refactor-while-adding-features]].

## When not to apply

The book states no limit. The following are this wiki's own.

- One cause requires coordinated edits in several places, such as changing a function's contract and every caller. That is one change.
- The edits are mechanical and verified separately by tooling (an automated rename), and the fix sits in its own step.
- The edits were made and verified one at a time and committed together, and the diff or its message says which edit fixes the reported defect and gives each other edit its own reason and test. The bundle is then a packaging choice, not two variables changed at once.

## Repair

1. Revert to the saved original; the book asks you to keep it before starting (p. 540).
2. Apply the single change your confirmed hypothesis calls for ([[debugging-procedure]]).
3. Rerun the tests used for diagnosis, then the regression suite (p. 542).
4. Put any other edit in a separate change with its own reason.

## Before and after

```
// before: one "fix" commit for a wrong page count
function pageCount(items, perPage):
    if items.isEmpty(): return 1                // edit A: new policy
    return ceil(items.size / perPage)           // edit B: was floor
// which edit fixed the report? did A create a new wrong answer?
```

```
// after: commit 1, the confirmed cause only
function pageCount(items, perPage):
    return ceil(items.size / perPage)
// commit 2, separate, with its own reason and test: the empty-list policy
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 23.3, pp. 540-542. The rule, the voodoo-programming passage and the advice to save the original are the book's, paraphrased except where quoted; quotations were transcribed from the extracted text with line-break hyphens joined, and «вуду-программирование» appears in the extraction split across a line. The experiment reading, the signs, the assignment against neighbouring pages, the limits and the pseudocode are this wiki's own.
