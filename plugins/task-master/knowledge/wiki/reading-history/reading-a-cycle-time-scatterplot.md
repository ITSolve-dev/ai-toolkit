---
title: Reading a Cycle Time Scatterplot
category: reading-history
summary: A procedure for turning the shapes on a cycle time scatterplot into questions about the policy that produced them; the chart shows variation but does not classify it.
tags: [method, scatterplot, cycle-time, variation, visualization]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reading a Cycle Time Scatterplot

Reading a [[cycle-time-scatterplot]] means inspecting the shapes formed by finished items, plotted by finish date (X) and cycle time (Y), and turning each shape into a question about the policy that produced it. Vacanti treats the chart as a way to reach the right question sooner, not as a detector that returns an answer. That matches this wiki's stance that a sign raises a question, not a verdict: see [[smell-is-not-a-finding]]. The walk over a CFD's shapes is the sibling page, [[reading-a-cfd]].

## Procedure

1. **Look for a shape, not at single dots first.** The chapter's checklist has five things to look for ([[vacanti-actionable-agile-metrics]] L2992-L3006): a triangle that never flattens ([[triangle-on-a-scatterplot]]), clusters of dots, high or low ([[low-cycle-time-cluster]]), long periods of gaps ([[gap-on-a-scatterplot]]), extreme outliers, and dots that just cross a percentile line (both on [[internal-and-external-variability]]).
2. **Ask which policy produced it.** Vacanti's first question for any anomaly is “What policy (either explicit or implicit) do we have in place that is causing our data to look like this?” (L2852). Implicit counts: a habit nobody wrote down is a policy for this purpose.
3. **Ask whether it is good or bad.** The chapter's questions are “What’s going on with our Cycle Time?”, “Is what’s going on a good thing or bad thing?”, “If good, how can we keep doing it?” and “If bad, what interventions could make things better?” (L2982). The second one cannot be skipped, because a pattern that looks like an improvement can be a defect, as with [[low-cycle-time-cluster]].
4. **Change the policy, then check it on later data.** Vacanti's loop is to use the data to suggest a policy change, “then verify the change had the intended effect by further collecting and re-examining future data” (L2852). A change with no later reading of the same chart is unverified.

**Inputs, and where each is read from.** The finish date and cycle time of each finished item come from board history; the percentile lines are computed from the same history ([[cycle-time-percentile-lines]]). The CFD reading used to separate causes comes from the same transitions ([[cumulative-flow-diagram]]). Nothing here needs logged hours.

**What would show a reading wrong.** The policy change is made and the shape persists on later data, which is step 4's check.

## Why policy comes first, and where it stops

The chapter's maxim is “Your policies shape your data and your data shape your policies” (L2850), and Vacanti closes on “most of the causes of randomness are things we do to ourselves” (L2984). The same chapter also says that extreme outliers are usually caused from outside the team (L2960).

This wiki reads those two claims as compatible: shapes formed by many dots point at policy, while the few extreme dots at the top point outside. A reader who applies “it's our policy” to a 181-day item, or “it's external” to a triangle, has picked the wrong default for that kind of signal. The split is the wiki's reading and the chapter does not state it in that form.

## What the chart cannot say

**It does not classify variation.** Vacanti writes: “I believe that it is mostly impossible to classify variation of your data into things like “special causes” or “common causes” simply by looking at a Scatterplot” (L2936), and “Use the Scatterplot as a powerful way to visualize variation. But do not think it will magically categorize that variation for you.” (L2972). A finding that says a dot *is* special-cause overstates what the chart can support.

**Variation is not the enemy.** Vacanti's position is that variation “will always exist”, and that “the point is not to always try to drive variation out; rather, the point will be to understand the causes of that variation” (L2944). A goal stated as a narrower scatter, with no cause named, does not follow from this chapter.

**It avoids the SPC argument on purpose.** The chapter deliberately drops the language of Statistical Process Control, not from disagreement with Shewhart and Deming, but because for most people the path “leads to academic debates” over control limits, and “These types of debates only serve to cause confusion and miss the point of what we are trying to accomplish anyway.” (L2972). Control limits on a cycle time chart are therefore not part of this procedure; see [[pseudo-control-chart]].

**It cannot show open work.** The chart's fundamental property is that “dots do not actually show up until a work item has finished” (L2872). This wiki draws the consequence: an item stuck right now is absent from this chart, and it arrives later as a single high dot, after the moment to act has passed. A question about what is stuck now needs age of open work, not this chart; see [[flow-metrics]] and [[which-view-of-cycle-time]].

## Trade-offs and limits

- Reading shapes is a judgement. Vacanti says as much: “you are still going to have to think for yourself in order to get more predictable” (L2972-L2978, joined across a page break).
- The chapter gives no minimum number of dots for a shape to be meaningful, so a small board's shape is weaker evidence than the book's multi-year charts. The book's figures run over many months.

## Survival under an agent

This wiki's judgement is that the procedure survives an agent executing and a person steering: it reads board history and depends on no human memory. What moves is what a “policy” is. In this setting the likely policies are how tasks are cut, what order they are pulled in, and when the person reviews a presented result. That list is the wiki's own and is unsourced.
