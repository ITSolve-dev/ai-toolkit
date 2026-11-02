---
title: Multitasking
category: moving-work
summary: Interleaving several started tasks; one study has value-adding time falling rapidly past two concurrent tasks for an individual, and even with no switching cost interleaving keeps each unit in process longer. Often set off by lateness, through requests for partial delivery.
tags: [failure-mode, wip, human-mechanism, dependencies]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Multitasking

Multitasking is working on several started tasks at once by switching among them. Cohn names it the second cause of planning failure and gives two separate arguments against it: one is a measured effect on people, and the other is arithmetic that needs no switching cost at all.

## The switching cost

Cohn reports a study by Clark and Wheelwright (1993): an individual's value-adding time "drops rapidly when the individual is working on more than two tasks" ([[cohn-agile-estimating-planning]] L618). The setting is individuals assigned concurrent tasks. The figure's data points did not survive extraction, so this wiki states no percentages.

Cohn's explanation for the shape is that two tasks help and three do not:

> With two value-adding tasks, if you become blocked on one you can switch to the other.
>
> — [[cohn-agile-estimating-planning]], L627

Cohn continues that we are rarely blocked on more than one task at once, and that with three or more "the time spent switching among them becomes a much more tangible cost and burden." (L627).

## The arithmetic

Cohn's second argument is Figure 2.3. Three pieces of ten days each, for a database, an API and a user interface, are done one after another, then redone as interleaved slices (L629-L638). Cohn's result is that "each of the desired units of work remains in process for 20 days rather than 10 as was the case when the work was done serially." (L642), and that the database and API work finish later than planned. He adds that the figure assumes no switching slowdown at all (L644), so this cost comes before any loss of productivity.

This wiki reconstructs the numbers, assuming equal five-day slices in the order the figure shows:

| Unit | Finishes, serial | Finishes, interleaved |
|---|---|---|
| Database | day 10 | day 20 |
| API | day 20 | day 25 |
| User interface | day 30 | day 30 |

This wiki reads the table as showing that the last unit finishes on the same day either way, so interleaving gains nothing at the end and loses it on everything before.

## How it starts

Cohn's account is that lateness triggers it: "Multitasking often becomes an issue once a project starts to have some activities finish late." (L629). Someone waiting asks for "just enough of the API work so that you can get started." (L633). He calls the result "the illusion of speed" (L642), and his summary says it is taken up "With good intentions" as a possible cure and leaves the project further behind (L678).

This wiki reads a partial delivery as a sign about the cut as well. A task whose result is requested in instalments is failing the charter's test that a result is presented once ([[unit-of-work]]), and a request for a subset suggests a smaller unit was there to be cut ([[vertical-slice]]).

Cohn gives two structural causes. The first is that "work is typically assigned well in advance of when the work will begin and it is impossible to efficiently allocate work in advance", which assigning to individuals rather than groups makes worse (L646). The second is the pursuit of full utilization, covered on [[filling-a-period]].

## Observable signs

- **In board state:** one executor holds more than two started tasks. This wiki reads the sign as a fact about a line of work on the board, and not as a judgement of anyone's load, which is outside the charter.
- **In board history:** a task's age is well above the time actually spent moving it, with its state alternating against other tasks held by the same executor.
- **In task history or comments:** a request for part of a task so another can begin, or a task marked done in stages.
- **In a plan:** tasks assigned to named executors long before they can start.

These signs are this wiki's derivation.

## Cost of avoiding it

This wiki notes that serial work leaves someone waiting, which is the pressure that produces the partial request. Holding to one thread means accepting that wait, and [[wip-control]] accepts the same cost.

## Agent executor note

The study measures people, and its limit of two does not transfer. This wiki does not use it to set a number on [[wip-control]], whose method remains the extended one recorded on that page. Cohn's reason for the limit, the burden of switching, is a human mechanism: an agent run has no attention to split.

The arithmetic survives only for an executor that really does interleave. Parallel agent runs do not interleave, so a unit's time in process need not double. What may remain is the same effect one level up, in the person steering, who switches among results to review. This wiki reads the study as more likely to apply there, since that person is the individual it measured. That is unmeasured.
