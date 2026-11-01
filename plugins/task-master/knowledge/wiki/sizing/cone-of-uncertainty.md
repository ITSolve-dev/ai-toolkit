---
title: Cone of Uncertainty
category: sizing
summary: Estimates narrow as a project proceeds; Boehm's 0.6x-1.6x at feasibility to +/-15% after requirements, with PMI's asymmetric ranges, all project-level and from sequential or traditional settings. Cohn re-uses the multipliers on velocity, one step per completed iteration from 0.6-1.6 to 0.9-1.1, and admits the mapping has no mathematical basis.
tags: [concept, estimation, uncertainty, numbers, velocity, range]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Cone of Uncertainty

The cone of uncertainty is the observation that an estimate's plausible error shrinks as a project moves forward. Barry Boehm drew its first version in 1981, and Steve McConnell later gave it the name ([[cohn-agile-estimating-planning]] L374). Cohn's summary is that "Estimates given early in a project are far less accurate than those given later." (L505).

## Figures and their conditions

All these figures are **project-level**. Boehm's are schedule estimates, explicitly for points "in a sequential development (“waterfall”) process" (L374). Cohn gives PMI's as "the progressive accuracy of estimates" (L391) without saying schedule, though he applies its budgetary margin to a schedule at L475.

**Boehm, as given by Cohn:**

| Point | Range | On a 20-week estimate | Citation |
|---|---|---|---|
| Feasibility | 60% to 160% of the estimate | 12 to 32 weeks | L382 |
| After requirements are written | +/- 15% | 17 to 23 weeks | L382 |

The figure's extracted text carries the multipliers 1.6x, 1.25x, 1.15x, 1.10x and 0.9x, 0.85x, 0.8x, 0.6x, and the milestones Initial Product Definition, Approved Product Definition, Requirements Specification, Product Design Specification, Detailed Design Specification and Accepted Software (L387, repeated at L3639). Chapter 16 pairs the first two by name, one iteration with the initial product definition and two with the approved product definition (L3659). Its step rule then gives 0.85 and 1.15 for the third milestone, which agrees with the +/- 15% at L382. This page leaves the fourth pair unassigned, since only counting steps would place it on Product Design Specification, and nothing in the source pairs the last milestones.

**PMI, as given by Cohn (L391):**

| Estimate | Range | On 20 weeks (this wiki's arithmetic) |
|---|---|---|
| Order of magnitude | +75% to -25% | 15 to 35 weeks |
| Budgetary | +25% to -10% | 18 to 25 weeks |
| Definitive | +10% to -5% | 19 to 22 weeks |

## The disagreement

Cohn presents Boehm's cone as symmetric and PMI's as asymmetric (L391). Both agree the range narrows. They differ on whether an overrun is more likely than an underrun of the same size.

This wiki resolves it as follows; the resolution is its own, since Cohn does not choose. When the plugin gives a forecast for work not yet understood, it uses PMI's shape, with the late side wider than the early side, because the cost of a surprise late date is usually what the person steering needs to see. Neither set of magnitudes transfers to a small project steered through an agent, so the plugin keeps the shape and not the percentages unless the project's own history supplies figures. The one exception is the velocity multipliers below, for a project with no history at all.

## Applying it to velocity

Cohn moves the cone from a schedule onto a rate. Multiply the average velocity by the low and high multiplier for the number of iterations completed (Table 16.1, L3663-L3668):

| Iterations completed | Low | High |
|---|---|---|
| 1 | 0.6 | 1.60 |
| 2 | 0.8 | 1.25 |
| 3 | 0.85 | 1.15 |
| 4 or more | 0.90 | 1.10 |

The rule is "for each iteration completed, move one step to the right on the cone of uncertainty" (L3659). Cohn's worked example is an average of 20 after three iterations, which gives 17-23 (L3672). The 0.6 and 1.6 pair is also used on a historical mean (15 gives 9-24, L3634) and on a forecast (25 gives 15-40, L3732-L3736).

Cohn's footnote notes that dividing would be technically correct, and that multiplying is close enough because 0.6 and 1.6 are near-reciprocals (L3630).

### Conditions on these multipliers

- **The mapping is a heuristic, by Cohn's own account:** "Although there’s no solid mathematical basis for the approach I’m about to describe, it does work and it makes sense" (L3659). This wiki treats the multipliers as conventional widths, not as measured confidence bounds.
- **It stops at three or four iterations.** "I don’t use the cone of uncertainty, for example, to pretend that after six iterations the team precisely knows their velocity and it won’t waver through the end of the project" (L3674). Velocity keeps moving, and this wiki does not read the narrowing as a proof of convergence.
- **The source contradicts itself at two iterations.** The prose gives 80% to 120% (L3659), while Table 16.1 and Figure 16.1 give 0.8 and 1.25. This wiki uses the table, because the figure agrees with it.
- **Equal width for unequal evidence.** This wiki notes that one observed iteration, a historical mean with comparability doubts, and a pure forecast all get 0.6-1.6, though Cohn says a forecast "must reflect a high degree of uncertainty" (L3684). The table does not grade evidence at its widest step, so a figure from this row should not be read as equally well founded across those cases.

### Against the simpler option

With three or more iterations a team can use the observed range instead (L3657). On Cohn's numbers the two nearly coincide: this wiki's arithmetic gives a mean of 14.3 for 12, 15, 16, which at 0.85-1.15 is 12.2-16.5, against the observed 12-16. Where iterations exist, the observed range needs no borrowed multiplier.

### In an agent-executed project

The transfer here is ours. The cone's phases and widths come from human projects, so nothing here shows that the funnel has the same shape when an agent executes. A project with no history still needs some width on a velocity figure, so this wiki allows the multipliers there as a labelled starting convention, and replaces them with the project's own observed spread as soon as one exists, per [[choosing-velocity-estimate-approach]]. See [[velocity-estimate-range]] for the rule, and [[run-iterations-to-observe-velocity]] for the default way to get that spread.

## What the plugin should do with it

This wiki reads the cone as a limit on stated precision, and proposes this as a question to check: an estimate far narrower than the state of the work allows, for example a single date on an item with no accepted scope, claims more than the cone admits. See [[single-date-plan]], and [[estimates-as-ranges]] for the rule Cohn draws from it in Chapter 2 (L662).

This wiki also reads it as meaning thorough early planning cannot buy accuracy, which is why [[no-planning-or-over-planning]] treats detail and accuracy as separate.

## Failure mode: reading a narrow range as knowledge

A plan cites 0.9-1.1 from many completed iterations as if the remaining work were pinned down. This sign is this wiki's: a plan whose date spread has stopped being revised while the iteration-to-iteration figures on the board still vary by more than the stated range.

## Limits

- The figures describe sequential phases with written gates. Chapter 1 says nothing on the shape of the cone for iterative work, and Chapter 16's move onto iterations is a heuristic by Cohn's own account and not evidence about that shape.
- They do not describe a single task's estimate. This wiki treats using them as task-size multipliers as a misuse.
- Cohn uses the cone to show difficulty, and rejects it as an excuse: "We cannot excuse ourselves from these activities just because they are hard." (L505).
