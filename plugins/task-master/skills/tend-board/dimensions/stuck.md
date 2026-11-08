# Dimension: stuck

## What it looks for

A started task that has stopped, or outlived its expectation, with nobody acting on it.

**Scope:** tasks `age.items` marks `started` (kinds `active`, `handed_off`, and `queued` where
`[process.wip]` limits it: `wip.started_statuses`); their `markers` and `subtasks`.

**The age.** Use `work_item_age_days` (Work Item Age from the started point). Where it is null, its
`work_item_age_reason` says why, and `days` stands in, named by its `basis`:

- `exact` is time in the current status, not Work Item Age: an age under the line does not clear a
  task that changed status recently.
- `since_created` overstates age: an age over the line does not show a stop.
- `unknown`: the task cannot be aged; list it under `not_covered`.

**The line.** `[process].sle` set: the metrics' `sle.days` (never parsed from the settings string),
which wins over `period_days`. No SLE, under iterations: `[process].period_days`. Neither: no age
line; check stop markers only and name the missing inputs under `not_covered`. **The checkpoint** is
`cycle_time.percentiles."70"`, with its `n` and each item's `start_source`; null, name it missing
with `percentile_reasons`, never estimate it.

## Read

- `wiki/reading-history/work-item-age.md` — What it covers (no age before the start), What it does
  not say (age names neither size nor waiting), What an audit needs.
- `wiki/moving-work/board-rules-by-setup.md` — which expectation applies under which setup.
- `wiki/moving-work/percentile-intervention-triggers.md` — The procedure (a question at the
  checkpoint, before the line), Signs (past an 85th-percentile SLE, why nobody intervened), and
  Which question comes first (read state before size).
- `wiki/moving-work/blocked-work-counts-against-wip.md`, Policies for blocked work — a blocked task
  past the age the project sets for leaving, with no decision, is a sign; no stated policy is one
  board-level question.
- `wiki/work-states/waiting-versus-blocked.md`, The test and the Agent executor note — waiting needs
  an outside party and an expected end; a stop for a person's decision is blocked.
- `wiki/work-states/started-and-finished-points.md`, Sign of violation — a `queued` task past the
  started point and not moving.
- `wiki/sizing/hidden-wip-in-large-items.md` — an `active` task with no marker: size or missing
  information.

## Not a finding

- A task not started: old unstarted items are triage's.
- A finished task, or one under the line and before the checkpoint.
- A task marked blocked or waiting inside the project's stated policy: the marker is the rule being
  followed.
- Age alone as a cause.
- How many tasks are in a state: that is `wip-limit`.

## Finding shape

Open with one line naming the age basis, the line and the checkpoint in days with their sources.
Then the common shape (README) per task: over the line with no blocked or waiting marker and no
subtasks is a finding; past the checkpoint but under the line is a question. Comments are not in
the snapshot, so whether anyone acted is part of the question.

Propose a `comment` asking the state-before-size question the pages give for the task's state.
Where `[process].executor` is `agent` or `mixed`, ask the blocker question first: a stop for a
person's decision is blocked, not waiting (waiting-versus-blocked, Agent executor note). The
snapshot cannot tell blocked from waiting, so add no marker: on a stopped task with no marker, the
comment asks what it waits on and who acts, naming the marker each answer sets (its label in
`marker_specs`). Never a move out of the state: a blocked task stays and counts. An `active` task
read as too large: name `decompose`.
