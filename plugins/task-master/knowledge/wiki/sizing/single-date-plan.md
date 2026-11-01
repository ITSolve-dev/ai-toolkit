---
title: Single-Date Plan
category: sizing
summary: A plan reduced to one date loses the assumptions behind it and cannot be judged; a usable forecast gives a range, the near-term work, its assumptions and how progress will be measured.
tags: [failure-mode, estimation, forecast, plan-content]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Single-Date Plan

A single-date plan is a forecast stated as one date or duration with nothing showing how it was reached. Cohn's diagnosis:

> Far too often a plan is reduced to a single date and all of the assumptions and expectations that led to that date are forgotten.
>
> — [[cohn-agile-estimating-planning]], L457

## What an estimate does not promise

> A plan does not guarantee an exact set of features on an exact date at a specified cost.
>
> — [[cohn-agile-estimating-planning]], L457

Cohn says a plan "describes one possibility of what may come to pass" and establishes "a set of baseline expectations" (L457). Whether anyone has agreed to answer for a date is a separate question, on [[estimate-versus-commitment]].

## Why it breaks

The reader of a bare date cannot assess it. In Cohn's example, an answer of seven months with no explanation leaves no way to tell "whether I’ve thought about the question sufficiently or whether my estimate is realistic", and he concludes "You should be skeptical of my estimate." (L463).

This wiki adds that the bare date also claims more precision than the [[cone-of-uncertainty]] allows while work is unresolved, and that once the assumptions are gone, nobody can tell which change in fact should move the date.

## What the plan should carry instead

Cohn's alternative is a plan that (L465):

- estimates completion in a range: "seven to nine months"
- shows what work will be completed in the first one or two months
- documents key assumptions
- establishes an approach for how progress will be measured collaboratively

With these, Cohn says the reader "can look at my plan and draw conclusions about the confidence you should have in it." (L465). The rule for the range itself is on [[estimates-as-ranges]]. This page is the wider failure: a range with no assumptions and no near-term work still cannot be judged.

## Observable sign

The rule detects an omission, so the omission is its sign. This wiki reads it as: a forecast or milestone recorded as one date, with no range, no stated assumptions and no named near-term work. A sign raises a question; a date imposed from outside, such as a fixed event, is not an estimate, and the question there is what scope fits it. See [[changing-the-plan-without-changing-the-date]].

## Trade-off

This wiki notes that a range is less satisfying to the person asking and takes longer to produce. Cohn does not treat that as a reason to give one number. He expects precision to grow with time: early a plan may say the third quarter rather than the second, later it needs to be more exact (L469). See [[good-plan-test]].

## Agent executor note

This wiki reads the mechanism as surviving unchanged: the failure is on the reader's side, and the person steering is that reader. If anything an agent makes it worse, since it will produce a confident date on request. The plugin should not emit a date without its range and assumptions.
