---
title: Droppable Stories as a Schedule Buffer
category: periods
summary: When a forecast leaves no margin, name about one period's velocity of low-priority stories, do them last, and drop them if time runs out; otherwise tell people the date may move. It is a feature buffer named late, not the time reserve of a schedule buffer.
tags: [rule, release-planning, buffer, planning-a-date, priority, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Droppable Stories as a Schedule Buffer

A release forecast that lands right on its date can be protected by naming, in advance, the stories that will be given up to hold it. In this wiki's vocabulary that is a [[feature-buffer]] named late: scope protects the date, and no reserve of time is added as on [[schedule-buffer]]. In the fictional case study of [[cohn-agile-estimating-planning]], the coach puts the choice as two branches.

> If we want to keep the schedule at ten iterations, though, we should make sure we’re willing to drop some low priority stories if we start to run out of time. If you’re not willing to do that, we should convey the expectation that it may take longer than ten iterations.
>
> — [[cohn-agile-estimating-planning]], L6372

The bottom of the priority list now carries the weight:

> This is a time when it’s important to know those at the bottom.
>
> — [[cohn-agile-estimating-planning]], L6376

## Inputs and where each is read from

- **The margin of the forecast:** from [[reforecasting-a-release-from-velocity]]. The case had a ratio of 7.8 against 8 periods available.
- **Velocity:** board history. The case's threshold was "at least 17 points of stories" (L6376), and its velocity was 17. This wiki reads the threshold as one period's velocity; the source does not state that derivation.
- **Which stories can go:** the person who owns value. The case's product manager named 8 + 8 + 6 = 22 points (L6378-L6382).
- **Whether a date matters:** the project's setup. This wiki reads a release with nothing tied to its date as having less to protect, and the case's release "isn’t tied to any specific date" (L6271), so what it protects there is the expectation already given to people.

## The rule

The named stories are ordered last.

> So you should work on those last. If you start to run out of time by the tenth iteration, drop one or more of those
>
> — [[cohn-agile-estimating-planning]], L6384

They stay in the plan until dropped. The product manager kept them because "they’re probably worth two additional weeks" (L6390). The same list also prices an earlier release: 133 − 22 = 111 points gives 7 more periods, 18 weeks rather than 20 (L6386-L6388).

## Against the feature buffer

Chapter 17's [[feature-buffer]] is set up when the plan is made, with 25-40% on top of mandatory work (L3849). The case's list is smaller. By this wiki's arithmetic its 22 points are 20% on top of the other 111, and the 17-point threshold would have been 15% on top of 116.

This wiki resolves the difference by when the question arises. While a plan is being built, the feature buffer applies and its range sets the size. Once a running plan has lost its margin, this page applies and one period's velocity is the minimum worth naming, because a reserve smaller than a period cannot absorb a period's shortfall. Neither figure is a measurement.

## What later fact would show the choice wrong

These are this wiki's readings.

- The date arrives with named stories finished and stories ranked above them unfinished: the order was not honoured.
- The date is missed although the buffer was spent: the buffer was too small for the error in the estimates.
- Time runs short and the owner refuses to drop what was named: the buffer existed only on paper.

The case does not settle this. It does not report whether the named stories were built, and its team delivered at 22 weeks for a different reason ([[chosen-delay-versus-slip]]).

## What it costs

The stories are real value held at risk, and the plan's headline scope cannot be promised whole. The rule also needs a person willing to name what they would give up, which is the step that can fail. Where nobody will, the source's second branch applies, and people are told the date may move.

## Agent executor note

This wiki reads nothing here as depending on a human executor. The person steering names the stories, and an agent can follow the order directly, provided the mark is on the board and not in a conversation ([[fact-stranded-outside-the-task]]). Compare [[ordering-by-value-and-urgency]].
