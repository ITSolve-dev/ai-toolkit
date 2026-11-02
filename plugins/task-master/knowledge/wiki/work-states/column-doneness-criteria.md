---
title: Column Doneness Criteria
category: work-states
summary: Each column states what must be true before a story leaves it, so quality steps are enforced at the move and not remembered; the last column's Done also fixes what the metrics cover.
tags: [rule, work-states, definition-of-done, policies, columns]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Column Doneness Criteria

Column doneness criteria are explicit conditions a story must satisfy before moving to the next column. They turn a board column from a label into a checkable state. In the [[siemens-hs-case]]:

> Each column had its own doneness criteria and by incorporating “doneness procedures” into our explicit policies we were able to ensure that all quality steps were followed before moving a story to the next column
>
> — [[vacanti-actionable-agile-metrics]], L4262

The source's example is the move "from “Specifying” to “Developing”" (L4262). The source is modest about the credit: "Most of these practices had predated Kanban; however the Kanban method provided more visibility and rigor." (L4262). So this wiki keeps the criteria as a rule without claiming that Kanban created them.

## Observable signs of violation

The signs are this wiki's reading, and each is a question to check.

- A column has no written exit condition.
- A story sits past a column with a required step unmet.
- Stories move backward because a step was skipped; see [[backward-movement]]. A backward move can have other causes.

## What breaks when ignored

The source's concern is that quality steps get skipped when a story moves on. This wiki adds a second consequence: time in state means nothing if nobody can say what ending a state requires, so [[judging-board-columns]] and any per-column reading lose their footing.

## The last column fixes what the metrics cover

At Siemens a feature "is declared “done” only once it has passed validation testing in a fully integrated environment" (L4014). Yet Done was not delivery: regression testing, beta testing, hosting and implementation lay outside (L4264). So Done sets the boundary of WIP, Cycle Time and Throughput ([[started-and-finished-points]]). This wiki reads the consequence plainly: a short Cycle Time measured to an early Done can coexist with long delivery. Siemens saw this and began extending Kanban across the whole value stream (L4264-L4270).

## Pairing with queue sub-states

Siemens' stream had queue states such as "developing done" alongside active work (L4184, L4192). This wiki reads the pair as follows: a doneness criterion says when a story may enter that queue, and the WIP limit of the next column says when it may leave. See [[active-versus-queued]] and [[mapping-workflow-states]]. Figure 17.1, which shows the actual board, is missing from the raw source, so the full column list cannot be read here.

## Trade-offs

Criteria add a check at every move. This wiki reads them as possibly more than a very small board needs; the source's setting is regulated healthcare software with FDA and ISO obligations (L4002).

## Agent executor note

The source relies on team discipline to apply the criteria. In this wiki's reading the rule gains value with an agent executing, because an agent does not fill gaps from unstated team habit: an exit condition that is not written down does not exist for it. See [[testable-acceptance]].
