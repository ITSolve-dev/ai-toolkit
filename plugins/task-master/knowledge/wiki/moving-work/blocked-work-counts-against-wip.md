---
title: Blocked Work Counts Against WIP
category: moving-work
summary: A blocked item stays in its column and counts toward that column's limit, so that being stopped restrains further pulling; moving it aside hides the stop. A project states in advance when stopped work is marked (with an agent, at once), how long it counts (until a decision, not a timer), and when it leaves the board (at a stated age, by a person's decision), with where it goes per setup.
tags: [rule, wip, work-states, kanban, blocked, board-history, scrum]
sources: [radzikowska-waiting-blocked, kanban-guide, scrum-guide-2020, wester-board-design, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Blocked Work Counts Against WIP

A blocked item stays where it stopped and keeps its place in the count. This is the direct answer the Kanban Maturity Model gives, as reported in [[radzikowska-waiting-blocked]]:

> Because of their negative effects on service delivery, blocked work items usually are marked by means of a symbol or a sticky note of a preselected color. They stay in the swim lane and column in which they are blocked, and they add to the WIP for that column. This might create tension because it impedes pulling work into the column, but it also encourages fast resolution of blockages.
>
> — [[radzikowska-waiting-blocked]], L34

The habit this restrains is on [[starting-more-work]].

## The rule

An item that is blocked ([[waiting-versus-blocked]]) stays in its state and counts toward that state's limit. It is marked as blocked, not moved.

## Sign of violation

- **In board state:** an unresolved blocked item sitting in a column other than the one it stopped in, or a holding column for blocked items that no limit covers.
- **In board history:** an item moved backward or sideways at the moment it stopped, and returned later to the same state.
- **In board state:** a state at its limit with blocked items not counted, and new work being pulled into it.

The source states the rule. These signs are this wiki's derivation from it.

## Why

What breaks is the signal. If a blocked item leaves the count, the state has room again and work continues to be pulled, so the stop has no effect on anything and nothing forces attention to it. The source's own wording is that counting "impedes pulling" and that this "encourages fast resolution" (L34). The waiting case is different: an item that cannot be shortened goes to a [[parking-lot]] instead, which has its own bookkeeping.

## Cost

The rule stops work on purpose, and the source calls that a stressor. It warns against adopting it early, and gives organizational maturity as the deciding factor:

> Hence, including blocked or waiting items in work in progress limits too soon (when you recognize that your organization is at Maturity Level 0, 1, or 2) may result in too much stress, too heavy resistance, and rejecting the practice.
>
> — [[radzikowska-waiting-blocked]], L76

This wiki does not keep that as a condition of the rule, because maturity level is not on a board and resistance is about people. It keeps it as a cost: expect objections, and expect a period in which pulling stops.

## Policies for blocked work: marking, counting, leaving

Blocked work ages with nothing moving it, so a project decides ahead of time how it is treated. [[flow-metrics-scrum-teams]] puts the duty this way:

> Whether the dependency is internal or external, we need to establish some policies around how we treat blocked work.
>
> — [[flow-metrics-scrum-teams]], L1196

The book names three levels of policy, each as a question, and it answers none of them (L1198-L1202). This wiki takes the three questions as a rule alongside the one above. The answers below are this wiki's reading, built from pages it already holds. What counts as blocked is on [[waiting-versus-blocked]].

### The rule

A project states when a stopped item is marked, how long it counts, and when it leaves. A board can then be read against a stated policy, and an unstated one leaves each stop to be settled ad hoc.

| Level | The book's question | This wiki's answer | Sign, in board history or state |
|---|---|---|---|
| Marking | "How much time needs to pass before we mark an item whose progress is stopped as blocked?" (L1198) | A stated time, set by the project. With an agent executing, at once | An open item with no movement for longer than the stated time, and no marker |
| Counting | "How long should a blocked item count towards our WIP limits and stop us from picking up other work?" (L1200) | For as long as it is on the board in that state | A blocked item left out of a state's count while it is still unresolved (the rule above) |
| Leaving | "At what point do we say that the item is going to be blocked for so long that it might not be relevant to track it?" (L1202) | At an age the project states, a person decides | A blocked item past that age with no decision recorded |

The book asks whether marking takes "hours, days or weeks" (L1198) and gives no figure. This wiki supplies none. The age for leaving comes from the project's own history ([[closing-what-no-longer-applies]]).

### Why state them

What breaks if these stay unstated is the reading of history. Two stops of the same kind get marked at different times, so blocked time is not comparable, and an item may sit for a long stretch before anyone counts it as stopped ([[capturing-flow-data]], [[flow-debt]]).

### The two conflicts

**How long it counts.** The book's question implies that an item might stop counting after a while, and the rule above says it stays and counts. This wiki resolves that with a single rule: counting ends by a decision and not by a timer. If an item should stop restraining the pull, it should leave, by the third level or as a declared exception ([[parking-lot]]). A timer would hide the stop at the moment it has lasted longest, which is what the count exists to prevent.

**Where it goes when it leaves.** The book offers "cancel the item or move it back to the backlog" (L1202), and [[backward-movement]] allows a return only at a period's end. This wiki resolves that per setup.

- **Flow setup, or iterations with a WIP control, inside a period:** cancel with a tag ([[non-standard-departure]]). An item expected to return leaves through the test on the same page, which keeps the history and marks it, and it does not count as an ordinary backward move.
- **Iteration setup, at the period's end:** it goes back to be ordered again ([[unfinished-at-period-end]]).
- **Iteration setup with no WIP control, inside a period:** the second level has no count to join, so only the marker and the threat to the goal remain (setup section below, [[mid-period-change]]).

### Reading the cause

The book splits causes in two. "If the cause is an internal dependency, we need to examine our process policies and look for improvement." (L1196). For an external one, it asks how to reduce the likelihood of the dependency or its effect on age (L1196). This wiki keeps the split as a question for an audit: does the same cause recur across blocked items in history? The answer goes to the people steering. The book's remedies, such as bringing expertise in house or improving vendor relationships, manage people and are dropped.

### Cost of the policies

A stated time produces false marks on items that were only slow, and a stated age for leaving can close something still wanted. This wiki reads both costs as smaller than leaving each stop undecided, and it has no measurement for that.

### Agent executor note on the policies

This wiki's reading, unmeasured. The first question assumes a person who may not notice or admit a stop for some time. An agent's stop is an event: the run ended, or it asked for something. The marker can follow at once, and no waiting time is needed. The usual holder of the next step is then a person inside the project, which [[waiting-versus-blocked]] classes as blocked. So the third level matters less for agent-run work than for outside dependencies, because the people who can clear the block are the people reading the policy.

## Agent executor note

The source's mechanism is human: "tension" among people who feel the stop. An agent feels nothing, so that part does not survive. The mechanical part does, and is arguably stronger: an agent that is not allowed to pull will stop pulling, so the pressure lands entirely on the people steering, who see no new results. Whether that produces faster resolution for a few people is not shown by this source, which reports no measurement of any kind.

## Positions

**Kanban Maturity Model:** blocked items stay and count, as above. The source places these practices at Maturity Levels 3 and 4 (L74).

**Kanban Guide:** the Guide does not address blocked items directly. It lists "Unblocking blocked work." ([[kanban-guide]] L135) as a form of active management and does not define the term. Its definition of WIP settles the count all the same, in this wiki's reading: "Any work items between a started point and a finished point are considered work in progress (WIP)." (L112). A blocked item sits between those points, so it counts. A project that wants otherwise has to say so, since "Any acceptable exceptions to controlling WIP should be made explicit as part of the DoW." (L143). The Guide therefore has no maturity gate, and the count applies from the start.

**Wester:** agrees on staying in place, for a further reason: "A better practice is to visualize this kind of wait in the place where it is incurred." ([[wester-board-design]] L53). The post also names what a holding column would hide, which [[column-versus-attribute]] records. Wester argues about columns and does not say in so many words that a blocked item counts, although the complaint about stashing work "so they can get around their WIP limits" (L51) assumes it should.

**Vacanti and Seele:** the book leaves the matter as a question for a project to answer: "How long should a blocked item count towards our WIP limits and stop us from picking up other work?" ([[flow-metrics-scrum-teams]] L1200). This wiki answers it in the policies section above: counting ends by a decision and not by a timer.

**Scrum Guide:** the Guide has no count, so the question does not arise in those terms. A stop is an impediment, and the Daily Scrum exists partly to "identify impediments" ([[scrum-guide-2020]] L240). What a stop threatens under Scrum is the goal and not a limit, so the handling goes through [[mid-period-change]].

## Which holds under which setup

- **Flow setup, or iterations with a WIP control:** the item stays in place and counts.
- **Iteration setup with no WIP control:** there is no count to join. The item still stays in place and is marked, because the marker is what shows the stop. Whether the stop endangers the goal becomes the question.

This resolution is this wiki's.
