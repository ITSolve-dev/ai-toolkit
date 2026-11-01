---
title: Critical Dependency
category: ordering
summary: A dependency needs protection only if planned high-priority work cannot proceed without the deliverable, no other valuable work can be swapped in, and a partial deliverable would not let the receiver start.
tags: [decision-rule, dependencies, prioritization, sequencing]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Critical Dependency

A critical dependency is one where a late deliverable actually stops valuable work. Cohn defines it by elimination, in order to decide where a feeding buffer belongs, and this wiki reads the same questions as separating a dependency that constrains the plan from one that only describes an order.

## The test

First allocate the work: "first allocate user stories among teams and iterations. Then look for critical dependencies between iterations and teams." ([[cohn-agile-estimating-planning]] L4193). This wiki reads a dependency as impossible to judge before allocation, because criticality depends on what is planned for when.

Then a dependency is critical only if all three hold:

1. **The blocked work is planned and high-priority, and cannot be done without the deliverable.** "add a feeding buffer only if a team will be unable to do planned, high-priority work without the deliverables of another team" (L4193).
2. **Nothing comparable can take its place.** "if the team can easily swap in other highly valuable work, a feeding buffer is unnecessary" (L4193-L4199).
3. **A partial deliverable would not let the receiver start.** "do not add a feeding buffer if the second team will be able to start making progress with a partial deliverable from the first team" (L4199).

## Inputs and where to read them

- Whether work is planned and its priority: the task's period and its place in the order.
- Whether it cannot proceed: the dependency link and the task's stated prerequisites.
- Whether a swap exists: the rest of the ordered backlog, specifically ready tasks of similar value.
- Whether a partial is enough: what the receiving task actually uses of the deliverable, read from both tasks' text.

## What later fact would show the choice wrong

These facts are this wiki's. A dependency judged not critical, where the deliverable was late and the receiver then sat idle or dropped to low-value work, means the swap or partial assumption was wrong. A dependency judged critical, where the deliverable was late and the receiver proceeded anyway, shows the opposite error.

## Trade-off

Treating every dependency as critical is the cheap judgement and the expensive plan, because protection can prolong a schedule (L4191). Treating none as critical is the reverse, and is paid when the hand-off slips.

## Transfer to a few people and an agent

The three questions are the part of this chapter that survives the scale change, since none refers to team count. This transfer is ours, and it goes beyond Cohn, who applies them only to the buffer decision. This wiki also reads them as a check on the dependency itself. For a few people steering an agent, they decide what comes first more than whether to buffer. A critical dependency fixes order. A dependency with a swap or a useful partial leaves order open, and the partial may suggest a better cut.

Related: [[sequence-versus-wait]], [[natural-order-of-work]], [[handoff-at-iteration-boundary]], [[feeding-buffer]], [[multi-team-techniques-scale-limit]].
