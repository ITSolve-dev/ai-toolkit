---
title: Parking Lot
category: moving-work
summary: A marked board area for items waiting on an outside party, with their time tracked; an item still parked past its expected end must become blocked. Wester rejects such areas, so this wiki narrows the parking lot to a declared exception under a WIP control. Its first limit is set from its own history, slightly above the mean and between the mean and the historical upper limit (radzikowska-waiting-blocked L61), then adjusted empirically.
tags: [rule, work-states, dependencies, kanban, wip]
sources: [radzikowska-waiting-blocked, kanban-guide, wester-board-design]
created: 2026-11-01
updated: 2026-11-02
---

# Parking Lot

A parking lot is a designated part of the board for items that are waiting on an outside party, so that they stop occupying an active state without disappearing. The source's instruction:

> You should designate a special area of the kanban board, a parking lot, for placing tickets that are currently waiting on an external group.
>
> — [[radzikowska-waiting-blocked]], L46

The source attaches one requirement and one expiry. The requirement is "Make sure to track the time the card spends in the parking lot." (L50). The expiry is that when the agreed time passes, the item is marked and managed as blocked (L53). [[waiting-versus-blocked]] holds the full test.

## The rule

Only an item that passes the waiting test goes in the parking lot, and an item stays there only until its expected end. After that it is blocked and is handled by [[blocked-work-counts-against-wip]]. Whether to use a parking lot at all depends on the setup, as set out below.

## Sign of violation

- **In board state:** a parked item whose expected end has passed and which is not marked blocked.
- **In board state or history:** a parked item whose next step belongs to someone inside the project. The parking lot is then being used to hide work that could move.
- **In board history:** an item that has sat in the parking lot for much longer than others of its kind.
- **In board history:** items entering the parking lot at the moment their state reaches its limit. This is the stash [[wester-board-design]] describes at L51.

The time in the parking lot is read from board history, so the source's tracking requirement does not need a logged field. These signs are this wiki's derivation from L44-L53.

## Why

What breaks is sight of the stopped work. The source says a limit on the parking lot helps "to avoid losing sight of the stopped work" (L59). A parked item with no expiry can stay parked forever, because nothing about the board changes while it does.

## Cost

Parking removes an item from the active count, so it makes room for more work, and that can hide a stop. This is why the expiry is part of the rule and why the parking lot has a limit of its own (below). A task parked after it started has also failed the charter's first working test ([[unit-of-work]]), which [[sequence-versus-wait]] addresses.

## Agent executor note

Waiting on an outside party does not depend on who executes, so the rule survives. Tracking time and checking expiry fall to the plugin, because an agent has no reason to look at a parked task. The source reports no measurement.

## The parking lot WIP limit

A limit on the parking lot caps how much work can be stopped on outside parties at once. This rule chooses: it sets a number. The source gives two cases and says a limit is available in both:

> A dependency parking lot buffers work between one kanban system and another. If the dependent system exhibits stability and predictable lead times, then it is possible to limit WIP in a dependency buffer without causing too much stress.
>
> — [[radzikowska-waiting-blocked]], L57

> Even if the dependent system doesn’t exhibit stability and predictability, a WIP limit can still be set for the buffer to avoid losing sight of the stopped work. The WIP limit acts as a stressor, potentially causing upstream stalling within the kanban system.
>
> — [[radzikowska-waiting-blocked]], L59

### Setting the first limit

The source's method:

> The WIP limit established for the first time should be set slightly higher than the average WIP. Assuming the dependency parking lot buffer was previously unbounded, a study of historical data will suggest an upper limit, and the new WIP limit should be set somewhere between the upper limit and the mean calculated using Little’s Law.
>
> — [[radzikowska-waiting-blocked]], L61

This wiki notes that the source does not define "upper limit" or say how to compute it. The mean and the sense of "slightly higher" are therefore the usable parts. After that the source says to "adjust the WIP limit empirically" until "a stable value has been realized" (L63).

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How many items have been parked over time | Board history |
| The average of that count | Calculated from board history |
| Whether the outside parties keep to their times | Board history: time parked against expected end |

The limit is too high if it is never reached, because then it does nothing. Reaching the limit while every parked item is within its expected time is the stress the source intends: the limit "acts as a stressor, potentially causing upstream stalling", to be discussed and escalated (L59). This wiki reads the limit as too low only if it is full for weeks with that stress never acted on.

### Scale note

The source writes for kanban systems feeding each other. For a few people, this wiki reads "the dependent system" as an outside party. With only a handful of parked items there is little history to compute from, so the first limit is a judgement near the usual count. That fallback is this wiki's, and the source does not address so small a case.

### Cost of the limit

The source names the cost: "potentially causing upstream stalling" (L59). It also places this practice at Maturity Level 4 (L76), which [[blocked-work-counts-against-wip]] records as a cost and not as a condition.

### Agent executor note on the limit

The source calls the limit a stressor, a human mechanism. With an agent the stall is mechanical: the limit is reached and pulling stops. The arithmetic does not depend on the executor. Whether a parking-lot limit earns its cost on a very small board is not shown here, and the source reports no measurement.

### Related to the limit

The bound on the whole workflow is on [[wip-control]], which also borrows this page's starting point. The Guide's view of whether parked items count at all is in the positions below.

## Positions

**Kanban Maturity Model:** as above.

**Kanban Guide:** the Guide has no parking lot. A parked item is between the started and finished points, so by L112 of [[kanban-guide]] it is still WIP, and leaving it out of the count is an exception that has to be "made explicit as part of the DoW" (L143). This wiki reads a parking lot as allowed under the Guide only as a declared exception.

**Wester:** disagrees, on this wiki's reading. The post does not mention parking lots. It says "say goodbye to Blocked or On Hold columns – or any other column with the same purpose." ([[wester-board-design]] L49), and a designated area for stopped work has that purpose. Its objections are that the location of the wait is lost, that such a column becomes "a place to stash work so they can get around their WIP limits", and that the return brings backward movement (L51).

**Scrum Guide:** no such area, since it has no board.

## Which holds under which setup

The charter asks for a resolution and not a report of the disagreement. This one is this wiki's, and both sources are practice with no measurement. Take the first case that applies.

1. **The wait recurs at the same place for a kind of work, and the task goes forward afterwards.** It is a handoff, so it gets a state of its own ([[column-versus-attribute]]) and not a parking lot.
2. **Iteration setup with no WIP control.** There is no count to leave, so a parking lot buys nothing. Mark the task in place.
3. **A WIP control exists, and the task passes the waiting test on [[waiting-versus-blocked]], and leaving it in the count would stop pulling for a time nobody can shorten.** A parking lot is acceptable, as an exception declared in advance, with the expiry and a parking lot WIP limit (above).
4. **Anything else.** Mark the task in place, and it counts ([[blocked-work-counts-against-wip]]).

Case 3 is narrow on purpose, and it is mostly a matter for small limits: with a bound of two, one long outside wait takes half the capacity for something nobody can shorten. Against Wester's three objections, the Kanban Maturity Model's safeguards answer two. Board history still shows which state a task left, and the limit and the expiry restrain the stash. The third stands: a task returning from a parking lot is a [[backward-movement]], and this is the cost of case 3.

The choice was wrong if parked tasks regularly pass their expected end, if the parked count grows, or if tasks enter the lot as their state reaches its limit. It was also wrong in the other direction if a limit stayed full for weeks on a wait nobody could shorten and nothing else moved.
