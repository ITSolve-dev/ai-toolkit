---
title: A Velocity Estimate Is a Range
category: sizing
summary: State estimated velocity as a range sized to the evidence behind it, never as one number; a date computed from a single velocity figure inherits a precision nobody has.
tags: [rule, velocity, range, release-planning, false-precision]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# A Velocity Estimate Is a Range

An estimate of [[velocity]] is given as a range whose width reflects how much is actually known, not as a single figure. Cohn holds this across every way of arriving at the number: "regardless of which approach you are using, if you need to estimate velocity you should consider expressing the estimate as a range" ([[cohn-agile-estimating-planning]] L3598). The chapter's summary repeats it as the closing rule (L3803). This is [[estimates-as-ranges]] applied to the rate and not to a date.

## Reasoning

A point estimate is almost certain to miss: of a figure of 20, Cohn writes, "You have a very limited chance of being correct" (L3598). The chapter's epigraph names the trade being made: "It is better to be roughly right than precisely wrong" (L3588). This wiki reads what breaks as follows: a release date divided out of one velocity figure looks exact ([[deriving-duration-from-velocity]]), and the error only appears when the date is missed.

## How wide

The width follows the evidence.

| What the estimate rests on | How the range is made | Source |
|---|---|---|
| History from the same team on a stable product | Mean plus and minus a few points, or the best and worst iterations over the past two or three months; Chapter 21 uses three values from the last eight, on [[velocity-range-forecast]] | L3624, L4658-L4664 |
| History with any comparability doubt | Mean times 0.6 and 1.6; 15 becomes 9-24 | L3626-L3634 |
| One observed iteration | Same multipliers; 15 becomes 9-24 | L3655 |
| Three or more observed iterations | The range of observed values (12, 15, 16 gives 12-16), or the [[cone-of-uncertainty]] step for that count | L3657-L3659 |
| Forecast with no observation | Any technique; Cohn prefers 0.6 and 1.6, so 25 becomes 15-40 | L3732-L3736 |

The multipliers and their limits are on [[cone-of-uncertainty]]. Which row applies is decided by [[choosing-velocity-estimate-approach]].

## Sign of a violation

This sign is this wiki's. A plan, release date or commitment quotes one velocity figure, or a date with no spread around it. This raises a question rather than a verdict: check whether a range exists somewhere and was dropped on the way to the plan, and whether the single figure is a stated midpoint or the whole estimate.

## What later fact shows it wrong

Observed velocity keeps falling outside the stated range. The source gives no confidence level for its ranges: the actual figure will "probably" fall inside (L3672). This wiki reads a single miss as proving little, and repeated misses as meaning the width or the midpoint was wrong.

## Trade-off

A defensible range is uncomfortably wide. Cohn concedes that "This range may feel large, but given the likely uncertainty at this point it is probably appropriate" (L3643). The cost is a date expressed as a spread, which someone asking for one date will resist.

## Agent executor note

The transfer here is ours. The rule's mechanism is forecast uncertainty, not human pace, so the rule survives an agent executing and a person steering. The specific widths do not automatically transfer: they come from human project experience, and nothing in this source tests them on agent-executed work.

The chapter assumes iterations. A project set up without them has no iteration count to apply; see [[flow-metrics]] for what is measured instead.
