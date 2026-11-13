---
title: Urgent Versus Important
category: ordering
summary: Value says how much a result is worth and urgency says how fast that worth drains away; they are rated apart because people conflate them, and two ratings that always move together are the sign they were not.
tags: [decision-rule, ordering, cost-of-delay, prioritization]
sources: [black-swan-qualitative-cod, kubernetes-issue-triage, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Urgent Versus Important

Urgency and importance are two separate facts about a task, and the charter names the difference as a topic. The source's warning:

> Let’s take a look at relative value first. To do this, we need to consider Value as *independent* of Urgency. This can be hard, as we tend to conflate the two together in our heads. In fact, we often make the mistake of treating things that feel *Urgent* as if they are therefore *Valuable –* and vice versa.
>
> — [[black-swan-qualitative-cod]], L37

The author repeats the point for urgency: "Again, we need to try and think about urgency independently from the value." (L60).

## The discriminating test

This wording is this wiki's, built from the band definitions on [[ordering-by-value-and-urgency]].

- **Importance, or value:** if this were delivered now, how much would it be worth? Time plays no part in the question.
- **Urgency:** if this were delivered later instead, what share of its worth would be gone, and how fast? The size of the worth plays no part in the question. The share follows the source's band, where the value "(whatever total value that might be) will quickly evaporate" (L56); a question about how much would be lost in absolute terms would rate every high-value task urgent, which is the correlation the first sign below detects.

A task can be high on one and low on the other. The author's examples: "Most cost-reducing initiatives would normally fall into this band." of Whenever (L58), whatever their total value, and an opportunity "however big or small" can sit at ASAP (L56).

## One scale or two

The Kubernetes guide uses one scale ([[kubernetes-issue-triage]] L230-L236), so the two sources disagree on the shape of a rating.

| Label | The guide's wording |
|---|---|
| `priority/critical-urgent` | "Stuff is burning. These should be fixed before the next release." |
| `priority/important-soon` | "Must be staffed and worked on either currently or very soon—ideally in time for the next release. Important, but wouldn’t block a release." |
| `priority/important-longterm` | "Important over the long term, but may not be currently staffed and/or may require multiple releases to complete. Wouldn’t block a release." |
| `priority/backlog` | "General agreement that this is a nice-to-have, but no one’s available to work on it anytime soon." |
| `priority/awaiting-more-evidence` | "Possibly useful, but not yet enough support to actually get it done." |

This wiki reads that scale as folding three things into one word: how much it matters, how soon, and whether someone is free. The third is a fact about a large staff and means little for a few people.

The disagreement resolves by project setup, and the resolution is this wiki's.

- **A project that ships in releases:** the guide's test, would this block the next release, is a sharp reading of urgency for defects and incoming requests against a release already under way. Use it there to separate ASAP from Soon, and rate value apart. It does not apply to the release's planned content: a release date is a date like any other, so membership in a release raises urgency only as the date approaches ([[a-date-is-not-urgency]]). Otherwise every must-have would be ASAP, since must-haves "need to be available before the product is released" ([[cohn-agile-estimating-planning]] L2413), and the category says nothing about when they are built ([[kano-model]], its section on ordering by category).
- **A project with no releases:** the test has nothing to act on, so use the two ratings as they stand.
- **Under both:** do not carry over "staffed", and read `priority/awaiting-more-evidence` as an item that has not been rated ([[incomparable-tasks]]).

## Sign of violation

- **In the ratings on a board:** value and urgency move together. Most high-value tasks are also high-urgency and most low-value tasks low-urgency, so the two columns carry one judgement.
- **In the rating sentences:** the sentence given for value is about time ("the client is waiting"), or the sentence given for urgency is about size ("this matters a lot").
- **In board history:** a task's value band went up on the day it was escalated, with nothing learned about its worth.

These signs are this wiki's. The source states the failure and gives no sign. The first has no threshold: some agreement between the two ratings is expected, and the source gives no figure for how much is too much. It prompts a reading of the sentences.

## Why

What breaks is the order. If urgency leaks into value, whatever feels pressing rises on both axes and comes out at the top of the table, and the work that matters and can wait never gets a turn, even after it starts to leak. This reasoning is this wiki's.

## Cost

Two ratings cost more than one. A project with few tasks and a clear order may not need them, and nothing here says when the single judgement is good enough.

## Agent executor note

The distinction concerns the work and survives. The conflation the author describes is a human habit, and whether an agent proposing bands would show it has not been tested. The evidence is one practitioner article with no measurement.
