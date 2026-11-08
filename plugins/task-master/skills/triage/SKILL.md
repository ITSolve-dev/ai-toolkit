---
name: triage
description: >-
  Triages unread items against the plugin's knowledge base: an outcome, kind, priority and size
  class each, duplicates and stale items proposed for closing, questions to reporters, each citing
  a page. Use when the board's untriaged items need reading, or new requests or bug reports arrive
  to sort. Not for an audit of the existing board: tend-board.
argument-hint: "[items as text or a file path; default: the board's untriaged items]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# triage

Turn unread items into triaged ones. Nothing is cut here: an item too big for one unit gets the
size that says so, and `decompose` takes it from there. Nothing is written to the board.

## Process

Plugin root: `${CLAUDE_PLUGIN_ROOT}`. Follow `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`
with `<skill>` = `triage` and these specifics:

1. **Settings.** No board but items passed as text: triage them on what needs no board. Write them
   to `.task-master/triage-items.md`, pass that file for the snapshot and `none` for the metrics,
   and say duplicates on the board, staleness and writes were not checked. No board and no items:
   stop.
2. **Snapshot.** Scope `board`, open and closed items: duplicates are searched among closed too.
3. **Metrics.**
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/triage-snapshot.json --settings <settings> --out .task-master/triage-metrics.json`
4. **Question.** Which items (the text items, or "the board's untriaged items"); which plugin ops,
   link relations and close reasons the tool's help shows a way for (`assign` only if it does); who
   the requests come from, if known (the person steering, or others).
5. **Dispatch** with `${CLAUDE_PLUGIN_ROOT}/skills/triage/method.md`.
6. **Relay** findings per item, then the changeset. Each close, priority and type is the person's
   decision at the apply. Items sized as needing cutting go to `decompose`.

## Reference files

- `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`: the shared run, step by step.
- `method.md`: the inspector's procedure and the pages it reads.
