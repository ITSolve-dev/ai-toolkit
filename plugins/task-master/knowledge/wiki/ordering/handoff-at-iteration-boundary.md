---
title: Hand Off at the Iteration Boundary
category: ordering
summary: Commit only to work whose inputs are finished before the period starts; a commitment resting on something due mid-period is more fragile and puts the schedule at greater risk.
tags: [rule, dependencies, commitment, iterations, wait]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Hand Off at the Iteration Boundary

A dependency between two pieces of work is safest when it is resolved between periods, so that the receiver plans against something finished rather than something expected.

## The rule

> Teams will often need to make commitments based on mid-iteration deliverables. However, to the extent possible, they should limit commitments to work completed prior to the start of the iteration.
>
> — [[cohn-agile-estimating-planning]], L4168

Cohn's contrast is one story under two situations. In the first, "at the start of the third iteration, Team 2 was able to make a meaningful commitment to completing the personal records user story because they knew that the API was finished" (L4168). In the second, the API is expected to finish a few days into the iteration. Even if the story could still be finished in time, "it is a much more tenuous commitment and the overall schedule is at greater risk" (L4168).

## The reasoning

A commitment is made at the start of a period from what is known then. A finished input is a fact and an expected input is itself an estimate, so the receiver's commitment inherits that estimate's error. This reasoning is this wiki's account of why the two cases differ. Cohn states the difference and not the mechanism. [[lateness-passes-down-the-schedule]] holds the same effect at the level of a schedule.

## Discriminating criterion: an open input at commitment

[[sequence-versus-wait]] separates those two relations by who holds the prerequisite. Cohn's two cases fall on the same side of that test, since both teams belong to one project, so both are sequences. They differ in whether the input is finished when the dependent work is committed. This wiki reads that as a second line, at the grain of a commitment:

- **Input finished before the period opens:** the order is settled and the receiver starts whenever it starts.
- **Input due during the period:** the work is still a sequence, but the receiver's completion depends on someone else's remaining estimate, so for this period the commitment carries the risk of a wait.

Cohn's own wording supports only the period-level version. The charter's test, "once started, the task can be finished without waiting", has no source and comes from the plugin's design. This rule sits next to that test as evidence at a different grain and does not ground it: Cohn is talking about commitments over an iteration, not what makes a unit of work.

## Sign of violation

These signs are this wiki's derivation from L4168.

- A task committed to a period depends on a task that was not done when the period started.
- The planning note for a task reads as an expectation about another task, such as due in a few days.
- In history, a task entered a period with an open prerequisite and then missed the period.

The last sign needs care: a miss can have other causes, so it asks whether the open prerequisite was the reason.

## Trade-off

This wiki notes that the rule costs utilisation or duration, since a receiver held to the next boundary may start later than it could have. Cohn does not make it absolute, as his "to the extent possible" shows. This wiki reads a mid-period dependency as acceptable when it is recognised as a risk to that commitment, and when it matters enough, Cohn's protection on a multi-team project is a feeding buffer (L4187), a technique this wiki does not keep at its scale. Whether it matters is decided at [[critical-dependency]].

## Agent executor note

The rule is about commitments and dependency, and neither depends on a human. The transfer here is ours: with one agent and no parallel stream, a period rarely contains a true mid-period hand-off, and the same logic applies at the grain of a task. An agent handed a task whose input is not finished cannot wait productively and will either stop or guess. So this wiki expects the sign to be more useful on a task's prerequisites than on a calendar boundary. Without fixed iterations, the boundary becomes the moment the task is started.

The rule's setting in Cohn is multi-team, and he exempts a single team from that chapter's techniques (L4211; see [[critical-dependency]]).
