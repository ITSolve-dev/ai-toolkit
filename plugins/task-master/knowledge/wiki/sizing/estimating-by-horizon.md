---
title: Estimating by Horizon
category: sizing
summary: Near-term items are written and estimated fine, distant or undecided ones stay epics or themes; every item with a reasonable chance of entering the upcoming release, plus a margin past the cut line, carries an estimate, and work further out needs none.
tags: [decision-rule, estimation, epic, theme, decomposition, rule, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Estimating by Horizon

How finely an item is written and estimated depends on how soon it will be worked on and how sure anyone is that it will be. Cohn distinguishes near-term stories, which must be small, from epics and themes, which may stay large. This page is the test between the two courses. It applies the reach and grain of [[planning-horizons]] to the estimate.

## Terms

In Cohn's usage an epic is one large user story. A theme is a set of related stories treated as a single entity for estimating or release planning, and an epic is often a theme on its own by size alone ([[cohn-agile-estimating-planning]] L1248, L1250). Its other use, as the unit of value when ordering, is on [[theme]].

## The test

**Near:** "User stories that will be worked on in the near future (the next few iterations) need to be small enough that they can be completed in a single iteration." (L1254). These get the fine scale, for Cohn 1, 2, 3, 5, 8.

**Distant:** "User stories or other items that are likely to be more distant than a few iterations can be left as epics or themes." (L1258). For these he adds 13, 20, 40 and 100 (L1258).

**Undecided:** horizon is not the only ground for staying large. Cohn writes: "For features that we’re not sure we want (a preliminary cost estimate is desired before too much investment is put into them) or for features that may not happen in the near future, it is often desirable to write one much larger user story." (L1248). This wiki reads that as two independent reasons: an item may be close and still undecided, and it still stays coarse until the decision is made.

## Trade-off

Cohn states the saving: "By aggregating some stories into themes and writing some stories as epics, a team is able to reduce the effort they’ll spend on estimating." (L1252). The cost comes in the same passage: "it’s important that they realize that estimates of themes and epics will be more uncertain than estimates of the more specific, smaller user stories." (L1252). This wiki reads the rule as an instance of [[estimating-effort-by-purpose]], since a preliminary cost decision does not need a fine number.

## Failure modes

- **A coarse item arrives at the top unsplit.** Sign: an item in the next ordering sits on a step above the fine scale. It fails the near test. The fix is cutting, per [[story-splitting-patterns]], and not re-estimating. The sign and fix are this wiki's reading of L1254.
- **A coarse number read as a fine one.** Sign: an epic's step is added to a period's commitment alongside task estimates, or quoted as a date. The source warns of the uncertainty and leaves the sign to us.
- **Distant work split early.** Sign: many fine tasks far down the order, estimated and later closed or rewritten unstarted. The reasoning is on [[how-far-to-split-up-front]].

## When estimates are made

Cohn names two occasions (L1352, L1354). The first is a batch before or at the start of a project. His "two or three meetings of from one to three hours" describes a human team and depends on "how many items there are to estimate, the size of the team, and the product owner’s ability to succinctly clarify the requirements" (L1352), so this wiki does not carry the figure over.

The second is ongoing: estimating new work near the end of each iteration, because "it allows new work to be considered in the prioritization of the coming iteration" (L1354). Cohn says teams set a deadline for themselves, "typically either that all stories must be estimated by the end of the day or by the end of the iteration" (L1356).

This wiki reads the second as the rule that survives without the meeting: **new work is estimated before the next time the order is decided.** Sign: an unestimated task in the pool when a period is filled. Whether that is a defect is judged on [[empty-fields]].

## Which setup

Cohn's horizon is counted in iterations. The resolution here is this wiki's.

- **With iterations:** near means the next few iterations, as he says, and the single-iteration bound holds.
- **Without iterations:** there is nothing to count, so near means the top of the order: what could be started next. The bound becomes the [[size-ceiling]] question for a flow setup.
- **Under both:** undecided items stay coarse whatever their place.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How soon the item will be worked on | Its place in the order; iteration capacity where iterations exist |
| Whether anyone has decided to do it | The task or its parent request |
| What the estimate is for | Whatever asked for it |

The choice was wrong if an item left coarse was pulled in unsplit and overran, which [[overrun-triggers-a-recut]] handles, or if an item written fine was dropped or rewritten before it started, so the effort bought nothing.

## Agent executor note

This wiki reads the grounds for staying coarse as that the work may change and may not happen, and neither depends on who executes, so it expects the rule to survive. The agent changes one input: writing an item fine is cheap to produce, so the cost that matters is the fine item going stale and needing review. No source here measures that. The single-iteration bound is denominated in a human team's capacity and is re-read from the project's own history.

## Estimate Only What May Be Selected

Estimation before a release has a bounded scope in both directions. The test at the top of this page says how finely an item is estimated. This rule says whether it needs an estimate at all.

### Why the floor exists

"Because an estimate represents the cost of developing a user story, it is important that each has been estimated." ([[cohn-agile-estimating-planning]] L2810). Cohn's image is shopping for a whole wardrobe in a mall where every price tag has been removed, which he says is what choosing feels like for a product owner given no estimates (L2810). This wiki reads the mechanism as the one on [[prioritization-factors]]: priority weighs value against cost, and the capacity arithmetic on [[fitting-stories-into-a-release]] cannot run on an unestimated story.

### Why the ceiling exists

> It is not necessary to estimate everything that a product owner may ever want. It is only necessary to have an estimate for each new feature that has some reasonable possibility of being selected for inclusion in the upcoming release.
>
> — [[cohn-agile-estimating-planning]], L2812

Cohn adds that a wish list often extends two, three or more releases out, and that estimates on that more distant work are not needed (L2812).

### Input and where it is read from

What counts as a "reasonable possibility": this wiki reads it from the position on the ordered list relative to the release's capacity, with some margin past the line, since stories below it can move up when something is dropped. SwimStats shows the need for that margin: the 3-point story at the very bottom of the list ended up in the release (L2941-L2943), and this wiki notes it could only be weighed against the 8-point story because both had estimates. The margin is this wiki's addition; the source sets no figure.

### Sign of a violation

These signs are this wiki's reading, seen in board state.

- **Under:** an item in or near the planned release has no estimate. Whether that is a defect is judged on [[empty-fields]].
- **Over:** estimates sit on items with no realistic path into the upcoming release. These are weaker: the cost is wasted effort, not a wrong plan.

### Later fact that shows it wrong

A story left unestimated as distant is pulled into the release, which means the boundary was drawn too tightly.

### Trade-off

Leaving far work unestimated means the total size of the wish list is unknown, so a long-range answer about all of it is not available from this data.

### Agent executor note

This wiki reads the mechanism as being about the chooser, not the executor, so it survives. It also has a local reason: estimates on distant work go stale as the code changes under an agent's work. The source does not state that reason.
