---
title: Malformed CFD
category: showing-work
summary: A chart labelled a CFD that breaks its definition, seen as a falling line, a line that falls once later steps are hidden, an outer line that is not arrivals or departures, a graphed backlog whose time the reported Cycle Time leaves out, or a plotted projection; the harm is wrong conclusions about the process and a team that stops trusting the chart.
tags: [failure-mode, showing-work, cfd, board-history, charts, arrivals, departures]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Malformed CFD

A malformed CFD is a chart presented as a [[cumulative-flow-diagram]] that breaks the definition. Vacanti's concern is practical: "an improperly constructed CFD can lead to improper conclusions about process problems", and worse, "improperly constructed CFDs can lead to team or management apathy amid claims that the charts are just not very useful." ([[vacanti-actionable-agile-metrics]] L1176). The defect lies in how arrivals and departures are counted, and any reading taken from such a chart is void: "Not accounting for arrivals and departures properly invalidates any resultant analysis of your chart." (L3890)

## Signs

Vacanti's checklist has three signs (L1526-L1532). The fourth comes from Property #1 in the body of his Chapter 4. Chapter 16 adds two tests for a chart a tool generated, set out below.

| Sign on the chart | Source | What to check |
|---|---|---|
| A line falls: "If any line on the chart slopes downward on any part of the graph." | L1528 | Whether the chart was built from counts, or a count was decremented. See [[cfd-built-from-entry-dates]] |
| A backlog is plotted: "If something that sounds like a “backlog” has been graphed (remember, a visualized backlog may not necessarily be bad—but it usually is!)." | L1530 | Whether backlog items are committed. See [[backlog-versus-commitment]] |
| A projection is plotted: "If some type of projection has been plotted." | L1532 | Whether the viewer is meant to read the future off a chart of the past |
| An outer line is something else: "Any chart that contains additional outside lines that do not represent process arrivals and departures is not a CFD." | L1242 | What the extra line is, such as a target or a scope line |

A falling line is the strongest of these. "You can immediately spot that a CFD has not been constructed properly if you see lines on the chart that go down." (L1406). A proper one has lines that are "either increasing (going up) or are flat" (L1406). Chapter 16 calls it the "telltale sign" (L3884), and this wiki notes that it is close to a proof, unlike most signs on a board: a cumulative count cannot fall.

The backlog sign is softer by the source's own wording: it allows that a graphed backlog may be fine. As everywhere here, a sign raises a question and is not a verdict; see [[smell-is-not-a-finding]].

## Two tests for a tool's chart

**A line falls once later steps are hidden.** A chart with no falling line can still fail. The test is to "try to “turn off” some of the latter workflow steps (if you can) starting from the bottom up. Do you see any of the remaining lines go down now? If so, it is a safe bet that the overall CFD has not been built according to all of the required CFD principles" (L3892).

This wiki reads the mechanism as follows: a correct chart plots, for each step, how many items have reached it so far, so hiding a later step leaves the other lines unchanged. A line that falls only when later steps are hidden suggests that the tool counts items sitting in a state at that moment and stacks those counts ([[cfd-built-from-entry-dates]]). The test requires a tool that can hide steps, so being unable to run it proves nothing.

**A backlog whose time is not counted.** The source does not ban a backlog: "Strictly speaking, there is nothing wrong with displaying a backlog on a CFD" (L3894). The issue is what the chart's lines then mean:

> CFD Property #1: The top line of a Cumulative Flow Diagram _always_ represents the cumulative arrivals to a process. The bottom line on a CFD _always_ represents the cumulative departures from a process.
>
> — [[vacanti-actionable-agile-metrics]], L3904

So approximate average Cycle Time runs from the top line to the bottom line, and if the chart "includes a backlog and your tool’s computed Cycle Time does not include the time spent in the backlog" the source says to be skeptical of the calculation (L3906). It also asks whether the tool calls its figure approximate at all, or would "lead you to believe it is an exact Cycle Time" (L3894-L3900).

This wiki resolves that through [[process-boundaries]] and [[backlog-versus-commitment]]: if the backlog is inside the arrival point, its time counts as Cycle Time; if it is outside, it does not belong on the chart. A chart that draws it and excludes its time is using two definitions of arrival at once.

## What to do on a sign

Derive the same chart from per-state dates as in [[verifying-tool-flow-analytics]]. A falling line needs no further evidence. This wiki reads the other signs as questions to check, because a wrong result may come from the tool or from how the board was used; see [[board-misuse-corrupts-flow-data]].

## The check runs one way

This wiki adds a limit the source does not state. No falling line does not prove correct construction. A count-based chart looks clean over any stretch in which nothing moved back or left, so it passes until the first such event, and a chart can pass every sign here and still sit on the wrong boundaries. Absence of the signs clears the chart of these defects and nothing more.

A second limit: a chart passing every test can still fail to show a process problem, since a violated assumption "will not clearly reveal itself on a CFD" many times (L1284).

## What breaks when ignored

The source names the conclusions and the apathy (L1176) but gives no case. This wiki reads the likeliest concrete error from Property #2: a falling line makes arrivals or finished work seem to shrink, so a reader sees flow that recovered, or a process that took in less, when items were only re-labelled or removed.

## Agent executor note

These are tests of a chart and depend on no executor. This wiki reads them as usable on a chart a tracker supplies, without knowing how the chart was computed, which is their value to a review of someone else's board.
