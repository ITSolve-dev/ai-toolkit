---
title: Timeboxed Iteration
category: periods
summary: An iteration ends on its date even if functionality is dropped; all kinds of work happen inside it, not in phases across iterations.
tags: [rule, iterations, timebox, commitment]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Timeboxed Iteration

A timeboxed iteration is a fixed span of work whose end date holds and whose content gives way. It is the unit Cohn's planning is built on, and when an iteration runs short, the thing that gives is scope.

> Iterations are timeboxed, meaning they finish on time even if functionality is dropped to do so, and are often very short.
>
> — [[cohn-agile-estimating-planning]], L764

This wiki uses "period" for the same thing elsewhere. How the length is chosen is on [[period-length]].

## Length, with its setting

> Most agile teams work in iterations of from one to four weeks long but some teams maintain their agility with iterations of up to three months.
>
> — [[cohn-agile-estimating-planning]], L764

This wiki reads these as descriptions of human teams, not recommendations derived from anything. On consistency Cohn reports two practices without choosing: "Most teams settle upon a relatively consistent iteration length. Some, however, choose the appropriate length for an iteration at the start of each iteration." (L764).

Cohn also ranks length below output: what matters more than the chosen length is that the iteration turns requirements into tested, shippable software (L768). See [[potentially-shippable-increment]].

## Against the Scrum Guide

Cohn's report is looser than the Scrum Guide's rule, which bounds a period at one month and holds its length fixed ([[period-length]]). The two are different kinds of statement: Cohn describes what teams do, and the Guide defines a method.

This wiki resolves it by setup. Where a project has periods, [[period-length]] holds: the length is fixed, because [[filling-a-period]] reads past periods as a guide to the next and periods of varying length break that comparison. Cohn's three months and his per-iteration length are kept as reports and are not carried over as permission. The resolution is this wiki's.

## No phases

Cohn says there is "no upfront requirements phase followed by analysis followed by architectural design and so on" and, once the project is under way, "all work (requirements, design, coding, testing, and so on) happens concurrently within each iteration." (L762). The allowed exception is narrow: "you may put a very short design, modeling, or other phase at the front end of the project" (L762).

## Signs to check

Cohn names no observable sign. This wiki reads the following as questions to ask of a board's history.

- The end date of an iteration moved after it started, or an iteration was extended to let an item finish. That spends the date to keep the scope, the reverse of the rule, and it is the sign on [[period-length]].
- An iteration holds only one kind of work, such as a run of iterations named for design and then for testing. That is a phase wearing an iteration's name, and [[activity-based-plan]] is the same fault at task level.

## Trade-offs

This wiki notes that holding the date means something planned does not ship in this iteration, and the dropped item has to go back through [[unfinished-at-period-end]] and [[replanning-on-new-knowledge]]. It also reads the held date as making the boundary a reliable point for looking at the plan, which is what [[planning-horizons]] needs.

## Which setup this applies under

Under an iteration setup. Under a flow setup there is no period and nothing is timeboxed ([[what-may-move]]).

## Agent executor note

This wiki reads "the date holds, the scope gives" as surviving an agent executing, since it is a rule about the plan and not about a person's pace. The week counts do not survive as figures: they come from human throughput. Under agent execution, this wiki's reading is that the length should come from how often the steering person can review a result, which needs a source of its own before it is treated as a rule.

Related: [[planning-horizons]], [[fitting-stories-into-a-release]].
