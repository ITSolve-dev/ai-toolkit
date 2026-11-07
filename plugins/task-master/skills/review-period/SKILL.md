---
name: review-period
description: >-
  Review a past iteration or a window of continuous flow against what was promised at its start:
  the selection and goal against what finished, unfinished work and its likely cause, velocity or
  throughput, cycle time, age and SLE hits, and the forces behind any gap, read from the project's
  board and grounded in the plugin's knowledge base. Says plainly which comparisons the board's
  history cannot support. Use when someone asks how the last sprint went, what became of the plan,
  why a release finished late, or for a retrospective in figures. A question about how to read such
  figures goes to ask; what comes next goes to schedule; changes it proposes are applied by board.
argument-hint: "<period name, or a window's start and end> [snapshot taken at its start] [goal, communicated date or forecast]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# review-period

Runs in your context: you read the board and run the arithmetic; `task-master:board-inspector`
does the judging, in its own.

1. **Read `.claude/task-master.toml`.** Absent: say the board is not set up and point to `init`.
   Continue only on a snapshot the caller passed; otherwise stop there. Note `[project].setup`,
   `period_days`, `commitment`, `sle`, `started_kinds`, `process_doc` and `[board.capabilities]`.
2. **Name the period.** Iterations: the sprint the input names; none named, the latest closed one
   from the recorded `sprints` command, or a question when `sprints = "caller"`. Flow: a window with
   both dates from the input; none, return a question, because the window decides every figure.
3. **Decide what can be compared, before reading.** What was promised at the start is known only
   from `history = "native"` or from a snapshot the caller passes, taken no later than the period's
   first day. Neither: the plan-against-fact table, scope and estimate changes, and the
   delay-or-slip test are not made. Today's membership of the period is never offered as its plan:
   work added since the start would read as planned, and work removed would vanish.
4. **Snapshot** the period's tasks, scope `sprint:<name>` (flow: `board`, since finishing in a
   window is not a filter the board offers), by `${CLAUDE_PLUGIN_ROOT}/skills/board/method.md`,
   *Before any job* and *Reads and the snapshot*, to `.task-master/review-period-snapshot.json`.
5. **Metrics**, with `<start>` and `<end>` the period's dates (a sprint's own dates under iterations):
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/review-period-snapshot.json --config .claude/task-master.toml --window-start <start> --window-end <end> [--sprint "<name>"] [--age-at <end>] [--compare <earlier snapshot>] --out .task-master/review-period-metrics.json`.
   `--sprint` under iterations. `--age-at` under flow, and only when `<end>` is not after the
   snapshot's read time. `--compare` with an earlier snapshot taken with the same scope: another
   scope makes the comparison refuse.
6. **Write the question** to `.task-master/review-period-question.md`: what the caller asked; the
   period and its dates; setup, `period_days`, `commitment`, `sle`, `process_doc`; every
   capability not `native`;
   the earlier snapshot and its metrics, if any; any goal, communicated date or forecast passed; and
   what step 3 ruled out.
7. **Dispatch `task-master:board-inspector`** with four paths: the snapshot, the metrics, the
   question, and `${CLAUDE_PLUGIN_ROOT}/skills/review-period/method.md`.
8. **Relay its result** in the shape of the `board` method, *The reply*, with the snapshot reply's
   caveats added to `assumptions`. Nothing is written to the board here.
