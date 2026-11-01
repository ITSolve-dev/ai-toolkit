---
title: Potentially Shippable Increment
category: periods
summary: Each iteration ends with features coded, tested and of releasable quality; the test is whether the team could ship, not whether it did.
tags: [rule, iterations, done, quality, failure]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Potentially Shippable Increment

A potentially shippable increment is the state a product must reach at the end of every iteration: what was added is finished to release quality, whether or not anyone chooses to release it. Cohn treats this as more crucial than iteration length ([[cohn-agile-estimating-planning]] L768).

> It is essential that the product be brought to this potentially shippable state by the end of each iteration.
>
> — [[cohn-agile-estimating-planning]], L770

Cohn's required grain is the feature: "each added feature is coded, tested, and of releaseable quality." (L768).

This wiki reads this as Cohn's form of the shared standard the Scrum Guide calls the Definition of Done ([[started-and-finished-points]]). It is the condition under which a task counts as finished in a period, and a task that misses it goes through [[unfinished-at-period-end]].

## What separates shippable from shipped

The discriminating criterion is capability, not the act. Cohn says many teams do not deliver every iteration to users, and "the goal is simply that they could." (L768). The requirement also does "not mean a team must do absolutely everything necessary to release since they often won’t release each iteration" (L770).

## The exception and its conditions

Cohn's single case is a product of hardware and software that needs two months of mean-time-between-failure testing before release. The team cannot shorten it, because it is "contractually required by their client" and often necessary to find hardware failures, and the team works in four-week iterations (L770). His claim is that "from running this two-month MTBF test, their product is at a truly releasable state at the end of each iteration." (L774).

This wiki reads the conditions as what make the exception valid: the excluded activity is named, forced from outside, and longer than an iteration. "We will test at the end" meets none of them.

## Failure: half-finished work passed on

Cohn's form of this failure is "coders do not throw half-tested code over a wall to testers" (L746), stated as what must not happen.

Cohn gives no observable sign. This wiki reads the following as questions to ask.

- A feature counted as finished while a separate item for its testing stays open or arrives later. [[activity-based-plan]] has the same "Test" item as a planning fault.
- A run of iterations whose finished features cannot be shown working, or a hardening stretch before a release that the plan did not name as an exception.

## Trade-offs

This wiki notes that finishing to this bar means fewer features per iteration than finishing to "coded". In return, Cohn gets a working product that can be shown to users each iteration, which is where early feedback comes from (L718).

## Agent executor note

This wiki reads the rule as surviving an agent executing: it is a statement about the state of the product, not about who produced it. The "wall" does not disappear, however: this wiki reads its remaining place as between an agent's result and the person reviewing it, so what the agent presents should already be tested, not sent on to be tested.

Related: [[timeboxed-iteration]], [[conditions-of-satisfaction]], [[user-valued-features-over-tasks]], [[release-versus-iteration]].
