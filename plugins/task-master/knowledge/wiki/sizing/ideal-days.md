---
title: Ideal Days as a Measure of Size
category: sizing
summary: An ideal day estimates a task's size while ignoring the environment's overhead, so it converts to duration through velocity just as story points do. Its weakness is that the unit reads like a calendar day.
tags: [concept, estimation, ideal-days, size, velocity]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ideal Days as a Measure of Size

An **ideal day** is a unit for estimating work: how many uninterrupted days a user story would take to develop, test and accept ([[cohn-agile-estimating-planning]] L1133), under the assumptions listed on [[ideal-time-vs-elapsed-time]]. A discussion question in the chapter takes one ideal day as "8 hours of uninterrupted, focused work" (L1161). Cohn's claim is that once overhead is left out, the number measures size rather than duration.

## Why it counts as size

When estimating in ideal days "it is not necessary to consider the impact of the overhead of the environment in which the team works" (L1133). Cohn's example is a screen that takes one ideal day whether he works at a startup with no overhead or at a huge bureaucracy. Only the elapsed time differs, and as demands on his time grow, "the amount of elapsed time to complete one ideal day of work will increase" (L1137).

> When considerations of organizational overhead are ignored, ideal days can be thought of as another estimate of size, just as story points are.
>
> — [[cohn-agile-estimating-planning]], L1139

Cohn draws the conversion from that: "an estimate of size expressed as a number of ideal days can be converted into an estimate of duration using velocity in exactly the same way as with story points" (L1139). See [[velocity]], [[story-points]] and [[size-versus-duration]].

The claim is qualified in the chapter summary: "ideal days are an estimate of size, although less strictly so than story points" (L1155). That chapter does not say why. Chapter 8 does: "Story points are a _pure_ measure of size. Ideal days are not." (L1580), because an ideal-day number also moves with how good the executor is. See [[ideal-day-estimate-decay]] and [[executor-bound-estimates]].

## Why estimate this way rather than in elapsed days

Cohn's reasoning is about what the estimator must consider: "Estimating in elapsed days requires us to consider all of the interruptions that might occur while working on the story." (L1155). An ideal estimate considers only the time the story itself takes (L1155). This wiki reads the difference as a forecast of the environment: an elapsed estimate has to make one, which makes it harder and ties the number to current conditions.

## Telling a size from a disguised duration

This wiki reads the startup-versus-bureaucracy example as a test: a size estimate should not change when the environment does. The sign of a violation is an estimate raised or lowered because of something outside the task, such as a week of meetings, a holiday or support duty. That sign raises a question and is not a verdict: check whether the task itself changed. If it did not, the number was carrying elapsed time, and the overhead will be counted twice once velocity converts it.

## One number per task

Cohn gives the estimate as a single aggregate figure and not one per role. That rule and its exception are on [[one-estimate-per-task]].

## Trade-offs

This wiki reads the unit's strength as being easy to explain, since it is a day, and that as also its weakness, because the same word invites reading the number as calendar time. That is the failure described at [[ideal-estimate-read-as-deadline]], and its pressure form is on [[ideal-days-compared-to-actual-days]]. Which unit to use is on [[story-points-or-ideal-days]].

## Agent executor note

This wiki reads the separation of size from duration as surviving and the unit's anchor as not surviving. An ideal day is calibrated on a person's focused day, and a day of agent execution is not that quantity. The transfer here is ours: because velocity is measured from fact, the conversion to duration still works if the numbers are used consistently as a relative scale. It stops working once anyone treats them as literal days of a person's work. This wiki would answer the chapter's discussion question about how many elapsed hours make one ideal day (L1161) from how long tasks lived on the board, not from logged hours.
