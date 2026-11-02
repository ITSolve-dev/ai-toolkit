---
title: Unfinished at Period End
category: periods
summary: A task that has not met the standard of done is not partly done; it goes back to be ordered again, it is not carried over automatically, and it does not count toward what the period finished. Cohn agrees and adds a reason, that each period is planned afresh, which removes the work's claim on the next period but not the partial work.
tags: [rule, iterations, definition-of-done, scrum, wip]
sources: [scrum-guide-2020, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Unfinished at Period End

A task that does not meet the project's standard of done when a period ends has not partly happened. The Scrum Guide's statement:

> If a Product Backlog item does not meet the Definition of Done, it cannot be released or even presented at the Sprint Review. Instead, it returns to the Product Backlog for future consideration.
>
> — [[scrum-guide-2020]], L319

The Guide also says "Work cannot be considered part of an Increment unless it meets the Definition of Done." (L311). This wiki notes that the passage sits under the Definition of Done and does not mention the end of a Sprint. Reading it as the rule for period end is ours, by way of the Sprint Review it names, which falls at the end of the period (L250).

## The rule

At a period's end, each task either met the standard of done or it did not. A task that did not goes back among the unstarted work and is ordered again against everything else. It enters the next period only if it is selected again.

## Sign of violation

- **In board history:** a task stays in an active state across a period boundary with no selection in the new period.
- **In a period's report:** partial credit, such as a task counted as 80% done.
- **In board history:** a task that did not meet the check is counted in what the period finished.
- **In board history:** the same task selected in several periods running. It is what repeated return looks like, and it suggests the task is too large or badly cut, so it goes to [[overrun-triggers-a-recut]].

The signs are this wiki's derivation from L311 and L319. The Guide does not use the word "carry". Cohn's split of a deferred story into a finished item and a new one is not a percentage of an open task; how it fits this rule is on [[partial-credit-for-unfinished-tasks]].

## Why

Two things break. The first is the record: counting partial work inflates the past performance that [[filling-a-period]] reads from. The second is the order: an unfinished task may no longer be the most useful thing to do, and an automatic carry-over means nobody asks. The Guide's phrase is "for future consideration", which leaves the task with no claim on the next period. This reasoning is this wiki's.

## Cost

Work in progress loses its place, and an agent's partial work may go stale before the task is selected again. Reordering is also a chore when the usual answer is to continue.

## Cohn's position

Cohn agrees with the Scrum Guide on the rule and adds a reason.

> Because work is not automatically rolled forward from one iteration to the next, each iteration is planned afresh. This means that work on a feature not fully implemented in one iteration will not necessarily be continued in the next. It often will be, but there’s no guarantee.
>
> — [[cohn-agile-estimating-planning]], L4881-L4885

Cohn counts this as a reason planning succeeds: "all work in process is eliminated at the end of each iteration" (L4881). The stated benefit is flow: "Because work in process is eliminated at the start of each iteration, teams are more easily able to work efficiently in short iterations." (L4887), which gives a shorter loop of feedback from users and earlier learning and risk control (L4887). The reasoning connects to [[starting-more-work]]. The Scrum Guide's text gives no such reason.

This wiki does not read "eliminated" literally. A half-built feature still exists on the day after the boundary, and by Cohn's own account it "often" continues. What is eliminated is the feature's claim on the next period, since nothing is continued without a decision ([[reprioritize-before-each-iteration]]). If nearly every unfinished item is reselected without being compared to the rest, work in process has only been renamed. The sign is the last one listed above: the same task selected in several periods running.

The flow benefit therefore rests on the boundary being a real choice. Whether it reduces cycle time when most work is continued is not shown in his chapter.

## Which setup this applies under

- **Iteration setup:** as above.
- **Flow setup:** there is no such moment. An unfinished task stays in its state and ages, and its age is compared with the SLE ([[overrun-triggers-a-recut]]). Nothing returns it to the backlog by the calendar. Cohn's position depends on an iteration setup in the same way and has no flow counterpart.

The return is the one sanctioned exception to [[backward-movement]].

## An open point

Neither guide says whether a returned task's age restarts when it is selected again. This wiki's view is that board history should keep the whole span, since a reset would hide exactly the task the sign above is looking for. No source states this. The erasure of an entry date on [[non-standard-departure]] applies only to the per-step dates that draw a chart, not to age or Cycle Time, so the two pages give a returned task the same age.

## Agent executor note

The rule concerns the task and survives. An agent also changes the cost. A person keeps the memory of partial work, whereas a stopped agent run leaves only what is in the repository and the task text. If a task returns, the plugin should treat its next start as a new start from the text and the repository, and not assume continuity.
