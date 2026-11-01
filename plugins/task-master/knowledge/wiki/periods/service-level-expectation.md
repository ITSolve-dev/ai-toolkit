---
title: Service Level Expectation
category: periods
summary: A per-item statement of how long an item should take from started to finished, as an elapsed time and a probability read from cycle time history; the Kanban Guide calls it a forecast and Vacanti a small-c commitment owed at the moment of pulling, it carries no penalty, and its example figures are not targets.
tags: [rule, forecast, commitment, kanban, flow-metrics, cycle-time, percentiles]
sources: [kanban-guide, scrum-guide-2020, radzikowska-waiting-blocked, kanban-playbook-right-sizing, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# Service Level Expectation

A service level expectation (SLE) is the Kanban Guide's forecast of how long one item should take. This rule chooses: it fixes the expectation that aging and sizing are then judged against.

> A service level expectation (SLE), which is a forecast of how long it should take a work item to flow from started to finished. The SLE itself has two parts: a period of elapsed time and a probability associated with that period (e.g., “85% of work items will be finished in eight days or less”). The SLE should be based on historical cycle time and, once calculated, should be visualized on the DoW. If historical cycle time data does not exist, a best guess will do until there is enough historical data for a proper SLE calculation.
>
> — [[kanban-guide]], L115

This wiki reads the following from that passage.

- **Both parts are required.** "Eight days" is not an SLE without its probability.
- **85% and eight days are the Guide's example.** They are not a recommended level. Neither figure comes with a setting, so they carry no information about what a project should expect.
- **It is a forecast.** The Guide calls it that, and it does not call it a commitment. An item may miss it by design, since the probability is below 100%.
- **It is per item.** It says nothing about what a period will contain.
- **The phrase "enough historical data" is undefined.** The Guide gives no count. Vacanti does: see [[choosing-a-service-level-expectation]].

Cycle time is defined on [[cycle-time]].

## Vacanti: owed at the moment of commitment

Line references in this section and the next two are to [[vacanti-actionable-agile-metrics]]. Vacanti treats the statement as the other half of deferred commitment: a team that delays committing until it pulls an item owes a forecast at that moment ([[just-in-time-commitment]]).

> we must—at the time of commitment—also communicate to our customers a date range and confidence level for each and every committed-to work item.
>
> — [[vacanti-actionable-agile-metrics]], L3012

The range is not guessed for the item. It is read from the percentile lines on the scatterplot of finished work (L3026; [[cycle-time-percentile-lines]]). In the book's example (Figure 10.5) the 50th, 85th and 95th percentiles of cycle time are 20, 43 and 63 days:

> any item that enters our process has a 50% chance of finishing in 20 days or less, an 85% chance of finishing in 43 days or less, or a 95% chance of finishing in 63 days or less.
>
> — [[vacanti-actionable-agile-metrics]], L3028

This wiki reads that sentence as true only while the process that produced the data keeps behaving the same way: the chapter makes the same point when it says the quality of the data depends on how well the process obeys the assumptions of [[littles-law]] (L3054). The figures are one chart's and carry no target.

## The name

The book's chapter uses "SLA" because the industry does, and Vacanti objects to the term himself.

> SLA sounds too much like the language of formally negotiated contracts with penalties for nonconformance.
>
> — [[vacanti-actionable-agile-metrics]], L3014

> Better nomenclature for the concept of a SLA, in my opinion, is “Service Level Expectation” or “Cycle Time Target”.
>
> — [[vacanti-actionable-agile-metrics]], L3024

This wiki uses SLE for the concept and keeps "SLA" only inside quotations and when reporting the source's wording.

## Forecast or commitment

The Kanban Guide says forecast and Vacanti says commitment, about the same statement. This wiki reads the gap as smaller than the words: Vacanti's commitment is the small-"c" kind ([[just-in-time-commitment]]), and he separates it from a contract with the same test as the Guide's probability.

- **SLE versus contract.** A contract carries a penalty for missing it. An SLE does not: "A team or an individual should not be punished for missing these commitments" (L3022). A miss starts a question instead: "the team should take any missed SLA as an opportunity to learn." (L3022)
- **SLE versus estimate of an item.** An estimate is a statement about one item. This wiki reads an SLE as a statement about the process, applied to each item as it enters. No item-level number is produced: the only item-level question it leaves is the yes/no of [[right-sizing]].

What is left of the difference is who stands behind it. This wiki reads the choice of a percentile as the step that turns a forecast into something agreed, which matches the separation on [[estimate-versus-commitment]]: history gives the probabilities, and choosing one with the receiver of the work is the decision. A statement read off the chart and never agreed stays a forecast.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Cycle times of finished items | Board history: timestamps at the [[started-and-finished-points]] |
| The probability | Chosen at project setup, with whoever receives the work: [[choosing-a-service-level-expectation]] |
| The items that count as comparable | Items with the same started and finished points |

The SLE was wrong if, over later items, the share finishing within the stated time is far from the stated probability. A share much higher than stated means the SLE is too loose to warn anyone. A share much lower means it no longer describes the workflow.

## What it is used for

The Guide's use is aging: "Ensuring work items do not age unnecessarily, using the SLE as a reference." (L134). See [[overrun-triggers-a-recut]]. Vacanti's chapter conclusion names the same use with the commitment beside it:

> SLAs not only allow teams to make commitments at the individual work item level, but they also give us extremely useful information about when teams need to intervene to ensure the timely completion of those items.
>
> — [[vacanti-actionable-agile-metrics]], L3166

The intervention points are on [[percentile-intervention-triggers]].

The Kanban Playbook adds another use, before a task starts: is there a good chance it finishes within the SLE? ([[kanban-playbook-right-sizing]] L30). See [[size-ceiling]], which also deals with the circle this creates. The Playbook warns that history full of oversized or tiny items "reflects that noise, not your system's real performance." (L22). This wiki reads that as a reason to compare like with like, and it does not take from it that an SLE is useless until a project has right-sized.

Vacanti goes further, on a condition: "if a team follows all of the principles presented in this book" ([[vacanti-actionable-agile-metrics]] L3166), then "the SLA can be used as a substitute for many upfront planning and estimation activities" (L3172). See [[right-sizing]]. This wiki reads the condition as load-bearing, so a project breaking the assumptions of [[littles-law]] does not get this substitution.

## Two meanings of SLE

The term does not mean one thing across this wiki's sources. In the Kanban Guide an SLE is a forecast with a probability, from started to finished, and Vacanti's "SLA" is the same statement under another name. In the Kanban Maturity Model text on [[waiting-versus-blocked]], "agreed waiting time (service level expectation \[SLE\])" ([[radzikowska-waiting-blocked]] L53) is an agreed time on one outside wait, and passing it changes an item's state. This wiki uses SLE in the Guide's sense, and calls the other an expected end.

## Which holds under which setup

- **Flow setup:** required, and it is the only forecast the setup has.
- **Iteration setup:** not required. The Scrum Guide forecasts a whole selection, not an item ([[filling-a-period]]), and the period is the coarse limit.
- **Iterations with a WIP control:** optional, and useful as an earlier warning than the period's end, because age can be checked while a task is open.

The resolution is this wiki's. An SLE under a period is capped in practice by the period's length, so history from such a project is not comparable with history from a flow setup.

## Cost

An SLE needs finished items, and a few people finish few of them. On a small board a percentile rests on a handful of items, so one outlier moves it. That caution is this wiki's, and the Guide does not discuss small samples. Vacanti's claim that percentiles resist outliers is reconciled with it on [[cycle-time-percentile-lines]].

A higher probability costs a longer promise, by an amount that depends on the shape of the data: [[percentile-spread]].

## Agent executor note

The SLE is read from a project's own history, so it survives a change of executor better than any borrowed figure does. Four cautions apply, and all four are this wiki's reasoning, unmeasured.

- A human team's SLE does not transfer to an agent, so a new project starts from the Guide's "best guess".
- An agent-run task's cycle time includes the time it waits for a person, so the SLE may mostly measure review and not execution.
- Changing the model, or how tasks are reviewed, changes the system the history describes, so older history then stops applying.
- On a project of a few people the customer is often the person steering. The commitment then has less of an external audience, and its intervention use matters more than its promise.
