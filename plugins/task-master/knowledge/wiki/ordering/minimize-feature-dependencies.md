---
title: Minimize Dependencies Between Features
category: ordering
summary: Features are written to reduce technical dependencies between them, because each dependency takes away a product owner's freedom to order by value.
tags: [rule, dependencies, prioritization, sequence]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Minimize Dependencies Between Features

This rule says features should be written so that each can be chosen without first building others. The purpose is ordering freedom: dependencies decide the sequence that value should have decided. [[independent-tasks]] holds the test for independence and the moves for a dependency that cannot be removed. This page holds Cohn's reason, stated at the level of a release plan.

> In order for the product owner to have the most flexibility in prioritizing, features must be written so as to minimize the technical dependencies between them.
>
> — [[cohn-agile-estimating-planning]], L780

## What breaks when it is ignored

> It is difficult for a product owner to prioritize features into a release plan if the selection of one feature requires the prior development of three others.
>
> — [[cohn-agile-estimating-planning]], L780

This wiki reads the cost as falling on the ordering. A feature worth doing first may have to come fourth, and its predecessors enter the release on the strength of being prerequisites, not of being valuable.

This wiki reads the dependency meant here as a sequence between features, not a wait on something outside. It constrains order. Whether something is a wait inside a task is a separate test, on [[sequence-versus-wait]].

## The sign

The source's own example is the sign: a feature that cannot be selected without prior development of others. This wiki reads it in a task's text or the board's links as:

- An item with a chain of prerequisites that a person would not have asked for on their own.
- A high-order item that sits behind lower-order items only because of a "blocked by" link.
- Several items of which only the last has any user-visible result; see [[user-valued-features-over-tasks]].

## Limit of the rule

The source does not ask for zero: "A team is unlikely to achieve a goal of absolutely no dependencies; however, keeping dependencies at a minimum is often quite feasible." (L780). This wiki reads a sign here as asking whether a dependency could be cut by writing the feature differently, not whether it exists.

## Trade-offs

The source does not state a cost. This wiki notes that recutting features to remove a dependency can mean some duplicated or provisional work, which is worth paying only when the order would otherwise be forced against value.

## Agent executor note

This wiki reads the rule as surviving an agent executing, since it concerns the order of work and not who does it. It may matter more, since an agent can pick up items faster than a person and a forced sequence is then the main thing limiting order, but this has no source and is only a reading.

Related: [[fitting-stories-into-a-release]], [[planning-horizons]], [[lateness-passes-down-the-schedule]], [[ordering-by-value-and-urgency]].
