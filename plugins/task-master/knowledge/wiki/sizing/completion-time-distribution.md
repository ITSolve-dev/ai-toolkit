---
title: Completion-Time Distribution
category: sizing
summary: How long a unit of work takes is a right-skewed range, so a single estimate means nothing until it is known which point on the curve it names; the 50% and 90% points are the two that planning uses.
tags: [concept, estimation, uncertainty, what-an-estimate-promises]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Completion-Time Distribution

The time one unit of work will take is a range with a long right tail, not a number. A single estimate names one point on that curve, and it can only be read once it is known which point. Cohn uses this as the basis for [[choosing-a-buffer]]: "we pretend that a single number reflects our expectations" ([[cohn-agile-estimating-planning]] L3877).

## Why the curve leans right

The asymmetry has a mechanism, not just a shape: "there is normally not much that can be done to accelerate the completion of a task but there are an indefinite number of things that can go wrong and delay the completion of a task" (L3879).

Two consequences follow in the source. The single most likely finish time sits at the peak, yet "finishing by that time is less than 50% likely" (L3890). And the question planning needs is not the chance of finishing on a given day but the chance of finishing on or before it, which is the cumulative curve (L3901).

## A worked shape, and its setting

Cohn's Table 17.1 imagines 100 equally skilled programmers building one feature independently (L3905-L3916). It is a thought experiment: he says the results "might be similar" to these. It is not a measurement, and the figures do not transfer as figures.

| Day | Finishing that day | Total finished |
|---|---|---|
| 1 | 5 | 5 |
| 2 | 40 | 45 |
| 3 | 25 | 70 |
| 4 | 15 | 85 |
| 5 | 10 | 95 |
| 6 | 5 | 100 |

This wiki reads the table as follows: the most common finish, Day 2, covers only 45 of the 100, and 90% confidence is not reached until Day 5, two and a half times the most common finish.

## What each point promises

- **A 50% estimate** is one "just as likely to be high as they are to be low" (L4000). It is overrun half the time by construction, so one task passing its 50% figure says nothing about the estimate. How far past an estimate justifies action is [[overrun-triggers-a-recut]].
- **A 90% estimate** is the 50% figure plus [[choosing-a-buffer]]. Cohn's programmer is "equally likely to beat or exceed" 3 days, yet would not be surprised by 5 (L3903).

Discriminating question for any estimate on a board: which of these two is it? An estimate is usable in a plan only if the answer is known, because [[choosing-a-buffer]] depends on it. Neither point is a promise ([[estimate-versus-commitment]]); expressing the spread is the subject of [[forecast-range-and-probability]].

## Checking it against fact

This wiki adds a check the chapter does not state. Where estimates are in time, or convert to it, the finished items in board history should show about half at or under their 50% figure and about nine in ten at or under their 90% figure. Nearly everything finishing under the 50% figure suggests the estimates are really pessimistic ones, and a buffer on top would count the same safety twice.

## Agent executor note

The transfer here is ours; no source in this chapter tests it. The asymmetry does not rest on human pace, so this wiki expects it to survive an agent executing: a failed check, an unrecoverable gap in a task, or a wait on the person steering can each delay work, and little can compress it. The shape of Table 17.1 does not carry over, and nothing here says how wide an agent's tail is.
