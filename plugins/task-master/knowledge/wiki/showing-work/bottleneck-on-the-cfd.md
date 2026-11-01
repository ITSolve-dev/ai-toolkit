---
title: Bottleneck on the CFD
category: showing-work
summary: A queue band that stays wide on a Cumulative Flow Diagram raises a question about capacity at the next step; per-column Throughput and Cycle Time confirm it, because the chart's shape alone names no bottleneck.
tags: [method, cfd, bottleneck, capacity, visualization]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Bottleneck on the CFD

Reading a bottleneck from a [[cumulative-flow-diagram]] means looking for the state where items persistently queue, confirming it with per-column numbers, then acting on that state's capacity. The [[siemens-hs-case]] gives the pattern.

Management saw higher Throughput in developing than in testing across all teams and decided to invest in test automation to rebalance capacity. The source says the sign was easy to see, because "the “developing done” state on the CFD consistently had stories queued up waiting for the “testing” column WIP limits" ([[vacanti-actionable-agile-metrics]] L4192).

## Procedure

1. Look for a queue band, a done sub-state ahead of a limited column, that stays wide over time and does not merely swell once. [[bulging-band-on-a-cfd]] holds the sign.
2. Confirm it by comparing Throughput and Cycle Time per column. Siemens analyzed "Throughput (story run rate) and Cycle Time for each column (specifying, testing and developing)" to see "where we were experiencing capacity problems" (L4184).
3. Choose where to act. At the team level, Siemens adjusted WIP limits "to ensure flow and prevent the build-up of bottlenecks" (L4192). At the program level, it shifted capacity to the constraint, with test automation.
4. Recheck the band. This wiki reads a band that narrows while downstream Throughput rises as confirming the diagnosis.

## A disagreement inside the book

The case and the author do not say the same thing. Of looking at a CFD alone, Chapter 6 says: "It is impossible to spot a systemic bottleneck." (L1944), and [[what-a-cfd-cannot-answer]] keeps that as a rule for wording. The case, told in Vallet's voice, says the shortfall "was actually easy to spot" (L4192).

This wiki resolves it by what the finding rests on. A chart's shape raises the question of where items wait, which is what Chapter 6 allows. Naming a step as the constraint takes the second reading in step 2, which is what the case actually had (L4184). So a finding may name a step only when per-column Throughput or Cycle Time support it, and it says so.

## What it needs

A band like this appears only if the board has a queue state and the next column has a limit. This wiki reads the converse as well: without them the same queue is hidden inside a column; see [[active-versus-queued]] and [[wip-control]].

## What it does not answer

A wide band says where items wait, not why. Whether testing lacks capacity or was starved or disrupted needs other evidence: the source links its testing bottlenecks to builds and environments as well (L4192). This wiki reads a band that grows while the whole diagram widens as a general arrival problem, for which [[conservation-of-flow]] comes first.

## Trade-offs

Adding capacity at a constraint costs money or attention, and it only pays once flow is stable, as the conclusion warns about improving an unstable system (L4260). See [[reduce-wip-before-raising-throughput]]. Which chart answers which question is collected at [[which-chart-for-which-plan-question]].

## Agent executor note

The source's example is a functional split between developers and testers, at enterprise scale. The transfer here is ours: on a board where a few people steer agents, the expected band is work awaiting a person's review. The lever there is the review queue and the cut of the work, and more agent runs would only widen the band.
