---
title: Priority Inflation
category: ordering
summary: Most open tasks end up in the top band of the priority scale, so the band stops deciding anything; the sign is a top band that no longer separates tasks, and the source gives no figure for how full is too full.
tags: [failure-mode, ordering, prioritization]
sources: [black-swan-qualitative-cod, kubernetes-issue-triage, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Priority Inflation

Priority inflation is the drift of tasks into the top band of a scale until the band no longer separates them. It breaks the question of what comes first, since an order in which everything is first decides nothing. The source names it twice: a plain scale is one "where everything tends to end up as “High”" (L42), and of its own top band it says:

> (The challenge, as with all relative/qualitative approaches, is to try and avoid inflation. There should be very few in this highest band, otherwise we end up in MoSCoW Hell, where everything is tagged a “must do”.)
>
> — [[black-swan-qualitative-cod]], L44

The author ties the remedy to the shape of value: the band should be small because "It is the typical Pareto “vital few” that [dominate](http://blackswanfarming.com/the-problem-with-projects/)." (L42). The author's other answer is to use descriptive words, so that a label states what it claims (L42).

## Sign

- **In board state:** the top band holds so many open tasks that choosing the next task among them needs some other criterion. The band has stopped deciding.
- **In board history:** a task's rating rose with no new sentence saying what changed ([[ordering-by-value-and-urgency]]).

These signs are this wiki's. The source says "very few" and gives no number, and this wiki does not supply one. A share of tasks would depend on how many tasks are open.

## Remedy

Rate again relative to each other, starting from the sentences that justify the band. A top-band task whose sentence does not claim that not doing it would badly damage the project moves down. This wiki also treats a band as something to defend, so a claim to the top band has to name its gain or loss.

The Kubernetes guide offers a way of contesting a rating without raising it: "if you notice an issue that you believe to be incorrectly prioritized, please leave a comment offering your counter-proposal and we will evaluate it." ([[kubernetes-issue-triage]] L228). This wiki reads that as separating the claim from the label, so a person who disagrees argues and does not simply promote.

One published remedy for old items works against this. The authors of [[montgomery-tracker-smells]] suggest: "If open issues are left too long, unassigned, then the curator can increase the priority/severity until a developer chooses to work on the issue." (L773). This wiki rejects that for the plugin. Age alone changes neither value nor urgency ([[cost-of-delay]]), so raising the rating records a falsehood in order to push a person, and an agent cannot be pushed. An old item is read again and its rating changes only if a sentence changes ([[zombie-issue]]).

## Why

What breaks is the plugin's output. If the top band is full, the next task is chosen by whatever breaks the tie, which usually means by the last person who asked. The reasoning is this wiki's.

## Agent executor note

The mechanism the source describes is social: labels rise because people want their work done. With a few people steering there is less of that pressure, but also nobody else to push back. Whether an agent proposing bands inflates them has not been tested, and the plugin's proposals should be read for it.
