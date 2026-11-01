---
title: Filling a Period
category: periods
summary: How much to select for an iteration; the Scrum Guide names three inputs, past performance, upcoming capacity and the Definition of Done, and gives no formula. Selection applies only under an iteration setup.
tags: [rule, iterations, forecast, scrum]
sources: [scrum-guide-2020]
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

## Why

Empiricism is the Guide's stated reason: "Only what has already happened may be used for forward-looking decision making." (L202). What breaks if it is ignored is the forecast's meaning, because a selection chosen by hope tells the people steering nothing about what will happen.

## Which setup this applies under

Under an iteration setup, as above. Under a flow setup nothing is selected for a period, so this page does not apply: the Kanban Guide replenishes on a capacity signal ([[what-may-move]]).

## Agent executor note

The Guide's inputs survive as inputs. Their contents shift.

- **Past performance** only counts if it comes from the same setup. A changed model or a changed way of reviewing makes older periods a poor guide.
- **Capacity** in the Guide means the Developers' time. With an agent executing, this wiki reads the limiting capacity as what the people steering can review in a period, not what an agent can run. That reading is unmeasured.
- **Sizing** is the Developers' job: "The Developers who will be doing the work are responsible for the sizing." (L280). This assumes the estimator also executes. No source in this wiki says whether an agent's own estimate can fill that place ([[size-ceiling]]), so the rule's source and its setting do not match here.
