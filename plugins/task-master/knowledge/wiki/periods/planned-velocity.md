---
title: Planned Velocity
category: periods
summary: Before any iteration has finished, the points committed to the first iteration stand in for velocity as a labelled guess until observed values replace it; it ranks behind waiting for one or three iterations, and its result goes out as a range.
tags: [method, velocity, forecast, release, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Planned Velocity

Planned velocity is a stand-in for [[velocity]] before any has been observed: the sum of the points on the stories committed to the first iteration. It exists because someone needs a schedule before any data does. The method comes from the fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961), so its speakers are characters and its figures are illustrations.

Velocity itself is defined there by finished work:

> After each iteration we can add up the story points for the stories that are finished. We call that velocity. Velocity will change from iteration to iteration, but its average is relatively stable over time.
>
> — [[cohn-agile-estimating-planning]], L6153

## The choice, in order of preference

1. **Wait three iterations.** "After three iterations we should have a good measure of how fast the team is progressing. We can divide the total amount of work remaining by the velocity and that will tell us how long to expect" (L6157).
2. **Wait for one.** "wait _at least_ two weeks, let the team run one iteration, and then base this initial plan off at least one observation of actual velocity" (L6187).
3. **Plan now, and label it.** "You’ve planned to do four stories in this first iteration. We can add up the points associated with each and call that our planned velocity. We have no idea if it will be, but it’s our initial guess." (L6167).

This wiki reads the first two as [[run-iterations-to-observe-velocity]], and the third as the forecast on [[forecast-velocity-by-what-fits]] run on the project's real first selection and not on a sample. The order agrees with the ranking on [[choosing-velocity-estimate-approach]].

## Procedure

1. Commit to a first iteration, by [[filling-a-period]].
2. Sum the points of the committed stories. In the case: 8 + 5 + 2 + 3 = 18 (L6169).
3. Divide the points wanted in the release by that sum. In the case 132 points divided by 18 gives just over 7 iterations (L6173). The 132 comes from the walk on [[ordering-by-kano-category]].
4. Publish the result as a range and name its velocity as planned, on [[stating-plan-uncertainty]].
5. Replace it with an observed figure as soon as one exists. The message for those waiting on the schedule is "we can provide better information every two weeks" (L6191).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Points committed to the first period | Story estimates on the board |
| Total points wanted | The release list |

The first observed velocity is what tests the guess. In the case it came in at 16 against a planned 18 (L6263), and the forecast was recomputed from the observed figure (L6267).

## Failure mode: a guess treated as a measurement

**Signs:** a published schedule with no finished iteration behind it and no note that its velocity is planned, or a planned velocity still being quoted after observed values exist. These signs are this wiki's. The second is the same defect as the one on [[choosing-velocity-estimate-approach]].

## Points do not convert evenly to hours

This wiki's calculation from the case's own tables gives three different ratios. The rings story is 8 points for 84 hours, about 10.5 hours a point. The bridges story is 5 points for 82 hours, about 16.4. Human versus human together with the winning-shape story is 5 points for 30 hours, about 6. So bridges was rated smaller than rings and came out about the same size in hours (L5752-L5763, L5838-L5845, L5865-L5880).

This wiki reads that spread as the reason planning hours check a commitment on [[filling-a-period]] and do not calibrate points. The general claim is on [[story-points-do-not-convert-to-hours]].

The count also has an edge. The team committed to three stories (L5933), yet the sum names four, because the winning-shape story had been absorbed into another. That is on [[independent-tasks]].

## Which setup this applies under

The resolution is this wiki's. It needs iterations and an estimate on every task. Under a flow setup there is no first selection to sum, and a forecast comes from history once there is any ([[flow-metrics]], [[service-level-expectation]]).

## Agent executor note

The method transfers, since it needs only points and finished stories. The claim that the average is stable concerns a human team and is untested for an agent, and "three iterations" is a remark in a case study and not a measured threshold. Those readings are this wiki's. A first selection of an agent-run project may also hold the tasks easiest to specify, as [[run-iterations-to-observe-velocity]] warns.
