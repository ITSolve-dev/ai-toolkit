---
name: estimate
description: >-
  Sizes a set of tasks relative to each other, saying what each size rests on and which tasks are
  too big to keep, citing the knowledge base; under flow without estimates it checks each against
  the SLE. Use when someone says "estimate these tasks", "point this backlog" or "check our
  estimates". Not for dates (schedule).
argument-hint: "<tasks as text or a file path> [finished tasks with their sizes]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**)
context: fork
agent: task-master:planner
background: false
---

Plugin root: ${CLAUDE_PLUGIN_ROOT}. Size the tasks below, following `skills/estimate/method.md`
under that root.

$ARGUMENTS
