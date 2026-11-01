---
title: Fact Stranded Outside the Task
category: task-content
summary: A decision or value that is known and recorded somewhere other than the task, such as a comment or a chat; practitioners called it problematic with no one disagreeing, and the sign is a field or text contradicted by what was said elsewhere.
tags: [failure-mode, task-content, agents, evidence]
sources: [montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Fact Stranded Outside the Task

A fact is stranded when it is known and written down, and the task does not show it. It breaks the question of what a task must carry: the task is out of date and it does not look out of date. The smell's definition gives the plain case: "In the comments, someone has referenced a property and the value it should be, but not updated it in the property. For example, “This ticket is now closed”, but the status of the ticket remains open." ([[montgomery-tracker-smells]] L179).

This is the only smell the study reports with no participant refuting it:

> The smell “properties discussed in the comments but not updated in the issue” was declared as problematic by 12 participants and not refuted by any participant. This smell is particularly problematic because it describes when information is known (and often reported somewhere), but is not recorded in the issue. Therefore, there is a known inconsistency, but it will be unknown to people who only have the information in the issue.
>
> — [[montgomery-tracker-smells]], L765

The study also shows a wider form of the same failure. Ten participants described information spread across systems, as in P20's note "multiple sources of truth: Slack, Jira, etc." (L472). And among the causes of missing information is that it may be "stored inside other communication tools such as Mattermost" (P19, L443). The study also lists the link version of the smell, a known link mentioned in comments but not documented (S2.4, L190), with no result in the text.

## Sign

- **In a task's comments:** a comment states a status, a value or a decision that the task's fields or text do not show.
- **In task text:** it points at another place for a decision: a chat, a call, a thread. This overlaps with the sign on [[conversation-moves-into-the-task]].
- **In board history:** a task's result followed a decision that appears only in a comment.

These wordings are this wiki's, from L179 and L765.

## What this sign does not establish

- That the task is misleading anyone in this project. A team may read comments as a matter of course. The study says some teams put everything in the description instead, and "no comments means everything is well" for another (L520).
- How often it happens. Twelve people called it a problem in an interview, which is a perception.
- That the fact should have been copied. A link to a decision record is not stranded. Writing decisions down at length is `spec-driven-guide` work, and the point here is only that the task must show the result.

## Remedy

Move the fact into the task, or update the field. The authors' account of the reasons includes "laziness, assumption of responsibility on someone else, and reliance on external tools for discussion" (L765), and this wiki keeps the third, which is a matter of where work happens. Their proposed tool, which would detect keywords in a comment, is out of scope.

## Agent executor note

This failure gets worse with an agent, and the mechanism is the one the authors name. The authors' "people who only have the information in the issue" (L765) describes an agent's normal position, while a person on the team has usually seen the chat. An agent given a task and not its comments works from a stale brief. An agent that does read comments still has to weigh them against the text, and nobody here tests how well it does. So the plugin should treat a comment that contradicts a task as something to resolve before the task starts. The agent case is this wiki's reading. The study has no agent in it.
