---
title: Comparing Estimate to Actual
category: sizing
summary: Cohn advises reluctance to compare logged hours against estimates; remaining work is more useful, evaluation pressure can worsen estimates, and variability never goes away. For an agent the pressure and the logging cost fall away, and the variability does not.
tags: [decision-rule, estimation, retrospective, agent-transfer]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Comparing Estimate to Actual

This test decides whether to compare what work took against what was estimated, in order to estimate better. Cohn's position is cautious:

> Teams should be reluctant to track the actual hours expended on tasks in order to get better at estimating. The risks and the effort to do so usually outweigh the benefits.
>
> — [[cohn-agile-estimating-planning]], L4551

The charter drops tracking spent hours as a practice. This page keeps Cohn's reasoning, because the question of how an estimate is refined against fact is in scope, and it answers with time lived from board history and not with logged hours.

## Cohn's three arguments

1. **Remaining beats spent.** "On a project, it is far more useful to know how much remains to be done rather than how much has been done." (L4521). His sailboat analogy carries the reason: "Measuring the distance traveled or time spent traveling are not helpful if we’re not sure all progress was in the right direction." (L4519). See [[overrun-triggers-a-recut]].
2. **Evaluation pressure can backfire.** Comparing effort with estimates "can lead to “evaluation apprehension” (Sanders 1984)" (L4521), under which estimators "rely more on instinct than on analytical thought (Jørgensen 2002)" (L4527). Whoever tracks must "avoid putting significant evaluation pressure on the estimators as doing so could results in estimates that are worse rather than better" (L4529).
3. **Variability has a floor.** "No matter how much effort is put into improving estimates, a team will never be able to estimate perfectly." (L4531). His example is a morning commute, whose variation no driving skill removes.

Cohn does not rule the comparison out: "Tracking effort expended in an effort to improve estimate accuracy is a very fine line. It can work (Lederer and Prasad 1998; Weinberg and Schulman 1974)." (L4529). All four studies are reached through Cohn and have not been read here, so the page reports his citation of them and not their findings. He gives no effect sizes in this chapter.

## The test

This framing and the inputs below are this wiki's.

Compare only if all three hold:

1. The comparison uses data the board already has, so nobody keeps a log.
2. The comparison looks at a size step across many tasks, not at one task.
3. No person's estimates are singled out by it ([[individual-velocity]]).

| Input | Read from |
|---|---|
| Time each task lived, per size step | Board history |
| The size step each task carried | Board history |
| Whether results are reported per person | The report itself |

The choice was wrong if the spread within a size step stays the same over many periods and effort keeps going into reducing it, since that is Cohn's floor. It was also wrong if, with people estimating, size steps drift upward after the comparison starts while time lived does not, since that is his evaluation pressure showing up as padding.

## Sign of violation

- **In a report:** estimate accuracy broken down by person.
- **In board history:** a size scale recalibrated after a single miss. This wiki reads the commute argument as saying one miss is not evidence.
- **In a process:** a task field for logged hours that someone must fill in.

## Trade-offs

Refusing the comparison leaves a size scale unchecked against fact, which the charter wants refined. Using time lived in place of effort is imprecise: a task's life includes queues and waits. Read [[flow-metrics]] for what it does measure.

## Agent executor note

Argument 2 rests on a human response, a "fight or flight" instinct (L4527), and does not survive for an agent. Part of Cohn's "effort" also goes, because run duration is recorded without anyone keeping it. This wiki reads his balance as shifting for agent-executed work: the comparison gets cheaper and safer. Argument 3 survives, so cheaper comparison does not promise convergence, and argument 1 survives, so a comparison never replaces asking what remains.

The evaluation-pressure argument still applies where people in the steering seat produce the estimates and someone else reads the comparison.
