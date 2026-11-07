---
name: triage
description: >-
  Triages incoming, unread items: checks and clarifies each, classifies it, proposes a priority and
  a size class, proposes duplicates and what no longer applies for closing, and drafts the comments
  that ask reporters for missing facts, each with its reason and a page of the plugin's knowledge
  base. Use when the board's untriaged items need reading, when someone hands over new requests or
  bug reports to sort, or when a board has piled up unread work. It does not cut tasks: an item too
  big for one unit gets the size that says so, and decompose takes it from there. Questions about
  triage go to ask; estimating or scheduling known tasks to estimate and schedule; applying the
  proposed changes to board.
argument-hint: "[items as text or a file path; default: the board's untriaged items]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python*${CLAUDE_PLUGIN_ROOT}/scripts/*)
---

# triage

Runs in your context and writes nothing to the board. The judgement happens in
`task-master:board-inspector`; you prepare its files and relay its result.

1. **Read `.claude/task-master.toml`** (format: `${CLAUDE_PLUGIN_ROOT}/skills/init/config-format.md`).
   Absent: say the board is not set up and point to `init`. Items passed as text are still triaged
   on what needs no board: write them to `.task-master/triage-items.md`, pass that file in place of
   the snapshot and `none` for the metrics, and state in the result that duplicates on the board,
   staleness and every write were not checked. No config and no items: stop there.
2. **Take a snapshot** of the whole board, open and closed items, by the `board` skill's snapshot
   procedure, to `.task-master/triage-snapshot.json`. The whole board, because a duplicate is
   searched for among closed items too (`wiki/intake/duplicate-reports.md`). Where
   `[board.capabilities].snapshot` is not `native`, the procedure composes it from reads: record in
   the result that it is not atomic.
3. **Compute the arithmetic**: run `${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py` over the snapshot
   (its `--help` gives the arguments), output to `.task-master/triage-metrics.json`. Where
   `[board.capabilities].history` is `none`, ages run from creation: record in the result that a
   long-stalled item cannot be told from a long-open one.
4. **Write the question** to `.task-master/triage-question.md`: which items to triage (the text
   items, or "the board's untriaged items"), the path of `.claude/task-master.toml`, and who the
   requests come from if you know (the person steering, or others).
5. **Dispatch `task-master:board-inspector`** with four paths: snapshot, metrics, question, and
   `${CLAUDE_PLUGIN_ROOT}/skills/triage/method.md`.
6. **Relay its envelope** with the fallbacks from steps 1-3 added to `assumptions`. The `changeset`
   is a proposal: say it is applied through the `board` skill, item by item where
   `[board.capabilities].batch` is not `native`, and that every closing is the person's decision at
   that point. Items sized as needing cutting go to `decompose`.
