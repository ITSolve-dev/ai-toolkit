---
title: Reading a Cumulative Flow Diagram
category: showing-work
summary: A fixed walk over the shapes of a CFD that turns each shape present into a question to check against context, never into a verdict.
tags: [method, cfd, visualization, flow, board-review]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reading a Cumulative Flow Diagram

Reading a [[cumulative-flow-diagram]] (CFD) is the qualitative pass over the chart: walk a short list of shapes and, for each one present, ask the question that shape raises about the process. Vacanti states the purpose as asking and not concluding: "the reason we visualize flow via a CFD is so that we can begin to ask the right questions sooner" ([[vacanti-actionable-agile-metrics]] L1778). The output of a reading is a list of things to check, not a list of faults.

## Preconditions

- **Context.** "If you look at a CFD without understanding the context in which it was created, then all you are doing is looking at a picture." (L1776) Vacanti calls the diagrams "very context specific" (L1776).
- **The quantitative reading comes first.** Vacanti says qualitative analysis of a CFD requires sound knowledge of how to do the quantitative analysis, and sends readers who skipped it back to his Chapters 4 and 5 (L1780-L1788). See [[reading-flow-metrics-off-a-cfd]].
- **Little's Law assumptions, for any forecast.** "the predictive power of your CFDs depends almost entirely on how well your process obeys the assumptions behind Little's Law" (L1964-L1970). See [[littles-law]].

## The walk

The checks below follow the closing list of his Chapter 6 (L1974-L1986).

| Check | Sign on the chart | Question it raises | Page |
|---|---|---|---|
| Arrival rate against departure rate | Top line steeper than bottom line | Why is more starting than finishing? | [[mismatched-arrivals-and-departures]] |
| Bulges | A band widens | What is causing the increased WIP, and is the cause really in this step? | [[bulging-band-on-a-cfd]] |
| Disappearing bands | A band thins out to nothing | Is it the reporting interval, starvation, or a skipped step? | [[disappearing-band-on-a-cfd]] |
| Flat lines | A line stays horizontal over a long period | Why is nothing getting done, and what gets it flowing? | [[flat-lines-on-a-cfd]] |
| Stair steps | A flat stretch followed at once by a jump | How is this batch affecting predictability? | [[stair-steps-on-a-cfd]] |
| S-curve | Flat, then steep, then flat, between two moments of zero WIP | Does the setup need WIP to reach zero? | [[s-curve-on-a-cfd]] |
| Nothing wrong | Lines look even and close | What could improve next, and what could the picture be hiding? | [[what-a-cfd-cannot-answer]] |

For anything found, Vacanti's closing questions apply: "What's going on with our flow?" "Is it a good thing or bad thing?" "If good, how can we keep doing it?" "If bad, what interventions can we take to make things better?" (L1948-L1954).

## Failure modes of the reading

- **Snap judgement.** "you will be tempted to jump to snap judgments the next time you see a Cumulative Flow Diagram. Do not." (L1778) This wiki takes the sign to be a finding that states a cause from the shape alone, with no question to check.
- **Reading the list as complete.** Vacanti offers these as "some of the more common things you will come across", and says all possible patterns would fill a book (L1948).

## What a finding should carry

Vacanti gives no threshold for how steep, how long or how thick a shape must be. This wiki does not invent one. It reads the charter's rule that a sign raises a question ([[smell-is-not-a-finding]]) as requiring a finding to name the shape, its date range, the line or band involved, and what to check next.

The cost of the method follows from that. Without the project's context, a reading yields questions and no conclusions.

## Agents and small teams

This wiki's reading is that the shapes survive an agent executing, because they are arithmetic on counts taken from board history. The causes do not all survive: several of Vacanti's examples are about people, such as holidays and ignored limits, and each pattern page notes which carry over. Vacanti does not discuss scale here. This wiki adds that on a board with few items a single move can change a shape, so a short stretch deserves less weight than the same stretch on a busy board.
