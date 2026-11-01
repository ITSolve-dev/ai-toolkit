---
title: Utilization Versus Slack
category: periods
summary: Loading to full capacity leaves nothing to absorb the variability of real tasks; keep a margin. The source gives the reasoning and an analogy, and no figure for the margin.
tags: [rule, iterations, capacity, human-mechanism]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Utilization Versus Slack

A plan can aim at keeping everyone busy or at keeping room for tasks that run differently than expected, and Cohn holds that these pull against each other. He names the pursuit of full use as one of two reasons multitasking arises on a traditional project.

> Second, it encourages focusing on achieving a high level of utilization of all individuals on the project rather than on maintaining sufficient slack to cope with the inherent variability in typical project tasks. Loading everyone to 100% of capacity has the same effect as loading a highway to 100% of capacity: no one can make any forward progress.
>
> — [[cohn-agile-estimating-planning]], L646

Chapter 22 repeats the point as a guideline at the level of a period: "Especially when planning an iteration, do not plan on using 100% of every team member’s time." (L4941). The text is on [[filling-a-period]].

This wiki treats the highway as an analogy and not as evidence. Cohn reports no measurement and gives no figure for how much slack is sufficient.

## The rule

Do not fill a period to the full capacity figure. Leave a margin for tasks that run long, and do not plan that margin away with other work. The wording is this wiki's, from Cohn's reasoning.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Capacity for the period | As on [[filling-a-period]] |
| How much finishes vary | Board history: spread of time in state for tasks of one size step |

The margin was too small if tasks repeatedly go back unfinished ([[unfinished-at-period-end]]). It was too large if the margin is never used, period after period. This wiki reads [[filling-a-period]]'s test for a selection that is too small as compatible with holding slack, since a real margin gets used by variability in most periods.

## Sign of violation

- **In a plan:** a selection built by adding estimates until they equal capacity, with nothing set aside.
- **In board history:** any overrun in a period forces something else out or late, because nothing could absorb it.

These signs are this wiki's. The charter excludes individual load, so they are read at the level of the period and not per person.

## Why

What breaks, on Cohn's account, is the ability to absorb variation. This wiki reads the consequence as an overrun on a fully loaded plan having nowhere to go, so it falls on other tasks, and it invites the partial deliveries described on [[multitasking]].

## Cost

This wiki notes the plain cost: a plan with a margin promises less than one without, and it reads as idle capacity to anyone counting.

## Which setup this applies under

Under an iteration setup, as above. Under a flow setup nothing is selected for a period ([[what-may-move]]), so this rule has no direct form there, and this wiki has no sourced equivalent.

## Agent executor note

Cohn's concern is individuals at full utilization. An idle agent costs almost nothing, so keeping an agent busy is not a goal and the human form of the argument does not transfer. This wiki reads the scarce resource as the review of the people steering, as on [[wip-control]] and [[filling-a-period]], and the margin as belonging there: results arriving at the full rate those people can review leave no room for one that takes longer. That reading is unmeasured.
