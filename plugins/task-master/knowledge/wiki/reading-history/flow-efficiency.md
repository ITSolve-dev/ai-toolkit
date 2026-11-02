---
title: Flow Efficiency
category: reading-history
summary: Flow Efficiency is active or touched time as a percentage of total Cycle Time, computed at Siemens HS from queue states plus blocked time; a low ratio says improvement lies in the waits and not the work, and its input needs a board whose states separate waiting from working.
tags: [method, flow-efficiency, cycle-time, waiting, flow, failures, vacanti, time-in-state]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Flow Efficiency

Flow Efficiency is a diagnostic built on [[cycle-time]]: "the ratio of the total elapsed time that an item was actively worked on to the total elapsed time that it took for an item to complete (its total Cycle Time)" ([[vacanti-actionable-agile-metrics]] L706). Vacanti uses it for an "overall picture of your process’s health" (L706).

## The calculation

The source treats an item in flow as being in one of two states: actively worked on, or not. Inactive examples are being blocked by an external dependency such as a team or vendor, and queuing while waiting to be pulled (L706). Both accumulate Cycle Time.

"To get Flow Efficiency, you take the Total Cycle Time, subtract out inactive time and then divide that result by the Total Cycle Time." (L706)

Flow Efficiency = (Total Cycle Time − inactive time) / Total Cycle Time

Worked example from the source: a story that took 20 days at 15% had 3 active days and 17 inactive days (L708).

## The Siemens HS form

The [[siemens-hs-case]] gives the same calculation as a procedure against a board (L4184-L4190):

1. Take total Cycle Time for the item from board history.
2. Add time in queue states, at Siemens the "specifying done and developing done" column.
3. Add any further blocked time. The sum of steps 2 and 3 is what the source there calls "wait time".
4. Subtract it: "Subtracting “wait time” from total Cycle Time gives us “touched time”."
5. Divide touched time by Cycle Time and express it as a percentage.

The two inputs are defined separately. "Wait time is the time a story sits in an inactive or done queue because moving to the next active state is prevented by WIP limits." and "Blocked time is the time work on a story is impeded, including impediments such as build-breaks, defects, waiting for customer validation etc." (L4184). The passage then uses "wait time" for the sum of both, so this wiki reads the word by context there. See [[waiting-versus-blocked]].

## Where each input is read from

Chapter 2 does not say. The Siemens form reads queue time from columns and takes blocks "directly by the tool" (L4184). This wiki's reading is that both inputs come from board history, since the charter excludes logged hours: total Cycle Time from the [[started-and-finished-points]], inactive time from time spent in queue columns and blocked states. So the method needs a board whose states separate waiting from working ([[active-versus-queued]]), and a record of blocks. On a board with one "in progress" column, all elapsed time reads as active, and the ratio reports nothing true. That is the sign to look for before computing it.

## What the result chooses

A low ratio directs attention to inactive time. The source's reasoning is about leverage: the 3 active days are "probably going to be very hard to improve" while the 17 hold "tons of opportunities" (L714), and any cut in inactive time reduces Cycle Time by definition (L714). Hence: "Looking at wait time is usually the best, easiest, cheapest area to investigate first for process improvement." (L714)

**What would show this choice wrong (this wiki's reading):** inactive time falls while total Cycle Time does not, which would mean that waiting moved between states and was not removed.

The chapter on Siemens does not state a split by cause; this one is this wiki's reading. Low efficiency with queue time dominant points at capacity or policy: read [[reading-a-cfd]]. Low efficiency with blocked time dominant points at the causes of blocks. High efficiency with long Cycle Time suggests the items are large; see [[hidden-wip-in-large-items]].

## Conditions on the 15% figure

The source's setting is "teams just starting out with managing for flow" (L708), stated as "not uncommon", with no data behind it. The charter grades a practitioner source on mechanisms, so this wiki keeps the mechanism, that waits dominate and are cheaper to attack, and does not use 15% as a benchmark. The Siemens chapter gives no value and no threshold, and its claim that the figure is a "powerful" KPI (L4190) carries no evidence.

## Limits

- The chapter's example is a single story. It does not say how to aggregate across items, or how many items a reading needs.
- The active/inactive split is binary. A wait a team cannot affect, such as a vendor's ([[waiting-versus-blocked]]), counts the same as an internal queue, so a low ratio says where time went, not what can be changed. This caution is this wiki's.
- This wiki reads "touched" as a residual and not an observation. An item in an active column with nobody on it counts as touched, so the figure is a ceiling. It supports comparison over time on one board, and it does not by itself say whether the process is good.

## Agent executor note

The calculation survives. The interpretation needs care, and this reading is ours: an agent's active time is short by construction, so a low ratio is close to guaranteed, and it carries less news than for human teams. The useful reading is the composition of the inactive time, such as waiting to be briefed, waiting for review, or blocked, because those are the waits a person steering controls. Absolute inactive time matters more here than the ratio, and the ratio should not be compared with figures from human teams, only with the same board's own past.
