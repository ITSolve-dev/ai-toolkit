---
title: A WIP Limit Is Not WIP
category: moving-work
summary: Having WIP limits does not guarantee Little's Law's assumptions; limits may be violated, may not change average WIP, and do not add up to the WIP actually in the process.
tags: [failure-mode, wip, kanban, board-rules, pull, retrospective]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# A WIP Limit Is Not WIP

This failure mode treats the WIP limits configured on a board as if they were the amount of [[work-in-progress]] actually in the process. Vacanti states it directly: "Setting a WIP limit is not necessarily the same as limiting Work In Progress" ([[vacanti-actionable-agile-metrics]] L1052). Running a Kanban system does not by itself satisfy the assumptions of [[littles-law]] (L1044).

## Three ways the gap opens

| What happens | Source | Sign, as this wiki reads it from board history |
|---|---|---|
| Limits exist and are routinely broken | "teams I come across that set WIP Limits but then routinely violate them" (L1052) | Column counts above the column's limit, repeatedly |
| A limit changes and average WIP does not | "changing WIP limits may have no effect on total average WIP", for example around a clear systemic bottleneck (L1046) | A limit was edited, and average open count before and after is about the same |
| Pull policy decides the real level | "Average WIP over a time period is highly dependent on pull policies in place" (L1054) | Average WIP sits well below, or pinned at, the sum of limits |

Vacanti names the unchanged average as one reason the "forecasted" behaviour expected from the law may not appear when limits are changed (L1046).

## The rule

Do not report WIP by adding up the limits: "you cannot just simply add up all the WIP Limits on your board and think that you have calculated WIP for your process" (L1056). Vacanti's instruction is to track the WIP physically present (L1056).

This wiki's reading for the plugin: any statement about WIP is taken from counts of items open in board history, and the limits serve only as the policy those counts are compared against.

## Why a limit still matters

Vacanti does not argue against limits. He restates the common claim that Little's Law is the best reason for Kanban, in a form he prefers: it is "the single greatest reason to move to a more WIP-limited, pull-based, continuous flow process" (L1058). This wiki reads the point as a discrimination between a declared limit, which is configuration, and a limited process, which is a fact shown in history.

## Trade-offs

Reading real WIP requires board history over time, not only a snapshot of current columns. The source's bottleneck example also implies, in this wiki's reading, that a limit honoured in a place the bottleneck already restrains changes little (L1046), so a limit that is kept is not thereby doing anything.

## Which setup this applies under

This wiki's resolution by setup: a project with no WIP limits has no such gap, but it also has no declared policy to audit, and the sign to look at is the open count itself. Whether a limit should exist at all under each setup is decided on [[wip-control]] and [[board-rules-by-setup]].

## Agent executor note

This wiki's reading: the failure survives unchanged, because it concerns a count against a configured number. A limit stored in project configuration binds an agent only if the agent actually reads it before starting, so a declared limit with no check is the same gap in a new form.
