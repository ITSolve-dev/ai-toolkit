---
title: Percentile Intervention Triggers
category: moving-work
summary: Compare each open item's age with the 50th, 70th and 85th percentile lines. Under an 85th-percentile SLE, the chance of missing rises from 15% at the start to 30% at the 50th line and 50% at the 70th, so each line is a checkpoint.
tags: [method, board-health, cycle-time, aging, percentiles, work-item-age]
sources: [vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Percentile Intervention Triggers

**Percentile intervention triggers** use the cycle time percentiles of finished work as checkpoints for unfinished work. As an open item's age crosses each line, the team stops and asks what it has learned about that item. The aim is to act before the item breaches its [[service-level-expectation]]. [[overrun-triggers-a-recut]] covers the point where the expectation has passed; this method acts earlier.

## Why age predicts more age

> Generally speaking, the older a work item gets, the greater chance it has of aging still more.
>
> — [[vacanti-actionable-agile-metrics]], L3134

Vacanti's analogy is life expectancy: a US-born female has an expectancy of 85.8 years at birth, 86.1 at age 5, 87.3 at age 50 and 93 at age 85, by a WorldLifeExpectancy.com calculator at the time of writing (L3122). Surviving means having outlived what might have ended it (L3132). Delay, in his framing, is the enemy of flow (L3134). Work Item Age is defined on [[work-item-age]].

## The procedure

Assume an SLE at the 85th percentile. Read each open item's age from board history and compare it with the lines on the scatterplot ([[cycle-time-percentile-lines]]).

| Age reaches | What is known | Chance of missing the SLE | Action |
|---|---|---|---|
| Pull | Nothing yet | 15% (L3144) | None |
| 50th percentile | Older than half of past items | 30% (L3144) | Pause and ask what was learned |
| 70th percentile | Older than more than two-thirds of past items (L3146) | 50%: "Flip a coin." (L3146) | Same questions, more urgent |
| Near the 85th | About to breach | Rising towards certain | Do everything possible first (L3148) |

The questions at the 50th line are concrete: "Do we need to swarm on it? Do we need to break it up? Do we need to escalate the removal of a blocker?" (L3144) They need not produce action at once: "Even if that does not cause concern, it should at least cause conversation." (L3144)

The arithmetic generalises. This derivation is the wiki's, not the source's: an item that has survived to percentile *p* misses an SLE at percentile *s* with chance (100−*s*)/(100−*p*), so 15/50 = 30% and 15/30 = 50%. It holds only if open items come from the same distribution as the finished ones, which is the assumption behind the SLE itself.

## After a breach

A breach ends the forecast, not the work. "We still need to finish that work." (L3148)

> once we breach our SLA we are squarely in unpredictable land
>
> — [[vacanti-actionable-agile-metrics]], L3150

From there no date can be given to the customer (L3150-L3156). In Figure 12.3 the 85th percentile is 43 days and one item took 181 days.

> That no man’s land between 43 days and 181 days (and potentially beyond) is a scary place to be in.
>
> — [[vacanti-actionable-agile-metrics]], L3162

A breach is not by itself a failure of the process: "The last thing we want is for that item to violate its SLA—even though we know it is going to happen 15% of the time." (L3148) What the method targets is arriving there without having tried.

## What to do at a line

[[flow-metrics-scrum-teams]] restates the table above for a fixed period (L1158-L1168), so the method needs an SLE and not a flow setup. What it adds is what follows the questions. Line references in this section are to that source, and the signs are this wiki's.

**Freed capacity goes to the aging item first.**

> Developers finishing the next item should be asked to help out with the aging PBI instead of picking up new ones.
>
> — [[flow-metrics-scrum-teams]], L1178

This wiki reads the part that transfers as a rule about starting, and not about adding hands, which the book itself qualifies with Brooks' law in the same passage. The sign is a new item started after an open item crossed a line, with nothing changed on the older item. It sits beside [[starting-new-work-when-blocked]], whose trigger is a stop and not an age.

The book lists three ways several people help (L1182-L1192), and this wiki sorts them by what an agent and a person steering can do.

- **Doing later steps earlier** (L1182) survives as preparing the review of an item before it arrives.
- **Dividing the item into subtasks** (L1184) is dropped. It sits one level below this wiki's task ([[unit-of-work]]), and expanding a task into steps is out of scope.
- **A fresh view of a sticking point** (L1186) survives as a person reading where the run stuck. Whether a new run on a restated task counts is untested.

**A blocked item goes to the project's policy for blocked work:** [[blocked-work-policies]].

**A large item is recut.** The book's starting point is that "your first hypothesis should be that this large PBI is probably composed of smaller, individually deliverable bits of value." (L1222). See [[story-splitting-patterns]] and [[hidden-wip-in-large-items]].

### Which question comes first

The book says "usually when a PBI is stuck in your process it is because it is too big" (L1210), while the caveat and the agent note below say an old item may be neither large nor still being worked on. This wiki resolves that by reading the item's state before its size, and the order is ours.

| What the board shows | Read as | Response |
|---|---|---|
| A stop marker, or no activity since the executor stopped | Blocked | [[blocked-work-policies]] |
| In a review state | Waiting for a person | Spend attention here before anything new starts |
| Later items pulled past it | Aged by order | [[artificially-aged-work]] |
| Active and still running | Size or missing information | [[overrun-triggers-a-recut]], [[hidden-wip-in-large-items]] |

On a human team with no review queue the book's order may hold, since the first three rows are then rare.

## Signs

These signs are the wiki's reading of the procedure, read from board state or history:

- An open item older than the 50th percentile line with no change to it since it crossed: no split, no blocker raised, no note.
- An open item past the 85th percentile, which is the question of why intervention did not happen at the earlier lines.
- Isolated dots far above the top line on the scatterplot, which show how far the unpredictable region runs.

A sign raises a question, not a verdict: an old item may be known, accepted and waiting on purpose ([[smell-is-not-a-finding]]).

## Costs and limits

- The method needs open-item age on the board and a percentile basis, so it needs the data of [[choosing-a-service-level-expectation]].
- Each checkpoint costs attention, and that cost lands on items already behind.
- This caveat is the wiki's: the source says an item at the 50th line "is now larger than half the work items" (L3138), but age measures size and waiting together. An item that is old because it sat blocked is not larger; the action differs, so the question to ask first is which it is ([[artificially-aged-work]], [[hidden-wip-in-large-items]]).

## Agent executor note

This note is the wiki's own. Age is read from board history, so the method does not depend on who executes. "Swarm" assumes adding people to an item and does not transfer as written. The other two questions do: split the task, or remove the blocker. With an agent executor, the likely cause of age is a wait for a person, which makes the blocker question the first one to ask.
