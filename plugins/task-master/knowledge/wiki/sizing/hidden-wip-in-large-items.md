---
title: Hidden WIP in Large Items
category: sizing
summary: WIP counts items and not work, so one large task can hold several tasks' worth of work under a count of one; the sign is a cycle time outlier or a task whose text lists separable results.
tags: [failure-mode, sizing, wip, flow-metrics]
sources: [kanban-playbook-right-sizing, kanban-guide]
created: 2026-11-01
updated: 2026-11-01
---

# Hidden WIP in Large Items

A large task counts as one item, whatever it holds. A bound on WIP can therefore be met in number and exceeded in effect. The Kanban Playbook's statement:

> Large items hide more WIP than your board shows. One item that could have been five smaller ones is still five items worth of work in progress. You just cannot see it. That invisible WIP inflates your actual Cycle Time and shows up as outliers in your data.
>
> — [[kanban-playbook-right-sizing]], L18

This wiki reads "five" as the page's illustration and not as a size of effect. The mechanism follows from the Kanban Guide's definitions, which count without weighing: WIP is "The number of work items started but not finished." and Throughput is "the exact count of work items" ([[kanban-guide]] L159-L160). Nothing in [[wip-control]] looks inside an item.

## Observable signs

- **In board history:** a task whose cycle time is far outside the rest of its kind.
- **In board state:** a task whose age has passed the SLE while the WIP count looks normal ([[overrun-triggers-a-recut]]).
- **In task text:** one task naming several separable results ([[compound-task-text-signs]]).
- **In the result:** a single review covers several unrelated changes.

The first sign is the Playbook's. The others are this wiki's.

## What to do

Cut it, by [[story-splitting-patterns]], before it starts if possible. The check before starting is on [[size-ceiling]]. A task that is already running and overdue goes through [[overrun-triggers-a-recut]].

## Agent executor note

The mechanism concerns counting and survives. An agent gives it a different consequence. The human cost is a stretched person. With an agent, one large task is one run that lands as one large result, so the hidden work reappears at review, where one item may take as long as several. This wiki reads that as the main reason the failure matters for a few people steering. That reading is unmeasured.
