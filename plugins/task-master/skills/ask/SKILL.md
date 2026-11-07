---
name: ask
description: >-
  Ask a question about organizing software work and get an answer from the plugin's curated
  knowledge base, with citations. How to cut a request into tasks, what a task must carry before an
  agent takes it, estimating and story points, what comes first, triaging incoming reports, board
  columns and WIP limits, filling an iteration and giving a date, velocity, cycle time and
  throughput, which chart answers which question — how to tell whether a task is too big, or "what
  makes a board healthy". Tasks handed over to cut, size or lay out go to decompose, estimate or
  schedule; a real board to check, items to triage, a past period or a chart to draw go to
  tend-board, triage, review-period or visualize. Not for configuring a tracker, running a meeting,
  or writing a design doc.
argument-hint: "<your question about planning or running a board>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**)
context: fork
agent: task-master:guide
background: false
---

Answer this question about organizing work on a board, from the knowledge base:

$ARGUMENTS
