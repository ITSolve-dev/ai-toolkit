---
title: Policies for Blocked Work
category: moving-work
summary: A project states three things about blocked work in advance; when stopped work gets marked, how long it counts against the limit, and when it leaves the board. The source asks these as questions and gives no figures, so this wiki answers per setup; counting ends by a decision and not by a timer, and an agent's stop is marked at once.
tags: [rule, blocked, wip, board-history, kanban, scrum]
sources: [flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Policies for Blocked Work

Blocked work ages with nothing moving it, so a project decides ahead of time how it is treated. [[flow-metrics-scrum-teams]] puts the duty this way:

> Whether the dependency is internal or external, we need to establish some policies around how we treat blocked work.
>
> — [[flow-metrics-scrum-teams]], L1196

The book names three levels of policy, each as a question, and it answers none of them (L1198-L1202). This wiki takes the three questions as the rule. The answers below are this wiki's reading, built from pages it already holds. What counts as blocked is on [[waiting-versus-blocked]].

## The rule

A project states when a stopped item is marked, how long it counts, and when it leaves. A board can then be read against a stated policy, and an unstated one leaves each stop to be settled ad hoc.

| Level | The book's question | This wiki's answer | Sign, in board history or state |
|---|---|---|---|
| Marking | "How much time needs to pass before we mark an item whose progress is stopped as blocked?" (L1198) | A stated time, set by the project. With an agent executing, at once | An open item with no movement for longer than the stated time, and no marker |
| Counting | "How long should a blocked item count towards our WIP limits and stop us from picking up other work?" (L1200) | For as long as it is on the board in that state | A blocked item left out of a state's count while it is still unresolved ([[blocked-work-counts-against-wip]]) |
| Leaving | "At what point do we say that the item is going to be blocked for so long that it might not be relevant to track it?" (L1202) | At an age the project states, a person decides | A blocked item past that age with no decision recorded |

The book asks whether marking takes "hours, days or weeks" (L1198) and gives no figure. This wiki supplies none. The age for leaving comes from the project's own history ([[closing-what-no-longer-applies]]).

## Why

What breaks if these stay unstated is the reading of history. Two stops of the same kind get marked at different times, so blocked time is not comparable, and an item may sit for a long stretch before anyone counts it as stopped ([[board-misuse-corrupts-flow-data]], [[artificially-aged-work]]).

## The two conflicts

**How long it counts.** The book's question implies that an item might stop counting after a while, and [[blocked-work-counts-against-wip]] says it stays and counts. This wiki resolves that with a single rule: counting ends by a decision and not by a timer. If an item should stop restraining the pull, it should leave, by the third level or as a declared exception ([[parking-lot]]). A timer would hide the stop at the moment it has lasted longest, which is what the count exists to prevent.

**Where it goes when it leaves.** The book offers "cancel the item or move it back to the backlog" (L1202), and [[backward-movement]] allows a return only at a period's end. This wiki resolves that per setup.

- **Flow setup, or iterations with a WIP control, inside a period:** cancel with a tag ([[accounting-for-abandoned-work]]). An item expected to return leaves through the test on [[non-standard-departure]], which keeps the history and marks it, and it does not count as an ordinary backward move.
- **Iteration setup, at the period's end:** it goes back to be ordered again ([[unfinished-at-period-end]]).
- **Iteration setup with no WIP control, inside a period:** the second level has no count to join, so only the marker and the threat to the goal remain ([[blocked-work-counts-against-wip]], [[mid-period-change]]).

## Reading the cause

The book splits causes in two. "If the cause is an internal dependency, we need to examine our process policies and look for improvement." (L1196). For an external one, it asks how to reduce the likelihood of the dependency or its effect on age (L1196). This wiki keeps the split as a question for an audit: does the same cause recur across blocked items in history? The answer goes to the people steering. The book's remedies, such as bringing expertise in house or improving vendor relationships, manage people and are dropped.

## Cost

A stated time produces false marks on items that were only slow, and a stated age for leaving can close something still wanted. This wiki reads both costs as smaller than leaving each stop undecided, and it has no measurement for that.

## Agent executor note

This wiki's reading, unmeasured. The first question assumes a person who may not notice or admit a stop for some time. An agent's stop is an event: the run ended, or it asked for something. The marker can follow at once, and no waiting time is needed. The usual holder of the next step is then a person inside the project, which [[waiting-versus-blocked]] classes as blocked. So the third level matters less for agent-run work than for outside dependencies, because the people who can clear the block are the people reading the policy.
