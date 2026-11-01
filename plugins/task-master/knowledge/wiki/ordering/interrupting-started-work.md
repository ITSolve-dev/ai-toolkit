---
title: Interrupting Started Work
category: ordering
summary: Reordering unstarted work costs nothing, while stopping started work costs something; this wiki allows it only for a task at the top rank, against work rated well below it, and through the route the project's setup permits.
tags: [decision-rule, ordering, cost-of-delay, wip, prioritization]
sources: [black-swan-qualitative-cod, kubernetes-issue-triage, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Interrupting Started Work

A task can arrive whose rank is above work already under way. This rule decides whether anything stops. The source's statement is mild:

> If something with a “Very High” Cost of Delay is waiting in a queue or is blocked by something with a “Medium” or “Low” Cost of Delay, you may decide to switch. A good example of this, (which happens naturally in e-commerce businesses) is if a key part of your site goes down then everyone drops what they are doing to fix it. It’s painfully obvious in this case that time is money.
>
> — [[black-swan-qualitative-cod]], L85

The Kubernetes guide has the same top level in stronger words: "Team leaders are responsible for making sure that these issues (in their area) are being actively worked on—i.e., drop what you’re doing. Stuff is burning." ([[kubernetes-issue-triage]] L232). Its examples, transcribed here because the extraction lost their separators, are user-visible bugs in core features, broken builds, tests, and critical security issues (L232). That list comes from a very large project's release process, so this wiki treats it as examples and not as a definition.

This wiki reads two cases in the first passage. A task that is only waiting in a queue needs a new order, which costs nothing before anything has started. A task held up by started work of lower rating is the case where something stops, and that is what this page is about. The author says "may decide", so the switch is allowed and not required.

## The rule

1. If the higher task has not displaced anything, reorder and finish here.
2. Interrupt only when the incoming task is at rank 1 of [[ordering-by-value-and-urgency]], and the work it would displace is well below it. The text fixes "Very High" as rank 1 and does not map "Medium" or "Low" to ranks, so "well below" is a judgement here and not a line.
3. Use the route the setup allows. Under a flow setup, that means a declared exception to the bound on [[wip-control]]. Under an iteration setup, it means a change judged by its effect on the goal ([[mid-period-change]]).
4. Record the interruption, so that its cost can be read later.

Steps 2 to 4 are this wiki's. The author gives one comparison and one example, and no procedure.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The rank of the incoming task | [[ordering-by-value-and-urgency]] |
| The rank of the work it would displace | The board's ratings, read again today |
| What stopping would lose | The state of the started task; an agent run leaves only what is in the repository and the task text ([[unfinished-at-period-end]]) |
| What the setup permits | Project configuration ([[board-rules-by-setup]]) |

The interruption was wrong if the incoming task, once delivered, had not lost value in the way its rating claimed, or if the displaced work lost more than the incoming work gained. Interruptions in general are being overused if most of them, rated again afterwards, were not for rank 1 tasks, or if started work keeps ageing behind a stream of interruptions ([[flow-metrics]]). These tests are this wiki's.

## The route around the rating

The interviews behind [[montgomery-tracker-smells]] name a way this rule gets bypassed. The context factor "customer priority" is "Smell can occur due to customer prioritisation overriding or skipping regular workflows" (L571), with P07's note that an "important customer finds something and this gets priority" (L548). It had 4 mentions. This wiki reads such a request as an input to the rating and not as an exception to it: an outside person's demand can be real urgency, and the rating says so in a sentence ([[a-date-is-not-urgency]]).

## Cost

Stopped work ages and may go stale. It also keeps its place in the count ([[blocked-work-counts-against-wip]]).

## Agent executor note

The author's example has people dropping what they are doing. An agent changes what stops. A second run can often start without stopping the first, so the first thing to give way is probably the attention of the people steering, and not the agent. Two started tasks then compete at review. This is this wiki's reading and is unmeasured. Where the runs touch the same code, the stop is real and the rule above applies. The source's evidence is one example with no measurement.
