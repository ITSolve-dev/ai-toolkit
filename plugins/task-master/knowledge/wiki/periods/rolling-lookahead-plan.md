---
title: Rolling Lookahead Plan
category: periods
summary: A release plan that shows detail only for the next two or three iterations and drops completed ones; the window's length follows how often and how heavily work depends across streams.
tags: [method, iterations, release-planning, dependencies, multi-team]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Rolling Lookahead Plan

A rolling lookahead plan is a release plan kept detailed only for a short window ahead. The window moves forward as iterations finish.

> A rolling lookahead plan simply looks forward a small number of iterations (typically only two or three) and allows teams to coordinate work by sharing information about what each will be working on in the near future.
>
> — [[cohn-agile-estimating-planning]], L4225

## How it runs

Cohn's baseline from release planning is detail for only the next couple of iterations, because "that is often enough to support the interdependencies encountered by many teams" (L4166). With several teams, the plan is "updated to show and coordinate the work of the next two or three iterations" (L4166), and "As iterations are completed, details about them are dropped from the plan." (L4166). Laufer's name for this is "peering forward" (L4166). See [[planning-horizons]].

## Choosing the window

- **Input:** how often work depends across streams and how much those dependencies matter. "The exact number of iterations will, of course, depend on the frequency and significance of the dependencies between teams." (L4166). Read it from dependency links on planned tasks.
- **What shows it wrong:** a dependency surfacing at the start of an iteration that the window should have shown, with the work it blocks already planned. That argues for a longer window. Detail that keeps being discarded before the work arrives argues for a shorter one.

The source gives neither sign. Both are this wiki's reading of what the window is for.

## Worked example

Cohn's SwimStats project has two teams, each at an estimated velocity of 20 points per iteration, and 110 points of work, so three iterations on the arithmetic (L4153). Of the 110 points, 30 are an API and 40 more can only be done after it. To finish those 70 points in three iterations, both teams must use the API, and so Team 2's personal-records story depends on Team 1's API work (L4153-L4157).

The arithmetic of total capacity did not reveal this constraint. It appeared only once work was allocated across iterations and teams. This wiki reads that as the method's practical value: a short allocated window exposes an order the total hides.

## Adequacy, and what comes after it

"For most teams in most situations, a rolling lookahead plan is adequate." (L4172). When dependencies are too complex or frequent for it, the first move is to reduce them. See [[feeding-buffer]].

## Trade-off

Keeping the plan current is repeated work each iteration, and dropping detail means the far end of the release stays coarse. The chapter's epigraph, from Mary Poppendieck, states the attitude behind this: "Do the planning, but throw out the plans." (L4081).

## Failure modes

The source names neither of these. Both are this wiki's inference from the method's definition.

- **Frozen plan:** finished iterations remain detailed and the window has not moved. Sign: the plan's detailed section does not start at the current iteration.
- **Detail past the dependencies:** many iterations are detailed although no dependency reaches that far. Sign: detail beyond the last planned dependency.

## Transfer to a few people and an agent

The coordination purpose belongs to several teams and falls below Cohn's threshold. See [[multi-team-techniques-scale-limit]]. The transfer here is ours: what carries over is the single-team baseline, in which a plan keeps detail only for the next couple of periods. That is a rule already held by [[planning-horizons]], and it needs no lookahead document of its own.
