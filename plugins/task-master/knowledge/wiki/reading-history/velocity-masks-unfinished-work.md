---
title: Velocity Masks Unfinished Work
category: reading-history
summary: Points completed can look on plan while features stay unfinished, because velocity counts claimed points and says nothing about how much was started.
tags: [failure-mode, velocity, wip, release, signs]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Velocity Masks Unfinished Work

Velocity masking unfinished work is the defect where a period's points look healthy while the work a release actually needs is not finishing. Velocity counts what was claimed. It does not count what was started, so a growing pile of open work leaves it unchanged.

At Siemens HS, the case behind this page ([[siemens-hs-case]]):

> While velocity rates at sprint reviews often seemed good, reality pointed to a large number of stories blocked or incomplete and multiple features in progress with few, if any, features completing until end of the release.
>
> — [[vacanti-actionable-agile-metrics]], L4026

The source names the cause: the gap "was primarily caused by teams starting too many features and/or stories" (L4026). It adds that velocity burn-ups "could look in line with expectations" while features "were not being completed on any regular cadence" (L4026).

## Observable signs

Each sign raises a question to check, not a verdict ([[smell-is-not-a-finding]]).

- Velocity or a burn-up is on plan while the count of finished features stays flat until late in the release.
- Blocked and incomplete stories accumulate across periods.
- Stories are finished, yet the features they belong to stay open. This wiki reads this as the check to run first, because it needs only board history.
- The end of each period shows a rush, in Siemens' case "to claim as many points as possible, resulting in hasty and over-burdened story testing" (L4026). See [[end-of-period-crunch]].
- Testing bottlenecks gather at the end of the release (L4026).

## What breaks

The metric reports progress while the release date slips out of reach, so the plan is trusted until the end, when nothing can be done about it. Siemens' metrics "were not providing the transparency needed to clearly gauge completion dates" (L4018). The cost is also misdirected effort: the organization assumed that better planning and harder work would fix it (L4026), and this wiki notes that this assumption did not address the WIP.

## What to read instead

The source moves to WIP, Cycle Time and Throughput ([[flow-metrics]]). This wiki adds that finished-feature count over time and open-item count over time expose the same gap with no points involved. See also [[velocity]], [[all-or-nothing-counting]] and [[diagnosing-unfinished-work]].

## Agent executor note

The case is 15 Scrum teams with 30-day sprints. This wiki reads the part of the mechanism that depends on people claiming committed points as not transferring directly: an agent has no points to claim. The defect survives anyway, in this wiki's reading, because the count mechanism does not depend on motive. A person steering agents can start work faster than it is presented and reviewed, and a points or tasks-closed count will not show it.
