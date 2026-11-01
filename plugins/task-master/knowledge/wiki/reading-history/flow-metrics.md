---
title: Flow Metrics
category: reading-history
summary: The four measures the Kanban Guide requires, WIP, Throughput, Work Item Age and Cycle Time, what each counts and does not, and why all of them can be read from board history without logged hours.
tags: [concept, flow-metrics, board-history, kanban]
sources: [kanban-guide, scrum-guide-2020, kanban-playbook-right-sizing]
created: 2026-11-01
updated: 2026-11-01
---

# Flow Metrics

The Kanban Guide requires four measures of a workflow and calls them "mandatory" (L157). This page is descriptive: it fixes what each one counts, so that other pages can use the names.

> - **WIP**: The number of work items started but not finished.
> - **Throughput**: The number of work items finished per unit of time. Note the measurement of throughput is the exact count of work items.
> - **Work Item Age**: The elapsed time between when a work item started and the current date.
> - **Cycle Time**: The elapsed time between when a work item started and when a work item finished.
>
> — [[kanban-guide]], L159-L162

## What each measures and does not

| Metric | Reads | Applies to | What it does not say |
|---|---|---|---|
| WIP | A count now | Open items | Whether any of them is moving |
| Throughput | A count over a time | Finished items | How large or how valuable the items were, because it counts items and the count depends on the cut |
| Work Item Age | Elapsed time so far | Open items only | How long the item will take; it can only rise while the item is open |
| Cycle Time | Elapsed time, complete | Finished items only | Anything about items still open, so it lags: the oldest open items are not in it yet |

The right-hand column is this wiki's reading, drawn from the definitions. The Guide states the definitions and leaves their limits to the reader.

## What the numbers rest on

All four depend on where a project put its [[started-and-finished-points]]: "started and finished refer to how the Kanban system members have established those points in their DoW." (L166). Two projects' cycle times are not comparable unless those points match.

The Guide also limits their use: "In and of themselves, these metrics are meaningless unless they can inform one or more of the three Kanban practices." (L168). This wiki reads that as a test for reporting: a number that changes no decision about limiting, aging or improving should not be reported as a finding. The Guide allows other names for the same measures (L164), so a board calling Cycle Time "Flow Time" means the same thing.

## Two ways the numbers mislead

Because the metrics count items, the cut can distort them in both directions. A large task hides work under a count of one ([[hidden-wip-in-large-items]]). Tasks that deliver nothing close fast and look healthy, which the Kanban Playbook calls "the opposite illusion" ([[kanban-playbook-right-sizing]] L20, and see [[component-task-masquerading]]). The Playbook says the two "look completely different in your data" (L20). This wiki reads the second as the harder case: a large task at least shows up as an outlier, while tasks that deliver nothing show up as health, so only reading the tasks catches them.

## Read from history

All four come from timestamps of state changes. That matches the charter's position that the time a task lived is read from board history and that logged hours are out of scope. Both ages are elapsed time, so they include nights, weekends, and time nobody touched the item. For an agent-run task that is the point, because the elapsed time includes the time a result sat waiting for a person.

## Positions

**Kanban Guide:** the four are required, and a project may add others (L170). All are measured against its own points.

**Scrum Guide:** no metric is required, and the word "velocity" does not occur in it. It mentions forecasting practices and declines to rank them: "Various practices exist to forecast progress, like burn-downs, burn-ups, or cumulative flows. While proven useful, these do not replace the importance of empiricism." ([[scrum-guide-2020]] L202). The input it does name is "past performance" (L222), left undefined. This wiki reads the empirical stance as compatible with all four metrics, and an iteration setup can keep them for free, since they come from the same timestamps.

## Agent executor note

The definitions are counts and timestamps, so they survive an agent executing. Their interpretation does not transfer: a figure formed on a human team says nothing about an agent's board, and Throughput in particular is cheap to raise by cutting finer.
