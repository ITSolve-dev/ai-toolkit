---
title: Do not catch only to log and rethrow
category: errors
summary: "A handler whose body only logs a message and rethrows the same exception, often repeated once per exception type."
tags: [rule, exceptions, coupling]
paradigm: any
sources: [pragmatic-programmer, elegant-objects]
created: 2026-11-01
updated: 2026-11-03
---

The book's section on this pattern contrasts a call wrapped in several handlers with the bare call (p. 150). The bare call is the version the authors prefer.

## Rule

Do not intercept an exception merely to log it and raise it again. Let it propagate (pp. 150-151).

The book gives two reasons. The application code is no longer buried under error handling. More importantly, it is less coupled: the wrapped version has to list every exception the callee can raise, so a new exception added by the callee leaves the wrapper subtly out of date, while the bare call propagates it automatically (pp. 150-151).

## Sign in code

- Each handler's body is a log line followed by a bare rethrow.
- Several handlers differ only in message text.
- A handler names exceptions of a callee and adds no information, decision or cleanup.

This wiki assigns the neighbouring cases as follows. This page owns a handler that logs and then rethrows the same exception. A catch that only logs and does not rethrow is [[recover-only-at-entry-points]], or [[crash-early]] where only a bug can produce the failure. A catch that throws a new exception is [[chain-exceptions]].

## When not to apply

The book names no exceptions; these limits are this wiki's reading of what its reasons leave open.

- This level can add something the final reader needs, such as the identifier it was working on, or the exception crosses a layer boundary. It should then wrap the exception with that context, or translate it so callers do not depend on what lies beneath, rather than log it: see [[chain-exceptions]], which resolves its book's "chain in every method" against this page by the same test. A handler that logs and then throws a wrapped exception still logs twice: delete the log line.
- It releases a resource or decides something, such as a retry. See [[exception-safe-release]].
- It sits at the top of the unit of work, where the failure is reported once.

## Repair

Delete the handler and leave the call. If the failure needs logging, log it once at the place that finally handles it. *Elegant Objects* reaches the same verdict on catching and logging, calling it «ужасный антипаттерн» (p. 217 of [[elegant-objects]]).

## Before and after

```
# before
function publish(report):
    try:
        upload(report)
    catch QuotaExceeded:
        log("quota exceeded, exiting")
        rethrow
    catch StorageOffline:
        log("storage offline, exiting")
        rethrow
```

```
# after
function publish(report):
    upload(report)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 150-151 for the rule and both reasons. The signs, the limits, the logging advice in the repair and the example are this wiki's own. Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018, [[elegant-objects]], p. 217, for catch-and-log as an anti-pattern; the quotation was checked against the page image.
