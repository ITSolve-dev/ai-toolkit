---
title: Stating Plan Uncertainty
category: periods
summary: A schedule or release forecast carries its uncertainty as a range or a confidence, plus its basis, on whichever of scope or date is not fixed, in units as coarse as the uncertainty; a bare date or a fractional iteration count claims a precision the plan's inputs do not have.
tags: [rule, estimation, forecast, uncertainty, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Stating Plan Uncertainty

A plan that names one date and one fixed scope claims a certainty nobody has. Cohn: "No plan is certain. Be sure to include an expression of uncertainty in any release plan you produce." ([[cohn-agile-estimating-planning]] L4917). Summing points, dividing by a guessed velocity and reading off a date produces a precise-looking result from imprecise inputs. [[estimates-as-ranges]] says why an early estimate carries a range, and [[single-date-plan]] is the wider failure of a forecast that carries nothing else. This page says what form the statement takes and where the uncertainty goes.

## The mistake

Cohn's example is saying “we’ll ship on June 14, which is 7.2 iterations from now.” His objection:

> This is wrong because it gives the impression that the knowledge from which we construct the plan is sufficiently precise as to support this type of estimate.
>
> — [[cohn-agile-estimating-planning]], L4593

## The rule

Hold one of scope and date fixed and state the other as a range.

- **Scope fixed:** give a date range: “We’ll finish in the third quarter” or “we’ll finish in between 7 and 10 iterations” (L4917).
- **Date fixed:** give a scope range: “We’ll be done on December 31 and the product will include at least these new features but probably no more than those other new features.” (L4917).
- **Greater uncertainty:** "Use bigger units (iterations, months, then quarters, for example) when the amount of uncertainty is greater." (L4917).

For a target date, Cohn's alternatives (L4597-L4601) are to include "either your degree of confidence in the estimate, a range of possible dates, or both", for example:

- "I am 90% sure we’ll complete the planned functionality by July 31"
- "Based on our assumptions about the project size and team performance, the project will take three to four months."

## Range or confidence

Cohn allows either, but his chapter gives no way to derive a percentage. This wiki therefore prefers the range when generating output: [[velocity-range-forecast]] computes one from board history, while "90% sure" with nothing behind it is the same false precision in another form. A confidence belongs only where something produced it.

## What a good statement carries

Ron Jeffries' wording, quoted by Cohn, is the fullest model (L4605). This wiki extracts four parts from it:

- **Size:** "Right now, this appears to be a 200-point project."
- **Basis, stated even when weak:** "Based on our performance on other projects (or a random guess)".
- **Conditions and range:** "with N programmers on it, and your intimate involvement in the project, a project of this size will take between 4 and 6 months".
- **How it will change:** "As we go forward, we’ll all see how fast we’re progressing, and our estimate of the time needed will improve."

## The range survives the arithmetic

The fictional case study in Chapter 23 (L4961) shows a range defended against a figure that looks settled. Dividing 132 points by a planned velocity of 18 gives just over seven iterations (L6173). The product manager asks to call it seven, and the coach refuses:

> I’d prefer to give the estimate as a range. If we’re looking at enough work to go into an eighth iteration, we should probably say the project will take 6–10 iterations.
>
> — [[cohn-agile-estimating-planning]], L6179

At two weeks per iteration that is 12 to 20 weeks (L6181, L6185). The chapter gives no derivation for the range. This wiki computes the spread as about 18% below and 36% above the 7.33 midpoint, so it is deliberately wider on the late side. It rests on a planned velocity with no iteration finished ([[planned-velocity]]), so it should not be reused for a schedule with observed velocity behind it, which goes through [[velocity-range-forecast]].

**Failure mode: the range is heard as its low end.** The reply in the case is "I really don’t want this project to take 20 weeks. But you’re saying it might only take 12, right?" and the answer is "It might. But it might take 20," (L6181, L6183). Sign: notes downstream quote only the earlier bound. The sign is this wiki's.

**Scope is the lever that holds the range.**

> You can help it avoid taking 20 weeks by removing your lowest priority features if velocity shows that we’re headed toward 10 iterations. Keep in mind, too, that Delaney is actively looking for more features. If she comes up with something we’ll have to extend the schedule or take the same amount of current features out.
>
> — [[cohn-agile-estimating-planning]], L6183

This wiki reads that as saying the fact that shows the estimate wrong is observed velocity projecting past the upper bound, and the response is a change of scope and not a reworded date. Any addition carries a stated cost, either an extension or an equal removal. See [[changing-the-plan-without-changing-the-date]].

## Accurate versus precise

This distinction separates a good early plan from a bad one. "For a plan to be useful it must be accurate, but we accept that early plans will be imprecise." (L4841). Cohn's example, invented for the purpose: an early plan says 300–400 story points in the third quarter, and it turns out accurate when 305 are delivered in August, though it was never very precise. Later the same project's plan narrows to 380-400 points in September (L4841).

An imprecise plan can be right. A precise plan can be wrong. Early on, the range "may very likely be a sufficient basis for making decisions" (L4841), and that gives the test: a plan is precise enough when the decision waiting on it can be made. The purpose of a plan, per Cohn, is to serve as the basis for the organization's decisions (L4829), which is also [[good-plan-test]]. This wiki reads narrowing as something the plan owes only as those decisions come due, by way of [[replanning-on-new-knowledge]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Which of scope and date is fixed | The project's stated commitment ([[date-driven-vs-feature-driven]]); if neither is, ask |
| Remaining size | The board, in the project's scale ([[size-versus-duration]]) |
| The rate | Board history; a range and not a single value where history varies |
| The decision the plan serves | Whoever asked for the forecast |

The choice was wrong if the outcome fell outside the stated range, which means the range was too narrow, or if the range was so wide that the decision could not be made from it. The table and these tests are this wiki's derivation. Chapter 22 gives no method for computing a range, and Chapter 21 gives [[velocity-range-forecast]].

## Sign of violation

- A release forecast with a single date and a fixed scope.
- A calendar date stated alone.
- An iteration count with a fractional part. This wiki reads the decimal in 7.2 as the clearest mark, because no period ends at 0.2.
- A precision out of keeping with its horizon, such as a day named two quarters ahead ([[planning-horizons]]).
- A date that stays the same across several closed periods, even though velocity has changed. Cohn: "Plans are updated throughout the project and these updates need to be communicated." (L4575)

The first four are this wiki's derivation.

## Trade-offs

A range reads as evasive to someone who needs a date, and someone may read only one end of it. The case study accepts that a demand for a figure will come anyway: "everyone wants to know at least an idea of what the schedule looks like" (L6189). Cohn's own qualifier is "When possible" (L4593-L4597). Jeffries' version makes a range easier to accept by promising frequent delivery and the right to stop at any point. This wiki reads that as setup-dependent: on a project that cannot ship until the end, the range has no such offset.

## Agent executor note

The rule rests on nothing specific to a human executor and survives. The plugin should give ranges and never a point when it plans a date. A short or newly changed history gives a wider honest range, which is the rule working as intended ([[filling-a-period]]).

See also [[a-date-is-not-urgency]], [[iteration-summary-plan-versus-fact]].
