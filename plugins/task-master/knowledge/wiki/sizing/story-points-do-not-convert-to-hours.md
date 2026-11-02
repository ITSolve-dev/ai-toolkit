---
title: Story Points Do Not Convert to Hours
category: sizing
summary: A points-to-hours factor holds only as an average over many items; per item the hours form a distribution, so some one-point stories take longer than some two-point stories. A fixed conversion is the defect.
tags: [rule, estimation, relative-estimation, failure, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Story Points Do Not Convert to Hours

A story point has an average cost in hours and no fixed cost. Relative estimation converts to time only in aggregate, over enough items for differences to cancel. Used per item, the conversion gives a precise number that is wrong.

## The rule

Do not derive one item's duration from its points. Use points for sums over many items, and leave the single item as a range.

## The mechanism

> I see teams go astray when they start to believe there is a strong relationship between a story point and an exact number of hours.
>
> — [[cohn-agile-estimating-planning]], L3360

Cohn's example is a team that divided its productive hours per iteration by its velocity, found about twelve hours per point, and came to believe each point always equalled twelve hours (L3360). This wiki notes that the average was fine, and the certainty was the error. Cohn says hours for one point form a distribution around twelve, and "Until the team identifies and estimates a story’s underlying tasks, it is hard to know where a particular story lies on a curve such as this." (L3362).

Distributions for neighbouring steps overlap, so "it is possible that some one-point stories will take longer than some two-point stories" (L3368). Cohn calls that reasonable and expected, on two conditions: enough stories in the release for outliers to average out, and everyone remembering that equal estimates do not mean equal durations (L3368).

## Numbers and their conditions

Twelve hours per point is one team's ratio and not a constant. Figures 14.5 and 14.6 are illustrative: Cohn calls the three-curve case "hypothetical" (L3368). How many items are enough is discussed on [[filling-a-period]], where Cohn puts it at twenty to thirty per iteration for that use (L3348).

## Sign of violation

These signs are this wiki's. Each raises a question and is not a verdict.

- **In project configuration or documents:** a stated hours-per-point or days-per-point factor.
- **In a task or a promise:** a date or duration for one task computed from its points.
- **In a review of a period:** a task called "mis-estimated" solely because it took longer than a lower-pointed one, with no sign that its scope was misunderstood.

A single task outliving its neighbours at a lower step is expected spread. The exception is a distribution per step read from history, which is not a conversion: [[overrun-triggers-a-recut]] compares a task's age with the 85th percentile of finished tasks on its step, so it fires on the tail of the spread and not on the spread itself. Repeated overruns in one direction are what call an estimate into question; the single case is handled on the same page.

## Trade-off

Giving up the conversion means giving up a per-item date from an estimate. The plan can offer a range or an aggregate forecast, and someone asking about one item will find that less satisfying.

## Agent executor note

The argument is about spread and sample size, so this wiki expects it to hold for an agent executing. Agent spread may be wider or narrower than a team's, and no source here measures that. Hours per point are a human unit in any case, and the same reasoning applies to any fixed factor between points and agent run time.

## Related

The scale itself and its ceiling are on [[estimation-scale]] and [[size-ceiling]]. The unit is defined on [[story-points]]. An aggregate conversion to money, used over a stretch of work and not per item, is on [[cost-per-story-point]].
