---
title: When to Use Class of Service
category: moving-work
summary: Start with no classes; build the process, operate it, measure it, and add one only if the data calls for it. For a single item, decide at commitment by comparing its due date with the forecast; if the forecast finishes first, it gets no preference.
tags: [decision-rule, class-of-service, pull-policy, forecast, due-date]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# When to Use Class of Service

This rule decides two things: whether a process has a [[class-of-service]] at all, and whether a given committed item gets a preferential pull. Vacanti's answer to the first is to start without one:

> You have to know what you are doing before you do it. Build your process. Operate it using the policies for predictability that I have outlined thus far. Measure it. And then make a determination if CoS can help. Chances are you will never need CoS.
>
> — [[vacanti-actionable-agile-metrics]], L3482

Vacanti closes with the same order: "Only introduce CoS after you have operated your process for a while and are confident that CoS is necessary." (L3520). He also asks that even then policies be chosen to mitigate the negative impact on flow (L3520), and that other ways of removing or mitigating the need be tried first (L3518). He does not forbid classes: "I am not saying that CoS is inherently evil or that all CoS implementations are incorrect" (L3470), and he says he argues from predictability only (L3476).

His "Chances are you will never need CoS." is a judgement and carries no measurement. This wiki keeps the order of steps and not the likelihood.

## The item-level test

The class is decided at the item's first pull and not before (L3256). Vacanti's worked case is an item pulled on February 1 with a due date of February 28, in a process whose SLA is 11 days. The forecast finishes well before the date, so "there would be no point in giving it any preferential treatment" (L3256).

This wiki reads a test from that case. At commitment, compare the time left until the date with the forecast for the process. If the forecast fits, the item gets the ordinary pull order. The chapter does not treat the opposite case, in which the date falls inside the forecast. This wiki reads that as the only case where a preference is even a question, and it is then answered on [[interrupting-started-work]] and [[slack-for-expedites]]. A date also counts here only if something outside the project changes at it ([[a-date-is-not-urgency]]).

Vacanti writes "SLA" for a figure that "would predict" completion (L3256), so this wiki reads it in the forecast sense of [[service-level-expectation]]. His FedEx example uses "the agreed SLA" (L3404), which is a promise to a customer. The figure compared above is the forecast, and it comes with a probability, so a fit is likely and not guaranteed.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Cycle time history | Board history ([[flow-metrics]]) |
| The forecast and its probability | [[service-level-expectation]] |
| The item's date, and what happens at it | The task's text ([[a-date-is-not-urgency]]) |
| How often exceptions happened | Recorded exceptions ([[slack-for-expedites]]) |

The tests here are this wiki's. Withholding a class was wrong if dated items that passed the test keep missing dates that had real consequences. Adding a class was wrong if ordinary items get slower or more spread out afterwards and the preferred items did not gain enough to justify it.

## Observable signs of skipping the order

These signs are this wiki's derivation and each raises a question ([[smell-is-not-a-finding]]).

- **At setup:** classes are defined for a board with no finished work behind it.
- **On the board:** an item with a distant date receives priority because it has a date.
- **In history:** classes exist, and no comparison of cycle times from before and after them was ever made.

## Cost

Going without classes leaves no fast path by policy until the data supports one. Real emergencies still go through the declared exception.

## Which setup this applies under

The chapter treats a continuous flow board. The item-level test needs a forecast per item, which a flow setup has and an iteration setup does not require ([[service-level-expectation]]). Under an iteration setup, this wiki reads the period itself as the coarse check, and a date beyond the period's end raises no pull question inside it.

## Agent executor note

The order of steps does not depend on who executes. The forecast does, since a human team's history does not transfer to an agent ([[service-level-expectation]]), so a new project has no measurement to base a class on. This wiki reads that as a further reason to start without classes, and the reading is unmeasured.
