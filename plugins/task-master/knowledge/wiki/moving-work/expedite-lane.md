---
title: Expedite Lane
category: moving-work
summary: An expedite lane is exempt from the board's other limits and can block started work, so its own WIP limit, often one, is the only bound on the flow debt it creates. A limit of one bounds concurrency, not frequency: a lane never empty is a renamed standard process, and a visible speed gap (getKanban, 10-11 days against 3 or less) invites every request to claim it. Predictable delivery with expedites needs slack: study the rate of true expedites and design for it, by lower overall WIP and free capacity helping started work first.
tags: [rule, kanban, wip-limit, expedite, flow-metrics, failure-mode, class-of-service, pull-policy, wip, slack]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Expedite Lane

An expedite lane is a separate swimlane on a Kanban board for work allowed to overtake everything else. The source treats it as "One great example of a process taking on Flow Debt" ([[vacanti-actionable-agile-metrics]] L2422). The rule is to keep the lane's WIP limit extremely low, because the lane is exempt from the other limits and its own limit is the only thing bounding what it borrows.

## The usual policies

The source describes these as what most systems do (L2432):

- The lane has "an extremely low WIP limit", "often set to one".
- Lane items "can violate WIP limits at each step in the workflow".
- An expedite "is pulled immediately for work" and may “jump the queue” ahead of other ready work.
- If nobody is free, "many teams will block other items to free up team members" for it.

From these the source concludes that "it is so important to be extremely conservative when setting the WIP limit on an expedite lane" (L2432).

The limit covers the lane as a whole. In the worked example, a limit of one means "only one work item can be in progress in that whole lane at any given time", wherever it sits among Ready, Design, Development and Test (L2440).

## What breaks when it is ignored

In the source's example the expedite reaches Development with no developer free, so the team blocks one or more of the three items in progress. "What has happened is that the team has chosen to artificially age one item (or more) in order to shorten the Cycle Time of another." (L2440) That is [[flow-debt]], and the bill arrives as longer Cycle Times on the blocked items or as discarded work. Blocked items still count against the limit; see [[blocked-work-counts-against-wip]].

## The sign

All of these read from board history or state:

- More expedites open at once than the lane's limit.
- The lane is never empty over a long stretch.
- Other items become blocked at the moment an expedite enters, and stay blocked until it leaves.

The first two are the source's speculative signals (L2468). The third is the source's example stated as a check. How many expedites are too many is resolved on [[flow-debt]].

## Trade-off

The lane is not condemned: the source allows "very good reasons" to take on hedge-class debt (L2478). Its cost is paid in the predictability of everything else on the board, and a lane that exists makes the exception easy to invoke. The hedge test adds a stricter option than the usual policy, letting existing work finish before the expedite is picked up (L2466). This wiki reads that option as cheaper in debt and slower for the expedite; which holds depends on whether the delay cost of the expedite outweighs the aging of what would be interrupted. See [[cost-of-delay]] and [[interrupting-started-work]].

## Class of service

The source says the chapter was avoiding a term: "Class of Service" (CoS) "is exactly what I am talking about" (L2550). It objects to the usual implementation rather than the idea, saying that "most teams do not know how to implement it properly" (L2550). The full argument, deferred to Chapter 13 (L2552), is on [[class-of-service]]. Chapter 13 also goes further than this page's rule: a low limit bounds concurrency and not frequency, so a lane limited to one and never empty is the failure in the section below.

## When the lane never empties, and when it attracts everything

The standard advice for expedites is to give them a lane with a WIP limit of one. The sections above hold those policies and why the limit must be low. Vacanti says that limit does not settle the problem, for two separate reasons, and calls the advice an error ([[vacanti-actionable-agile-metrics]] L3420, L3424, L3430).

> If you are going to have an expedited lane, and you limit that lane’s WIP to one, but there is always one item in it, then, I am sorry to say, you do not have an expedited process. You have a standard process that you are calling an expedited process, and you have a substandard process which is everything else.
>
> — [[vacanti-actionable-agile-metrics]], L3438

### First failure: the lane is never empty

A limit of one bounds how many expedites run at once and says nothing about how often one is running. The simulation on [[fifo-pull-order]] held expedites to exactly one at a time and still got the worst results: with FIFO among Standard items the 85th percentile went from 50 to 65 days, and with random pull it reached 100 days, with a range of 40 to 170 days against 30 to 50 in the baseline (L3334, L3356). Those figures belong to that simulation's setting, where an expedite was always on the board by construction.

### Second failure: the lane attracts everything

Vacanti's evidence comes from the getKanban board game, which has an expedite lane with a WIP limit of one. Standard items typically take ten or eleven days at the 85th percentile, spread over three to 15 days, and expedited items always take three days or less (L3430). He then projects that to a requester who sees the two numbers:

> What do you think is going to happen in the real world? That is right: everything becomes an expedite! Good luck trying to keep to the WIP of the expedited lane limited to one.
>
> — [[vacanti-actionable-agile-metrics]], L3430

This wiki notes that the second failure is an argument from a game's numbers and is not a measurement of a real team. The mechanism is still checkable: the better the lane works, the larger the visible gap, and the stronger the reason to ask for it. This wiki reads it as the same decay as [[priority-inflation]], with the incentive made explicit by the gap in days.

