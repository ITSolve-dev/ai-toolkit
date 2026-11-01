---
title: Sources of Return
category: ordering
summary: A theme's return is forecast per period under four headings, new revenue, incremental revenue, retained revenue and operational efficiencies, and retained revenue can start before delivery; the requester should be able to quantify the reason.
tags: [method, ordering, prioritization, value, themes]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Sources of Return

Cohn ([[cohn-agile-estimating-planning]]) forecasts what a theme will earn or save by filling one row per period under four headings: new revenue, incremental revenue, retained revenue and operational efficiencies (L1950). Though "it is common for one category to dominate" a project's return, most earn from more than one (L1950). The result is the cash flow stream that [[financial-measures-for-themes]] reads.

## The four headings

- **New revenue:** from customers you do not have, which can arise even when the software is not sold directly (L1954).
- **Incremental revenue:** more from existing customers, through more licences, add-ons, a higher price, or consulting (L1962-L1970).
- **Retained revenue:** "the revenue an organization will lose if the project is not performed" (L1974).
- **Operational efficiencies:** tasks streamlined or removed. On commercial software, "most often this will refer to your own inefficiency" (L1978), such as tooling built for the project itself.

The headings are a default. Change or split them when a theme needs it: "It is not necessary to estimate all themes with the same set of columns." (L1914). The same project can legitimately land in two headings, as when a multi-practitioner version retains growing customers and also justifies a higher price (L1974).

## Procedure

1. **Fix when it ships.** Divide the theme's points by velocity to get iterations, since returns cannot begin before that. In the example, 150 points at 20 per iteration is 8 iterations (L2010). Partial delivery moves this date earlier, and it "should always be a goal" (L2010).
2. **Forecast per period, by count times value.** New customers per quarter times revenue per customer (L2014-L2016). Prorate the quarter in which the theme ships (L2016).
3. **Price only the difference.** Retained revenue counts customers who would otherwise leave. Operational efficiency counts staff not hired against the existing staffing plan, not staff removed (L2085).
4. **Subtract development cost by period and sum to net cash flow** (L2144-L2157). Development cost comes from [[cost-per-story-point]].

## Horizon

Cohn's default is two years by quarter: "I find that looking out two years works well on most projects. It strikes a good balance between guessing at the distant future and looking far enough ahead." (L1893). The condition he gives is the high uncertainty of software projects. It is an author's judgement, not a measurement, and he allows monthly rows or a longer look (L1893, L2342).

## Things the example shows that a naive forecast misses

- **Retained revenue can begin before the feature exists.** In the example, customers stay on the prospect of it: "the benefits of the overnight project begin in the first quarter, even though overnight delivery won’t be available until in the second quarter" (L2060). This wiki reads a return that starts before delivery as depending on those customers knowing the work is coming; a forecast cannot count it for an unannounced theme.
- **Operational inefficiency is sized at the future load, not today's.** Returns processing at two person-hours a day is no issue today, and it becomes twenty person-hours a day if sales grow ten-fold (L1982). The drive "comes from anticipated growth" (L1982).

## Rule: the requester quantifies the reason

"At a minimum, whoever is requesting the theme should be able to quantify the reasons for developing it." (L1918). The chapter's epigraph states the hard form: "As a general rule of them, when benefits are not quanified at all, assume there aren’t any." (L1887, spelling as in the source file; DeMarco and Lister).

- **Sign:** a request whose stated benefit carries no number and no unit, and no one who can give one.
- **What it does not require:** solid data. The worked example runs on a salesperson's impression, with "We don’t have any solid data." (L2014) and no metric for churn at all (L2041).

This wiki reads the epigraph with [[incomparable-tasks]]: asking comes first ([[clarifying-questions]]), and what remains unquantified counts as no shown benefit, so it is neither ranked on a guess nor closed for that reason alone. The sign raises a question, not a verdict.

## Failure modes

These failure modes are this wiki's derivation from the procedure.

- **One-column forecast.** A theme that prevents loss or saves effort is valued on new revenue alone, and looks worthless. Sign: empty columns on a theme whose stated purpose is keeping customers or removing manual steps.
- **Counting the feature's whole value as of the start.** Returns placed in periods before the theme ships, retained revenue aside. Sign: non-zero new or incremental revenue before the iteration count from step 1 has elapsed.
- **Precision the inputs do not have.** The arithmetic gives figures to the euro from estimates like "around one-third" (L2014). This wiki treats the forecast as an ordering aid, and not as a commitment.

## Setting: a few people steering an agent

This wiki's reading: most small projects have no sales forecast, so the heading that usually applies is operational efficiency, including the project's own tooling, sized as person-hours or agent runs avoided. Retained revenue maps to what stops working for existing users if the work is not done. Both can be stated roughly by the person steering, and neither can be read from a board.
