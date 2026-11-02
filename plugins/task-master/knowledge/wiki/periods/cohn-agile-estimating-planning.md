---
title: Agile Estimating and Planning (Cohn)
category: periods
summary: Mike Cohn's practitioner book, here in a pre-publication manuscript, on planning as finding the best answer to what to build and by when; it keeps size apart from duration, derives dates from a measured rate, states uncertainty and replans each iteration. It is the wiki's largest source, written for human teams on iterations, with no agent in it and no measurement of its own.
tags: [summary, estimation, release-planning, iterations, prioritization, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Agile Estimating and Planning (Cohn)

This is a book in seven parts and twenty-three chapters (L318). The raw file's `title` reads "AEP2.book" and its `authors` field is empty, so the author and title here come from the origin file name (L5) and from the book's own introduction (L314). It is a manuscript and not the printed book: the acknowledgments read "TBD--this will come later" (L344). This wiki cites it by line of the raw file, so a citation does not map to a page of the published edition.

It is the wiki's largest source by far. It stands behind most of `sizing`, `periods` and `ordering`, and its pages make up about three quarters of the base.

## Thesis

> Planning is an attempt to find an optimal solution to the overall product development question: features, resources, and schedule.
>
> — [[cohn-agile-estimating-planning]], L4829

The book is "mostly about planning", which it takes as answering "what should we build and by when?" (L316). Its claim is that the process has to be agile itself (L314). Its closing summary gives the reasons it works: plans made at different levels with frequent replanning, plans based on features and not tasks, size estimated first with duration derived from it, small stories, work in process removed at each iteration's end, progress measured at team level, and uncertainty acknowledged and planned for (L4947).

## Authority

The authority is a practitioner's. The author writes in the first person from projects he has worked on, including two named case studies on iteration length (L3522, L3534). He borrows from others where he reaches for evidence: the cone of uncertainty from Boehm (L374), survey and overrun figures from Lederer and Standish (L529-L533), a user sample size from Griffin and Hauser (L2423), and cycle time from queuing theory by way of Poppendieck and Reinertsen (L4873). The book reports no study of its own and gives no measurement of whether its process produces better results. Under the charter it is graded on mechanisms, and a figure in it is kept with its setting or dropped.

## Scope

- **Covers:** size and duration, story points and ideal days, techniques for estimating, re-estimating, prioritizing by value, cost, knowledge and risk, financial measures, the Kano model and relative weighting, splitting, release and iteration planning, iteration length, estimating velocity, buffers, multi-team planning, monitoring and communicating.
- **Setting assumed:** one cross-functional human team on fixed iterations, with a product owner. A planning poker group "will typically not exceed ten people" (L1312).
- **Thin or absent:** continuous flow without iterations, WIP limits across a workflow, and intake. Cycle time and work in process appear only as supporting arguments (L4873-L4887). No agent appears, and the book's latest dated reference is from October 2004 (L6622).

## Key takeaways

- **Size and duration are separate estimates.** Duration is derived from size and a measured rate: [[size-versus-duration]], [[story-points]], [[velocity]], [[velocity-range-forecast]].
- **An estimate is a comparison on a coarse scale.** It is made independently, by analogy, and its effort is set by the decision it feeds: [[estimation-scale]], [[triangulation]], [[independent-estimates]], [[estimating-effort-by-purpose]].
- **Order weighs four things.** They are value, cost, new knowledge and risk removed, and urgency is not among them: [[prioritization-factors]], [[combining-prioritization-factors]], [[kano-or-relative-weighting]].
- **Cut by what is delivered.** Do not cut by activity: [[story-splitting-patterns]], [[when-to-split-a-task]], [[activity-based-plan]].
- **Plan at several horizons.** Each horizon holds a different level of detail: [[planning-horizons]], [[filling-a-period]].
- **State uncertainty on whichever of date or scope is not fixed.** Protect what must hold with a buffer: [[forecast-range-and-probability]], [[velocity-range-forecast]], [[choosing-a-buffer]].
- **Only finished work counts.** Progress is read net of scope and estimate changes: [[all-or-nothing-counting]], [[unfinished-at-period-end]], [[release-progress-forces]], [[release-burndown-chart]].
- **A plan that does not change has stopped learning.** Replanning is the normal case, and a later date can be a choice: [[replanning-on-new-knowledge]], [[adding-scope-to-a-release-plan]], [[velocity-range-forecast]], [[chosen-delay-versus-slip]].

## What transfers to an agent

This wiki's reading is that the rules transfer more often than the reasons given for them. Arithmetic on size, rate and order depends on no human executor, and neither does the rule that a task counts only when finished ([[all-or-nothing-counting]]). Several reasons fall away while the rule survives on another footing ([[individual-velocity]], [[who-estimates]], [[wip-per-executor]]). Some mechanisms are human outright: [[parkinsons-law]], the calibration of the unit on [[ideal-days]], and the hours arithmetic on [[choosing-velocity-estimate-approach]] and [[iteration-capacity]]. One moves the other way, since a soft gate for people becomes a firmer one for an agent ([[tests-specified-before-start]]). Each page says which case it is. None of these transfers has been tried.

## Limits

- **Manuscript state.** Besides the acknowledgments, the reference list is unfinished, with notes such as "Tom P to send cop to me" (L6658) and "TBD: SPELLING" (L6646). So citations to third parties cannot always be followed from here, and the raw has typing errors, such as "going long than" (L6376) and "Sasah" (L6300), which quotations keep.
- **Chapter 23 is fiction.** It is "written as fiction" (L4961), so its speakers are characters and its figures are illustrations. Pages using it say so, and no outcome in it counts as evidence.
- **One voice, one setup.** Most dates here rest on a stable velocity per fixed period. The book gives no way to give a date without periods ([[commitment-over-a-period]]).
- **Internal looseness.** The source sometimes uses "velocity" for net progress (L4288, L4373), which [[velocity]] separates. Its case study also forecasts from one averaged figure where its own method asks for a range ([[velocity-range-forecast]]).

## What this wiki dropped, and why

- **Meeting scripts.** This covers the steps of planning poker (L1308-L1356) and the running of planning meetings. Only what survives without the meeting is kept ([[independent-estimates]]). The charter excludes ceremony.
- **Tracking effort expended** (L4517) as a practice. The charter excludes logged hours, and [[comparing-estimate-to-actual]] keeps only the argument.
- **Getting more time on a project** (L3708) and the personnel part of the end-of-iteration summary (L4707). These are about managing people.
- **The budget or personnel buffer** (L4031), which the source itself says is seen less on small projects ([[choosing-a-buffer]]).
- **Most of Chapter 18 as practice.** The charter excludes frameworks for scaling. A scale limit is kept ([[multi-team-techniques-scale-limit]]), along with two techniques that say when they apply ([[rolling-lookahead-plan]], [[feeding-buffer]]).
- **Build results as a metric** (L4727). This is about tooling and not about a board.
- **The narrative of Chapter 23.** Only its decisions and arithmetic are kept.

## Extraction caveat

- The raw's `structure` map stops inside Chapter 21 (L310). Chapters 22 and 23 are in the body and are not listed there.
- Figures survive only as picture text (for example L6425), so charts are known from the prose around them. Tables mostly survive.

## How to read it

Trust the structure: separate size from duration, read rates from what was finished, say how unsure a forecast is, and revise it as facts arrive. Read each number as an example from a human team, and check the reason behind each rule before assuming that it survives an agent. Where a page rests only on this book, it rests on one practitioner's judgement, and the size of that dependence is recorded on [[synthesis]].
