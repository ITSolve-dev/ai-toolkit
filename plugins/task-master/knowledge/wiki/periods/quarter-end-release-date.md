---
title: Quarter-End Release Date
category: periods
summary: Do not aim a release or period end at a date where value steps down, such as a fiscal quarter end; Cohn's one-week slip past March 31 cost a full quarter's revenue recognition, and month-aligned periods hit a quarter end every third period.
tags: [rule, iterations, release-date, dates, cost-of-delay]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Quarter-End Release Date

Cohn advises against tying periods to month ends, because some of those dates carry a large step in value.

> If you tie iterations to the ends of months, one out of every three iterations will coincide with the end of a fiscal quarter.
>
> — [[cohn-agile-estimating-planning]], L3552

Cohn says the risk is greatest at public companies under pressure to hit quarterly revenue goals, and "not quite as much of a problem with private companies" (L3552).

## The case behind the rule

A significant release was set for Friday, March 31, 2000, after nine months of work. With two weeks left the product owner went on vacation, and although he tried to take part in calls, "some important work was not completed" in the final period (L3554). A shorter one-week period finished it, moving the release to April 7 (L3556). Revenue from the planned shipment could not be recognized until the next quarter: "We might as well have delivered on June 30 as April 7." (L3556). Cohn concludes: "I haven’t planned a month-end release since then." (L3558).

The rule rests on this one project. Cohn's "at all costs" (L3552) is stronger than one case supports, though the mechanism is clear enough to keep.

## The mechanism, generalized

This wiki reads the case as a step in value at a date. A one-week slip costs a week before the step and a full quarter across it, so the slip's size stops predicting its cost. The quarter end is one instance. Any date where something outside the project changes behaves the same way, which is the condition in [[a-date-is-not-urgency]]. The cost-of-delay reading is this wiki's ([[cost-of-delay]]).

## The rule that chooses

This wiki states the rule: a planned release date should not sit just before a step in value. Set it far enough ahead of the step that a normal slip lands before the step and not after it.

| Input | Read from |
|---|---|
| Whether a step exists at or near the date, and what changes there | The people steering, or the requester ([[clarifying-questions]]) |
| The planned date, and the period ends it falls on | The project setup |
| How far plans usually slip | Board history: planned against actual dates on earlier releases |

The source gives no margin, only that one week was too little, and this wiki does not supply a figure. The later fact that shows the choice wrong is a release that crossed the step, or a date moved forward for a step that turned out to have no effect.

## Sign of violation

- **In the plan:** a release date or final period end falling on or just before a known value step, with little room left in it.
- **In the setup:** periods aligned to calendar month ends, on a project where a quarter end has an external effect.

These signs are this wiki's derivation from L3552-L3558. A date with no outside effect is not a violation, and month-end alignment alone proves nothing.

## Cost

Dating a release ahead of a step gives up some time before it. Aiming for the start of a quarter also delays revenue that an on-time quarter-end release would have counted sooner, and the source does not weigh that.

## A related figure

Cohn says in passing that nine months "is the upper limit for how long a single release should be" (L3554). The aside gives no reasoning and no condition, so this wiki records it as his opinion and does not use it as a rule.

## Scale and setup

The case is from a publicly traded company shipping hundreds of copies. A few people steering an agent may have no fiscal step at all, so the rule fires only where the first input above finds one. It applies to dates in any setup, including a milestone under flow, though the warning about month-aligned periods needs periods.

## Agent executor note

The step-in-value mechanism does not involve an executor, so it survives unchanged. The trigger of the case does too, in a sharper form: the slip came from the owner being unavailable near the end. This wiki reads that as a warning for agent work, where questions wait on the people steering, and a date near a step should be checked against their availability.
