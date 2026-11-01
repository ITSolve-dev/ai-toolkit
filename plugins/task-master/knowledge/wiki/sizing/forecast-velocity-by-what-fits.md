---
title: Forecast Velocity by Seeing What Fits
category: sizing
summary: When no history exists and no iteration can run, expand a representative sample of stories into estimated tasks until available capacity fills, then range the resulting points; the hours arithmetic is human and does not transfer to an agent.
tags: [method, velocity, capacity, release-planning, numbers, human-executor]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Forecast Velocity by Seeing What Fits

This method derives [[velocity]] with no history and no iteration, by simulating one: expand stories into estimated tasks until an iteration's capacity is full, then count the points that fit. Cohn calls it "very similar to iteration planning" ([[cohn-agile-estimating-planning]] L3801). It is the last resort in [[choosing-velocity-estimate-approach]]: "Forecasting velocity is rarely your first option" (L3686). It applies when the project is too far off or too uncertain to spend on, such as one that starts in twelve months or only once a contract is signed (L3684), and in strategic planning and budgeting ahead of a project (L3781).

## Procedure

The steps are at L3688-L3694.

1. Estimate the hours each person can give the project per day.
2. Multiply out the hours for the iteration. Four people at six hours for ten days is 240 (L3718).
3. Pick stories, expand them into tasks and estimate those, until capacity is reached.
4. Sum the points or ideal days of what fit, and convert that to a [[velocity-estimate-range]].

The SwimStats example fits nine stories, 25 points and 221 hours, against 240 hours available, and the 25 becomes 15-40 (L3728, L3732-L3736, L3740-L3751). The stopping point is a judgement: the team "could commit to this but probably no more" (L3728). Capacity is not filled to the hour. This wiki reads that as the forecasting form of adding stories until no more can be committed ([[velocity-versus-commitment-planning]]).

These are planning hours, estimated ahead. They are not logged hours, which this wiki excludes.

## Rules inside the procedure

**The sample must be representative.** Priority order is not needed: "What you really want is a fairly random assortment of stories" (L3724). Do not expand only the one- and two-point stories, and do not expand only user-interface or database stories (L3724). Sign: the expanded set is all one size or one layer of the system.

**Capacity is capped by the scarcest skill, not by the total.** Hours do not pool across people who cannot do each other's work: "Select stories until one skill set on the team can’t handle any more work" (L3726). Sign: the total fits, but the tasks needing one specialist exceed that person's hours. The same check appears on [[iteration-capacity]].

**No adjustment for holidays or sickness.** "Don’t bother; it’s not worth the extra effort and it’s unlikely to be more accurate anyway" (L3720). The availability figure already allows for them.

**Part-time members need a per-person table.** With a uniform figure the SwimStats team gets 240 hours; listing Sergey at 4, Yury at 6, Carina at 2 and Sasha at 6 gives 180 (L3757-L3773). Carina is the mechanism to note: split across two projects, she could give nearly six hours in total, yet is shown at two on this project, because she moves between them many times a day and "this multitasking impacts her productivity" (L3759-L3763). See [[multitasking]].

## Numbers and their conditions

| Figure | Setting | Standing |
|---|---|---|
| 4-6 hours per day | Individuals assigned full-time to one project | Cohn's opinion, "From observation and discussion with colleagues" (L3704) |
| 55% of time on project activities | An empirical measurement | Citation unresolved in this copy, printed as "(TBD: REFBOEHM)" (L3704) |
| 80% | Toyota engineers, under a lean process | Kennedy 2003, cited as the high end (L3704) |

A large bureaucracy sits at the low end and a three-person startup at the high end (L3706).

Story points and task hours do not move in lockstep. In Table 16.2 a 1-point story has 14 hours while a 2-point story has 12 (L3745, L3748), so this wiki warns against converting a points total into hours from an average ratio ([[story-points-do-not-convert-to-hours]]).

## What later fact shows it wrong

Actual velocity from the first real iterations falls outside the range, at which point the actuals replace it (L3793).

## Agent executor note

The transfer here is ours. The hours arithmetic, the 4-6 hour figure and the Carina case all rest on a human's divided day, and they do not survive an agent executing: an agent has no meetings or e-mail eating its day. Two parts of the method do survive. Sampling representatively still prevents a biased estimate, and the scarcest-skill cap still applies with a different resource, which this wiki expects to be the steering person's attention for review and acceptance. That last point is a hypothesis with no support in this source. It should not be used as a number.

This wiki reads the method, for a few people steering agents, as mostly a fallback for budgeting before any iteration is possible, since an iteration there is likely cheap enough to run instead; see [[run-iterations-to-observe-velocity]].
