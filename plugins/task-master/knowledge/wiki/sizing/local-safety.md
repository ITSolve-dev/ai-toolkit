---
title: Local Safety
category: sizing
summary: The extra time between a task's 50% and 90% estimates; summed across tasks it produces a plan far longer than needed, because all tasks do not go wrong on the same run, and it protects tasks rather than the deadline that matters.
tags: [concept, estimation, uncertainty, buffer, human-executor-mechanism]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Local Safety

Local safety is the protection attached to each individual task instead of to the plan as a whole: "The additional time between the 50% and the 90% estimate is called local safety" ([[cohn-agile-estimating-planning]] L3922). People add it to any estimate they want to be sure of meeting. It is a sensible move for one task and a costly one for a plan.

## Why it does not sum

Cohn's warning is that estimating every story at its 90% point to get a 90% schedule means "the project schedule will almost certainly be too long" (L3920). His airport trip (L3931-L3935) gives the size of the effect.

| Step | 50% estimate (min) | Local safety (min) |
|---|---|---|
| Find keys | 1 | 5 |
| Drive | 45 | 30 |
| Park | 10 | 5 |
| Check in | 7 | 30 |
| Security | 7 | 30 |
| **Total** | **70 (1:10)** | **170 with safety (2:50)** |

The 50% sum leaves no room for the slightest delay, and the 90% sum over-protects because "there’s very little chance that everything will go wrong" (L3935). The numbers are an illustration, not data.

The second reason is what is being protected. Only one date matters, and "Because it isn’t important if any one task on my way to airport finishes late, I do not need to buffer the on-time completion of the tasks" (L3937). The remedy in [[schedule-buffer]] takes local safety off the tasks and puts a fraction of it into one shared buffer (L3943).

## The behavioural argument, and whether it survives

Cohn adds that moving safety off tasks defeats two effects: [[parkinsons-law]], that work expands to fill the time available, and student syndrome, starting at the last moment that still allows success (L3954). His conclusion is that "a shorter schedule that includes a schedule buffer is more likely to be met than is a longer schedule" (L3954).

Both mechanisms depend on a human executor. This wiki reads them as not transferring directly: an agent has no reason to stretch work to fill an allowance or to delay its start. The aggregation argument above is statistical and stands regardless of who executes, within the assumption stated on [[project-buffer-sizing]]. So for an agent the case for moving safety rests on the shorter plan alone, and the claim that a shorter plan is more likely to be met has no support here. The person steering may still show both effects when reviewing.

## Trade-off

Removing local safety means individual tasks overrun about half the time, on purpose. That is only workable if an overrun of a 50% figure is not treated as a fault. Cohn notes that people pad "if they expect to be beaten up if they are wrong" (L4041). This wiki reads that as the way local safety returns: chase task-level overruns and the estimates quietly drift back to 90%, and [[buffer-versus-padding]] then stacks a buffer on them.

## Sign

A plan whose date is the plain sum of task estimates, where those estimates were given as numbers someone felt safe with. This sign is this wiki's. The question to ask is which point on the [[completion-time-distribution]] the numbers name.
