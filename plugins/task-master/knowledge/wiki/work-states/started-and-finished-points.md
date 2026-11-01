---
title: Started and Finished Points
category: work-states
summary: The two defined moments between which a task counts as work in progress; every flow metric hangs from them, so each has to be an event the board can show and not a claim by the executor. The Kanban Guide lets each workflow define them, and the Scrum Guide fixes only finished, as one Definition of Done.
tags: [decision-rule, work-states, definition-of-done, kanban, scrum]
sources: [kanban-guide, scrum-guide-2020, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Started and Finished Points

A task is work in progress from the moment it crosses a defined started point until it crosses a defined finished point. The Kanban Guide makes these points part of the minimum definition of a workflow:

> A definition for when work items are started and finished within the workflow. Depending on the work item, your workflow may have more than one started or finished point.
>
> — [[kanban-guide]], L111

The Guide's next element gives the points their consequence: "Any work items between a started point and a finished point are considered work in progress (WIP)." (L112). The Guide then ties all four metrics to them: "For these four mandatory flow metrics, started and finished refer to how the Kanban system members have established those points in their DoW." (L166).

This wiki reads that as saying the points are the most consequential choice on a board. They decide what [[wip-control]] counts and what every number on [[flow-metrics]] means.

## The decision

The Guide lets each project define the points and does not say where they belong. The test below is this wiki's.

- **Started** is the first moment the task takes up capacity. With an agent executing, that is when the agent takes the task.
- **Finished** is the first moment nothing more is owed on the task, and the board can show it as an event. An executor's report that it is done is not such an event, because it only states what a check is supposed to establish ([[testable-acceptance]]).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| When capacity is first taken up | Board history against the record of runs |
| What has to be true for nothing more to be owed | The project's stated workflow and the task's acceptance check |

The started point is too late if work happens before it: activity on a task appears in history before its started timestamp. The finished point is too early if tasks past it come back, so that history shows a finished task returning to an earlier state. It is too late if tasks sit in the last state with nothing owed on them.

## Sign of violation

- **In board history:** a finished task returning to an earlier state.
- **In board history:** two tasks of the same kind reach the finished point with visibly different evidence, so the point does not mean one thing.
- **In board history:** a task's started timestamp comes after the first activity on it.

These signs are this wiki's.

The interviews behind [[montgomery-tracker-smells]] support the first sign, as a perception. Nine participants said scoping is hard, and the authors report that "users might incorrectly assume issues to be done and close them too early, leading to issues needing to be reopened." (L487). Five named the same trouble with status names: P05 asked "what does ‘resolved’ actually mean?" (L431), and P06 said their team "has a definition of ‘done’/‘ready’ that cannot be made transparent in Jira" (L431). This wiki reads the second as a requirement on the plugin: the definition has to be stated somewhere it can read. The study gives no rate of reopening, and a reopened task alone does not show a bad point, since a real defect can surface later.

## More than one point

The Guide allows several started or finished points depending on the item (L111). This wiki reads that as permission for a bug and a feature to differ, and as a warning for comparison: metrics from items with different points do not measure the same thing, so history compares like with like only when the points match. That caution is ours.

## Positions

**Kanban Guide:** both points are the project's to define, per workflow and per kind of item, as above.

**Scrum Guide:** finished is fixed, and started does not exist. The Guide defines one standard across all items: "The Definition of Done is a formal description of the state of the Increment when it meets the quality measures required for the product." ([[scrum-guide-2020]] L315). The effect is immediate: "The moment a Product Backlog item meets the Definition of Done, an Increment is born." (L317). The Guide has no started point, because it has no count of open work, and being selected for a Sprint is not the same as being started.

Scrum's standard also differs in kind from a task's acceptance check. The Definition of Done applies to every item, while [[testable-acceptance]] is specific to one task, and the Guide does not mention acceptance criteria. This wiki reads the two as complementary: a task is finished when it passes its own check and meets the shared standard.

## Which holds under which setup

- **Flow setup:** define both points. Every metric needs them.
- **Iteration setup:** one shared standard of done is required. A started point is optional for the guide, but this wiki wants one, because history cannot show age without it.
- **Iterations with a WIP control:** both, as a count needs a started point.

## Agent executor note

The definitions concern the work and survive. The risk grows with an agent, because an agent reports completion readily and nobody across the desk notices that it did not really finish. This wiki therefore wants a finished point that sits with a check or with the person reviewing, and not with the executor's own statement.
