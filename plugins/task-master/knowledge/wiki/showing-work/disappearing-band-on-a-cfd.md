---
title: Disappearing Band on a CFD
category: showing-work
summary: A band that vanishes from a CFD has three candidate causes, a too-coarse reporting interval, a starved step or a skipped step, and they mean different things.
tags: [decision-rule, cfd, reporting-interval, workflow, variability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Disappearing Band on a CFD

A disappearing band is a workflow step whose band on a [[cumulative-flow-diagram]] thins out to nothing. Vacanti says such bands "could be telling us one of several things" ([[vacanti-actionable-agile-metrics]] L1884), and names three. The chart alone does not separate them.

## The three causes

| Cause | Source's account | Test (this wiki's) |
|---|---|---|
| Reporting interval too coarse | "the reporting interval that we have chosen is too big" (L1884). With weekly reporting and a Test column passing work in a day or two, any given reporting point will likely show zero WIP there, so the band does not appear (L1884). | Item history shows entries into the state, but each lasted less than one interval. Redrawing at a finer interval brings the band back. |
| Downstream starvation | "some upstream variability in our process is causing downstream steps to be starved" (L1890). | No items entered the state during the gap, and earlier steps show uneven delivery. Work resumes through the step later. |
| Skipped step | "the team frequently decides to skip a certain step in the workflow altogether" (L1892). Vacanti's deliberately exaggerated example is a team near the end of a release skipping Test and pushing work from Development straight to production (L1892-L1898). | Items reached later states with no entry into this one in their history. |

This wiki reads the first cause as a defect of the chart and the other two as facts about the process.

## Good or bad

For the skipped step, Vacanti does not rule: "It would be up to you to decide given your particular context whether this is good or bad." (L1898)

This wiki adds what would show a reading wrong. A chart redrawn at a finer interval that still has no band rules out the first cause, and a history showing every item passed through the state rules out the third.

## With an agent executing

The transfer here is ours. An agent can pass through a step in far less time than a person would, so the coarse-interval cause is likely to be more common on such a board, and a state that has become too quick to show may no longer be a step worth drawing. A skipped step keeps its meaning, with the added question of who decided to skip it, the person or the agent.
