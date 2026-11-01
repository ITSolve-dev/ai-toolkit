---
title: Ideal Estimate Read as a Deadline
category: sizing
summary: A number meant as uninterrupted work gets counted off on a calendar, so the date is wrong from the moment it is written. The sign is a date derived from an estimate with no conversion through velocity.
tags: [failure-mode, estimation, ideal-time, dates]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ideal Estimate Read as a Deadline

An estimate given as uninterrupted work is received as calendar time, and a date is set from it directly. Cohn's scene: a manager asks "How long will this take?", a team member says "five days", and "the manager counts off five days on her calendar and marks the day with a big red X" ([[cohn-agile-estimating-planning]] L1119). The team member meant something else:

> Five days if that’s all I do; but I do a lot of other things so probably two weeks.
>
> — [[cohn-agile-estimating-planning]], L1119

This wiki reads the two-week figure as an illustration of the shape of the problem, not a measured ratio.

## Why it happens

This wiki reads the two people as using different quantities under the same word; see [[ideal-time-vs-elapsed-time]]. Neither states which. It reads the [[ideal-days]] unit as making the confusion easier, because its name is a calendar word.

## The sign

- A due date equals a start date plus the estimate, with no conversion in between. [[estimate-versus-commitment]] reads the same sign for a different failure: a date nobody decided to hold to.
- An estimate appears as a bare number of days, with no statement of whether it means ideal or elapsed.
- Board history shows tasks finishing late by a consistent factor. This wiki reads a steady ratio as pointing at an unconverted estimate rather than at poor estimating, and a scattered one as pointing elsewhere. That reading is ours, and the sign is a question to check.

## What to do

This wiki derives two steps from the chapter. State the quantity whenever a number is given, so a size is never mistaken for a duration. Produce a date only through [[velocity]], which is the conversion Cohn names for ideal days (L1139), by the method on [[deriving-duration-from-velocity]].

## Agent executor note

This wiki reads the failure as surviving, and possibly as worse. The mechanism is two readers of one number, and a person planning around an agent's output is still a reader. The transfer here is ours: a task that executes quickly but then waits for review looks like it should finish on the day it starts, so a date set from execution time alone leaves out the wait.

Related: [[estimate-is-not-a-promise]], where the problem is what a date is taken to mean and not which quantity it holds; [[ideal-days-compared-to-actual-days]], where the comparison with the calendar becomes pressure on the unit itself.
