---
title: Actionable Agile Metrics for Predictability (Vacanti)
category: reading-history
summary: Daniel Vacanti's practitioner book arguing that a process becomes predictable by managing flow through Work In Progress, Cycle Time and Throughput rather than by estimating and planning better; it builds from Little's Law through charts, service levels, pull policies and forecasting to one large case, offers no controlled measurement, and its author sells an analytics tool for these metrics.
tags: [summary, flow-metrics, predictability, retrospective-analysis, visualization, concept, case-study, wip, setting]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Actionable Agile Metrics for Predictability (Vacanti)

This is Daniel S. Vacanti's practitioner book on the data side of flow, in the version published on 2016-05-16 (L165, L169). The raw file's `authors` and `published` fields are empty, and the title pages carry both. Its opening claim is that unpredictability is self-inflicted: "You have been taught to collect the wrong metrics, implement the wrong policies, and make the wrong decisions." (L230). The proposed replacement is to manage flow, track three metrics, and let them suggest changes to policy.

## Thesis

The author's strategy is "to focus on the management of flow" (L514). He says this requires two shifts: in thinking, "away from capacity utilization and estimation and planning", and in the quantities used to judge a process, "away from ideal hours, level of effort, points, velocity, etc." (L514-L520). The first shift is on [[good-plan-test]], and the second on [[points-or-time-and-count]]. The book closes the argument in four steps: set policies on the assumptions of Little's Law, collect the metrics, visualize them, and act on them ([[littles-law]]).

## Key takeaways

These are this wiki's statement of what the book amounts to for the charter.

- **Three metrics, between two stated points.** WIP, Cycle Time and Throughput all come from the dates work crossed the process's boundaries, so they need no logged hours and no estimates.
- **The law's assumptions matter more than its arithmetic.** Little's Law looks back and relates averages. Its use is as a list of policies a process should keep, and it does not forecast.
- **Two charts for two questions.** A CFD gives averages and shows balance. A scatterplot gives one item's time with a likelihood.
- **Commitment is per item, at a percentile.** It is owed when an item is pulled, and pull order then decides whether it holds.
- **A date is a range with a probability.** It comes from history, and only from a stable process.
- **Few items are enough to start.** Five bracket the median, though a small sample says little about the tail.

## What it contributes to this wiki

- **Part One, flow and its measures.** A definition of predictability that can be scored afterwards: [[good-plan-test]]. Queues as the observable form of poor flow: [[starting-more-work]]. The three metrics, each defined against the process's two boundaries: [[flow-metrics]], [[work-in-progress]], [[cycle-time]], [[throughput]], [[started-and-finished-points]]. A diagnostic for where elapsed time goes: [[flow-efficiency]]. A test for whether a metric earns its place: [[actionable-metrics]]. A checklist of behaviours, which this wiki turns into board signs: [[signs-of-poor-flow]]. The claim that uniform size is not needed: [[size-spread]].
- **Part One, Little's Law.** The law and, above all, its assumptions: [[littles-law]], [[forecast-range-and-probability]]. Assumptions turned into running policy are on the same page, with two ways that policy gets missed, [[starting-more-work]] and [[work-in-progress]].
- **Part Two, Cumulative Flow Diagrams.** The chart, how it is built and read, and its limits: [[cumulative-flow-diagram]]. Its shapes: [[reading-a-cfd]]. Balance and debt: [[conservation-of-flow]], [[constant-wip]], [[flow-debt]], [[non-standard-departure]].
- **Part Three, scatterplots and service levels.** [[cycle-time-scatterplot]], [[cycle-time-percentile-lines]], [[reading-a-cycle-time-scatterplot]], [[pseudo-control-chart]], [[service-level-expectation]].
- **Part Four, pull, forecasting and starting.** [[fifo-pull-order]], [[class-of-service]], [[value-decided-at-replenishment]], [[forecast-range-and-probability]], [[throughput-monte-carlo]], [[service-level-expectation]], [[started-and-finished-points]], [[capturing-flow-data]], [[how-much-flow-data]].
- **Part Five, the case.** The setting and numbers are in *Siemens HS Case Study* (below), which lists the pages drawing on it. Among them are [[velocity-masks-unfinished-work]], [[starting-more-work]], [[iteration-length-versus-cycle-time]] and [[dropping-estimates-for-flow-forecasts]].

