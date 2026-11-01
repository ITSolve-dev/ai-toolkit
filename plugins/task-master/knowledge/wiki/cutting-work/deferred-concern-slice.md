---
title: Deferred Concern Slice
category: cutting-work
summary: A task may be cut by leaving out a cross-cutting concern or a nonfunctional target, provided the first version says what it omits, the second version exists, and the first is not released alone.
tags: [rule, decomposition, splitting, nonfunctional]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Deferred Concern Slice

A deferred concern slice is a version of a task built without one of the qualities it will finally need: security, logging, error handling, or a performance or resource target. It is the one cut in [[story-splitting-patterns]] that deliberately produces something that should not ship alone. Cohn recommends it with that cost stated.

## The rule

Cut a concern away only if the first version says what it leaves out and a second task carries the concern. This wording is this wiki's, built from Cohn's two guidelines and his marking.

Cohn states the two forms separately:

> Consider removing cross-cutting concerns (such as security, logging, error handling, and so on) and creating two versions of the story: one with and one without support for the cross-cutting concern.
>
> — [[cohn-agile-estimating-planning]], L2665

> Considering splitting a large story by separating the functional and nonfunctional aspects into separate stories.
>
> — [[cohn-agile-estimating-planning]], L2671

Cohn also gives the marking: "The version would clearly note that it is not secure." (L2657). The nonfunctional form extends beyond speed, to a feature that "must consume less than a defined amount of memory, be drawn with fewer than a number of shapes, or use a critical resource for less than a defined amount of time" (L2673).

## When it applies

The concern has to be what makes the task too big. In the login example the password rules were small one by one: "None of this may be particularly time-consuming, but in aggregate it may make the story a little too big to fit in an iteration." (L2657). In the stock chart example, "caching would be a significant part of the effort" (L2669), so it became its own task in the next iteration.

This wiki reads the condition as a limit: a task that fits gets no such cut, since the cut exists only to reach a size. [[size-ceiling]] decides that.

## Observable signs

The signs are this wiki's reading of Cohn's marking and of his two-versions wording.

- **In task text:** a task's result omits a concern the request names, and the task does not say so.
- **On the board:** the first version is present and the second is not, so the omission is recorded nowhere that anyone will schedule.
- **In board history:** a release includes the first version while the second is still open. A sign raises a question, and the check is whether anyone decided that on purpose.

## Cost

Cohn is direct: "You probably would not choose to release the product with only the first story supported, but there may be value in splittng the stories in this way." (L2657). The search example shows how far the first version can go: "Their solution was to ignore this security restriction and in the first iteration on this feature users could see the entire result set." (L2653). That passage does not say whether this version ever reached real users, and this wiki reads it as acceptable only if it did not.

This wiki therefore reads the first version as possibly a [[vertical-slice]] and still not finished work. The Humanizing Work trap on pattern 8 of [[story-splitting-patterns]] is the same risk, and the same remedy applies: each half gets its own acceptance check, per [[testable-acceptance]]. A deferred concern is also a sequence between two tasks and not a wait, per [[sequence-versus-wait]].

The chapter does not discuss the cost of adding a concern later to code built without it. Its own citation points the other way, Kernighan and Plauger's "Make it work then make it faster." (L2669), and it is given second-hand with no measurement.

## Agent executor note

The evidence is Cohn's own projects, with no measurement. The rule survives an agent executing, and this wiki expects the marking to matter more with one: a person who built the insecure version remembers it, and an agent working the next task knows only what the task says, as [[recoverable-versus-task-only-facts]] sets out. The omission has to be written where the next executor will read it.
