---
title: Unit of Work
category: cutting-work
summary: What this wiki means by a task, how that maps onto the sources' words "story" and "task", and the two working tests a unit has to pass.
tags: [concept, decomposition, vocabulary]
sources: [wake-invest, humanizing-work-splitting, radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-01
---

# Unit of Work

A unit of work is the thing this wiki calls a **task**: the piece that goes on a board, is taken by one executor, and comes back as one result. The sources do not use the word that way, so every page in this wiki that reports a source keeps the source's word and every page that prescribes uses "task" in this sense.

## Vocabulary

| This wiki | Wake | Humanizing Work | What it is |
|---|---|---|---|
| task, unit of work | story | story, vertical slice | The unit that carries a result someone other than the implementer can look at |
| (not produced) | task | task, component | A piece of a story, made for the implementer's benefit, or an item with no observable result of its own |

The Humanizing Work authors define their unit by what it changes: a user story is "*a description of a change in system behavior from the perspective of a user*" (L53). Their use of "task" is pejorative where Wake's is neutral, which is why the two sources should not be merged by word: for Wake a task is a legitimate piece of a story, and for the authors a task "pretending to be a story" is a defect ([[component-task-masquerading]]).

Wake separates the two levels plainly:

> Stories are broken into tasks for the benefit of developers, but a customer should still be able to expect that every task can be explained and justified.
>
> — [[wake-invest]], L110

This wiki reads the first half as a boundary on the plugin. Expanding a task into step-by-step instructions is outside the charter, so the plugin stops at the level Wake calls a story. Wake's task-level criteria are kept only where they transfer to that level, and each page that uses one says so.

## The working tests

The charter states two tests for a unit: once started, the task can be finished without waiting, and its result is presented once. These tests are the charter's own, written before any source was ingested. No source in this wiki states them in those words, so a page citing them cites the charter and not a source.

The second test has a close source statement in the Humanizing Work definition of a slice: "When you call the slice “done,” the system is observably more valuable to a user." (L133). This wiki reads a result that can be presented as a result of that kind. See [[vertical-slice]].

The first test has no source statement. This wiki reads board history as its evidence: a task that reached a parked or blocked state after starting did not meet it ([[sequence-versus-wait]], with the states defined on [[waiting-versus-blocked]]). A stop for a decision from the person steering counts too, which makes [[conversation-moves-into-the-task]] part of the same test.

## A task that fails

- It has no result of its own: combine it, per [[component-task-masquerading]].
- It is too big: cut it, per [[size-ceiling]] and [[story-splitting-patterns]].
- It is too unknown to cut: see [[spike-as-last-resort]] and [[how-far-to-split-up-front]].
- It contains a known wait: cut at the wait, per [[sequence-versus-wait]].
