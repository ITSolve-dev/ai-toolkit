---
title: Started and Finished Points
category: work-states
summary: The two defined moments between which a task counts as work in progress, which Vacanti calls a process's arrival and departure points; every flow metric hangs from them, so each has to be an event the board can show and not a claim by the executor. The Kanban Guide lets each workflow define them, the Scrum Guide fixes only finished, as one Definition of Done, and arrival is the first pull in a pull system and a stakeholder's expectation in a push system.
tags: [decision-rule, work-states, definition-of-done, kanban, scrum, commitment-point, pull, push, flow]
sources: [kanban-guide, scrum-guide-2020, montgomery-tracker-smells, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# Started and Finished Points

A task is work in progress from the moment it crosses a defined started point until it crosses a defined finished point. The Kanban Guide makes these points part of the minimum definition of a workflow:

> A definition for when work items are started and finished within the workflow. Depending on the work item, your workflow may have more than one started or finished point.
>
> — [[kanban-guide]], L111

The Guide's next element gives the points their consequence: "Any work items between a started point and a finished point are considered work in progress (WIP)." (L112). The Guide then ties all four metrics to them: "For these four mandatory flow metrics, started and finished refer to how the Kanban system members have established those points in their DoW." (L166).

This wiki reads that as saying the points are the most consequential choice on a board. They decide what [[wip-control]] counts and what every number on [[flow-metrics]] means. Vacanti treats the same two points as a process's boundaries, its arrival point and departure point, and calls defining them "the crucial starting point in predictable process design" ([[vacanti-actionable-agile-metrics]] L596). He adds that the step is "a necessary (but unfortunately not sufficient) step down the road to predictability" ([[vacanti-actionable-agile-metrics]] L592).

## The decision

The Guide lets each project define the points and does not say where they belong. The test below is this wiki's.

- **Started** is the first moment the task takes up capacity. With an agent executing, that is when the agent takes the task.
- **Finished** is the first moment nothing more is owed on the task, and the board can show it as an event. An executor's report that it is done is not such an event, because it only states what a check is supposed to establish ([[testable-acceptance]]).

## Arrival: pull against push

Vacanti's arrival point is where "a unit of work transforms from being just some arbitrary idea into being a legitimate work item that is to immediately be acted on and completed" ([[vacanti-actionable-agile-metrics]] L574-L580). Before it the item is a candidate, and after it the item counts as WIP until it departs. He gives two ways of placing it.

| | Pull system | Push system |
|---|---|---|
| What starts work | The team has capacity and takes the item | A request, regardless of capacity |
| Arrival point | The team's first pull transaction ([[vacanti-actionable-agile-metrics]] L582) | When any stakeholder has a reasonable expectation that the work is committed ([[vacanti-actionable-agile-metrics]] L584) |
| How hard to define | Fairly easy | Much harder |

The discriminating test is whether the people doing the work chose to take the item. In a pull system an item counts only "if it has been voluntarily pulled into the process by the individual, team, or organization responsible for operating that process" ([[vacanti-actionable-agile-metrics]] L582). In a push system the expectation counts "whether the team responsible for performing the work knows about it or agrees to it or not", and it may arise because the work was requested, a project was funded, or a manager thinks it is a good idea to start ([[vacanti-actionable-agile-metrics]] L584). For a push system he says the best first exercise is to define the boundaries at all ([[vacanti-actionable-agile-metrics]] L592). He also calls the pull arrival point the point of "commitment", deferring the details to his Chapter 8 ([[vacanti-actionable-agile-metrics]] L582).

Most backlog items fall outside: "for the most part—when I talk about WIP, I do not include backlog items in that discussion" ([[vacanti-actionable-agile-metrics]] L624). He flags this as a subtlety tied to the point of commitment and does not resolve it in this chapter.

## Departure

Departure may be delivery to an end user or to a downstream team or process ([[vacanti-actionable-agile-metrics]] L594). His example is a choice by responsibility: a team that deploys its own work counts an item as departed once deployed to production, and a team that does not counts it as departed once handed off to operations ([[vacanti-actionable-agile-metrics]] L594). This wiki reads the input as where the process's responsibility ends, read from the project's setup and not from column names.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| When capacity is first taken up | Board history against the record of runs |
| What has to be true for nothing more to be owed | The project's stated workflow and the task's acceptance check |

The started point is too late if work happens before it: activity on a task appears in history before its started timestamp. The finished point is too early if tasks past it come back, so that history shows a finished task returning to an earlier state. It is too late if tasks sit in the last state with nothing owed on them.

In this wiki's reading, a point is also wrong if the numbers it produces fail to answer the question asked. If a promised date is met by the metric and the customer has received nothing, the finished point sits before the customer's definition of done. If the started point precedes real commitment, waiting that belongs to intake shows up as cycle time.

## Sign of violation

- **In board history:** a finished task returning to an earlier state.
- **In board history:** two tasks of the same kind reach the finished point with visibly different evidence, so the point does not mean one thing.
- **In board history:** a task's started timestamp comes after the first activity on it.
- **In board state:** nothing on the board or in its description says which transition means work has started.
- **In board history:** start dates equal creation dates, so items are counted from the moment they were filed. That is the push definition in effect, whatever the board is called.
- **In board history:** items past the started point wait a long time before their first further move. Vacanti's arrival point is for work "to immediately be acted on" ([[vacanti-actionable-agile-metrics]] L580), so this wiki takes that wait as a sign that the point sits too early, or that more has been committed than can start.
- **In board history:** some items leave at merge, some at deploy and some at acceptance, so their cycle times do not measure the same thing.

These signs are this wiki's.

The interviews behind [[montgomery-tracker-smells]] support the first sign, as a perception. Nine participants said scoping is hard, and the authors report that "users might incorrectly assume issues to be done and close them too early, leading to issues needing to be reopened." (L487). Five named the same trouble with status names: P05 asked "what does ‘resolved’ actually mean?" (L431), and P06 said their team "has a definition of ‘done’/‘ready’ that cannot be made transparent in Jira" (L431). This wiki reads the second as a requirement on the plugin: the definition has to be stated somewhere it can read. The study gives no rate of reopening, and a reopened task alone does not show a bad point, since a real defect can surface later.

## More than one point

The Guide allows several started or finished points depending on the item (L111). This wiki reads that as permission for a bug and a feature to differ, and as a warning for comparison: metrics from items with different points do not measure the same thing, so history compares like with like only when the points match. That caution is ours.

## Positions

**Kanban Guide:** both points are the project's to define, per workflow and per kind of item, as above.

**Scrum Guide:** finished is fixed, and started does not exist. The Guide defines one standard across all items: "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product." ([[scrum-guide-2020]] L315). The effect is immediate: "The moment a Product Backlog item meets the Definition of Done, an Increment is born." (L317). The Guide has no started point, because it has no count of open work, and being selected for a Sprint is not the same as being started.

Scrum's standard also differs in kind from a task's acceptance check. The Definition of Done applies to every item, while [[testable-acceptance]] is specific to one task, and the Guide does not mention acceptance criteria. This wiki reads the two as complementary: a task is finished when it passes its own check and meets the shared standard.

**Vacanti:** the project defines both, as boundaries of its process, and the definition of departure "holds true whether you are operating a pull or a push system" ([[vacanti-actionable-agile-metrics]] L594). The arrival point differs by system, as above. Crossings are counted on their real dates, whatever a sprint is doing: [[process-boundaries]].

## Which holds under which setup

- **Flow setup:** define both points. Every metric needs them. A flow setup pulls, so Vacanti's first pull and this page's capacity test name the same moment.
- **Iteration setup:** one shared standard of done is required. A started point is optional for the guide, but this wiki wants one, because history cannot show age without it.
- **Iterations with a WIP control:** both, as a count needs a started point.
- **Work promised before anyone takes it:** the two tests differ, since Vacanti's push arrival comes earlier than capacity is taken up. This wiki keeps the capacity test for the started point, because a count that includes untouched promises gives a bound nothing to restrain, and it reads the time since the promise separately as the wait the requester felt. This departs from Vacanti for push systems, and the departure is ours.

## Trade-offs

This wiki's reading, not a source's: narrow points give shorter, cleaner numbers that omit the waits outside them, and wide points give numbers closer to what the customer feels but mix in time the project does not control. Vacanti's related point is that every such figure is relative to perspective ([[vacanti-actionable-agile-metrics]] L680; see [[cycle-time]]).

## Agent executor note

The definitions concern the work and survive. The risk grows with an agent, because an agent reports completion readily and nobody across the desk notices that it did not really finish. This wiki therefore wants a finished point that sits with a check or with the person reviewing, and not with the executor's own statement.

The transfer of Vacanti's "capacity" is ours: with an agent executing, a pull is limited less by the executor than by the attention of the person steering to brief it and check its results, so the pull decision stays with that person.

The charter treats review of a presented result as no wait inside a task, because the executor's part has ended. That concerns where a task is cut, and it does not settle where the finished point sits. This wiki treats the two as separate: if the finished point is set after acceptance, review time counts as cycle time even though it is not a wait inside the task.
