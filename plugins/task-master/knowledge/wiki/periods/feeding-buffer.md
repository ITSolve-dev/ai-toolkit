---
title: Feeding Buffer
category: periods
summary: Reserved time in the delivering team's plan that protects another team's start date from a late hand-off, added after reducing dependencies, sized at about 50 percent by default, and rarely longer than an iteration.
tags: [method, dependencies, buffer, multi-team, uncertainty]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Feeding Buffer

A feeding buffer is reserved capacity placed before a hand-off, so that late delivery by one team does not become a late start for another. Cohn's plain version: "if your team needs something from my team tomorrow at 8:00 A.M., my team shouldn’t plan on finishing it at 7:59" ([[cohn-agile-estimating-planning]] L4176). It has the same purpose as the project buffer ([[choosing-a-buffer]]), applied to a single hand-off rather than the project's end.

This is a technique for multi-team projects with heavy dependencies: Cohn's summary places it "on highly complex projects with many interteam dependencies" (L4227). See the gate at [[multi-team-techniques-scale-limit]] first.

## Reduce before you protect

When a [[rolling-lookahead-plan]] cannot cope, "your first recourse should be to try to find a way to reduce the number of interdependencies so that a rolling lookahead plan is adequate" (L4172-L4176). The buffer is the fallback for dependencies that cannot be removed.

## Mechanism

"all you need to do is plan temporarily for a lower velocity for the team that is delivering a capability to another team" (L4187). A buffer is therefore planned capacity and not idle time. In the SwimStats plan, Team 1's second iteration is split evenly between the rest of the API and the buffer, and the expectation is that they "complete 10 points on the API, need only a portion of the buffer, and begin work on the national records user story during the second iteration" (L4187).

## Where it goes

Only at a [[critical-dependency]]. The tests are on that page: allocate first, then buffer only where planned high-priority work is stopped and neither a swap nor a partial deliverable would help (L4193-L4199).

## Sizing

The square-root-of-sum-of-squares calculation from [[choosing-a-buffer]] usually does not apply, because "most inter-team dependencies are based on no more than a handful of stories or features at a time" (L4203). Instead, size it as a percentage of the stories creating the dependency: "You can use 50% as a default buffer size but this should be adjusted based on team judgment." (L4203). The 50% is a default for hand-offs of a handful of stories, not a measured value.

This wiki notes that the worked example does not apply that default. Team 1's buffer is 10 points against a 30-point API, about a third of the stories creating the dependency, and half of a 20-point iteration (L4153, L4187). Cohn does not say the figure was sized by the rule, so the example should not be read as evidence for 50%.

## An oversized buffer is a sign

> I’ve never had to use a feeding buffer that was larger than a full iteration and have rarely used one longer than half an iteration.
>
> — [[cohn-agile-estimating-planning]], L4207

This wiki reads that as a limit from one practitioner's experience, with no measurement behind it. A buffer longer than an iteration usually means a large chunk is being passed in one piece (L4205). Cohn's response is to change the plan rather than the buffer:

- Divide the hand-off: it "should almost certainly be divided so that the functionality is delivered incrementally" (L4205), so the receiver can start on the first part.
- Let the receiver order the delivery: "Having the receiving team act as a product owner or customer of the delivering team will allow the two teams to usually work out an incremental delivery sequence that works for both teams." (L4205).
- Expect mid-course adjustment: teams would likely split work or adjust between iterations "as soon as they noticed one team slipping behind" (L4205), so the large buffer would not be consumed anyway.
- Shorten the chain: he reviews the plan "to see what I can do to shorten the chain of deliverables being passed from one team to another" (L4207).

## Trade-off

A buffer may lengthen the plan. In the example it did not, because Team 1's third iteration was not full (L4191). By this wiki's arithmetic, Team 1 carries 30 + 10 + 10 points of stories plus a 10-point buffer, exactly filling three 20-point iterations. Where the plan is full, the added duration is, in Cohn's view, a realistic expectation and not padding, "not in a “let’s pad the schedule so we don’t have to work hard” way" (L4191). Because it can prolong the schedule, it is added only when necessary (L4191).

## Failure modes

The signs are this wiki's.

- **Buffer as slack.** The delivering side treats reserved capacity as free time. Cohn rejects this for Team 1 (L4187). Sign: the capacity reserved for a buffer goes unused while other ready work waits.
- **Buffers everywhere.** Sign: buffers appear on hand-offs that do not pass the [[critical-dependency]] test.
- **Buffer longer than an iteration.** Sign as above. Check whether the hand-off could be split.

## Transfer to a few people and an agent

Cohn says a single team needs none of this (L4211), and this wiki keeps the buffer as a noted multi-team technique. Velocity reduction for one team to protect another has no direct target when one agent runs one stream. The transfer here is ours: the part worth keeping is the reading of a large hand-off as a cutting problem. A task whose output is passed on whole, with the next task unable to start on any part of it, is a candidate for a cut into increments.
