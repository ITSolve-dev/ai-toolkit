---
title: Fix the model, not the offset
category: debugging
summary: "A literal +1 or -1 applied to a value received from elsewhere with no named reason, often paired with an opposite adjustment in another function."
tags: [rule, root-cause, compensation, time]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

When a result comes out wrong by a small constant, adding that constant makes the symptom vanish and leaves its cause in place. The book treats this as the lack-of-precision form of [[programming-by-coincidence]]: the constant error is itself a coincidence, sitting on top of a deeper flaw. It is the numeric case of [[fix-the-root-cause]].

## Rule

This wiki draws the rule from the book's story: find out why a value is off before changing it, and do not compensate with an adjustment whose meaning you cannot state.

The book's case is a large project reading data from devices spread across states and time zones, each set to local time (p. 248). Conflicting time-zone interpretation and daylight-saving rules left results wrong, nearly always by one. The developers added or subtracted one to get the right answer, and the next function would notice the value had moved the other way and move it back. Without a proper model of time, the code base became «совершенно непригодную массу операторов +1 и -1» (p. 248). None of them turned out right, and the project was scrapped (p. 248).

This wiki's reasoning is that a compensation encodes a guess about one situation. A second function that compensates for the first now depends on it, so neither can be corrected alone.

## Sign in code

- A literal adjustment such as `+ 1`, `- 1` or a fixed number of hours applied to a value straight after it arrives from another function or source, with no name or comment giving its meaning.
- An opposite adjustment to the same quantity in another function.
- A conditional correction: if the value looks too high, subtract.
- One quantity handled in different representations across functions, such as local time in one and universal time in another, with nothing in the names or types saying which.

This wiki assigns the two neighbouring shapes by what the code does to the value. This page owns a number that is corrected and passed on. A guard that absorbs the value by returning, defaulting or catching belongs to [[fix-the-root-cause]]. A guard a fix adds at the failing line, absorbing the value by returning, defaulting or catching, and a single input-keyed correction of a computed result added by a fix, are [[fix-the-root-cause]]. Two or more input-keyed corrections accreted in one method on its own computed result are [[rewrite-a-method-you-do-not-understand]].

## When not to apply

- The offset has a stated meaning and lives at one boundary, such as converting a one-based external index to a zero-based internal one. That conversion is part of the model.
- A constant comes from the domain itself, under a name that says so.

## Repair

1. Name the quantity and fix one internal representation for it. For time the book's footnote gives the veteran's advice to use UTC (p. 248).
2. Convert once, at the point where the value enters the system.
3. Delete every compensation, in pairs, checking after each pair.
4. If the cause is still unknown, leave the failure visible and investigate it. An adjustment hides the evidence.

## Before and after

```
// before
function readingHour(device):
    return device.localHour() + 1

function reportHour(reading):
    return readingHour(reading.device) - 1
```

```
// after: one representation, converted at the edge
function readingTime(device):
    return toUtc(device.localTime(), device.zone)

function reportHour(reading):
    return hourOf(readingTime(reading.device))
```

## Source

[[pragmatic-programmer]], Topic 38, p. 248, for the case and the UTC footnote. The quotation follows the page image, because the extracted text adds a space after the plus. The statement of the rule, the reasoning about paired compensations, the signs and their assignment against [[fix-the-root-cause]], the limits, repair steps 2-4 and the example are this wiki's own.
