---
title: Ordering for Early User Feedback
category: ordering
summary: Move forward the features that let real or likely users react, including those with significant user-facing parts, because this best reduces the risk of building the wrong product; it applies only if someone can react, and does not mean building the interface alone.
tags: [rule, ordering, prioritization, risk, learning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ordering for Early User Feedback

This rule moves earlier the work that lets users respond to something real. Cohn ([[cohn-agile-estimating-planning]]) calls the risk it answers "the most serious risk facing most projects: the risk of developing the wrong product" (L1855).

## The rule

> This risk can be dramatically reduced by developing early those features that will best allow us to get working software in front of or in the hands of actual users.
>
> — [[cohn-agile-estimating-planning]], L1777

Cohn applies the four [[prioritization-factors]] to user interface work to show it (L1851-L1859).

- **New knowledge:** yes. Building the main components or the navigational model lets the system be shown "to real or likely users in an early form" (L1853), and the reactions become product knowledge.
- **Risk:** it "probably doesn’t eliminate technical risk" unless this kind of interface is new to the team, but it reduces the risk of the wrong product (L1855).
- **Cost:** doing it early is not usually cheaper: "In most cases, this is not the case." (L1857).

So the case rests on learning and risk, not on cost. Cohn's conclusion is to move earlier "those themes that will allow users to provide the most feedback on the usability and functionality of the system" (L1859).

## What it does not mean

> This does not mean that we would work on the user interface in isolation or separate from the functionality that exists beneath the user interface.
>
> — [[cohn-agile-estimating-planning]], L1859

This wiki reads this as the same requirement as a [[vertical-slice]]: what is shown must work. A separate interface task with nothing behind it fails the rule, and the sign is a task that delivers screens and no behaviour ([[component-task-masquerading]]).

## Two positions and when each holds

Cohn sets out a disagreement: common advice does interface design entirely within the iteration of the underlying feature, while others argue that usability improves if designers consider the whole interface upfront (L1851). He resolves it by moving forward the features that carry significant interface and gain the most feedback. He does not choose whole-interface design as a task of its own.

This wiki's reading by setting is as follows. If a person or group can react soon, follow the rule above. If the overall structure of the interface is itself the open question, the first feature shown should be the one that exercises that structure, which is what Cohn means by "the navigational model" (L1853).

## Sign

The signs are this wiki's, and each raises a question. A long run of history in which every finished task is internal and nothing was presented to anyone. Or a project whose open questions about what to build stay open while the tasks that could settle them sit low.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who can react to the result, and how soon | The person steering |
| Which open questions are about what to build | [[end-and-means-uncertainty]], the tasks' open questions |
| Which item would expose the most to reaction | The tasks' descriptions of what users see |

The move was wrong if the result was shown and nothing changed afterwards: no new, changed or dropped tasks came of it. The test is this wiki's. It means either that the uncertainty was smaller than assumed or that the wrong people saw it.

## Conditions and cost

This wiki notes that the rule requires someone who can react. Where no user is reachable, the feedback does not arrive, and the early move buys nothing this source can name. With a few people, the only reader may be the person steering, whose reaction tests the result less well than a user's would. Early user-facing work may also be redone as reactions come in, and that rework is the price of the knowledge ([[cost-now-versus-cost-later]]).

## Agent executor note

This wiki reads the rule as surviving whole, because the uncertainty lives with users and not with the executor ([[end-and-means-uncertainty]]). It may matter more with an agent, since this wiki expects an agent to build the wrong thing as readily as the right one. That expectation is ours and the source does not test it. See also [[iterating-reduces-uncertainty]].
