---
title: Crash early
category: errors
summary: "An impossible branch logs or returns a default and carries on, a catch swallows the failure, or a failure only a bug can produce returns a sentinel such as NaN or -1 that flows onward."
tags: [rule, failure-handling, fail-fast]
paradigm: any
sources: [pragmatic-programmer, code-complete, object-oriented-thought-process, against-railway-oriented-programming]
created: 2026-11-01
updated: 2026-11-07
---

When code finds that something assumed impossible has happened, it can no longer be trusted to continue. The book's tip is «Пользуйтесь досрочным аварийным завершением программы» (p. 151).

## Rule

Check often and stop as soon as such a state is found. Code that has detected the impossible means «такой код больше не считается жизнеспособным», everything it does afterwards is suspect, and it should stop as soon as possible (p. 151). «Мертвая программа, как правило, наносит намного меньше вреда, чем испорченная.» (p. 151).

The alternative the book names is carrying on and writing corrupted data to a live database (p. 151). A failure left to travel sometimes surfaces far from its cause, in a third-party library or a switch's default arm, long after the logic error that produced it (p. 149).

*Code Complete* gives the same verdict on the empty catch: «Избегайте пустых блоков catch» (p. 196). An empty catch means either that the try block throws for no reason or that the catch fails to handle a possible exceptional situation; find which, and fix the try or the catch (p. 196). Wlaschin's *Against Railway-Oriented Programming* gives a related verdict for any failure the program cannot continue after: «If something does go wrong, and you can’t continue, don’t return a `Result` and keep going. Fail fast instead with an exception or even just exit the app immediately» ([[against-railway-oriented-programming]]; the last words are a link in the post). This wiki reads it here only for states a bug produces; a failure a correct program meets and cannot continue after (a config file the program depends on) is decided by the fail-fast limit on [[wrap-values-between-transformations]] and is caught at [[recover-only-at-entry-points]]. McConnell's spectrum from robustness to correctness limits how far stopping reaches: where the cost of a wrong result is low, the book allows substituting a value and going on (p. 192), which [[robustness-versus-correctness]] decides.

## Sign in code

- A branch for a state that should not exist logs or returns a default, and the work carries on. This page owns that shape. Where the branch is empty, nothing was checked, and the shape belongs to [[assert-the-impossible]]. This page owns it where the module's production reaction must also be a stop; where the production reaction may be polite, a reaction that differs between builds is [[offensive-programming]].
- A catch block is empty, typically around a large try block (*Code Complete*, p. 196), or catches everything and continues. A catch whose type admits a failure a correct program can meet, a catch-all included, that ends in a sentinel, a default, a fallback or only a log, is [[recover-only-at-entry-points]]; [[crash-early]] owns a catch, branch or sentinel only where the code in view shows that only a bug can produce the failure. A catch at an entry point that reports the failure and ends the request or job is not this sign: [[recover-only-at-entry-points]]. Weisfeld's *The Object-Oriented Thought Process* shows the shape: a handler catches the `ArithmeticException` of a division the code in view makes by zero, prints the message, assigns `count = 1` and continues (p. 77).
- An internal failure returns NaN, -1 or null, and callers pass it along unchecked. The book's example is NaN propagating into later arithmetic (p. 146). This page owns that shape where only a bug can produce the state, which [[assertion-or-error-handling]] decides. Where the project carries failures as values (a result or option type), [[wrap-values-between-transformations]] owns a sentinel or marker returned for a failure; where it carries them as exceptions, [[recover-only-at-entry-points]] owns a sentinel returned from a catch; a null or marker returned for an absence, rather than a failure, is [[never-return-null]]. A catch that turns an exception into a failure value of a result type, rather than into a sentinel or a default, is [[wrap-values-between-transformations]], which decides whether that failure belongs in the result at all.
- The result of closing a file or writing a trace is ignored because it cannot fail (p. 150). [[assert-the-impossible]] owns that shape, because the code has no failure path at all, which is a missing check.

This wiki assigns the neighbouring cases as follows. This page owns a failure dropped in standing code. A guard or catch that a bug-fix diff adds at the failing line, with the producer unchanged, is [[fix-the-root-cause]]. A catch-all that a diff adds against a region where errors propagate is [[first-do-no-harm]]. A dropped error with a note that this is for now is [[broken-windows]].

