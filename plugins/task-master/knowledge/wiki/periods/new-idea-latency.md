---
title: New Idea Latency
category: periods
summary: Under a fixed period, an idea arriving at a random moment reaches working software after 1.5 period lengths on average; half a period waiting for the next start and one full period to build it.
tags: [concept, iterations, period-length, latency]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# New Idea Latency

New idea latency is the time from a good new idea to working software under a period setup. It is the price of holding priorities still during a period ([[mid-period-change]]), and Cohn gives it as a simple multiple of the period length.

> The key point to remember from this example is that the time from new idea to working software will be an average of 1½ times the length of the team’s iterations.
>
> — [[cohn-agile-estimating-planning]], L3457

## Derivation

Cohn's example uses four-week periods. Ideas are assumed equally likely at any moment, so on average one arrives mid-period. It waits two weeks for the next start, then takes a full four weeks to appear as potentially shippable software (L3457, L3468). That is six weeks in total.

| Period length | Average latency |
|---|---|
| 1 week | 1.5 weeks |
| 2 weeks | 3 weeks |
| 4 weeks | 6 weeks |

Only the four-week row is the source's. The other rows, and the bounds that follow, are this wiki's arithmetic. An idea arriving just before a period starts takes one period length. One arriving just after takes two.

## Conditions on the number

1.5 is the result of a model, not a measurement. It holds only if:

- ideas arrive evenly across the period (L3457);
- the idea is selected for the very next period, since each period it misses adds one full length;
- the result is delivered at the period's end, because software is "usually of potentially shippable quality only at the end of an iteration" (L3431);
- the idea does not fit a declared support reserve (L3459), which would bypass the wait.

## Using it

This use is this wiki's, not the source's. The number turns a question about how quickly new ideas must land into a limit on period length: the longest acceptable average wait, divided by 1.5, gives the longest period that meets it.

| Input | Read from |
|---|---|
| Longest acceptable wait for a new idea | The people steering |
| Period length | The project setup |
| Actual wait | Board history: time from a task's creation to its finish, for tasks created during a period |

The choice was wrong if the actual wait repeatedly exceeds what the people steering accept, or if selected ideas keep missing the next period, which means the model's second condition fails and the real multiple is higher.

## Which setup this applies under

Only under an iteration setup. Under a flow setup the wait is the queue ahead of the task plus its time in progress, read from history ([[service-level-expectation]]). This contrast is this wiki's.

## Agent executor note

The arithmetic does not depend on a human executor, so it survives. Its meaning changes. If an agent finishes a task in hours, the full period in the formula is no longer time spent working, and the wait is set by the period container and not by the executor. This wiki reads that as a cost of a long period for agent-executed work, and as a reason to check whether a result may be presented before the period ends.

## Related

This limit is one input to [[period-length]].
