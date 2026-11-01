---
title: Iteration Plan Versus Release Plan
category: periods
summary: Cohn's two stages of agile planning; a coarse release plan over months and a detailed iteration plan made as the iteration starts, which exists to refine the release plan's guesses with what has since been learned.
tags: [concept, iterations, planning, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Iteration Plan Versus Release Plan

An iteration plan and a release plan are the two stages of what Cohn calls one process. The release plan gives the long view with rough edges, and the iteration plan gives a detailed view of a single iteration, made as that iteration begins.

| | Release plan | Iteration plan |
|---|---|---|
| Planning horizon | 3-9 months | 1-4 weeks |
| Items in plan | User stories | Tasks |
| Estimated in | Story points or ideal days | Ideal hours |

The table is Cohn's ([[cohn-agile-estimating-planning]] L3061-L3065). The prose just before it says "usually three to six months out at the start of a new project" (L3057), while the table and the chapter summary (L3381) say three to nine. This wiki keeps the table's range and treats the difference as loose wording in the source.

## What the second stage is for

> The primary purpose of iteration planning is to refine suppositions made in the more coarse-grained release plan.
>
> — [[cohn-agile-estimating-planning]], L3069

Cohn gives two reasons the refinement has value: the release plan is "usually intentionally vague" about story order, and the team knows more at iteration start than when the release plan was last updated (L3069). This wiki reads the discriminating criterion as timing against knowledge. Detail belongs in a plan only when it is made late enough to use what has been learned. Cohn adds that an iteration plan "still has some rough edges and continues to be uncertain" (L3075), so the second stage narrows uncertainty without ending it.

## Levels in this wiki's vocabulary

Cohn's user story is this wiki's task, and Cohn's task is the level below it, which the plugin does not produce ([[unit-of-work]]). The transfer here is ours: for the plugin, the second stage means confirming the selection and order for the period, starting from a refreshed order ([[reprioritize-before-each-iteration]]). It does not mean expanding each task into hour-sized pieces, and how far the second stage looks into the how is on [[planning-stops-at-guesses]].

## Failure mode and its sign

The sign is this wiki's: detail written far past the coming period, such as fully sequenced work items several iterations out. That detail was fixed before the knowledge that should shape it existed, so it will either be rewritten or followed against better information. See [[how-far-to-split-up-front]] and [[release-plan-level-of-detail]].

## Agent executor note

The two-stage logic rests on when facts become known and not on who executes, so this wiki expects it to survive an agent executing. The horizons and the estimation units come from human teams. Ideal hours do not transfer ([[size-ceiling]]), and the choice of period length is on [[period-length]].

## Related

Filling the second stage is on [[velocity-versus-commitment-planning]] and [[filling-a-period]]. The levels of planning as a whole are on [[planning-horizons]].
