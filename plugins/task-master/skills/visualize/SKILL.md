---
name: visualize
description: >-
  Answer one question about a board or a period with a chart chosen for that question: a Mermaid
  file under .task-master/ and a short text reading, each saying what the chart cannot answer.
  Burndowns, velocity, a feature Gantt, a cumulative flow diagram, a cycle time scatterplot or
  histogram, an aging view: the choice comes from the plugin's knowledge base, and a chart the
  board's history cannot support is refused with the reason. Use when someone asks to see progress,
  flow, how long work takes or what is planned where, or asks for a chart for a team or a client.
  A question about which chart fits goes to ask; a review of a past period to review-period;
  publishing the chart is left to the caller.
argument-hint: "<the question the chart should answer> [tasks, a period or a window] [who will read it]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python*${CLAUDE_PLUGIN_ROOT}/scripts/*)
---

# visualize

Runs in your context: you read the board and run the arithmetic; `task-master:board-inspector`
chooses and draws the chart, in its own.

1. **Take the question.** A chart is chosen by the question it answers, so a request naming only an
   occasion ("for the demo", "show the board") returns a question asking what the reader wants to
   learn. A request naming a chart is passed on as it is; the method maps it to its question.
2. **Read `.claude/task-master.toml`.** Absent: say the board is not set up and point to `init`.
   Continue only on a snapshot or figures the caller passed; otherwise stop there. Note
   `[project].setup`, `period_days`, `sle`, `started_kinds`, `[fields].theme` (optional) and
   `[board.capabilities]`.
3. **Snapshot** the scope the question names (a period's tasks, a release, the whole board) by the
   procedure in `${CLAUDE_PLUGIN_ROOT}/skills/board/method.md` (*Before any job*, step 2, and
   *Reads and the snapshot*), to `.task-master/visualize-snapshot.json`.
4. **Metrics:** run `${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py` with python on the snapshot and
   the config, output to `.task-master/visualize-metrics.json`. The chart's numbers come from here.
5. **Write the question** to `.task-master/visualize-question.md`: the question as asked; the scope
   and its dates; the reader, the people steering or someone outside the project (unstated: the
   people steering, recorded as assumed); setup, `period_days`, `sle`, `started_kinds`, the theme
   field (absent: say so); every capability not `native`.
6. **Dispatch `task-master:board-inspector`** with four paths: the snapshot, the metrics, the
   question, and `${CLAUDE_PLUGIN_ROOT}/skills/visualize/method.md`.
7. **Relay its result**: from `findings`, the chart's path and the reading, or the refusal. Add to
   `assumptions` each fallback taken here and its cost; a composed snapshot is not atomic. The
   plugin has no means of publishing, so publishing stays in `needs_caller`.
