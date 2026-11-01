---
title: Tests Specified Before Start
category: moving-work
summary: Cohn holds most cards out of In Process until a story's high-level acceptance tests are specified. It is a soft gate for people and a firmer one for an agent, which guesses at what it is not told.
tags: [rule, readiness, acceptance-criteria, iterations]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Tests Specified Before Start

This rule puts a readiness gate on the move into active work: what a task will be judged against is written down first. On Cohn's board the gate is a column of checkmarks.

> I have teams put a big checkmark in the Tests Ready column when they have specified the high level tests for a story. Further, I encourage teams not to move many cards to the fourth column, In Process, unless the tests are specified.
>
> — [[cohn-agile-estimating-planning]], L4482

Cohn keeps the gate soft in three ways. His verb is "encourage", the limit falls on "many cards" and not on every card, and he allows that the column is optional: "You may not need a Tests Specified column but it’s a useful, visible reminder to a team that is trying to become accustomed to specifying acceptance tests before coding a feature." (L4482). His gate is on the story, which is this wiki's task ([[unit-of-work]]), so it transfers without a change of level.

## The rule

A task enters an active state only with its acceptance tests specified. A few exploratory starts are tolerated by Cohn. This wiki allows that for people and not for an agent, as the note below explains.

## Sign of violation

- **In a task's text:** no checkable acceptance criteria ([[testable-acceptance]]). This rule is about task content, so the omission is the sign.
- **In board state:** an active task whose acceptance section is empty, or whose readiness marker is unset.
- **In board history:** acceptance criteria first added after the task moved to active.

These signs are this wiki's.

## Why

Cohn's reason is what the programmer gets: "they can refer to specific examples of how each function and business rule is expected to work" (L4480). The gate also costs little where planning already did the work: if the conditions of satisfaction were identified at iteration planning, this "is easy as the conditions of satisfactions are essentially a user story’s high-level acceptance tests" (L4476). See [[conditions-of-satisfaction]].

## Cost

Work that could start waits for a specification. That cost falls on planning, and Cohn's tolerance of a few cards is the concession to it.

## Column or marker

Cohn's own use is a marker: a checkmark on a row, and no cards pass through the column ([[iteration-task-board]]). This wiki reads that as a case for [[column-versus-attribute]]: readiness belongs on the task, and a board does not need a column for it. Cohn offers the column as a training aid, which fits, because he expects a team to outgrow it.

## Agent executor note

Cohn's mechanism is a habit forming in a team, and that part does not transfer. This wiki reads the rule as stronger for an agent: a person lacking a test can ask or recall, and an agent proceeds on a guess ([[agent-silence-is-not-completeness]], [[underspecified-task]]). So the tolerance of a few untested starts is dropped there, and the gate is firm. Cohn does not say this, and nothing in his chapter tests it.
