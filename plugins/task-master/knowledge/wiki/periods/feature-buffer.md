---
title: Feature Buffer
category: periods
summary: Planning for mandatory work plus 25-40% optional work, built last, so a firm date can be met by dropping the optional part; DSDM's MoSCoW caps Must Have at 70% of effort for the same effect.
tags: [method, planning-a-date, buffer, scope, dsdm, moscow]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Feature Buffer

A feature buffer protects a date with scope rather than time: the plan contains more than must ship, and the excess is what gets dropped. The promise is "we’ll get you all of the functionality in this pile and hopefully some of the functionality in that pile" ([[cohn-agile-estimating-planning]] L3849). It suits work where the date is firmer than the exact contents ([[fixed-date-variable-scope]]); [[choosing-a-buffer]] covers the choice, and [[schedule-buffer]] is the time-side counterpart.

## Procedure

1. The customer selects the absolutely mandatory work and its estimates are summed. "This represents the minimum that can be released" (L3849).
2. The customer selects another 25–40% more work, toward the top of the range when uncertainty is higher or tolerance for schedule risk lower (L3849).
3. Plan as normal for the whole set.
4. Build the optional work last: "The optional work is developed last, only after the mandatory work is complete" (L3853).

Cohn's example: 100 mandatory points plus 30 optional is 130; at 10 points per one-week iteration that is 13 iterations, with mandatory work done after ten if all goes well (L3855). If time runs short, "the schedule can still be met by dropping items in the feature buffer" (L4063).

## DSDM's position

DSDM sorts requirements into Must, Should, Could and Won't Have (MoSCoW), and "No more than 70% of the planned effort for a project can be targeted at Must Have requirements" (L3857). Cohn calls this consistent with his process. This wiki notes that the two figures are measured differently: Cohn's 25–40% is on top of mandatory work, so the optional share of the plan is 20–29%, while DSDM's 30% is of the whole, which is about 43% on top of Must Have. In this wiki's reading, a project set up with DSDM uses the 70% cap, which is the larger buffer, and any other setup uses Cohn's range, stating which base the percentage is taken from.

## Inputs and the fact that would show the choice wrong

- **Which items are mandatory:** from the person who owns what ships. This wiki maps Cohn's customer to the person steering; it is not a judgement for an agent to make.
- **Estimates and velocity:** from the items and board history.
- **Uncertainty and tolerance for schedule risk:** from the plan's setting, and they place the figure in the 25–40% range.

This wiki reads the optional part as too small if mandatory work overran into the date and the optional items were already gone. It was not a buffer at all if the optional items proved unshippable to leave out when the date came.

## Signs

These signs are this wiki's. Each raises a question to check, not a verdict.

- An optional item in progress while a mandatory item has not started. This breaks the order that makes the buffer work, and this wiki reads it as the sign most visible on a board.
- Every item in a plan with a firm date is marked mandatory, so there is nothing to drop.
- Must-level items exceed 70% of planned effort on a DSDM setup.
- Items move from optional to mandatory during the plan, shrinking the buffer without any item being dropped.

## Trade-offs

The customer accepts that some selected work may not arrive, and the team plans work it may never build. Cohn presents the setup as simple on an agile project (L3849), since prioritized, independently deliverable work is what makes dropping cheap. This wiki reads that as the condition: the buffer depends on items that can be left out, which is a cutting question ([[vertical-slice]]) and an ordering one ([[ordering-by-value-and-urgency]]).

## Agent executor note

This method depends on plan order, not on any human mechanism, so this wiki expects it to survive an agent executing unchanged.
