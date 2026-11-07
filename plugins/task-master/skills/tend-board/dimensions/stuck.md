# Dimension: stuck

Which started task has stopped or outlived its expectation, and nobody has acted on it? Read
`README.md`, *Every dimension*, first.

**Reads:** started tasks, those `age.items` marks `started` (kinds `active`, `handed_off`, and
`queued` where `[process.wip]` limits it: `wip.started_statuses`); their `markers`, `subtasks`;
`age.items` (`work_item_age_days` with its `work_item_age_basis` and `work_item_age_reason`;
`days` with its `basis`); `cycle_time.percentiles`, where not null.

## Steps

1. **Fix the age and say its basis.** Step 3 reads `work_item_age_days`, Work Item Age from the
   started point (basis `transitions` or `started_at`). Where it is null, its `work_item_age_reason`
   says why; then `days` stands in, named by its `basis`: `exact` is time in the current status, not
   Work Item Age, so an age under the line does not clear a task that changed status recently;
   `since_created` overstates age, so an age over the line does not show a stop, and the finding
   says so (`${CLAUDE_PLUGIN_ROOT}/skills/board/method.md`, Before any job: history). `unknown`: the task cannot be aged; list it
   under `not_covered` (`wiki/reading-history/work-item-age.md`, What an audit needs).
   *Output:* one line naming the basis. *Wrong if:* an approximate age is called Work Item Age.
2. **Fix the line by setup** (`wiki/moving-work/board-rules-by-setup.md`, the expectation for a
   task's life). `[process].sle` set (flow, or iterations keeping one): it wins over `period_days`;
   its days are the metrics' `sle.days`, never parsed from the settings string. No SLE, under
   iterations: `[process].period_days`. Neither: no age line; run steps 4-5 only and name the
   missing inputs under `not_covered`. The checkpoint is the 70th percentile of finished work's
   cycle time, `cycle_time.percentiles."70"`, with its `n` and each item's `start_source`; null, name it missing
   with `percentile_reasons`, never estimate it (`wiki/moving-work/percentile-intervention-triggers.md`).
   *Output:* the line and the checkpoint, in days, with their sources.
3. **Age over the line.** A task whose age (step 1) exceeds the line, with no blocked or waiting
   marker and no subtasks: finding. Under the line but past the checkpoint: a question, not a
   finding, so it is asked before the line is reached
   (`wiki/moving-work/percentile-intervention-triggers.md`, The procedure). Comments are not in the
   snapshot, so whether anyone acted in them is the question, not the finding. Past an 85th-percentile SLE the question is why
   nobody intervened earlier (`wiki/moving-work/percentile-intervention-triggers.md`, Signs).
4. **Read state before size** for each task from step 3, and for each task marked blocked or
   waiting (`wiki/moving-work/percentile-intervention-triggers.md`, Which question comes first):
   - marked blocked: the project's blocked-work policy applies. A blocked task past the age the
     process document sets for leaving, with no decision recorded, is a finding; no stated policy
     is one board-level question, not one per task (`wiki/moving-work/blocked-work-counts-against-wip.md`,
     Policies for blocked work);
   - marked waiting: waiting needs an outside party and an expected end. Past that end it is
     blocked; no end readable in the task means the test cannot run, which is the question
     (`wiki/work-states/waiting-versus-blocked.md`, The test);
   - `handed_off`: a result waiting for a person; ask that it be reviewed before new work starts;
   - `queued`, where started: committed and not moving; ask what keeps it from being pulled, since
     a long wait past the started point suggests the point sits early or too much was committed
     (`wiki/work-states/started-and-finished-points.md`, Sign of violation);
   - `active`, no marker: size or missing information; propose asking whether to re-cut, through
     `decompose` (`wiki/sizing/hidden-wip-in-large-items.md`).
   Where `[process].executor` is `agent` or `mixed`, ask the blocker question first: a stop for a person's decision is
   blocked, not waiting (`wiki/work-states/waiting-versus-blocked.md`, Agent executor note).
5. **Propose** a comment asking the question of step 4. Blocked or waiting cannot be told from the
   snapshot, so no `add_label` for either: on a stopped task with no marker the comment asks what
   it waits on and who acts, and names the marker each answer sets, by its label in `marker_specs`: waiting for an
   outside party with an expected end, blocked otherwise (`wiki/work-states/waiting-versus-blocked.md`,
   The test). Never a move out of the state: a blocked task stays and counts
   (`wiki/moving-work/blocked-work-counts-against-wip.md`, The rule).

## Not a finding

- A task not started (kinds above): it has no age before the start
  (`wiki/reading-history/work-item-age.md`, What it covers). Old unstarted items are triage's.
- A finished task, or one under the line.
- A task marked blocked or waiting that is inside the project's stated policy: the marker is the
  rule being followed, not broken.
- Age alone as a cause: age measures size and waiting together and names neither
  (`wiki/reading-history/work-item-age.md`, What it does not say).
- How many tasks are in a state: that is `wip-limit`.
