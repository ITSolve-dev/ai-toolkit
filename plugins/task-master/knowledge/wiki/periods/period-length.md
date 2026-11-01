---
title: Period Length
category: periods
summary: A period is a fixed length of one month or less, chosen by how long its goal stays valid against the shortest span in which something can finish; extending a period to fit its work is the sign of violation.
tags: [rule, iterations, scrum]
sources: [scrum-guide-2020, kanban-guide]
created: 2026-11-01
updated: 2026-11-01
---

# Period Length

The length of a period is fixed at setup and held. The Scrum Guide sets an upper bound and states the trade-off:

> They are fixed length events of one month or less to create consistency. A new Sprint starts immediately after the conclusion of the previous Sprint.
>
> — [[scrum-guide-2020]], L189

> Sprints enable predictability by ensuring inspection and adaptation of progress toward a Product Goal at least every calendar month. When a Sprint’s horizon is too long the Sprint Goal may become invalid, complexity may rise, and risk may increase. Shorter Sprints can be employed to generate more learning cycles and limit risk of cost and effort to a smaller time frame.
>
> — [[scrum-guide-2020]], L200

This wiki reads "one month" as a rule of the Guide with a stated condition, Scrum as defined there. It is an upper bound and not a recommendation, and the Guide gives no lower bound. The Guide also does not say how to pick a value below the bound. The method below is this wiki's, built from the trade-off the Guide names.

## Choosing the length

Choose the shortest length in which a typical selected task can finish and be reviewed, and no longer than the goal stays valid.

| Input | Read from |
|---|---|
| How long a task takes from started to finished | Board history |
| How long a goal has stayed valid in earlier periods | Board history: goals gone obsolete, and tasks added or dropped mid-period |
| How often the people steering can review | The people steering |

The length was too long if goals repeatedly go obsolete during the period ([[mid-period-change]]). It was too short if tasks repeatedly go back unfinished for reasons of size ([[unfinished-at-period-end]]), or if the review of one period runs into the next.

## The rule that detects

Once chosen, the length does not move to suit the work.

## Sign of violation

- **In board history:** a period's end date moved later while its work was unfinished.
- **In board history:** successive periods of different lengths with no change of setup recorded.
- **In board history:** a gap between periods, which contradicts "starts immediately after".

The signs are this wiki's derivation from L189.

## Why

What breaks is the comparison. Past performance only predicts the next period if the periods are alike, and [[filling-a-period]] rests on that. An extended period also hides the fact that the selection was too big, which is the evidence the period exists to produce.

## Cost

A fixed length leaves some periods with spare time and others short. The Guide accepts this and treats the fixed end as what makes inspection regular.

## Which setup this applies under

Under an iteration setup, as above. Under a flow setup there is no period. The Kanban Guide says reviews "can occur continuously, at regular intervals, or through a combination of both" ([[kanban-guide]] L137), so a regular interval there is a review habit and not a container for work.

## Agent executor note

The month is a figure from human teams, whose work takes days to weeks. An agent may finish a task in much less time, so the shortest usable length is likely set by the people steering and not by the executor. This wiki has no evidence of what length suits a few people steering an agent, and it reads the Guide's bound as a limit and offers no value inside it.
