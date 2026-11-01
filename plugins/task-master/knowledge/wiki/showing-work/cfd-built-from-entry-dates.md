---
title: Build a CFD from Entry Dates, Not Counts
category: showing-work
summary: A CFD is derived from the date each item entered each step, not from periodic counts of what sits in each column, because counts subtract when items move back or are removed and lines then fall; counts are safe only if neither ever happens.
tags: [rule, showing-work, cfd, board-history, flow-metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Build a CFD from Entry Dates, Not Counts

A [[cumulative-flow-diagram]] is derived from the date each item entered each step, and not from counting what sits in each column at intervals. The usual advice is to count the items in each step at regular intervals and plot the counts. Vacanti calls this "building a chart based on counts" and says that "building a chart just by counting items in progress is, in a word, dubious." ([[vacanti-actionable-agile-metrics]] L1288). The rule he gives instead: "what we really need to do is track the date that a particular item enters each step of our work flow." (L1418).

This reads oddly against his own anatomy, which says that at each interval we "calculate the total number of items at each step" (L1206). This wiki reads the two as fitting together: the plotted value is a cumulative count, and his objection is to obtaining it by counting what is in progress at that moment.

## Why counts fail

A count cannot represent an item that went somewhere other than forward. His example: reporting hourly, four customers arrive at 9:59 and leave at 10:01 for a non-standard reason, the arrival count is decremented, and the arrival line falls (L1354). That produces "a negative arrival rate", which "violates the whole principle of a _Cumulative_ Flow Diagram" (L1370), and which cannot exist, because "[a]rrivals are binary: either something has arrived or it has not." (L1370).

> This is where building a CFD based on counts breaks down and why it is very difficult—and not at all recommended— to build a CFD just by counting items.
>
> — [[vacanti-actionable-agile-metrics]], L1372-L1378

## When counts are enough

Counts work only if both conditions hold (L1434-L1438):

1. "You never have items that move backward in your workflow"
2. "You never have items that are just completely removed from your process before they are completed"

Vacanti reports at least one of these in every process he has been part of (L1440). The second can be repaired on its own by counting every exit in Done (L1442); see [[non-standard-departure]]. The first cannot.

## The second reason

Even where counts would draw a correct chart, they stop there. With dates "we also get all the data we need to build an array of other very useful charts" (L1430), and Cycle Time needs them regardless (L1452). The reasoning is short: "So since you can create a CFD from dates, why not just use those?" (L1452).

## How the choice is applied

| Input | Read from |
|---|---|
| Each item's date of entry into each state | Board history |
| Whether any item moved backward or left unfinished | Board history |

This wiki reads the derivation as follows; the source calls it "rather straight forward" (L1424) and does not give it. A line for a state, at a date, counts the items whose entry into that state or any later state is on or before that date. Counting later states as well keeps an item that jumped straight to Done from pushing one line beneath another.

Built this way a line cannot fall, because adding dates only raises a count. This wiki reads that as the real reason dates work: a correction changes the record and redraws the past, instead of subtracting from today.

**Sign of violation:** the chart's data is a table of column sizes per date, with no per-item dates behind it; or a line falls ([[malformed-cfd]]).

**What would show the choice wrong:** a line falls on a chart believed to be date-built, which means the derivation or the data is at fault.

## Cost

The book's data holds one date per item per step. This wiki reads that as a real loss: a second visit to a state has nowhere to go, so the first visit's date is either kept or erased. That is the concrete form of the data problem [[backward-movement]] leaves unspelled, and a reason to draw expected cycles as forward states.

Collecting the dates costs nothing in this setting. They come from board history, in line with the charter's position that the time a task lived is read and not logged. Nobody has to keep them, which removes the human-discipline dependency a manual date table would have.
