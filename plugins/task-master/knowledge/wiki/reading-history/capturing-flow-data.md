---
title: Capturing Flow Data
category: reading-history
summary: Flow analytics need one record per item holding the date it entered each workflow step, plus attributes that later serve as filters, including how the item ended. The record is no better than the board's use: late updates, uncaptured blockers and random moves leave history to repair or discard. A tracker's built-in flow charts are checked by deriving the same numbers from a sample of per-state dates.
tags: [method, flow-metrics, board-history, data, cycle-time, failure-mode, data-quality, charts, verification]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Capturing Flow Data

Flow data is a per-item record of the date the item entered each step of the workflow, decorated with attributes used for filtering. Every flow chart in the book is derived from this one shape, so the shape comes first. Vacanti's phrasing is: "you need to physically record the date that each work item enters each step of your workflow" ([[vacanti-actionable-agile-metrics]] L3806).

Figure 16.1, which shows the format, is absent from the raw text (L3814-L3816). The shape on this page is taken from the prose around it.

## The procedure

1. **List the workflow steps.** The source's example is "Analysis Active, Analysis Done, Development Active, Development Done, Test, Done" (L3806-L3812, rejoined across a line break).
2. **Record one date per item per step.** "you would need to document the day that each item entered each state" (L3812). See [[cumulative-flow-diagram]].
3. **Handle the special cases deliberately.** These are "work flowing backward, work skipping steps, work being cancelled versus closed" (L3828). Backward movement is treated in Chapter 4 of the source (L3818); see [[backward-movement]] and [[non-standard-departure]].
4. **Add attributes that will act as filters.** Examples: "which team worked on an item, what type it was (for example, user story, defect, etc.), if it finished normally" (L3820). The choice is free, and the reason to do it is filtering: "those attributes will serve as filter points later" (L3820).

## Two sources for the record

The source separates manual tracking from extraction from a tool (L3806, L3822). The second is "easier said than done" because "most Agile tools do not track data in this way" (L3828). The extraction has to produce the same shape, handle the same special cases and carry the same metadata (L3828). The tool-specific part is out of scope for this wiki and for the source (L3828).

This wiki reads the two cases as one rule: the shape of the record is fixed, and only its origin differs. This is also not hour logging, which the charter excludes. The record holds transition dates, which board history already holds when the board is used consistently; see board misuse, below.

## Signs that the record cannot support the analysis

These signs are this wiki's reading. Each one is a question to check.

- A finished item has one closing date and no dates for the steps in between.
- Cancelled and completed items cannot be told apart, so a cancelled item enters Cycle Time as a normal finish. The source's example filter is "all the items that got cancelled while in progress" (L3820).
- There is no type attribute, so defects and features share one distribution and cannot be read apart.

## Trade-off

Tagging costs attention on every item. The source calls it "a powerful practice that will enhance your understanding of overall process performance" (L3820) and gives no measure of the gain. For a few people, this wiki's reading is that the team attribute adds little, since there is rarely more than one, while type and how-it-ended still earn their place.

## Board misuse corrupts the record

This failure occurs when a board is not used consistently, so its history cannot support flow metrics however carefully it is extracted. The source's statement is flat: "Your data is only as good as your use of your Agile tracking tool" ([[vacanti-actionable-agile-metrics]] L3834). It holds for both electronic systems and physical boards (L3830).

### Observable signs

The source names three:

> If work items are not updated in a timely manner, or blockers not captured properly, or items are moved back and forth randomly, then that lack of attention to process policies will be reflected in your data.
>
> — [[vacanti-actionable-agile-metrics]], L3836

This wiki reads those as the following marks in board history, each of which raises a question to check (see [[smell-is-not-a-finding]]):

- **Late updates:** several states traversed by one item on the same day, or many items moved at one moment.
- **Uncaptured blockers:** an item idle in an active state for a long stretch with no blocked marker recorded.
- **Random moves:** repeated back-and-forth transitions that match no rework reason. See [[backward-movement]].

