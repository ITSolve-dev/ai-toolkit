---
title: Backward Movement
category: moving-work
summary: Moving a card to an earlier state loses visibility and data, so an expected cycle such as rework after review stays in the later state or goes to a new state on the right; the Scrum Guide's return of an unfinished item to the backlog is the one sanctioned exception.
tags: [rule, moving-work, board-history, kanban, scrum]
sources: [wester-board-design, kanban-guide, scrum-guide-2020, montgomery-tracker-smells, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# Backward Movement

When review finds a defect, the natural move is to drag the card back to the earlier state. Wester argues against it:

> If the team doesn’t talk about how to handle the discovery of bugs when work is in the *Validating* column, they may think that the best course of action is to move it back to the *Executing* column (and repeat this process as many times as it takes.) Unfortunately, moving cards backwards causes us to lose visibility and data.
>
> — [[wester-board-design]], L34

Wester offers two alternatives: "One option is to keep all cards in *Validating* until all found bugs are fixed." (L36), or a new column to the right of *Validating*, called *Fixing*, into which cards move when bugs are found (L36). Wester's reason is that "data is preserved" (L36): the original time in the first state stays measurable, and so does the time since the task first reached the second state.

The post does not spell out the data problem and links to another article for it (L34), which this wiki has not read. So the data claim is kept at that level.

## The rule

A task moves forward only. A cycle that is expected is drawn on the board in advance, by staying in the later state or by a state to its right.

## Sign of violation

- **In board history:** a task's sequence of states contains a move to an earlier state.
- **In board history:** the same task moves between two states several times, which is Wester's "as many times as it takes".

The second sign also shows that a cycle is expected, and so that the board should be drawn for it.

What the second sign does not establish is a defect. The study behind [[montgomery-tracker-smells]] lists "Properties such as status and assignee are switched back and forth between the same values." (L158) as a smell, and 4 of 13 disagreed or said it depends (L528). P02 said it is "part of their process to pass issues back and forth between assignee and reviewer; it is their quality assurance", and P06 that "it is intended" (L528). This wiki reads those as agreeing with the second sign's meaning: the movement shows a cycle is expected. Whether that is a failure depends on whether the board draws the cycle, so apply [[smell-is-not-a-finding]]. The study gives no count at which switching becomes too much.

## Why

What breaks is the reading of history. Time in each state stops meaning one thing once a task visits a state twice, so [[flow-metrics]] and any age comparison become harder to interpret.

## Cost

Keeping a task in *Validating* during a fix means the state no longer says what is happening, which works against [[active-versus-queued]]. Adding *Fixing* adds a state. The choice between them is below.

## Choosing between the two remedies

Wester gives both options and no way of choosing. This choice is this wiki's.

| Input | Read from |
|---|---|
| How often tasks of this kind need rework after review | Board history |
| Whether the time spent on rework is worth seeing | The people steering |

Use the *Fixing* state when rework is common, because the amount of rework is then something to see. Stay in the later state when rework is rare. The choice was wrong if a *Fixing* state sits empty most of the time, or if tasks stay long in the review state while being reworked.

## Positions

**Wester:** as above.

**Kanban Guide:** silent. It requires "Explicit policies about how work items can flow through each state from started to finished." ([[kanban-guide]] L114), so a project may allow backward moves by policy.

**Scrum Guide:** it prescribes a backward move in one case. An item that misses the Definition of Done "returns to the Product Backlog for future consideration." ([[scrum-guide-2020]] L319). This wiki reads that as leaving the workflow and not as moving back within it.

**Vacanti:** forward only for ordinary defects, which do "not normally constitute an egregious enough offense to cause the item to be moved back", but an item in Test "so broken that it cannot even be tested" goes back to the appropriate prior step with its Test date erased ([[vacanti-actionable-agile-metrics]] L1416); see [[non-standard-departure]].

**Kanban Maturity Model:** a task leaving a [[parking-lot]] returns to the active state it left, which is a backward move of the kind Wester objects to.

## Which holds under which setup

- **Inside a period or a flow:** forward only, as the rule says, except the two narrow cases on [[non-standard-departure]]: an item too broken to be tested goes back one step, and an item expected to return leaves the board with its history kept. This wiki reads neither as an expected cycle: the first is an arrival in a step whose entry condition was not met, and the second leaves the workflow. The lookup row on [[board-rules-by-setup]] carries the same exceptions.
- **At a period's end, under iterations:** an unfinished task leaves the workflow and returns to the unstarted pile, by [[unfinished-at-period-end]]. This is not a violation, and history should show it as a return at a period boundary.

The resolution is this wiki's.

## Agent executor note

This case is routine with an agent. A person reviews a result, finds it wrong, and sends it back. The rule says to send it to *Fixing* or leave it in review, and not to drag it back to the executing state. The mechanism concerns data and survives the change of executor. The evidence is practice from human teams, with no measurement.
