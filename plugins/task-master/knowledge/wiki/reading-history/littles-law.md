---
title: Little's Law
category: reading-history
summary: The relationship of averages that locks WIP, Cycle Time and Throughput together over a completed period; its practical value lies in its assumptions and not its arithmetic.
tags: [concept, flow-metrics, wip, cycle-time, throughput, retrospective]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Little's Law

Little's Law is the relationship among average [[work-in-progress]], average [[cycle-time]] and average [[throughput]] that holds for a queuing system over a period, provided the law's assumptions hold. John Little gave the first rigorous proof of the arrival form in 1961 ([[vacanti-actionable-agile-metrics]] L830, L850). Vacanti's position is that the arithmetic is the least useful part: "It is all about the assumptions." (L1002). Those assumptions are checked on [[littles-law-assumptions]] and turned into rules on [[process-policies-from-littles-law]].

## The forms

| Equation | Form | Stated in terms of |
|---|---|---|
| (1) | L = λ * W | Arrival Rate. L is average items in the system, λ is average arrivals per unit time, W is average wait time in the system (L834-L842) |
| (2) | CT = WIP / TH | Departure Rate, the form the Lean and Kanban community adopted (L876, L904) |
| (3) | TH = WIP / CT | Rearrangement of (2) (L890) |
| (4) | WIP = CT * TH | Rearrangement of (2) (L896) |

Equations (1) and (2) are logically equivalent as mathematics (L922), but they are not equivalent in what must be true for them to apply. Vacanti gives this its own callout:

> Looking at Little’s Law from the perspective of Throughput rather than from the perspective of Arrival Rate necessitates a change in the assumptions required for the law to be valid.
>
> — [[vacanti-actionable-agile-metrics]], L950

This wiki reads the consequence as follows: the everyday form on a board, Equation (2), is the one with the longer list of conditions.

## What it asserts

It is a relationship of averages, and "average" here means arithmetic mean (L830, L844). Vacanti says most knowledge-work discussions neglect this, and that the fact is only harmful when the law is used for something it was not meant for (L844). Little's own framing, as quoted by Vacanti:

> Little’s Law will not tell the managers how to handle trade-offs or provide innovations to improve their chosen measures, but it lays down a necessary relation.
>
> — [[vacanti-actionable-agile-metrics]], L850

Given any two of the three averages, the third follows (L852). Little's example is a wine rack that holds 100 bottles on average and is replenished at 2 bottles a week. A bottle therefore spends 50 weeks in the rack on average. The result needs no individual dates, no knowledge of ordering, no probability distributions and no bottle sizes (L854, L860).

This any-two property matters little on a board, because history already holds all three: "the three flow metrics’ data is so easy to capture that you should never have to compute one of them—just go look at the data!" (L998). This wiki reads that as follows: computing a value the board already records is not analysis. The useful act is comparing the board's behaviour with the assumptions.

## What it does not assert

- **It does not forecast.** The exact relation applies looking back over a completed period: "Little’s Law is about examining what has happened in the past." ([[vacanti-actionable-agile-metrics]] L3550). Its use on a forecast stops at a qualitative gut check; see [[littles-law-does-not-forecast]].
- **It does not say which metric moves.** Changing one metric will almost certainly affect one or both of the others (L908), and the law does not determine which. See [[starting-more-work]] for what this does to the usual advice.
- **It does not require equal-sized items.** See [[right-sizing-not-same-sizing]].

## Segmenting by work type

WIP may be split into types such as user stories, production defects and maintenance requests, and the law then applies to the whole system "as well as to each type or groups of types" (L1036). The practical use Vacanti names is diagnostic: ask which segment is violating the assumptions, for example defects alone, or defects grouped with maintenance requests (L1038). He defers segmenting by [[class-of-service]] to his Chapter 13 and warns that its effect on predictability is "usually bad" (L1040).

## Agent executor note

This wiki's reading, not the source's: the relation does not depend on who or what performs the service. Little's definition covers any stream of discrete items that arrive, wait, receive service and depart, and it explicitly allows for service that is not the bottleneck (L822). The arithmetic therefore carries over unchanged to an agent executing and a person steering. What changes is where the queue forms, which is likely at the person's review rather than at execution. That placement is an untested transfer. A team should read it from its own board history, not assume it.
