---
title: Slack for Expedites
category: moving-work
summary: Delivering predictably with classes of service takes spare capacity, so study how often true expedites occur and design for that rate, for instance with lower overall WIP and free capacity helping work in process first; the source gives no formula.
tags: [rule, class-of-service, expedite, wip, slack]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Slack for Expedites

When emergencies cannot be refused, the variability they bring has to be absorbed somewhere. Vacanti says that only spare capacity does it:

> Pretty much the only way to predictably deliver in the face of variability introduced by different CoS is to build slack into the system.
>
> — [[vacanti-actionable-agile-metrics]], L3416

This rule chooses how a process is shaped given that expedites will arrive. Vacanti's example is FedEx, which on his account keeps empty planes in the air and redirects them when a location is overwhelmed (L3408). He argues that a pure waste-elimination view would forbid those flights, because they cost salaries, fuel and maintenance, and that FedEx accepts the cost to keep its service agreements (L3410, L3416). This wiki treats the FedEx story as an illustration, since the source gives no figures for it. [[utilization-versus-slack]] holds the general case.

## Not refusing, and not idling

Vacanti rejects two easy answers. Telling teams to stop expediting ignores that expedites "happen all the time" and vary in size and number, which he accepts for most teams (L3392). Keeping people idle in wait for them is not something management will accept (L3418), and that objection concerns people, so it is noted here only for the agent case below. Capping expedites at one is the third answer, and it fails too ([[standing-expedite-lane]]).

What he offers for a true emergency, such as production being down or a new regulatory requirement, is design around the frequency:

> Obviously, those things will—and should—take precedence. But, just like the FedEx example, you should study the rate of occurrence for those items and adjust your process design accordingly. That will potentially mean lowering overall process WIP. That will probably mean making sure free resources look to help out with other items in process before pulling in new items.
>
> — [[vacanti-actionable-agile-metrics]], L3456-L3462

This wiki reads the passage as two levers: a lower bound on [[wip-control]], which keeps capacity unoccupied, and a pull rule in which a free executor first helps what is started. He ends the passage with "And so on", so the list is open.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How many true expedites arrived per period | Board history, if exceptions are recorded ([[interrupting-started-work]] step 4) |
| Whether each one was true | Rating them again afterwards ([[ordering-by-value-and-urgency]]) |
| The current bound on work in process | Project configuration ([[wip-control]]) |
| The effect on ordinary items | Their cycle time and age against the [[service-level-expectation]] |

Vacanti gives no way to turn a rate into a WIP number, so the direction is his and the size is a judgement. The tests that follow are this wiki's. The slack was too small if expedites still push ordinary items past their expectation. It was too much if the bound keeps capacity empty through periods with no expedite. This is what the rule costs: quiet periods deliver less than a fully loaded process would.

## Failure signs

These signs are this wiki's derivation and each raises a question.

- **In history:** exceptions are frequent and the WIP bound has never changed.
- **On the board:** a free executor starts new work while started items sit waiting.
- **In history:** exceptions were never recorded, so the rate cannot be read at all.

## Agent executor note

The objection to idle developers depends on the executor being a salaried person. An idle agent costs little, so this wiki expects execution slack to be cheap. The slack that costs something is the steering person's attention, because an expedite still needs someone to direct and review it. This wiki reads the rule as keeping review capacity below full, and it reads "help out with other items" as finishing and reviewing what is open before starting more. Both are transfers of ours and are unmeasured.
