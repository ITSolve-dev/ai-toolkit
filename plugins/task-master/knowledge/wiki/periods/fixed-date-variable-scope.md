---
title: Fixed Date, Variable Scope
category: periods
summary: Cohn's timed-race view of a project; the end date is known and what will be delivered by it is not, so planning means revising goals against the date.
tags: [decision-rule, iterations, planning-a-date, scope, commitment]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Fixed Date, Variable Scope

Fixed date, variable scope is the view that a project's end point is usually a date, not a known quantity of work, and that the plan's job is to find how much of the most valuable work fits before it. Cohn contrasts it with a project treated as a race of known length.

> An agile project is more like a timed race than a 10-kilometer race: run as far as possible in sixty minutes. In this way, the agile project team knows when it will finish, but not what they will deliver.
>
> — [[cohn-agile-estimating-planning]], L816

Cohn qualifies the claim. He says "we often know we need to get to it or as close as we can by a known date" (L816), which is often, not always.

## Why the finish line is treated as unknown

Cohn's grounds are that "the end result is both somewhat unknown as well as unknowable in advance", so "planning becomes a process of setting and revising goals that lead to a longer term objective." (L816). This wiki reads a plan that assumes a known finish line as assuming exactly the complete knowledge that [[replanning-on-new-knowledge]] says a project does not have.

## Applying it

This wiki reads the rule as a choice with these inputs.

- The date: read from the release's [[conditions-of-satisfaction]].
- The ordered list of features: read from the board's order ([[order-by-value-not-convenience]]).
- The rate of progress: read from history of completed work in past iterations.

The output is an expected cut line in the ordered list, stated as an expectation and not a promise ([[estimate-versus-commitment]]).

Later fact that would show the choice wrong: the date arrives and the work finished lies below work left undone in the order, or the date is moved to fit the scope, which reveals that the scope was the fixed thing all along.

## When it does not hold

Cohn allows the opposite preference in the same chapter: a product owner may trade a month for more stories (L857). When the conditions of satisfaction fix the content and let the date move, this wiki reads the timed race as the wrong model, and the plan states a date range from the rate of progress instead ([[estimates-as-ranges]]). Cohn does not spell out this case here; the reading is this wiki's.

If date, scope and quality all stay fixed and no plan satisfies them, Cohn's answer is that "the conditions of satisfaction must change." (L859).

## Trade-offs

This wiki notes that fixing the date gives up a promise about content. Anyone needing a specific feature by that date gets a likelihood, shaped by the feature's place in the order. The order then carries the weight of the commitment, since what is at the top is what ships. A date that holds while scope gives is also the shape of a period on [[commitment-over-a-period]].

## Agent executor note

This wiki reads the rule as surviving an agent executing. The mechanism is uncertainty in the work, not human pace, although the rate of progress must come from agent-executed history and not from an earlier human team's.

Related: [[timeboxed-iteration]], [[release-versus-iteration]], [[planning-horizons]], [[changing-the-plan-without-changing-the-date]].
