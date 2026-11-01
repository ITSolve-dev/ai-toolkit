---
title: Triangle on a Scatterplot
category: reading-history
summary: Dots rising in a wedge mean cycle time is growing; it is expected while a process fills from empty, and a defect when it never flattens, from arrivals exceeding departures or from flow debt.
tags: [failure-mode, scatterplot, cycle-time, flow-debt, wip]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Triangle on a Scatterplot

A triangle on a [[cycle-time-scatterplot]] is a wedge of dots whose upper edge rises over time. Vacanti says it appears “in any situation where Cycle Time increases over” time ([[vacanti-actionable-agile-metrics]] L2858-L2866, joined across a page break). The pattern on its own is not a defect: it is expected while a process fills from empty. The sign to act on is a triangle that keeps growing, which the chapter lists as “A triangle pattern that never flattens out” (L2994).

## Why the shape is a triangle

The explanation rests on the chart's basic property, that a dot appears only when an item finishes. Vacanti: “the longer the Cycle Time (the dot’s Y- component) the longer the amount of time we are going to have to wait (the dot’s X-component) to see that data point” (L2872). Long-lived items therefore land late on the chart, which pushes the top of the scatter up and to the right.

This wiki adds a consequence: the right-hand edge of any scatterplot under-represents long items, because the ones still in progress have not landed yet. A chart read at its right edge looks better than the process is.

## The cases, and how to separate them

| Case | What the CFD shows | Is it a defect? |
|---|---|---|
| Starting from zero WIP | Lines start together while steps fill | No, if it flattens |
| Arrivals exceed departures, WIP never at zero | Top and bottom lines diverge | Yes |
| Flow debt | Lines stay matched, and the triangle is there anyway | Yes |

The table's first column is Vacanti's two major cases, with the start-up situation split out from the first. The discriminating test is his too: “If Arrival Rate and Departure Rate are matched, then the only way you will not see a triangle on your Scatterplot is if you control Flow Debt.” (L2896).

**Starting from empty.** While steps fill, “work will be pulled in faster than it departs—even if we are limiting WIP” (L2882), so a WIP limit does not prevent this triangle. Once stable flow occurs, “the expectation is that the triangle will eventually flatten out into a more predictable arrangement” (L2882); Figure 11.2 shows this happening when the process stabilizes (L2888).

**Arrivals exceed departures.** When WIP never reaches zero, “a triangle will form whenever you have a nontrivial period of time where the top line and bottom line on your CFD diverge” (L2890). Vacanti's example is a team that did not control WIP for almost the whole timeline: “Not controlling WIP will only cause Cycle Times to get longer and longer and longer.” (L2890). The mechanism is on [[wip-lengthens-cycle-time]], the CFD form on [[mismatched-arrivals-and-departures]], and the response is [[wip-control]].

**Flow debt.** “Even if a team explicitly controls WIP, Flow Debt can occur.” (L2896). Vacanti's reading of the shape: “The items at the bottom of the triangle were those items that were pulled preferentially through the process (for whatever reason) whereas items toward the top of the triangle were left to age unnecessarily (again, for whatever reason).” (L2896). The named causes of arbitrary aging are blocks, too much WIP, and poor or misunderstood pull policies (L2896). This case is the trap: a team that holds its WIP limit and sees a triangle has not ruled out a pull-order problem. See [[flow-debt]], [[artificially-aged-work]] and [[blocked-work-counts-against-wip]].

## Sign and check

- **Sign:** on the scatterplot, the top of the dots keeps rising with no plateau, past the point when the process should have filled.
- **Check first:** read the CFD for the same interval. Divergent lines point at intake exceeding finishing. Matched lines point at pull order and aged items.
- **Later fact that settles it:** after WIP is held or the aged items are pulled through, later dots should flatten. A triangle that continues means the cause was not the one assumed.

The chapter gives no duration after which a triangle counts as not flattening, and this page does not invent one.

## How the reading goes wrong

- **Calling a start-up triangle a defect.** A project read before it has reached stable flow shows a triangle whatever its policies. This wiki notes that a short project may never leave this phase, so its whole history can be a triangle with nothing wrong in it; the plugin should say so and not raise a finding.
- **Stopping at “we limit WIP, so it isn't that”.** That excludes one cause only. Flow debt remains.

## Survival under an agent

This wiki's judgement is that the mechanism survives: dots land at finish whoever executes, and the shape is arithmetic. The causes shift. An agent does not pick favourites, so preferential pulling, in this setting, would come from the order the person or the plan sets, or from easy tasks being re-prioritized past older ones. Arrivals exceeding departures would come from tasks being generated faster than presented results get reviewed. Both transfers are the wiki's own and are unsourced. See [[reading-a-cycle-time-scatterplot]].
