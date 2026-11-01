---
title: Release Plan Level of Detail
category: periods
summary: A release plan holds stories, not tasks, assignees or in-iteration order, places work into named iterations only for the near term, because later detail is planned with less knowledge than it will have, and needs its detail in two places, what comes next and what may not make it.
tags: [rule, iterations, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Release Plan Level of Detail

A [[release-plan]] stays coarse on purpose. Detail is added as late as it can be, for specific reasons, which is the grain side of [[planning-horizons]].

## What stays out

> During release planning we do not want to create a plan that indicates which developers will work on which user stories or tasks or the sequence in which work will be performed within an iteration.
>
> — [[cohn-agile-estimating-planning]], L2781

Cohn calls that level of detail "dangerous and misleading during release planning" (L2781). Three things are excluded:

- **Who does what.** "Decisions about who works on what and the sequence of activities are best left to the individuals working on those tasks and are best deferred as long as possible." (L2781).
- **Sequence inside an iteration.** Same passage.
- **Engineering tasks.** Items are stories. "During release planning it is too early and some user stories may be insufficiently understood to be disaggregated into engineering tasks." (L2781). They are split at the start of the iteration that contains them (L2781); see [[iteration-planning]].

## What goes in which iteration

Placing stories into named iterations is optional, and the source gives the trade-off (L2838):

- **For:** more detail, useful when coordinating work among multiple teams.
- **Against:** it takes more time, and "even if we do preliminarily assign work to specific iterations, we do so with less knowledge than we’ll have at the start of each iteration."
- **Net:** "Undoubtedly, the plan will change as we learn more throughout the project.", so the effort should be weighed against that.

Cohn's own position:

> What I find to be a good compromise is to place specific work into the first one to three iterations, treating the rest of the release plan as one large bucket. It’s almost always worth allocating specific work to the first iteration, especially if it is starting immediately.
>
> — [[cohn-agile-estimating-planning]], L2838

The summary states the same thing in softer form: it is usually enough to identify the stories for the first couple of iterations and leave the rest to be placed later (L2969).

## Where the detail goes

The fictional case study in Chapter 23 (L4961) narrows this further, to two places. Everything between them is a stack in priority order: "I’ll stack up the story cards you said you really want in the release and that’s our plan" (L6207).

> The most important thing is to know what is going to be worked on next.
>
> — [[cohn-agile-estimating-planning]], L6195

> The next most important thing is to know those features at the bottom of the list that may or may not make it into the release.
>
> — [[cohn-agile-estimating-planning]], L6195

**The next period,** because the rest of the plan expires quickly: "In two weeks we’ll know so much more than we do today. Why plan what we’ll do in an iteration until we have to?" (L6203).

**The bottom of the list,** because items near the cut line are the ones an outside promise can get wrong: "we wouldn’t want marketing to design packaging that said, ‘Now with background music’ if that’s a feature that may get dropped at the last minute." (L6199). The source adds that this matters little at the first planning and more near the end of the release (L6199).

The exception is scale: "On a larger project, particularly with multiple teams that need to coordinate work, we might look ahead two or three iterations." (L6203). This wiki notes that the exception concerns coordination across teams, which is out of scope here, so for a few people the rule stands as stated. The form for several teams is [[rolling-lookahead-plan]].

## Sign of a violation

These signs are this wiki's reading, seen in board state:

- Stories assigned to iterations more than about three ahead.
- A release-horizon story already split into engineering tasks long before its iteration.
- Assignees or an internal order set on work that has not reached an iteration.
- An ordered list with no marked items that may not make it, while something outward-facing depends on them.

Each sign raises a question rather than a verdict. The source allows that some projects warrant more detail (L2838), and multi-team coordination is the reason it names. That reason is at a scale this wiki does not serve, so for a few people it rarely applies.

## What breaks when it is ignored

The source does not spell out how the misleading happens, so this reading is this wiki's. The plan claims precision it does not have, and a reader takes it as commitment ([[estimate-versus-commitment]]). Effort spent on far-iteration placement is lost when the plan changes, which the source expects.

## Trade-off

Following the rule leaves the far part of the release as an undifferentiated bucket, so the plan cannot answer what ships in a given late iteration, and someone who wants that answer gets a range ([[stating-plan-uncertainty]]). It also gives up any cross-team coordination that depended on that detail.

## Agent executor note

This wiki reads the two reasons differently. "best left to the individuals" (L2781) is a human-autonomy argument and does not carry over: with one agent there may be no choice of assignee to defer. The knowledge argument carries over unchanged and is the stronger of the two: a story expanded into tasks early is expanded on assumptions the earlier iterations may change, and an agent fills gaps by guessing, not by asking ([[underspecified-task]]). So the no-early-disaggregation rule survives on the second reason alone.
