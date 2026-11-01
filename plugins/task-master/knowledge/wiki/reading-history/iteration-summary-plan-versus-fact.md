---
title: Iteration Summary of Plan Versus Fact
category: reading-history
summary: A per-story table of result, points planned and points earned shows plan against fact for an iteration; unfinished work earns zero and an overrun is recorded as text, so the total is the iteration's velocity.
tags: [method, retrospective, velocity, plan-versus-fact, reporting]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Iteration Summary of Plan Versus Fact

An end-of-iteration summary is a short record of what an iteration held and delivered. Cohn offers it as optional, useful "both in disseminating current information and as an historical document for use in the future" ([[cohn-agile-estimating-planning]] L4797). Its most useful part for this base is the table comparing plan with fact.

## The table

Cohn's sample (L4765-L4771), with the story names shortened:

| Story | Result | Points planned | Points earned |
|---|---|---|---|
| Enter swimmers | Finished | 8 | 8 |
| Define practice sessions | Finished; bigger than planned | 8 | 8 |
| See my times | Finished | 3 | 3 |
| Update demographics | Started; not finished | 1 | 0 |
| **Total** | | **20** | **19** |

This wiki reads three conventions from the sample. Cohn shows them without stating them.

- **Started but unfinished earns zero.** No partial credit appears; see [[unfinished-at-period-end]] and [[all-or-nothing-counting]].
- **An overrun does not change the points.** The "bigger than planned" story keeps its 8. The overrun is recorded in the Result column, which keeps the estimate as a plan figure.
- **The earned total is the iteration's velocity.** The 19 here matches the most recent value of the chart at L4757, so the summary is also the input to [[velocity-range-forecast]].

## Procedure

1. List the stories planned for the iteration with their points.
2. Record the result of each in words, including surprises.
3. Award full points only to finished stories.
4. Total both columns, and explain the difference from the rows that account for it.

A row like "Finished; bigger than planned" is the input for [[overrun-triggers-a-recut]].

## Pass-or-fail reporting

Cohn's build report gives a success count only if everything passed; otherwise it gives only the failures:

> Reporting that 99 out of 100 tests passed leads to the temptation to think that since 99% of the tests passed we must be doing well.
>
> — [[cohn-agile-estimating-planning]], L4739

This wiki transfers that reasoning to task status: a report of nine out of ten acceptance criteria met invites the same comfort, and a task in that state is not finished. The transfer here is ours. Cohn writes only about tests.

## Cost

Cohn: "I find that I can complete this summary document in less than 30 minutes per iteration", which at two-week iterations is at most 15 minutes a week (L4688). That figure is his own, for a hand-assembled report. A plugin reading board history pays a different cost, and this source does not measure it. He leaves the choice open: "You’ll have to decide for yourself whether you want to take the time to do this." (L4688)

## Limits

This wiki notes that the sample table has no way to show a story added or removed mid-iteration, so its planned total does not reveal [[mid-period-change]]. The comparison also means nothing if the plan was never believed ([[plan-deliberately-overstated]]). Cohn's report also covers personnel and an iteration review. Both are left out here: the first is individual load and the second is a meeting record, and the charter excludes both.

See also [[which-chart-for-which-plan-question]], [[commitment-over-a-period]].
