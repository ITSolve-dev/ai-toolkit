---
name: review-period
description: >-
  Reviews a past iteration or flow window against what was promised at its start: plan against
  fact, unfinished work, velocity or throughput, cycle time and SLE hits, citing the knowledge
  base and saying which comparisons the history cannot support. Use when asked how the last sprint
  went or why a release finished late. Not for what comes next: schedule.
argument-hint: "<period name, or a window's start and end> [snapshot taken at its start] [goal, communicated date or forecast]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# review-period

Review a past period in figures: what was promised, what came out, and what explains the
difference. Nothing is written to the board.

## Process

Plugin root: `${CLAUDE_PLUGIN_ROOT}`. Follow `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`
with `<skill>` = `review-period` and these specifics:

1. **Settings.** No board: continue only on a snapshot the caller passed. Note `[process].setup`,
   `period_days`, `commitment`, `sle`, `doc`.
2. **Name the period.** Iterations: the sprint named; none, the latest closed one from the tool's
   sprints command, or a question if it lists none. Flow: a window with both dates; none, return a
   question, because the window decides every figure.
3. **Decide what can be compared, before reading.** The promise at the start is known only from the
   tool's history or a caller's snapshot taken by the period's first day. Neither: no
   plan-against-fact table, no scope or estimate changes, no delay-or-slip test. Never offer
   today's membership as the plan: work added since would read as planned, and work removed would
   vanish.
4. **Snapshot.** Scope `sprint:<name>`; under flow `board`, since finishing in a window is not a
   board filter.
5. **Metrics.** `<start>` and `<end>` are the period's dates:
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/review-period-snapshot.json --settings <settings> --window-start <start> --window-end <end> [--sprint "<name>"] [--age-at <end>] [--compare <earlier snapshot>] --out .task-master/review-period-metrics.json`
   - `--sprint` under iterations.
   - `--age-at` under flow, only when `<end>` is not after the snapshot's `taken_at`.
   - `--compare` with an earlier snapshot of the same scope; another scope refuses.
6. **Question.** What was asked; the period and dates; setup, `period_days`, `commitment`, `sle`,
   `doc`; the earlier snapshot, if any; any goal, communicated date or forecast; what step 3 ruled
   out.
7. **Dispatch** with `${CLAUDE_PLUGIN_ROOT}/skills/review-period/method.md`.
8. **Relay** the review, conclusion first, with each comparison not made and why.

## Reference files

- `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`: the shared run, step by step.
- `method.md`: the inspector's procedure and the pages it reads.
