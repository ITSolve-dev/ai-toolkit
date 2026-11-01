---
title: Changing the Plan Without Changing the Date
category: periods
summary: When something is learned the plan changes, but the date is only one lever; scope can be dropped or reduced instead, and a change with no named learning is suspect.
tags: [decision-rule, planning, scope, replanning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Changing the Plan Without Changing the Date

The rule separates two things that are often merged: revising a plan and moving its date. Cohn:

> Just because we’re changing the plan does not mean we change the dates.
>
> — [[cohn-agile-estimating-planning]], L487

## The decision

**Should the plan change?** Yes, if something was learned; no, otherwise.

> We don’t want to change the plan just for the sake of changing, but we want to change because change means we’ve learned something or that we’ve avoided a mistake.
>
> — [[cohn-agile-estimating-planning]], L483

Cohn's examples of learning are that users want more of one feature or less of another, that usability matters more than believed, and that a new language takes longer than expected (L483). He adds that the financial impact of each can be assessed and, "if worthy," can alter plan and schedule (L483).

**Which lever?** Cohn lists "We can drop a feature, we can reduce the scope of a feature, we can possibly add people to the project, and so on." (L487). Moving the date is one option among these and does not have to come first.

## Inputs and where they are read

This wiki's reading of what the rule needs, since Cohn gives no procedure:

- **What was learned:** a discovery recorded on a task, or a task that took materially more or less than forecast.
- **Whether the date is fixed:** stated by whoever needs the date, in the project's setup or the request.
- **What can be cut:** open tasks ordered by value, per [[tradeoff-needs-cost-and-benefit]].

**What later fact would show the choice wrong.** The cut scope is requested again soon after the date, or the date is still missed after the cut.

## Failure signs

These are this wiki's questions to check:

- A date moved with no scope considered: the board's history shows the date changing while the open scope is unchanged.
- Order or scope reshuffled with no stated reason, which is the "for the sake of changing" case.
- Learning recorded with no change to the plan, which is the failure Cohn warns of under [[plan-conformance-as-success]].

## Trade-offs

Cutting scope to hold a date costs value, and Cohn's June example shows that sometimes a slightly later date with more features is the better answer (L403). This wiki reads the rule as not favouring dates: it only keeps the date from being the automatic lever. Where the date is the fixed thing from the start, the rule becomes [[fixed-date-variable-scope]]. Within a running period, [[mid-period-change]] governs what may move. When the learning is a new feature worth having, [[adding-scope-to-a-release-plan]] decides whether it enters.

## Agent executor note

For a few people steering an agent, this wiki reads "add people" as usually unavailable, which makes dropping and reducing scope the practical levers alongside the date. Cohn hedges the lever himself with "possibly" (L487).
