---
title: Flow Metrics for Scrum Teams (Vacanti and Seele)
category: periods
summary: A short practitioner book by Daniel Vacanti and Will Seele that runs Scrum's events on flow data; most of it repeats Vacanti's earlier book, and it was ingested in part. It adds a recipe for forecasting from daily Throughput, a third way to fill a period, Work Item Age named as the first measure to read, policies for blocked work and three more cuts. It reports no measurement in the ranges read.
tags: [summary, flow-metrics, iterations, forecasting, scrum]
sources: [flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Flow Metrics for Scrum Teams (Vacanti and Seele)

This is *Flow Metrics for Scrum Teams* by Daniel Vacanti and Will Seele (L115), subtitled "Because story points were never a part of Scrum anyway" (L113), in the Leanpub version published on 2022-08-10 (L117-L119). The raw file's `authors` and `published` fields are empty, and the title page carries both.

## Gate: partly in scope, read in part

The book restates much of [[vacanti-actionable-agile-metrics]] for Scrum, and it says so of its Chapter 9 (L1468). This ingest was directed to read only four ranges and the title page.

| Lines | Content | Result |
|---|---|---|
| L372-L382 | Work Item Age | [[work-item-age]] |
| L776-L1095 | Sprint Planning, parts I and II | [[throughput-monte-carlo]], [[filling-a-period]] |
| L1118-L1318 | The SLE at a daily check, and items not flowing | [[blocked-work-policies]], [[percentile-intervention-triggers]], [[story-splitting-patterns]] |
| L1382-L1442 | When is it done, and what can be done | [[throughput-monte-carlo]], [[date-driven-vs-feature-driven]] |

The rest was not read. Saying that it repeats the earlier book is the direction given to this ingest and not a finding of this page. One part is known to be new to this base: Chapter 4's Aging Chart (from about L736), since "Aging Chart" does not occur in the raw of the earlier book. [[work-item-age]] holds only what L1154 says of it.

## Thesis

Scrum's events can run on flow data in place of estimates. Planning forecasts a count from Throughput at a chosen risk, the daily check reads each open item's age against percentile lines, and a review forecasts the rest of the work the same way. The conclusion to the planning chapters puts it in one line: "feed historical Throughput data into an MCS and interpret the results to make probabilistic forecasts about what can be done." (L1080).

## What this wiki took from it

- A recipe for simulating from daily Throughput, in both directions, with how to read each and how to choose the window and the risk: [[throughput-monte-carlo]].
- A third way to fill a period, which this wiki resolves by setup: [[filling-a-period]], and the consequences on [[velocity]], [[velocity-versus-commitment-planning]] and [[dropping-estimates-for-flow-forecasts]].
- Work Item Age as a measure of its own: [[work-item-age]].
- Three levels of policy for blocked work: [[blocked-work-policies]].
- What to do at a percentile line, and which question to ask first: [[percentile-intervention-triggers]].
- The size check run at selection, and the question of smallest value: [[right-sizing]], [[size-ceiling]].
- Three more cuts, by acceptance criterion, by customer and by assumption: [[story-splitting-patterns]].
- A bare count as a failed forecast: [[forecast-range-and-probability]].
- A figure for how much Throughput a simulation wants, in days: [[how-much-flow-data]].

## What repeats the base

These passages say what a page already holds, so those pages were left alone unless a condition was added.

- Dividing by an average rate (L802-L812): [[forecast-from-an-average]].
- The general pattern of a Monte Carlo method (L842-L850): [[monte-carlo-simulation]].
- Right size is not same size, and the wood chipper's floor and ceiling (L1034-L1036): [[right-sizing-not-same-sizing]], [[size-ceiling]].
- Skipping the Scrum Guide's decomposition to a day or less (L1048): [[size-ceiling]].
- Checking a tool by computing the result yourself (L1058-L1062): [[verifying-tool-flow-analytics]].
- That not all items finish inside a period (L1130): [[iteration-length-versus-cycle-time]].
- The SLE, how it is chosen, and the rise from 15% to 30% to 50% (L1144-L1168): [[service-level-expectation]], [[percentile-intervention-triggers]].
- WIP hidden in a large item (L1228): [[hidden-wip-in-large-items]].

## What this wiki dropped, and why

- **Planning durations and timeboxes** (L1064-L1076). These concern how long a meeting takes, which is a ceremony.
- **The conversations around a forecast** (L1418-L1428), including the budget argument. These are scripts for a meeting.
- **The Daily Scrum example** (from L1318). It is outside the ranges read, and it is a script.
- **Staffing and vendor remedies** (L1178, L1196). These manage people.
- **The worked prototyping ladder** beyond its one rule (L1304-L1316). Its steps are people's research, and the rule is kept on [[story-splitting-patterns]].

## How far to trust it

The ranges read report no measurement. The figures are illustrations whose charts are lost, and the claims are practice. This wiki reads "a very accurate forecast" (L1090) as an assertion, and the evidence offered for the cuts is "It is a list that Dan, Will, and others have successfully used in the past" (L1230). Under the charter the book is graded on its mechanisms.

It is no second voice for [[vacanti-actionable-agile-metrics]], since Vacanti is its first author, and neither is it independent of [[kanban-guide]]. Where this book agrees with those, this wiki counts one voice. This wiki reads the stake as the same too, since the authors say "he has a very strong bias to one tool in particular" (L1056). The tone is provocative, as in "snake oil" (L970), and this wiki reads such a sentence as a position.

Its claims are wider than its support in places.

- It says "estimation is not needed" (L970) and then that the count covers right-sized items only (L1022). This wiki reads the second as limiting the first ([[dropping-estimates-for-flow-forecasts]]).
- It calls the stability assumption safe under professional Scrum (L862). This wiki does not accept that ([[forecast-needs-a-stable-process]]).
- It says a stuck item is usually too big (L1210) and elsewhere gives other causes (L1178, L1196). This wiki settles the order by what the board shows ([[percentile-intervention-triggers]]).

Agents appear nowhere in the ranges read, and every mechanism assumes a team of people.

## Slips in the text

- The method's steps repeat "steps 2-3" at L850 and "steps 1-3" at L886. This wiki follows L850, since the input does not change between runs.
- The caption of Figure 5.3 reads "18 Or More Items Complete" (L936) over a passage about 12 (L938).
- One form is "How Much" at L1390 and "How Many" at L1422.
- The same line calls one figure both "up to 8" (L1020) and "the minimum capacity to plan for" (L1020). This wiki reads it as the floor at that probability, used as a limit on selection.

## Extraction caveat

Running heads and page numbers are interleaved with the text, so paragraphs break across raw lines (for example L946-L952). Quotations on this wiki's pages stay inside one raw line. Figures are lost and their captions survive, so every number here comes from the prose. Endnote markers appear in the text as superscript characters.