### Why the lane looks like it works

The lane's own numbers are good. "The truth is that the only part of your process that is more predictable with CoS is the highest priority class." (L3476), so a review of expedites alone reports success. The damage shows up in Standard items. Vacanti's own summary is "For all practical purposes, introducing CoS is one of the worst things you can do to predictability." (L3442), which he later qualifies: CoS is not "inherently evil" and he is speaking from predictability alone (L3470, L3476).

### Observable signs

These are this wiki's derivation, and the source gives no threshold for any of them. Each raises a question ([[smell-is-not-a-finding]]).

- **On the board:** the lane or label is occupied on most days.
- **In history:** when one expedite finishes, another starts soon after.
- **In history:** the share of arriving items marked expedite rises over time.
- **In history:** expedited cycle times stay tight while the spread and age of ordinary items grow ([[flow-metrics]]).

A real incident stream is the competing explanation. Vacanti accepts that for most teams expedites do happen, unpredictably in size and number (L3392), so a busy lane raises two questions: are these real, and has the process been designed around their rate? The second is in the next section.

### What to do instead

- Keep a pull order that does not need the lane ([[fifo-pull-order]]).
- Treat true emergencies as a declared exception ([[interrupting-started-work]]) and study their rate (next section).
- Add a class only after measuring a working process ([[class-of-service]]).

### Agent executor note on a standing lane

The first failure is about a shared resource, so it survives wherever one exists; for an agent-run board that is probably the reviewer's attention. The second failure needs a requester separate from the team. On a project where the person requesting is also the person steering, this wiki expects the incentive to be weaker, and the inflation to come from impatience and not from competition for a slot. Both readings are this wiki's and are unmeasured.

## Slack for the rate of true expedites

When emergencies cannot be refused, the variability they bring has to be absorbed somewhere. Vacanti says that only spare capacity does it:

> Pretty much the only way to predictably deliver in the face of variability introduced by different CoS is to build slack into the system.
>
> — [[vacanti-actionable-agile-metrics]], L3416

This rule chooses how a process is shaped given that expedites will arrive. Vacanti's example is FedEx, which on his account keeps empty planes in the air and redirects them when a location is overwhelmed (L3408). He argues that a pure waste-elimination view would forbid those flights, because they cost salaries, fuel and maintenance, and that FedEx accepts the cost to keep its service agreements (L3410, L3416). This wiki treats the FedEx story as an illustration, since the source gives no figures for it. [[utilization-versus-slack]] holds the general case.

### Not refusing, and not idling

Vacanti rejects two easy answers. Telling teams to stop expediting ignores that expedites "happen all the time" and vary in size and number, which he accepts for most teams (L3392). Keeping people idle in wait for them is not something management will accept (L3418), and that objection concerns people, so it is noted here only for the agent case below. Capping expedites at one is the third answer, and it fails too (previous section).

What he offers for a true emergency, such as production being down or a new regulatory requirement, is design around the frequency:

> Obviously, those things will—and should—take precedence. But, just like the FedEx example, you should study the rate of occurrence for those items and adjust your process design accordingly. That will potentially mean lowering overall process WIP. That will probably mean making sure free resources look to help out with other items in process before pulling in new items.
>
> — [[vacanti-actionable-agile-metrics]], L3456-L3462

This wiki reads the passage as two levers: a lower bound on [[wip-control]], which keeps capacity unoccupied, and a pull rule in which a free executor first helps what is started. He ends the passage with "And so on", so the list is open.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How many true expedites arrived per period | Board history, if exceptions are recorded ([[interrupting-started-work]] step 4) |
| Whether each one was true | Rating them again afterwards ([[ordering-by-value-and-urgency]]) |
| The current bound on work in process | Project configuration ([[wip-control]]) |
| The effect on ordinary items | Their cycle time and age against the [[service-level-expectation]] |

Vacanti gives no way to turn a rate into a WIP number, so the direction is his and the size is a judgement. The tests that follow are this wiki's. The slack was too small if expedites still push ordinary items past their expectation. It was too much if the bound keeps capacity empty through periods with no expedite. This is what the rule costs: quiet periods deliver less than a fully loaded process would.

### Failure signs

These signs are this wiki's derivation and each raises a question.

- **In history:** exceptions are frequent and the WIP bound has never changed.
- **On the board:** a free executor starts new work while started items sit waiting.
- **In history:** exceptions were never recorded, so the rate cannot be read at all.

### Agent executor note on slack

The objection to idle developers depends on the executor being a salaried person. An idle agent costs little, so this wiki expects execution slack to be cheap. The slack that costs something is the steering person's attention, because an expedite still needs someone to direct and review it. This wiki reads the rule as keeping review capacity below full, and it reads "help out with other items" as finishing and reviewing what is open before starting more. Both are transfers of ours and are unmeasured.

## Agent executor note on the lane

The blocking step in the source rests on no people being free. This wiki reads the limit as still applying with an agent executing, since what the lane spends is whatever is scarce, which for a few people steering agents is likely their review and attention. The source does not test this.

## Related

[[flow-debt]], [[what-may-move]], [[wip-control]], [[board-rules-by-setup]], [[priority-inflation]], [[kanban-guide]]
