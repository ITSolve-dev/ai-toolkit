---
title: Work Item Age
category: reading-history
summary: How long an open item has been in the workflow so far; it applies only to unfinished items, turns into Cycle Time at the finish, keeps running through blocks and waits, and is read against the percentile lines of finished work. It is the one flow metric that reports on an item while the item can still be changed, and it measures size and waiting together, so it raises a question and names no cause.
tags: [concept, flow-metrics, work-item-age, board-history, aging, retrospective-analysis]
sources: [flow-metrics-scrum-teams, kanban-guide, vacanti-actionable-agile-metrics, kanban-playbook-workflow-states]
created: 2026-11-02
updated: 2026-11-02
---

# Work Item Age

Work Item Age is how long an open item has been in the workflow so far. The charter names age of open work as a measure of retrospective analysis, and it is the only one of the four flow measures that reads an item before the item has finished. Bare line references on this page are to [[flow-metrics-scrum-teams]].

> the total amount of time that has elapsed since an item entered a workflow.
>
> — [[flow-metrics-scrum-teams]], L376

The Kanban Guide's wording is "The elapsed time between when a work item started and the current date." ([[kanban-guide]] L161). This wiki reads the two as one measure, on the condition that a project's started point is where an item enters its workflow ([[started-and-finished-points]]). The name "WIP Age" means the same thing (L378).

## What it covers

> Because Work Item Age is a measure of current time in progress for all of your current work in progress it–by definition–applies only to items that have entered but not exited the workflow. Once an item exits the workflow, then all the age that has accumulated up to that point immediately becomes converted to Cycle Time.
>
> — [[flow-metrics-scrum-teams]], L380

This wiki draws four consequences from that passage and the definition.

