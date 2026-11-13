---
title: The Kanban Guide (May 2025)
category: moving-work
summary: The minimal definition of Kanban as a strategy for optimizing flow; it requires a stated workflow, explicit control of work in progress, a service level expectation and four flow metrics, and it gives no columns, no order and no period.
tags: [summary, kanban, wip, work-states, flow-metrics]
sources: [kanban-guide]
created: 2026-11-01
updated: 2026-11-01
---

# The Kanban Guide (May 2025)

This is the May 2025 edition of the Kanban Guide, taken from kanbanguides.org. It describes itself as "a unifying reference for the community by offering the minimal guidance for Kanban" (L38). The raw file's `authors` field is empty. The copyright notice names Orderly Disruption Limited and Daniel S. Vacanti, Inc. (L56).

The Guide is normative. It says what its authors require of something called Kanban, and it offers no measurement that the requirements work. Read it as the definition of a position and not as evidence for that position.

## Thesis

Kanban is defined as "a strategy for optimizing the flow of value through a process" (L68), made of three practices: defining and visualizing a workflow, actively managing items in it, and improving it (L70-L72). The Guide makes one thing the root of everything else: "DoW is a fundamental concept of Kanban. All other elements of this guide depend heavily on how workflow is defined." (L106).

A Definition of Workflow (DoW) has six required elements (L110-L115): what a work item is, when one counts as started and finished, the states between those points, how WIP is controlled, the policies for flowing through each state, and a service level expectation.

## What this wiki took from it

- The bound on started, unfinished work, and what counts toward it: [[wip-control]].
- Starting only on a capacity signal, and moving by stated policies: [[what-may-move]].
- Started and finished as defined points that all metrics hang from: [[started-and-finished-points]].
- The forecast of how long an item should take, with its two parts: [[service-level-expectation]].
- The four mandatory metrics: [[flow-metrics]].
- A Guide reading of whether stopped work counts: [[blocked-work-counts-against-wip]] and [[parking-lot]].
- Aging as something to manage against the SLE: [[overrun-triggers-a-recut]].
- The Guide's "work item" in the wiki's vocabulary: [[unit-of-work]].

## What the Guide does not say

These silences matter as much as the requirements, because a reader might assume otherwise.

- **No columns.** The Guide requires "One or more defined states" (L112) and then says "There are no specific guidelines for how a visualization should look." (L125). It offers no state set.
- **No order among items.** Nothing says which item goes next. The one sentence about order, at L117, concerns the order of adopting the DoW elements. A capacity signal says that something may start and not which item.
- **No period.** The word "sprint" and any fixed planning period are absent. The SLE is per item, and reviews "can occur continuously, at regular intervals, or through a combination of both" (L137).
- **No definition of blocked.** "Unblocking blocked work." (L135) is the only mention. The Guide does not say what blocked means or whether a blocked item counts.
- **No backward moves.** Moving an item to an earlier state is not discussed.
- **No estimate.** Nothing is sized. The SLE comes from elapsed time, not from a judgement of effort.

## What this wiki dropped, and why

- **The value framing** (L80-L86): effectiveness, efficiency and predictability, and "the right questions sooner". No sign and no inputs.
- **The claim of universal fit** (L88): "Kanban can be used at any scale and in most contexts where value is delivered." This is an unsupported assertion, and scale is outside the charter's setting.
- **Multiple DoWs** (L121) across groups and levels of an organization. This answers a scaling question.
- **Added values, principles and working agreements** (L119) and the theory list (L94). They are named and not stated.
- **Review cadence** (L137, L151). Reviews are meetings. The one usable point, that a change to the workflow does not have to wait for a formal meeting, has no sign and is left out.
- **The history and the acknowledgments** (L182-L192), except as noted under How to read it.

## Extraction caveat

The raw file carries `[top](#top)` navigation links between sections, with no effect on the text. The license is stated two ways: L58 offers it under Attribution ShareAlike, and L215 says Creative Commons Attribution 4.0 International. This wiki notes the mismatch and does not resolve it.

## How to read it

The Guide is authoritative on what the Kanban Guide's Kanban requires, and on nothing beyond that. "Kanban" is not one school: the [[radzikowska-waiting-blocked]] article speaks for the Kanban Maturity Model, which is a different body of work. Pages in this wiki label a position by its source for that reason. The Guide also thanks Julia Wester among its reviewers (L192), so [[wester-board-design]] is not an independent voice on it.

Most of the mechanisms the Guide offers concern the work and survive an agent executing. The exceptions are stated in human terms, such as "focus, commitment, and collaboration" (L143), and [[wip-control]] handles them.
