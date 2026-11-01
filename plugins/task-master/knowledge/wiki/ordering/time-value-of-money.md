---
title: Time Value of Money
category: ordering
summary: Returns arriving in different periods are not summed as they stand; each is discounted to present value at the organization's opportunity cost. The mechanism is sound, but over a two-year horizon its effect is often smaller than forecast error.
tags: [rule, ordering, prioritization, value, discounting]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Time Value of Money

Money later is worth less than money now, so two themes cannot be compared by adding up what each returns. Cohn's rule ([[cohn-agile-estimating-planning]]): "We cannot compare projects and make prioritization decisions by simply summing the total row of a worksheet" (L1920). His illustration: a stream of ¤100k, ¤200k, ¤500k over three quarters "is far less valuable than a stream that delivers those same returns but in the opposite sequence" (L1920).

## Mechanism

- **Present value** is what must be invested today to reach a future amount. At 10% a year, ¤0.91 today is ¤1.00 in a year; at 20%, ¤0.83 (L2173).
- **Discounting** moves a future amount back to its present value (L2175).
- **The discount rate** is the organization's opportunity cost, which "reflects the percentage return that is passed up in order to make this investment" (L2175). If past projects typically earned 20%, a new one is assessed against 20% (L2175).

This wiki notes that the chapter converts a yearly rate into quarters by simple division: its factors at "12% / year" (L2191) reproduce exactly as 1.03 to the power minus t, with t in quarters.

## Rule

- **Sign:** themes are ranked on a total return with no period attached, or two themes with different timing get the same value because their totals match. A related sign is an undiscounted ROI, whose problem is that it puts "equal value on the money invested in year one and the money earned in year five" (L2171).
- **What breaks if ignored:** a theme whose returns come late is ranked level with one whose returns come early, though the early one frees the money for the next investment.
- **Inputs:** the return per period ([[sources-of-return]]) and the discount rate. The rate comes from past project returns or the organization's stated minimum (L2175, L2222); neither lives on a board.

The cost of following it is needing that rate. Cohn counts this against NPV, noting that IRR avoids having "to establish (or, in the worst case, guess at)" it (L2256). See [[financial-measures-for-themes]].

## How much it changes, under what conditions

This section is this wiki's arithmetic on the chapter's figures.

- In WebPayroll, at 12% a year over eight quarters, the undiscounted net total is ¤70,100 and the NPV is ¤46,341. The drop looks large because the net is small against the flows that make it up. The lowest discount factor is only 0.789 (L2200).
- Payback did not move: both the plain and the discounted running totals turn positive in the seventh quarter (L2287, L2316).
- Cohn's own illustration at 12% a year: the stream as given is worth about ¤743k, and reversed about ¤765k. That is a 3% gap, not "far less". The charter grades a practitioner source on its mechanisms rather than its magnitudes, so the mechanism stands and the size does not.

This wiki's reading: on a two-year horizon at ordinary rates, discounting moves any single flow by about a fifth at most, and the forecasts it discounts are rougher than that ("We don’t have any solid data.", L2014). So timing matters mainly as a coarse question of which theme pays sooner, and a ranking that flips on the discount rate alone should be read as a tie and passed to [[incomparable-tasks]]. Over longer horizons or at higher rates this stops holding.

## Setting: a few people steering an agent

This wiki's reading: few such projects have an opportunity cost figure to apply, and computing present values for them is precision with no use. What transfers is the qualitative rule: between two pieces of work with similar return, prefer the one that pays sooner. On a small project this usually arrives through [[cost-of-delay]] and through delivering part of the value early, not through a discount rate.