- **One clock.** Age and [[cycle-time]] are the same clock, read before and after the finish, so they need the same started and finished points and the same counting convention. The book states the convention for both: "Cycle Time equals the finished date minus the started date plus one (CT = FD - SD + 1)" (L440), and "Work Item Age equals the current date minus the started date plus one (Age = CD - SD + 1)." (L454). It adds: "The “plus one” argument is the same as for Cycle Time above. Our apologies, but you will never have a PBI that has an Age of zero days." (L456). Its Chapter 4 describes plotting a dot by subtracting the start date from today's (L754) without the added one; this wiki reads that as shorthand for L454. Vacanti's earlier book gives the same added unit for Cycle Time (on the same page).
- **No age before the start.** An item in a backlog has none, and how old an unstarted item is gets read separately ([[zombie-issue]], [[backlog-versus-commitment]]).
- **It runs through stops.** The book says of blocked and on-hold work, "These PBIs age" (L1196). This wiki reads that as saying a stopped item's age includes the stop, so nothing pauses the clock.
- **A return does not reset it.** This wiki keeps the whole span for a task that went back and was selected again ([[unfinished-at-period-end]]), or that left the board and came back ([[non-standard-departure]], whose erasure of a step's date feeds the chart and not age). No source here states that.

## Why it is read first

The book's claim is "Age is by far the most important of all the Flow Metrics to track." (L374), and it sends the reader to its Chapter 4 for the detail (L374). The reason given there is timing:

> The problem with a Cycle Time Scatterplot –if there is one– is that by definition, a dot does not show up until a PBI has finished. However, if a PBI is taking too long to finish then waiting until it has finished to do something about it is too late.
>
> — [[flow-metrics-scrum-teams]], L730

The book's answer is "a view into our process data while PBIs are still in progress" (L730-L736). The claim also departs from its first author's earlier book, which calls WIP the most important of three metrics and leaves age off the list ([[vacanti-actionable-agile-metrics]] L550-L562, see [[flow-metrics]]).

This wiki resolves that by use, and the resolution is ours. WIP is what a project sets, so it comes first when setting a limit ([[wip-control]]). Age is what a project reads, item by item, while something can still be done, so it comes first in a daily look or an audit of open work. Neither ranking is measured.

## How to read it

The book reads age on what it calls "an Aging Work In Progress chart (or “Aging Chart” for short)" (L736), set out in its Chapter 4 (L728-L760). Its anatomy:

- **Columns, not a timeline.** "Unlike the Scatterplot, you can see the whole chart has been segmented into columns to match your process’s workflow. Up the side of the chart is the Age of PBIs." (L746-L752). The book's example workflow runs Analysis Active, Analysis Done, Dev Active, Dev Done, Testing, Done, with "Analysis Active" as the started point and "Done" as the finished point, and the authors say it is illustrative, not a good workflow (L738).
- **One dot per open item.** "every dot on the chart represents a PBI that has entered the process but has not exited the process. To plot a dot, you simply find the workflow stage that it is currently in" and compute its age from the start date, which needs "the timestamp for when the item entered your process" (L754).
- **Age is not Cycle Time.** The chart shows "the total elapsed time that an item has spent started but not completed (Age) as opposed to the total elapsed time it took for an item to complete (Cycle Time)" (L754). Any time unit may be used (L754).
- **The same percentile lines.** "These percentile lines are exactly the same lines that we calculated for our Scatterplot." (L756):

> You overlay percentile lines on the Aging Chart so that you can see how current PBIs in progress are flowing as compared to the total amount of time it took previous items to complete.
>
> — [[flow-metrics-scrum-teams]], L756

The book repeats the passage, in slightly different words, at L1154. It places the chart's use at the daily check: comparing current age with past performance "will help tremendously during our Daily Scrum" (L758). The conclusion of the chapter sends readers to Vacanti's other books for more (L760-L768); the earlier book in this base has no Aging Chart.

This wiki reads the column layout as adding one thing a list of ages lacks: an old item is seen in the state where it sits, which points the first question at that state (a queue column or an active one; [[active-versus-queued]]). That reading is ours.
This wiki sets the uses out by question. The table and its grouping are ours, and the procedure for the first row is on [[percentile-intervention-triggers]].

| Question | Read | Page |
|---|---|---|
| Which open item needs attention now? | Each open item's age against the percentile lines | [[percentile-intervention-triggers]], [[cycle-time-percentile-lines]] |
| Is an item being left behind? | Its age against newer items that finished or moved past it | [[flow-debt]] |
| Is the process stable over this window? | Mean age of open items at the end of the window against the start | [[littles-law-assumptions]] |
| Is a finished view hiding something? | Open items older than the lines, which no finished-item chart shows yet | [[which-chart-for-which-plan-question]] |

## What it does not say

Age rises at the same rate for an item being worked on, one waiting for review and one nobody remembers. The book itself names different causes: "previously unknown complexity" (L1178), dependencies (L1196), and size, in "usually when a PBI is stuck in your process it is because it is too big" (L1210). This wiki reads age as a prompt to find out which, and the order of questions is on [[percentile-intervention-triggers]]. This wiki also notes that age does not say how long an item will take ([[flow-metrics]]), and that a long-lived item is not thereby a badly written one.

## What an audit needs

The signs below are this wiki's. Each raises a question ([[smell-is-not-a-finding]]).

- **In board state:** an open item in an active state with no recorded entry date. Its age cannot be read, so the board cannot be audited for it ([[started-and-finished-points]]).
- **In board history:** states that do not separate waiting from working, which is the failure the Kanban Playbook describes as age being "hard to interpret" ([[kanban-playbook-workflow-states]] L22, see [[judging-board-columns]]).
- **In a report:** an age figure with no stated started point. Two ages with different starts are not comparable.

## Agent executor note

This wiki's reading, unmeasured. Age comes from timestamps, so it survives an agent executing and a person steering. Its meaning shifts. The book calls age "current time in progress" (L380), and with an agent most of that time is likely to be a result waiting for a person, so a high age usually says more about the review queue than about the task.
