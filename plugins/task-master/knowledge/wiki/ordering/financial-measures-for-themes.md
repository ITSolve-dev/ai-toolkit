---
title: Financial Measures for Comparing Themes
category: ordering
summary: NPV, IRR, payback period and discounted payback each answer a different question about a theme's cash flow; none decides alone, and the chain needs money figures a board does not hold, so it applies to themes only when a person supplies them.
tags: [decision-rule, ordering, prioritization, value, themes]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Financial Measures for Comparing Themes

Cohn ([[cohn-agile-estimating-planning]]) compares themes, meaning groups of related stories ([[theme]]), by converting each theme's forecast into a cash flow stream and reading that stream through four measures: net present value, internal rate of return, payback period and discounted payback period (L1926-L1932). Each measure answers a different question. The chapter's conclusion is that the choice stays a judgement: "Making a decision is not cut and dry; the product owner and team will need to consider a variety of situationally-specific factors" (L2324).

## Which measure answers which question

| Question | Measure | What it does not answer |
|---|---|---|
| How much is this worth today? | NPV: the sum of the present values of the stream (L2179) | How much cash it ties up to get there |
| How fast does the money grow? | IRR: the rate at which NPV is 0 (L2236) | How much money that is, or who else needs the same people |
| How long is the money at risk? | Payback period: time to earn back the investment (L2270) | Time value, and profitability (L2291-L2295) |
| The same, in today's money? | Discounted payback period: payback run on discounted flows (L2299) | Profitability |

## Why no single measure is enough

- **NPV hides the size of the investment.** Two projects can both show ¤100,000 NPV with very different upfront cost, so "comparing the values of two different cash flow streams can be misleading" (L2205). An NPV floor also fails, because "NPV values are highly dependent on the magnitude of the project", and with such a floor "small (but valuable) projects would never be approved" (L2222). The usable threshold is a minimum attractive rate of return applied to IRR (L2222).
- **IRR hides scale and capacity.** "You cannot usually use IRR in isolation, though, for making decisions." (L2258). Cohn gives two reversals. A 45% project on a small investment and a 25% project on a large one may need the same critical developer, and the 25% project may earn more. A 45% project needing two years of investment may lose to a 25% project that pays from year one, if the organization cannot fund the wait (L2258-L2260).
- **IRR is not always computable.** It needs one or more expenses first, a stream that stays positive once it turns positive, and more money in than out overall (L2244-L2248). This wiki notes that a theme with recurring later costs fails the second condition.
- **Payback does not measure profit.** It says when the money returns, but "it doesn’t address how much money will be made" (L2295). Its merit is reading risk: "The larger the payback period, the riskier the project because anything could change during that period." (L2289).

## The worked comparison

Table 10.15 (L2328-L2332), at ¤675 per point:

| Theme | Points | Cost | NPV | ROI | Discounted payback |
|---|---|---|---|---|---|
| Overnight service | 150 | ¤101,250 | ¤46,341 | 45% | 7 quarters |
| Custom reporting | 90 | ¤60,750 | ¤34,533 | 15% | 6 quarters |
| Partner integration | 60 | ¤40,500 | ¤30,013 | 49% | 3 quarters |

Cohn reads it this way: overnight has the highest NPV and the longest payback, partner integration the best rate and payback with the lowest NPV, and custom reporting the lowest rate, though it "could be combined with partner integration and done with the same cost as the overnight service theme" (L2324). The factors he lists for deciding are tolerance for risk, need for short payback, availability of resources, and other options for the money (L2324).

This wiki adds the arithmetic he leaves implicit: the combination costs ¤101,250 and sums to ¤64,546 of NPV against ¤46,341 for overnight alone. So the comparison is between sets of themes that fit a capacity, not between single rows. The sum ignores that the same team cannot start both on day one, which would push one stream later.

## Applying the rule

The inputs and where each is read from:

- **Return per period for each theme:** from the requester or from whatever market research justified the work ([[sources-of-return]]). Not on a board.
- **Cost:** the estimate times [[cost-per-story-point]]. On the board, if estimates and velocity exist.
- **Discount rate:** the organization's opportunity cost ([[time-value-of-money]]). Not on a board.
- **Constraints:** who is scarce and how long the money can stay out. Only a person knows these.

The chapter names no later fact that would show a choice wrong. This wiki's reading: the check is the forecast itself. If the running total of actual returns is not on the forecast path when the projected payback period arrives, the valuation that ordered the theme was wrong, and any theme still queued on the same assumptions deserves a second look.

## Setting: a few people steering an agent

This section is this wiki's reading, not Cohn's.

The unit here is a theme of 60 to 150 points, several iterations long, in an organization with salespeople, a finance function and a discount rate. A task on a small board cannot carry a cash flow of its own, so this chain does not order tasks.

Three parts transfer anyway. The questions are separable: how much, how fast, and how long at risk stay distinct, and a person choosing between two large bets can answer them roughly. Combining smaller items to the capacity of one large item transfers directly. And scarcity beats rate: the "critical developer" reversal survives with the steering person as the scarce resource.

For the plugin, these money figures are task-only facts ([[recoverable-versus-task-only-facts]]). If a person supplies them, the plugin may compare themes this way and must show the measure beside the number. If nobody supplies them, ordering stays with [[ordering-by-value-and-urgency]], and the plugin does not invent a figure. A figure with no one behind it is the case [[incomparable-tasks]] handles.

These measures also value a theme; they do not say what waiting does to it. Two themes with equal NPV can differ entirely in what a quarter's delay costs, which is what [[cost-of-delay]] asks, so this wiki treats a high return as an argument about importance rather than urgency ([[urgent-versus-important]]). The chapter does not make this distinction.

## Defects in the source's figures

This wiki recomputed the chapter's numbers. NPV, payback and Table 10.11 all reproduce. These do not:

- **The WebPayroll IRR is wrong as stated.** Cohn says the Excel formula yields 12%, "equivalent to earning a 12% annual return on the company’s investment" (L2254). The stream is quarterly, so that function returns a per-quarter rate: 12.2% per quarter, or about 49% nominal and 59% effective per year. His own definition rules out 12% annual as well, since NPV at 12% a year is ¤46,341 rather than 0 (L2187, L2236). Table 10.15 then shows 45% for the same theme (L2330), which matches neither.
- **ROI carries two meanings.** L2211 makes ROI a synonym of IRR. L2171 says "ROI calculations put equal value on the money invested in year one and the money earned in year five", which describes an undiscounted figure. Do not cite the ROI column without saying which is meant.
- **Cost and NPV in Table 10.15 rest on different costs.** See [[cost-per-story-point]].

The failure to guard against, seen in the source itself: a rate computed on quarterly flows and reported as annual. The sign is a rate with no stated period.
