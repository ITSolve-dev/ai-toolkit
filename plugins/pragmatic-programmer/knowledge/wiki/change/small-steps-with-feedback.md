---
title: Small steps with feedback
category: change
summary: "For a change too large to verify at once: establish where things stand, take the smallest step a check can judge, evaluate and repair before the next one, and split any task that needs a forecast."
tags: [method, safe-change, feedback, small-steps]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

The tip is «Всегда предпринимайте небольшие шаги» (p. 164). The reason is the same limit of foresight as in [[replaceable-code-over-forecast]]. The book returns to the idea in its section on agility, where a three-step loop is the whole of its recipe for working under uncertainty (p. 317). The method survives apart from any process vocabulary.

## Procedure

The book's recipe has three steps (p. 317):

1. «Выясните, где находитесь.»
2. «Сделайте наименьший значимый шаг в нужную сторону.»
3. «Оцените, где вы оказались, и исправьте все, что нарушили.»

The steps repeat until the work is done, and the authors add: «Пользуйтесь данным рецептом рекурсивно на каждом уровне всей своей деятельности.» (p. 317).

The book's earlier statement gives the evaluation its content (p. 164). Take one small, deliberate step. Get feedback, meaning anything that independently confirms or refutes the step; the book's examples are REPL output for your understanding of an API or algorithm, unit tests for the latest code change, and a demo for features and usability. Adjust, and only then continue.

## Why it works

The authors' argument is that the unknown appears as soon as work starts, so no fixed plan can cover it, and that the response has to be made in the moment and in context (p. 316). This wiki reads that as saying a plan fixes decisions before the feedback that should inform them.

They also claim the method pays at scale at both ends. At the low end a variable name led to a better dependency, see [[name-friction-exposes-coupling]]. At the high end one step on a client's requirements showed that the best solution needed no software at all (p. 317).

*Code Complete* gives the same argument for joining classes one at a time. When classes that never ran together are joined at once, «Все классы находятся под подозрением» (p. 675); with one piece added to a working whole, a new problem is evidently caused by the new piece, its interface or its interaction with what is already there (p. 677). This wiki adds that the bound holds only if the state before the step was passing; a step taken on top of failing tests returns the ambiguity in miniature ([[all-tests-pass-always]]).

## How large is too large

The book's test is that a task is too large if it requires predicting the future. Its horizon is one or two steps, at most a few hours or days (pp. 164-165). Beyond that, a reasoned guess quickly becomes speculation (p. 165).

This wiki reads this for a code change as one reversible edit between runs of the tests, and treats an edit whose result cannot be checked until several others are finished as a sign that it needs splitting.

## Running it on code

The translation of the recipe into code is this wiki's own. The book gives the three steps and two examples.

- *Where you are* means a known state: the tests pass, or the failures that exist are listed before the change starts.
- *The smallest step that means something* is one change a check can judge: one rename, one extracted function, one case added with its test. A step that cannot be judged by itself is too large or is not yet a step.
- *Evaluate* means running the check that would show the step wrong. Reading the diff is not that check when a test can be run.
- *Repair what you broke* comes before the next step. If the step turned out to be wrong, undoing it is a repair.

## Failure modes

The book names the third one. The others are this wiki's own.

- The step is so large that a failure cannot be attributed to any part of it. Bisecting the step is then the first task; see [[binary-search-debugging]].
- Several steps run without evaluation, so several unjudged changes stack up and the state at step one is lost.
- The repair is skipped. The authors warn that repair has to be as painless as possible, otherwise there is a temptation to leave things as they are, and they point to software entropy (p. 318). See [[easier-to-change]].
- Steps keep failing along one path. More steps of the same kind will not help, so question the path itself; see [[find-the-real-constraints]].

## Limits and trade-offs

This wiki notes that the method says nothing about a change that cannot be divided, such as a single migration of stored data. There the safety has to come from elsewhere. The book's list of fortune-telling also includes dates months ahead and guesses about users' future needs (p. 165), which fall outside this wiki's charter.

The costs below are this wiki's own statement. Small steps pay a check per step, which is expensive where the check is slow, and they can leave intermediate states that are awkward to keep valid, as when a rename crosses a published interface. They do not choose a direction either: the method corrects a course and does not supply a destination.

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 164-165, 316-318. The reading for a single code change, the reading of the plan argument, the translation of the recipe into code, the failure modes other than the skipped repair, the limit on indivisible changes and the trade-offs are this wiki's own. The authors extend the loop to a team's own process; that part is out of this wiki's scope and is left out.

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]], ch. 29, pp. 675-677: the localisation argument for incremental integration. The book's integration orders (top-down, bottom-up, feature-oriented and the rest) are system-level process and are left out. The limit about a passing state before the step is this wiki's own.
