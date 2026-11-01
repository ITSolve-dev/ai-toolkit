---
title: Updating the Release Plan
category: periods
summary: A release plan is revisited on a regular cadence; after each iteration by default, and up to four to six weeks only while velocity holds and iteration planning brings no surprises.
tags: [rule, iterations, release, plan-versus-fact]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Updating the Release Plan

A [[release-plan]] is a live document. "The release plan should be revisited and updated with some regular frequency." ([[cohn-agile-estimating-planning]] L2857). Cohn warns against filing it away, and in his summary a plan is not left hanging on a wall to rot (L2973). What the update folds in is on [[replanning-on-new-knowledge]]. This page holds the cadence.

## The cadence and its conditions

The figure comes with its condition:

> If the development team’s velocity has remained fairly constant and iteration planning hasn’t introduced any big surprises, you may want to go as long as four to six weeks without formally updating the release plan.
>
> — [[cohn-agile-estimating-planning]], L2857

Cohn's default leans shorter: "many projects benefit from establishing a rule that the release plan will be revisited after each iteration" (L2857), and the summary says the plan is usually updated at the start of each iteration (L2973). Chapter 22 states the outer limit in iterations: "The release plan is updated either after each iteration or, at worst, after every few iterations." (L4833). It gives "every few" no number.

This wiki reads the two as one rule. Revisit after each iteration by default. The longer gap is an allowance earned only while both conditions hold, and four to six weeks is the outer limit under them, not a schedule.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Velocity trend | The last iterations' completed points, on [[velocity]] |
| Surprises in iteration planning | Whether expanding stories into tasks changed their size or revealed new ones, on [[iteration-planning]] |
| Plan assumptions | Team, iteration length, first and last dates, where stated on the [[release-plan]] |

This wiki's test: the longer gap was a mistake if the first update after it moved the plan by more than the steady velocity would have implied, or if people relied on a date the arithmetic had already ruled out.

## Sign of a violation

Seen in board history: the release plan has not changed since it was made, while iterations have completed. A stronger form is a plan whose story list still sums to more than remaining iterations × current velocity, so the plan is no longer arithmetically possible by [[fitting-stories-into-a-release]]. The source gives the rule without a sign, so both signs are this wiki's derivation.

## What breaks when it is ignored

This wiki's reading: the plan stops being the current expectation of where the team will arrive, which is the job the source gives it (L2773), and people relying on it for dates are relying on an old forecast.

## Trade-off

Each update costs attention, and this wiki reads a project with steady velocity as getting little from one, which is why the source allows the longer gap.

## Agent executor note

This wiki reads the need as strengthening where velocity history is short or unstable, since the stability condition for the longer gap cannot be shown. The update itself is arithmetic the plugin can prepare from board history, so its cost falls. The four-to-six-week figure comes from human teams on iterations of weeks and should not be carried over as a number.
