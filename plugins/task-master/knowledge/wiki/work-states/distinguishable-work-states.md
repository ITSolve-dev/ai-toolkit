---
title: Distinguishable Work States
category: work-states
summary: The sources give criteria and no canonical column set, and treat a fixed list as the failure case; what they support is a small set of distinctions any board must let a reader make, drawn partly as columns and partly as markers. A board's columns are judged by criteria each with the sign of failing it, six per column and four across the board. Cohn's iteration task board is worked through as an example: only To Do and In Process are required states, and the rest are a marker, an optional handoff and a computed total.
tags: [concept, work-states, board-design, method, audit, iterations]
sources: [kanban-guide, scrum-guide-2020, wester-board-design, kanban-playbook-workflow-states, radzikowska-waiting-blocked, kubernetes-issue-triage, montgomery-tracker-smells, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Distinguishable Work States

The charter expects either a canonical state set or the criteria for one. The finding from this base is the second. No source offers a canonical set of columns, and the two that come closest argue against one. What the sources support is a set of distinctions a board must let a reader make.

## Why there is no canonical set

- **The Kanban Guide requires states and declines to name them.** It asks for "One or more defined states" ([[kanban-guide]] L112) and says "There are no specific guidelines for how a visualization should look." (L125).
- **The Kanban Playbook treats a familiar list as the failure case.** Its illustrated team sets up "To Do, In Analysis, In Development, In Testing, Done" and finds that "The board cannot answer the question because it was never designed to reflect how work actually moves." ([[kanban-playbook-workflow-states]] L33). The remedy is derivation and not a better list ([[mapping-workflow-states]]).
- **Wester gives tests and no list.** The columns in the post, such as *Executing* and *Validating*, are examples ([[wester-board-design]] L32).
- **The Scrum Guide has no states.** Its one state-like line is whether an item meets the Definition of Done ([[scrum-guide-2020]] L319).

The charter's note of 2026-11-01 predicted criteria for a mapping and not a fixed set, and the sources bear that out. All of them are normative or practice writing, though. No source compares state sets, so this is an absence of a set and not evidence against one.

## The distinctions

This table is this wiki's assembly. No source lists these together, and each row names where it comes from. A board can draw them in many ways, as long as a reader can tell each one.

| Distinction | The question it answers | Drawn as | From | What breaks without it |
|---|---|---|---|---|
| Unstarted or started | Has this taken up capacity? | The started point | [[kanban-guide]] L111-L112 | WIP cannot be counted |
| Started or finished | Is anything more owed? | The finished point | [[kanban-guide]] L111; [[scrum-guide-2020]] L315 | Throughput and cycle time mean nothing |
| Active or queued | Is anything happening to it? | States or sub-columns | [[wester-board-design]] L40 | Waiting reads as slow work |
| With the executor or handed off | Who is expected to hold it now? | A state | [[wester-board-design]] L57 | A planned review looks like a stop |
| Moving or stopped | Is it stuck? | A marker on the task | [[wester-board-design]] L49 | A stop is hidden or moved away from where it happened |
| Waiting or blocked | Does someone need to act now? | A marker, with its reason | [[radzikowska-waiting-blocked]] L44, L53 | An outside wait gets chased, or a real block gets left alone |

The first two rows are points and the next two are states, so together they account for a board's columns. The last two are conditions of a task in a state. The word "state" covers both in the charter. Wester's argument is that only the first kind belongs in columns ([[column-versus-attribute]]).

## What the plugin can treat as canonical

This wiki reads that as giving the plugin a classification rather than a column list. Each column of any board maps to one of five kinds: before the started point, queued, active, handed off, or past the finished point. Two markers then sit on tasks: blocked and waiting. The classification is this wiki's, and it is what *Judging a Board's Columns* (below) audits against.

This classification would be shown wrong by a column that fits none of the five kinds and yet passes every criterion, or by a real board whose tasks could not be told apart with it. Nothing has tested it on a real board, since the boards for that check are held out and do not yet exist.

## One distinction before the started point

The table says nothing about work before it starts, and [[kubernetes-issue-triage]] adds a line there: an item is either awaiting triage or accepted, shown by a label that triage replaces (L152). This wiki reads that as one more distinction inside the kind "before the started point": has anyone looked at this? It can be drawn as a marker or a column, and [[triage-procedure]] depends on it. Without it, an item nobody has read looks like one that is ready.

## Agent executor note

The distinctions concern the work and survive. The handoff row gains weight, since nearly every agent-run task ends with a person reviewing it. The active row becomes easier to check, because a run either exists or does not.

## Judging a Board's Columns

This method audits an existing board. The sources offer design advice and no checklist, so the list below is this wiki's assembly. Each criterion names who supplied it, and the signs are this wiki's wording unless a source is quoted. All three sources come from one school and report no measurement. See *Distinguishable Work States* (above) for what the criteria are protecting.

The Kanban Guide sets no limit on what a board may look like: "There are no specific guidelines for how a visualization should look." ([[kanban-guide]] L125). Wester says the same thing more bluntly: "there are no board police to decide what is right and wrong." ([[wester-board-design]] L61). A failed criterion therefore says what a column will cost, and it does not say the board is illegal.

### Per column

| # | Criterion | Sign of failing it | Source | Remedy |
|---|---|---|---|---|
| 1 | It names the work and not the worker | The name reads as a job title, a person, or an executor, such as a column for the agent | [[wester-board-design]] L22; the executor case is this wiki's | Rename by the stage of the work |
| 2 | It is a stage and not an attribute | Blocked, On Hold, or a column tasks enter from several states and leave for where they came from | [[wester-board-design]] L49 | [[column-versus-attribute]] |
| 3 | A task enters and leaves it at a point in time | Two readers would place the same task in different columns, or one task fits two columns | [[kanban-playbook-workflow-states]] L18, L22 | Redraw the boundary, or merge |
| 4 | It holds a group of activities and not one activity | Tasks pass through in almost no time, and several neighbouring columns behave alike | [[kanban-playbook-workflow-states]] L20 | Merge into one state |
| 5 | It says whether work is active or queued | Tasks sit in it with nothing happening, and the board cannot say so | [[wester-board-design]] L40 | [[active-versus-queued]] |
| 6 | Work actually uses it | History shows a kind of task routinely skipping it | [[kanban-playbook-workflow-states]] L35 | Decide whether that kind has a different path ([[started-and-finished-points]]) |

The Wester sign for criterion 1 is stated as a question: "Do the column names of your board sound like the titles of the people in your team?" (L22). The same line asks whether people often work in just one column. This wiki leaves that out, since it concerns individual assignment.

A column can pass every criterion and still have no written exit condition, which is the separate rule on [[column-doneness-criteria]].

Criterion 6 goes beyond its source. The Playbook only reports that a bug fix skipped a step, and the reading of that as a test is ours.

### Across the board

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

### Reading the result

The criteria are not all equal. Criteria 2, 3 and 9 are the ones that break the numbers, because they decide what is counted and when, so this wiki treats a failure there as a defect to fix. The others cost readability and can wait. A board for a few people should not add states to pass criterion 5 or 7 unless tasks are actually sitting there. This weighting is ours.

The criteria pull against each other. Criterion 5 and the handoff in criterion 7 add states, and criterion 4 removes them. The Playbook warns about "too many states" (L20), and Wester warns that with "too much granularity, team members can be confused" (L30). The resolution is the same in each case: add a state only where history shows tasks there.

### What practitioners report

The interviews behind [[montgomery-tracker-smells]] come from outside the Kanban school, so they are a second voice on three of these criteria. They add signs and no new criterion. They are perceptions from mostly large organisations, with no thresholds.

| Problem | Participants | Sign | Criterion |
|---|---|---|---|
| Lack of a Fitting Workflow | 17 (L423) | People work around the states. P26: "you have to cheat the process to make it work for these 10%". On a board this wiki reads it as tasks that pass through states in no time | 6, 7 |
| Workflow Bloat | 14 (L427) | P17: "fitting yourself into the workflow, instead of just doing the work" | 4 |
| Unclear Workflow | 5 (L431) | P05: "what does ‘resolved’ actually mean?" | 3, 9 |

P26's 90 and 10 percent are a way of speaking and not a measurement. The authors' reading of the first two problems is "a complex and nuanced trade-off within these systems between too much and too little support workflow options." (L421), which agrees with the tension between criteria described above. The study's "Too many issue types" (L160) is the same complaint about types, and its text gives no result. How many is too many is not stated, and the study does not establish that any of these harmed a project ([[smell-is-not-a-finding]]).

### Which holds under which setup

The criteria do not depend on the methodology, since each guide leaves column design open and neither disagrees with them. An iteration setup does add one rule of its own: a task that returns at a period's end is not a failure of criterion 8 ([[backward-movement]]).

### Agent executor note

The criteria concern the board and survive. Criterion 1 needs one addition, which is that a column named after the executor fails for the same reason as one named after a job title, since it records who holds the task and not what stage it has reached. Criterion 3's sign relies on a reader, and the plugin can be that reader. Wester's and the Playbook's reason for it, confusion among people, does not apply to an agent. What applies is the count, which goes wrong whoever is confused.

## Iteration Task Board

Cohn's task board is the layout he recommends for tracking one iteration. He gives it two jobs: "a convenient mechanism for organizing their work and a way of seeing at a glance how much work is left" ([[cohn-agile-estimating-planning]] L4457). It has one row per story and a fixed set of columns, shown in his Figure 20.1 (L4470). This section records that layout and classifies each column, because the columns mix several different kinds of thing under one word.

### Levels

Cohn's cards are a level below this wiki's task. His story is this wiki's task, and his task card is the piece of a story that the plugin does not produce ([[unit-of-work]]). So the row is the unit a board in this wiki tracks, and the cards inside it move across the columns. Applying these columns to whole tasks is this wiki's transfer, and Cohn does not make it.

### The columns, classified

The left column below is Cohn's. The classification is this wiki's, using [[column-versus-attribute]].

| Cohn's column | What he says it holds | Classification here |
|---|---|---|
| Story | The story card with its point estimate (L4465) | Row label, not a state |
| To Do | Task cards, each showing "the estimate of the work remaining to complete the task" (L4474) | Queued state |
| Tests Ready | A checkmark once the story's high-level tests are specified (L4482) | Marker on the row, not a stage cards pass through. See [[testable-acceptance]] |
| In Process | "cards that developers have signed up for" (L4484) | Active state |
| To Verify | A card awaiting "a fresh pair of eyes", when there is no test card (L4486) | Optional handoff: predictable place, goes forward afterwards |
| Done | Optional: a finished card "is removed from the task board" or moved to a Done column (L4486) | The finished point, if it is kept |
| Hours | The sum of hours remaining for the row (L4488) | Computed value, not a state. It feeds the [[iteration-burndown]] |

Two things this wiki takes from that classification:

- **Column does not mean state in this layout.** Only To Do and In Process are always stages. A check of a board against this layout should compare stages to stages, per *Judging a Board's Columns* (above), and not count columns.
- **Removing finished cards loses the finished point.** Cohn allows it because a paper board needs only the work left. This wiki reads that as unsafe for a board whose history is read later, since a task that leaves the board has no recorded crossing of [[started-and-finished-points]].

### To Verify: the discriminating criterion

Cohn separates two ways of checking finished work. Where a test card was written at planning, the finished programming card leaves and someone signs up for the test card. Where no test card exists, or a developer "would like a fresh pair of eyes to take a quick, verifying look", the card goes to To Verify (L4486). He says the column is one "that you may or may not need" and finds it useful "especially when working with a team that is learning how to become agile" (L4486).

This wiki reads the split as a question of whether the check is planned work or a handoff. At this wiki's level a test is part of the task's result and not a separate unit, so the first route does not transfer: the plugin does not produce a code card and a test card for one result ([[component-task-masquerading]]).

### What the board requires

Cohn requires flexibility of the board, not a form: it must "allow the team a great deal of flexibility in how they organize their work" (L4457), and that is what makes [[tasks-are-not-assigned-at-planning]] visible. He also admits equivalents, writing of the board "(or something equivalent to it)" (L4457). The physical details he gives are a matter of medium and this wiki drops them.

### Agent executor note

The classification concerns the work and survives. In the To Verify row, "a fresh pair of eyes" maps onto review by the person steering, which [[column-versus-attribute]] already treats as a handoff that takes a column. For an agent's output this wiki reads that column as required and not optional, because the executor cannot be the only check on its own result. That reading is this wiki's, and Cohn's reason for the column is about teams learning a habit.
