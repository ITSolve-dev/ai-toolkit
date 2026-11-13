---
title: Lateness Passes Down the Schedule
category: ordering
summary: A task with several prerequisites starts early only if all of them go well and starts late if any one goes badly, so dependent plans lose time and do not recover it; the asymmetry is structural and survives any executor.
tags: [failure-mode, dependencies, ordering, planning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Lateness Passes Down the Schedule

Where a task depends on several others, its start is exposed to an asymmetry: everything has to go well for it to start early, and one thing going badly is enough for it to start late.

> In other words, an early start requires a combination of things to go well, a late start can be caused by one thing going wrong.
>
> — [[cohn-agile-estimating-planning]], L602

Cohn's example is Figure 2.1, in which testing follows both coding of the user interface and coding of a middle tier, and the middle tier follows adding tables to a database (L575-L586). An early test start needs three things at once: the middle tier finishes early, the interface finishes early, and the tester is available early (L577-L581). A late start has four separate causes: the interface finishes late, the middle tier runs long, the middle tier starts late because the tables were late, or the tester is unavailable (L594-L600).

## How it compounds

Cohn joins this to [[parkinsons-law]]: because activities rarely finish early, "activities will start late and that the lateness will get passed down the schedule." (L604). He concludes that an early start for a task like testing is rarer still than an early finish (L604).

Cohn's list includes a person's availability alongside the task arrows. This wiki reads that as a warning about what a dependency graph leaves out: the figure draws three task prerequisites, and the fourth cause of lateness is on no arrow.

## Observable signs

- **In board state:** a task with a planned start or date and more than one unfinished prerequisite, whose date did not change when a prerequisite slipped.
- **In board history:** tasks with several prerequisites start later than planned more often than tasks with one.
- **In a forecast:** a date reached by adding durations along a chain, with no allowance at the points where chains merge.

These signs are this wiki's derivation from Cohn's figure.

## What to do

Cohn gives no treatment in this section. This wiki's reading is that exposure grows with the number of unfinished prerequisites, so two moves follow. Cut so that fewer tasks merge on one ([[independent-tasks]]), and do not state a date for a task without naming the prerequisites the date rests on. A wait held by an outside party is worse than a sequence, because the project cannot act on it ([[sequence-versus-wait]]).

The inputs are the prerequisites each task rests on, read from the task's text and its links on the board, and their finish dates, read from board history. This wiki's test of the choice: the cut was wrong if the merged-on task still started late for a cause outside the prerequisites named.

## Cost

This wiki notes that cutting to reduce merges can add scaffolding or duplicate work, and [[independent-tasks]] records that cost.

## Scale and setup

Figure 2.1 assumes separate roles for database, interface and testing. This wiki reads the structure as holding for a few people, since the arrows are between tasks and not between roles. A dated plan shows the effect directly. On a flow board there are no planned starts, so this wiki reads the sign as applying only when someone gives a date for such a task.

## Agent executor note

The asymmetry between all and any is structural and survives any executor. The compounding half rests on tasks rarely finishing early, which depends on a human mechanism, so it weakens: an agent can finish early, and on a board where the next task starts when its prerequisite finishes, that early finish can be used. This wiki adds that the availability item changes hands: an agent is rarely the missing resource, and the person steering, whose review a later task may need, is the likelier one. These two points are this wiki's and are unmeasured.
