---
title: Partial Credit for Unfinished Tasks
category: reading-history
summary: A task unfinished at a period's close earns no velocity by default; only when the remainder will not be done next period is it split, with the done part and the rest estimated separately and no need to sum to the original.
tags: [decision-rule, velocity, iterations, retrospective-analysis, re-estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Partial Credit for Unfinished Tasks

This rule decides what a task left unfinished at the close of an iteration contributes to velocity, and what happens to its estimate. The default is all-or-nothing. Splitting with partial credit is the exception for work that is being deferred.

## Default: all or nothing

"if a story is done (coded, tested, and accepted by the product owner) then the team earns all the points, but if anything on the story isn’t done, they earn nothing" ([[cohn-agile-estimating-planning]] L1496). The source's reason is that this is the easiest case to assess at the end of an iteration (L1496).

The cost is that velocity dips in one iteration and rises in the next, when all the points land for work partly done earlier. The source accepts that because "we’re mostly interested in the team’s average velocity over time, not in whether velocity jumped up or down in a given iteration" (L1496).

## Exception: the remainder is not coming next

"in some cases the unfinished portion of a story may not be done in the next iteration. In these cases it can be appropriate to allow the team to take partial credit" (L1498). The procedure:

1. Treat what was finished as a story in its own right and estimate it relative to other stories.
2. Rewrite what is left as a new story describing only the remaining work.
3. Estimate that story relative to other stories, with current knowledge.

In the source's example, a five-point story to recommend who swims in each event finished individual events but not relays. The done part is judged equivalent to 3 points, and the rest becomes "As a coach I can have the system recommend who should swim in each relay" (L1498).

The two estimates are independent: "The combined estimates would not need to equal the original estimate of five" (L1498), and the summary repeats that the sum "does not need to equal the initial estimate" (L1514). This wiki reads that as following from size being judged against other stories, not divided out of the original figure. The story was "deceptively complex" (L1486), so forcing a sum of five would carry the earlier mistake forward.

## The choice

**Inputs.**
- Whether anything on the task is unfinished at the period's close: read from board state.
- Whether the remainder will be taken in the next period: read from the next period's plan or its ordering.

**Decision.** Remainder taken next: count nothing now and everything on completion. Remainder deferred: split, re-estimate both parts, and credit the finished part.

**What later fact shows the choice wrong** (this wiki's derivation): a task left at nothing because the remainder was expected next is still open a period later, so its completed work stayed out of velocity for longer than the default assumes.

The source's guidance is less firm than this choice implies. The chapter body says partial credit "can be appropriate", while the summary says "I do not recommend giving partial credit" yet allows that a team "may choose" to re-estimate (L1498, L1514). This wiki reads them together as a default with a narrow exception.

## Against the Scrum Guide's rule

[[unfinished-at-period-end]] has an item that missed the Definition of Done return to the backlog and count for nothing. Cohn's default agrees. His exception looks like a conflict, and this wiki resolves it as follows; the resolution is ours. The exception does not credit a fraction of an open task, because it replaces the task with two. Under a setup following the Scrum Guide, the split is allowed only if the finished part meets the standard of done as an item in its own right, so what is counted is a finished item. The remainder then goes back to be ordered like anything else, with no claim on the next period. A task counted at a percentage stays the sign of violation on that page.

## The better answer is upstream

"the two best solutions to allocating points for incomplete stories are first not to have any incomplete stories and second to use sufficiently small stories that partial credit isn’t an issue" (L1500). This wiki reads a task repeatedly crossing a period boundary as raising a question about how it was cut, not about how to credit it. That reading fits the plugin's working test that a started task can be finished without waiting, though that test has no source and comes from the plugin's design.

## Observable signs

Derived by this wiki from the rule; each raises a question.

- A period's velocity includes points from tasks not in a done state.
- A split pair sums exactly to the original estimate, which may mean the parts were apportioned arithmetically and not estimated against other tasks.
- The same remainder is carried over more than one period.

## Settings and executors

The rule exists only where velocity is counted over a period. In this wiki's reading, a project with no iterations has no boundary at which to divide credit, and a task simply counts when it closes.

Being "accepted by the product owner" (L1496) is a condition on earning, so a task whose result is presented and awaiting a verdict has earned nothing yet. This wiki takes that to carry over to a person reviewing an agent's result: the executor's part may have ended, while the points have not been earned. The all-or-nothing rule does not depend on a human executor.

Related: [[velocity]], [[re-estimate-when-relative-size-changes]], [[hindsight-re-estimation]], [[unfinished-at-period-end]].
