---
title: Overrun Triggers a Recut
category: sizing
summary: A task running past the expectation set for its size is a signal to act on the task itself, not to wait longer.
tags: [rule, estimation, smart, board-history]
sources: [wake-invest, ambig-swe]
created: 2026-11-01
updated: 2026-11-01
---

# Overrun Triggers a Recut

A task carries an expectation of how long it should live, and passing that expectation forces a decision about the task. This is the part of Wake's "Time-boxed" criterion that transfers from his sub-story tasks to this wiki's unit ([[unit-of-work]]).

> A task should be *time-boxed*: limited to a specific duration. This doesn’t need to be a formal estimate in hours or days, but there should be an expectation so people know when they should seek help. If a task is harder than expected, the team needs to know it must split the task, change players, or do something to help the task (and story) get done.
>
> — [[wake-invest]], L114

This wiki keeps "split the task" and drops "change players", since assigning people is outside the charter.

## The rule

When a task in an active state outlives the expectation for its size, recut it, unblock it, or say why it stays as it is. Leaving it to run on is the violation.

## Sign of violation

Board history shows a task in an active state for longer than tasks of its size step usually take, with no split, no state change and no recorded reason in that time. The sign is read from board history and needs no logged hours, because the charter reads time a task lived from history and leaves hour tracking out.

## Why

What breaks if ignored is the signal itself. An overrunning task is the first evidence that it was cut or described wrongly, and that evidence loses its value once the task quietly finishes late.

## Cost

Following the rule interrupts some tasks that were nearly done. The rule accepts that cost in exchange for not discovering a wrong cut at the end.

## Agent executor note

Wake's mechanism is a person who notices the expectation has passed and seeks help. That part rests on a human executor. An agent has no such habit unless it is given one, so this wiki moves the check to the board and to the person steering, who reads age from history. The expectation itself survives; the self-report does not.

An agent's overrun may also mean something different from a person's. The Ambig-SWE footnote on Claude Sonnet 4 in the Hidden setting reports:

> The model compensates for the lack of information with increased exploration and solution attempts leading to substantially higher evaluation costs.
>
> — [[ambig-swe]], L155

The authors repeat the point at L159: Claude Sonnet 4 "extensively explores the codebase and attempts multiple solutions to overcome the lack of information". This wiki reads that as a second diagnosis for an overrun: with an agent, a task running long may be an [[underspecified-task]] and not a big one. The evidence is one model on stripped issues, and it concerns cost and not age on a board, so the reading is a hypothesis to check first when an overrun appears. It does not establish the cause. The response is then to fix the task text and not to split it.