## When not to apply

- The failure is expected in a correct program. Handle it: see [[assertion-or-error-handling]], and for where the handling belongs, [[recover-only-at-entry-points]].
- The book allows that a plain exit may be unacceptable where resources are held, log messages must be written, open transactions cleaned up or other processes told (p. 151). The principle stays, and cleanup may run. The book's advice for a failed assertion is that the cleanup code «не опирался на информацию, послужившую причиной того, что утверждение не подтвердилось» (p. 153).
- *Code Complete* names one case where an empty catch is right: a lower-level exception that does not match the abstraction level of the calling routine. Then at least document why: «хотя бы задокументируйте, почему блок catch должен быть пустым» (p. 196), in a comment or by writing a message to a log (p. 196). This wiki reads that limit as narrow: a catch that only logs and carries on is still this page's sign whenever the failure leaves the program in a state it cannot trust, and the documented empty catch fits only where continuing is correct. Where the mismatch of abstraction is the problem, the usual repair is to translate rather than swallow: [[exception-at-the-interface-abstraction]].
- A possible error in data, as opposed to a state only a bug can produce, may be absorbed at the robustness end of the scale: [[robustness-versus-correctness]].
- This wiki adds that the unit to stop need not be the whole process. Where one process serves many independent requests, failing the request or job may be the right size.
- This wiki adds: in an interactive program where users hold unsaved work, the production reaction is decided on [[defensive-code-in-production]].

The book quotes Joe Armstrong calling defensive programming a waste of time, and a page earlier says its authors use it (pp. 150-151). This wiki resolves the two by setting: Armstrong's view holds where a supervisor owns failure, cleaning up and restarting the code (p. 151). Without a supervisor, the checks stay and a failed check stops the work.

## Repair

For an empty catch, decide which side is wrong first (*Code Complete*, p. 196): if the try region throws for no reason, remove the cause or narrow the region; if the catch should handle, handle it or let it propagate; if, rarely, ignoring is correct, say why in the catch.

Replace the continuation with an abort or exception that carries the offending values. Remove sentinels from internal failure paths. Put cleanup in one place at the top of the unit being stopped, and see [[exception-safe-release]]. A handler that only logs and rethrows is a separate case: see [[log-and-rethrow]].

## Before and after

```
# before
function apply_status(order, status):
    # status is produced only by this module; production must stop on an unknown one
    if status == PAID: mark_paid(order)
    else if status == REFUNDED: mark_refunded(order)
    else: log("unknown status")
    save(order)
```

```
# after
function apply_status(order, status):
    # status is produced only by this module
    if status == PAID: mark_paid(order)
    else if status == REFUNDED: mark_refunded(order)
    else: abort("unknown status", status, order.id)
    save(order)
```

The rare empty catch that is correct, documented as *Code Complete* asks. The fallback is stated in the routine's contract, so the after falls under the specified-degradation limit of [[recover-only-at-entry-points]]:

```
# before
try:
    ... many lines ...
    remove_temp_file(path)
catch AnyException:
    pass
```

```
# after
# contract: succeeds when the file is already absent
try:
    remove_temp_file(path)
catch FileNotFound:
    # the file is already gone, which is the state we wanted
    log_debug("temp file already removed", path)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 146, 149-151, 153. McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 196 for the empty-catch rule, its reasoning, its one exception and the decision between try and catch; p. 192 for the spectrum. Wlaschin, "Against Railway-Oriented Programming", fsharpforfunandprofit.com, 2019, [[against-railway-oriented-programming]], for the fail-fast quotation; restricting it here to states a bug produces is this wiki's own. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], p. 77: the `ArithmeticException` handler; the book shows it as a handling example, and reading it as this page's sign is this wiki's own. The narrow reading of that exception, the first three signs as worded, the assignments of neighbouring cases, the request-sized limit, the limit for unsaved user work, the resolution of the Armstrong tension, the repair apart from the empty-catch decision, and both examples are this wiki's own. Related: [[constructors-without-code]], which decides per setting whether a check in a constructor is deferred, as *Elegant Objects* asks, or kept eager.
