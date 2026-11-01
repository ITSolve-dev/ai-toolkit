---
title: What May Move
category: moving-work
summary: The trigger that lets a task start or change state; under the Kanban Guide a task starts only on a capacity signal and moves by stated policies, and under the Scrum Guide it enters by selection for a period, stays while the goal is safe, and leaves unfinished only by going back.
tags: [decision-rule, wip, pull, kanban, scrum]
sources: [kanban-guide, scrum-guide-2020]
created: 2026-11-01
updated: 2026-11-01
---

# What May Move

Every board needs an answer to one question: what makes it allowable for this task to start or change state now? The answer depends on the methodology chosen when the project was set up.

## Kanban Guide: a capacity signal

> An effect of controlling WIP is that it should create a pull system; Kanban system members should start work on an item (pull or select) only when there is a clear signal that there is capacity to do so. When WIP drops below the control set in the DoW, that can be a signal to select new work. Kanban system members should refrain from selecting more than the number of work items into a given part of the workflow beyond the WIP control.
>
> — [[kanban-guide]], L141

This wiki reads three claims there. A start needs a signal. The ordinary signal is the count falling below the bound on [[wip-control]]. The same limit applies to a part of the workflow, so a state with its own bound refuses work the same way.

Moves between states follow the project's own rules. The Guide requires "Explicit policies about how work items can flow through each state from started to finished." (L114). It requires that the policies exist and says nothing about what they contain, so a Kanban project cannot read its forward rule from the Guide.

## Scrum Guide: selection, the goal, and Done

The Scrum Guide has no board and no states, so it says nothing about a move between columns. Its claims concern three edges of a period.

- **Entering.** Work enters by selection: "Through discussion with the Product Owner, the Developers select items from the Product Backlog to include in the current Sprint." ([[scrum-guide-2020]] L220). See [[filling-a-period]].
- **During.** Once selected, how the work proceeds is the team's own: they "internally decide who does what, when, and how" (L114). The only constraint on change is the goal ([[mid-period-change]]).
- **Leaving.** An item leaves by meeting the Definition of Done, or else it "returns to the Product Backlog for future consideration" (L319). See [[unfinished-at-period-end]].

This wiki reads the difference between the two guides as a difference in when the decision is made. The Kanban Guide decides at each start, from the state of the board. The Scrum Guide decides once for the period, from a forecast, and then protects the result.

## What the signal does not decide

A capacity signal says that something may start. It does not say which task, because the Kanban Guide has no ordering rule ([[kanban-guide]]). The Scrum Guide names who orders the backlog and gives no criterion. Which task comes from [[independent-tasks]] and [[sequence-versus-wait]]. Whether the task is fit to start comes from the task-content pages, such as [[conversation-moves-into-the-task]].

## The rule

A task starts only when the setup's trigger has fired, and it changes state only as the project's stated policy allows.

- **Flow setup:** the trigger is the capacity signal.
- **Iteration setup:** the trigger is selection for the current period.
- **Iterations with a WIP control:** both must hold. A selected task still waits for the signal, and an unselected task does not start on the signal alone.

The whole lookup is on [[board-rules-by-setup]].

Moves toward an earlier state are a separate question, on [[backward-movement]].

## Sign of violation

- **In board history:** a task started while the count was at the bound, with no declared exception.
- **In board history:** a state change that the project's stated policy does not allow, such as an item entering a state whose entry condition it does not meet.
- **In board state:** many tasks started and few of them moving, which is what pushing work looks like from the outside.
- **In board history, under iterations:** a task started during a period that was never selected for it and that no agreed change brought in.

The signs are this wiki's derivation from L114 and L141 of [[kanban-guide]] and L220 of [[scrum-guide-2020]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The project's setup | Project configuration |
| The started, unfinished count and the bound | Board state and project configuration |
| The period's selection | The period's record |
| The policy for the state in question | Project configuration |

A start was wrong if the task then sat with nobody and nothing acting on it. That shows the signal did not reflect real capacity. With an agent, this usually means the count was below the bound while the people steering could not take on another result.

## Agent executor note

The Guide's "pull or select" is an act by a person who looks at the board. An agent does not look at a board unless something tells it to, so the check belongs to the plugin or to the person steering. The trigger itself concerns counts and survives. What it means by capacity does not transfer directly, as [[wip-control]] explains.
