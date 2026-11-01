---
title: When an Arrivals Column Is Needed
category: work-states
summary: An explicit arrivals column is optional when work can be pulled ad hoc without outside coordination; balance then comes from constant WIP alone.
tags: [decision-rule, arrivals-column, board-setup, kanban, wip-limit]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# When an Arrivals Column Is Needed

A board usually has an explicit [[arrival-point]] column, but “an explicit arrivals column is neither prescribed nor required for predictable process design.” ([[vacanti-actionable-agile-metrics]] L2170) This page holds the test for deciding whether a board needs one.

## The test

The input is whether pulling new work needs coordination with someone outside the team. It is read from how the project's priorities are set.

- **The column may be superfluous** when a team can “pull new work items in an immediate, ad hoc manner”, because “you need no coordination with any external stakeholder to prioritize items or you have a proxy for those stakeholders embedded with your team.” (L2162)
- **Keep the column** otherwise. This wiki reads the default this way because the column is then where the coordinated decision lands, a reading the source implies but does not state.

## What holds balance without the column

The requirement does not go away. Dropping the column means arrivals are matched to departures by [[constant-wip]] alone: per-step limits, one global limit, or a mix (L2168). The arrival point itself also remains required, since Arrival Rate must still be counted (L2202). This wiki reads the first working column as taking that role, so the moment an item is pulled into it is the moment it arrives.

## Trade-offs

The source says even such a team “could benefit from an arrivals column” but does not say why here (L2170). What is lost, per the two reasons it gives elsewhere, is a named throttle and a visible commitment signal (L2186-L2188).

## What would show the choice wrong

This wiki reads these as the later facts, unsourced:

- WIP drifts upward, since nothing visible throttles intake.
- People outside the team begin asking which items have been accepted, so the signal the column gave turns out to be needed.

## Setup note

A few people steering an agent, with priorities decided by those same people, fit the first case on the source's test. This wiki reads the column there as optional and not forbidden: the choice should be made at project setup and stated, not left implicit.
