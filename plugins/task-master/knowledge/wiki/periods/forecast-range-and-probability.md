---
title: A Forecast Carries a Range and a Probability
category: periods
summary: Vacanti calls a date a forecast only if it states both a range and the probability of landing in it, computed from recorded data; the sign is a date with neither, and this wiki resolves it against Cohn's range-or-confidence by what the project has recorded.
tags: [rule, estimation, forecasting, predictability, date-commitment]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# A Forecast Carries a Range and a Probability

A **forecast**, in Vacanti's usage, is a calculated statement about when an item or items will finish, and it is incomplete unless it states both a date range and the probability of landing in that range. A single date, or a range with no probability, is an unqualified claim about an uncertain future.

> A forecast is a calculation about the future completion of an item or items that includes both a date range and a probability.
>
> — [[vacanti-actionable-agile-metrics]], L3534

> You should never—and I mean never—communicate a forecast that does not include at least two things: a date range and a probability for that date range occurring.
>
> — [[vacanti-actionable-agile-metrics]], L3530

## Reasoning

Vacanti's argument is that uncertainty about the future requires a probabilistic statement: "A forecast without an associated probability is deterministic, and, as you know, the future is anything but deterministic." (L3544). What breaks when the rule is ignored, as this wiki reads it, is the ability to check the statement afterwards: a bare date is simply hit or missed, and a miss cannot be told apart from an ordinary outcome that the distribution already allowed.

## Sign

A date in a plan, a milestone, a status answer or a reply to "when will this be done?" that states no probability, or a range that states none. As everywhere in this base, the sign raises a question and not a verdict; the question to check is what the date is. [[single-date-plan]] is the wider failure.

## What separates neighbouring cases

- **Forecast versus estimate.** Vacanti allows that "an estimate can be thought of as a forecast" (L3526) but sets the forecasts of the chapter apart as "much more scientific than just some poor guy’s best guess" (L3526). This wiki reads the discriminator as the origin of the two numbers: a forecast's range and probability are computed from recorded data, for instance from [[single-item-forecast]]. An invented "90% sure" meets the form of the rule and misses its point.
- **Forecast versus deadline.** This distinction is ours, not the source's: a deadline is a date somebody demands, a forecast is a date somebody calculates. A deadline carrying no probability is not a violation; the violation is presenting one as the other. See [[estimate-versus-commitment]].
- **A date versus a count.** [[flow-metrics-scrum-teams]] applies the same pattern to how many items fit: "We have a 50% chance of getting 18 or more PBIs to done in this Sprint" (L958). This wiki notes that the range is open at one end. The book says a bare count misleads in a specific way: told "18", a reader assumes "the team has a 100% chance of getting exactly 18 items done" (L966), when the book puts that chance at about 6%. This wiki reads a bare count someone will rely on as the same sign as a bare date. The method is on [[throughput-monte-carlo]].
- **Time versus other forecasts.** Vacanti limits the chapter to completion times but says the principles "are applicable to any type of forecast" (L3528). This wiki reads that as covering a relative estimate once it is converted into a date: the points carry no date claim, and the conversion does.

## Which holds under which setup

Vacanti requires range and probability together. Cohn asks for a confidence, a range, or both, and this wiki already prefers the range where nothing produced a percentage ([[stating-plan-uncertainty]]). The resolution below is this wiki's, and it turns on what the project has recorded.

- **Per-item cycle times exist:** both parts are required, and they are read from the same percentile ([[single-item-forecast]], [[monte-carlo-simulation]]).
- **Finish dates exist and start dates do not:** a count or a date can still carry both parts, from daily Throughput ([[throughput-monte-carlo]]), because that needs only when items finished.
- **Only a velocity history exists, under iterations:** give the range from [[velocity-range-forecast]] with its basis, and say that no probability was computed. That meets Cohn's form and half of Vacanti's rule, and the statement should not claim more.
- **No history exists:** no conforming forecast is possible. This wiki's position is that saying so is the honest output, with any figure labelled a guess. The chapter does not address that case.

## Trade-off

The rule costs the appearance of commitment: the reader gets "43 days or less 85% of the time" (L3580) in place of a date, and the remaining share is stated openly. It also needs recorded history.

## Agent executor note

This wiki's reading is that the rule survives: it concerns the statement and not who does the work, and nothing in its mechanism relies on human pace or memory.

## See also

[[single-item-forecast]], [[forecast-from-an-average]], [[straight-line-projection]], [[monte-carlo-simulation]], [[estimates-as-ranges]]
