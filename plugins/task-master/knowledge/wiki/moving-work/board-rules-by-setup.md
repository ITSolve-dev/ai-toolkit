---
title: Board Rules by Setup
category: moving-work
summary: The lookup from a project's setup to the rule that holds for moving, limiting and committing; two switches, a fixed period and a WIP control, resolve where Kanban and Scrum differ, and neither guide says when to pick the other.
tags: [decision-rule, wip, iterations, kanban, scrum]
sources: [kanban-guide, scrum-guide-2020]
created: 2026-11-01
updated: 2026-11-02
---

# Board Rules by Setup

The charter says the rule for what moves where depends on a choice made when a project is set up. This page is the lookup. The reasoning for each row is on the page it links to.

Two switches describe a setup, and the plugin can read both from project configuration: whether there is a fixed period, and whether there is a stated WIP control. That reduction is this wiki's. The guides do not describe themselves as settings of a switch.

## The setups

- **Flow setup:** no period, and a WIP control. This is the Kanban Guide's position.
- **Iteration setup:** a fixed period with a goal, and no WIP control. This is what the Scrum Guide's mechanics amount to, although it is not Scrum ([[scrum-guide-2020]]).
- **Iterations with a WIP control:** both. Each guide allows this. The Kanban Guide says "Kanban can and should be used to augment those delivery techniques." ([[kanban-guide]] L96), and the Scrum Guide says Scrum "functions well as a container for other techniques, methodologies, and practices." ([[scrum-guide-2020]] L327). Neither guide names the other, so reading these lines as permitting this pairing is this wiki's step.
- **Neither switch:** this is not a setup any source supports, so the plugin should ask.

## What holds under each

| Question | Flow setup | Iteration setup | Iterations with a WIP control | Page |
|---|---|---|---|---|
| What lets a task start? | The count falls below the bound | Selected for the period | Selected, and the count is below the bound | [[what-may-move]] |
| Is concurrent work limited? | Yes, by the stated bound | Not by the guide; the period bounds the total only | Yes, by the stated bound | [[wip-control]] |
| What is promised? | Nothing for a period; a forecast per task | The period's goal; the items are a forecast | The period's goal | [[commitment-over-a-period]] |
| How much goes in? | Replenished on the signal | Filled from history at the start | Filled from history, started on the signal | [[filling-a-period]] |
| Can the list change mid-way? | Yes, up to the moment of starting | Yes, if the goal is safe | Yes, if the goal is safe | [[mid-period-change]] |
| What if a task is unfinished? | It stays and ages | It goes back and is ordered again | It goes back and is ordered again | [[unfinished-at-period-end]] |
| What is the expectation for a task's life? | The SLE | The period | The period, and the SLE if kept | [[overrun-triggers-a-recut]] |
| What is the size ceiling? | Likely to finish inside the SLE | Fits inside the period, and a fraction of it, or inside the SLE if kept | Fits inside the period, and a fraction of it, or inside the SLE if kept | [[size-ceiling]] |
| Does a blocked task count? | Yes | There is no count to join | Yes | [[blocked-work-counts-against-wip]] |
| Can a stopped task leave its place? | Only as a declared exception, in a narrow case | No: there is nothing to gain | Only as a declared exception, in a narrow case | [[parking-lot]] |
| Can a task go back? | No | Only by returning to the unstarted pile at a period's end | Only by returning to the unstarted pile at a period's end | [[backward-movement]] |

## Choosing a setup

Neither guide says when to pick the other. The Kanban Guide claims to "work with virtually any workflow" (L88), and the Scrum Guide claims "adaptive solutions for complex problems" (L61). So the rule below is this wiki's and is built from what each mechanism needs. It rests on no comparison of the two.

| Input | Read from |
|---|---|
| Whether one objective can be stated for the coming period | The tasks waiting, as a test: can a sentence cover them without being a list |
| How often work must start that was not known at the start of a period | Intake history |
| Whether someone needs to know what a period will deliver | The people steering |

Prefer an iteration setup when one objective can honestly be stated and the people steering want a commitment on it. Prefer a flow setup when work arrives as a stream of unrelated items, because a goal would then only be a list, and a protected period would keep refusing urgent work. Add a WIP control to an iteration setup when the executor can start the whole selection at once, because the period restrains the total and not the moment.

The choice was wrong if, under iterations, goals repeatedly restate the selection or go obsolete mid-period, or urgent work keeps forcing cancellations. It was wrong if, under flow, the people steering repeatedly ask what will be done by a date and the board cannot answer.

## Agent executor note

The third setup is likely to matter most here, and that reading is this wiki's. The Scrum Guide assumes people, whose own hours limit how much starts at once. An agent has no such limit, so an iteration setup with no WIP control could start everything on the first day, and the guide has nothing to say about it.
