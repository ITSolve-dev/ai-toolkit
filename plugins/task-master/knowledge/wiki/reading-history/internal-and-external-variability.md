---
title: Internal and External Variability
category: reading-history
summary: Moving up a scatterplot's stack, long cycle times tend to have causes outside the team; moving down, causes the team controls. Outliers are kept and investigated, and items just past a percentile line are the actionable ones.
tags: [decision-rule, scatterplot, cycle-time, variation, outliers]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Internal and External Variability

Internal and external variability is Vacanti's working split for where to look for the cause of a dot, based on its height on a [[cycle-time-scatterplot]]. High up, the cause is more likely outside the team; low down, more likely inside it. It decides where an investigation starts and who can act on the result. It is a tendency to start from, not a classifier: see [[reading-a-cycle-time-scatterplot]] for what the chart cannot do.

## The rule

- **Up the stack, start outside.** “More often than not, those outliers will be caused by circumstances that are outside of the team’s control.” ([[vacanti-actionable-agile-metrics]] L2960).
- **Down the stack, start inside.** “As you move “down the stack” the work items that took less time to complete were generally due to reasons that were totally under the team’s control.” (L2962).
- **Just past a percentile line, act.** Of dots that barely cross the 85th percentile, Vacanti asks whether the team could have prevented the violation, and answers “Probably” (L2962-L2968, joined across a page break), naming “swarm or break up the item” (L2968). The chapter's checklist lists “Dots that just cross a give percentile line” (L3006).

**Worked figures.** The example is Figure 11.5: 50th percentile 20 days, 85th percentile 44 days, one item at 181 days (L2960). These are one illustrative data set in the book, not a benchmark. The external reasons offered for the 181-day item are a dependency on an external vendor or another internal team, no test environment immediately available, and a customer not immediately available for sign-off (L2960); the book offers these as possibilities for that dot, not as findings.

## Keep the outliers

Vacanti's position is that “while those points are outliers, they obviously happened and probably warrant some deeper investigation” (L2958), and that even if statistically insignificant “there might be some good contextual or qualitative reasons to keep them in from an analysis perspective” (L2958). Proving a dot statistically irrelevant is therefore not a reason to stop asking about it. This wiki reads that as the opposite failure to [[low-cycle-time-cluster]], though both pages share one test: what would recur?

## Where the rule fails

Vacanti gives the exceptions himself: “Will all outliers be due to external causes? Certainly not.” (L2970). His internal examples at the top are “Maybe the team allowed an item that ended up being too big into the process. Maybe the team ignored an item once it had been pulled.” (L2970). In the other direction, “will there be external issues hiding in the shorter Cycle Times? Almost certainly.” (L2970).

The rule also has a condition: “the more you adhere to the assumptions of Little’s Law, the more confident we can be that the “up the stack” dots are due to outliers, and the “down the stack” dots are due to team policies.” (L2970). This wiki reads the converse as the practical warning: on a process that breaks those assumptions, for example with uncontrolled WIP ([[littles-law]]), height says less about cause, so the split should be stated with less confidence.

## Applying it

- **Inputs.** Cycle time per finished item and the [[cycle-time-percentile-lines]] come from board history. Causes come from what the board recorded about the item: blocks, waiting, comments.
- **Output.** A question to check per dot, starting from the side the height suggests. A high dot with no recorded outside cause raises the “too big” or “ignored after pull” question; see [[diagnosing-unfinished-work]].
- **What later fact shows the choice wrong.** The investigation of a high dot finds an internal cause, or of a low one an external one. Vacanti's exceptions say to expect some of each, so one such result does not break the rule; a run of them says the process does not meet the condition above.
- **Cost.** Attention goes to the extreme dots, which are the ones least under the team's control by this same rule. The dots just past the line are where action is cheapest, and this wiki reads that as a reason to look at both groups and not only the dramatic one.

## Survival under an agent

This wiki's judgement is that the split survives, with “the team” redefined. For a few people steering an agent, a wait on the steering person is inside the team's policy, so such a dot does not count as external even when it looks external from the agent's side. Of Vacanti's two remedies, breaking up the item carries over directly ([[story-splitting-patterns]]); swarming assumes several executors on one item and may not carry over to a single agent. Both notes are the wiki's own and are unsourced.
