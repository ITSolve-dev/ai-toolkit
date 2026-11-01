---
title: Plan Deliberately Overstated
category: periods
summary: Dates or scope known to be unrealistic are stated so that a partial result looks acceptable; the plan stops being a forecast, and comparing it with fact shows nothing.
tags: [failure-mode, commitment, estimation, plan-versus-fact]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Plan Deliberately Overstated

A plan is deliberately overstated when someone states more work, or an earlier date, than they expect, in the hope of getting a fixed share of it. Cohn gives both forms and one anecdote.

## The source's cases

- A product owner gives developers "artificial dates" ([[cohn-agile-estimating-planning]] L4581).
- Developers "give estimates that the product owner knows are unrealistic" (L4581).
- One team reported that "their executives ask for more work than can reasonably be expected because “that way if they get 80%, they’re happy.”" (L4581)

The 80% is that team's account of its executives' reasoning. It is an anecdote from one team, not a measured figure.

## What breaks

Cohn's mechanism is trust: once a false figure is discovered, trust goes, and information stops flowing. A developer who knows a task will take far longer must feel safe saying so, or "problems such as this will remain hidden longer" (L4583).

This wiki reads a second break that needs no social mechanism. A plan nobody believes cannot be compared with fact, so the difference between them says nothing and [[iteration-summary-plan-versus-fact]] loses its use.

## Observable signs

Cohn gives no sign. The ones below are this wiki's, and each raises a question to check, not a verdict; see [[smell-is-not-a-finding]].

- Planned points sit above the top of the [[velocity-range-forecast]] period after period.
- Planned and earned points keep a stable ratio, as if the gap were expected.
- A date is held although no value in the range reaches it.

A single overfull iteration is not this defect. An honest plan misses too, and the sign is the repetition.

## Agent executor note

Trust between people is a management concern outside this wiki's scope, so that mechanism is recorded only as Cohn's reasoning. In a setting of a few people steering an agent, this wiki reads the defect as surviving in reduced form: nobody is pressured, but a person can still fill a period past what history supports, and the agent will not object on its own. The cost that remains is the loss of plan-versus-fact.

See also [[filling-a-period]], [[commitment-over-a-period]], [[priority-inflation]].
