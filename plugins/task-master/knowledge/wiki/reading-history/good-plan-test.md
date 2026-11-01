---
title: Good Plan Test
category: reading-history
summary: A plan is judged by whether it was reliable enough to decide on, not by accuracy; six months delivered in seven was still useful, in twelve was not, and regular updates are part of the verdict.
tags: [decision-rule, plan-vs-fact, estimation, retrospective]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Good Plan Test

The test judges a plan by what it was for:

> A good plan is one that stakeholders find sufficiently reliable that they can use it as the basis for making decisions.
>
> — [[cohn-agile-estimating-planning]], L469

This wiki reads that as separating a useful plan from an accurate one: a plan can be wrong and still good.

## Cohn's worked boundary

In his example a six-month release plan feeds marketing, advertising and customer-upgrade decisions (L471-L473).

| Actual | Verdict | Reason |
|---|---|---|
| 12 months | Not a good plan | "If development takes twelve months, instead of the planned six, then this was not a good plan." (L473) |
| 7 months | Probably still useful | Incorrect and may have "led to some slightly mistimed decisions", but within PMI's budgetary margin (L475) |

This wiki reads the figures as holding only for that case: a half-year release at budgetary-estimate stage. This wiki's arithmetic against [[cone-of-uncertainty]]: seven months is about 17% over, inside PMI's +25% for a budgetary estimate; twelve is 100% over, outside even the +75% of an order-of-magnitude estimate.

## The update clause

The verdict depends on whether the plan was kept current:

> In that case, the one-month late delivery should not have been a last-minute surprise to anyone.
>
> — [[cohn-agile-estimating-planning]], L475

Cohn says the plan "should have been updated regularly throughout the course of the project" (L475). This wiki reads that as judging a plan across its revisions, not by its first date alone.

## Inputs and where they are read

This wiki's reading for applying the test to a finished period or milestone:

- **Plan:** the forecast and its assumptions as recorded, per [[single-date-plan]].
- **Fact:** completion dates from board history.
- **Decisions taken on the plan:** stated by the person steering; a board does not show them.
- **Revision history:** when the forecast moved, relative to when the slip was knowable.

**Question it answers.** Did the miss hurt a decision taken in good faith, and did the plan warn in time?

**What later fact would show the verdict wrong.** A slip called harmless turns out to have cost a dependent decision.

## Precision has to rise over time

Cohn's test moves with the project. Early, a useful plan may say the third quarter and "approximately a described set of features"; later, "in order to remain useful for decision making, this plan will need to be more precise." (L469). His release plan splits features into those certain to ship and those that may ship "depending on how well things progress." (L471). This wiki reads that split as usable directly in a forecast for a few people.

## Failure signs

These are this wiki's questions to check: a plan-versus-fact reading that scores only the size of the miss, which ignores what the plan was used for; or a forecast that moved only at the very end, which is the last-minute surprise. See also [[plan-conformance-as-success]], the neighbouring error of scoring a project against its original list.

## Trade-off

This wiki notes that a usefulness test depends on knowing the decisions, which are not recorded on a board, so the plugin must ask. Stakeholders are the judges in Cohn's definition, which makes the test partly subjective.
