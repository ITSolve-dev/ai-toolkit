---
title: Related Changes Temptation
category: cutting-work
summary: Work added to an already sized task because it is nearby; it is kept only if it is necessary for the task or of equal priority to it, and otherwise it is ordered as a task of its own.
tags: [failure-mode, decomposition, sizing]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Related Changes Temptation

The related changes temptation is the undoing of a good cut by refilling it. A task reaches the right size and then gains work because the work is nearby:

> Once you’ve split a story and have it at an appropriate size, don’t make things worse by adding work to the story. Often this comes in the form of the temptation of related changes. We tell ourselves, “While I’m in that code, I might as well take care of these other lingering changes…”
>
> — [[cohn-agile-estimating-planning]], L2711

## Observable signs

Cohn gives the phrase. The other signs are this wiki's reading of his summary, which sets the bar at "related changes that are not necessary for the delivery of the user story" (L2729).

- **In task text:** added lines in the manner of "while we are in there" or "also clean up", with no link to the task's purpose ([[task-must-justify-itself]]).
- **In the result:** changes that no acceptance criterion accounts for.
- **In board history:** a task's estimate or scope grows after it was sized and cut. A sign raises a question, since scope can grow for other reasons, and [[overrun-triggers-a-recut]] covers those.

## The test

Cohn does not forbid the extra work. He makes it compete:

> Avoid making things worse by adding related changes to an appropriately sized feature, unless the related changes are of equivalent priority.
>
> — [[cohn-agile-estimating-planning]], L2713

His framing of the comparison is a question of what the same time buys: "which is higher priority: spending a half-day fixing a year-old bug or spending the same amount of time on something else?" (L2711). He calls the answer "entirely contextual" (L2711). This wiki reads the rule as: being close in the code is not an argument about priority. If the change is necessary for the task, it is part of the task. If it is not, it is compared like any other work: of equivalent priority it may join, and otherwise it takes its place in the order as a task of its own, per [[ordering-by-value-and-urgency]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Whether the change is needed for delivery | The task's acceptance criteria |
| The change's priority | The order on the board, or the person steering |
| The priority of the work it displaces | The order on the board |

Adding the change was wrong if the task then passed [[size-ceiling]] or missed its period. Refusing it was wrong if the separate task was immediately needed to finish this one, which means it was necessary all along. Both tests are this wiki's.

## Trade-off

Cohn grants the case for doing it: "It can very possibly be appropriate to fix a bug or address an old issue while working on a separate issue in the same part of the code." (L2711). This wiki notes the cost of refusing, which is a separate task for something small, and that cost is what [[combining-small-tasks]] addresses. The two differ in when and how the work joins: a combine is made while planning, estimated as a whole and prioritized as one, while a related change arrives after sizing and is compared with nothing.

## Agent executor note

Cohn's mechanism is a person's impulse at the keyboard, and the chapter does not say an agent has it. The harm is not on the executor's side, so this wiki expects the rule to survive: a result reviewed once gets harder to review for every change outside its purpose, and the person steering pays that. A task's stated boundaries and non-goals are where the rule gets applied to an agent, before work starts.
