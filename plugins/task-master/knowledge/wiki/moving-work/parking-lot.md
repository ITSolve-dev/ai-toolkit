---
title: Parking Lot
category: moving-work
summary: A marked board area for items waiting on an outside party, with their time tracked; an item still parked past its expected end must become blocked.
tags: [rule, work-states, dependencies, kanban]
sources: [radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-01
---

# Parking Lot

A parking lot is a designated part of the board for items that are waiting on an outside party, so that they stop occupying an active state without disappearing. The source's instruction:

> You should designate a special area of the kanban board, a parking lot, for placing tickets that are currently waiting on an external group.
>
> — [[radzikowska-waiting-blocked]], L46

The source attaches one requirement and one expiry. The requirement is "Make sure to track the time the card spends in the parking lot." (L50). The expiry is that when the agreed time passes, the item is marked and managed as blocked (L53). [[waiting-versus-blocked]] holds the full test.

## The rule

Only an item that passes the waiting test goes in the parking lot, and an item stays there only until its expected end. After that it is blocked and is handled by [[blocked-work-counts-against-wip]].

## Sign of violation

- **In board state:** a parked item whose expected end has passed and which is not marked blocked.
- **In board state or history:** a parked item whose next step belongs to someone inside the project. The parking lot is then being used to hide work that could move.
- **In board history:** an item that has sat in the parking lot for much longer than others of its kind.

The time in the parking lot is read from board history, so the source's tracking requirement does not need a logged field. These signs are this wiki's derivation from L44-L53.

## Why

What breaks is sight of the stopped work. The source says a limit on the parking lot helps "to avoid losing sight of the stopped work" (L59). A parked item with no expiry can stay parked forever, because nothing about the board changes while it does.

## Cost

Parking removes an item from the active count, so it makes room for more work, and that can hide a stop. This is why the expiry is part of the rule and why [[parking-lot-wip-limit]] exists. A task parked after it started has also failed the charter's first working test ([[unit-of-work]]), which [[sequence-versus-wait]] addresses.

## Agent executor note

Waiting on an outside party does not depend on who executes, so the rule survives. Tracking time and checking expiry fall to the plugin, because an agent has no reason to look at a parked task. The source reports no measurement.
