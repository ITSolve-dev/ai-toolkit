---
title: Cost of Delay
category: ordering
summary: What a piece of work loses by arriving later; it has two ingredients, value and urgency, which act on each other and do not add, it is usually a rate and not a sum, and it changes over time.
tags: [concept, ordering, cost-of-delay, prioritization]
sources: [black-swan-qualitative-cod]
created: 2026-11-01
updated: 2026-11-01
---

# Cost of Delay

Cost of delay is what a piece of work loses by arriving later. That one-line wording is this wiki's. The source gives the idea through its parts, and it is the comparison this wiki uses for what comes first. It asks how much is lost by waiting, and it does not ask how much the work is worth in general.

## Two ingredients that act on each other

> Cost of Delay has two essential ingredients: [Value](http://blackswanfarming.com/understanding-value/) and [Urgency](http://blackswanfarming.com/urgency-profiles/). To understand the Cost of Delay you really need to understand both. These ingredients are NOT additive ([as some might suggest](http://blackswanfarming.com/safe-and-weighted-shortest-job-first-wsjf/)), but rather they act on each other.
>
> — [[black-swan-qualitative-cod]], L29

This wiki reads "act on each other" as the point that matters for a rating. A task with high value and no urgency loses little by waiting, and so does a task with high urgency and little value. A sum would rank both in the middle and would hide that. The linked argument against addition has not been read, so the source's own reasoning on that point is not available here.

## A rate and not a sum

> One thing to remember is that Cost of Delay is NOT a sum of money, except in extreme examples of total loss due to delay. More typically, the value leaks away gradually – so it is almost always a rate. If you are delayed one week, then the Delay Cost incurred is often a fraction of what it would be if you were delayed by 10 weeks.
>
> — [[black-swan-qualitative-cod]], L73

This wiki reads that as two cases. In the usual one, every week of waiting costs something, so the order of work matters all the time. In the exception, the value is lost at one moment, such as when an opportunity closes ([[a-date-is-not-urgency]]). The author's text gives "total loss due to delay" and no example of it.

## It changes

> Cost of Delay is dynamic, and can change hugely between when you first triage the option and when it eventually becomes urgent enough to start work on it.
>
> — [[black-swan-qualitative-cod]], L64

The author adds that both ingredients can move: "Just because an idea or feature might initially plot as “Meh” and “Whenever” doesn’t mean that it can’t change along *both* axes." (L75). This wiki reads that as saying a rating has a date on it. A rating made at intake is a statement about that day and has to be read again before it decides anything later.

## What it leaves out

Cost of delay says what waiting loses. It does not say how much work a task takes, so a comparison by cost of delay alone ignores the capacity each task uses. That second step is on [[cost-of-delay-over-duration]].

It also does not say whether a task can be started: dependencies come first, from [[sequence-versus-wait]] and [[independent-tasks]].

## At what level it applies

The source speaks of ideas, initiatives and "your teams’ backlog of features" (L79). A task in this wiki can be smaller than a feature ([[unit-of-work]]). This wiki reads cost of delay as belonging to what delivers value on its own. A slice that delivers something a person can observe has one ([[vertical-slice]]). A piece that only delivers together with its neighbours has none of its own, and it is rated with them ([[component-task-masquerading]]). The source does not discuss this.

## Agent executor note

Value and urgency describe the result and the world around it, so they do not depend on who executes, and the idea survives. The evidence is one practitioner article with no measurement ([[black-swan-qualitative-cod]]).
