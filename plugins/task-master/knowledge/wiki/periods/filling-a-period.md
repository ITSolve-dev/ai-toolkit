---
title: Filling a Period
category: periods
summary: How much to select for an iteration; the Scrum Guide names three inputs, past performance, upcoming capacity and the Definition of Done, and gives no formula, while Cohn's case fills one story at a time, stops at the tightest stage and not at the total, and leaves room to add. Selection applies only under an iteration setup.
tags: [rule, iterations, forecast, capacity, scrum, cohn]
sources: [scrum-guide-2020, montgomery-tracker-smells, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Filling a Period

Filling a period means choosing how much work to select for it. This rule chooses a quantity, and the Scrum Guide gives it inputs and no formula:

> Selecting how much can be completed within a Sprint may be challenging. However, the more the Developers know about their past performance, their upcoming capacity, and their Definition of Done, the more confident they will be in their Sprint forecasts.
>
> — [[scrum-guide-2020]], L222

The Guide calls the result a forecast, and this wiki holds it to that: it is not a promise ([[commitment-over-a-period]]). This wiki also reads the three inputs as a rule: selection is judged against history and against what has to be true for an item to count, and not against how much someone would like to get done.

## The rule

Select from what is ready, up to what history says can be finished to the project's standard of done in a period of this length, adjusted for known changes in capacity.

An item is ready for selection on a size test: "Product Backlog items that can be Done by the Scrum Team within one Sprint are deemed ready for selection in a Sprint Planning event." (L278). See [[size-ceiling]]. This is a narrower meaning of "ready" than this wiki uses for task content, because it says nothing about what the task text carries ([[recoverable-versus-task-only-facts]]).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Past performance | Board history: what was finished in earlier periods, counted only if it met the standard of done |
| Upcoming capacity | The calendar of the people steering and any known change in the agent setup |
| The standard of done | The project's stated definition; a stricter one means less fits |

The selection was too large if tasks repeatedly go back unfinished at the period's end ([[unfinished-at-period-end]]), or if the goal is reached only by relaxing the standard of done. It was too small if the selection is finished well before the period ends, period after period.

A related board sign is weak. The study behind [[montgomery-tracker-smells]] lists "Too many difficult or complex issues have been added to a sprint." (L209) as a smell, and 4 of 14 disagreed or said it depends (L552). The reasons given were that "you can just delay issues to the next sprint without repercussions", and that the count alone says little if the work is well distributed between people (L552). The first reason describes the carry-over that [[unfinished-at-period-end]] rejects, so this wiki does not accept it as a defence. The second concerns people and falls away with an agent. Since the study gives no number for "too many", this page relies on the history test above and does not count complex tasks.

## Why

Empiricism is the Guide's stated reason: "Only what has already happened may be used for forward-looking decision making." (L202). What breaks if it is ignored is the forecast's meaning, because a selection chosen by hope tells the people steering nothing about what will happen.

## Leave slack

Cohn adds a limit on the selection, as one of his guidelines:

> Especially when planning an iteration, do not plan on using 100% of every team member’s time. Just as a highway experiences gridlock when filled to 100% capacity, so will a development team slow down when every person’s time is planned to be used.
>
> — [[cohn-agile-estimating-planning]], L4941

The highway is an analogy and not a finding, and no figure comes with it. The rule, its signs and its cost are on [[utilization-versus-slack]]. This wiki reads the mechanism as the one on [[wip-lengthens-cycle-time]]: with no spare capacity, any delay queues everything behind it. The margin comes from the project's own history, since no source here gives one.

The case study below gives one more reason for stopping short: "you’re better off adding something mid-way through the iteration than dropping something." (L5931). The source states no mechanism. This wiki reads the implied cost as a commitment broken in the open against capacity left idle for a while; see [[mid-period-change]].

## Cohn's case: filling one story at a time

Chapter 23 of [[cohn-agile-estimating-planning]] runs the commitment-driven form from [[velocity-versus-commitment-planning]] on a fictional project, and its figures are illustrations (L4961). The team works in two-week iterations at six planned hours a person a day ([[iteration-capacity]]), with five people carrying work. The chapter's "tasks" sit one level below this wiki's ([[unit-of-work]]), and its hours are a planning input and not a log. Line references in this section are to that source.

1. Take the most important remaining story ([[ordering-by-value-and-urgency]]).
2. Split it into estimated pieces, including the test work.
3. Sum the hours per skill and compare each sum with that skill's capacity.
4. Note declared absences, because "This will help us know how much we can commit to" (L5797). In the case Rose is away 2 days and Allan perhaps 1 (L5814-L5815).
5. Repeat until the tightest skill says it is close to full.
6. Add work that is not a story so that it is accounted for. Here that was 12 hours of research and "four board and piece sets at four hours each" (L5923, L5925).
7. Check the aggregate last, as a sanity check only.

| Story | Programming | Testing | Artwork |
|---|---|---|---|
| Weak engine, rings | 48 | 36 | 0 |
| Human vs human | 12 | 14 | 4 |
| Weak engine, bridges | 44 | 38 | 0 |
| Total | 104 | 88 | 4 |

Table 23.11 (L5894) labels its first row with the human-vs-human story. Its 48 and 36 are the rings hours of Table 23.7, so this wiki reads that label as a misprint in this copy of the source.

Programming stands at 104 hours against 120, from "two programmers each getting 30 hours a week" (L5903). Testing stands at 88 hours against Prasad's 60, which holds only because Rose and Delaney offer to help (L5909-L5913). With the 28 added hours the total is 224.

### The total hides the tightest stage

The aggregate looks comfortable, and the case explicitly distrusts it:

> It’s 224 hours in total now. With five of us on the project— Allan, Prasad, Rose, Delaney, and me—this works out closer to five hours a day. But that’s if all the work and each of us is interchangeable. We’re not.
>
> — [[cohn-agile-estimating-planning]], L5929

**Failure mode, overflow at one stage.** Sign: the total fits while one stage's sum exceeds its capacity, as testing does here at 88 against 60 under a total that looks fine. The same check is on [[iteration-capacity]], without the worked numbers.

## Which setup this applies under

Under an iteration setup, as above. Under a flow setup nothing is selected for a period, so this page does not apply: the Kanban Guide replenishes on a capacity signal ([[what-may-move]]).

## Agent executor note

The Guide's inputs survive as inputs. Their contents shift.

- **Past performance** only counts if it comes from the same setup. A changed model or a changed way of reviewing makes older periods a poor guide.
- **Capacity** in the Guide means the Developers' time. With an agent executing, this wiki reads the limiting capacity as what the people steering can review in a period, not what an agent can run. That reading is unmeasured.
- **Sizing** is the Developers' job: "The Developers who will be doing the work are responsible for the sizing." (L280). This assumes the estimator also executes. No source in this wiki says whether an agent's own estimate can fill that place ([[size-ceiling]]), so the rule's source and its setting do not match here.
- **Hours per person and per skill** in Cohn's case do not transfer, and the plugin does not produce the level they count. The structure does: find the stage everything has to pass through, which for a few people steering an agent is likely the review of presented results, and fill against that and not against a total.
- **Slack** in Cohn's words protects "every team member’s time" (L4941), and an agent has no time of that kind to protect. This wiki applies the rule to the capacity that limits the project, as above. That reading is unmeasured.
