---
name: tend-board
description: >-
  Checks an area of the board against the plugin's knowledge base one dimension at a time: stuck
  work, WIP over the limit, acceptance criteria, duplicates, status mapping, unit of work,
  unwritten decisions, contradicting links. Use when asked whether the board is in order, or to
  tidy or audit it. Not for untriaged items: triage.
argument-hint: "[scope: board | sprint:<name> | label:<name> | parent:<id>] [dimensions; default: all]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# tend-board

Check the board one dimension at a time, each judged by its own `task-master:board-inspector` so
none crowds out another. You prepare their files, merge and relay. Nothing is written to the board.

## Process

Plugin root: `${CLAUDE_PLUGIN_ROOT}`. Follow `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`
with `<skill>` = `tend-board` and these specifics:

1. **Settings.** No board: a snapshot the caller hands over is checked in its place, as composed
   and with no history; otherwise stop.
2. **Scope and dimensions.** The scope as given, in the `board` method's form; none, the whole
   board, recorded in `assumptions`. The dimensions named, else every row of `dimensions/README.md`;
   an unknown name goes to `not_covered`; one whose data step 1 found unavailable is skipped with
   that reason.
3. **Snapshot.** One snapshot of the scope, open and finished tasks; history only for started tasks
   (age) and finished ones (cycle time).
4. **Metrics.** Once, for every dimension:
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/tend-board-snapshot.json --settings <settings> --out .task-master/tend-board-metrics.json`
5. **Question.** One per dimension, at `.task-master/tend-board-q-<dimension>.md`: the dimension,
   the scope, `[process].doc` (absent or not found: say which, and that nothing counts as declared
   intended), the changeset path `.task-master/changeset-tend-board-<dimension>.json` with refs
   `<dimension>-<n>`. Record the tool's link type for each of `blocks`, `duplicates`, `relates`, or
   `none`; a relation the tool records in one direction only is listed once.
6. **Dispatch** the inspectors in parallel, in one message, one per dimension, each with its own
   question, then `${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/README.md` and
   `${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/<dimension>.md`, in that order.
7. **Merge the envelopes.**
   - `status`: the worst of theirs (blocked, then partial, then done). `findings` by dimension; a
     task two dimensions report on one sign stays under the owner the README names, noting the other.
   - Merge the changeset files that exist into `.task-master/changeset-tend-board-<scope>.json`
     (scope slugged as the `board` method says), dropping an op identical (same `op`, task and
     values) to one from the owning dimension.
   - List each dimension with no findings and its examined count, and each skipped one with its
     reason. Union the rest.
   - Over about 150 lines: write `.task-master/tend-board-result.md`; return the path and a short
     summary per dimension.
8. **Relay** the merged result. Closing a duplicate or stale task is the person's decision at the
   apply; a re-cut goes to `decompose`.

## Reference files

- `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`: the shared run, step by step.
- `dimensions/README.md`: the dimensions, what each owns, and what all share.
