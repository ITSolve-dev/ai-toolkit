---
title: Cycle Time Adds One Time Unit
category: reading-history
summary: Vacanti counts Cycle Time inclusively, adding one reporting unit to the date subtraction, so same-day work is one unit rather than zero. Consistency matters more than the convention, and the rule applies to Cycle Time, not to the Throughput run.
tags: [rule, retrospective-analysis, cycle-time, measurement]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Cycle Time Adds One Time Unit

**Adding one time unit** is Vacanti's convention for [[cycle-time]]: finish date minus start date, plus one reporting unit, so both end dates count. All Cycle Time calculations in the book follow it ([[vacanti-actionable-agile-metrics]] L1616).

## The rule and its reasoning

The stated premise is that "the shortest amount of time that an item can take to complete is one unit" (L1610). Two cases carry the argument (L1610):

- An item that starts and completes on September 1 would otherwise have a Cycle Time of zero days. Vacanti calls that misleading, because it suggests no time was spent.
- An item that starts on September 1 and finishes on September 2 would otherwise have one day, although time was spent on both dates. Adding the unit gives two.

The convention is declared as advice, not as a law:

> You might disagree with this advice for your own particular situation. And that is ok (as long as you are consistent in your calculations).
>
> — [[vacanti-actionable-agile-metrics]], L1610-L1616

This wiki reads that as making consistency the binding part: either convention is defensible, and mixing them is not.

## Applying it

- **Inputs:** the start and finish dates of an item, read from board history, or the two dates of a horizontal reading on a CFD; and the reporting unit.
- **The horizontal reading takes the unit too.** It is step 5 of the procedure, turning 23 days into 24 (L1606-L1608). See [[reading-flow-metrics-off-a-cfd]].
- **It is a Cycle Time rule.** The book's Throughput example takes "November 16 minus June 21 equals 148 days" with no added unit (L1682). This wiki notes that an inclusive count would give 149 days and 3.47 items per day instead of 3.49, so the two conventions should not be blended by habit. See [[throughput]].

## Signs of a violation

These signs are this wiki's derivation. They raise a question about the calculation, not about the work.

- A Cycle Time of zero in a dataset: the unit was not added, or the unit is too coarse to be meaningful.
- Two Cycle Time series that differ by a constant one unit: they use different conventions.
- An exact average from item dates compared with a CFD reading when only one includes the unit: part of the gap is arithmetic, which would pollute the comparison on [[approximate-average-cycle-time]].

## What would show the choice wrong

This section is this wiki's reading. If most finished items land exactly on the minimum of one unit, the metric has stopped discriminating and the reporting unit is too coarse.

## Does it survive an agent executing

The argument assumes work that spans a meaningful fraction of the reporting unit: time "was spent" on each date counted. This wiki's reading is that an agent can start and finish a task within an hour, and that the day-based version of the rule then reports a full day for it. On that reading the arithmetic of the rule survives and the day unit may not. The fix follows from the source's own remark that the steps hold for whatever time unit is chosen (L1592-L1598): report in a finer unit and add one of that unit. The transfer is ours.