## How far to trust it

The book argues from experience. The Preface and Chapter 1 report no measurement, and their one case is a phone call and a quotation from a director at Siemens Health Services (L376-L380, L398). Under the charter this is a practitioner source, so it is graded on its mechanisms and not on claimed effects.

Little's Law is the exception in kind: a proved relation, and not an opinion of the author's. Little's words reach this wiki through Vacanti, and his papers have not been read here, so what is recorded is Vacanti's report of them. What the author builds on the law, such as "Every time you violate an assumption of Little’s Law your process becomes less predictable." (L1006), is his own claim and carries no measurement.

The two sources of numbers are weak in different ways. The pull-policy simulation in Chapter 13 is a constructed scenario ([[fifo-pull-order]]). The Siemens case in Chapter 17 is real, but it is one organization's before-and-after report, written up with an insider, with other changes running alongside it and several internal inconsistencies (*Siemens HS Case Study* (below)). So no figure in the book shows that the method beats an alternative under controlled conditions.

The author has a stake in the conclusion. The charts in the book were built with ActionableAgile Analytics, "one that my company has developed" (L344), and his claims that "most agile electronic tools build them incorrectly" (L292) and that tooling provides "incorrect or incomplete information" (L484) come from a tool vendor. Chapter 16 repeats this and adds what it calls a "shameless plug" (L3920). This wiki does not carry those claims, and trackers are out of scope in any case. It keeps the checks a reader can run: [[capturing-flow-data]].

The tone is deliberately provocative, and the author says so (L494). A strong sentence here is a position and not a finding, as with "I promise that you will be predictable" (L3964).

The book also contains errors a reader can catch. Its statement about eleven samples does not survive arithmetic ([[how-much-flow-data]]), and it disagrees with itself on spotting bottlenecks ([[reading-a-cfd]]) and on reporting intervals ([[cycle-time-scatterplot]]).

## Scope and claimed reach

The author says the concepts are "relevant regardless of your chosen Agile implementation" (L338) and that they "can be equally applied to any process regardless of domain" (L340). This wiki treats the first as a claim to check per setup, and it does not rely on the second. His setting is human teams in product organizations, and the largest example is an organization of about 50 teams, so transfer to a few people steering an agent is assessed page by page.

The book says little about what comes before a task reaches a board: how to cut it, what it must carry, how to compare value. It orders committed work for predictability alone, which leaves a disagreement with the cost-of-delay source, resolved on [[value-decided-at-replenishment]]. Agents appear nowhere.

It is not independent of [[kanban-guide]], whose copyright names Daniel S. Vacanti, Inc. ([[kanban-guide]] L56), so the two agreeing on flow metrics or an SLE counts as one voice.

## Map of the book

The Preface lays it out (L278-L328):

- **Part One:** predictability, the basic metrics (Chapter 2), Little's Law (Chapter 3).
- **Part Two:** Cumulative Flow Diagrams, how to read them, arrivals and departures, Conservation of Flow, Flow Debt (Chapters 4-9).
- **Part Three:** Cycle Time Scatterplots, Histograms and Cycle Time SLAs (Chapters 10-12).
- **Part Four:** pull policies, forecasting, Monte Carlo, getting started (Chapters 13-16).
- **Part Five:** the Siemens case (Chapter 17).

The author says the book builds in order and that each chapter can also stand alone (L276). He defers the definition of flow itself to Reinertsen and others (L330-L336).

## What this wiki dropped, and why

