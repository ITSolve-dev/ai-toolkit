---
title: Activity-Based Plan
category: cutting-work
summary: A plan that lists what will be done rather than what will be delivered, and counts progress by activities completed; the plan can finish on paper with nothing received, and its reviews look for forgotten steps rather than missing features.
tags: [failure-mode, decomposition, planning, vertical-slice]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Activity-Based Plan

An activity-based plan lists the work to be performed rather than the results to be delivered, and measures progress by the activities completed. Cohn names it the first cause of planning failure, in the setting of a traditionally managed project tracked with a Gantt chart or work breakdown structure ([[cohn-agile-estimating-planning]] L543). A board can take the same shape: the unit it counts is then something someone does, and not something anyone receives.

> A first problem with activity-based planning is that customers get no value from the completion of activities. Features are the unit of customer value. Planning should, therefore, be at the level of features, not activities.
>
> — [[cohn-agile-estimating-planning]], L543

This wiki reads "feature" here as the level at which a plan is stated and counted. Cohn does not say in this chapter how large a feature is, so this page sets no size, and [[size-ceiling]] does that work.

Chapter 22 returns to the rule as a reason agile planning works: "A traditional plan in the form of a Gantt chart, PERT chart, or work breakdown structure focuses on the tasks needed to create a product. An agile plan focuses instead on the features that will be needed in the product." (L4863).

**Terminology.** Cohn's "task" is an activity one level below a feature or story. This wiki's task ([[unit-of-work]]) sits at the level of his feature. So his rule says that a plan's units are this wiki's tasks, and that his tasks do not belong in it. A Gantt chart can meet the rule if it stops at features ([[gantt-at-feature-level]]).

## The rule

State the plan and count progress in results someone can receive. Activities may exist inside a unit, but they are not what the plan counts. Each item in a plan names something the product will do or be, and an item that names an activity is either inside another item or a sign that the work was cut by discipline. This wording is this wiki's, from Cohn's rule above.

## Observable signs

- **In task text:** the title names an act of building and not a result. Cohn's Figure 2.1 has four such items: "Add tables to database", "Code middle tier", "Code the user interface" and "Test" (L586).
- **Across tasks:** a request is cut by role or phase, with a closing "Test" item that everything else feeds into.
- **In a report:** progress is given as activities finished. Cohn says of the activity list "This becomes how we measure the progress of the team." (L543).
- **In a review of the plan:** the question asked is what has been left off the to-do list. Cohn's wording is "When we review a schedule showing activities we do so looking for forgotten activities rather than for missing features." (L545).
- **After an overrun:** quality is reduced to save time, or a change-control policy appears. Cohn says such policies are "designed to constrain product changes, even highly valuable changes." (L547).
- **In a plan:** the titles would be unchanged for a different product. Cohn's observation is the basis: "At a task level, many project plans look the same; every agile plan is specific to the product being developed." (L4869). Turning that into a test, by swapping the product's name and seeing whether the plan still reads, is this wiki's.

The signs in task text and across tasks are this wiki's reading of Cohn's figure. The report, review and overrun signs are Cohn's.

## Why

Four things break.

- **Progress stops meaning anything.** Every activity can be finished with nothing delivered, because activities carry no value of their own (L543).
- **Review looks in the wrong place.** A reviewer checks the list for completeness as a list of steps, so a missing feature is not looked for (L545).
- **Overruns become likely.** Cohn gives three reasons: "Activities don’t finish early", "Lateness is passed down the schedule" and "Activities are not independent" (L549-L553). Each has its own page: [[parkinsons-law]], [[lateness-passes-down-the-schedule]] and [[similar-tasks-overrun-together]].
- **A plan can look complete without understanding.** Cohn quotes Highsmith: “It is easy to plan an entire project using standard tasks without really understanding the product being built. When planning by feature, the team has a much better understanding of the product.” (L4869). This wiki reads the breakage as a plan nobody can question, since no one can say what the product gains from it.

## Relation to a component task

[[component-task-masquerading]] describes one item that has nothing to present. This wiki reads the activity-based plan as the same defect at the level of the whole plan. The two signs do not fully overlap: "Test" is neither a layer nor an artifact, so a phase item is caught here and not by the component test. The remedy is the one on that page, which is to combine the pieces into a [[vertical-slice]] and not to cut them smaller.

## Cost

Cohn names no cost in this chapter. This wiki's reading is that a plan stated in results hides the order of steps inside each result, and that work serving several results has no natural home. Combining pieces also makes items larger, which can push them against [[size-ceiling]]. Activities that belong to no feature, such as upgrades and infrastructure, have no natural place in such a plan, and Chapter 22 does not address them. [[vertical-slice]] and [[component-task-masquerading]] treat the neighbouring cases.

## Agent executor note

Cohn's central reason concerns what a receiver gets and does not depend on who executes, so it survives. This wiki adds that an agent will carry out an activity item as readily as any other, so nothing on the executor's side pushes back on the cut. The overrun mechanisms survive to different degrees, and each linked page says how far.

Half of Chapter 22's argument depends on a human executor:

> When features are developed iteratively there is less need for upfront thinking about the specific tasks necessary. The work of an iteration emerges and the team will think of or discover all of the tasks as they are needed.
>
> — [[cohn-agile-estimating-planning]], L4869

This wiki reads the survival of that passage in two parts. Planning at feature level survives, because it concerns what the plan is about. Leaving the rest to emerge survives only for the steps. An executor that guesses where a person would recall does not fill gaps from context, so purpose, boundaries and acceptance have to be in the text ([[underspecified-task]], [[recoverable-versus-task-only-facts]]). Expanding a task into steps is out of scope for this wiki either way.
