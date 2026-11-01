---
title: Parkinson's Law
category: sizing
summary: Work expands to fill the time allowed, so a stated duration acts as permission and early finishes rarely appear; the mechanism is human, and only its visible form, additions nobody asked for, may survive an agent, for a different reason.
tags: [failure-mode, estimation, human-mechanism, board-history]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Parkinson's Law

Parkinson's Law is the claim, dated 1957 in Cohn's citation, that the time a task takes grows to match the time allowed for it. Cohn uses it to explain why activities on a schedule rarely finish early.

> Work expands so as to fill the time available for its completion.
>
> — [[cohn-agile-estimating-planning]], L563

Cohn's gloss is that "we take as much time to complete an activity as we think we’ll be allowed" (L565). This wiki treats that as a claim about behaviour under a stated duration, and not as a measured effect: the chapter reports no measurement, only a personal anecdote and the name of the law.

## The mechanism

Cohn gives the channel explicitly. When a chart shows five days, "it gives implicit permission to the developer to take up to that long to complete." (L571). The spare time is then used in one of two ways: gold-plating, meaning "adding a few bells and whistles", or other work the executor prefers (L569, L571). Cohn adds a motive for not reporting an early finish, which is that a manager may read it as a padded estimate or start expecting more early finishes (L569). This wiki keeps that motive only as part of the mechanism, since managing people is outside the charter.

## Observable signs

- **In board history:** for tasks that carried a stated duration, finishes sit at or after that duration and rarely before it. Cohn's claim is "What she will not do very often is finish the activity early." (L569). The one-sidedness is the sign, because accurate estimates would scatter on both sides. This reading of history is this wiki's.
- **In a presented result:** additions that no acceptance criterion asks for. This wiki reads that as gold-plating seen at review.

Either sign raises a question and does not settle one. A one-sided history can also come from estimates that are simply too low.

## Why it matters

What breaks is the benefit of an early finish. An estimate error in the favourable direction never reaches the plan, so errors in the other direction are not offset, and [[lateness-passes-down-the-schedule]] depends on exactly that: "we’ve already established that activities will rarely finish early." (L604).

This wiki adds a second consequence, which Cohn does not state. If durations fill the estimate, then past performance read from history partly records the estimates and not the work, which weakens it as an input to [[filling-a-period]].

## Limit

The mechanism as Cohn states it needs a stated duration. This chapter does not say whether a relative size step, which names no duration, gives the same permission.

## Agent executor note

This is a human mechanism, and this wiki does not carry it over as stated. An agent does not prefer one task to another, does not read a chart as an allowance, and does not fear being thought to have padded an estimate. Filling time therefore does not survive.

The visible form may survive with a different cause. This wiki's hypothesis is that an agent can add unrequested work when a task's boundaries are missing, which is a fault of the task text and has nothing to do with time ([[underspecified-task]]). No source here measures that. Where a person executes, the page applies as written.
