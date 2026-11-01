---
title: Story Points or Ideal Days
category: sizing
summary: Which unit to estimate in; Cohn prefers story points because they are a pure measure of size, and allows ideal days as a starting point or where an early velocity forecast is needed.
tags: [decision-rule, estimation, story-points, ideal-days, project-setup]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Story Points or Ideal Days

The choice of estimating unit decides whether a number states how much work there is or how long someone expects it to take. Cohn treats both as workable: "Each is a viable choice with advantages to recommend it." ([[cohn-agile-estimating-planning]] L1648). His own preference is settled: "My preference is for story points." (L1636).

## The considerations

In favour of [[story-points]] (L1538-L1546):

- They push an estimate to cover the whole of a task instead of a sum of parts; see [[summed-role-estimates]].
- They do not go stale as the executor improves; see [[ideal-day-estimate-decay]].
- They are a pure measure of size, so they are estimated by analogy and invite no comparison with the calendar; see [[ideal-days-compared-to-actual-days]].
- Estimating is usually faster. Cohn offers this as experience and gives a mechanism, not a magnitude: "when estimating in ideal days it is easier to think about the individual tasks necessary to develop a story, rather than thinking in terms of the size of the story relative to other stories." (L1596). The design discussion runs deeper as a result.
- They can be compared between people; see [[executor-bound-estimates]].

In favour of [[ideal-days]] (L1612-L1616):

- They are easy to explain outside the team, because of the intuitive reading "This is the amount of time it would take me if it’s all that I worked on." (L1622).
- They are easier at the start. A team on story points has no ready baseline and "has to find its own baseline by estimating a few stories" (L1626). Cohn bounds this cost: "Usually within an hour, many teams estimate in story points as naturally as if they’d been doing it for years." (L1628).
- They make an initial velocity prediction easier. This chapter only states the claim and defers the reasoning to the chapter on estimating velocity (L1632); see [[velocity]].

## How Cohn weighs them

Cohn discounts two of the three points for ideal days. Starting costs are short-lived, and of explaining the unit he writes: "we probably shouldn’t choose based on how hard it will be to explain to outsiders." (L1640). He also turns the intuitive feel against the unit, since it is what invites pressure on the number (L1640). The third point, the early velocity forecast, is not rebutted in his recommendation.

He allows one exception: "I usually only do this with a team that cannot accept that it is beneficial to separate estimates of size and duration." (L1642). The separation is the rule on [[size-versus-duration]].

## The rule, per setting

The resolution below is this wiki's own reading, built on Cohn's positions. He writes for a human team and does not address an agent.

| Input | Read from | Choice |
|---|---|---|
| Who executes | Project setup | An agent executing and a few people steering: relative size. An ideal day is anchored on a person's uninterrupted working day, and this wiki sees no such anchor for an agent. |
| Whether the executor's capability will shift during the project | Project setup: new technology, a domain new to the team, a change of model or tooling | A shift expected: relative size, because the estimates survive it. |
| Whether a duration forecast is required before any history exists | The request; board history showing no completed sized work | Required now: ideal days are the easier route per Cohn, with [[velocity]] as the place to work it out. |
| Whether the people involved can separate size from duration | How estimates are given and discussed in task text | They cannot yet: start in ideal days and shift, as below. |

Audience outside the team is deliberately not an input, following Cohn (L1640).

## What would show the choice wrong

These signs are this wiki's derivation from Cohn's mechanisms. Each raises a question rather than a verdict.

- Ideal days were chosen, and later: [[velocity]] stays flat while completed items multiply, comparable tasks get smaller numbers over time, or the numbers are argued against the calendar.
- Story points were chosen, and later: every point is routinely translated into a fixed number of days. The unit is then duration under another name, and its advantages over ideal days are gone.

## Moving from ideal days to points

Cohn's route is to change the question asked, not to announce a new unit: "How big is this one compared to the one we estimated five minutes ago?" (L1644). The aim is to move talk from how long the pieces take to relative size, and "Most teams hardly notice the gradual switch" (L1658). This wiki keeps that as a statement of what changes, not as a script for a meeting: an estimate phrased relative to an earlier task is a point estimate in practice, whatever it is called.

## Trade-offs

This wiki sums up the two sides. Choosing points costs a short period without a baseline, a unit that is harder to explain, and, per Cohn, a harder initial velocity forecast. Choosing ideal days costs everything listed on the linked failure pages.
