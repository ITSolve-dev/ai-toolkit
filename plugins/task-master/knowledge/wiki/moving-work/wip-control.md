---
title: WIP Control
category: moving-work
summary: An explicit bound on how many tasks may be started and not finished; the Kanban Guide requires one over the whole workflow in any form, treats running under it as a departure too, and wants exceptions declared in advance, and Vacanti reaches it from the queue, with one count that both measures and stops.
tags: [rule, wip, kanban, flow, queues]
sources: [kanban-guide, scrum-guide-2020, radzikowska-waiting-blocked, cohn-agile-estimating-planning, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# WIP Control

WIP control is an explicit bound on how many tasks may sit between a project's started and finished points at once. The Kanban Guide makes it mandatory:

> Kanban system members must explicitly control the number of work items in a workflow from started to finished. That control can be represented on a Kanban board in any way that Kanban system members deem appropriate. Ideally, the system would operate neither above nor below the agreed upon control.
>
> — [[kanban-guide]], L139

This wiki reads three things from that passage and its neighbours.

- **The bound is on the workflow, not necessarily on a column.** The span is "from started to finished" (L139), and the 2025 edition lists "Less explicit (and hence more flexible) how WIP is controlled" among its changes (L204). A limit per column is one allowed form, and one number for the whole span is another.
- **The count is set by position and not by activity.** The Guide says "Any work items between a started point and a finished point are considered work in progress (WIP)." (L112). A stopped item is therefore still WIP unless the project has declared otherwise ([[blocked-work-counts-against-wip]]). Vacanti's definition agrees: "All discrete units of customer value that have entered a given process but have not exited" ([[vacanti-actionable-agile-metrics]] L600). The count is of what is there, and [[work-in-progress]] defines it; a sum of the limits is no substitute.
- **Running under the bound is also a departure.** The Guide's words are "neither above nor below".

## The rule

A project states a bound on the number of started, unfinished tasks, and nothing starts past that bound. An allowed exception is stated in advance. The Guide says "Any acceptable exceptions to controlling WIP should be made explicit as part of the DoW." (L143).

## Sign of violation

- **In board state:** more tasks between started and finished than the stated bound, with no declared exception covering the excess.
- **In board history:** a task started at a moment when the count was already at the bound.
- **In board history:** the started, unfinished count rises week over week while the number finished per week stays flat. This shows on a project that never stated a bound, so the sign does not depend on a missing field. It is the first policy Vacanti lists as self-inflicted: "you start new work at a faster rate than you finish old work" ([[vacanti-actionable-agile-metrics]] L232).
- **In board history:** the count stays well under the bound while ready tasks sit unstarted. This is the "below" departure.

The Guide states the rule. These signs are this wiki's derivation from it.

## Why

What breaks is the start signal. The Guide says "An effect of controlling WIP is that it should create a pull system" (L141). Without a bound, nothing on the board says when to stop starting, and [[what-may-move]] has no trigger to read.

The Guide also claims that controlling WIP "helps flow and often improves the Kanban system members’ collective focus, commitment, and collaboration." (L143). It reports no measurement. This wiki keeps "helps flow" only through the pull signal, and it treats the rest under the agent note below.

Vacanti reaches the bound from the queue. Since the aim is that queues never form ([[starting-more-work]]), they have to be measured, and he says the measure is a plain count:

> The best way to measure a queue is to simply count the number of items you are working on at any given time. When that number gets too big then no new work gets started until something old has finished.
>
> — [[vacanti-actionable-agile-metrics]], L440

This wiki reads two things from that passage. The start of new work is tied to a finish event, so a slot opens only when something old leaves. And the count is both a measure and a control: the same number reports the queue and stops it. The usual response that defeats the bound is on [[starting-more-work]].

## Choosing the number

The Guide requires a control and gives no number and no way of choosing one. Vacanti's Chapter 1 says only "too big" ([[vacanti-actionable-agile-metrics]] L440), also with no number and no method. The only method in this base is the Kanban Maturity Model's for a parking lot, which starts "slightly higher than the average WIP" ([[radzikowska-waiting-blocked]] L61; see [[parking-lot]]). Carrying that method over to a whole workflow is this wiki's extension, and no source states it.

| Input | Read from |
|---|---|
| The started, unfinished count over recent history | Board history |
| How many results the people steering can review in the time a task is expected to live | Board history: the time tasks spend waiting for review |

The number is too high if it is never reached, because it then restrains nothing. It is too low if it is reached constantly while nothing is waiting for the people steering, because capacity then sits idle.

## Cost

Ready work stays unstarted while an executor may be free. The rule accepts that on purpose. Vacanti says it plainly: "It will mean saying no to customer requests to start new work immediately." ([[vacanti-actionable-agile-metrics]] L234). With an agent the cost is easy to see and tempting to avoid, because starting another run costs almost nothing at the moment it is started.

## Agent executor note

The benefits the Guide names, "focus, commitment, and collaboration" (L143), are human and do not survive: an agent has no focus to protect. The mechanical part survives, because a count on the board stops a start whoever executes.

What changes is what the bound protects. With people executing, it protects their attention. With an agent executing, this wiki reads the scarce thing as the review and decisions of the people steering, since everything an agent finishes lands with them. So the number follows what they can absorb and not how many runs an agent can hold. That reading is this wiki's, and no source here tests it.

## Positions

**Kanban Guide:** required, in any form, over the started-to-finished span (L139).

**Kanban Maturity Model:** the limit is per column, and blocked items add to it ([[blocked-work-counts-against-wip]]).

**Cohn:** the limit is per developer, one or two sub-story cards at a time ([[wip-per-executor]]). What work in process does to cycle time is on [[starting-more-work]].

**Vacanti:** count the items in progress, and when the count is too big, start nothing until something finishes ([[vacanti-actionable-agile-metrics]] L440). His later policy states the same thing as a rate, starting new work "at about the same rate that we finish old work" ([[vacanti-actionable-agile-metrics]] L1018), which this wiki sets beside the bound on [[littles-law]].

**Scrum Guide:** there is no limit on concurrent work. The term "WIP" does not occur in it. What the Guide limits is the objective and the total. There is one Sprint Goal, "the single objective for the Sprint" ([[scrum-guide-2020]] L301), and one Product Goal at a time: "They must fulfill (or abandon) one objective before taking on the next." (L291). The selection for a period bounds how much is taken on over the period ([[filling-a-period]]). None of this bounds how much is open at one moment. How work proceeds inside the period is left to the team, which is self-managing, "meaning they internally decide who does what, when, and how." (L114).

## Which holds under which setup

The two guides do not contradict each other, because they limit different things: the Kanban Guide limits the moment, and the Scrum Guide limits the period. Each permits the other's addition ([[board-rules-by-setup]]). The resolution below is this wiki's.

- **Flow setup:** a WIP control is required, because it is the only thing that makes a start signal.
- **Iteration setup with people executing:** the period's selection is the only bound the Guide gives, and people's own hours restrain the moment.
- **Iteration setup with an agent executing:** add a WIP control. An agent can start the whole selection at once, so the period restrains nothing at the moment that matters, and nothing in the selection protects the people who have to review it.

The last point would be shown wrong if the bound was never reached over several periods, or if results reached the people steering no faster than they could review them with no bound in place.
