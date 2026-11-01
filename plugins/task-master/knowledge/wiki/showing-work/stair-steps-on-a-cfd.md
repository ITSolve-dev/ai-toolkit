---
title: Stair Steps on a CFD
category: showing-work
summary: Stair steps on a CFD reveal a batch transfer, regular or not, and the batch is not a defect in itself but a prompt to weigh its effect on predictability.
tags: [concept, cfd, batch, cadence, predictability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Stair Steps on a CFD

Stair steps are the shape a batch transfer leaves on a [[cumulative-flow-diagram]]: "a flat period on a line (as discussed above) immediately followed by a jump up in arrival rate" ([[vacanti-actionable-agile-metrics]] L1834-L1840). Items that move together cross the line together, so the line waits and then rises at once.

## Examples with their settings

- Daily reporting interval, input column replenished every five days: "five straight days of a flat input line followed by an immediate increase when the column is replenished" (L1846).
- The bottom line represents a production deployment that happens every three months (L1846). Vacanti leaves the resulting shape as a question.

## Cadence is not required

Vacanti corrects a common attribution: "Any batch transfer—whether due to a regular cadence or not—will cause these stair steps to form." (L1848) The two cases differ in appearance:

- Regular cadence: "the stair steps will be of roughly uniform size and shape" (L1848).
- Nonregular batch: "a more uneven appearance to the steps" (L1848).

## A sign, not a defect

"batch in and of itself is not necessarily a bad thing" (L1856). Vacanti asks how the batch affects predictability, "positively or negatively", and then:

> Can those periods of batch be reduced? Eliminated? Should they be? What would it take to do that? What would the impact to Cycle Time be?
>
> — [[vacanti-actionable-agile-metrics]], L1856

## Per project setup

This section is this wiki's reading, not Vacanti's. On a setup with a fixed period, uniform steps are what the chosen cadence produces, so finding them is not a finding against the board, and the question left is whether the period suits the work. On any setup, uneven steps show a transfer that follows no stated rhythm, which is the more useful thing to check. A flat stretch with no following jump belongs to [[flat-lines-on-a-cfd]].

## With an agent executing

This wiki holds that the shape survives an agent executing, because it comes from when items cross a line and not from who does the work. Where a person replenishes the input or accepts finished work in sittings, the batch belongs to the person's rhythm, so that is where this wiki would look first.
