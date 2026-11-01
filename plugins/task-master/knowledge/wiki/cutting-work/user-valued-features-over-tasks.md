---
title: User-Valued Features Over Isolated Tasks
category: cutting-work
summary: Work is completed and delivered as features a user values, not as isolated tasks that only combine into value later.
tags: [rule, decomposition, vertical-slice, value]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# User-Valued Features Over Isolated Tasks

This rule says the unit of completion that counts is a feature a user or customer would value, not a piece of work that has meaning only once combined with others.

> agile teams focus on completing and delivering user-valued features rather than on completing isolated tasks
>
> — [[cohn-agile-estimating-planning]], L782

Cohn lists this as the second of two ways a team shows commitment to business priorities (L780-L782), and calls user stories "One of the best ways to do this" (L782); see [[user-story]]. He gives no separate reason. This wiki reads one from the same passage: order is set on features by what they return (L780), so a piece with no value of its own cannot be ordered on that basis, and finishing it delivers nothing to compare.

## A note on terms

Cohn's "task" is not this plugin's unit of work. In his iteration planning, tasks are the pieces "needed to transform a feature request into working and tested software." (L839). This wiki reads the plugin's unit, finished without waiting and presented once, as closer to his feature than to his task ([[unit-of-work]]). Pieces smaller than that are the executor's business and do not belong on the board as separate results. The "finished without waiting" test has no source; it comes from the plugin's design.

## Signs to check

The source gives none. This wiki reads the following as questions to ask of a task's text or a board.

- Items titled by a technical layer or an activity, such as "add table" or "write endpoint", with nothing a user could notice. The same sign at the level of a whole plan is on [[activity-based-plan]], and at the level of one item on [[component-task-masquerading]].
- Several items closed and no change visible to anyone until a later one closes.
- A story's "so that" clause that restates the capability, or names only a technical benefit.

A technical item is not automatically a defect: the sign raises a question about whether it should be folded into the feature that needs it, which is the [[vertical-slice]] remedy.

## Trade-offs

The source does not state one. This wiki notes the likely one: cutting by user-visible result can make a single item touch several layers and grow, which then has to be checked against [[size-ceiling]].

## Relation to dependencies

This wiki notes that pieces with no value of their own usually come with an order among them, which is the shape [[minimize-feature-dependencies]] warns about. Fixing one tends to help the other.

## Agent executor note

The rule concerns what a receiver gets and does not depend on who executes, so this wiki reads it as surviving. An agent will carry out a technical item as readily as a feature, so nothing on the executor's side pushes back on a bad cut, and the check has to happen before a task reaches it.

Related: [[user-story]], [[potentially-shippable-increment]], [[order-by-value-not-convenience]].
