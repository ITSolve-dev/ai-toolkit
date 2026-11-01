---
title: Distinguishable Work States
category: work-states
summary: The sources give criteria and no canonical column set, and they treat a fixed list as the failure case; what they do support is a small set of distinctions any board must let a reader make, drawn partly as columns and partly as markers.
tags: [concept, work-states, board-design]
sources: [kanban-guide, scrum-guide-2020, wester-board-design, kanban-playbook-workflow-states, radzikowska-waiting-blocked, kubernetes-issue-triage]
created: 2026-11-01
updated: 2026-11-01
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

This wiki reads that as giving the plugin a classification rather than a column list. Each column of any board maps to one of five kinds: before the started point, queued, active, handed off, or past the finished point. Two markers then sit on tasks: blocked and waiting. The classification is this wiki's, and it is what [[judging-board-columns]] audits against.

This classification would be shown wrong by a column that fits none of the five kinds and yet passes every criterion, or by a real board whose tasks could not be told apart with it. Nothing has tested it on a real board, since the boards for that check are held out and do not yet exist.

## One distinction before the started point

The table says nothing about work before it starts, and [[kubernetes-issue-triage]] adds a line there: an item is either awaiting triage or accepted, shown by a label that triage replaces (L152). This wiki reads that as one more distinction inside the kind "before the started point": has anyone looked at this? It can be drawn as a marker or a column, and [[triage-procedure]] depends on it. Without it, an item nobody has read looks like one that is ready.

## Agent executor note

The distinctions concern the work and survive. The handoff row gains weight, since nearly every agent-run task ends with a person reviewing it. The active row becomes easier to check, because a run either exists or does not.
