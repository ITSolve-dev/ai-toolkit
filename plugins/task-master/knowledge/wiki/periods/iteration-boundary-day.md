---
title: Iteration Boundary Day
category: periods
summary: Where an iteration starts in the week is a choice; Cohn's example team moved to Friday-to-Thursday so a Friday release had the quiet weekend as a buffer, with Friday morning absorbing leftovers.
tags: [decision-rule, iterations, cadence, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Iteration Boundary Day

The weekday on which an iteration begins is a setting that many teams never examine. Cohn's teams routinely ran Monday to Friday, until one case changed his mind ([[cohn-agile-estimating-planning]] L3081).

## The case

The team ran a website busy on weekdays and barely used on weekends. "The most logical night for this team to deploy new web updates was Friday evening." (L3083), because something going wrong over a quiet weekend had minimal impact. They ran two-week iterations from Friday to Thursday. Friday held the review and the next plan, and the iteration started in earnest on Monday (L3083). Friday morning also occasionally served as slack for last-minute work, which was preferable to working the weekend (L3085). Cohn stresses that the team did not make a habit of it.

This is one team's anecdote. The website pattern is its condition, and it does not show that a Friday boundary is better in general.

## The decision

This generalization is this wiki's. Place the boundary so that the period's end leaves a low-risk window for whatever release follows it. The opposite case, a boundary that sits against a date where value steps down, is on [[quarter-end-release-date]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| When use of the product is lowest | Usage pattern of the product, or the people steering |
| When a release can be watched and fixed | The availability of the people steering |
| Whether releases follow the period at all | Project configuration |

The choice was wrong if releases made at the boundary still fall in busy hours, or if fixes after a release need someone present when no one is.

## Trade-off

A boundary tied to releases can invite treating the period's end as a release gate, which [[commitment-over-a-period]] warns against. Where releases are independent of periods, the inputs above do not apply and the boundary is free to be set by when the people steering can review.

## Agent executor note

A quiet weekend matters for risk regardless of who executes, but the boundary's human benefits, such as avoiding a Monday of meetings (L3083), do not transfer. This wiki reads the buffer as only as good as a person's availability to respond, since an agent that deploys still leaves a person answerable.
