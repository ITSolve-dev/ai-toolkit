---
title: Flat Lines on a CFD
category: showing-work
summary: A CFD line that stays horizontal for a long period means zero arrivals or, more often the concern, zero departures, and calls for asking at once why nothing is moving.
tags: [failure-mode, cfd, throughput, predictability, blocked-work]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Flat Lines on a CFD

A flat line on a [[cumulative-flow-diagram]] is a stretch over which a cumulative line does not rise, meaning no item crossed that boundary during the stretch. Because the lines are cumulative, "lines can never go down" ([[vacanti-actionable-agile-metrics]] L1814), so flat is the lowest reading they can give. This wiki treats a line that does go down as a defect in the chart or its data and not as a process shape; see [[malformed-cfd]].

## Sign

"any lines that flatten out over long periods of time" (L1814). Vacanti gives no length for "long". In a board history, this wiki reads it as no item crossing a state boundary across the stretch.

## Which line is flat

Vacanti says such lines can represent "either periods of zero arrivals or periods of zero departures", and that the usual concern is departures (L1824): "zero departures means nothing is getting done", so "no value is being delivered to the customer (or to a downstream step)" (L1824).

This wiki's reading of the parenthesis is that an inner line can show this too. An inner flat line means a step has stopped passing work on, even if the bottom line is still moving for a while on what is already past that step. All lines flat together means nothing moved anywhere.

## What breaks

Vacanti leaves the effect as questions: what happens to the Approximate Average Cycle Time drawn as a horizontal line, and what happens when zero Throughput is put into Little's Law while WIP is nonzero (L1828). This wiki's answer is that the horizontal distance grows for every item in progress during the stretch, and that WIP divided by a Throughput of zero has no finite value, so [[littles-law]] stops giving a usable Cycle Time for that period.

## What to ask

Vacanti says "an emergent flat line on a CFD should trigger some type of urgent conversation" and names two questions (L1830):

- "Why isn't anything getting done?"
- "What can we do to get things flowing again?"

This wiki keeps these as the finding's content. Running the conversation is out of scope.

## Causes the source names

- Holidays with most staff away, such as "the two weeks around Christmas and New Year's in the U.S." (L1826).
- An external block, such as "the whole test environment being down such that testing cannot complete" (L1826).

The source lists these as examples, not as a complete set: "There are all kinds of circumstances that could cause this pattern to emerge" (L1826).

## What separates it from stair steps

A flat stretch followed immediately by a jump is a batch transfer, not a stop: see [[stair-steps-on-a-cfd]] (L1834-L1840). This wiki's test is to look at what comes after. A jump that clears the accumulated work points to a batch, and a return to the old slope with nothing made up points to a real stop.

## With an agent executing

This wiki reads the external block as surviving unchanged. The holiday cause survives only in altered form: an agent does not take leave, but a person it waits on does, so a flat line may mark the person's absence and not the executor's.
