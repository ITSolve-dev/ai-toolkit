---
title: Judging a Board's Columns
category: work-states
summary: The criteria for auditing a board's columns, each with the sign of failing it; six are judged per column and four across the board, and they apply to any setup with states.
tags: [method, work-states, board-design, audit]
sources: [wester-board-design, kanban-playbook-workflow-states, kanban-guide, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Judging a Board's Columns

This method audits an existing board. The sources offer design advice and no checklist, so the list below is this wiki's assembly. Each criterion names who supplied it, and the signs are this wiki's wording unless a source is quoted. All three sources come from one school and report no measurement. See [[distinguishable-work-states]] for what the criteria are protecting.

The Kanban Guide sets no limit on what a board may look like: "There are no specific guidelines for how a visualization should look." ([[kanban-guide]] L125). Wester says the same thing more bluntly: "there are no board police to decide what is right and wrong." ([[wester-board-design]] L61). A failed criterion therefore says what a column will cost, and it does not say the board is illegal.

## Per column

| # | Criterion | Sign of failing it | Source | Remedy |
|---|---|---|---|---|
| 1 | It names the work and not the worker | The name reads as a job title, a person, or an executor, such as a column for the agent | [[wester-board-design]] L22; the executor case is this wiki's | Rename by the stage of the work |
| 2 | It is a stage and not an attribute | Blocked, On Hold, or a column tasks enter from several states and leave for where they came from | [[wester-board-design]] L49 | [[column-versus-attribute]] |
| 3 | A task enters and leaves it at a point in time | Two readers would place the same task in different columns, or one task fits two columns | [[kanban-playbook-workflow-states]] L18, L22 | Redraw the boundary, or merge |
| 4 | It holds a group of activities and not one activity | Tasks pass through in almost no time, and several neighbouring columns behave alike | [[kanban-playbook-workflow-states]] L20 | Merge into one state |
| 5 | It says whether work is active or queued | Tasks sit in it with nothing happening, and the board cannot say so | [[wester-board-design]] L40 | [[active-versus-queued]] |
| 6 | Work actually uses it | History shows a kind of task routinely skipping it | [[kanban-playbook-workflow-states]] L35 | Decide whether that kind has a different path ([[started-and-finished-points]]) |

The Wester sign for criterion 1 is stated as a question: "Do the column names of your board sound like the titles of the people in your team?" (L22). The same line asks whether people often work in just one column. This wiki leaves that out, since it concerns individual assignment.

Criterion 6 goes beyond its source. The Playbook only reports that a bug fix skipped a step, and the reading of that as a test is ours.

## Across the board

| # | Criterion | Sign of failing it | Source | Remedy |
|---|---|---|---|---|
| 7 | Every recurring step has a place | Tasks keep sitting in a state for a reason its name does not mention | [[kanban-playbook-workflow-states]] L35; [[wester-board-design]] L57 | Add a state or a handoff |
| 8 | No expected cycle runs backward | History shows tasks moving to an earlier state, repeatedly between the same two | [[wester-board-design]] L34 | [[backward-movement]] |
| 9 | The started and finished points can be read off | Two readers count WIP differently from the same board | [[kanban-guide]] L111-L112 | [[started-and-finished-points]] |
| 10 | Piles appear where work really piles up | A pile-up that nobody can explain, or age figures that cannot be read | [[kanban-playbook-workflow-states]] L22 | [[mapping-workflow-states]] |

The Playbook's general statement of the failure, which criterion 10 turns into a test, is this:

> A board without well-designed states cannot help you manage flow. Work will pile up in places that do not match what is actually happening. Work Item Age will be hard to interpret. WIP will be difficult to control because the boundaries between states will be unclear to the people doing the work.
>
> — [[kanban-playbook-workflow-states]], L22

## Reading the result

The criteria are not all equal. Criteria 2, 3 and 9 are the ones that break the numbers, because they decide what is counted and when, so this wiki treats a failure there as a defect to fix. The others cost readability and can wait. A board for a few people should not add states to pass criterion 5 or 7 unless tasks are actually sitting there. This weighting is ours.

The criteria pull against each other. Criterion 5 and the handoff in criterion 7 add states, and criterion 4 removes them. The Playbook warns about "too many states" (L20), and Wester warns that with "too much granularity, team members can be confused" (L30). The resolution is the same in each case: add a state only where history shows tasks there.

## What practitioners report

The interviews behind [[montgomery-tracker-smells]] come from outside the Kanban school, so they are a second voice on three of these criteria. They add signs and no new criterion. They are perceptions from mostly large organisations, with no thresholds.

| Problem | Participants | Sign | Criterion |
|---|---|---|---|
| Lack of a Fitting Workflow | 17 (L423) | People work around the states. P26: "you have to cheat the process to make it work for these 10%". On a board this wiki reads it as tasks that pass through states in no time | 6, 7 |
| Workflow Bloat | 14 (L427) | P17: "fitting yourself into the workflow, instead of just doing the work" | 4 |
| Unclear Workflow | 5 (L431) | P05: "what does ‘resolved’ actually mean?" | 3, 9 |

P26's 90 and 10 percent are a way of speaking and not a measurement. The authors' reading of the first two problems is "a complex and nuanced trade-off within these systems between too much and too little support workflow options." (L421), which agrees with the tension between criteria described above. The study's "Too many issue types" (L160) is the same complaint about types, and its text gives no result. How many is too many is not stated, and the study does not establish that any of these harmed a project ([[smell-is-not-a-finding]]).

## Which holds under which setup

The criteria do not depend on the methodology, since each guide leaves column design open and neither disagrees with them. An iteration setup does add one rule of its own: a task that returns at a period's end is not a failure of criterion 8 ([[backward-movement]]).

## Agent executor note

The criteria concern the board and survive. Criterion 1 needs one addition, which is that a column named after the executor fails for the same reason as one named after a job title, since it records who holds the task and not what stage it has reached. Criterion 3's sign relies on a reader, and the plugin can be that reader. Wester's and the Playbook's reason for it, confusion among people, does not apply to an agent. What applies is the count, which goes wrong whoever is confused.
