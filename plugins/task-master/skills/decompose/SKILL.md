---
name: decompose
description: >-
  Cuts a design doc, requirements, an epic or a description into a tree of tasks an AI agent can
  each finish and show, each with acceptance criteria and a size, citing the knowledge base. Use
  when someone says "break this down into tasks", "split this epic" or "plan tasks from this doc".
  Not for a question about how to cut work (ask).
argument-hint: "<path to the document, or a description> [neighbouring or finished tasks]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**)
context: fork
agent: task-master:planner
background: false
---

Plugin root: ${CLAUDE_PLUGIN_ROOT}. Cut the work below into a task tree, following
`skills/decompose/method.md` under that root. Write the result to `.task-master/decompose-<slug>.md`
and return its path; the `board` skill applies it from there.

$ARGUMENTS
