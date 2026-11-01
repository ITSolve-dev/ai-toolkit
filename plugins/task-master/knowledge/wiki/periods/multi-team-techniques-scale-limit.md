---
title: When Multi-Team Planning Techniques Apply
category: periods
summary: Cohn's four multi-team techniques are added only as needed, and by his own account a single team needs none of them, so they are not applied to a few people as ritual.
tags: [decision-rule, multi-team, scale, planning, dependencies]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# When Multi-Team Planning Techniques Apply

Cohn names four techniques for planning a project of several teams: a common estimation basis, adding detail to stories sooner, lookahead planning, and feeding buffers. He gates them by scale himself, which makes the gate the first thing to apply before any of them.

## The rule

> Keep in mind that you don’t need to do any of this if you’ve got a single team. You probably don’t even need to do this if you have just three or four approximately seven-person teams as long as those teams communicate often.
>
> — [[cohn-agile-estimating-planning]], L4211

This wiki reads the default answer below that scale as no. The number carries its condition: three or four teams of about seven are exempt only "as long as those teams communicate often". Team count alone does not decide it.

> A project may require some or all of these techniques depending on how many sub-teams are involved as well as how often and intensely they need to coordinate.
>
> — [[cohn-agile-estimating-planning]], L4097

## Inputs and where to read them

- **How many streams of work run in parallel.** Read from the board: who or what holds in-progress work at the same time.
- **How often work crosses between streams, and how heavily.** Read from dependency links between tasks held by different streams.
- **Whether a date is announced far ahead.** Cohn's justification for the extra work is that "many large projects need to announce and commit to deadlines many months in advance" (L4215). Without such a date, that justification falls away.

## What later fact would show the choice wrong

Hand-offs across streams slipping and pulling the plan with them: a task that was to start after another could not, repeatedly, while no technique was in place. One slip is not that fact, since that is what estimates do. This reading is this wiki's.

## Order of adoption

Cohn advises adding only as many as necessary, starting with the common basis and working toward feeding buffers (L4097-L4103). The summary softens this: "These techniques are generally introduced to a project in the order described. They can, however, be introduced in any order desired." (L4229). This wiki reads the order as cost-ascending advice rather than a dependency among the techniques: [[estimation-baseline]], then [[conditions-of-satisfaction]], then [[rolling-lookahead-plan]], then [[feeding-buffer]].

## Trade-off

The techniques cost planning time, and Cohn concedes it: "Well, yes, but so is a large, multi-team project." (L4211). His return is a target date estimated with more confidence and "some protection against easily avoided schedule delays" (L4215). Neither benefit is measured in the chapter, so it supports the mechanism and not a size of effect.

## Failure mode

**Scaling ritual on a small project.** Sign: a few people steering an agent keep a team-level baseline ceremony, a hand-off buffer, or a lookahead document, while the board shows one stream of work and no cross-stream dependencies. This raises a question to check, not a verdict: there may be a parallel stream the board does not show.

## Transfer to a few people and an agent

The transfer here is ours. The setup this plugin serves is under Cohn's stated threshold, so nothing in the chapter is required of it as a multi-team practice. Individual rules survive where their mechanism is not about team count: the hand-off rule at [[handoff-at-iteration-boundary]] and the discriminators at [[critical-dependency]] apply wherever one piece of work waits on another. The case that would reopen the gate is several agents or people working parallel streams with real hand-offs.
