---
name: decompose
description: >-
  Cut a design doc, requirements, an epic or a loose description into a tree of tasks an AI agent
  can each finish and present once: boundaries, what is out of scope, acceptance criteria,
  dependencies and a relative size on every task, with the reasoning cited from the plugin's
  knowledge base. Use when someone hands over work to break down, plan tasks from a document, split
  an epic or a story, or re-cut existing tasks. A question about how to cut work goes to ask; not
  for writing the document itself.
argument-hint: "<path to the document, or a description> [neighbouring or finished tasks]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**)
context: fork
agent: task-master:planner
background: false
---

Follow the method at `${CLAUDE_PLUGIN_ROOT}/skills/decompose/method.md` on this input:

$ARGUMENTS
