---
title: Standing Expedite Lane
category: moving-work
summary: An expedite lane limited to one but never empty gives no fast path, only a renamed standard process and a worse one for everything else; a visible speed gap also invites every request to claim the lane.
tags: [failure-mode, class-of-service, expedite, pull-policy, wip]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Standing Expedite Lane

The standard advice for expedites is to give them a lane with a WIP limit of one. [[expedite-lane]] holds those policies and why the limit must be low. Vacanti says that limit does not settle the problem, for two separate reasons, and calls the advice an error ([[vacanti-actionable-agile-metrics]] L3420, L3424, L3430).

> If you are going to have an expedited lane, and you limit that lane’s WIP to one, but there is always one item in it, then, I am sorry to say, you do not have an expedited process. You have a standard process that you are calling an expedited process, and you have a substandard process which is everything else.
>
> — [[vacanti-actionable-agile-metrics]], L3438

## First failure: the lane is never empty

A limit of one bounds how many expedites run at once and says nothing about how often one is running. The simulation on [[fifo-pull-order]] held expedites to exactly one at a time and still got the worst results: with FIFO among Standard items the 85th percentile went from 50 to 65 days, and with random pull it reached 100 days, with a range of 40 to 170 days against 30 to 50 in the baseline (L3334, L3356). Those figures belong to that simulation's setting, where an expedite was always on the board by construction.

## Second failure: the lane attracts everything

Vacanti's evidence comes from the getKanban board game, which has an expedite lane with a WIP limit of one. Standard items typically take ten or eleven days at the 85th percentile, spread over three to 15 days, and expedited items always take three days or less (L3430). He then projects that to a requester who sees the two numbers:

> What do you think is going to happen in the real world? That is right: everything becomes an expedite! Good luck trying to keep to the WIP of the expedited lane limited to one.
>
> — [[vacanti-actionable-agile-metrics]], L3430

This wiki notes that the second failure is an argument from a game's numbers and is not a measurement of a real team. The mechanism is still checkable: the better the lane works, the larger the visible gap, and the stronger the reason to ask for it. This wiki reads it as the same decay as [[priority-inflation]], with the incentive made explicit by the gap in days.

## Why the lane looks like it works

The lane's own numbers are good. "The truth is that the only part of your process that is more predictable with CoS is the highest priority class." (L3476), so a review of expedites alone reports success. The damage shows up in Standard items. Vacanti's own summary is "For all practical purposes, introducing CoS is one of the worst things you can do to predictability." (L3442), which he later qualifies: CoS is not "inherently evil" and he is speaking from predictability alone (L3470, L3476).

## Observable signs

These are this wiki's derivation, and the source gives no threshold for any of them. Each raises a question ([[smell-is-not-a-finding]]).

- **On the board:** the lane or label is occupied on most days.
- **In history:** when one expedite finishes, another starts soon after.
- **In history:** the share of arriving items marked expedite rises over time.
- **In history:** expedited cycle times stay tight while the spread and age of ordinary items grow ([[flow-metrics]]).

A real incident stream is the competing explanation. Vacanti accepts that for most teams expedites do happen, unpredictably in size and number (L3392), so a busy lane raises two questions: are these real, and has the process been designed around their rate? The second is on [[slack-for-expedites]].

## What to do instead

- Keep a pull order that does not need the lane ([[fifo-pull-order]]).
- Treat true emergencies as a declared exception ([[interrupting-started-work]]) and study their rate ([[slack-for-expedites]]).
- Add a class only after measuring a working process ([[when-to-use-class-of-service]]).

## Agent executor note

The first failure is about a shared resource, so it survives wherever one exists; for an agent-run board that is probably the reviewer's attention. The second failure needs a requester separate from the team. On a project where the person requesting is also the person steering, this wiki expects the incentive to be weaker, and the inflation to come from impatience and not from competition for a slot. Both readings are this wiki's and are unmeasured.