### What it costs

"no data extraction scheme will make up for abusing either your electronic or physical board" (L3836). Once the data is bad, the choice left is unpleasant: "try to fix the data or discard it altogether" (L3836). This wiki reads the second consequence as a reset of the sample: discarded history means [[how-much-flow-data]] starts again from zero.

### The rule

The prevention is upstream of the data. The source calls it "a much better strategy to make sure all team members use your Agile tracking tool in an agreed upon matter" (L3836-L3842). The agreement covers what is moved when, and what a blocker looks like on the board.

### Agent executor note on board misuse

The mechanism in the source is human lapse: people forgetting to update. This wiki's reading is that it only partly survives. An agent moving its own tasks timestamps them as it goes, so lateness on the executor's side should shrink. Lateness moves to the steps a person owns, such as review and acceptance, where a batch of approvals in one sitting produces the same false dates. Board-level automation can also add its own moves. The same signs apply, though they now point at the person's steps.

### See also, on board misuse

[[flow-metrics]], [[waiting-versus-blocked]]

## Verifying a tool's flow analytics

A chart generated by a tool should be checked against the same numbers derived independently, because its label does not show how it was computed. Vacanti's advice for anyone starting out is: "do not necessarily trust the data or charts that your Agile tool displays for you. Do not trust its associated calculations" ([[vacanti-actionable-agile-metrics]] L3918).

### The procedure

1. **Take a sample of per-state dates** in the shape set out at the top of this page: "initially track some sample data yourself" (L3918). [[how-much-flow-data]] says a small sample is enough to start.
2. **Derive the metrics.** "All you need to do is turn the above dates into WIP counts for the CFD, and subtract the first date in the workflow from the last date in the workflow to calculate Cycle Time for the Scatterplot and Histogram" (L3872). For the CFD, [[cumulative-flow-diagram]] says why the counts must come from entry dates.
3. **Compare with what the tool produces** for the same items: "compare it to what your electronic tool generates for you. You may be surprised at how different those results can be" (L3918).
4. **Check the known failures:** [[cumulative-flow-diagram]] and [[pseudo-control-chart]].

This wiki reads the source's closing question, "which method will you trust more?" (L3918), as a rule: on a disagreement, the derivation that can be traced to dates wins until the difference is explained.

### The same caution for instructions

The source also warns against generic chart recipes, because "(a) those websites do not assume you have your data in the proper format, and (b) the instructions they give can lead to improperly constructed analytics" (L3872). This wiki reads that as a warning about construction: the charts are simple to draw and easy to draw wrongly.

### How far to take the source's claims about tools

The source's claim that it has "yet to see an electronic tool that generates a CFD correctly" (L3884) comes with an exception for the author's own product, which the source itself calls a "shameless plug" (L3920). This wiki does not keep the survey claim: it is dated and comes from an interested party. It keeps the checks, which any reader can run, and the source's own hedge about its product: "do not take our word for it. Collect the data yourself and validate any results independently" (L3920).

### Trade-off of verifying

The check takes time, and the source calls it "tedious" (L3918). This wiki's reading is that it is a one-off per chart definition and not a recurring cost.

### Agent executor note on verifying a tool

The check does not depend on who executes. The consequence for this plugin is this wiki's own: since the plugin reads board history, it should compute flow numbers from transitions and not repeat a tracker's chart. Which trackers expose what is configuration and stays out of this wiki.

### See also, on verifying a tool

[[flow-metrics]], [[which-chart-for-which-plan-question]]

## Agent executor note

This wiki's reading: the method does not depend on a human executor. Where an agent moves its own tasks, the transition dates can be recorded as a side effect of the move, which removes the manual cost named at L3806. Moves made by the person steering still need the same discipline.

## See also

[[flow-metrics]], [[how-much-flow-data]], [[started-and-finished-points]]
