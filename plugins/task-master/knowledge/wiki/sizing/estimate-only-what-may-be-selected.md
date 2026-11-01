---
title: Estimate Only What May Be Selected
category: sizing
summary: Every story with a reasonable chance of entering the upcoming release needs an estimate, because estimates are its price; work further out does not need one.
tags: [rule, estimation, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Estimate Only What May Be Selected

Estimation before a release has a bounded scope in both directions. [[estimating-by-horizon]] says how finely an item is estimated. This rule says whether it needs an estimate at all.

## Why the floor exists

"Because an estimate represents the cost of developing a user story, it is important that each has been estimated." ([[cohn-agile-estimating-planning]] L2810). Cohn's image is shopping for a whole wardrobe in a mall where every price tag has been removed, which he says is what choosing feels like for a product owner given no estimates (L2810). This wiki reads the mechanism as the one on [[tradeoff-needs-cost-and-benefit]]: priority weighs value against cost, and the capacity arithmetic on [[fitting-stories-into-a-release]] cannot run on an unestimated story.

## Why the ceiling exists

> It is not necessary to estimate everything that a product owner may ever want. It is only necessary to have an estimate for each new feature that has some reasonable possibility of being selected for inclusion in the upcoming release.
>
> — [[cohn-agile-estimating-planning]], L2812

Cohn adds that a wish list often extends two, three or more releases out, and that estimates on that more distant work are not needed (L2812).

## Input and where it is read from

What counts as a "reasonable possibility": this wiki reads it from the position on the ordered list relative to the release's capacity, with some margin past the line, since stories below it can move up when something is dropped. SwimStats shows the need for that margin: the 3-point story at the very bottom of the list ended up in the release (L2941-L2943), and this wiki notes it could only be weighed against the 8-point story because both had estimates. The margin is this wiki's addition; the source sets no figure.

## Sign of a violation

These signs are this wiki's reading, seen in board state.

- **Under:** an item in or near the planned release has no estimate. Whether that is a defect is judged on [[empty-fields]].
- **Over:** estimates sit on items with no realistic path into the upcoming release. These are weaker: the cost is wasted effort, not a wrong plan.

## Later fact that shows it wrong

A story left unestimated as distant is pulled into the release, which means the boundary was drawn too tightly.

## Trade-off

Leaving far work unestimated means the total size of the wish list is unknown, so a long-range answer about all of it is not available from this data.

## Agent executor note

This wiki reads the mechanism as being about the chooser, not the executor, so it survives. It also has a local reason: estimates on distant work go stale as the code changes under an agent's work. The source does not state that reason.
