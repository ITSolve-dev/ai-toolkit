---
title: Executor-Bound Estimates
category: sizing
summary: A duration estimate is true only for the person who gave it, so two people can both be right, have no way to settle on one number, and the estimate fails when the work changes hands.
tags: [failure-mode, estimation, ideal-days, discriminating-criterion]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Executor-Bound Estimates

An estimate of time describes a pairing of work and worker, not the work alone. Cohn's section title states it: "My Ideal Days Are Not Your Ideal Days" ([[cohn-agile-estimating-planning]] L1598).

## The discriminating case: size against duration

Cohn's example is two runners at a trail, one fast and one slow. They can agree that it is one kilometre and about half the length of another trail, and these discussions are meaningful (L1600). If they discuss time instead, one says six minutes and the other at least ten: "Each would be right, of course" (L1602). The only way out is to agree always to talk in terms of one particular runner (L1602).

The criterion that separates the two is whether the disagreement can be settled. A dispute about size has something to settle it, namely the comparison with other work. A dispute about duration between two people of different speed has not: "they may each be right and they have no basis on which to argue and establish a single estimate." (L1650).

## What breaks

With ideal days the example becomes three days against five, and both may be right (L1604). Choosing the estimate of whoever is expected to do the work bets on the assignment holding: "by the time we actually do the work you may be too busy and I have to do it. And I’ll be late because it’s estimated at three days for you but will take me five." (L1604).

## When ignoring it is acceptable

"What most teams do is ignore the issue. This is acceptable if all developers are of approximately the same skill or if programmers always work in pairs, which helps balance out extreme differences in productivity." (L1606).

## Observable signs

These signs are this wiki's derivation. Each raises a question to check.

- Estimating comments give different numbers, each justified by how long that person would take.
- An estimate is recorded along with the name of the person it assumes.
- In board history, tasks that changed assignee overrun their estimates more often than those that did not.

## The remedy and its limit

Expressed in [[story-points]], the same people can converge: "Two developers of different skill or experience can agree on the size of something while disagreeing about how long it will take to do." (L1636). This wiki notes that the duration question has not gone away. It has moved to the point where size is converted to time through [[velocity]]. The choice is on [[story-points-or-ideal-days]], and who supplies an estimate is on [[who-estimates]].

## With an agent executing

This wiki reads Cohn's first condition as largely met when one agent does all the work, so the problem shrinks. It returns when the executor changes: a person taking over a task from an agent, or a different model or tool picking it up. A time estimate carried across that change has the failure above.
