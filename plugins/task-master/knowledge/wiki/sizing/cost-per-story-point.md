---
title: Cost per Story Point
category: sizing
summary: Dividing what a stretch of work cost by the points finished in it turns any estimate into money without logging hours; it is a rough conversion for a keep-or-drop decision, it omits support cost, its labour figures do not transfer to an agent, and costing by points and by whole iterations gives different answers.
tags: [method, estimation, prioritization, velocity, cost]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Cost per Story Point

Cost per story point converts a relative estimate into money, so a size can be set against a value. Cohn ([[cohn-agile-estimating-planning]]) offers it because "it is important to remember that time costs money" (L1740), and he calls it a "rough conversion" (L1740). Later he adds: "It is often useful to know the cost per story point (or ideal day)." (L2128).

## The calculation

Cohn gives it twice, with different figures. Both are illustrations and not measurements, and the two are from different examples. The method applies equally to ideal days (L1740, L2128).

**From a recent stretch (Chapter 9, L1740).**

1. Add the salaries of everyone involved over a recent stretch: ¤150,000 over the last twelve weeks. Everyone means the product owner, project manager, programmers, testers, database engineers, analysts, user interface designers and so on.
2. Take the points completed in the same stretch: 120.
3. Divide: 120 story points at ¤150,000 give ¤1,250 per point.
4. Price the item: thirty points cost ¤37,500.
5. Ask whether the functionality is worth that investment.

**From a team's cost per iteration (Chapter 10, L2087-L2128).**

1. Take each person's salary and add about 50% for space, equipment, software and benefits. The result is the *fully burdened labor cost* (L2087). The 50% is the chapter's approximation: "around another 50% of an employee’s salary" (L2087).
2. Cost per iteration is that figure over 26, for two-week iterations (L2126).
3. Multiply by the share of time on the project. A team with one programmer at 50% totals ¤13,550 per iteration, rounded to ¤13,500 (L2126).
4. Divide by velocity: "divide the adjusted cost per iteration by the team’s average or expected velocity" (L2128). At 20 points per iteration: ¤13,500 / 20 = ¤675 per point.

Then a 100-point request costs ¤67,500 (L2128). Theme cost feeds the net cash flow in [[sources-of-return]].

This wiki notes that the method needs no time tracking, which the charter excludes. The inputs are team cost and finished points read from the board, and nobody logs hours.

## Conditions

These conditions are this wiki's unless a line is cited.

- The money and the points must come from the same people over the same stretch, because the rate is only as stable as the velocity behind it ([[velocity]]).
- The rate belongs to one project. Points are relative, so it does not transfer between projects.
- The result covers building only. Cohn's second factor reads "developing (and perhaps supporting)" (L1714), and a rate of labour over points says nothing of later support.
- Chapter 9 counts salaries alone and Chapter 10 counts burdened labour. This wiki reads the Chapter 10 figure as the fuller one; neither counts anything else the work consumes.
- A velocity with no history has to be predicted, which is why the source says "average or expected" (L2128).

## Two costs for the same theme

The chapter uses two costs for the overnight theme without saying so. By iterations, 150 points at 20 per iteration is 7.5, taken as 8 iterations, costing ¤108,000 (L2010, L2161, L2187); that figure drives the ¤46,341 NPV. By points, Table 10.15 shows 150 x ¤675 = ¤101,250 beside that same NPV (L2330). The gap is ¤6,750, half an iteration, and about 7% of the lower figure.

This wiki's reading of when each holds:

- **Whole iterations** when the theme occupies the team alone until done, because the half iteration is paid for regardless.
- **Points** when several themes share a plan, so that the leftover capacity goes to something else. Combining themes up to a capacity needs this figure ([[financial-measures-for-themes]]).

The sign of the mistake is a cost and a return in the same row built on different assumptions.

## The capacity form

This form is ours. Where money is not the deciding unit, the same division gives a share of capacity: thirty of the 120 points in twelve weeks is a quarter of that stretch, or three weeks. The question becomes whether the item is worth three weeks of what could otherwise be done. It needs only board history, so the plugin can state it without being given a salary figure.

## Inputs and what would show it wrong

| Input | Read from |
|---|---|
| Points finished in a stretch | Board history |
| Cost of that stretch | The person steering; it is not on the board |
| Item size | The task's estimate |
| Item value | [[prioritization-factors]] |

This wiki's test: the conversion was misleading if the item's real share of capacity differed widely from its priced share, or if the rate moved a lot between stretches. Both read from history.

## What it does not promise

This wiki notes that the result looks more exact than its inputs. A figure of ¤37,500 inherits every error in a relative estimate, and in a value it is compared with, so it supports a yes-or-no question and not a fine ranking. It is an average, valid only while the team, the mix of work and the meaning of a point stay stable, and a cost computed from it is a forecast rather than a price.

## Setting: a few people steering an agent

This section is this wiki's reading, not Cohn's.

The structure survives and the numbers do not. Salaries, burden and a 26-iteration year describe a staffed human team, and Cohn's list of roles names a whole team. When an agent executes and a person steers, the cost of an iteration is that person's time plus agent usage, and the steering time is usually the scarce part. If points and throughput can be read from board history, the same division gives a usable cost per point in whichever unit the person cares about, including steering hours.

This needs a point scale kept stable under an agent, which is its own question for [[size-ceiling]] and the estimation pages. Velocity under an agent may not behave as it does for a stable human team, so the rate should be read from the project's own recent history and rechecked. If there are no stable points, there is no cost per point, and the plugin should not report one.
