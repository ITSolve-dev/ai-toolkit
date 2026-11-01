---
title: Cost of Delay Over Duration
category: ordering
summary: Where durations vary widely and capacity is constrained, divide cost of delay by duration so that the work freeing most value per unit of capacity goes first; with word ratings the division has no arithmetic, so this wiki applies it only within one rank.
tags: [decision-rule, ordering, cost-of-delay, estimation, prioritization]
sources: [black-swan-qualitative-cod, zimmermann-good-bug-report]
created: 2026-11-01
updated: 2026-11-01
---

# Cost of Delay Over Duration

This rule breaks the order that [[ordering-by-value-and-urgency]] leaves open. Two tasks that lose the same amount by waiting are not equal if one takes far longer. The source calls the division CD3:

> You can use this assessment of Cost of Delay to help with prioritisation as well. Assuming that you are dealing with things where the duration is highly variable I would recommend dividing the Cost of Delay by Duration. The CD3 (**C**ost of **D**elay **D**ivided by **D**uration) scheduling algorithm will generate more total value in a given time for a scarce or constrained capacity.
>
> — [[black-swan-qualitative-cod]], L91

This wiki reads two conditions in that passage. Durations have to be "highly variable", and capacity has to be "scarce or constrained". Without the first, dividing changes nothing. Without the second, nothing is queueing and order has little to decide. The claim of "more total value" is the author's, and the article shows no derivation or measurement for it.

The author does not ask for precision: "This can be as quick and easy as a simple T-shirt sizing of the various options." and "I’d start with what you already have and use that as your denominator." (L93).

A second voice, of low weight, says something similar. One developer's survey comment in [[zimmermann-good-bug-report]] reads: "For me it amounts to a consideration of ‘how serious is this?’ versus ‘how long will it take me to find/fix it?’." (L445). That is one person's description of a habit and not a finding of the paper.

## The gap in the source

The author recommends the division in an article about ratings in words, and does not say how to divide "Very High" by "Medium". A rate over a duration needs numbers. This wiki does not supply numbers for the bands, since any such numbers would be invented.

## The rule

This wiki's application is narrower than the source's.

1. **Check the conditions.** If the sizes of the tasks in question are about the same, or nothing is waiting for capacity, skip this rule.
2. **Within one rank of [[ordering-by-value-and-urgency]], the smaller task goes first.**
3. **Across ranks, leave the rank standing,** unless the project already holds cost of delay as a number, in which case divide as the source says.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Each task's rank | [[ordering-by-value-and-urgency]] |
| Each task's size | The task, on the project's own scale ([[size-ceiling]]); the source accepts "what you already have" (L93) |
| How far the sizes differ | The tasks being compared |
| Whether capacity is constrained | Board state: is work waiting to start or waiting for review? |

The choice was wrong in one of three ways. These tests are this wiki's, and the article gives none.

- **A large task starved:** a larger task of the same rank was passed over repeatedly until its value had gone. Read this from its age against its rank.
- **The size was wrong:** the task chosen as smaller overran ([[overrun-triggers-a-recut]]), so the comparison rested on a false input.
- **The conditions did not hold:** the order made no visible difference, because nothing was waiting.

## Cost

The rule favours small tasks, and a project that applies it across everything can leave large tasks unstarted. Those are the tasks [[size-ceiling]] asks to have cut, so a starving large task is also a prompt to cut it. It also depends on estimates, with the limits on [[size-ceiling]].

## Agent executor note

The mechanism concerns capacity, and the source's capacity is a team's time. With an agent executing, this wiki's working reading is that the scarce thing is the attention of the people steering ([[synthesis]]). If so, "duration" should mean what a task will cost them to direct and review, and not how long a run takes, and the condition "scarce or constrained" is met at the review queue. This is unmeasured. No source here says how well an agent estimates either ([[size-ceiling]]).
