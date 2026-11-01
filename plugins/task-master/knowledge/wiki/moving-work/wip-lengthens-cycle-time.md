---
title: WIP Lengthens Cycle Time
category: moving-work
summary: Work started and unfinished delays each new feature that must wait behind it; expediting past that queue pushes the problem onto the next feature. Cohn's cycle time ends at delivered value, not at a done column.
tags: [concept, wip, cycle-time, flow-metrics]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# WIP Lengthens Cycle Time

Cohn defines the measure and the cause together. "On a software project, cycle time is the time from when the team begins work on a feature until it delivers value to users. The shorter the cycle time the better." ([[cohn-agile-estimating-planning]] L4873). Work in process "exists on any feature that the team has started developing but has not yet finished" (L4879).

## The mechanism

> High amounts of work in process slow down a team. [...] The more work in process there is, the longer any new feature will take to develop as the new feature must follow along behind the already started work.
>
> — [[cohn-agile-estimating-planning]], L4879

The reasoning is a queue: capacity is occupied by what was started first, so what starts later waits. Cohn draws on queuing theory through Poppendieck and Reinertsen and gives no figures here (L4873). The other named influence on cycle time is variability ([[size-spread]]). Chapter 19 states the same effect as its leading reason against partial credit ([[all-or-nothing-counting]]).

## Expediting does not escape it

The obvious way past the queue is to jump it. Cohn rules that out in a parenthesis: "(Or, the new feature needs to be expedited, jumping ahead of the work in process but that just compounds the problem for the next feature that cannot be expedited.)" (L4879). This wiki reads it as saying that an expedited item adds to work in process and leaves the queue as it was, so the delay moves to whatever comes next.

## Observable signs

- **On the board:** many items started and few finishing, with ages growing.
- **In history:** tasks started later finish before tasks started earlier, repeatedly, which is what expediting looks like.
- **In history:** cycle time rises while the size of tasks stays the same.

The signs are this wiki's derivation. A sign raises a question: tasks of very different size also finish out of order.

## Reading the definition

Cohn's end point is delivered value, which is later than a "done" column on many boards. This wiki notes that board history can give his cycle time only if a state marks delivery. [[started-and-finished-points]] and [[flow-metrics]] cover how the points are chosen. Time between done and delivered is invisible otherwise.

## Which setup this applies under

The mechanism holds under both setups. The controls differ, and that resolution is this wiki's: a flow setup limits WIP directly ([[wip-control]]), and Cohn's iteration setup clears it by the calendar ([[unfinished-at-period-end]]).

## Agent executor note

The queue in Cohn's sentence is a team's capacity. Agents can run in parallel, so a new feature need not "follow along behind" at execution. This wiki expects it to hold at review, where started results wait for the few people steering. That reading is unmeasured. [[interrupting-started-work]] covers the expediting decision.
