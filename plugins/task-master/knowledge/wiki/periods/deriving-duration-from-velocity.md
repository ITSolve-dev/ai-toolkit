---
title: Deriving Duration from Velocity
category: periods
summary: Sum the size of the desired work, divide by velocity to get iterations, round deliberately, and map the result onto a calendar.
tags: [method, release-planning, velocity, planning-a-date]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Deriving Duration from Velocity

Duration is computed, not estimated: total size divided by velocity gives a number of iterations, and iteration length turns that into a calendar span. Cohn's summary states it directly:

> The duration of a project is not estimated as much as it is derived by taking the total number of story points and dividing it by the velocity of the team.
>
> — [[cohn-agile-estimating-planning]], L1056

This is the mechanical half of [[size-versus-duration]].

## Procedure

The procedure is Cohn's (L1021); the board-reading column is this wiki's mapping.

| Step | Action | Input read from |
|---|---|---|
| 1 | Sum the point estimates of all desired features | Estimates on the tasks in scope |
| 2 | Divide total size by [[velocity]] to get iterations | Past velocity from board history, or an estimate if none exists |
| 3 | Round: up, or remove enough scope to land on the lower whole number | The fractional result |
| 4 | Multiply by iteration length and count forward on a calendar | Iteration length, start date |

## Worked example

Cohn's example, with constructed figures (L1021): 100 points at a velocity of 11 per two-week iteration gives 100 ⁄ 11 = 9.1 iterations. He offers two options:

> We can either round that up to 10 iterations or find one point to remove so that it becomes 9 iterations.
>
> — [[cohn-agile-estimating-planning]], L1021

Cohn takes the conservative option, 10 iterations, which gives twenty weeks, and counts twenty weeks forward on the calendar (L1021).

## Limits

Cohn flags the method as a first approximation: "This very simplistic explanation of release planning works for now." (L1023). He says it is extended in Part IV, and that the example was simple because it used past velocity, whereas velocity must sometimes be estimated (L1023-L1029).

This wiki reads three limits from the chapter as written. The output is a single date with no range, which is what [[estimates-as-ranges]] and [[single-date-plan]] warn about. It assumes the total is complete, so unestimated items understate it, which is why [[estimating-underspecified-work]] matters here. It assumes the rate holds for the whole span. A derived date is also still an estimate until someone decides to hold to it, per [[estimate-versus-commitment]].

## Failure modes

These signs are this wiki's derivation. Each raises a question to check.

- **Rounding down with no cut.** The plan shows the lower number of iterations while the scope still divides to a fraction above it. In the example, 9 iterations with 100 points still in scope. Cohn allows 9 only with a point removed.
- **A date with no division behind it.** The date cannot be reproduced from the size total, the rate and the iteration length.
- **A stale rate.** The date was derived from a planned velocity and not recomputed after observed velocity differed.

## What would show the result wrong

This wiki reads two later facts as showing it: observed velocity over the first iterations differing from the rate used, or the total size changing. Either one calls for recomputing the date, not for re-estimating the work by default; see [[velocity-self-correction]] and [[re-estimate-when-relative-size-changes]].

## Which setup this applies under

The resolution here is this wiki's. The method presumes iterations. A milestone without fixed periods needs a rate per unit of calendar time in their place, which this chapter does not address; [[velocity]] states what that rate can be under each setup. Whether a unit is ended by a date or by a content set is on [[release-versus-iteration]].

## Agent executor note

The transfer here is this wiki's, not Cohn's. The division holds for any rate. Its value depends on whether the rate is stable in the given setup, which is the open question recorded on [[velocity]].
