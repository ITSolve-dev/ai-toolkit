---
title: Class of Service
category: moving-work
summary: A policy on the order in which committed work is pulled; it differs from a work item type, attaches only at commitment, differs from replenishment, and exists on any board with an order, declared or not. Vacanti treats it as a cost to predictability.
tags: [concept, class-of-service, pull-policy, flow-metrics, kanban]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Class of Service

A class of service (CoS) is a rule for what a freed-up executor picks next among work already committed to. Vacanti defines it this way:

> A Class of Service is a policy or set of policies around the order in which work items are pulled through a given process once those items are committed to (i.e., once those items are counted as Work In Progress).
>
> — [[vacanti-actionable-agile-metrics]], L3236

Vacanti widens the definition so that no board escapes it: "Any time that you put a policy in place (explicit or not!) around the order in which you pull something through a process, then you have introduced a Class of Service." (L3248). This wiki reads that as saying a board with no declared classes still has a pull order, and the only open question is whether anyone can state it. The names usually discussed are Expedite, Fixed Date, Standard and Intangible, which Vacanti calls "only four examples of limitless kinds" (L3248).

## What it is not

Vacanti separates the term from two neighbours, and this page keeps both as discriminating criteria.

- **Not a work item type.** Types are any segmentation of work: stories, defects, finance work, regulatory work, technical debt (L3246). Vacanti says "a Class of Service is different than a work item type" (L3240), and that many writers use the terms interchangeably. His stated preference, which he labels "just personal preference", is to make CoS a dimension of an existing type: "a work item of type user story has an expedited CoS" (L3246). This wiki reads that preference as an attribute marked on the task and not a column or a lane of its own ([[column-versus-attribute]]).
- **Not replenishment.** "The criteria for what items we pull next off the backlog are very different from the criteria around the order in which we pull those items once in progress." (L3258). What enters is settled on [[value-decided-at-replenishment]]. CoS covers only what happens after that.

## It attaches at commitment

"CoS does not attach until a work item has been pulled into the process." (L3250). Vacanti gives two reasons a discussion of classes on backlog items is wasted (L3250, L3256). There is no confidence a backlog item will ever be worked on. The forecast at the time of commitment may also show that the item needs no preference at all; the worked case is on [[when-to-use-class-of-service]].

## What it costs

Vacanti states the cost in two sentences. "The truth is that the only part of your process that is more predictable with CoS is the highest priority class." (L3476). "CoS represents an institutionalized violation of those assumptions." (L3464), where the assumptions are those of Little's Law: he names the fourth, and potentially the first and the third ([[littles-law-assumptions]]). He says the resulting unpredictability shows up, among other things, as [[flow-debt]] (L3476). The figures are on [[fifo-pull-order]] and [[standing-expedite-lane]].

## It exists because a resource is shared

The chapter's airport has one agent serving several queues. Vacanti's conclusion is that more agents remove the classes altogether: "If each queue had its own server, then there would be no need for CoS." (L3468). His remark on hiring is out of this wiki's scope, and the mechanism is not: a pull-order policy exists only where several queues compete for one executor.

## Observable signs

These signs are this wiki's derivation from the distinctions above. Each one raises a question and is not a finding ([[smell-is-not-a-finding]]).

- **In a task's text or labels:** items still in the backlog carry a class such as expedite or fixed date. Check whether the label is an order among committed work or only a rating, which belongs at replenishment.
- **On the board:** class names sit in the list of work types. Check whether the two questions, what kind of work this is and in what order it is pulled, have been merged.
- **In history:** items do not finish in commitment order, and nobody can state the rule that produced this. An undeclared CoS is in force. Tasks of very different size also finish out of order, so size is checked first.

## Agent executor note

The definition has no human in it, so it survives. The last section above changes shape, and the following is this wiki's reading, unmeasured. Parallel agent runs give each queue something close to its own server at execution, so pull order may matter little there. The server that stays shared is the person reviewing results, so the pull-order question moves to the review queue ([[wip-lengthens-cycle-time]]).
