---
title: S-Curve on a CFD
category: showing-work
summary: Between two moments of zero WIP a CFD typically goes flat, steep, flat, and Vacanti argues those flat ends make arrivals and departures hard to match and hurt predictability.
tags: [concept, cfd, zero-wip, iterations, predictability, methodology-difference]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# S-Curve on a CFD

An S-curve is "the typical pattern that emerges on CFD between any two time instances of zero WIP" ([[vacanti-actionable-agile-metrics]] L1904). It "is characterized by a flat beginning section, followed by a steep middle section, and finishing again with a flat end period" (L1904). Vacanti says the cause of the shape is beyond the scope of the section (L1914), so this page holds its sign and its consequence, not its mechanism.

## Where it appears

Vacanti gives two settings, both the special case of [[littles-law]] where system WIP may reach zero (L1902). [[littles-law-assumptions]] calls this the exact case.

- A project, which "usually begins with zero WIP and (ideally) ends with zero WIP".
- An "ideal Scrum sprint", which "starts with zero WIP and ends with zero WIP".

## What it costs

Vacanti asks whether, on such a curve, it is easy or even possible to match arrival and departure rates (L1914), which is the assumption [[mismatched-arrivals-and-departures]] depends on. He then states: "those flat spots add inefficiencies and kill predictability" (L1918-L1924).

His argument runs on as questions: whether managing projects this way is optimal, whether it is "predicatively optimal" to repeat the effect through zero-WIP-bounded sprints, and "How might we become more predictable day to day, week to week, month to month by never allowing WIP to go to zero?" (L1916). He limits the claim: "I am talking about predictability here, not necessarily about how accounting or finance sees the world" (L1916). He ends the section with "Just something to think about…" (L1926). This wiki reads this as a position argued from Little's Law's assumptions, not a measured result, and notes that no figure is given.

## Per project setup

This section is this wiki's reading. Scrum's ideal and Vacanti's preference disagree about whether WIP should reach zero at a boundary.

- **Setup with a fixed period that empties.** A repeating S-curve is what the setup produces. It is not a finding, and a forecast within the period should allow for the flat ends and not use the steep middle's rate.
- **Continuous setup with no emptying boundary.** A repeated return to zero WIP is unplanned, so it is worth asking why: arrivals may be batched, or the queue may be running dry.
- **Small board with an agent executing.** WIP may reach zero simply because nothing is waiting. Vacanti does not address this scale, and the argument against zero WIP assumes a steady supply of work, so this wiki would not read that case as a defect.

What would show the first reading wrong: the same work run without an emptying boundary gives steadier delivery with no loss elsewhere.
