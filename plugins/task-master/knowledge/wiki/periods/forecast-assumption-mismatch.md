---
title: Forecast Assumption Mismatch
category: periods
summary: A forecast is wrong when the model or its tool assumes a policy the process does not follow; one unmodelled pull order moved an 85th-percentile forecast from 65 to 100 days in Vacanti's scenario.
tags: [failure-mode, forecasting, pull-order, wip-limit, policies]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Forecast Assumption Mismatch

A forecast assumption mismatch is the gap between what a forecasting model assumes about how work moves and how work actually moves. Vacanti treats closing it as the main determinant of accuracy:

> Your model’s ability to produce an accurate forecast is going to depend on how well you match your process policies to your model’s assumptions.
>
> — [[vacanti-actionable-agile-metrics]], L3712

He defines process policies as "the day-to-day rules around how you operate your process" (L3708). The point is made about [[monte-carlo-simulation]].

## Assumptions live in two places

The source separates "the assumptions built into your model" from "the assumptions built into how whatever tool that you use" implements them (L3702). The second kind is the harder to see, because a tool can fill in what nobody modelled. In the first example below the tool "defaults to a strict FIFO pull order in the absence of any other policy being modeled" (L3728). Policies can be unstated on the process side too: the same example's random pull order is used "without explicitly stating it" (L3728). This wiki reads that pair as the shape of the failure: an unstated tool default meeting an unstated team habit, with neither visible in the model.

## Case 1: pull order (65 versus 100 days)

The scenario, from the book's Class of Service chapter (L3714), is a Kanban board with Standard and Expedite items, at most one Expedite item on the board, and Expedite items allowed to violate WIP limits and block Standard items (L3726). All of that is modelled correctly. The pull order between Standard items that finish at the same time is not modelled (L3726). The tool assumes FIFO; the real process pulls at random (L3728). See [[fifo-pull-order]].

The result, for Standard items at the 85th percentile: 65 days forecast, 100 days realised (L3730). "Due to that one missed assumption, you have over-optimistically forecast by up 35 days _per item_" (L3730).

These figures belong to that simulated scenario and are not portable. Vacanti adds that the problem "gets multiplied if you have hundreds of items in your backlog" (L3730) but gives no figure. This wiki notes that a per-item percentile gap does not simply add up across items that run in parallel, so the 35 days should not be multiplied by a backlog count.

The discriminating point is that nothing else in the model had to be wrong: the rest of the scenario was specified correctly, and one policy moved the percentile.

## Case 2: open WIP slot not pulled

In Figure 15.2 the Test column has a WIP limit of three and holds one item, three items wait in Development Done, and the board has stayed that way for several days (L3742). The simulation tool never allows that state, since it "automatically and immediately pulls an item from Dev Done to Test whenever Test has space under its WIP Limit" (L3742). Real items therefore age longer than the simulated ones (L3742). See [[wip-control]].

## Observable signs

Each sign raises a question to check, not a finding ([[smell-is-not-a-finding]]).

- **Board state:** a column below its WIP limit while the preceding done column holds waiting items, lasting days (L3742). What to check: whether the model assumes immediate pull.
- **Forecast against fact:** items aging past what the simulation showed (L3742), or realised percentiles running past the forecast ones (L3730). What to check: which policy in use is absent from the model.
- **Board history (our operationalisation, not the source's):** items entering work in an order other than the one they queued in, while the model assumes FIFO. What to check: what order the project actually means to pull in.
- **Tool configuration (our operationalisation, not the source's):** a policy with no modelled counterpart. What to check: what the tool does by default in its absence.

## What to do about a mismatch

The source gives two responses and requires one of them:

> you have to use the assumptions in your model (both explicit or implicit) as actionable interventions to take while you are actually operating your process, or you have to take action to change the assumptions in the model to match the real world as it unfolds.
>
> — [[vacanti-actionable-agile-metrics]], L3744

The source does not say how to choose. This wiki reads it this way: if the modelled policy is what the project wants, make the process follow it, as with pulling promptly into an open slot. If the model describes something the project does not intend or cannot hold, change the model and let the forecast move.

Either way the work continues after the forecast: "You need to actively manage to the assumptions in the model or change the model assumptions based on new information." (L3752). The chapter's takeaways rank this highest: "Most importantly, you have to manage to those assumptions!" (L3778). The trade-off, as this wiki reads it, is that a forecast obliges someone to watch the process it assumed for as long as it is relied on, or it stops being a forecast of that process.

## Agent executor note

The mechanism does not depend on human pace or memory: it depends on any gap between modelled and actual policy, so it survives an agent executing and a person steering. The transfer here is ours: with an agent executing, a person may still be the one who decides what is pulled next or who takes a presented result, so an assumption of immediate pull can fail at those points even where execution itself is quick. The chapter does not discuss this.
