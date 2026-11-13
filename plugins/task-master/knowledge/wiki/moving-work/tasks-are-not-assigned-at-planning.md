---
title: Tasks Are Not Assigned at Planning
category: moving-work
summary: Cohn leaves tasks unallocated when an iteration is planned; a task gets its executor at the moment it moves to active and stays unowned and visibly available until then, and people take one or two related tasks at a time, because who should do what only becomes clear during the period.
tags: [rule, assignment, pull, iterations, board-state, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Tasks Are Not Assigned at Planning

Cohn holds that the executor of a task is decided when it starts and not when the period is planned: "While planning an iteration, tasks are not allocated to specific individuals." ([[cohn-agile-estimating-planning]] L3045).

## The rule

> Individuals do not sign up for tasks until the iteration begins and generally only sign up for one or two related tasks at a time. New tasks are not begun until previously selected ones are completed.
>
> — [[cohn-agile-estimating-planning]], L3051

This wiki reads the second half as a work-in-progress limit stated at the person level. It is on [[wip-per-executor]], and it belongs alongside [[wip-control]].

Chapter 20 states the same rule from the board's side, and moves the moment from the start of the iteration to the moment of being ready:

> Individuals on an agile team do not sign up for (or get assigned) work until they are ready to work on it. This means that except for the last day or two of an iteration, there are typically many tasks that no one has yet signed up for.
>
> — [[cohn-agile-estimating-planning]], L4457

Cohn describes the move as one act: "a developer takes a card from the To Do column, puts her initials on it, and moves it to the In Process column" (L4484). This happens "throughout the day as developers are finishing work and selecting what they’ll work on next" (L4484). This wiki reads that as tying the owner to the state change: naming an executor and moving to active are the same event. So set the executor when the task enters an active state, and not before. A queued task is unowned.

## Reasoning

Cohn gives three reasons. The first is about information: "what is obvious at the start may not be what happens during the iteration", as when the expert on a query never reaches that task and someone else steps up (L3045-L3049). The second is about the team: signing up early "works against fostering a unified commitment" (L3053). The same unallocated state is his first reason for estimating as a group ([[who-estimates]]).

The third is that the board shows what is free: it "makes these tasks highly visible so that everyone can see which tasks are being worked on and which are available to sign up for" (L4457). This wiki reads the breakage as follows: an assignee on a queued task makes that task look taken, so the board can no longer answer what could be started next, and the choice of who does what has been made with less information than will exist when the work starts.

Cohn changed his position on this. He recommended individual allocation in his earlier book and says it works, but now prefers leaving it out (L3321). If allocation is needed, "the allocations should be considered temporary and subject to complete change once the iteration is planned and underway" (L3323).

The fictional case study in Chapter 23 (L4961) plays the rule out. A programmer offers to initial his card, and the coach declines: "No, it sounds like you’ll probably be the one to do it. But it works better if we don’t assign work to specific individuals right now." (L5714). Testing follows the same line: "Keep in mind, testing tasks are not assigned specifically to you, Prasad," and "Anyone can do them. If you fall a little behind, others will be expected to pick up testing tasks." (L5853).

## Sign of violation

These signs are this wiki's. Each raises a question and is not a verdict: an assignee on a queued task may be a real constraint, such as the one person who can do it.

- **In board state:** queued tasks that already have an assignee, most clearly when every selected task has one at the start of a period.
- **In board state:** an active task with no assignee. Cohn's single move rules this out too.
- **In board state during a period:** one assignee holding more than two tasks in progress, or unrelated ones, against the threshold on [[wip-per-executor]].
- **In board history:** the assignee was set long before the task's first move to an active state.
- **In board history:** a task reassigned late, after sitting assigned and unstarted.

## Trade-off

Leaving tasks unassigned gives up the check of each person's load that Cohn calls "the personal math" (L3321). The overall capacity check on [[iteration-capacity]] has to stand in for it, and it can miss overload on one function. This wiki notes a second cost: nobody can read a person's coming work from the board, and a task only one executor can do is discovered at pull time and not at planning. The case study shows the limit of "Anyone can do them": a helper offers to test and says "I probably can’t do any of the automation but I can help specify good test cases." (L5911). This wiki reads that as pickup across skills being partial, so unassigned tasks do not remove a bottleneck, and [[filling-a-period]] checks for one separately. The charter leaves individual load out of scope, so this page does not weigh that loss further.

## Which setup this applies under

The resolution is this wiki's.

- **Flow setup:** the rule follows from the pull signal, where members "start work on an item (pull or select) only when there is a clear signal that there is capacity to do so" ([[kanban-guide]] L141, quoted on [[what-may-move]]).
- **Iteration setup:** the Scrum Guide leaves this to the team, which decides "who does what, when, and how" ([[scrum-guide-2020]] L114, quoted on [[wip-control]]). Cohn's rule is one permitted choice inside that, and this wiki adopts it as the default. With several executors drawing from a shared selection, assign at start.
- **Either setup with one executor:** an assignee field carries no decision, so the rule has nothing to check and the signs above do not apply.

What survives under any setup is the limit on how much one executor holds at once ([[wip-per-executor]]). A task that needs a particular person's review should record that as a fact about the task. It is not an assignment.

## Agent executor note

The second reason is about people's solidarity. This wiki does not carry it over: motivation is out of scope, and an agent has none to foster. Cohn's picture of people choosing what to do next does not transfer either, and with a single agent the assignee field carries no information. The first reason survives only where more than one executor could take the task, whether several agents or a person and an agent. There the assignee set at start is the record of which run holds the task, and a pre-assigned queue is a plan that the next start may contradict.
