---
title: Incomparable Tasks
category: ordering
summary: Tasks are incomparable when the rating ties them or cannot be made at all; a tie goes to duration and then to anything cheap, and a task that cannot be rated is not forced into a band.
tags: [decision-rule, ordering, cost-of-delay, prioritization]
sources: [black-swan-qualitative-cod, kubernetes-issue-triage]
created: 2026-11-01
updated: 2026-11-01
---

# Incomparable Tasks

The charter asks what to do with tasks that cannot be compared. No ingested source treats this as a topic, so the rule below is assembled by this wiki from sourced parts, and each part says where it comes from. There are two cases, and they need different answers: the rating ties the tasks, or the rating cannot be made.

## The rating ties them

Nine combinations cannot separate many tasks. The author does not need them to: "We don’t need the Cost of Delay to be precise for this to work." ([[black-swan-qualitative-cod]] L101). This wiki reads a tie as a statement that the rating cannot tell the tasks apart, and it does not ask for a finer rating.

1. Use [[cost-of-delay-over-duration]]: the smaller task goes first if sizes differ.
2. Use order constraints: a task that unblocks another goes first ([[sequence-versus-wait]]).
3. If both are equal, the order does not matter by this rule. Take either, and do not spend the person's time on the question. This last step is this wiki's: if two tasks lose the same by waiting and use the same capacity, swapping them changes nothing the rule can see.

## The rating cannot be made

Sometimes nobody can say what a task is worth or what waiting does to it. A forced band here would be a guess that reads like a judgement.

- **If a person can answer, ask.** Value and urgency are task-only facts ([[recoverable-versus-task-only-facts]]), so one question is usually the cheapest step ([[clarifying-questions]]).
- **If nothing stands behind it yet, hold it outside the order.** The Kubernetes guide has a level for this: "Possibly useful, but not yet enough support to actually get it done." and "Mostly placeholders for potentially good ideas, so that they don’t get completely forgotten, and can be referenced or deduped every time they come up" ([[kubernetes-issue-triage]] L236). This wiki reads that as a place for what cannot be compared, and it counts each time the idea comes up again as evidence for rating it. The holding rule is on [[closing-what-no-longer-applies]].
- **If the answer depends on learning something,** the first step is the smallest thing that shows it, which is a matter of cutting ([[find-core-complexity]], [[spike-as-last-resort]]).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Each task's rank | [[ordering-by-value-and-urgency]] |
| Each task's size | The task |
| Which tasks wait on which | The tasks' stated dependencies |
| Whether a person can supply the rating | The requester |

A tie was broken wrongly if the rating was in fact able to separate the tasks, which shows later as one of them losing value that the other did not. A task held out of the rating was held out wrongly if the need it served expired while it sat there.

## Cost

Taking either task saves a decision, and it gives up any chance that a closer look would have found a difference. This wiki accepts that, since the look costs the person's time and the rating has already said it sees none.

## Agent executor note

The steps concern the tasks and survive. The last step of the tie matters more with an agent, because the plugin can ask a person about every tie, and each question spends the budget that [[clarifying-questions]] protects.
