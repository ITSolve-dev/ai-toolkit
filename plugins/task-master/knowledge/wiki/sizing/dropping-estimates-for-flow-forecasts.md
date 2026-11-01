---
title: Dropping Estimates for Flow Forecasts
category: sizing
summary: Run a flow forecast beside points for a release and test points against Cycle Time on your own history; retire estimates for date forecasting only if the evidence supports it, and keep sizing for cuts.
tags: [decision-rule, estimation, story-points, forecasting, cycle-time]
sources: [vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Dropping Estimates for Flow Forecasts

This rule decides whether relative estimates should still drive date forecasts once Cycle Time history exists. Siemens HS decided they should not ([[siemens-hs-case]]), and the way it decided is more portable than the verdict.

> In analyzing the metrics, Siemens also discovered that there was no correlation between story point estimates and actual Cycle Time.
>
> — [[vacanti-actionable-agile-metrics]], L4232

The source also calls the move away from velocity estimation "an easy decision" (L4226). Its takeaways are more careful: Siemens could "mostly abandon their old estimation practices" (L4288).

## The rule

This wiki's rule is not to retire estimates on a general argument, and to run the test on the project's own history:

1. Reach stable Cycle Times first; the forecast depends on them (L4226-L4232). See [[conservation-of-flow]] and [[forecast-needs-a-stable-process]].
2. For finished items, compare points against Cycle Time.
3. For one release, run a flow forecast beside the existing plan and compare both to the outcome, as Siemens did: "we adopted this practice along with our current points and velocity estimation planning methods and compared the results" (L4202). The conditional matters: "If these forecasts proved reliable, we would no longer need to estimate." (L4202)
4. Retire estimates for date forecasting only if the forecast did better.

## Inputs and where they are read

- Points per item, from the task.
- Cycle Time per item, from board history.
- Forecast dates and the actual finish, from the plan and board history.

## What would show the choice wrong

After estimates stop, forecasts begin to miss beyond their stated likelihood, or the mix of work changes and history stops describing it. Then the forecast needs rebuilding, and estimates may need to return for new kinds of work.

## What the finding does not establish

The chapter gives no coefficient, method or sample for "no correlation". It comes from one organization, on the pre-existing process. This wiki offers a hypothesis the source does not state: where most of an item's life is queueing, as [[flow-efficiency]] would show, elapsed time reflects WIP and blocks more than size, so even a good size estimate would not correlate with Cycle Time. That would make the finding a statement about the system more than about estimators.

## Resolving the disagreement by setup

This section is this wiki's own reading, on sourced positions. [[story-points]] and [[velocity-self-correction]] hold that relative estimates plus observed velocity give usable forecasts. This chapter holds that distributions of observed Cycle Time do better.

- **Stable history with enough finished items:** forecast from flow; [[monte-carlo-simulation]], [[single-item-forecast]].
- **New project, or unstable or thin history:** keep relative estimates and a [[velocity-range-forecast]]; flow data does not yet exist ([[how-much-flow-data]]).
- **Deciding how much fits in a period:** a count from Throughput needs no points, and the size check stands in for them ([[filling-a-period]], [[throughput-monte-carlo]]). Keeping points beside it for a while is the same test as step 3.
- **Deciding whether to cut a task:** keep sizing either way. Retiring estimates here concerns dates. The charter's size above which a task is cut is a different question, and the chapter does not address it. See [[estimate-versus-commitment]], [[size-ceiling]] and [[right-sizing]].

Which unit an outside reader should be given is a separate choice, on [[points-or-time-and-count]].

## Other reasons offered

The source reports that stakeholders found points confusing and were "always looking for time based answers" (L4236), and that Cycle Time and Throughput are more tangible. See [[story-points-do-not-convert-to-hours]]. The claim that dropping estimates "eliminated the emotion and recrimination" (L4272) is a report about people; this wiki keeps it as testimony only.

## A stronger claim, with less behind it

A later book by the same author goes further than Siemens:

> That’s because with an MCS approach, estimation is not needed.
>
> — [[flow-metrics-scrum-teams]], L970

The book calls estimated relative complexity "an extremely poor predictor of capacity" (L970), and its reasoning is that Throughput history already holds items of every complexity, blocked, interrupted or unlike earlier work (L978-L994). The ranges read here report no measurement. This wiki therefore treats it as a general argument, which the rule above does not accept as grounds by itself, and it does not count as a second voice beside Siemens, since the author is the same.

This wiki keeps two conditions from the book all the same. History replaces estimation only "if you choose your inputs properly" (L970). And the count covers right-sized items only (L1022), which [[right-sizing]] records as an estimate of a smaller kind, so what the book retires is the scale and the number, and not the judgement of size.

## Trade-offs

This wiki notes that estimation sessions also surface unknowns ([[unknowns-surfaced-by-estimating]]), and that retiring them removes that side effect. The chapter does not weigh this.

## Agent executor note

This wiki's reading: the human cost being saved, estimation sessions and their friction, is smaller when an agent drafts sizes. The comparison in steps 2 and 3 survives unchanged, because it reads only board history.
