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
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# triage

Runs in your context and writes nothing to the board. The judgement happens in
`task-master:board-inspector`; you prepare its files and relay its result.

1. **Read `.claude/task-master.toml`** (format: `${CLAUDE_PLUGIN_ROOT}/skills/init/config-format.md`).
   Absent: say the board is not set up and point to `init`. Items passed as text are still triaged
   on what needs no board: write them to `.task-master/triage-items.md`, pass that file in place of
   the snapshot and `none` for the metrics, and state in the result that duplicates on the board,
   staleness and every write were not checked. No config and no items: stop there.
2. **Take a snapshot** of scope `board`, open and closed items, by
   `${CLAUDE_PLUGIN_ROOT}/skills/board/method.md`, *Before any job* and *Reads and the snapshot*,
   to `.task-master/triage-snapshot.json`. The whole board, because a duplicate is searched for
   among closed items too (`wiki/intake/duplicate-reports.md`).
3. **Compute the arithmetic**:
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/triage-snapshot.json --config .claude/task-master.toml --out .task-master/triage-metrics.json`.
4. **Write the question** to `.task-master/triage-question.md`: which items to triage (the text
   items, or "the board's untriaged items"), the path of `.claude/task-master.toml`, and who the
   requests come from if you know (the person steering, or others).
5. **Dispatch `task-master:board-inspector`** with four absolute paths (`${CLAUDE_PLUGIN_ROOT}`
   expanded, `.task-master/` resolved in the project): snapshot, metrics, question, and
   `${CLAUDE_PLUGIN_ROOT}/skills/triage/method.md`.
6. **Relay its envelope** in the shape of the `board` method, *The reply*, with step 1's fallback
   and the caveat lines *Reads and the snapshot* produced added to `assumptions`: the `findings` per item, then the
   changeset. Items sized as needing cutting go to `decompose`.
