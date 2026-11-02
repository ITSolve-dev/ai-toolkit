---
title: INVEST
category: cutting-work
summary: The six characteristics Wake named for a good story, what each letter claims, and which page holds the sign that makes it usable.
tags: [concept, decomposition, invest, user-stories]
sources: [wake-invest, humanizing-work-splitting]
created: 2026-11-01
updated: 2026-11-02
---

# INVEST

INVEST is the acronym Bill Wake coined in 2003 for six characteristics of a good user story: Independent, Negotiable, Valuable, Estimable, Small, Testable ([[wake-invest]] L37-L44). Wake offers it as a reminder: "As you discuss stories, write cards, and split stories, the INVEST acronym can help remind you of characteristics of good stories" (L118). A reminder cannot audit a task, so this page records what each letter claims and points to the page that gives the letter a sign or a set of inputs.

## What each letter claims

| Letter | Wake's claim | Where it becomes usable |
|---|---|---|
| Independent | Wake would "like" stories "to not overlap in concept" and to be schedulable "in any order", and says "We can’t always achieve this" (L48-L50) | [[independent-tasks]] |
| Negotiable | "details will be co-created by the customer and programmer during development" (L54) | [[conversation-moves-into-the-task]] |
| Valuable | Valuable "to the customer", reached by slicing vertically through the layers (L58-L60) | [[vertical-slice]] |
| Estimable | "just enough to help the customer rank and schedule" (L66) | [[size-ceiling]] |
| Small | Stories "typically represent at most a few person-weeks worth of work" (L70) | [[size-ceiling]] |
| Testable | "I understand what I want well enough that I *could* write a test for it." (L76) | [[testable-acceptance]] |

## Where the two sources read a letter differently

| Letter | Wake | Humanizing Work | What this wiki uses |
|---|---|---|---|
| Independent | Any order, as an aim he concedes cannot always be met (L48-L50) | "can be prioritized by something other than technical dependency" (L111) | The weaker reading. Both sources concede the strong form cannot always be met; see [[independent-tasks]] |
| Negotiable | Details are "co-created" during development (L54) | "leaves room for collaboration around the details of what and how", and "as the collaboration happens and you capture more detail, the story becomes less negotiable" (L113) | The second clause: negotiability falls as detail is captured |
| Valuable | Valuable "to the customer" (L58) | "some increment of visible value for users", not necessarily worth shipping (L115, L117) | Observable, per [[vertical-slice]] |
| Small | "a few person-weeks" (L70) | A ratio to the sprint (L121) | Resolved per setup on [[size-ceiling]] |
| Testable | "*could* write a test" (L76) | "a concrete change in system behavior" (L123) | Both, on [[testable-acceptance]] |

## The letters pull against each other

The letters cannot all be maximised, and the Humanizing Work authors name the cost:

> Of course, there’s tension between some of these attributes. As stories get smaller, for example, it becomes harder to make them independent and valuable. The more negotiable they are, the harder they are to estimate and test.
>
> — [[humanizing-work-splitting]], L125

The authors resolve the tension by time, not by weight:

> Fortunately, different attributes matter at different times. Going into sprint planning, it’s more important that stories be small, estimable, and testable. We still want some independence, negotiability, and value, but those attributes become less important. Further into the future, it’s the reverse.
>
> — [[humanizing-work-splitting]], L127

This wiki reads that as a staging rule: a task far from being started is judged on whether it is independent, negotiable and valuable, and a task about to start is judged on whether it is small, estimable and testable. The authors tie the moment to sprint planning, a human ceremony. The transfer to the moment a task is about to start is this wiki's, and it applies under any project setup because the reason is the nearness of the work and not the ceremony.

## Negotiable rests on a human executor

Negotiable is the letter that depends most on who executes. Wake's reason for leaving details out of a story is that someone will talk them through later:

> A good story is *negotiable*. It is not an explicit contract for features; rather, details will be co-created by the customer and programmer during development.
>
> — [[wake-invest]], L54

This wiki reads that as a claim about a programmer who can walk over and ask. It does not survive unchanged when an agent executes, because the mechanism is a conversation during development and nothing in Wake's text says who holds that conversation when the executor is not a person. [[conversation-moves-into-the-task]] gives the replacement rule and the evidence for it.

## Agent executor note

Five of the six letters are properties of the work and survive a change of executor: overlap, value to a reader of the result, estimability, size and testability do not depend on who implements. The evidence for all six is the experience of human teams. Neither source reports a measurement, so a letter surviving here means its reasoning still applies, not that anyone has tested it with agents.
