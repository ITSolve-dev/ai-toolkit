---
title: A Date Is Not Urgency
category: ordering
summary: A date on a task raises its urgency only if something outside the project changes at that date; such a date moves the task up the urgency bands as it approaches, and a date with no outside effect leaves urgency where it was.
tags: [decision-rule, ordering, cost-of-delay, dates, prioritization]
sources: [black-swan-qualitative-cod]
created: 2026-11-01
updated: 2026-11-01
---

# A Date Is Not Urgency

A task often arrives with a date, and the date reads as urgency. This rule decides whether it is. The source's answer has two parts.

> **How to deal with dates??** An important question, and one that is often misunderstood because the date is (more often than not) simply an *internal* date and is unconnected with any *external* effect if things are delayed. At any rate, to handle dates you just have to dynamically shift the urgency. As an example: the urgency could start off as “whenever”, and then as the option expiry date approaches it could shift into “soon” – and then finally, as the option expiry date gets very close it can shift into the “ASAP” band.
>
> — [[black-swan-qualitative-cod]], L62

The author also says most dated things start with no cost of delay at all: "it comes as a surprise to many people that most of the things that have a date attached to them start off with a Cost of Delay of $Zero/week." (L64). That statement is the author's experience of quantifying, and the article shows no count behind it. The same goes for "the Cost of Delay beyond that date is exactly the same as the Cost of Delay before that date (an all too common scenario, I’m afraid)" (L99), which is the failure case this rule exists for.

## The rule

1. Ask what changes outside the project at the date, if the work is not done.
2. **If nothing changes,** the date does not affect urgency. Rate urgency as if the date were absent ([[ordering-by-value-and-urgency]]).
3. **If something changes,** urgency depends on the time left. A task may start at Whenever and move to Soon and then to ASAP as the date approaches; the source's example says "could start off" (L62).
4. Work out the band when the order is decided, from the date and the current day. Do not store it.

## How close is close

The author gives no distance, only "approaches" and "very close" (L62). This wiki does not supply a figure. It reads closeness against how long the task takes: a task reaches ASAP when the time left is about what such tasks need, because after that point starting later means missing the date. That time is read from the project's own history ([[service-level-expectation]]), or from the size where there is no history. This reading is ours.

This wiki reads Soon the same way, one step earlier, and this reading is also ours: a task reaches Soon when the time left no longer covers both its own time and the time of the tasks ahead of it in the order, so it can still make the date but not if it waits its turn. The input is the same history, summed over the tasks ranked above it. The source gives no figure for Soon either, leaving it to context (L57).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The date | The request |
| What happens at the date if the work is late, and to whom | The request, or the requester's answer ([[clarifying-questions]]) |
| How long such a task takes | Board history ([[service-level-expectation]]), or the task's size |
| The current day | The clock, each time the order is decided |

The source does not state what would show this wrong, so these tests are this wiki's.

- **A date was treated as external and it was not:** the date passed with the work unfinished and nothing happened. Read this from board history against the sentence saying what would happen.
- **A date was treated as internal and it was not:** the date passed and a loss followed that the rating said would not.
- **The band moved too late:** the date was external, the task was started on the shift to ASAP, and it still missed.

## What counts as outside

The author contrasts "internal" and "external" (L62) without defining them. This wiki's test is whether anyone beyond the people steering loses something at that date. A date promised to a client or a user is external by this test, even if it was invented, because breaking it has an effect on someone. A date a person set for their own planning is internal. A wish for a date with no reason attached is also internal, until a reason is given.

## Cost

A person who set an internal date may still care about it, and the rule takes the urgency away from it. The author calls this use of dates an "anti-pattern of coercion by dates" (L64), and this wiki does not take a position on that. A plugin following the rule should show the date and say why it did not raise the band, so the person steering can correct the reading.

A deadline can also reach the board by another route. The author says of a date estimate: "Once the cat is out of the bag though, it tends to be the thing that gets communicated as a “deadline”" (L99). So a forecast can come back as a date. This wiki's reading is that a forecast from [[commitment-over-a-period]] or [[service-level-expectation]] is not a date in the sense of this page, until someone outside depends on it.

## Agent executor note

The rule concerns dates and outside effects and not the executor, so it survives. It also suits a plugin, because the band can be worked out afresh each time from stored facts. The evidence is one practitioner article with no measurement.
