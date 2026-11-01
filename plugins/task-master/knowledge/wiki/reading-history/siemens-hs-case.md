---
title: Siemens HS Case Study
category: reading-history
summary: The setting, timeline and numbers of Siemens Health Services' move from points and velocity to WIP, Cycle Time and Throughput, with the chapter's internal inconsistencies recorded.
tags: [concept, case-study, flow-metrics, wip, setting]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Siemens HS Case Study

The Siemens Health Services (HS) case is the worked example closing Vacanti's *Actionable Agile Metrics*, written from the perspective of Bennet Vallet ([[vacanti-actionable-agile-metrics]] L3978). It records a development organization replacing story points and velocity with Work In Progress (WIP), Cycle Time and Throughput, and it is the setting behind the numbers quoted on other pages. This page holds that setting so that no figure travels without it. It prescribes nothing.

Vacanti says the study was previously published twice, on InfoQ and on the Agile Alliance site, and that he and Vallet have presented it at conferences (L3974). It is a report by people who ran the change, and Vallet partnered with the author on the write-up (L3978). It is not an independent study.

## Setting

- About 50 teams in the development organization; the pilot was the revenue-cycle application, 15 Scrum teams across Malvern, Brooklyn and Kolkata (L3994, L4038).
- Regulated healthcare software with a very high premium for delay (L4002, L4016).
- Before the change: mature Scrum and XP, 30-day sprints, planning poker, relative point estimation, and large releases about once a year (L4006, L4012).
- The change was a "big-bang" rollout with standardized policies across all teams (L4044).

This scale is far above the few people this wiki serves. This wiki keeps the mechanisms, which rest on arithmetic and queueing, and treats the magnitudes as one organization's result. The charter grades a practitioner source this way.

## Definitions used

WIP was "any work item (e.g., user story, defect, etc.) that was between the “Specifying Active” step and the “Done” step in our workflow" (L4058). Cycle Time was "the amount of total elapsed time needed for a work item to get from “Specifying Active” to “Done”", and Throughput was "the number of work items that entered the “Done” step per unit of time" (L4064). All three measure between the same two points; see [[started-and-finished-points]] and [[flow-metrics]].

"Done" here is not delivery. Regression testing, beta testing, hosting and customer implementation sat outside the measured stream (L4014, L4264), so these Cycle Times do not say when a customer received anything.

## Timeline and numbers

| Release | 50th percentile | 85th percentile | First pass yield | Conditions |
|---|---|---|---|---|
| Before Kanban | 21 days | 71 days | 75% | Points and velocity; Cycle Times trending upward over the release (L4078, L4200) |
| First Kanban, April to December 2012 | not given | 43 days | 86% | WIP limits added only partway through; on schedule and over 10% under budget (L4044, L4132, L4200) |
| Second Kanban, March to September 2013 | not given | 40 or 41 days (see below) | 95% | After limits were in place; 33% more stories than the previous release (L4046, L4144, L4200, L4286) |

The first row covers "finished stories in the Financials organization" (L4068), not the whole pilot, and the chapter does not say whether the later rows have the same scope.

First pass yield means "the percentage of formal integration and regression tests passing the first time they are executed" (L4200). The headline "42% reduction in Cycle Time" (L3988) is not tied to a stated pair of figures; this wiki's arithmetic finds that it matches 71 to 41 days, not 71 to 43.

## Internal inconsistencies

A reader citing this chapter should know these. They concern magnitudes and dates, not the mechanisms kept here.

- **When limits began.** The text says the team delayed "until the third month of the release" (L4100), and the release began in April (L4044), yet it also dates the limits to "early September 2012" (L4132).
- **Decrease or stabilization.** Limits are said to have stopped growth, "such that Cycle Times no longer continued to grow" (L4126), and elsewhere to have produced "an immediate decrease in Cycle Time" (L4178).
- **Second release figure.** 41 days (L4144) and 40 days (L4154, L4286).
- **A percentile stated as a bound.** "Cycle Times of 43 days or less" (L4154) omits that this covers 85% of stories.
- **A rounded ratio.** 71 days is called "2.5 sprints" (L4078), and 71 divided by 30 is about 2.4.
- **Figure references.** Figure 17.4 is called "the release before Kanban" (L4132) but is captioned as early in the first Kanban release (L4112).
- **Histogram counts.** 30% is 410 stories and the next 20% is 225 stories (L4202); these imply different totals.
- **Attribution of the whole gain to limits.** The first release's 85th percentile covers months without limits, and quality gains came alongside "significant focus" on CI and quality management (L4262).

The figures themselves are absent from the raw source, so any reading of a chart here rests on the chapter's prose.

## Pages drawing on this case

[[velocity-masks-unfinished-work]], [[starting-new-work-when-blocked]], [[reduce-wip-before-raising-throughput]], [[conservation-of-flow]], [[push-delays-defect-discovery]], [[column-doneness-criteria]], [[flow-efficiency]], [[bottleneck-on-the-cfd]], [[cycle-time-scatterplot]], [[iteration-length-versus-cycle-time]], [[monte-carlo-simulation]], [[dropping-estimates-for-flow-forecasts]].
