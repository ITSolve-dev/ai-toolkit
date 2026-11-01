---
title: Low Cycle Time Cluster
category: reading-history
summary: A tight group of unusually low dots is a question, not good news; a temporary surge in capacity produces it, and the skewed data then flows into forecasts and service levels.
tags: [failure-mode, scatterplot, cycle-time, forecasting, data-quality]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Low Cycle Time Cluster

A low cycle time cluster is a group of dots sitting well below the usual scatter over a short interval. Clusters of any height are a thing to look for (“Clusters of dots (either high or low)”, [[vacanti-actionable-agile-metrics]] L2996), and the chapter's sharper claim is about the pleasant-looking kind: “not all clusters of very low Cycle Times are good.” (L2912). A drop in cycle time is an event to explain before it is accepted as an improvement.

## What to ask

Vacanti's order for any cluster is “what’s going on here?”, then “is this a good thing or a bad thing?”, then what can be done if it is bad (L2910). The chapter then presses the reader on the second question: “Are you only thinking of good reasons? What might be some bad reasons that would cause this to happen?” (L2912). Only the low case is explored; the chapter names high clusters and does not work through one.

## The reasoning: why a temporary gain poisons the data

The bad reason Vacanti names is mandatory overtime. His arithmetic is that moving from 8-hour days and 5-day weeks to 12-hour days and 7-day weeks will probably improve cycle time, on the condition that WIP stays limited (L2912-L2918). The damage is to predictability: “Not only are long periods of mandatory overtime not sustainable but it also skews our data.” (L2918). He then puts the question that makes the point: “Do you really want to be offering an SLA or making a forecast with mandatory overtime as one of the upfront assumptions that is baked in?” (L2918).

This wiki keeps that mechanism and drops the practice. Overtime as a way of managing people is out of scope; what is in scope is that history used for a forecast or a [[service-level-expectation]] silently assumes the conditions it was produced under.

## Sign and check

- **Sign:** a band of dots clearly below the surrounding scatter, in a bounded interval, with the scatter returning afterwards or not yet returned.
- **Check:** name what changed in that interval. Inputs are the finish dates on the board, plus whatever the project records about who was available and what kind of tasks ran then.
- **Choice that follows:** whether those dots belong in the history used for forecasting. A condition that will not recur should not be baked in. This wiki infers that choice from Vacanti's question; he does not state a rule for excluding dots, and elsewhere in the chapter he argues for keeping outliers in ([[internal-and-external-variability]]).
- **Later fact that shows the choice wrong:** cycle time stays at the new level after the supposed temporary condition ended, so the change was real and belonged in the data.

## Survival under an agent

The overtime mechanism itself does not survive: an agent has no overtime, and its hours are not the constraint. This wiki's judgement is that the general form does survive. Any temporary change in capacity or in the mix of work lowers cycle time for a while, and a forecast reads it as the process. In a setting with a few people steering an agent, the plausible equivalents are a burst of unusually available review, or a run of tasks much smaller than usual. Those equivalents are the wiki's own and are unsourced.

## Source note

The book refers to the cluster chart as “Figure 8.11” at L2910 and L2912, while introducing and describing it as Figure 11.3 at L2900 and L2910. The discussion is plainly about the one chart; this reads as a stale cross-reference in the source. See also [[reading-a-cycle-time-scatterplot]] and [[velocity-trend-is-not-a-forecast]].
