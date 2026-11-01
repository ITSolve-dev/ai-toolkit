---
title: Velocity Self-Correction
category: sizing
summary: Because points are relative, a shared misjudgement of size or rate shows up as a different observed velocity and corrects the forecast without re-estimating, so consistency matters more than correctness; it covers shared error, not error in the ratios, and only while estimates stay untouched and the rate stays stable.
tags: [concept, estimation, velocity, plan-versus-fact, forecasting]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Velocity Self-Correction

Velocity self-correction is Cohn's claim that a points-based plan fixes its own forecast once work starts: the observed rate replaces the assumed one and the end date moves, with no estimate touched. Chapter 7 calls the same mechanism "the great equalizer" (L1435). An estimate need not be right, because the forecast divides estimated size by a rate measured in the same estimates.

> The beauty of a points-based approach to estimating is that planning errors are self-correcting because of the application of velocity.
>
> — [[cohn-agile-estimating-planning]], L1033

> Because the estimate for each feature is made relative to the estimates for other features, it does not matter if our estimates are correct, a little incorrect, or a lot incorrect. What matters is that they are consistent.
>
> — [[cohn-agile-estimating-planning]], L1435

## The mechanism

This wiki states the arithmetic plainly: if every estimate is wrong by the same factor, the remaining work and the measured velocity are wrong by that factor too, and the factor cancels when one is divided by the other.

Cohn's numeric example, with constructed figures (L1033): 200 points at an assumed 25 per iteration plans 8 iterations. Observed velocity is 20.

> Without re-estimating any work they will have correctly identified that the project will take 10 iterations rather than 8.
>
> — [[cohn-agile-estimating-planning]], L1033

The painting example shows why it works (L1035-L1037). Rooms are sized from a floorplan with no dimensions: small bedrooms at 5 and the master at 10, because it looks twice as large. If the bedrooms turn out twice the size assumed:

> If you find that the bedrooms are twice the size you thought then the master bedroom is also twice the size you thought. The estimates remain the same but because the rooms have four times the area you expected, your rate of progress through them will be slower.
>
> — [[cohn-agile-estimating-planning]], L1037

Cohn therefore treats an absolute misjudgement as a rate change. The estimates are "estimates of the relative effort" and stay useful even though the true scale was unknown (L1037). This rests on [[size-versus-duration]].

Chapter 7's example has fifty stories at one point each, one person, one point a day expected and two-week iterations (L1437). The plan says ten stories per iteration and five iterations. After the first iteration five stories are done: "If I let velocity take care of correcting my misperceptions I will realize that the project will take 10 iterations since my velocity is half of what I’d planned" (L1437). This wiki notes that no estimate changed, and that one person is working, so the mechanism is not tied to team size.

## The condition

Chapter 4 states the claim without qualification. Chapter 7 supplies the condition: "What matters is that they are consistent." (L1435). Consistency is not arbitrariness: "We cannot simply roll a die and assign that number as the estimate to a feature." (L1435). This wiki reads the painting example the same way: every room is wrong by the same factor, so the ratios hold. The table is this wiki's, from that condition and from Cohn's charting case in Chapter 7.

| Error | Absorbed by velocity? | Why |
|---|---|---|
| All items misjudged by a common factor | Yes | Ratios hold; only the rate moves |
| The team's rate was simply assumed wrong | Yes | The observed rate replaces it |
| A class of items misjudged against the rest | No | Cohn's charting case (L1460-L1480); the open items of that class need new estimates |
| One item misjudged against the others | No | The ratios are wrong, so the total's composition is wrong |
| Items not yet discovered | No | They are absent from the total being divided |

A second condition is time. Velocity "becomes apparent over the first few iterations" (L1033), and the schedule grows reliable by "measuring velocity over the first few iterations" (L1435), so this wiki notes that the correction arrives only after those iterations have been spent. The fifty-story example corrects after one iteration only because it is constructed so, and the source gives no figure for how many "the first few" means. This wiki adds that a rate observed on early items forecasts later items only if those items are of a similar kind.

A third condition is untouched estimates. Changing the estimates of finished tasks alone breaks the cancellation; see [[hindsight-re-estimation]].

The rule for when to change an estimate is on [[re-estimate-when-relative-size-changes]]. The case this page settles is narrower: a uniform slowdown is a reason to recompute the date and not to rewrite the sizes.

## What it does not say

The source does not claim a late project stops being late: the fifty-story project takes twice as long. This wiki's reading is that velocity corrects the forecast and not the outcome.

## Failure modes

These signs are this wiki's derivation. Each raises a question to check.

- **Re-estimating instead of re-measuring.** After slow iterations, estimates across the board are raised. That spends effort on the one thing that did not need changing, and it distorts the velocity history.
- **Treating self-correction as complete.** A date is trusted because velocity was applied, while a few items have run far beyond others of equal points. The ratios may be the error.
- **Keeping the plan after the fact.** Observed velocity differs from the planned one and the date stays where it was. The correction is available only if someone recomputes it through [[deriving-duration-from-velocity]].

## Agent executor note

The transfer here is this wiki's, not Cohn's. The arithmetic carries over: a measured rate replaces an assumed one. What would need checking in a setup with an agent executing is whether misjudgement stays shared. The painting example assumes a common cause, the true scale of the house. Agent work may have item-specific causes, such as how well a task's context is written, and those would fall in the rows of the table that velocity does not absorb. The source gives no evidence either way. See [[velocity]].

The usefulness of the cancellation also assumes the rate stays roughly stable between periods, which the source takes for granted from a human team. A change in how an agent runs (the model, the tools, the amount of steering) can move the rate, so history from before such a change may not forecast what follows. A plugin leaning on this concept should therefore say which periods its velocity came from.
