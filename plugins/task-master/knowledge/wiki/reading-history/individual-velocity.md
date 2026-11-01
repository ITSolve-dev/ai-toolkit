---
title: Individual Velocity
category: reading-history
summary: Velocity split by person measures the wrong thing and, per Cohn, rewards finishing alone over helping. The plugin does not report it. His supporting claim that stories should need several people does not transfer to an agent.
tags: [failure-mode, velocity, retrospective, agent-transfer]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Individual Velocity

Individual velocity is story points or ideal days "completed by an individual team member" ([[cohn-agile-estimating-planning]] L4535). Cohn rejects it flatly:

> Do not track individual velocity. Tracking individual velocity leads to behavior that works against the success of the project.
>
> — [[cohn-agile-estimating-planning]], L4535

This page is about what a measure says, which the charter keeps under retrospective analysis. How people are managed is outside it, so the rule here is limited to what the plugin reports.

## Observable sign

- **In a report:** velocity, throughput or finished counts broken down by assignee.
- **In a request:** someone asks the plugin who is fastest, or to compare two people's output.

These signs are this wiki's.

## Why it fails

Cohn gives two arguments.

**Incentive.** "If I am forced to choose between finishing a story on my own and helping someone else, what incentive does measuring individual velocity give me?" (L4535). His conclusion is "Team velocity matters; individual velocity doesn’t. It’s not even a metric of passing interest." (L4537).

**It should not be computable.** "Most user stories should be written such that they need to be worked on by more than one person, such as a user interface designer, programmer, database engineer, and a tester." (L4539). He concludes that "If most of your stories can be completed by a single person, you should reconsider how your stories are written." (L4539).

## What to do

The plugin reports velocity and throughput for the board as a whole, per [[velocity]] and [[flow-metrics]], and declines a per-person breakdown, saying why. Chapter 22 carries the same position through to charts: "there are no individual burndown charts prepared, only a team-wide burndown chart." (L4893). A per-assignee view may still be used to find a concurrency problem ([[wip-per-executor]]), and that is a question about the board and not about the person.

## Trade-offs

The board loses a view that would show one person carrying more of the work than the others. The charter already excludes individual load, so nothing the plugin does depends on that view.

## Agent executor note

The incentive argument rests on people responding to being measured. It does not apply to an agent, and it still applies to the few people steering, whose finished counts would mostly show how tasks were routed to them.

The second argument does not transfer, and this wiki rejects it for this setting. Cohn assumes a team divided by role, with one story passing through several people. With an agent executing, one executor often finishes a task, and the charter's test wants it finished without waiting ([[unit-of-work]]). Following his remedy, writing stories "at a higher level so that work from multiple individuals is included with each" (L4539), would build the handoffs into the task that this wiki cuts out ([[sequence-versus-wait]]). So a task completed by one executor is no sign of a bad cut, and this page keeps only his first argument.
