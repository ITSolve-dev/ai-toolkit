---
name: schedule
description: >-
  Order estimated tasks and lay them out over iterations, and give the date that follows as a
  range, with what does not fit kept as a separate tail. Uses the team's velocity history, never
  individual load; under continuous flow it gives a forecast with a probability instead. Grounded
  in the plugin's knowledge base. Use when someone hands over estimated tasks and velocity history
  and asks when they will be done, what fits in the next sprint or release, what to do first, or
  to plan a release. Unestimated tasks go to estimate first; a question about how forecasting
  works goes to ask.
argument-hint: "<estimated tasks> <velocity history> <period length and calendar>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.task-master/**)
context: fork
agent: task-master:planner
background: false
---

Follow the method at `${CLAUDE_PLUGIN_ROOT}/skills/schedule/method.md` on this input:

$ARGUMENTS