- **The argument over the words Lead Time and Cycle Time** beyond its one useful point (L682-L690). It changes no output, and [[cycle-time]] keeps the point that either word needs its boundaries stated.
- **The respect-for-people experiment** (L500-L506). It has no sign and concerns managing people.
- **Staffing questions** (L746). Managing people is out of scope.
- **Spreadsheet and tool advice** (L3872-L3876, L3920). It is configuration, apart from the warning kept on [[capturing-flow-data]].
- **The Monte Carlo cost figures and unit costs** at Siemens (L4214, L4234). No dollar figure reaches a board, and this wiki's purpose does not need them.
- **The morale and stand-up reports** (L4238-L4244). They are testimony about managing people.

## Extraction caveat

Running heads and page numbers are interleaved with the text, so a sentence can span several raw lines (for example L574-L580), and quotations across such a break are joined here. Figures are lost and only their captions survive, so a page that needs a figure works from the prose around it. This matters most for Chapter 17, whose charts are its evidence.

## Siemens HS Case Study

The Siemens Health Services (HS) case is the worked example closing Vacanti's *Actionable Agile Metrics*, written from the perspective of Bennet Vallet (*Actionable Agile Metrics for Predictability (Vacanti)* (above) L3978). It records a development organization replacing story points and velocity with Work In Progress (WIP), Cycle Time and Throughput, and it is the setting behind the numbers quoted on other pages. This section holds that setting so that no figure travels without it. It prescribes nothing.

Vacanti says the study was previously published twice, on InfoQ and on the Agile Alliance site, and that he and Vallet have presented it at conferences (L3974). It is a report by people who ran the change, and Vallet partnered with the author on the write-up (L3978). It is not an independent study.

### Setting

- About 50 teams in the development organization; the pilot was the revenue-cycle application, 15 Scrum teams across Malvern, Brooklyn and Kolkata (L3994, L4038).
- Regulated healthcare software with a very high premium for delay (L4002, L4016).
- Before the change: mature Scrum and XP, 30-day sprints, planning poker, relative point estimation, and large releases about once a year (L4006, L4012).
- The change was a "big-bang" rollout with standardized policies across all teams (L4044).

This scale is far above the few people this wiki serves. This wiki keeps the mechanisms, which rest on arithmetic and queueing, and treats the magnitudes as one organization's result. The charter grades a practitioner source this way.

### Definitions used

WIP was "any work item (e.g., user story, defect, etc.) that was between the “Specifying Active” step and the “Done” step in our workflow" (L4058). Cycle Time was "the amount of total elapsed time needed for a work item to get from “Specifying Active” to “Done”", and Throughput was "the number of work items that entered the “Done” step per unit of time" (L4064). All three measure between the same two points; see [[started-and-finished-points]] and [[flow-metrics]].

"Done" here is not delivery. Regression testing, beta testing, hosting and customer implementation sat outside the measured stream (L4014, L4264), so these Cycle Times do not say when a customer received anything.

### Timeline and numbers

| Release | 50th percentile | 85th percentile | First pass yield | Conditions |
|---|---|---|---|---|
| Before Kanban | 21 days | 71 days | 75% | Points and velocity; Cycle Times trending upward over the release (L4078, L4200) |
| First Kanban, April to December 2012 | not given | 43 days | 86% | WIP limits added only partway through; on schedule and over 10% under budget (L4044, L4132, L4200) |
| Second Kanban, March to September 2013 | not given | 40 or 41 days (see below) | 95% | After limits were in place; 33% more stories than the previous release (L4046, L4144, L4200, L4286) |

The first row covers "finished stories in the Financials organization" (L4068), not the whole pilot, and the chapter does not say whether the later rows have the same scope.

First pass yield means "the percentage of formal integration and regression tests passing the first time they are executed" (L4200). The headline "42% reduction in Cycle Time" (L3988) is not tied to a stated pair of figures; this wiki's arithmetic finds that it matches 71 to 41 days, not 71 to 43.

### Internal inconsistencies

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

### Pages drawing on this case

[[velocity-masks-unfinished-work]], [[starting-more-work]], [[conservation-of-flow]], [[column-doneness-criteria]], [[flow-efficiency]], [[reading-a-cfd]], [[cycle-time-scatterplot]], [[iteration-length-versus-cycle-time]], [[throughput-monte-carlo]], [[dropping-estimates-for-flow-forecasts]].
