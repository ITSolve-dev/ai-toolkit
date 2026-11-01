---
title: Chosen Delay Versus Slip
category: reading-history
summary: Before calling a release late, check which date people were told, whether scope changed by a recorded decision, and whether the earlier date was still available; a later finish with none of these is a slip.
tags: [decision-rule, plan-versus-fact, retrospective-analysis, release-planning, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Chosen Delay Versus Slip

A later finish is not one event. This wiki's definitions: a slip is the same scope arriving later than forecast, and a chosen delay is a later date taken by decision in exchange for more value while the earlier date was still reachable. The fictional case study in [[cohn-agile-estimating-planning]] draws this line twice, once in advance and once afterwards.

> It wouldn’t be a slip, Phil
>
> — [[cohn-agile-estimating-planning]], L6320

The product manager backs that by saying the original 12-20 weeks was still achievable, and that the open question was how much longer a more valuable game would take (L6320).

## The test

Read each of these from history. The three questions are this wiki's reading of what the case's characters argue.

1. **Which date were people told?** Compare with that, not with an internal figure. A tester says "We originally thought we’d be done in just over 14 weeks." (L6496), and the answer is "We never said we’d be done in 14 weeks." (L6498). People had been told 12-20.
2. **Did the scope change, and was the change recorded when it was decided?** The total rose by 35 points at a known moment (L6362-L6364).
3. **Was the earlier date still available?** "we could have shipped two weeks ago if we’d wanted" (L6500). The extra two weeks went to changes from beta testers.

This wiki's reading: where all three point the same way, the delay was chosen. Where the total did not change and the date moved, it is a slip, whatever it is called. A rise that came from revised estimates and not from a decision also counts as a slip here, which is why the total has to be split first ([[release-progress-forces]]).

## The sign

A forecast moves later with no rise in the release total at that point in board history. This wiki reads that as the slip's signature, to be checked against estimates that grew. A rise in the total with a dated decision beside it is a replan. Each sign raises a question ([[smell-is-not-a-finding]]).

## What later fact would show the reading wrong

This wiki reads the claim that an earlier date was available as checkable: the stories in the release were finished by that date. If they were open when it passed, the delay was not chosen. The case cannot be checked this way, because the only evidence for the earlier date is the product manager's statement (L6500).

## The trade-off

The distinction is easy to abuse, and the case does not fully clear itself. Its product manager concedes the first plan's error and counts the distance from the top of the range.

> Sure, the initial schedule was wrong but so was the product design.
>
> — [[cohn-agile-estimating-planning]], L6500

The release ended two weeks past the upper bound people had been told, and a person there still reported "the feeling that we’re late" (L6496). This wiki reads a chosen delay as one that was recorded when taken and offered against a still-open earlier date. A label applied afterwards, with no such record, does not qualify.

## Why a range matters here

A single figure leaves no room for any of this.

> It’s a good thing our original schedule was a range and that we didn’t just tell people ‘eight iterations.’
>
> — [[cohn-agile-estimating-planning]], L6368

This wiki reads the range as what made "two weeks past" a small statement and not a large miss against a point estimate ([[stating-plan-uncertainty]]). The figures are a narrative's and show how to read a comparison, not a typical overrun. Whether the plan was still good enough to decide on is the separate question on [[good-plan-test]].

## Agent executor note

This wiki reads the test as independent of who executes, since it asks about dates, totals and decisions. The decision has to be written where history can find it, because an agent keeps no memory of why a date moved ([[fact-stranded-outside-the-task]]).

How the scope was accepted is [[adding-scope-to-a-release-plan]]. The arithmetic behind each forecast is [[reforecasting-a-release-from-velocity]]. For a date treated as a reason to hurry, see [[a-date-is-not-urgency]].
