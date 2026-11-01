---
title: Starting New Work When Blocked
category: moving-work
summary: Reacting to a block by starting the next item raises WIP without finishing anything, and it looks like productivity on a points chart.
tags: [failure-mode, blocked, wip, pull, signs]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Starting New Work When Blocked

Starting new work when blocked is the habit of answering a stalled item by opening another. It feels productive and it keeps a points chart moving, but it adds to [[work-in-progress]] while the stalled item stays unfinished. It differs from [[starting-more-work-when-cycle-time-is-long]] in its trigger: there the pressure is a long Cycle Time, here it is one stopped item.

At Siemens HS ([[siemens-hs-case]]), two habits fed it. One was a hedge: "It had been common practice to start multiple features at one time to mitigate possible risks." ([[vacanti-actionable-agile-metrics]] L4026). The other was the reaction to a block:

> whenever a story or feature was blocked (for a variety of reasons such as waiting for a dependency from another team, waiting for customer validation, inability to test because of environmental or build break issues, etc.), teams would simply start the next story or feature so that we could claim the points which we had committed to achieve.
>
> — [[vacanti-actionable-agile-metrics]], L4026

This wiki reads the hedge as self-defeating on the source's own arithmetic: when arrivals outrun departures, each extra start raises average Cycle Time, the hedged items included ([[wip-lengthens-cycle-time]], [[conservation-of-flow]]).

## Observable signs

These signs are this wiki's reading of the passage above.

- In board history, an item enters a blocked state and a new item starts with no finish in between.
- Blocked count and in-progress count rise together.
- Items stay blocked for a long time while the team's points look normal; see [[velocity-masks-unfinished-work]].

These raise a question ([[smell-is-not-a-finding]]). A new start can be legitimate if the limit allows it and the blocked item truly cannot be helped.

## What stops it

The source's remedy is a pull system with WIP limits and not a stated rule about blocks: Siemens "instituted a policy of limiting WIP across all teams" (L4120). This wiki links that to [[blocked-work-counts-against-wip]]: only if a blocked item still occupies a slot does the limit stop the reflex. A limit that excludes blocked items gives no pressure to clear the block.

## Trade-off

Holding to the limit means capacity can sit unused while a block persists. The chapter does not price this, and it does not say how long a team should wait. This wiki's reading is that the case supports the direction and not a threshold.

## Agent executor note

The motive in the source, claiming committed points, is human and does not survive. The structure does, in this wiki's reading: an agent waits on a person or a dependency, and the person steering starts a second agent because the first is idle. The plugin's own test, that a started task can finish without waiting, treats a block inside a task as a possible bad cut; that test comes from the plugin's design, not from this source. See [[waiting-versus-blocked]] and [[sequence-versus-wait]].
