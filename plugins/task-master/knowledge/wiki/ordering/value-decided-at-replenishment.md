---
title: Value Decided at Replenishment
category: ordering
summary: Vacanti weighs value only when choosing what enters the process, and pulls committed work for predictability thereafter. This wiki resolves his objection to cost of delay by moment; ratings order what has not started, age orders what has, with a narrow exception.
tags: [decision-rule, ordering, class-of-service, cost-of-delay, pull-policy]
sources: [vacanti-actionable-agile-metrics, black-swan-qualitative-cod]
created: 2026-11-02
updated: 2026-11-02
---

# Value Decided at Replenishment

Two decisions look alike and take different inputs: what enters the process, and in what order committed items move through it. Vacanti puts value on one side of that line only:

> I do believe that the business value of an item should be considered, but I believe it should only be considered at input queue replenishment time. After an item is placed in process then I believe the best long term strategy is to pull that item—and all other items—through the process as predictably as possible.
>
> — [[vacanti-actionable-agile-metrics]], L3454

Vacanti lumps cost of delay and risk management in with business value for this argument (L3444), so this wiki reads the rule as covering them too.

## The reasoning

- **Value is known late.** Vacanti argues that value is determined by customers, so "an item’s true value can only be known once put in the hands of the customer" (L3444). A business case is a proxy for it.
- **A pull preference is a bet, and it stakes more than one item.** By giving preference, you gamble that the preferred item is worth more. If that is wrong "you will have not only lost the bet on the expedited item, but you will have also lost the bet for every other item in progress that you skipped over." (L3452).
- **Value depends on the time to deliver.** "If you cannot answer the question “how long?” then how much confidence can you really have in your business value calculation?" (L3454). This wiki reads that as saying that predictability feeds the value judgement and does not merely compete with it.

Vacanti's assertions about how often the bet is lost, and about how many business cases are fiction, state a size of effect with no measurement, and he half withdraws them ("I am only mostly that cynical", L3454). This wiki keeps the mechanism and leaves those sizes out.

## The disagreement, and its resolution

This wiki's ordering pages compare tasks by [[cost-of-delay]], and Vacanti names "fictional Cost of Delay calculations" as no reason to leave FIFO (L3390). The two positions conflict less than the wording suggests, because they concern different moments. The following resolution is this wiki's.

| Moment | What decides | Page |
|---|---|---|
| The item has not started | Value and urgency rating; reordering costs nothing | [[ordering-by-value-and-urgency]] |
| The item has started, a slot freed | Age in process | [[fifo-pull-order]] |
| A top-rank task arrives while work is started | A declared exception | [[interrupting-started-work]] |

The third row is not a loophole taken against Vacanti. He grants it himself for "obvious high value expedites": production down, or a regulatory requirement with massive fines (L3456). The sources differ on where the line falls. The cost-of-delay source allows a switch when a very high item waits behind medium or low work, and Vacanti wants those cases rare and designed for ([[slack-for-expedites]]).

Under a flow setup, replenishment is each refill of the input queue, so ratings are read fresh at each refill ([[just-in-time-prioritization]]; [[cost-of-delay]] changes over time). Under an iteration setup, this wiki reads selection for the period as the replenishment moment ([[reprioritize-before-each-iteration]]), with the same rule for pull order inside the period. Vacanti does not discuss iterations in this chapter.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Whether the item has started | Board state, at the [[started-and-finished-points]] |
| Value and urgency rating | The task, read again today ([[ordering-by-value-and-urgency]]) |
| Whether a true exception applies | [[interrupting-started-work]] |

The tests here are this wiki's. The choice was wrong if a committed item lost real value while waiting behind older work, in a way that a rating made at the time would have shown, and if that happens repeatedly. A recurring case points to too much in process or too slow a refill, and only after those to the rule.

## Failure sign

This sign is this wiki's derivation and raises a question. **In history:** started items are overtaken by later-started ones because of a higher rating, with no recorded exception. The rating has then been used as a [[class-of-service]].

## Cost

Committed work cannot respond to new information about its value, short of the exception. That cost is lower when little is in process and when items are small, because new value waits for less.

## Agent executor note

The distinction between entering and moving does not depend on the executor, so it survives. Value is judged by the people steering in either case. Where parallel agent runs mean a started task blocks nothing at execution, this wiki expects the conflict to appear only at review, where a person still chooses what to look at first. This reading is this wiki's and is unmeasured.
