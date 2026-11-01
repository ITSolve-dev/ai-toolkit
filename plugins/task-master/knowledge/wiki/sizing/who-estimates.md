---
title: Who Estimates
category: sizing
summary: Estimates come from the group that may do the work and not from a single expert, because the executor is not known in advance and others catch what the expert forgets; with an agent executor the first reason goes and the second is what survives.
tags: [rule, estimation, shared-estimate]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Who Estimates

Cohn's position is that an estimate is shared: "Agile teams do not rely on a single expert to estimate." ([[cohn-agile-estimating-planning]] L1212). This rule chooses who supplies an estimate. Applied to a person steering an agent, its reasons do not transfer evenly, and that is the part that matters here.

## The rule

> Despite well-known evidence that estimates prepared by those who will do the work are better than estimates prepared by anyone else (Lederer 1992), estimates are best derived collaboratively by the team, which includes those who will do the work.
>
> — [[cohn-agile-estimating-planning]], L1212

This wiki notes that the sentence concedes the evidence and then overrides it for two reasons of Cohn's. The later citation points the same way: Jørgensen is quoted as concluding that "the people most competent in solving the task should estimate it." (L1362). This wiki has read neither study. The Scrum Guide's position on who sizes is on [[filling-a-period]].

## The two reasons

**The executor is not known yet.** A specialist may be busy when the time comes. "So, since anyone may work on anything, it is important that everyone have input into the estimate." (L1214).

**Others catch what the estimator forgets.** Someone who could not do the work may still recall how it went: "Kristy, you’re nuts; the last time you worked on a feature like that it took a lot longer. I think you’re forgetting how hard it was last time." (L1216). Cohn's report of the outcome is his experience and not a measurement: "However, more often than not in my experience, she will acknowledge that she was indeed underestimating the feature." (L1216).

## Who counts

- All disciplines that touch the work. Cohn's "developers" covers programmers, testers, database engineers, analysts and designers (L1312).
- Not the person who wants the work: "The product owner participates in planning poker but does not estimate." (L1312). The chapter gives no reason. The role is kept for answering questions (L1316).
- At least two people. Even when estimating in spare moments Cohn says: "I’d prefer that when someone has a few spare minutes to devote to estimating that he find at least one other person and that they estimate jointly." (L1356). For sub-groups of a larger team he asks for "at least three estimators" per group (L1344), a condition of a scale this wiki does not address.

## Failure sign

A task whose estimate was set by one person, or by the requester, with no other input. Board history may show who set the field. It will not show a conversation, so the sign raises a question only, per [[smell-is-not-a-finding]]. This sign is ours.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who executes | Project setup, or the task's assignee if set |
| Who reviews and steers | Project setup |
| Who asked for the work | The task or the originating request |

The choice was wrong if finished work repeatedly lands far from its estimate in a way someone present could have predicted, for instance for a kind of work the project has done before. That reading is ours.

## Agent executor note

The transfer here is ours, and no source in this chapter treats it.

When an agent executes, the first reason mostly falls away, because the executor is known in advance. The Lederer point also becomes awkward: "those who will do the work" would be the agent, and these sources say nothing about whether an agent's estimate of its own work has that advantage.

The second reason survives, in a changed form. What Kristy's colleague supplies is a memory of how similar work actually went. On a project steered by few people, that memory is in the steering person and in the board's history. So the plugin's estimate is a proposal that a person who remembers can correct, set against evidence from similar finished tasks, as on [[triangulation]]. It should not stand as a sole opinion. How the two views are compared is on [[independent-estimates]].

The product owner's exclusion is a question for a project of one or two people, where the person who wants the work may be the only person available. Chapter 6 does not treat that case. This wiki would keep the separation where there is a second person and otherwise record that the estimate is single-sourced.
