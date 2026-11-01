---
title: Relative Penalty
category: ordering
summary: Score what the absence of a feature would cost as well as what its presence gains, because work that brings no benefit but cannot be left undone is invisible to a benefit-only ranking; penalty is not urgency, and scoring it does not by itself guarantee a place.
tags: [rule, ordering, prioritization, value]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Relative Penalty

Relative penalty is the loss incurred if a feature is not implemented, scored separately from the benefit it brings. It is a column of [[relative-weighting]], and the same idea drives the dysfunctional question of the [[kano-questionnaire]]. The rule is to keep it: "You may be tempted to drop the Relative Penalty column. Don’t." ([[cohn-agile-estimating-planning]] L2537). The stated reason: "it can be very useful to look at features from the perspective of how users will be impacted by the presence of the feature as well as by the absence of the feature" (L2537).

## What breaks without it

The source's example is a client in financial services whose product owner had one feature that "would bring no value to the company other than keeping the company in compliance with certain new government regulations" (L2539). She joked that the only downside of skipping it was that the CEO might go to prison: "And she (since she wasn’t the CEO) was OK with that risk if it meant getting other features into the product instead." (L2539). The author's verdict: "This is a clear example of a feature with a relative benefit of 1 but a relative penalty of 9." (L2541).

This wiki reads two things in that anecdote. Ranked on benefit alone the feature comes last, though leaving it out could be the worst outcome on the list. And the person scoring is not the person who bears the loss, which is a reason to ask whose penalty it is. The source tells the second as a joke and draws no rule from it, so the rule is ours.

## Kinds of work this catches

The source names compliance. This wiki extends it to work whose value lies wholly in what its absence would do: obligations under a contract, security, keeping a system running, and a task a [[kano-model]] threshold feature depends on. That list is ours.

## Penalty is not urgency

This is the criterion that separates the rule from its neighbours. **Penalty** asks what is lost if this is not done. **Urgency** asks how fast the value drains while it waits ([[urgent-versus-important]]). A task can be high on one and low on the other. A regulation with a date has both, and only the date part is urgency, with the limits on [[a-date-is-not-urgency]]. The separation is this wiki's; the book does not make it in this chapter.

The Killer band of [[ordering-by-value-and-urgency]] already folds penalty in, since its description covers what happens "if we *don’t* do something" ([[black-swan-qualitative-cod]] L44). So this wiki reads a project ordering by bands as needing no extra field: it needs the absence question asked when the band is chosen.

## Scoring it is not enough

This section is this wiki's derivation. The compliance feature totals 10 (1 + 9). Placed on the list in [[relative-weighting]] with an estimate of 32, it would score 10/32 = 0.31, below everything else there. The penalty column makes such a feature visible and does not protect it, because the score lets other things compensate for it. A loss that cannot be accepted is a constraint and not a weight, so it belongs in the filter on [[kano-or-relative-weighting]].

## Sign and application

These signs are this wiki's.

- **The sign in a board:** a task whose request names a regulation, a contract, or a failure that would stop the product, ranked below feature work.
- **The sign in a ranking:** a value score or a value sentence that states only what doing the task gains, on a list containing such a task.

A sign raises a question: the loss may be accepted, knowingly, by the person who would bear it.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| What would be lost if this is never done | The request, or the requester's answer ([[clarifying-questions]]) |
| Who bears that loss | The requester or the person steering |
| Whether the loss is acceptable at all | The person steering; it cannot be derived from the task |

The source gives no test of the rule, so this one is ours: the scoring was wrong if the loss that was rated low came to pass after the task was ranked below others, or if a task rated high on penalty was left undone and nothing happened.

## Cost

Asking a second question per feature doubles the judgement to supply. A penalty score can also be inflated more easily than a benefit, since anyone can picture a disaster, which feeds [[priority-inflation]]. Both points are this wiki's.

## Agent executor note

The rule concerns the work and survives. An agent can notice that a request names an obligation, and can ask the absence question. The answer is a task-only fact ([[recoverable-versus-task-only-facts]]), and an agent that reads only what a task gains will rank this kind of work last without any visible signal, so the question has to be part of the plugin's procedure.
