---
name: schedule
description: >-
  Orders estimated tasks, lays them out over iterations from the team's velocity and gives the
  date as a range, or a probabilistic forecast under flow, citing the knowledge base. Use when
  someone asks "when will this be done?", "what fits in the next sprint?" or "what order to take
  these estimated tasks in". Not for unestimated tasks (estimate).
argument-hint: "<estimated tasks> <velocity history> <period length and calendar>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**)
context: fork
agent: task-master:planner
background: false
---

Plugin root: ${CLAUDE_PLUGIN_ROOT}. Order and lay out the tasks below, following
`skills/schedule/method.md` under that root.

$ARGUMENTS
