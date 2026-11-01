---
title: Departure Point
category: work-states
summary: A process needs one exact point past which work no longer counts as WIP; it must be counted even if it is not visualized.
tags: [rule, done, done-column, explicit-policy, throughput, flow]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Departure Point

The departure point is the exact line past which an item stops being work in progress. It is the board form of the finished side of [[started-and-finished-points]]. "Any predictable process needs a clear, unambiguous point at which it considers items to have “departed”." ([[vacanti-actionable-agile-metrics]] L2204) The Departure Rate of [[conservation-of-flow]], and with it [[throughput]], is a count of items crossing this line.

The requirement is to “define the exact point of the system where work departs, (hopefully) never to return.” (L2050) The source's examples are deploying code to production and handing an item to a downstream team (L2050).

## What the point requires

- **It must be counted, not necessarily shown.** Items past the point “do not necessarily have to be visualized” but “they do need to be counted” (L2050). Most teams give it board space, titled “Done”, “Deployed” or similar.
- **It has no WIP limit.** If shown, the column typically carries none (L2050, L2082).
- **It needs an explicit policy.** The expectation is that the team “has put in place a set of policies for what it means for items to move from Test to Deployed” (L2060).
- **It releases capacity.** Once across, “they no longer count against the capacity of the team; i.e., they no longer count as WIP.” (L2060)

## Why it matters

The source ties value and measurement to this line: “It is only when work departs our system that customer value can truly be recognized and our predictability be assessed.” (L2188) This wiki adds the consequence: without the line, items leave WIP at no defined moment, so neither the Departure Rate nor the finish date of an item means anything.

## Signs

These signs are this wiki's application of L2050-L2062; each raises a question to check.

- Board history has no single transition that all finished items cross.
- A “Done” column has no stated policy for entering it, so two items in it may mean different things; see [[column-doneness-criteria]].
- Items return from the departed state, against “(hopefully) never to return”: the line may sit too early.
- Finished work waits in a state before the line with nobody acting on it: the line may sit past the point where the team's part ended.

## Choosing where the line falls

The source gives no test for where to put the line beyond the two examples. Its examples do show that the line need not mean the work reached a user: a handoff to a downstream team also counts (L2050). This wiki reads that as a choice of what the measured system is, so a board's cycle time and throughput are only comparable to figures measured with the same line.

For a person steering an agent, this wiki reads the same choice as deciding whether acceptance of an agent's result falls inside the system. Whichever is chosen, see the note on [[conservation-of-flow]]. Related: [[arrival-point]].
