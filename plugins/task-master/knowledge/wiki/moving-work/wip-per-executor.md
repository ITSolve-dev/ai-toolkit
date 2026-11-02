---
title: WIP Per Executor
category: moving-work
summary: One run of an agent holds one task and a person very few: Cohn limits each developer to one or two cards in process, for flow and against context switching, and one study has value-adding time falling rapidly past two concurrent tasks. Even with no switching cost, interleaving keeps each unit in process longer (20 days instead of 10 in Cohn's figure), and it is often set off by lateness through requests for partial delivery. What transfers to an agent is one task per run, alongside a workflow-wide bound.
tags: [rule, wip, iterations, board-state, failure-mode, human-mechanism, dependencies]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# WIP Per Executor

This rule bounds concurrent work by who holds it, not by the whole workflow. Cohn states it for the iteration task board:

> No one should sign up for more than one or two cards at a time. This helps maintain a consistent flow of work through the process and reduces the cost of context switching among multiple tasks.
>
> — [[cohn-agile-estimating-planning]], L4484

He keeps it in view with the layout: "As a constant reminder of this, when I have a team set up their task board I have them make the In Process column the width of one card." (L4484). Chapter 14 gives the same figure when tasks are left unallocated at planning, "one or two related tasks at a time" (L3051, on [[tasks-are-not-assigned-at-planning]]).

## Conditions on the number

The figure "one or two" is an experienced practitioner's advice with no measurement. It applies to a developer holding Cohn's task cards, which are pieces of a story and smaller than this wiki's task ([[unit-of-work]]). It does not say how many whole tasks one executor should hold, and this wiki does not carry the number up a level.

This wiki reads the one-card width as a reminder and not a bound: a column that narrow limits nothing by count once several people work the same row. Cohn calls it a reminder himself.

## The rule

One run of an agent holds one task. A person executing holds very few. Cohn's one or two is the figure this base has for that, and the study in *Multitasking* (below) points the same way with the limits stated there.

The first sentence is this wiki's transfer, from the charter's test that a result is presented once ([[unit-of-work]]). Cohn's allowance of two is not carried over to a run.

## Sign of violation

- **In board state:** one run holding more than one active task, or one person more than two (Cohn's "one or two", L4484), with no declared reason. This is the one threshold this wiki uses for the sign, here and on [[tasks-are-not-assigned-at-planning]].
- **In board history:** one run moved two tasks to active and presented one combined result. This also points at a bad cut ([[compound-task-text-signs]]).

These signs are this wiki's. The first applies to the board's concurrency only. Whether a given person is overloaded is outside the charter.

## Why

Cohn names two effects, a consistent flow of work and a lower cost of context switching (L4484). He gives no figure for either here, and *Multitasking* (below) holds the study behind the second. This wiki keeps the first as a mechanism and treats the second under the note below.

## Cost

Cohn names none here. A blocked executor with a limit of one has nothing to do. Chapter 2 gives the reason for holding a second task, quoted under *The switching cost* (below). This wiki reads the second card in his allowance the same way, as slack for a stopped task, though Chapter 20 does not connect the two. See [[blocked-work-counts-against-wip]].

## Agent executor note

Context switching is a human cost, and it does not survive as stated: an agent has no attention to fragment. A per-executor limit also restrains less with agents. Ten runs holding one task each pass this rule and still flood the people who review them. So the bound that matters there is the workflow-wide one in [[wip-control]], and this page only keeps a run from mixing two results.

The study under *Multitasking* (below) measures people, and its limit of two does not transfer. This wiki does not use it to set a number on [[wip-control]], whose inputs are recorded on that page.

The arithmetic survives only for an executor that really does interleave. Parallel agent runs do not interleave, so a unit's time in process need not double. What may remain is the same effect one level up, in the person steering, who switches among results to review. This wiki reads the study as more likely to apply there, since that person is the individual it measured. That is unmeasured.

## Which holds under which setup

The resolution is this wiki's.

- **Iteration setup with people executing:** [[wip-control]] says people's own hours restrain the moment. Cohn's limit is the explicit form of that restraint, and a project wanting one can state it.
- **Iteration or flow setup with an agent executing:** one task per run, plus the workflow bound.
- **Flow setup with people executing:** the workflow bound is required, and a per-person limit is one allowed extra, since the Guide leaves the form open ([[kanban-guide]] L139, quoted on [[wip-control]]).

## Multitasking

Multitasking is working on several started tasks at once by switching among them. Cohn names it the second cause of planning failure and gives two separate arguments against it: one is a measured effect on people, and the other is arithmetic that needs no switching cost at all.

### The switching cost

Cohn reports a study by Clark and Wheelwright (1993): an individual's value-adding time "drops rapidly when the individual is working on more than two tasks" ([[cohn-agile-estimating-planning]] L618). The setting is individuals assigned concurrent tasks. The figure's data points did not survive extraction, so this wiki states no percentages.

Cohn's explanation for the shape is that two tasks help and three do not:

> With two value-adding tasks, if you become blocked on one you can switch to the other.
>
> — [[cohn-agile-estimating-planning]], L627

Cohn continues that we are rarely blocked on more than one task at once, and that with three or more "the time spent switching among them becomes a much more tangible cost and burden." (L627).

### The arithmetic

Cohn's second argument is Figure 2.3. Three pieces of ten days each, for a database, an API and a user interface, are done one after another, then redone as interleaved slices (L629-L638). Cohn's result is that "each of the desired units of work remains in process for 20 days rather than 10 as was the case when the work was done serially." (L642), and that the database and API work finish later than planned. He adds that the figure assumes no switching slowdown at all (L644), so this cost comes before any loss of productivity.

This wiki reconstructs the numbers, assuming equal five-day slices in the order the figure shows:

| Unit | Finishes, serial | Finishes, interleaved |
|---|---|---|
| Database | day 10 | day 20 |
| API | day 20 | day 25 |
| User interface | day 30 | day 30 |

This wiki reads the table as showing that the last unit finishes on the same day either way, so interleaving gains nothing at the end and loses it on everything before.

### How it starts

Cohn's account is that lateness triggers it: "Multitasking often becomes an issue once a project starts to have some activities finish late." (L629). Someone waiting asks for "just enough of the API work so that you can get started." (L633). He calls the result "the illusion of speed" (L642), and his summary says it is taken up "With good intentions" as a possible cure and leaves the project further behind (L678).

This wiki reads a partial delivery as a sign about the cut as well. A task whose result is requested in instalments is failing the charter's test that a result is presented once ([[unit-of-work]]), and a request for a subset suggests a smaller unit was there to be cut ([[vertical-slice]]).

Cohn gives two structural causes. The first is that "work is typically assigned well in advance of when the work will begin and it is impossible to efficiently allocate work in advance", which assigning to individuals rather than groups makes worse (L646). The second is the pursuit of full utilization, covered on [[filling-a-period]].

### Observable signs

- **In board state:** the sign at the top of this page, one run holding more than one started task or one person more than two. This wiki reads it as a fact about a line of work on the board, and not as a judgement of anyone's load, which is outside the charter.
- **In board history:** a task's age is well above the time actually spent moving it, with its state alternating against other tasks held by the same executor.
- **In task history or comments:** a request for part of a task so another can begin, or a task marked done in stages.
- **In a plan:** tasks assigned to named executors long before they can start.

These signs are this wiki's derivation.

### Cost of avoiding it

This wiki notes that serial work leaves someone waiting, which is the pressure that produces the partial request. Holding to one thread means accepting that wait, and [[wip-control]] accepts the same cost.
