---
title: Purpose of Planning
category: periods
summary: Cohn's claim that planning exists to answer what to build and not only to produce a date, and the five things a planning process supports, each filtered here for what survives a few people steering an agent.
tags: [concept, planning, estimation, value, human-mechanism]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Purpose of Planning

In Cohn's account the purpose of planning is to find the best available answer to what should be built, given features, resources and schedule. He says estimating and planning "are not just about determining an appropriate deadline or schedule" ([[cohn-agile-estimating-planning]] L403). Cohn separates three questions: planning ("what should we build and by when?"), estimating ("How big is this?") and scheduling ("When will this be done?" and "How much can I have by then?") (L316).

## The claim

Cohn grants that organizations demand estimates for ordinary reasons, such as marketing campaigns, release activities and training internal users, and that the difficulty of estimating does not excuse anyone from providing them (L395). He then calls those needs perfunctory and states the larger reason:

> Planning—especially an ongoing iterative approach to planning—is a quest for value.
>
> — [[cohn-agile-estimating-planning]], L403

Cohn says the question "cannot be answered all at once" and "must be answered iteratively and incrementally" (L403). His example is a product scoped for August 31, where in June the team may decide that slightly later with slightly more, or slightly sooner with slightly fewer, is better (L403).

## What a planning process supports

Cohn lists five supports (L405-L415). The notes on what each changes in this setting are this wiki's reading.

- **Reducing risk.** Estimating discussions expose what nobody knows. See [[unknowns-surfaced-by-estimating]].
- **Reducing uncertainty.** New knowledge about product and technology has to be fed back into the plan (L425-L431). See [[plan-conformance-as-success]] and [[changing-the-plan-without-changing-the-date]].
- **Supporting better decision making.** Trade-offs need both a cost and a benefit figure. See [[tradeoff-needs-cost-and-benefit]].
- **Establishing trust.** Reliable delivery of promised features builds trust, and "Reliable estimates enable reliable delivery." (L451).
- **Conveying information.** A plan sets baseline expectations and is not a guarantee. See [[single-date-plan]].

## The trust loop, and whether it survives an agent

Cohn describes a loop: "Reliable estimates benefit developers by allowing them to work at a sustainable pace." (L453), which yields fewer bugs, which "lead back to more reliable estimates because less time is spent on highly unpredictable work such as bug fixing." (L453).

This wiki reads the loop as half transferable. The first link depends on a human executor's pace and does not survive an agent executing, because an agent has no pace to protect. The second link survives: unpredictable rework still degrades forecasts whoever does it. The trust claim survives for the person steering, who is the one deciding whether to believe a forecast. Cohn makes no claim about agents; this transfer is the wiki's.

## Scale

Chapter 1 argues at whole-project scale, with teams of people and budgets in the millions in its examples. Its go/no-go reasoning is not kept here as a rule. This wiki reads what carries to a few people as the ordering of questions: what to build comes before when it lands. See [[agile-planning]] for how Cohn distributes that work over time.
