---
title: Push Delays Defect Discovery
category: moving-work
summary: Pushing large batches or starting too much hides defects inside incomplete work, so they surface late; a pull system exposes them earlier.
tags: [failure-mode, quality, pull, batch-size, wip]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Push Delays Defect Discovery

Push delaying defect discovery is the defect where work is started in large amounts, so faults sit undetected inside items that are not yet finished. The Siemens HS chapter contrasts this with a pull system ([[siemens-hs-case]]).

> “pushing” a large batch of requirements and/or starting too many requirements will delay discovery of defects and other issues; as defects are hidden in incomplete requirements and code.
>
> — [[vacanti-actionable-agile-metrics]], L4170

The source credits managing queues, limiting WIP and batch size, and building a cadence through pull with the opposite effect: "we were able to expose more defects and execute more timely resolutions" (L4170). It also reports continued clean builds, stable testing environments and "the clearing of previously persistent testing bottlenecks" (L4192-L4198).

## Observable signs

- The gap between defects created and defects resolved widens during a release; the source reports that gap narrowing under Kanban (L4170).
- Defects cluster late, near the end of the release. This sign is this wiki's reading of the mechanism.
- Low first pass yield, "the percentage of formal integration and regression tests passing the first time they are executed" (L4200).
- Testing is rushed at period end (L4026); see [[end-of-period-crunch]].

Each sign raises a question ([[smell-is-not-a-finding]]).

## Numbers and their conditions

First pass yield went from 75% before Kanban to 86% and then 95% (L4200), in a regulated product with a dedicated test role in each team (L4002, L4014). The chapter does not isolate WIP as the cause. It states that "Along with the gains we achieved through managing WIP; we had placed significant focus on reinforcing and improving our CI and quality management practices." (L4262). This wiki therefore keeps the mechanism, late feedback on unfinished work, and treats the percentages as one confounded result; the charter grades a practitioner source on mechanisms for this reason.

## Trade-offs

This wiki reads the cost as more frequent integration and test runs, which Siemens could afford because CI and TDD were already in place (L4006-L4012). The source does not say how far the effect holds without them.

## Agent executor note

The mechanism rests on when verification happens and not on human memory, so in this wiki's reading it survives an agent executing. Several unfinished agent results waiting for one person's review are the same hidden stock. See [[hidden-wip-in-large-items]] and [[multitasking]].
