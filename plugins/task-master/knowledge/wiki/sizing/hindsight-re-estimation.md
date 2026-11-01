---
title: Hindsight Re-Estimation
category: sizing
summary: Raising the estimates of finished tasks after they ran long, while open tasks stay on the old scale, inflates velocity and mixes two scales, so the forecast pulls in without any more work done.
tags: [failure-mode, estimation, velocity, board-history]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Hindsight Re-Estimation

Hindsight re-estimation is raising the estimates of tasks after they ran long, without moving comparable open tasks to the same scale. Velocity rises, the remaining total does not, and the forecast improves although nothing more was delivered.

## What breaks

The damage is a mixture of scales in one calculation: "I am mixing revised and original estimates" ([[cohn-agile-estimating-planning]] L1439). The source's arithmetic: fifty one-point stories, five finished in the first iteration of a planned ten. Re-estimating those five at 2 gives a velocity of 10 with 45 points left, so "I expect to finish the project in 4.5 iterations" (L1439). Left alone, velocity is 5 and the project takes 10 iterations in all (L1437). By this wiki's calculation, that means 4.5 iterations remaining against 9 for the same delivered work.

The revision cannot be extended to the open tasks to repair this: "when still looking forward at the remaining 45 stories I cannot predict which of those one-point stories I will want to say were worth two points in hindsight" (L1439).

The move also gains nothing even when applied evenly. Doubling every story doubles velocity and doubles remaining work, leaving "their situation" unchanged (L1418). This wiki concludes that the only version that changes the forecast is the one that makes it wrong.

A milder form appears in the worked case: re-estimating the finished chart story from 3 to 6 and leaving the other charts at their old estimates gives velocity 11 and an 11-point plan that the team "will not be able to" average (L1474-L1476).

## Observable signs

These signs are this wiki's derivations from the mechanism; the source states the mechanism, not a detection method. Each one raises a question.

- **In board history:** a task's estimate changed after it was closed, while open tasks of the same kind kept their estimates.
- **In period figures:** velocity rises between periods while the count of closed tasks does not.
- **In the forecast:** the projected finish moves earlier in a period that delivered no more than the one before.
- **In the stated reason:** the justification for an estimate change is that the task took longer, not that it was bigger compared with something named.

What to check: whether the change was applied to the whole class of work, as in the legitimate case in [[re-estimate-when-relative-size-changes]], where finished and open chart stories were doubled together (L1480).

## Why it happens

In the source the trigger is disappointment. The team "doesn’t feel good about this" and doubles the points, after which their velocity is 12, "which they feel better about" (L1416). This wiki notes that the same pressure can reach a person steering an agent, because the figure reported upward is the one that improves.

Related: [[velocity-self-correction]], [[velocity]], [[partial-credit-for-unfinished-tasks]].
