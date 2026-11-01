---
title: Bulging Band on a CFD
category: showing-work
summary: A widening CFD band signals a WIP explosion in that step, whose cause may lie upstream or downstream, and a queue band that bulges or stays thick is the worse case.
tags: [failure-mode, cfd, wip, queue, predictability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Bulging Band on a CFD

A bulging band is a workflow step's band on a [[cumulative-flow-diagram]] widening over time. Any such bulge "clearly signals an explosion of WIP in that particular workflow step" ([[vacanti-actionable-agile-metrics]] L1860). The band's thickness at a date is the [[work-in-progress]] in that step.

## Sign

A band visibly wider than its own earlier width. Vacanti gives no ratio.

## What breaks

"large WIP is bad because it almost always results in longer Cycle Times and poorer predictability" (L1866). Vacanti's first question is "what is causing our increased WIP" (L1866).

## Causes the source names

Vacanti's answer depends on the situation, and he offers examples (L1872):

- The team is ignoring WIP limits and starting new work arbitrarily.
- Several key team members have gone on holiday for extended periods.
- Work is progressing slowly due to poor requirements or poor design.

## The cause may not be in the step that bulges

"the cause of the increased WIP may not necessarily be found in the workflow step where the bulge appears" (L1874). Vacanti names a push from a previous step, or a blockage in one or more downstream steps, and warns: "Do not be lulled into thinking the problem is always in the obvious place." (L1874)

This wiki turns that into a check on the neighbouring lines. If the line entering the step steepened while the line leaving it held, look upstream at what pushed the work in. If the line leaving it flattened while the line entering it held, look downstream at what stopped pulling. This test is ours, and the chart only says where to look next.

## Queue bands are the worse case

Vacanti recommends splitting each workflow step into "Active" and "Done" sub-steps and graphing both. The "Done" sub-steps are queuing columns: "columns where no value add work is happening; work is just sitting there waiting to be pulled" (L1876). See [[active-versus-queued]].

"while a bulging band in general is bad, a bulging band in a queuing step can be especially bad" (L1876). Queue bands should be "as thin as possible", and "Whenever those bands are constantly thick or whenever they bulge, then that pattern is suggesting something is going wrong with our process" (L1876).

This wiki reads that as giving queue bands a second sign that active bands lack: a band need not grow to raise the question, because staying thick is enough. [[bottleneck-on-the-cfd]] takes a thick queue band from sign to procedure.

## With an agent executing

This wiki reads the causes differently under an agent. Starting past a limit survives if the limit is what the person dispatching work ignores. Poor requirements survive and probably sharpen, since an executor that guesses cannot fill the gap from context. The holiday cause survives only for the person. A queue band in front of a person's review measures that person's part, so a thick one there says something about review and not about execution.
