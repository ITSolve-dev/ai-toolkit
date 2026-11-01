---
title: A Trade-Off Needs Cost and Benefit
category: ordering
summary: Decisions about what to do, delay or trim need estimates of both cost and benefit; estimates also let a feature be sized down, and customers only make these calls early if past estimates held up.
tags: [rule, prioritization, estimation, value, trade-off]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# A Trade-Off Needs Cost and Benefit

Cohn's rule is that a trade-off cannot be decided on one side of the ledger:

> In order to make these decisions we need estimates of both the costs and benefits.
>
> — [[cohn-agile-estimating-planning]], L447

The decisions he means are of the form: is a feature worth delaying the release, should the release be held for more features, should a tool be bought (L447). He says "Many of the decisions made while planning a project are tradeoff decisions." (L445).

## Inputs and where they are read

This wiki's reading, since Cohn states the rule without a procedure:

- **Cost:** the task's estimate, as a range where the work is unresolved. See [[estimates-as-ranges]].
- **Benefit:** the value stated in the task's purpose or by whoever requested it ([[task-must-justify-itself]]). Chapter 1 gives no benefit scale; the bands this wiki uses when value cannot be put in numbers are on [[ordering-by-value-and-urgency]].
- **Scarce people:** Cohn says "Sometimes the staffing profile of a project can be more important than its schedule." (L439). His example is a project worth starting only if a plan avoids the fully committed chief architect (L439). This wiki reads that, for a few people steering an agent, as: the steering person's attention can be the scarce input, not the agent's capacity.

**What later fact would show the choice wrong.** A chosen item delivered little of the value claimed for it, or a deferred one kept returning as a request.

## How much of a feature

Estimates also size a feature, not only rank it:

> Rather than investing twenty days and getting everything, perhaps ten days of effort will yield 80% of the benefit.
>
> — [[cohn-agile-estimating-planning]], L451

This wiki reads the numbers as an illustration, since Cohn writes "perhaps" and reports no measurement. It keeps the mechanism: a task can be compared against a cheaper version of itself, which also feeds decomposition ([[story-splitting-patterns]]).

## The precondition

> Customers are reluctant to make these types of tradeoff decisions early in a project unless the developers’ estimates have proven trustworthy.
>
> — [[cohn-agile-estimating-planning]], L451

This wiki reads that as an order dependency: comparing tasks by cost is only as useful as the estimates' record, so [[good-plan-test]] has to pass before the comparison carries weight. In this setting the person steering plays the customer's role.

## Failure sign

This wiki's question to check: tasks ordered with size recorded but no statement of what each is for, or the reverse, tasks ordered by claimed importance with no size. Either way the comparison had one side. The charter does not accept an omission as the sign of a rule that chooses, so this only supports the later-fact test above, and it is no proof of a bad order: a board cannot show a wrong order directly.

## Trade-off

This wiki notes that a rough benefit estimate on every task costs effort and can give false confidence. Chapter 1 does not say how rough is acceptable; it shows only that a comparison made without both sides is not one. Where the benefit is expressed as a rate and durations vary widely, the comparison is made on [[cost-of-delay-over-duration]]. See also [[purpose-of-planning]].
