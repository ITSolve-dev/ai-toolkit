---
name: visualize
description: >-
  Answers one question about a board or a period with one chart the knowledge base picks: a
  Mermaid file under .task-master/ and a short reading of what it cannot answer; a chart the
  history cannot support is refused. Use when asked to see progress, flow, how long work takes or
  what is planned where. Not for a review of a past period: review-period.
argument-hint: "<the question the chart should answer> [tasks, a period or a window] [who will read it]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py *)
---

# visualize

Answer one question with one chart. The inspector chooses and draws it; nothing is written to the
board, and nothing is published.

## Process

Plugin root: `${CLAUDE_PLUGIN_ROOT}`. Follow `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`
with `<skill>` = `visualize` and these specifics:

1. **Take the question.** A request naming only an occasion ("for the demo", "show the board") gets
   a question back: what does the reader want to learn? A named chart is passed on as is.
2. **Settings.** No board: continue only on a snapshot or figures the caller passed. Note
   `[process].setup`, `period_days`, `sle`.
3. **Snapshot.** The scope the question names: `sprint:<name>`; `parent:<id>` or `label:<name>` for
   a release; or `board`.
4. **Metrics.** Every number in the chart comes from here:
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/board_metrics.py .task-master/visualize-snapshot.json --settings <settings> [--window-start <start> --window-end <end>] [--sprint "<name>"] [--compare <earlier snapshot>] --out .task-master/visualize-metrics.json`
   - A window for a span of time.
   - `--sprint` for an iteration burndown.
   - `--compare` for a release burndown, with the caller's snapshot of an earlier period start in
     the same scope. Several period starts: one run per snapshot, each `--compare` the earliest, to
     `.task-master/visualize-metrics-<n>.json`, in date order.
5. **Question.** The question as asked; the scope and dates; the reader, the people steering or
   someone outside (unstated: the people steering, recorded as assumed); setup, `period_days`,
   `sle`.
6. **Dispatch** with `${CLAUDE_PLUGIN_ROOT}/skills/visualize/method.md`.
7. **Relay** the chart's path and reading, or the refusal. The plugin cannot publish, so publishing
   stays in `needs_caller`.

## Reference files

- `${CLAUDE_PLUGIN_ROOT}/skills/board/inspector-run.md`: the shared run, step by step.
- `method.md`: the inspector's procedure: chart table, pages, Mermaid limits.
