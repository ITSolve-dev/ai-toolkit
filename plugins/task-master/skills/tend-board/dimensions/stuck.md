# Dimension: stuck

Which started task has stopped or outlived its expectation, and nobody has acted on it? Read
`README.md`, *Every dimension*, first.

**Reads:** tasks of a kind in `[project].started_kinds` (absent: `active`, `handed_off`); their
`markers`; `age.items` with each `basis`; cycle-time percentiles, where the metrics carry them.

## Steps

1. **Fix the basis and say it.** `exact` is time in the current status, from the tool's history:
   it is not Work Item Age, which runs from the started point, so an age under the line does not
   clear a task that changed status recently. An age the metrics give from `started_at` is Work
   Item Age, and step 3 reads that one. `since_created` overstates age, so an age over the
   line does not show a stop: a stuck task cannot be told from a long-open one, and the finding
   says so (design table "Чего инструмент не умеет"). `unknown`: the task cannot be aged; list it
   under `not_covered` (`wiki/reading-history/work-item-age.md`, What an audit needs).
   *Output:* one line naming the basis. *Wrong if:* an approximate age is called time in state.
2. **Fix the line by setup** (`wiki/moving-work/board-rules-by-setup.md`, the expectation for a
   task's life). Flow, or iterations keeping one: the days of `[project].sle`. Iterations without
   one: `[project].period_days`. Neither: no age line; run steps 4-5 only and name the missing
   inputs under `not_covered`. The 50th and 70th percentile checkpoints need cycle-time
   percentiles of finished work: take them from the metrics; absent there, name them as missing,
   never estimate them (`wiki/moving-work/percentile-intervention-triggers.md`).
   *Output:* the line, in days, with its source.
3. **Age over the line.** A task whose `age.items[].days` exceeds the line, with nothing on it
   since (no blocker marked, no split): finding. Past an 85th-percentile SLE the question is why
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
   With an agent executing, ask the blocker question first: a stop for a person's decision is
   blocked, not waiting (`wiki/work-states/waiting-versus-blocked.md`, Agent executor note).
5. **Propose.** A marker where a stopped task carries none; a comment asking the question of step 4.
   Never a move out of the state: a blocked task stays and counts
   (`wiki/moving-work/blocked-work-counts-against-wip.md`, The rule).

## Not a finding

- A task of a kind outside `started_kinds`: it has no age before the start
  (`wiki/reading-history/work-item-age.md`, What it covers). Old unstarted items are triage's.
- A finished task, or one under the line.
- A task marked blocked or waiting that is inside the project's stated policy: the marker is the
  rule being followed, not broken.
- Age alone as a cause: age measures size and waiting together and names neither
  (`wiki/reading-history/work-item-age.md`, What it does not say).
- How many tasks are in a state: that is `wip-limit`.
