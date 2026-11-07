---
name: estimate
description: >-
  Estimate a set of tasks relative to each other and say what each estimate rests on: the
  reference tasks, the step of the scale and what it means, and which tasks are too big and
  should be cut again. Grounded in the plugin's knowledge base. Use when someone hands over tasks
  or a backlog to size, point or estimate, to check their estimates, or to flag which are too big;
  under continuous flow without estimates it says what replaces one. A question about how
  estimating works goes to ask; for dates, use schedule.
argument-hint: "<tasks as text or a file path> [finished tasks with their sizes]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**)
context: fork
agent: task-master:planner
background: false
---

Follow the method at `${CLAUDE_PLUGIN_ROOT}/skills/estimate/method.md` on this input:

$ARGUMENTS
