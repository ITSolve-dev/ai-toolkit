---
title: End-of-Period Crunch
category: periods
summary: Too long a period produces a relaxed start and a frantic end; the remedy is a length that spreads pressure evenly, not more pressure, and the opposite failure is a period so short it stays hectic with no recovery.
tags: [failure-mode, iterations, period-length, pace]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# End-of-Period Crunch

End-of-period crunch is the pattern in which work relaxes at the start of a period and panics at the end. Cohn treats it as evidence the period is too long for the team.

> If the duration is too long, there is a natural tendency to relax a bit at the start of the iteration, which leads to panic and longer hours at the end of the iteration.
>
> — [[cohn-agile-estimating-planning]], L3496

The mechanism comes from Niels Malotaux: "As long as the end date of a project is far in the future, we don’t feel any pressure and work leisurely… When the pressure of the finish date becomes tangible, we start working harder." (L3480, L3490). Cohn scales this down from a project to a period: "many teams will feel tangibly less stress during their first week than during the fourth and final week of an iteration." (L3490).

## Observable sign

Cohn describes the sign as felt stress, which a board cannot show. This wiki's board equivalent is:

- **In board history:** finishes bunch in the last days of each period, across several periods, while the first days show few.

The sign raises a question and proves nothing ([[smell-is-not-a-finding]]). Bunched finishes can also come from tasks too large to finish earlier, from review that happens only at the end, or from results presented once in a batch. Check those before reading it as this failure.

## What to do

The remedy is length and not pressure. The aim is "to take the total amount of stress they’d normally feel and distribute it more evenly across a suitably long iteration" (L3492). Telling people to deliver today is what Cohn explicitly rejects (L3492).

Shortening has a limit. The opposite failure is a period so short it stays hectic: "One-week iterations (or anything shorter) can be very hectic and stressful." (L3498), with no recovery if someone is out sick or anything goes wrong (L3498). Cohn's sign for this length is a next deadline "never more than four days away" (L3498). The two failures bracket the choice in [[period-length]].

## Trade-off

A long period buys room for more creative solutions (L3506), and the crunch is part of what that costs. Cohn still accepts four weeks for an experienced team in a highly exploratory phase (L3506), so this failure is a cost to weigh and not an automatic reason to shorten.

## Agent executor note

This failure rests on human pace, so the charter requires a note. It does not survive for an agent executor, which does not relax early or feel a deadline. Bunched finishes on an agent-executed board therefore point elsewhere, most likely to the people steering, who start, unblock or review work on a human clock. Whether those people show the same pattern has no evidence in this wiki, and this reading is untested. The neighbouring claim about work filling the time allowed is on [[parkinsons-law]].
