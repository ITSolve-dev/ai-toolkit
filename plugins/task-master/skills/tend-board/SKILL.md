---
name: tend-board
description: >-
  Checks an area of the board (a sprint, a label, an epic, or the whole board) against the
  plugin's knowledge base, one dimension at a time: stuck tasks, work in progress over the limit,
  tasks without acceptance criteria, duplicates, statuses that do not match the mapping, tasks that
  fail the two tests of a unit of work, decisions left out of the text, and contradicting links.
  Returns the findings for each dimension with a cited page and the proposed changes. On a board
  in order it returns no findings. Use when someone asks whether the board is in order, asks to
  tidy or audit it, or wants to check it against the process. Questions about the rules go to ask;
  re-cutting a task goes to decompose, sizes to estimate, the timeline to schedule; applying the
  proposals goes to board.
argument-hint: "[scope: board | sprint:<name> | label:<name> | parent:<id>] [dimensions; default: all]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# tend-board

Runs in your context and writes nothing to the board. Each dimension is judged by its own
`task-master:board-inspector`, so no dimension crowds out another; you prepare their files, then
merge and relay what they return. The dimensions and what each needs are listed in
`${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/README.md`.

1. **Read `.claude/task-master.toml`** (format: `${CLAUDE_PLUGIN_ROOT}/skills/init/config-format.md`).
   Absent: say the board is not set up and point to `init`. A snapshot the caller hands over, with
   its state mapping, is checked in its place, as composed and with no history; otherwise stop.
2. **Pick the scope and the dimensions.** The scope as given, in the form of the `board` method;
   none given, the whole board, recorded in `assumptions`. The dimensions named, else every row of
   the README. An unknown name goes to `not_covered`. A dimension whose README row needs data the
   config records as unavailable is skipped with that reason, and not dispatched.
3. **Take one snapshot** of the scope, open and finished tasks, by
   `${CLAUDE_PLUGIN_ROOT}/skills/board/method.md`, *Before any job* and *Reads and the snapshot*,
   to `.task-master/tend-board-snapshot.json`.
4. **Compute the arithmetic once**:
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/tend-board-snapshot.json --config .claude/task-master.toml --out .task-master/tend-board-metrics.json`.
5. **Write one question per dimension** to `.task-master/tend-board-q-<dimension>.md`: the
   dimension, the scope, the config path, `[project].process_doc` (absent, or named but not found:
   say which, and that nothing counts as declared intended), and the changeset path
   `.task-master/changeset-tend-board-<dimension>.json`, refs `<dimension>-<n>`.
6. **Dispatch the inspectors in parallel**, in one message, one per dimension, each with the
   snapshot, the metrics, its question, and two method paths in this order:
   `${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/README.md` and
   `${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/<dimension>.md`.
7. **Merge the envelopes.** `status` is the worst of theirs: blocked, then partial, then done. In
   `findings`, grouped by dimension, one per task per dimension. Where two dimensions report one
   task on the same sign, keep it under the dimension the README says owns it and note the other.
   Merge the changeset files that exist (a dimension with no ops writes none) into
   `.task-master/changeset-tend-board-<scope>.json`, dropping an op identical (same `op`, task and
   values) to one from the owning dimension. List every dimension that ran with no findings, with
   how many tasks it examined, and every skipped one with its reason. Union the other parts, and
   add the snapshot reply's caveats to `assumptions`. Over about 150 lines: write it to
   `.task-master/tend-board-result.md` and return the path and a short summary per dimension.
8. **Relay it** in the shape of the `board` method, *The reply*. Closing a duplicate or a stale
   task is the person's decision at the apply; a re-cut goes to `decompose`.
