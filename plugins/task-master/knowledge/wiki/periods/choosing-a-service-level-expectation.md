---
title: Choosing a Service Level Expectation
category: periods
summary: Pick the percentile from the cycle time scatterplot together with whoever receives the work, usually starting at the 85th; it needs about 11 to 30 finished items from a process that obeys Little's Law, and three mistakes each have a sign.
tags: [decision-rule, estimation, cycle-time, percentiles, commitment]
sources: [vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Choosing a Service Level Expectation

Choosing a [[service-level-expectation]] means picking which percentile of past cycle time the team will commit to. It is a choice about how often a miss is acceptable, so it is made with the receiver of the work, from data the team has already looked at. The source calls the same thing an SLA; see the note on the name on the SLE page.

## Inputs and where each is read from

- **Percentile lines:** the cycle time scatterplot built from board history ([[cycle-time-percentile-lines]]).
- **Tolerance for missing:** asked of the customer or stakeholder. It is not on the board. "They may opt" for a shorter SLE with more uncertainty, or a longer one with more certainty ([[vacanti-actionable-agile-metrics]] L3074-L3080).
- **Context the team lacks:** "Our customers and stakeholders almost certainly have contextual information that we do not that will have some bearing on our choice of an SLA." (L3080)

## The choice

Given lines at 20 days (50th) and 43 days (85th), a customer content to see half of commitments missed gets 20 days at 50%, and one who wants more certainty gets 43 days at 85% (L3028).

The default starting point is an observation from Vacanti's experience, not a rule: most teams start at the 85th percentile (L3030). Whether the standard percentiles fit a given context is deferred to a later book: "begin with these standard ones and experiment from there" (L3052). [[flow-metrics-scrum-teams]] names settings for a forecast of a period, on [[throughput-monte-carlo]] (its L954). This wiki reads them as a starting point for an SLE as well, which the book does not say.

The goal after choosing has two stages: "first meet that SLA at least 85% of the time (true predictability)" (L3036), then lower the number of days the percentile stands for.

## How much data

> As few as maybe 11 or 12. Probably no more than 30.
>
> — [[vacanti-actionable-agile-metrics]], L3054

That figure is conditional. Vacanti immediately says "The bigger question is in terms of quality not quantity." (L3054) The better a process obeys the assumptions of [[littles-law]], the fewer points it needs, and one that keeps violating them gets no trustworthy confidence level from any amount of data (L3054-L3060). The figure is from his practice and is stated without a study behind it.

This wiki adds a consequence: a project with fewer than about a dozen finished items has no SLE to read from history. The Kanban Guide's best guess stands in until then, labelled as a guess, and anything that depends on a measured SLE, such as [[right-sizing]], has only that guess to stand on. How little a percentile says on few dots is on [[cycle-time-percentile-lines]], and what can be said below that point is on [[how-much-flow-data]].

## What later fact shows the choice wrong

This test is the wiki's reading of the stated goal (L3036): the share of finished items at or under the SLE stays below the stated confidence. At 85%, more than 15% of items finishing late means the commitment is not being met, and the question is whether the percentile or the process is at fault. Each miss also gets its own question: "Why did we miss the SLA?" (L3022)

## Three mistakes and their signs

Vacanti names three (L3062-L3068). The signs are this wiki's phrasing of what each would look like.

1. **Set without analysing cycle time data.** Sign: no scatterplot or percentile behind the published number. The mistake is not disagreeing with the data: "there is nothing (necessarily) wrong with choosing an SLA that is not supported by the data" (L3070), so an 85th percentile of 45 days can sit beside a published 35 days at 85%, provided the choice follows a look at the data (L3070). This wiki notes that such an SLE is predicted by its own data to be missed more often than it claims.
2. **Set by an external manager or management group.** Sign: the number arrives from outside the people doing the work. The reasoning is ownership: "Since it is the team who is making the commitment, it should be the team that chooses what that commitment point is." (L3072)
3. **Set without the customer or stakeholders.** Sign: the receiver of the work cannot say what confidence they agreed to.

The source rules out two parties and admits one: the only other party in the decision is a customer or stakeholder (L3072).

## Trade-offs

A higher percentile buys certainty with a longer promise, and how much it costs depends on the shape of the data: see [[percentile-spread]], where 15 points of confidence cost more than double the days. In that real case the customer chose the 70% SLE to start (L3050).

## Per setting

This section is the wiki's reading. On a project of a few people steering an agent, mistakes 2 and 3 can collapse into one person: the person steering is both the team and the customer. Mistake 1 stays fully applicable, since it needs only board history.
