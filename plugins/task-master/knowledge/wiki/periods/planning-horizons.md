---
title: Planning Horizons
category: periods
summary: Plan at the release, iteration and day levels, with detail shrinking as the horizon nears and each level doing a different job, so none replaces another; a plan that runs past what can be seen needs built-in points to look again.
tags: [rule, iterations, planning-levels, release, uncertainty]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Planning Horizons

A planning horizon is the distance ahead at which a plan can still be trusted. Cohn's position is that a plan loses accuracy quickly past that distance, so planning happens at several nested levels, each with its own reach and its own grain, rather than once for the whole project.

## The rule

Cohn says "the accuracy of a plan decreases rapidly the further we attempt to plan beyond where we can see." ([[cohn-agile-estimating-planning]] L820).

His illustration is a small boat: eyes nine feet above the water see slightly over four miles, so a twenty-mile trip needs at least five looks ahead (L820). This wiki reads the arithmetic as exact only for the boat, and the figure as an analogy and not a planning number.

Cohn states the risk, and it has two parts that must both hold:

> A project is at risk if its planning extends well beyond the planner’s horizon and does not include time for the planner to raise her head, look at the new horizon, and make adjustments.
>
> — [[cohn-agile-estimating-planning]], L822

This wiki reads that as saying a long plan alone is not the defect. The defect is a long plan with no scheduled point at which it is looked at again.

## The three levels

Cohn says "The three horizons are the release, the iteration, and the current day." (L828). His planning onion places product, portfolio and strategy outside them, and "Most agile teams are only concerned with the three innermost levels of the planning onion." (L837).

| Level | Reach (L896) | Grain | Precision (L4857) | Revised |
|---|---|---|---|---|
| Release | Typically three to six months | User stories or themes; answers scope, schedule, resources (L837) | "the least precise of all" | Usually at the start of each iteration (L837) |
| Iteration | Typically one to four weeks | Tasks that turn a feature request into working, tested software (L839) | Less precise than a day's plan, because each story is imperfectly specified | At the start of each iteration (L839) |
| Day | The next day (L841) | Tasks and the activities leading to their completion (L841-L845) | Fairly precise | Daily |

Cohn makes the link between reach and grain explicit: "Because we are looking at a closer horizon than with release planning, the components of the plan can be smaller." (L839). At release level he says the plan contains "only a prioritized list of desired user stories and one or more estimates of how much of the desired functionality is likely to be delivered by the desired release date" (L4857).

## What each level is for

> Do not make the mistake of thinking that a release plan makes an iteration plan unnecessary, or the other way around.
>
> — [[cohn-agile-estimating-planning]], L4913

Cohn gives two benefits (L4857, L4859). Different levels make plain that plans exist for different reasons, so no level has to hold precision it cannot have. They also give different views of the project: the iteration plan coordinates work inside a short period, while "A release plan provides a broader perspective on the project and ensures that the team does not lose the forest of the release for the trees of an iteration." (L4859).

This wiki's reading is that a plan should be judged against the precision of its own level: a release plan that lists tasks is over-precise, and a daily plan that lists themes is useless. [[stating-plan-uncertainty]] gives the test.

## Failure when a level is missing

> A team that works iteration to iteration without awareness of a more distant goal runs the risk of continually pursuing short-term goals while missing out on targeting a truly lucrative longer-term goal.
>
> — [[cohn-agile-estimating-planning]], L4859

## Signs to check

Cohn gives the risk statements above but no board-level sign. This wiki reads the following as what to check; each raises a question, not a verdict.

- A plan with dated commitments far ahead and no marked point at which it will be revised.
- Far-off work already cut to task grain, which spends cutting effort on detail past the horizon and will be stale when reached ([[how-far-to-split-up-front]]).
- Near work still held at release grain when an iteration is about to take it.
- **No release level:** a project has iterations but no stated goal beyond the next one, and each iteration's work cannot be related to any forecast. A small project may need no release plan at all.
- **No iteration level:** tasks are started directly from a long list, and nothing states what the next period is meant to produce.

## Trade-offs

This wiki notes that revising at each level costs repeated effort, and that a plan that keeps moving offers less to promise against. It reads Cohn as accepting this cost because the alternative is precision that the horizon does not support ([[cone-of-uncertainty]]).

## Which setup this applies under

The three levels assume an iteration setup. Under a flow setup there is no iteration level, leaving a release or milestone horizon and the next tasks to be started. This wiki reads the two-part risk as still holding there, with the point of looking again supplied by something other than the start of an iteration. That reading is this wiki's, and Cohn does not address it. [[commitment-over-a-period]] covers the difference between those arrangements.

## Agent executor note

This wiki reads the horizon argument as surviving an agent executing, because its mechanism is what is unknown about the future, not how a person works. The reaches in the table are figures from human teams and should not be carried over as they stand. The daily level rests on a standup, "team member commitments made to each other" (L896), a human coordination mechanism that does not transfer; what survives is only that the nearest plan has the shortest reach and the smallest grain. Chapter 22 places it in "a team’s daily meeting" (L4857), and running such a meeting is out of scope in any case.

The iteration level's stated reason, "the highly coordinated work of a cross-functional team" (L4859), also assumes people. This wiki reads a few people steering an agent as possibly needing that level for a different reason, which is to plan what they can review in a period. That reading is unmeasured.

Related: [[release-versus-iteration]], [[timeboxed-iteration]], [[replanning-on-new-knowledge]], [[fixed-date-variable-scope]].
