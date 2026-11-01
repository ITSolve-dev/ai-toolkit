---
title: Parking Lot WIP Limit
category: moving-work
summary: How to set a first limit on the parking lot from its own history, what the limit does, and what later fact shows it is wrong.
tags: [rule, wip, kanban]
sources: [radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-01
---

# Parking Lot WIP Limit

A limit on the [[parking-lot]] caps how much work can be stopped on outside parties at once. This rule chooses: it sets a number. The source gives two cases and says a limit is available in both:

> A dependency parking lot buffers work between one kanban system and another. If the dependent system exhibits stability and predictable lead times, then it is possible to limit WIP in a dependency buffer without causing too much stress.
>
> — [[radzikowska-waiting-blocked]], L57

> Even if the dependent system doesn’t exhibit stability and predictability, a WIP limit can still be set for the buffer to avoid losing sight of the stopped work. The WIP limit acts as a stressor, potentially causing upstream stalling within the kanban system.
>
> — [[radzikowska-waiting-blocked]], L59

## Setting the first limit

The source's method:

> The WIP limit established for the first time should be set slightly higher than the average WIP. Assuming the dependency parking lot buffer was previously unbounded, a study of historical data will suggest an upper limit, and the new WIP limit should be set somewhere between the upper limit and the mean calculated using Little’s Law.
>
> — [[radzikowska-waiting-blocked]], L61

This wiki notes that the source does not define "upper limit" or say how to compute it. The mean and the sense of "slightly higher" are therefore the usable parts. After that the source says to "adjust the WIP limit empirically" until "a stable value has been realized" (L63).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How many items have been parked over time | Board history |
| The average of that count | Calculated from board history |
| Whether the outside parties keep to their times | Board history: time parked against expected end |

The limit is too high if it is never reached, because then it does nothing. It is too low if it is reached constantly while the parked items are all within their expected times, because it then stalls work over delays nobody can shorten.

## Scale note

The source writes for kanban systems feeding each other. For a few people, this wiki reads "the dependent system" as an outside party. With only a handful of parked items there is little history to compute from, so the first limit is a judgement near the usual count. That fallback is this wiki's, and the source does not address so small a case.

## Cost

The source names the cost: "potentially causing upstream stalling" (L59). It also places this practice at Maturity Level 4 (L76), which [[blocked-work-counts-against-wip]] records as a cost and not as a condition.

## Agent executor note

The source calls the limit a stressor, a human mechanism. With an agent the stall is mechanical: the limit is reached and pulling stops. The arithmetic does not depend on the executor. Whether a parking-lot limit earns its cost on a very small board is not shown here, and the source reports no measurement.

## Related

The bound on the whole workflow is on [[wip-control]], which also borrows this page's starting point. The Guide's view of whether parked items count at all is on [[parking-lot]].
