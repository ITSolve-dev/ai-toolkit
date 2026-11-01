---
title: Velocity Versus Commitment Planning
category: periods
summary: Two ways to fill an iteration; sum story estimates to last period's velocity, or add stories one at a time until the team can commit no further. Cohn prefers commitment because 3 to 12 stories are too few for estimate errors to average out, so velocity gauges progress against the release and is not a fill line for the next period.
tags: [decision-rule, iterations, velocity, filling, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Velocity Versus Commitment Planning

Cohn describes two ways to decide how much goes into an iteration. They share their first steps, adjusting priorities and identifying a goal, and differ in what stops the selection. He notes they "can be combined to varying degrees" ([[cohn-agile-estimating-planning]] L3091) and "will often result in the creation of the same iteration plan" (L3383).

## Velocity-driven

The team sets a target velocity, then selects top-priority stories that support the goal: "As many stories are selected as necessary for the sum of their ideal day or story point estimates to equal the target velocity." (L3093). Stories are split into tasks and estimated only after that. The target usually comes from one of two figures: "The default assumption by most teams is that their velocity in the next iteration will equal the velocity of the most recent iteration" (L3120), called yesterday's weather, or a moving average over perhaps the last three iterations. A team new to working together must forecast velocity instead (L3122).

## Commitment-driven

The stopping rule is a judgement repeated per story: "the team is asked to add stories to the iteration one-by-one until they can commit to completing no more" (L3276). Each story is selected, split and estimated before the next is considered, because "after each story is split into tasks and the tasks estimated, the team decides whether or not they can commit to delivering that story during the iteration" (L3289). Near the limit, a team may drop a story and replace it with a smaller one (L3301). The check on capacity is on [[iteration-capacity]].

## Why Cohn prefers commitment

Cohn gives two reasons (L3346-L3348). Velocity measures coarse estimates and "is not accurate enough for planning the work of short iterations". And "a team would need to complete twenty to thirty user stories per iteration for errors in the story point or ideal day estimates to average out". He sets that against the count that actually occurs: "most teams plan between three and a dozen stories into each iteration" (L3354).

His illustration is a team with a velocity of thirty over five iterations. Deliberately picking six slightly easy five-point stories could raise that to forty, and picking slightly hard ones could lower it, so a small draw can land lucky or unlucky by chance (L3352-L3354). The conclusion is about scope of use: "since these differences do average out over the course of a release, velocity works extremely well for release planning" (L3356). The same reasoning, applied to a single item, is on [[story-points-do-not-convert-to-hours]].

## Velocity is a gauge and not a quota

The fictional case study in Chapter 23 (L4961) draws the line between the two uses. A team with a velocity of 16 plans 18, and when asked why, the coach answers:

> We use velocity as a guide for measuring our progress against the release plan
>
> — [[cohn-agile-estimating-planning]], L6296

> We don’t automatically plan each new iteration to have exactly the velocity of the last iteration or the average velocity of the last few iterations. We plan each iteration based on how much work we can commit to.
>
> — [[cohn-agile-estimating-planning]], L6296

The points are summed only after the commitment is reached, and the total is expected to land "somewhere close to our historical average, but it’s going to vary" (L6296). The team names what changed: the artist returns to art and away from testing, and one story already has a head start (L6300). Its second plan is also "15 total hours less than the last iteration" (L6304). The plan held, since they "had completed each of the stories they’d planned" (L6310).

This wiki reads a total far from history as a reason to ask what changed, and not as an error. The rule costs a judgement per period where a quota needs only arithmetic, and that judgement can be optimistic, so velocity stays as the check on it.

## Numbers and their conditions

The figures of twenty to thirty and of three to a dozen are Cohn's coaching experience, stated without measurement. The thirty-to-forty swing is a thought experiment and not a recorded result. The 16 and 18 of the case study are invented.

## The decision, by setup

This resolution is this wiki's. Count how many tasks the period holds, in this wiki's sense of task, and see whether a breakdown below that level exists.

- **Iteration setup, twenty or more tasks in a period, stable history on one scale:** velocity can fill the period, since Cohn's own condition for errors averaging out is met.
- **Iteration setup, the usual small selection:** use velocity as a cross-check and not as the filler. Add tasks one at a time in priority order and let the people steering stop when they will not commit. A total above recent velocity is acceptable when something named has changed, as in the case above, and otherwise it is a reason to stop. Cohn's hour sum is unavailable here, because the plugin does not produce the level below a task ([[unit-of-work]]), so the stopping judgement rests on the people steering, informed by [[filling-a-period]].
- **No history yet:** there is no velocity to use, so only the one-at-a-time form applies.
- **Flow setup:** nothing is selected for a period, so neither applies ([[what-may-move]]).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Tasks per period | Board history |
| Velocity, and whether it is stable | Board history, on one scale |
| Top-priority tasks supporting the goal | The ordered backlog and the period's record |
| What changed since the last period | Named by whoever plans |

The choice was wrong if selections equal to velocity keep over- or under-running while the velocity figure itself stays steady. This wiki reads Cohn's mechanism as predicting exactly that when the selection is small. One-at-a-time filling was wrong if the people steering repeatedly commit past what history supports, or if a plan set above recent velocity ends with tasks unfinished.

## Trade-off

Commitment-driven filling costs more, because every story is examined before the next is added. Velocity-driven filling is cheap and can overfill or underfill a period by chance.

## Agent executor note

The averaging argument is statistical and holds for any executor. The value of asking a team whether it can commit depends on people answering for work, and an agent cannot do that ([[commitment-over-a-period]]). A velocity measured before a change of model or review practice is a poor guide ([[filling-a-period]]). The case's first reason for going above velocity rests on one person's specialism and its hours on a human capacity estimate, and this wiki reads neither as transferring. The rule underneath does: a plan total may differ from past velocity when something named has changed, such as prior work on a carried task.

## Related

The stage this page fills is defined on [[iteration-plan-versus-release-plan]]. The measure itself is on [[velocity]].
