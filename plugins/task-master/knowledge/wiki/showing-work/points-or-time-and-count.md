---
title: Points or Time and Count
category: showing-work
summary: Which unit a project states progress and forecasts in; Vacanti rejects points and velocity as foreign to customers and silent on what to do, and this wiki resolves it by reader and setup, so outside readers get elapsed time or item count and points may stay inside where the project estimates.
tags: [decision-rule, story-points, velocity, forecasting, retrospective-analysis, visualization]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Points or Time and Count

This decides the unit in which a project states its progress and forecasts. Cohn builds forecasting on [[story-points]] and [[velocity]]. Vacanti rejects both: "it is incomprehensible to me that metrics like Story Points and Velocity are accepted as Agile. I am being purposefully provocative here" ([[vacanti-actionable-agile-metrics]] L494). The author's admission means this is a stated position, and he reports no measurement for it. He extends it to "the corresponding analytics like Burn Down charts" (L494).

## Vacanti's arguments

1. **The customer's language.** "to me, collaboration means speaking the language of the customer" (L496), and that extends to metrics. "I guarantee all of your stakeholders understand the concept of elapsed time." He adds that they understand the total number of features in a release (L498).
2. **No intervention.** "traditional Agile metrics and analytics give no visibility nor any suggestion of what to do when things go wrong" (L482). This is the test on [[actionable-metrics]].
3. **Evaluating the process.** Focusing on flow means moving the quantities "used to evaluate process performance" away from "ideal hours, level of effort, points, velocity, etc." (L514-L520).

## What the arguments reach

This wiki reads all three as being about reporting and evaluation. None says that relative size is a bad gauge for deciding when to cut a task ([[size-ceiling]]), and Chapter 1 offers no case against estimating for that purpose. Argument 1 has force only where the reader is outside the project. Argument 2 is partly answered in this base, because [[release-progress-forces]] and [[diagnosing-unfinished-work]] give velocity some causes to check, though they work from period summaries and not from what is stuck now.

## The rule

The resolution is this wiki's, and neither author states it.

| Setup | Reader | State it in |
|---|---|---|
| Any | Someone outside the project | Elapsed time or item count, whatever produced the figure. A velocity forecast is converted before it leaves ([[velocity-range-forecast]]) |
| Estimates kept, with or without iterations | The people steering | Points and their rate may stay, per period or over a stated span as on [[velocity]]. For why something is slow, read count, age and cycle time as well |
| No estimates | Anyone | Time and count only, since points have no input and [[throughput]] needs none |

A burndown in points falls under the same table: usable by the people steering, and converted before it goes outside.

Whether to drop estimates for dates altogether is a separate test, on [[dropping-estimates-for-flow-forecasts]].

## Sign of violation

A status or forecast addressed to someone outside the project is denominated in points, in its text. A velocity drop reported as a finding with no reading of what is stuck is the second sign. A sign raises a question ([[smell-is-not-a-finding]]).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who will read the figure | The request |
| Whether the project estimates | Project configuration |
| Whether the project has fixed periods | Project configuration |

The choice was wrong if outside readers keep asking what a stated figure means, or if a project's forecasts by time and count come out less accurate than its forecasts by points over several releases. The second would undercut Vacanti's position and not only this rule.

## Cost

Converting points before reporting hides what the figure rests on, so it must carry its range ([[forecast-range-and-probability]]). A project that keeps points inside and time outside maintains two vocabularies.

## Agent executor note

Argument 1 does not depend on the executor. In a project of a few people steering an agent, the customer may be those same people, and then this wiki reads the argument as having little force. Argument 2 survives, since a rate says nothing about what to do. The source's setting is stakeholders such as a CFO (L496), which is a larger organization than the charter's.
