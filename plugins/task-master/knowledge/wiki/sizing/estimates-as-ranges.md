---
title: Estimates as Ranges
category: sizing
summary: Early estimates should carry their uncertainty as a range and narrow as uncertainty is removed; a single unqualified date or a precise figure on imprecise work is the sign of ignoring it.
tags: [rule, estimation, uncertainty, forecast]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Estimates as Ranges

A date given for uncertain work should show how uncertain it is. Cohn names ignored uncertainty the fourth cause of planning failure, and says it appears as false precision: we "pretend we can assign precise estimates (“2 weeks”) to imprecise work" ([[cohn-agile-estimating-planning]] L660), and schedules are "expressed as a single, unqualified date" (L662).

> During the earliest part of a project we are the most uncertain. The estimates we give should reflect our uncertainty. One way of doing this is by expressing the end date as a range.
>
> — [[cohn-agile-estimating-planning]], L662

Cohn's pair of examples is “We will ship on June 30,” against “We’ll ship sometime between June and August,” (L662). This wiki reads a range as one way of stating uncertainty and not the only one: Cohn says "One way".

## The rule

Give a date for uncertain work as a range, whose width reflects how much is still unknown. Narrow it as the unknowns are removed. Cohn's words are "As the project progresses and as uncertainty and risk are removed from the project, estimates can be refined and made more precise." (L662). This is the [[cone-of-uncertainty]] applied to a stated date, and [[single-date-plan]] is the wider failure of a forecast that carries nothing else with it. What removes the unknowns is on [[iterating-reduces-uncertainty]]. How a release plan words it, and which of scope or date takes the range, is on [[stating-plan-uncertainty]].

## Sign of violation

- **In a stated date:** a single date, with no range or stated uncertainty, for work not yet begun.
- **In board history:** the same width, or the same date, is repeated as the work proceeds, so nothing learned has reached the estimate.

The first is Cohn's. The second is this wiki's derivation.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How much of the work is still undone or unclear | Board state and task text |
| How similar work actually ran | Board history |

The range was wrong if actual finishes repeatedly land outside it, or if it never narrows. Cohn gives no method for setting the width in this chapter.

## Why

What breaks is what a listener takes from the number. This wiki reads a single date as seeming more known than it is, which invites [[estimate-versus-commitment]]. Cohn also says that plans which ignore uncertainty about how to build miss activities, which raises the chance of lateness, dropped features or inappropriate quality trade-offs (L680).

## Limit

Cohn's example is a project's end date, in months. This wiki reads the same reasoning as covering any stated date, and it does not extend to a size step, which states no date at all ([[size-ceiling]]).

## Cost

This wiki notes that a range does not give someone with a fixed deadline what they asked for, and a wide one can read as evasion. Choosing the date to hold to is then a separate decision ([[estimate-versus-commitment]]).

## Agent executor note

The rule concerns what is known and not who works, so it survives. This wiki adds a plugin-side consequence: anything the plugin says about when work will be done should come out as a range or as a forecast from history, because a point date from a tool reads as more exact than a person's guess. The width of an agent-executed project is unsourced here, and history from a different setup is a poor guide to it, as [[filling-a-period]] notes.
