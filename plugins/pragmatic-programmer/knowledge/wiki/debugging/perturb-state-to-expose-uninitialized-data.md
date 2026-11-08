---
title: Perturbing system state to expose hidden defects
category: debugging
summary: "Procedure for a program that fails once in a hundred runs on the same input, which usually means it reads uninitialised state: fill memory with non-zero patterns, fail allocations, check bounds, so the failure happens every time."
tags: [method, intermittent-failure, uninitialized-variables, fault-injection]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Many programmers know a program that works 99 times in 100 and crashes on the hundredth run with the same data. McConnell says the cause is almost always a variable that was not initialised, and that it is hard to reproduce because 99 times in 100 the uninitialised variable happens to hold zero (p. 517). The remedy is to perturb the environment so the latent defect shows every time.

## Techniques the book lists (pp. 517-518)

- **Memory filling.** Fill memory with arbitrary values before the run, so an uninitialised variable does not luckily read 0. A specific value can be chosen to trap: on x86, 0xCC is the breakpoint instruction, so executing memory that should not be executed stops in the debugger.
- **Memory shaking.** Rearrange the program's memory between runs to expose code that depends on data sitting at absolute rather than relative addresses.
- **Selective memory failure.** A memory driver simulates shortage: it refuses a request after an arbitrary number of successes, or grants after failures. Useful for programs that allocate dynamically.
- **Bounds checking.** Watch pointer operations to find uninitialised or dangling pointers.

## Generalisation and limits

The book's tools are low-level and language-bound; their mechanics are taken at work time from the project's tooling. This wiki reads the method behind them as general: when a failure is intermittent on identical input, the varying part is state the code did not set; make that state hostile and deterministic (poison defaults, injected failures of resources the code acquires) so the failure reproduces, then find the read that precedes the write ([[variable-state-anomalies]], [[initialize-close-to-first-use]]). In languages that forbid reading uninitialised variables, this wiki expects the same shape as unset fields, stale caches or state shared between tests. Where the varying part is thread timing rather than unset state, see [[random-failures-suspect-concurrency]]. The generalisation beyond memory is this wiki's, not McConnell's.

When a failure is intermittent on identical input, [[perturb-state-to-expose-uninitialized-data]] makes it occur every time; once it occurs every time, [[stabilize-the-error]] reduces the failing test.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 517-518, via [[code-complete]]. The generalisation beyond memory, the links to neighbouring pages and the order against [[stabilize-the-error]] are this wiki's own.
