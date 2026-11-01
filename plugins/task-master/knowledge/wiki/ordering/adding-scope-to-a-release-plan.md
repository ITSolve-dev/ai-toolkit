---
title: Adding Scope to a Release Plan
category: ordering
summary: New features enter a release after being estimated and compared on forecast value; the date moves only if the gain justifies it and the feature cannot ship afterwards.
tags: [decision-rule, release-planning, scope-change, value, prioritization, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Adding Scope to a Release Plan

A release plan is a prediction made at one moment, so a discovery that changes what is worth building is a reason to replan and not a threat to the plan. In the fictional case study of [[cohn-agile-estimating-planning]], an analyst brings two new features to the team. A tester calls it scope creep and says the team was already at the upper end of its range (L6342). She answers:

> Plans are always point in time predictions about the future. We just found a better future to aim at.
>
> — [[cohn-agile-estimating-planning]], L6344

## Inputs and where each is read from

- **Size of the candidates:** estimated by the team, which "split some of her original stories and combined others" (L6358). Online play came to 30 points. Characters came to 15 for the first and 5 for each further one, 35 for five.
- **Value of the candidates:** a revenue forecast from outside the board, built here on buyer conversations and financial models (L6350, L6360).
- **Effect on the date:** [[reforecasting-a-release-from-velocity]] on the new total.
- **Whether the feature can wait for a later release:** the project's setup and market.

## The rule

The smaller candidate lost. Characters were taken at 35 points and online play left out at 30, because the forecasts showed characters likely to generate more revenue (L6360). This wiki reads that as size pricing the option and value deciding it.

The product manager's acceptance test has two conditions, joined by "and":

> I’m completely willing to change the date of the project if we can make enough more money and it’s not a big delay.
>
> — [[cohn-agile-estimating-planning]], L6346

The case also states when he would have refused the delay.

> If we could have released a version 1.0 without characters and then added characters later, I would have done that. But we can’t do that in our industry.
>
> — [[cohn-agile-estimating-planning]], L6500

This wiki reads that as the first branch of the test: a later release comes first, and the date moves only for what has no later release to go to. Where a setup releases continuously, that branch will usually take the feature.

## Points do not hold every cost

The 30 points for online play sat beside "space in a data center", hardware and staff (L6336), which were discussed as partnering options (L6338). This wiki notes that a comparison on points alone would have missed them. Costs outside the team's work belong next to the estimate.

## Where discovery comes from

A survey ranks a known list and does not widen it.

> Questionnaires are good for prioritizing what we already know
>
> — [[cohn-agile-estimating-planning]], L6350

The two features had appeared in some replies, "not enough that I thought there was a trend" (L6350), and conversations with likely buyers confirmed them. This wiki's reading is that a weak signal in intake calls for a direct check, neither dismissal nor immediate acceptance.

## What later fact would show the choice wrong

The value forecast would, and revenue is not on a board, so the check falls outside the plugin. The plugin can state which forecast the decision rested on. The case reports only the product manager's confidence (L6478, L6500), and no results.

## What it costs

The date moves, and in the case the CEO told about it was not pleased at first (L6318). The plan's margin also shrank to near zero, which led to [[droppable-stories-as-a-schedule-buffer]]. Whether the delay stays defensible is tested by [[chosen-delay-versus-slip]]. For value as an ordering input, see [[cost-of-delay]] and [[ordering-by-value-and-urgency]]. The case's analyst calls the characters an exciter (L6340), which is a category on [[kano-model]].

## Which setup this applies under

The resolution here is this wiki's. Under an iteration setup the addition belongs at a period boundary ([[mid-period-change]]), as it does in the case. The rule on levers still applies, so the date is one choice among several ([[changing-the-plan-without-changing-the-date]]).

## Agent executor note

This wiki reads the rule as independent of who executes. An agent may surface new work while running a task, but the value forecast and the decision to move a date stay with the person steering.
