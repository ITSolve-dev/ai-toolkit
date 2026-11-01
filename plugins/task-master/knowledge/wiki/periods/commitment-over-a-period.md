---
title: Commitment Over a Period
category: periods
summary: What a project actually promises; the Scrum Guide commits to a Sprint Goal and only forecasts the items, Cohn commits to the functionality of the selected stories and keeps the goal loose, the Kanban Guide has no period and forecasts per item, and under every setup a list of sub-steps is never the commitment.
tags: [decision-rule, commitment, iterations, scrum, kanban, cohn]
sources: [scrum-guide-2020, kanban-guide, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Commitment Over a Period

A commitment is what the project will answer for at the end of a time span. The sources differ on this more sharply than on anything else, and the setup decides which holds.

## Scrum Guide: the goal is the commitment

> The Sprint Goal is the single objective for the Sprint. Although the Sprint Goal is a commitment by the Developers, it provides flexibility in terms of the exact work needed to achieve it.
>
> — [[scrum-guide-2020]], L301

The Guide does not make the items the commitment. Its word for the selection is a forecast: "the more confident they will be in their Sprint forecasts" (L222). Its other two commitments are a Product Goal for the backlog and the Definition of Done for the Increment (L266-L270). The Product Goal comes one at a time: "They must fulfill (or abandon) one objective before taking on the next." (L291).

This wiki reads that as the central point. The Guide promises an outcome and leaves the list of work free to change, and [[mid-period-change]] is the same idea applied during the period.

## Kanban Guide: no period, a forecast per item

The Kanban Guide has no period and uses the word "commitment" only as a benefit of limiting WIP (L143). Its nearest equivalent is the [[service-level-expectation]], a forecast with a probability for each item. Nothing in the Guide promises what a given week will contain.

## Cohn: the functionality, and not the tasks

Cohn rejects a commitment to tasks, commits to the functionality of the selected stories, and treats the iteration goal as a unifying statement. He asks a team to commit to "the features we’ve discussed", and says of the alternative wording:

> That is a very different question, and a far weaker commitment since it is a commitment to complete a set of tasks rather than a commitment to deliver new functionality.
>
> — [[cohn-agile-estimating-planning]], L3293

Cohn's reason is what happens when work is discovered, which he expects: "a team that is committed to delivering the functionality described by a user story will try to complete the new tasks as well", and a team that committed only to a list may not (L3295-L3299).

The fictional case study in Chapter 23 (L4961) gives the position its plainest wording. Asked which of the two a team commits to, the coach answers:

> You commit to the story. We identify the tasks as a way of seeing how much work is involved and of helping us make the commitment. Because you’re committing to the story, not just the tasks, it’s important that you think about this as a whole team commitment. At the end of the iteration I don’t want Sasha to say she’s done with the state management classes but that Allan isn’t done. That wouldn’t do you any good. You can think about tasks, but you commit to stories.
>
> — [[cohn-agile-estimating-planning]], L5779

This wiki reads the sub-steps here as a measuring instrument: they show how much a story holds and whether it fits, and they are not what gets delivered. What breaks when that is ignored is the period's end, which arrives with a stack of finished sub-steps and nothing to present. The source's stated cost is that partial completion by one contributor is worth nothing to the team (L5779). Who holds which sub-step during planning is on [[tasks-are-not-assigned-at-planning]].

### What gives way

Discovered work can still overflow. Then the team must "discuss the situation with the product owner and see if there is still a way to meet the iteration goal; they may need to reduce the functionality of a story or drop one entirely" (L3299). This wiki reads that as agreeing with the Scrum position in the case that matters: when the two collide, the goal survives and the selection gives way.

### How specific a goal must be

> The iteration goal is a unifying statement about what will be accomplished during the iteration. It does not have to be very specific.
>
> — [[cohn-agile-estimating-planning]], L3138

Cohn calls "Make progress on reports" a good goal that needs no narrowing to "Finish 15 reports" (L3138). A goal must still match the selection: if the export story falls too low to be included, a goal of all demographics features should be re-stated as "The most important demographics features are finished." (L3152).

## Resolving the goal's looseness

This resolution is this wiki's. Cohn's looseness and the test below, that a commitment was shaped wrongly if nobody can say at the end whether it was met, look like a conflict, but they sit on different objects. For Cohn the goal is not the commitment, since the commitment is to the stories, so a goal nobody can score costs little. Under a setup where the goal is the commitment, as in the Scrum Guide, it must be decidable. "Make progress on reports" fails that test and should not be used as the period's commitment.

## The decision

Ask what the project will answer for, and read it from the setup.

- **Iteration setup, the goal is the commitment:** one objective for the period, which may be loose about amount but must be decidable at the end. Selected tasks are a forecast of how to reach it. A period is reported as goal met or not met, and not as a share of items finished.
- **Iteration setup, the selected tasks are the commitment:** a looser goal is acceptable, and the report is per task on functionality delivered.
- **Flow setup:** no period commitment exists. Each started task carries the SLE. A question about what will be done by a date is a forecast from history, computed on [[single-item-forecast]] for one item and [[monte-carlo-simulation]] for several, and stated as on [[forecast-range-and-probability]].
- **Iterations with a WIP control:** the period's commitment is as in the two iteration cases, and the SLE, if the project keeps one, is a forecast inside it. Whether stories fit the period at all can be read from history on [[iteration-length-versus-cycle-time]].
- **Under every iteration setup:** a list of sub-steps is never the commitment. The work that must be covered is on [[all-work-to-finished-is-in-the-plan]].

The sources do not resolve this between them, because each describes only itself. The per-setup statement is this wiki's. How the amount is chosen is on [[velocity-versus-commitment-planning]].

## Sign of violation

- **In the goal's text, where the goal is the commitment:** the goal restates the selection, so that removing any item would break it. The Guide says a goal "provides flexibility in terms of the exact work", so a goal with no such flexibility is a list.
- **In the goal's text, under any iteration setup:** a goal saying "all" of something while the selection omits part of it.
- **In a report on a period, where the goal is the commitment:** results are given as items promised against items delivered, with the goal unmentioned.
- **In a report on a period, under any iteration setup:** all planned sub-steps done, while the functionality does not work.
- **In a report on a period, under any iteration setup:** finished sub-steps are counted, or one contributor is reported done while the task stays open.
- **In board state at period end:** a task still open with some of its sub-steps closed. This raises a question for [[unfinished-at-period-end]] and is not a verdict.
- **In board history, where the goal is the commitment:** a period closed as a failure with its goal met, or as a success with its goal missed.
- **In board history:** discovered work left out of the period with no recorded decision on reduced functionality or a dropped task.
- **On a flow board:** a date given for a batch of items, with no history behind it.

These signs are this wiki's.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Whether the project has fixed periods | Project configuration |
| Whether the goal or the selection is the commitment | Project configuration, or the period's record |
| The goal for the period | The period's record |
| Whether one objective can be stated for it | The tasks being considered |

The commitment was shaped wrongly if the goal went obsolete during the period, or if, where the goal is the commitment, nobody could say at the end whether it was met.

## A period versus a milestone

Neither guide uses the word "milestone". The distinction below is this wiki's, built from what the Scrum Guide says about each.

- **A period fixes time and lets scope move.** Sprints are "fixed length events" (L189), and scope may be "clarified and renegotiated" (L198).
- **A milestone fixes a result and lets the date move.** The nearest thing in the Guide is the Product Goal, "a future state of the product" (L284), which has no date.

The test is which of the two gives way when they collide. If the date holds and scope gives, it is a period. If the result holds and the date gives, it is a milestone. A plan that fixes both has no room to absorb anything.

## What a period does not do

A period is not a release gate. The Guide says "an Increment may be delivered to stakeholders prior to the end of the Sprint. The Sprint Review should never be considered a gate to releasing value." (L309). The sign, in this wiki's wording, is finished tasks whose release dates cluster at the end of each period regardless of when they were finished. A task's finish point is on [[started-and-finished-points]].

## Agent executor note

The Guide says the goal is "a commitment by the Developers". An agent cannot answer for a commitment, so the commitment falls to the people steering, and an agent's report that a goal is met is only an input to their judgement. The Guide's claim that a goal creates "coherence and focus" (L301) is a claim about people working together. This wiki does not carry it over. What survives for an agent is the single objective as a test for what belongs in the period.

The whole-team reason at L5779 does not transfer either, since an agent has no share of a team to protect. The unit does: what is reported and judged is the presented result of the task, which fits the charter's test that a result is presented once ([[unit-of-work]]). That reading is this wiki's.

Cohn's claim that a committed team will take on new work is also a claim about people. This wiki reads its transfer as a property of the task text: an executor told to deliver a stated behaviour must treat discovered work inside that behaviour as part of the task, which needs acceptance criteria and not a list of steps ([[testable-acceptance]]). The call to shrink or drop stays with the people steering ([[mid-period-change]]).
