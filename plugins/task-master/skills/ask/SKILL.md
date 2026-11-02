---
name: ask
description: >-
  Ask a question about organizing software work and get an answer from the plugin's curated
  knowledge base, with citations. How to cut a request into tasks, what a task must carry before an
  agent takes it, estimating and story points, what comes first, triaging incoming reports, board
  columns and WIP limits, filling an iteration and giving a date, velocity, cycle time and
  throughput, which chart answers which question — and "is this task too big" or "is this board
  healthy". Not for configuring a tracker, running a meeting, or writing a design doc.
argument-hint: "<your question about planning or running a board>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**)
context: fork
agent: task-master:guide
background: false
---

Answer this question about organizing work on a board, from the knowledge base:

$ARGUMENTS
