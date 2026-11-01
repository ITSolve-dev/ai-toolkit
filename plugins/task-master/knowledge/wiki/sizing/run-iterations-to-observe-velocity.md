---
title: Run Iterations to Observe Velocity
category: sizing
summary: The default way to estimate velocity is to hold the number back for one to three iterations and measure; this buys a founded estimate at the cost of giving no figure at the start.
tags: [method, velocity, iterations, release-planning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Run Iterations to Observe Velocity

Instead of predicting [[velocity]], run one to three iterations and estimate from what was observed. Cohn says "Because the best way to predict velocity is to actually observe velocity, this should always be your default approach" ([[cohn-agile-estimating-planning]] L3647). In [[choosing-velocity-estimate-approach]] this option ranks first.

## Procedure

1. Hold off giving a velocity figure for at least one iteration; Cohn holds that most project managers can do this (L3655).
2. Run the iteration on the real project.
3. Turn the observation into a [[velocity-estimate-range]]:
   - After one iteration: multiply by 0.6 and 1.6. A velocity of 15 gives 9-24 (L3655).
   - After three or more: use the range of observed values, or the mean with the [[cone-of-uncertainty]] step for that count. 12, 15, 16 gives 12-16 (L3657).
4. Plan the release date from the range (L3653).

## Reasoning

The time is spent anyway. Cohn's argument is that traditional projects use their early weeks on "obvious" requirements and on assembling a plan, "often as long as a few iterations on an agile project" (L3647). The early iterations are not only a measurement. Their stated purpose is "to assess the dark corners of the system, better understand the technologies involved, refine the understanding of the requirements, and measure how quickly the team can make progress on this project" (L3680).

The evidence offered is one anecdote: a development director whose yearlong projects set deadlines about two months in, with plans "always off at least 50% and often more" (L3653). This wiki keeps the mechanism and not the 50%: one company's experience, stated by one person.

## Trade-off

The cost is having no number at the start. Cohn expects resistance from organizations unwilling to start without any idea of duration, and advises stressing that the delay stems "not from a desire to avoid making an estimate but to avoid making an estimate without adequate foundation" (L3680). When a number cannot wait, or the iteration cannot be funded, this method is unavailable and [[forecast-velocity-by-what-fits]] applies.

## Failure mode

**Measuring an unrepresentative start.** This failure mode is this wiki's inference and not in the source. The sign is that the first iterations are filled with one kind of work, such as setup or infrastructure, so their velocity describes that work rather than the backlog. Check what the first iterations contained before extrapolating.

## What later fact shows it wrong

Later iterations land outside the range built from the early ones. The source expects velocity to keep moving and warns against treating it as settled even after six iterations (L3674).

## Agent executor note

The transfer here is ours. The method does not depend on human pace, so it survives. The first iteration of an agent-run project may overstate later velocity if it contains only the tasks easiest to specify, which is a reason to check the mix and not to skip the measurement.
