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
argument-hint: "[scope: sprint, label, parent or 'board'] [dimensions; default: all]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python*${CLAUDE_PLUGIN_ROOT}/scripts/*)
---

# tend-board

Runs in your context and writes nothing to the board. Each dimension is judged by its own
`task-master:board-inspector`, so no dimension crowds out another; you prepare their files, then
merge and relay what they return. The dimensions and what each needs are listed in
`${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/README.md`.

1. **Read `.claude/task-master.toml`** (format: `${CLAUDE_PLUGIN_ROOT}/skills/init/config-format.md`).
   Absent: say the board is not set up and point to `init`. A snapshot the caller hands over, with
   its state mapping, is checked in its place, as composed and with no history; otherwise stop.
2. **Pick the dimensions**: those named, else every row of the README. An unknown name goes to
   `not_covered`. A dimension whose README row needs data the config records as unavailable is
   skipped with that reason, and not dispatched.
3. **Take one snapshot** of the scope, open and finished tasks, by the `board` skill's snapshot
   procedure, to `.task-master/tend-board-snapshot.json`. Where `[board.capabilities].snapshot`
   is not `native`, it is composed from reads: record that it is not atomic.
4. **Compute the arithmetic once**: run `${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py` over the
   snapshot with `--config .claude/task-master.toml`, output to `.task-master/tend-board-metrics.json`.
   Where `[board.capabilities].history` is `none`, ages run from creation: record that a task
   stuck in a state cannot be told from one long open.
5. **Write one question per dimension** to `.task-master/tend-board-q-<dimension>.md`: the
   dimension, the scope, the config path, and `[project].process_doc` (absent: say none was found,
   so nothing counts as declared intended).
6. **Dispatch the inspectors in parallel**, in one message, one per dimension, each with four paths:
   the snapshot, the metrics, its question, and
   `${CLAUDE_PLUGIN_ROOT}/skills/tend-board/dimensions/<dimension>.md`.
7. **Merge the envelopes.** `status` is the worst of theirs. In `changeset`, findings grouped by
   dimension, one per task per dimension. Where two dimensions report one task on the same sign or
   propose the same change, keep it under the dimension the README says owns it and note the
   other. List every dimension that ran with no findings as such, with how many tasks it examined,
   and every skipped one with its reason. Union the other parts; add steps 1-4's fallbacks to
   `assumptions`. Over about 150 lines: write it to `.task-master/tend-board-result.md` and return
   the path and a short summary per dimension.
8. **Relay it.** The `changeset` is a proposal, applied through the `board` skill, one by one where
   `[board.capabilities].batch` is not `native`. Closing a duplicate or a stale task is the person's
   decision at that point; a re-cut goes to `decompose`.
