---
title: Capturing Flow Data
category: reading-history
summary: Flow analytics need one record per item holding the date it entered each workflow step, plus attributes that later serve as filters, including how the item ended.
tags: [method, flow-metrics, board-history, data, cycle-time]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Capturing Flow Data

Flow data is a per-item record of the date the item entered each step of the workflow, decorated with attributes used for filtering. Every flow chart in the book is derived from this one shape, so the shape comes first. Vacanti's phrasing is: "you need to physically record the date that each work item enters each step of your workflow" ([[vacanti-actionable-agile-metrics]] L3806).

Figure 16.1, which shows the format, is absent from the raw text (L3814-L3816). The shape on this page is taken from the prose around it.

## The procedure

1. **List the workflow steps.** The source's example is "Analysis Active, Analysis Done, Development Active, Development Done, Test, Done" (L3806-L3812, rejoined across a line break).
2. **Record one date per item per step.** "you would need to document the day that each item entered each state" (L3812). See [[cfd-built-from-entry-dates]].
3. **Handle the special cases deliberately.** These are "work flowing backward, work skipping steps, work being cancelled versus closed" (L3828). Backward movement is treated in Chapter 4 of the source (L3818); see [[backward-movement]], [[non-standard-departure]] and [[accounting-for-abandoned-work]].
4. **Add attributes that will act as filters.** Examples: "which team worked on an item, what type it was (for example, user story, defect, etc.), if it finished normally" (L3820). The choice is free, and the reason to do it is filtering: "those attributes will serve as filter points later" (L3820).

## Two sources for the record

The source separates manual tracking from extraction from a tool (L3806, L3822). The second is "easier said than done" because "most Agile tools do not track data in this way" (L3828). The extraction has to produce the same shape, handle the same special cases and carry the same metadata (L3828). The tool-specific part is out of scope for this wiki and for the source (L3828).

This wiki reads the two cases as one rule: the shape of the record is fixed, and only its origin differs. This is also not hour logging, which the charter excludes. The record holds transition dates, which board history already holds when the board is used consistently; see [[board-misuse-corrupts-flow-data]].

## Signs that the record cannot support the analysis

These signs are this wiki's reading. Each one is a question to check.

- A finished item has one closing date and no dates for the steps in between.
- Cancelled and completed items cannot be told apart, so a cancelled item enters Cycle Time as a normal finish. The source's example filter is "all the items that got cancelled while in progress" (L3820).
- There is no type attribute, so defects and features share one distribution and cannot be read apart.

## Trade-off

Tagging costs attention on every item. The source calls it "a powerful practice that will enhance your understanding of overall process performance" (L3820) and gives no measure of the gain. For a few people, this wiki's reading is that the team attribute adds little, since there is rarely more than one, while type and how-it-ended still earn their place.

## Agent executor note

This wiki's reading: the method does not depend on a human executor. Where an agent moves its own tasks, the transition dates can be recorded as a side effect of the move, which removes the manual cost named at L3806. Moves made by the person steering still need the same discipline.

## See also

[[flow-metrics]], [[how-much-flow-data]], [[verifying-tool-flow-analytics]], [[process-boundaries]]
