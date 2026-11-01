---
title: Ideal-Day Estimate Decay
category: sizing
summary: Estimates in ideal days fall as the executor gets better, so equal work carries different numbers and velocity stays flat while output grows, which hides the improvement.
tags: [failure-mode, estimation, ideal-days, velocity]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ideal-Day Estimate Decay

An ideal-day estimate embeds how good the executor currently is, so it ages as that changes. "An estimate expressed in story points has a longer shelf life than an estimate in ideal days." ([[cohn-agile-estimating-planning]] L1564). The causes Cohn names are "the team’s experience with the technology, the domain, and themselves, among other factors" (L1564).

## What breaks

The first damage is to comparability: two pieces of work of exactly the same size carry different estimates (L1564). The second is that the measurement meant to catch this does not catch it. Cohn is direct: "We would like to think that measuring velocity over time would correct or account for this problem. It won’t. Instead, we’ll see a consistent velocity even though more work is being done." (L1566).

## The worked figures and their conditions

The figures belong to a constructed illustration, not a measurement. The setting is one programmer alone on the team, one-week iterations, and an environment where a calendar day equals an ideal day (L1566-L1572).

| | Estimate for one application | Applications finished in the iteration | Velocity |
|---|---|---|---|
| Learning the language | 5 ideal days | 1 | 5 |
| A few months later | 1 ideal day | 5 | 5 |

Five times the work produces the same velocity (L1572). This wiki notes the corollary, which is implied and not stated by Cohn: in story points the same application keeps its size, so velocity would rise and show the gain.

Cohn limits the weight of this: "For some projects, especially those adopting new technologies or on which the team is new to the domain, this can be a consideration." (L1574).

## Observable signs

These signs are this wiki's derivation, since Cohn gives the mechanism and no board sign. Each raises a question to check.

- In board history, comparable tasks carry falling ideal-day estimates over time.
- Velocity in ideal days is flat while the count of completed tasks of similar scope rises.
- A backlog holds estimates of different ages for like work. This wiki adds that such a backlog does not add up: old numbers overstate what remains if the executor has improved since.

## Discriminating criterion: did the work change, or the executor?

Re-estimate both units if the size of the effort changed, for example "based on the development of a framework" (L1576). Only ideal days need changing "when the team" gets better at something (L1576). This wiki's test before touching an estimate is whether the same work remains to be done. If it does, a story point stays put.

## With an agent executing

Cohn's mechanism is human learning. This wiki reads it as surviving in a changed form: an agent's capability does not grow gradually, but moves in steps when a model, the tooling or the context available to it changes. A day-denominated estimate is then stale across the whole backlog at once. A caveat that the source does not cover: if such a step helps some kinds of task more than others, relative sizes may shift too, and the claim that size is unaffected would need checking.

The remedy is the unit choice on [[story-points-or-ideal-days]]; the unit that avoids this is [[story-points]]. See also [[ideal-days]] and [[velocity]].
