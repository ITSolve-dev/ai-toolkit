---
title: Arrival Point
category: work-states
summary: A process needs one explicit point at which work counts as WIP; on most boards it is a WIP-limited first column that signals commitment and is not a backlog.
tags: [rule, arrivals-column, commitment-point, backlog, ready-column, explicit-policy, flow]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Arrival Point

The arrival point is the explicit place where a request becomes work the team has taken on. It is the board form of the started side of [[started-and-finished-points]]. Vacanti requires one for any predictable process, because the Arrival Rate of [[conservation-of-flow]] cannot be counted without it: "Any predictable process needs a clear, unambiguous point at which it considers items to have “arrived”." ([[vacanti-actionable-agile-metrics]] L2202)

It is defined as “an explicit and obvious entry point where teams can pull in new work such that it is counted as WIP” (L2014). It usually takes the form of a WIP-limited first column named “Input”, “Ready”, “To Do” or the like (L2014-L2020). Placing an item there is “a clear, unambiguous signal to the world that the team has accepted work.” (L2026)

## The three policies

The source makes these explicit (L2036):

1. An item has arrived only once it is placed on the arrivals column.
2. The column has a WIP limit, and new work is pulled in only when that limit signals capacity. See [[arrivals-column-wip-limit]].
3. Work can arrive only through this column, so downstream steps may pull only from it.

## Arrivals column versus backlog

This wiki takes the discriminating criterion to be whether the place represents capacity or demand. [[backlog-versus-commitment]] holds the argument about the backlog itself.

| | Arrivals column | Backlog |
|---|---|---|
| Purpose | Work the team has accepted | Candidate requests |
| Size | Bounded by a WIP limit | Unbounded |
| Counts as WIP | Yes | No |
| Shown on a CFD | Yes | No (L2028) |

The column “is not meant to be an ever-expanding repository for all candidate customer requests.” (L2028) Its limit represents “the real-time capacity of the system to take on new work” (L2028).

## Why it matters

The source ranks this as one of the most important columns, if not the most important, for two reasons (L2184-L2188):

- **Throttle.** It is “the throttle by which we constrain the amount of work that can arrive to our system at any given time.” (L2186)
- **Commitment.** It acts as "our “commitment” point to start new work", with the implication that "when new work is committed to, we expect it will flow completely through the process and depart the system." (L2188)

This wiki reads the commitment clause as the meaning of moving an item here: placing an item on the column is a claim that it will be finished, not a note that it might be.

## Against the started point

[[started-and-finished-points]] sets started at the first moment a task takes up capacity, and gives the agent taking the task as the example. Vacanti counts an item as WIP from the column, before anyone has touched it. This wiki reconciles the two by reading a slot on a limited column as capacity, so on a board with such a column the clock starts at the column, and time waiting there counts as Cycle Time. The reconciliation is ours. On an unlimited first column the slot means nothing, so the column is a backlog under another name and the started point falls later.

## Signs

Each sign raises a question to check.

- The first column has no limit, or its count only grows: it is probably a backlog under another name.
- Items appear in a working column without having passed through the first column: policy 3 is not held, and arrivals are being undercounted.
- Items sit on the first column for a long time, or are often removed from it: the column may be storing candidates and not commitments.
- Nothing on the board distinguishes requested from accepted, so the Arrival Rate cannot be read at all.

These signs are this wiki's application of L2014-L2036; the source states the policies, not their signs.

## Trade-offs

An explicit column adds a coordination step and is not always needed; see [[when-an-arrivals-column-is-needed]]. Which items go on the column, and in what order they leave it, is deliberately left out of Vacanti's Chapter 7 (L2176).

The definition concerns a boundary, not who does the work, so this wiki keeps it unchanged for a person steering an agent.
