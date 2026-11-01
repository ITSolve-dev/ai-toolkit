---
title: Service Level Expectation
category: periods
summary: Kanban's forecast of how long an item should take from started to finished, stated as an elapsed time and a probability and read from cycle time history; it is per item, a forecast and not a promise, and its example figures are not targets.
tags: [rule, forecast, kanban, flow-metrics]
sources: [kanban-guide, scrum-guide-2020, radzikowska-waiting-blocked, kanban-playbook-right-sizing]
created: 2026-11-01
updated: 2026-11-01
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
- **The phrase "enough historical data" is undefined.** The Guide gives no count.

Cycle time is defined on [[flow-metrics]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Cycle times of finished items | Board history: timestamps at the [[started-and-finished-points]] |
| The probability | Chosen at project setup |
| The items that count as comparable | Items with the same started and finished points |

The SLE was wrong if, over later items, the share finishing within the stated time is far from the stated probability. A share much higher than stated means the SLE is too loose to warn anyone. A share much lower means it no longer describes the workflow.

## What it is used for

The Guide's use is aging: "Ensuring work items do not age unnecessarily, using the SLE as a reference." (L134). See [[overrun-triggers-a-recut]].

The Kanban Playbook adds a second use, before a task starts: is there a good chance it finishes within the SLE? ([[kanban-playbook-right-sizing]] L30). See [[size-ceiling]], which also deals with the circle this creates. The Playbook warns that history full of oversized or tiny items "reflects that noise, not your system's real performance." (L22). This wiki reads that as a reason to compare like with like, and it does not take from it that an SLE is useless until a project has right-sized.

## Two meanings of SLE

The term does not mean one thing across this wiki's sources. In the Kanban Guide an SLE is a forecast with a probability, from started to finished. In the Kanban Maturity Model text on [[waiting-versus-blocked]], "agreed waiting time (service level expectation \[SLE\])" ([[radzikowska-waiting-blocked]] L53) is an agreed time on one outside wait, and passing it changes an item's state. This wiki uses SLE in the Guide's sense, and calls the other an expected end.

## Which holds under which setup

- **Flow setup:** required, and it is the only forecast the setup has.
- **Iteration setup:** not required. The Scrum Guide forecasts a whole selection, not an item ([[filling-a-period]]), and the period is the coarse limit.
- **Iterations with a WIP control:** optional, and useful as an earlier warning than the period's end, because age can be checked while a task is open.

The resolution is this wiki's. An SLE under a period is capped in practice by the period's length, so history from such a project is not comparable with history from a flow setup.

## Cost

An SLE needs finished items, and a few people finish few of them. On a small board a percentile rests on a handful of items, so one outlier moves it. That caution is this wiki's, and the Guide does not discuss small samples.

## Agent executor note

The SLE is read from a project's own history, so it survives a change of executor better than any borrowed figure does. Three cautions apply, and all three are this wiki's reasoning, unmeasured.

- A human team's SLE does not transfer to an agent, so a new project starts from the Guide's "best guess".
- An agent-run task's cycle time includes the time it waits for a person, so the SLE may mostly measure review and not execution.
- Changing the model, or how tasks are reviewed, changes the system the history describes, so older history then stops applying.
