---
name: ask
description: >-
  Answers a question about organizing software work (cutting, sizing, ordering, triage, board
  limits, dates, flow metrics) from the plugin's knowledge base, with citations. Use when someone
  asks "how big should a task be?", "what makes a board healthy?" or "what does cycle time tell us?".
  Not for cutting real work into tasks (decompose).
argument-hint: "<your question about planning or running a board>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**)
context: fork
agent: task-master:guide
background: false
---

Answer this question about organizing work on a board, from the knowledge base. Plugin root:
${CLAUDE_PLUGIN_ROOT}

$ARGUMENTS
