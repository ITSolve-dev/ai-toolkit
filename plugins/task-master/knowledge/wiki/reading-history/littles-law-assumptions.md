---
title: Checking Little's Law's Assumptions
category: reading-history
summary: Which assumptions a flow calculation needs depends on the form of the law and on whether WIP reached zero; each throughput-form assumption can be checked against board history for a chosen window, and three of them double as an audit of a process's policies.
tags: [method, flow-metrics, predictability, conservation-of-flow, stability, retrospective]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Checking Little's Law's Assumptions

This method tests whether the Throughput form of [[littles-law]] can be trusted for a chosen window of board history. Vacanti treats the assumptions, not the formula, as the substance of the law, and every process policy he derives from it comes from them ([[vacanti-actionable-agile-metrics]] L1000-L1004, L1016).

## Step 1: find which case applies

| Situation | What is required | Standing of the result |
|---|---|---|
| Arrival form, Equation (1) | Steady state (stationary processes), an arbitrarily long observation period, consistent units (L934-L938) | Holds under those conditions |
| Throughput form, WIP is zero at both ends of the window | A start and end with zero WIP, and everything that enters eventually exits (L954) | Exact |
| Throughput form, WIP never reaches zero | All five assumptions below (L966-L976) | Holds if they hold; otherwise an estimate |

The second case is the strong one: "Little’s Law is exact between any two time instances where total process WIP is zero" (L954). It needs no assumption about stability or about the length of the period. Vacanti notes separately that consistent units are needed in every form (L988).

## Step 2: check each assumption over the window

The five assumptions and their grouping are Vacanti's (L968-L976, L986). The signs are this wiki's reading of where each one shows in board history, because the source defers how to read them to its Chapters 7-9. A sign raises a question, not a verdict.

| # | Assumption | Notion | Sign to read from board history |
|---|---|---|---|
| 1 | Average Arrival Rate equals average Departure Rate | [[conservation-of-flow]] | Items entering the process exceed items leaving it across the window |
| 2 | All work started eventually completes and exits | Conservation of flow | Items closed without finishing, or items open since long before the window with no movement |
| 3 | WIP is roughly the same at the start and the end of the window | Stability | The open-item count differs noticeably between the two ends |
| 4 | Average age of WIP is neither rising nor falling | Stability | Mean age of open items at the end of the window differs from the start |
| 5 | Cycle Time, WIP and Throughput use consistent units | Arithmetic | A calculation mixes units; see below |

## Step 3: read the result by project setup

This section is the wiki's own resolution, built on the source's cases.

- **A sprint or project that closes with an empty board:** the exact case applies. Vacanti's examples are an ideal project and canonical Scrum, where "by definition you start each sprint with zero WIP and you end each sprint with zero WIP", with the caveat that "practice usually falls far short of prescription" (L954).
- **A sprint with carry-over:** this is the five-assumption case. Unfinished sprint work is one of Vacanti's own examples of never running out of WIP (L962). The Scrum label does not earn the exact result; an empty board at both ends does.
- **Continuous flow, or several concurrent streams:** the five-assumption case applies (L962).
- **A few people steering an agent:** this wiki's unverified expectation is that a small batch may genuinely drain to zero between batches, which would make the exact case more common than Vacanti's teams found it. The check is the board: whether the open count actually reached zero.

## When an assumption fails

A failed assumption does not void the calculation: the law "can still be used as an estimation", but "the “goodness” of the estimation depends on how badly the assumptions have been violated" (L978-L984). Vacanti's stronger claim is that the cost is paid whether or not anyone computes the law:

> Every time you violate an assumption of Little’s Law your process becomes less predictable.
>
> — [[vacanti-actionable-agile-metrics]], L1006

He says the cost may appear as longer Cycle Times, more variability or both, and that it may not appear at once: the data "may be showing you a rosier picture of the world than is really occurring", and a forecast built on it can be much too optimistic (L1006-L1012). This wiki reads one way that can happen as follows: Cycle Time is measured on finished items, so items left ageing do not yet count against it, and the finished set looks healthy while assumption 4 is failing. The source does not give this mechanism in this chapter.

## The same checks as a policy audit

The steps above test a window of data. Vacanti's *Getting Started* chapter turns the assumptions on the policies that produce the data, asking which "are in direct violation of the assumptions of Little’s Law" (L3800). The stake is the same: "each violation of one of Little’s Law’s assumptions hampers your ability to be predictable" (L3800).

The questions appear at L3800, and the same three appear as rules in the book's closing summary (L3934-L3938). The right column is this wiki's reading of where each shows up. [[process-policies-from-littles-law]] states the positive form.

| Policy check | Rule | Where to look |
|---|---|---|
| Are arrivals explicitly controlled? | "Do not start new work at a faster rate than you finish old work." (L3934) | Items started per period against items finished per period; a WIP count that keeps rising |
| Does everything started complete? | "Minimize the amount of work that is started but never finishes." (L3938) | Items cancelled after their arrival date; items abandoned in an active state with no recorded outcome |
| Do items age arbitrarily? | "Do not allow items to age arbitrarily due to blockages, too much WIP or poor pull policies (Class of Service)." (L3936) | Open items much older than others of their kind, especially ones blocked or passed over by newer work |

The source gives softer forms that matter for reading the result. The second check allows a fallback: make sure everything started completes, "or at least tag and track items that do not complete properly" (L3800). This wiki reads that as follows: an item cancelled with a tag stays explainable in history, and an untagged one looks like an ordinary completion ([[capturing-flow-data]], [[non-standard-departure]]). Ageing is listed with its causes: "Class of Service, blockages, queuing, etc." (L3800).

The instruction is modest: "you may want to think about changes to implement to get your process more aligned with that law" (L3800). It sets no threshold, so a breach here is a question about a policy and not a defect to be scored ([[smell-is-not-a-finding]]). The chapter states the checks without deriving them, and it gives no figure for what a violation costs.

This wiki's reading for a few people steering an agent: an agent can start tasks faster than a person can review them, so the first check is the one most likely to fail between execution and review, and reading it means counting work waiting on the person as open ([[blocked-work-counts-against-wip]]).

## Failure mode: mixed units

Vacanti reports a Scrum team that plugged velocity in story points per sprint in as Throughput, used the count of stories completed in the sprint as WIP, and expected a Cycle Time in days (L988-L994). The numbers did not come out as they expected. Throughput must be items per the same time unit in which Cycle Time is expressed, and average WIP must be averaged over that same unit (L988).

- **Sign:** a flow calculation takes [[velocity]] as its Throughput, or its inputs carry different time units or different counted things.
- **What breaks:** the output has no meaning in the unit it is reported in.
- **Discriminating test:** velocity counts points; Throughput here counts items.

## Trade-offs

The check needs a chosen window, and its result may change with that choice, because assumptions 3 and 4 compare the window's two ends. This wiki suggests recording the window alongside any finding. Violations can also be legitimate: Vacanti allows that they are sometimes "unavoidable or even necessary" (L1014). The aim of the check is to know a violation is happening and what it costs, not to forbid it.
