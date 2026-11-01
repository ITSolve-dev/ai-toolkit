---
title: Mismatched Arrivals and Departures
category: showing-work
summary: When the top CFD line climbs faster than the bottom line, WIP grows, Cycle Time lengthens, and the process is unstable and cannot be predicted.
tags: [failure-mode, cfd, stability, wip, predictability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Mismatched Arrivals and Departures

Mismatched arrivals and departures is the shape of a [[cumulative-flow-diagram]] in which work enters the process faster than it leaves. It is the first check in [[reading-a-cfd]], and the chart's form of a breach of [[conservation-of-flow]]. The procedure for reading the balance is [[reading-flow-balance-on-a-cfd]].

## Sign

"the slope of the top-most line is steeper than the slope of the bottom-most line" ([[vacanti-actionable-agile-metrics]] L1800). In board history, this wiki reads that as the count of items entering the first tracked state rising faster than the count reaching the last one, over the same window.

## What breaks

When items arrive faster than they depart, WIP grows over time, and Vacanti says an increase in WIP "will almost certainly lead to an increase in Cycle Time" (L1802-L1808). Arrival rate equalling departure rate on average is also one of the key assumptions behind [[littles-law]] (L1808), so the arithmetic that would support a forecast stops holding.

"It is impossible to be predictable in a world where WIP constantly increases and Cycle Times elongate." (L1808)

"By definition, a process that exhibits a shape similar to Figure 6.1 is unstable." (L1810) Vacanti calls stability "fundamental to process predictability" (L1810), and defers causes and remedies to his Chapter 7; see [[arrivals-column-wip-limit]] and [[constant-wip]].

## What separates it from a neighbouring case

The assumption is about rates "on average" (L1808), so a short mismatch is not this pattern. His Chapter 6 gives no window length. This wiki reads the sign as a slope difference that persists, with the gap between the lines still widening at the end of the window. The steep start and flat end of an [[s-curve-on-a-cfd]] are temporary mismatches of a different kind, and belong to that page.

A later fact would show the reading wrong: the two slopes converge without any change to the process.

## With an agent executing

The mechanism is arithmetic on counts, so this wiki holds that it survives an agent executing. The transfer here is ours: where an agent finishes work and a person accepts it, whether the bottom line means "agent finished" or "person accepted" decides what the pattern says. A gap measured to acceptance may be a gap in the person's review and not in execution, which is worth settling before asking why work is not leaving.
