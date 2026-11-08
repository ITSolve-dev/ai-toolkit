---
title: Code inspection
category: testing
summary: "Procedure for reviewing code by reading it against a one-page checklist of known defect types, detecting rather than fixing; catches unclear error messages, misleading comments, hard-coded values and duplication that no test exposes."
tags: [method, review, inspection, checklist, defect-detection, code-reading]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Code inspection** is the procedure of finding defects in code by reading it, guided by a checklist of the defect types that have caused trouble before, with the goal of *detecting* defects rather than repairing them. McConnell (ch. 21, pp. 471-489) presents it as the most effective of the collaborative techniques and as a complement to testing, not a replacement for it. This page keeps only what changes how a reader, human or agent, goes through a piece of code; the chapter's meeting logistics, roles, management attendance and team culture are out of this wiki's scope.

## Why reading finds what tests do not

The book's figures put average defect detection at about 30% for unit testing and 35% for integration testing, against 55% for design inspections and 60% for code inspections (p. 472, citing Jones 1996); a single inspection typically finds about 60% of defects (p. 478). These are 1990s figures, and this wiki records them as the reason for the method, not as a promise. See [[defect-detection-techniques-are-complementary]].

The stronger point for this wiki is that reading and testing find **different kinds** of defects (p. 473). McConnell quotes Wiegers: a reviewer can notice «неясные сообщения об ошибках, неадекватные комментарии, жестко закодированные значения переменных и повторяющиеся фрагменты кода, которые следует объединить. При тестировании все это невозможно» (p. 473). This wiki maps each of those to its page: error messages to [[exception-message-carries-context]], comments to [[comment-why-not-how]], hard-coded values to [[named-constants-over-literals]], duplication to [[dry]]. The book's conclusion is that a quality programme needs both reviews and tests (p. 489).

Why a green suite leaves this work undone is owned by [[defect-detection-techniques-are-complementary]]; this wiki aims the review at the categories above.

## The procedure, as it applies to one reader

1. **Work from a checklist of defect types, not from a general impression.** The book says checklists focus inspectors on areas that have caused problems before (p. 477). The checklist is kept to one page, because longer ones cannot be used at the level of detail an inspection needs (p. 482). It evolves: add a defect type when it starts recurring, remove one when it stops (p. 482).
2. **Detect, do not fix.** The aim of an inspection is «обнаружение, а не исправление дефектов» (p. 477). Discussion of a found defect stops once it is agreed to be one; its type and severity are recorded and the reading goes on (p. 480). Solutions are discussed afterwards (p. 481).
3. **Read every branch.** The code is walked through with an explanation of all its logic, including every branch of every logical structure (p. 480).
4. **Read from an assigned angle or scenario.** Some organisations found more defects when each inspector read from one perspective (the maintainer, the customer, the designer) than in general reviews; the book calls the evidence incomplete (p. 480). A scenario can be a concrete question, such as whether there is a requirement this design does not meet, or a task, such as listing the requirements the code does satisfy (p. 480).
5. **Keep to a pace.** Too slow loses concentration, too fast misses defects (p. 480). The book's reference rates: about 500 lines/hour for application code and 125 lines/hour for system code during preparation (Humphrey 1989, p. 480); 150-200 non-blank, non-comment lines/hour as a starting rate at a meeting (Wiegers 2002, p. 481). Sessions longer than about two hours lose concentration (p. 481).
6. **Record type and severity of each defect,** and feed the record back into the checklist and the pace (pp. 481-482).

This wiki's transfer to an agent reviewing code: the plugin's per-group `inspector` is a perspective-based reader in the book's sense, one angle per reader, each with its own checklist (the group's pages). The book's pacing figures are human reading rates and do not transfer. This wiki reads the warning behind them as transferring: a reader who goes through a large body of code at once misses defects, so a large diff is better split.

## Code that needs its author to explain it

In an inspection the author plays a small role, because one aim is to make sure the code «говорит сам за себя»; if the code looks unclear, the author is told to improve it (p. 478). The same reasoning makes the book wary of a preliminary overview by the author, which can push the readers into the author's reading of unclear places (pp. 479-480).

This wiki routes such a passage, one whose correctness a reviewer could not establish without an explanation from outside the code, through [[design-warning-signs]] and [[rewrite-tricky-code]]; the repair is in the code, not in the review thread.

## Treat every suspected defect as needing clarification

Some teams forbid even debating at the meeting whether a reported defect really is one, on the ground that anything in code that looks like a defect to anybody «нуждается в пояснении» (p. 481). The author decides what to do with each item after the review (p. 482). This wiki's transfer: a finding that turns out to be a false alarm still shows that the code misled a careful reader, and that is evidence for clarifying it, unless the reader simply lacked context the code cannot reasonably carry.

## Reading alone versus together

At AT&T about 90% of defects were found in preparation and only about 10% at the meeting itself (p. 487, Votta 1991). In code reading, reviewers go through the code independently, about 1000 lines a day, followed by a short meeting on the problems found, which is not strictly required; this puts more of each reviewer's time into finding problems (pp. 486-487). A NASA study found about 3.3 defects per hour by reading against 1.8 per hour by testing (p. 486, Card 1987).

## When not to apply

- The book's rates and percentages are averages from 1980s-1990s organisations, which it says depend on the environment (p. 480); it tells readers to collect their own data rather than adopt the figures (p. 480).
- An inspection is not a place to debate alternatives or who is right (p. 482); the book also warns against style disputes (p. 477). This wiki adds that style questions belong to a coding standard and to tooling, which this wiki leaves out of scope.
- Changing the procedure without measuring the effect is warned against: dropping or merging steps usually costs more than it saves (Fagan 1986, p. 482). This wiki reads that as a reason not to treat a found-nothing review as proof of clean code when the checklist or the pace was skipped.
- This wiki adds: a review that finds no defect is a valid result, and code with no finding owes no change.

## Trade-offs

Inspections of design and code take about 10-15% of a project's budget and, per the book, usually lower its total cost (p. 478). Informal walk-throughs find 20-40% of defects and are, per McConnell, much less effective than inspections (p. 485); his advice is that material not worth a formal inspection is not worth a meeting at all, and should be reviewed by reading instead (p. 485).

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 21, pp. 471-489, via [[code-complete]]: detection rates (pp. 472, 478, 485), reviews finding defects tests cannot (p. 473), checklist, detection-not-correction and roles (p. 477), code speaking for itself (pp. 478-480), perspective and scenario reading (p. 480), pacing (pp. 480-481), checklist evolution and the one-page limit (p. 482), code reading and the AT&T finding (pp. 486-487). This wiki's own: the mapping of Wiegers' list to this wiki's pages; the routing of code that needs its author to explain it to [[design-warning-signs]] and [[rewrite-tricky-code]]; the aim of a review at Wiegers' categories; the reading of a false alarm as evidence for clarification; the transfer to per-group inspectors and the advice to split a large diff; the style and no-change limits.
