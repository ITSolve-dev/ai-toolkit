---
title: Test window into running code
category: debugging
summary: "A long-running component writes a counter or status field that no accessor, endpoint or log line reads, or a comment says to attach a debugger to see it, so nothing outside the process can read its state."
tags: [rule, debugging, logging, observability]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Even the best test suite misses bugs that only production conditions reveal. A test window is a deliberate way to see a module's internal state in a running system, where a debugger is awkward or impossible.

## Rule

The book's option is to provide views of a module's internal state that need no debugger (p. 273). It offers two mechanisms. Trace messages in log files should have a precise, consistent format, since they may need automatic analysis to find processing times or the logic paths taken. Badly or inconsistently formatted diagnostics are hard to read and useless to parse (p. 273). See [[trace-statements]] for the format. The second mechanism is a hot-key sequence or a magic URL that opens a diagnostic view with status messages, and more generally a feature switch that enables extra diagnostics for one user or a class of users (pp. 273-274).

## Sign in code

- A long-running component updates a counter or status field in memory, and no accessor, endpoint or log line reads it. For a field that is not private this needs a search of its readers, and this wiki gives no verdict without one.
- A comment tells the reader to attach a debugger to see a running component's state.

This wiki assigns the two neighbouring shapes by whether a line exists. This page owns state that no line or view exposes at all. Lines that exist in a form no tool can read belong to [[trace-statements]].

## When not to apply

- A short-lived script or a batch job that fails loudly at the point of failure needs no window. This limit is this wiki's own.
- State nobody needs during diagnosis needs no window. This wiki does not count a private working variable as a violation merely because nothing outside reads it. This limit is this wiki's own.
- A window is itself attack surface. The book requires that any test window be protected from prying eyes (p. 286); see [[do-not-disclose-in-output]]. This wiki reads a window without an access check as a violation of that rule, not an application of this one.

## Repair

1. Expose the state through one of the book's mechanisms: a trace message, or a diagnostic view (p. 273).
2. Guard the view, and switch it on per user where the system supports it (p. 274).
3. Delete a comment that sent the reader to a debugger.

## Before and after

Before: the count exists, and only a debugger can reach it.

```
class Worker
    field retries
    field queue

    method on_failure(job):
        retries = retries + 1    // attach a debugger to see this
        requeue(job)
```

After:

```
class Worker
    field retries
    field queue

    method on_failure(job):
        retries = retries + 1
        trace("worker.retry", job = job.id, retries = retries)
        requeue(job)

    method status():
        return { retries = retries, queued = length(queue) }

route "/diagnostics/worker" guarded by support_role:
    return worker.status()
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 273-274, 286. This wiki's own: the signs and their assignment against [[trace-statements]], the first two limits, the reading of a window without an access check, repair step 3 and the pseudocode.
