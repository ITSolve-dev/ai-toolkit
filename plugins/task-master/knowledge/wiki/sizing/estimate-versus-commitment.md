---
title: Estimate Versus Commitment
category: sizing
summary: An estimate is a probability attached to a date; a commitment is a date chosen after weighing business factors and risks. When the first is taken as the second, the team never gets to make that decision.
tags: [decision-rule, estimation, commitment, forecast]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Estimate Versus Commitment

An estimate and a commitment answer different questions: how likely is this date, and which date will we answer for. Cohn names confusing them the fifth cause of planning failure, and draws on Phillip Armour (2002) for the distinction.

> As Phillip Armour (2002) points out, an estimate is a probability and a commitment cannot be made to a probability. Commitments are made to dates.
>
> — [[cohn-agile-estimating-planning]], L674

Cohn's illustration is a new high-end word processor: finishing by the end of the week has probability 0%, finishing in ten years has probability 100%, and each date between has its own probability (L668-L672). This wiki reads the numbers as illustrative endpoints and not data. It reads the point as being that an estimate with no probability stated is incomplete, because "Embedded within each and every estimate is a probability that the work will be completed in the estimated time." (L668).

## The discriminating test

Ask whether anyone decided to hold to the date.

- **Estimate:** a statement about likelihood, produced from what is known about the work.
- **Commitment:** a decision, taken after that estimate, with the business situation in view. Cohn says "Prior to making such a commitment the team needs to assess a variety of business factors and risks." (L674).

The two usually land on different dates, in Cohn's account, because "Normally the date that a team is asked (or told) to commit to is one to which they would assign a less than 100% probability." (L674). This wiki reads that as meaning a commitment accepts a known risk, and that the risk has to be seen for it to be accepted.

## The rule

Keep the two apart in what is written down. An estimate does not become a date anyone answers for until someone has decided that it does. Cohn's words are "It is important that they be given this opportunity and that every estimate does not become an implicit commitment." (L674).

## Sign of violation

- **In a stated date:** a due date identical to an estimate, with no recorded decision to adopt it.
- **In a report:** a variance from an estimate is reported as a missed commitment.
- **In conversation:** Cohn's description of the outcome, "As soon as a team expresses an estimate they are forced to commit to it." (L682).

The first two are this wiki's derivation from Cohn's distinction.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The estimate and its uncertainty | [[forecast-range-and-probability]], and board history |
| Business factors and risks | The person steering; a board does not show them |
| Who decides | The project's setup |

The choice was wrong if a date treated as a commitment turns out never to have been agreed by anyone who could answer for it, or if a date nobody decided on was taken as binding.

## Why

What breaks is the decision itself. This wiki reads the consequence as follows: if giving an estimate is the same as committing, the step in which risks are weighed never happens, and those asked for an estimate have a reason to pad it. Cohn says neither of these in those words.

## Cost

This wiki notes that the separation adds a step, and that someone asking for a date is told there is a likelihood first and a date later. That is more friction than a single number.

## Relation to other pages

[[commitment-over-a-period]] covers what a project promises under each setup. The Scrum Guide's forecast there is an estimate in this sense. This page holds at any scale, including one task's estimate, and [[forecast-range-and-probability]] says how an estimate should be written. Cohn does not give a method for attaching a probability, and [[service-level-expectation]] is the nearest thing this base has.

## Agent executor note

The distinction concerns people answering for dates, so it survives, and its weight shifts. An agent cannot answer for a commitment, as [[commitment-over-a-period]] notes, so any commitment falls to the people steering. This wiki adds a plugin-side consequence: output should label an estimate as one, and should not write one into a due date without the person's decision, since a date on a board reads as agreed whoever put it there.
