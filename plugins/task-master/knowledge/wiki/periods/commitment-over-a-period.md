---
title: Commitment Over a Period
category: periods
summary: What a project actually promises; the Scrum Guide commits to a Sprint Goal and only forecasts the items, the Kanban Guide has no period and forecasts per item, and a board reported as a list of promised items misstates both.
tags: [decision-rule, commitment, iterations, scrum, kanban]
sources: [scrum-guide-2020, kanban-guide]
created: 2026-11-01
updated: 2026-11-01
---

# Commitment Over a Period

A commitment is what the project will answer for at the end of a time span. The two guides differ on this more sharply than on anything else, and the setup decides which holds.

## Scrum Guide: the goal is the commitment

> The Sprint Goal is the single objective for the Sprint. Although the Sprint Goal is a commitment by the Developers, it provides flexibility in terms of the exact work needed to achieve it.
>
> — [[scrum-guide-2020]], L301

The Guide does not make the items the commitment. Its word for the selection is a forecast: "the more confident they will be in their Sprint forecasts" (L222). Its other two commitments are a Product Goal for the backlog and the Definition of Done for the Increment (L266-L270). The Product Goal comes one at a time: "They must fulfill (or abandon) one objective before taking on the next." (L291).

This wiki reads that as the central point. The Guide promises an outcome and leaves the list of work free to change, and [[mid-period-change]] is the same idea applied during the period.

## Kanban Guide: no period, a forecast per item

The Kanban Guide has no period and uses the word "commitment" only as a benefit of limiting WIP (L143). Its nearest equivalent is the [[service-level-expectation]], a forecast with a probability for each item. Nothing in the Guide promises what a given week will contain.

## The decision

Ask what the project will answer for, and read it from the setup.

- **Iteration setup:** one objective for the period. Selected tasks are a forecast of how to reach it. A period is reported as goal met or not met, and not as a share of items finished.
- **Flow setup:** no period commitment exists. Each started task carries the SLE. A question about what will be done by a date is a forecast from history, and this wiki has no page yet on how to compute one.
- **Iterations with a WIP control:** the period's goal is the commitment, and the SLE, if the project keeps one, is a forecast inside it.

The Guides do not resolve this between them, because each describes only itself. The per-setup statement is this wiki's.

## Sign of violation

- **In the goal's text:** the goal restates the selection, so that removing any item would break it. The Guide says a goal "provides flexibility in terms of the exact work", so a goal with no such flexibility is a list.
- **In a report on a period:** results are given as items promised against items delivered, with the goal unmentioned.
- **In board history:** a period closed as a failure with its goal met, or as a success with its goal missed.
- **On a flow board:** a date given for a batch of items, with no history behind it.

These signs are this wiki's.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Whether the project has fixed periods | Project configuration |
| The goal for the period | The period's record |
| Whether one objective can be stated for it | The tasks being considered |

The commitment was shaped wrongly if the goal went obsolete during the period, or if nobody could say at the end whether it was met.

## A period versus a milestone

Neither guide uses the word "milestone". The distinction below is this wiki's, built from what the Scrum Guide says about each.

- **A period fixes time and lets scope move.** Sprints are "fixed length events" (L189), and scope may be "clarified and renegotiated" (L198).
- **A milestone fixes a result and lets the date move.** The nearest thing in the Guide is the Product Goal, "a future state of the product" (L284), which has no date.

The test is which of the two gives way when they collide. If the date holds and scope gives, it is a period. If the result holds and the date gives, it is a milestone. A plan that fixes both has no room to absorb anything.

## What a period does not do

A period is not a release gate. The Guide says "an Increment may be delivered to stakeholders prior to the end of the Sprint. The Sprint Review should never be considered a gate to releasing value." (L309). The sign, in this wiki's wording, is finished tasks whose release dates cluster at the end of each period regardless of when they were finished. A task's finish point is on [[started-and-finished-points]].

## Agent executor note

The Guide says the goal is "a commitment by the Developers". An agent cannot answer for a commitment, so the commitment falls to the people steering, and an agent's report that a goal is met is only an input to their judgement. The Guide's claim that a goal creates "coherence and focus" (L301) is a claim about people working together. This wiki does not carry it over. What survives for an agent is the single objective as a test for what belongs in the period.
