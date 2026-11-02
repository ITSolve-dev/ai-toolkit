---
title: Work In Progress
category: reading-history
summary: WIP is the count of work items between a process's arrival and departure points; it is counted and not sized, it is not the sum of WIP limits, and it excludes most of the backlog and can be segmented by type. A configured limit is not the WIP in the process: limits are broken, a changed limit may leave average WIP unchanged, and pull policy sets the real level, so WIP is read from counts in board history.
tags: [concept, wip, flow, metrics, kanban, vacanti, failure-mode, board-rules, pull, retrospective]
sources: [vacanti-actionable-agile-metrics, kanban-guide]
created: 2026-11-02
updated: 2026-11-02
---

# Work In Progress

Work In Progress (WIP) is "All discrete units of customer value that have entered a given process but have not exited" ([[vacanti-actionable-agile-metrics]] L600). It is the first of the [[flow-metrics]] and the one the other two are defined against. Vacanti calls it the hardest of the three to define and the easiest to measure (L564, L606). This page defines the count. The bound on it is [[wip-control]].

## Two parts of the definition

**Work.** Any direct or indirect discrete unit of customer value is a candidate. The generic term is "work item", which may be a user story, epic, feature, project, requirement, use case or enhancement; what is captured and how it is named is left to the team (L566).

**In progress.** This depends entirely on the [[started-and-finished-points]], which Vacanti calls the process's arrival and departure points. An item counts from the first until the second.

## Measuring it

"To calculate WIP you simply count the discrete number of work items within your process boundaries as defined above. That’s it: just count." (L606)

**Count, do not size.** Vacanti rejects weighting: WIP needs no Story Points or ideal hours, and items need not share a size or complexity (L608-L610). The chapter asks the reader to "suspend disbelief" and defers the argument to the Little's Law chapter (L610-L612); the grounds are on [[right-sizing-not-same-sizing]]. He goes further than the metric: "you need to abandon that type of thinking if you truly want to build predictable processes" (L610).

That line conflicts with sources that make relative estimation central. This wiki resolves it by use, not by side: the source's claim concerns counting WIP and predictability, while a size scale used to decide whether a task should be cut answers a different question and is untouched by it ([[size-ceiling]]). On a project set up around points and velocity, WIP is still counted in items. The price of counting items is on [[hidden-wip-in-large-items]].

**The level is free.** WIP can be tracked at portfolio, project, feature, epic or story level (L614-L620). This wiki adds a condition the source leaves implicit: one count mixes levels only at the cost of meaning, since a count of items is comparable only with a count at the same level.

## WIP is not the sum of WIP limits

"You cannot calculate WIP simply by adding up all the WIP limits on your board." (L622) Boards rarely sit exactly at their limits: columns run below them, and limit violations are common, often in several columns at once. So the sum is wrong in both directions, and "you still have to actively track the total number of work items in your process" (L622). The other ways a limit and the count come apart are in the next section.

**Sign:** a reported WIP figure equals the sum of the board's column limits. Check against an actual count from the board.

## A WIP limit is not WIP

This failure mode treats the WIP limits configured on a board as if they were the amount of WIP actually in the process. Vacanti states it directly: "Setting a WIP limit is not necessarily the same as limiting Work In Progress" ([[vacanti-actionable-agile-metrics]] L1052). Running a Kanban system does not by itself satisfy the assumptions of [[littles-law]] (L1044).

### Three ways the gap opens

| What happens | Source | Sign, as this wiki reads it from board history |
|---|---|---|
| Limits exist and are routinely broken | "teams I come across that set WIP Limits but then routinely violate them" (L1052) | Column counts above the column's limit, repeatedly |
| A limit changes and average WIP does not | "changing WIP limits may have no effect on total average WIP", for example around a clear systemic bottleneck (L1046) | A limit was edited, and average open count before and after is about the same |
| Pull policy decides the real level | "Average WIP over a time period is highly dependent on pull policies in place" (L1054) | Average WIP sits well below, or pinned at, the sum of limits |

Vacanti names the unchanged average as one reason the "forecasted" behaviour expected from the law may not appear when limits are changed (L1046).

### The rule

Do not report WIP by adding up the limits: "you cannot just simply add up all the WIP Limits on your board and think that you have calculated WIP for your process" (L1056). Vacanti's instruction is to track the WIP physically present (L1056).

This wiki's reading for the plugin: any statement about WIP is taken from counts of items open in board history, and the limits serve only as the policy those counts are compared against.

### Why a limit still matters

Vacanti does not argue against limits. He restates the common claim that Little's Law is the best reason for Kanban, in a form he prefers: it is "the single greatest reason to move to a more WIP-limited, pull-based, continuous flow process" (L1058). This wiki reads the point as a discrimination between a declared limit, which is configuration, and a limited process, which is a fact shown in history.

### Trade-offs

Reading real WIP requires board history over time, not only a snapshot of current columns. The source's bottleneck example also implies, in this wiki's reading, that a limit honoured in a place the bottleneck already restrains changes little (L1046), so a limit that is kept is not thereby doing anything.

### Which setup this applies under

This wiki's resolution by setup: a project with no WIP limits has no such gap, but it also has no declared policy to audit, and the sign to look at is the open count itself. Whether a limit should exist at all under each setup is decided on [[wip-control]] and [[board-rules-by-setup]].

This wiki's reading for an agent: the failure survives unchanged, because it concerns a count against a configured number. A limit stored in project configuration binds an agent only if the agent actually reads it before starting, so a declared limit with no check is the same gap in a new form.

## Backlog is mostly excluded

Items sitting in a backlog usually do not qualify, because they have not passed the point of commitment (L624). The source flags this as a subtlety and defers it to its Chapter 8.

**Sign (this wiki's reading):** a figure described as WIP that moves when the backlog is groomed. A real WIP count changes only when items cross a boundary.

## Segmenting

WIP can be viewed whole or split into types. The source's example is a team serving sales, marketing and finance while maintaining existing applications, which could be viewed as one group or by each of those (L626-L634). The split carries through to the other metrics: "If your team does segment WIP into different categories, then it is also going to be valid to talk about the Cycle Time and Throughput of those different type segments." (L634) The chapter does not say when to split, only that it can be "desirable" in some contexts (L634).

## Why it comes first

Vacanti's strongest claim for WIP is prescriptive: "if your team ever wants to have any hope of operating a predictable process, then you are going to have to get control of WIP" (L636). This chapter gives only the definitional reason, that the other two metrics are defined in terms of it. The reasoning from queues is on [[wip-control]], and the relation among the three is on [[littles-law]].

## Positions

**Vacanti:** "entered a given process but have not exited" (L600).

**Kanban Guide:** "The number of work items started but not finished." ([[kanban-guide]] L159). This wiki reads the two as one definition, since each depends on a project's own two points.

## Agent executor note

This wiki reads the count as independent of the executor: it depends on what crossed a boundary, not on who did the work. Whether controlling it brings the same benefit with an agent is a separate question, taken up on [[wip-control]] and [[starting-more-work]].
