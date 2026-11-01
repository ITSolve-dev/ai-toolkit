---
title: Blocked Work Counts Against WIP
category: moving-work
summary: A blocked item stays in its column and counts toward that column's limit, so that being stopped restrains further pulling; moving it aside hides the stop.
tags: [rule, wip, work-states, kanban]
sources: [radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-01
---

# Blocked Work Counts Against WIP

A blocked item stays where it stopped and keeps its place in the count. This is the direct answer the Kanban Maturity Model gives, as reported in [[radzikowska-waiting-blocked]]:

> Because of their negative effects on service delivery, blocked work items usually are marked by means of a symbol or a sticky note of a preselected color. They stay in the swim lane and column in which they are blocked, and they add to the WIP for that column. This might create tension because it impedes pulling work into the column, but it also encourages fast resolution of blockages.
>
> — [[radzikowska-waiting-blocked]], L34

## The rule

An item that is blocked ([[waiting-versus-blocked]]) stays in its state and counts toward that state's limit. It is marked as blocked, not moved.

## Sign of violation

- **In board state:** an unresolved blocked item sitting in a column other than the one it stopped in, or a holding column for blocked items that no limit covers.
- **In board history:** an item moved backward or sideways at the moment it stopped, and returned later to the same state.
- **In board state:** a state at its limit with blocked items not counted, and new work being pulled into it.

The source states the rule. These signs are this wiki's derivation from it.

## Why

What breaks is the signal. If a blocked item leaves the count, the state has room again and work continues to be pulled, so the stop has no effect on anything and nothing forces attention to it. The source's own wording is that counting "impedes pulling" and that this "encourages fast resolution" (L34). The waiting case is different: an item that cannot be shortened goes to a [[parking-lot]] instead, which has its own bookkeeping.

## Cost

The rule stops work on purpose, and the source calls that a stressor. It warns against adopting it early, and gives organizational maturity as the deciding factor:

> Hence, including blocked or waiting items in work in progress limits too soon (when you recognize that your organization is at Maturity Level 0, 1, or 2) may result in too much stress, too heavy resistance, and rejecting the practice.
>
> — [[radzikowska-waiting-blocked]], L76

This wiki does not keep that as a condition of the rule, because maturity level is not on a board and resistance is about people. It keeps it as a cost: expect objections, and expect a period in which pulling stops.

## Agent executor note

The source's mechanism is human: "tension" among people who feel the stop. An agent feels nothing, so that part does not survive. The mechanical part does, and is arguably stronger: an agent that is not allowed to pull will stop pulling, so the pressure lands entirely on the people steering, who see no new results. Whether that produces faster resolution for a few people is not shown by this source, which reports no measurement of any kind.

## Positions

**Kanban Maturity Model:** blocked items stay and count, as above. The source places these practices at Maturity Levels 3 and 4 (L74). Other methodologies' positions will be added here as sources are ingested.
