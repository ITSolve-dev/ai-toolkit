---
title: Blocked Work Counts Against WIP
category: moving-work
summary: A blocked item stays in its column and counts toward that column's limit, so that being stopped restrains further pulling; moving it aside hides the stop.
tags: [rule, wip, work-states, kanban]
sources: [radzikowska-waiting-blocked, kanban-guide, scrum-guide-2020, wester-board-design]
created: 2026-11-01
updated: 2026-11-01
---

# Blocked Work Counts Against WIP

A blocked item stays where it stopped and keeps its place in the count. This is the direct answer the Kanban Maturity Model gives, as reported in [[radzikowska-waiting-blocked]]:

> Because of their negative effects on service delivery, blocked work items usually are marked by means of a symbol or a sticky note of a preselected color. They stay in the swim lane and column in which they are blocked, and they add to the WIP for that column. This might create tension because it impedes pulling work into the column, but it also encourages fast resolution of blockages.
>
> — [[radzikowska-waiting-blocked]], L34

The habit this restrains is on [[starting-new-work-when-blocked]].

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

**Kanban Maturity Model:** blocked items stay and count, as above. The source places these practices at Maturity Levels 3 and 4 (L74).

**Kanban Guide:** the Guide does not address blocked items directly. It lists "Unblocking blocked work." ([[kanban-guide]] L135) as a form of active management and does not define the term. Its definition of WIP settles the count all the same, in this wiki's reading: "Any work items between a started point and a finished point are considered work in progress (WIP)." (L112). A blocked item sits between those points, so it counts. A project that wants otherwise has to say so, since "Any acceptable exceptions to controlling WIP should be made explicit as part of the DoW." (L143). The Guide therefore has no maturity gate, and the count applies from the start.

**Wester:** agrees on staying in place, for a further reason: "A better practice is to visualize this kind of wait in the place where it is incurred." ([[wester-board-design]] L53). The post also names what a holding column would hide, which [[column-versus-attribute]] records. Wester argues about columns and does not say in so many words that a blocked item counts, although the complaint about stashing work "so they can get around their WIP limits" (L51) assumes it should.

**Scrum Guide:** the Guide has no count, so the question does not arise in those terms. A stop is an impediment, and the Daily Scrum exists partly to "identify impediments" ([[scrum-guide-2020]] L240). What a stop threatens under Scrum is the goal and not a limit, so the handling goes through [[mid-period-change]].

## Which holds under which setup

- **Flow setup, or iterations with a WIP control:** the item stays in place and counts.
- **Iteration setup with no WIP control:** there is no count to join. The item still stays in place and is marked, because the marker is what shows the stop. Whether the stop endangers the goal becomes the question.

This resolution is this wiki's.
