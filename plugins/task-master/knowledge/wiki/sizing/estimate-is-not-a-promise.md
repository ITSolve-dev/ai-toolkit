---
title: An Estimate Is Not a Promise
category: sizing
summary: Nobody is surprised when a game scheduled to end at 4:00 ends at 4:15, yet the same 8% overrun on a twelve-month project is a surprise. A forecast holds up because of the conditions around it, not because it is exact.
tags: [concept, estimation, overrun, expectations]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# An Estimate Is Not a Promise

An elapsed forecast is an estimate even when it is printed as a time. Cohn's example is the television guide listing a football game from 1:00 to 4:00: "most football fans know that when a football game is scheduled to end at 4:00 that is only an estimate" ([[cohn-agile-estimating-planning]] L1096). This page concerns how a forecast is received and what makes it safe. Whether anyone decided to hold to a date is the separate question on [[estimate-versus-commitment]].

> No one is surprised when the game goes till 4:15 (an overrun of 8%). They may be frustrated or annoyed, but not surprised. Why then are we surprised when a software project estimated at twelve months takes thirteen (an equivalent 8% overrun)?
>
> — [[cohn-agile-estimating-planning]], L1096

This wiki reads the 8% as arithmetic used for the comparison: fifteen minutes on three hours and one month on twelve. It is not a finding about how large an overrun is normal, and the chapter gives no such threshold.

## Why the network's forecast survives

Cohn lists what the network knows and the viewer does not (L1094):

- The content can flex: "they plan to add or remove a few commercials based on how quickly the game is progressing".
- The spread is narrow around the forecast: "most games are somewhere close to three hours".
- An early finish is absorbed by commercials, interviews or other filler.
- A late finish is tolerated: "If the game goes long, so what?" Interested viewers keep watching, and others wait if the delay is short.
- Expectation has been set: "after decades of televising football games, the networks have accustomed us not to expect a precise finish time".

Cohn calls the last of these the important difference (L1096). This wiki reads the list as saying that a date is safe because of the arrangements around it, and that accuracy is only part of it. A date is safer when scope can flex, history shows a narrow spread, the cost of lateness is low, and the reader knows it is an estimate. The list as a set of conditions is this wiki's arrangement; Cohn gives it as a description of one network.

## How to use it

This wiki reads the following checks as a way to apply this when a date is reported, since each condition can be read from the plan or the board:

- Is there scope that can be added or removed near the end? See [[fixed-date-variable-scope]].
- Does history for similar work show a narrow spread? See [[velocity]].
- What does a late finish actually cost the person waiting?
- Has the person receiving the date been told it is an estimate? See [[estimates-as-ranges]].

A date that fails all four raises a question about the plan. It does not show the estimate was wrong.

## Trade-offs

The football comparison has a limit that the source does not discuss. This wiki notes that the audience has decades of experience with the same event, while a software project is usually unique, so the narrow spread cannot be assumed. The comparison explains why surprise is unreasonable and gives no basis for assuming a software date will land within 8%.

## Agent executor note

This wiki reads this as independent of who executes: it concerns how a forecast is received, and that reader is the same person. Related: [[ideal-estimate-read-as-deadline]], where the problem is a number's meaning rather than its accuracy.
