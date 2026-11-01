---
title: Percentile Spread
category: reading-history
summary: A wide gap between cycle time percentile lines signals process variability and makes each extra point of confidence expensive. The improvement aim is to shift all the lines down and close the gaps.
tags: [rule, retrospective-analysis, cycle-time, percentiles, variability, predictability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Percentile Spread

**Percentile spread** is the distance between the [[cycle-time-percentile-lines]] on a [[cycle-time-scatterplot]]. It is a reading of how variable the process is, and it sets the price of confidence when a [[service-level-expectation]] is chosen.

> A wider spread in those lines means not only a higher number of days that we must communicate for our SLA, but it also means that our process is suffering from more variability.
>
> — [[vacanti-actionable-agile-metrics]], L3036

Vacanti states that both effects reduce overall predictability (L3036).

## The worked case

Figure 12.1 comes from a real client, with percentiles of 20 days (50th), 25 days (70th), 54 days (85th) and 75 days (95th) (L3044). The source text labels this figure "Figure 8.6" at L3044, directly under the caption for Figure 12.1, which this wiki takes for a slip in the book.

Going from 70% to 85% confidence, "just a 15% increase in confidence", means going from 25 days to 54 days, more than double (L3044). The customer chose the 70% SLE to start. By the end of the project the team had shifted the lines so that the 85th percentile was 25 days, the figure the 70th had been months earlier (L3050).

> The team removed unnecessary variability, and, by definition, became more predictable.
>
> — [[vacanti-actionable-agile-metrics]], L3050

The book reports no measure of what work removed the variability beyond "the strategies outlined in this book" (L3050), and it is one client's project.

## The rule

Read the gaps between lines as well as the lines. Process improvement means shifting all the lines down "as much as possible (but no further!)" (L3036). The parenthesis marks a limit the chapter does not explain. This wiki reads it as saying that percentiles have a floor set by the work itself, so pressing below it stops being improvement.

## Sign

This sign is the wiki's phrasing: a large jump in days between neighbouring percentile lines, especially when the step to the commitment percentile is much bigger than the earlier ones. The book's own example gives one setting, 5 days from 50th to 70th and 29 days from 70th to 85th, and it states no threshold. The sign raises a question: what differs about the items in the top band?

## What to do

- At choice time, put the spread in front of the receiver, as in [[choosing-a-service-level-expectation]]: they may prefer a lower confidence at a far shorter promise.
- Look at the items in the top band, then at whether they share a type, which leads to [[sle-by-work-item-type]], or a cause, such as blockers or size, which leads to [[right-sizing]] and [[percentile-intervention-triggers]]. [[internal-and-external-variability]] says what the top of the stack usually means.

## Limits

This caveat is the wiki's: on few finished items the top percentiles rest on a handful of dots, so a wide spread at the 95th may be one outlier and not a property of the process. The chapter's data-point range of 11 to 30 is given for setting an SLE (L3054), not for reading spread. The arithmetic is on [[cycle-time-percentile-lines]].
