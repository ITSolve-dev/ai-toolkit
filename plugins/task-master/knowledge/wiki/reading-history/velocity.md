---
title: Velocity
category: reading-history
summary: The sum of the points of the items completed in an iteration; a rate of completion used both as a retrospective measure and as the forecast for the next iteration, which says nothing about scope change and is not the net progress the source sometimes calls by the same word.
tags: [concept, velocity, iterations, forecasting, retrospective-analysis]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Velocity

Velocity is the rate at which a team completes estimated work, expressed in points per iteration. It is the link that turns unitless [[story-points]] into calendar time, and Cohn introduces it for exactly that reason ([[cohn-agile-estimating-planning]] L1008).

## Definition

> Velocity is a measure of a team’s rate of progress. It is calculated by summing the number of story points assigned to each user story that the team completed during the iteration.
>
> — [[cohn-agile-estimating-planning]], L1008

Cohn's examples: three five-point stories give 15, and two five-point stories give 10 (L1008). Only completed stories enter the sum (L1008, L1054). Chapter 19 restates it shortly:

> Velocity is expressed as the number of story points (or ideal days) completed per iteration.
>
> — [[cohn-agile-estimating-planning]], L4288

Its example is a team that finished twelve stories worth 30 points in its last iteration, a velocity of "30 points per iteration" (L4288). The source calls velocity "the primary measure of a team’s progress" (L4290), which is why the counting rule matters. Chapter 7 settles the partly done story: Cohn is "generally in favor of an all-or-nothing stance toward counting velocity" (L1496), and the rule and its reasons are on [[all-or-nothing-counting]]. His exception is on [[partial-credit-for-unfinished-tasks]], and the Scrum Guide's position is on [[unfinished-at-period-end]].

This wiki notes that velocity can be read from board history without anyone logging anything: the points of the items that reached a finished state inside the period.

## Use as a forecast

> If a team completed ten story points of work last iteration, our best guess is that they will complete ten story points this iteration.
>
> — [[cohn-agile-estimating-planning]], L1010

Cohn adds that this holds regardless of mix, "whether they work on two five-point stories or five two-point stories" (L1010). This wiki reads that as a consequence of the additive claim in [[story-points]], so it inherits that claim's weakness: it is true only so far as the ratios hold.

Cohn calls this a best guess, and the chapter gives no error bounds. He also notes that a past velocity is not always available and that it must sometimes be estimated, which he defers to Chapter 16 (L1023-L1029); which way to estimate it is decided on [[choosing-velocity-estimate-approach]], the labelled first guess is on [[planned-velocity]], and the result is stated as a [[velocity-estimate-range]]. This wiki reads velocity as what fills the "past performance" input on [[filling-a-period]]. The conversion to a date is on [[deriving-duration-from-velocity]], and what the rate corrects on its own is on [[velocity-self-correction]].

## What it measures and does not

The definition makes velocity a measure of completed estimated size per period. This wiki reads its limits from that definition; Cohn does not list them here.

- It is denominated in a team's own arbitrary scale. Since the raw value is unimportant (L953), one team's velocity gives no basis for comparison with another's.
- It does not measure value or correctness, only points finished.
- It moves with the estimates as well as the work. If estimates inflate, velocity rises with no extra work done. The sign to check is points per iteration rising while the count and observed size of finished items stay flat.
- It says nothing about individual items: a forecast for a period is not a promise for a task.
- It is not distance to the goal. Velocity reduces the work left only "Assuming that the scope of the project hasn’t changed" (L4288). If forty points are added and thirty completed, the team is further from the end than it was (L4273). [[release-progress-forces]] separates the causes.
- It excludes partly done work, so a period's figure can sit below the effort that went into it.

## Velocity versus net progress

The strict definition counts points completed. Later, the same chapter says "velocity has slowed to only 20" and then offers as one explanation that the team "may have completed their planned 30 points of work but may have increased estimates on some remaining stories such that net progress is 20 rather than 30" (L4373). Under the definition at L4288 that team's velocity is 30, and 20 is its net progress.

This wiki keeps the two apart. **Velocity** is the sum of estimates of tasks completed in the period, read from tasks that crossed the finished point. **Net progress** is the change in work remaining, read from [[release-burndown-chart]]. A plugin that reads velocity off a burndown slope is reading net progress, and the two diverge whenever estimates or scope moved.

## Numbers and their conditions

The figures in this chapter (10, 11, 15, 20, 25 points per iteration) and the 30 of Chapter 19 are constructed examples, not measurements, and say nothing about what a typical velocity is.

## Which setup this applies under

The resolution here is this wiki's. Velocity needs two things a project may not have: a fixed period and an estimate on every task.

- **Iterations with estimates:** velocity as defined here.
- **No iterations, estimates kept:** the same sum over a stated span of calendar time.
- **No estimates:** Throughput on [[flow-metrics]], which counts items and asks no estimate. It says less about size, because the count depends on the cut.

The Scrum Guide does not use the word, as [[flow-metrics]] records, so velocity is Cohn's reading of an iteration setup and not a requirement of one.

## Agent executor note

The transfer here is this wiki's, not Cohn's. Velocity's arithmetic survives any executor: it sums what finished. Its use as a forecast rests on a mechanism the chapter assumes without stating, namely that the rate is stable because the same team does similar work at a similar pace. When an agent executes and a person steers, the limit on the rate may sit elsewhere, for example in how fast results can be reviewed, and the stability of that rate is not shown by this source. The term "team" is the source's; the charter's setting is a few people steering an agent, so a velocity read here should be treated as a rate for that arrangement, and checked against history, not assumed to behave as Cohn's team does. On this reading a change in velocity may reflect the steering and not the execution. Points are also relative to whoever calibrated the scale, so a period run by hand and one run by an agent are compared only after checking the estimation pages ([[estimation-baseline]]).
