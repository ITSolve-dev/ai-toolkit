---
title: Wrap values passed between transformations
category: errors
summary: "A fallible routine returns a bare value and signals an expected failure by null, -1 or an empty string, so its declared result hides that it can fail; or the reverse, a result type used in place of exceptions: a catch-all turning any exception into a failure value, a failure holding a caught exception or stack trace, a failure type listing every way an I/O call can fail."
tags: [rule, error-handling, result-type, pipeline, transformation]
paradigm: any
sources: [pragmatic-programmer, elegant-objects, railway-oriented-programming, against-railway-oriented-programming]
created: 2026-11-01
updated: 2026-11-07
---

In a chain of transformations, a stage that can fail must say so in the value it returns. The book raises this as the obvious objection to linear chains: if code is only a straight chain, where does the conditional logic for checking errors go? Its answer is a convention common to every approach: a wrapper type holding the value and a way to tell whether it is good (p. 194).

## Rule

«значения ни в коем случае нельзя передавать от одного преобразования к другому в исходном виде» (p. 194). Instead, wrap each value in a structure or type where its validity can be checked. The book names the wrappers Maybe in Haskell and Option in F# and Scala, and uses a tagged success-or-error pair in Elixir (pp. 194-195). The wrapper carries either the value or a reason for failure.

Wlaschin reaches the same wrapper from the shape of a function: «A function can only have one output, so we must use the `Result` type», with a success case and a failure case ([[railway-oriented-programming]]). His later post bounds what goes in it. A result type is «a glorified boolean with extra information. It’s only for *expected* control-flow, not for unexpected situations.» He sorts errors into three classes: domain errors, expected as part of the business process, which belong in the result; panics, which leave the system in an unknown state («out of memory», «divide by zero», «null reference») and are handled by abandoning the work and raising an exception caught at the highest appropriate level; and infrastructure errors such as a network timeout, which are sometimes modelled and sometimes treated as panics ([[against-railway-oriented-programming]]).

**The test that selects the wrapper:** whether the caller is meant to handle this failure as part of its normal work. If it is, the failure goes in the result. If only the top of the program will deal with it, it stays an exception. This wiki distils the test from the post's three classes and its list of reasons; the post words it through the domain.

## Sign in code

The book states the convention but not its violation. This wiki reads the sign as any of these:

- A fallible routine returns a bare value and signals failure in-band: null, -1, an empty string or a false. This page owns that shape where the failure can occur in a correct program. Where only a bug can produce it, the shape belongs to [[crash-early]]. Where the project carries failures as values (a result or option type), [[wrap-values-between-transformations]] owns a sentinel or marker returned for a failure; where it carries them as exceptions, [[recover-only-at-entry-points]] owns a sentinel returned from a catch; a null or marker returned for an absence, rather than a failure, is [[never-return-null]]. [[hybrid-coupling]] owns a value stored in a variable or field and read elsewhere, whose ranges encode different meanings.
- A stage's declared return type or documented result gives no way to represent failure, while its body has a path on which the work cannot be done.
- An error reason is lost where the code that follows needs it: that code reports or branches on why, and the stage reports only that something failed. Where no code in view reads the reason, an option is enough (see the limits).

A stage that cannot fail but returns success(...) on every path only to fit a chain is [[handle-errors-in-stages-or-in-the-pipeline]], whose repair lifts it at the chain with map; [[wrap-values-between-transformations]] owns a stage that can fail and returns no wrapper.

The reverse shape, a result type used where an exception belongs, is also this page's, after [[against-railway-oriented-programming]]:

- A catch-all below an entry point turns any exception into a failure value, typically failure(exception.message). The post: «Don’t reinvent “try-catch”!», and «No matter how many exceptions you convert into `Result`s, some will always leak out.»
- A failure case holds a caught exception, a stack trace or the location of the error. The post: «don’t use `Result` as a substitute for exceptions but then store a stack trace or a whole exception inside a `Result`. What’s the point?»
- A failure type lists every way an I/O call can fail (not found, no directory, not accessible, path too long, other), while the code in view handles them all alike. The post: «only model the bare minimum that you need for your domain, and let all the other errors become exceptions.»

A catch that turns an exception into a failure value of a result type, rather than into a sentinel or a default, is [[wrap-values-between-transformations]], which decides whether that failure belongs in the result at all.

A check repeated between stages is not closed by wrapping alone: that shape belongs to [[handle-errors-in-stages-or-in-the-pipeline]]. A null for nothing found on a routine returning a collection is [[strict-accept-narrow-promise]], unless the caller in view cannot go on with an empty result, which is this page.

## When not to apply

The book says the details depend on the language (p. 194). This wiki's own limits follow, and it does not transfer the rule to any language: how failure is carried in a given project is decided at work time from that project's conventions.

- Where a project signals failure by another established mechanism, such as exceptions, adding wrappers in one corner makes two conventions in one codebase. There, the repair of an in-band sentinel for a failure is to throw a named exception in its place.
- A stage that cannot fail needs no wrapper of its own: Wlaschin's `map` lifts such a stage at the chain instead ([[railway-oriented-programming]]). The exception, in the words [[handle-errors-in-stages-or-in-the-pipeline]] uses: a stage that cannot fail is called from code outside any chain too, and the project's convention is that every routine of the module returns the wrapper.
- *Elegant Objects* rejects Optional-style wrappers as an envelope foreign to object thinking (pp. 209-210 of [[elegant-objects]]). This wiki resolves that per setting as [[never-return-null]] does: where the convention is a checked optional type, follow it and name the method for what it returns.
- A failure that means a bug and not an expected condition should not be carried along as data for later stages to pass on. See [[crash-early]] and [[assertion-or-error-handling]]. *Against Railway-Oriented Programming* puts panics in the same place: abandon the work and raise, and catch at the highest appropriate level, such as the main function.

The limits below are from [[against-railway-oriented-programming]], each named in its closing list of reasons.

- **Fail fast.** «If something does go wrong, and you can’t continue, don’t return a `Result` and keep going.» The same operation can fall on either side, which the post settles by setting: a word processor that cannot open the file a user chose expects that and handles it gracefully, so a result fits; a program that cannot open the config file it depends on «should just fail fast». And: «If the end of your workflow will throw an exception anyway, don’t use `Result` inside the workflow.»
- **Diagnostics.** «If you care about stack traces or the location of an error, don’t use `Result`.»
- **I/O.** Do not model every possible I/O failure in the result; model the minimum the callers handle and let the rest be exceptions.
- **Apathy.** «Don’t return a `Result` if no one cares about the errors.» Where the callers only want the value and not why it is missing, the post returns an option instead; this wiki reads that as the form for an absence, chosen on [[null-object-or-optional]].
- **Performance.** In code known to be performance-sensitive, be wary of a result type, but measure to find the hot spots rather than guess ([[premature-code-tuning]]). The post calls this «more of a “be careful” than an absolute prohibition».
- **Interop.** At an interface whose callers do not use such types, return failure in the form idiomatic for them: «Don’t force the caller to become an expert in functional idioms just so they can call your API.» The post allows even null on occasion; where the callers' convention forbids it, [[never-return-null]] holds.

The 2013 article wraps a database update in an adapter that turns any exception into a failure ([[railway-oriented-programming]]); its author's 2019 post rejects converting exceptions wholesale. This wiki resolves the two by setting, with the test above: convert an exception into a failure only where the caller is meant to handle that failure, such as a record already taken that the caller reports to its user; otherwise let it travel to an entry point ([[recover-only-at-entry-points]]).

## Repair

1. Choose the representation first (p. 194). Prefer the one the language or project already uses.
2. Make each fallible stage return that wrapper, with a reason on the failure side.
3. Turn in-band sentinels into explicit failures. This wiki generalises that step from the book's single example, a search stage that converts an empty match list into an error with a reason (pp. 195-196). The book makes that choice without discussing it. This wiki treats empty as a failure where the caller in view cannot go on with an empty result.
4. Decide where the check lives: [[handle-errors-in-stages-or-in-the-pipeline]].

For the reverse shape:

1. Keep in the failure type only the cases the callers handle; let the rest propagate as exceptions to an entry point ([[recover-only-at-entry-points]]).
2. Replace a catch-all that converts any exception with a check or a catch of the named, expected case, or with nothing.
3. Where a failure holds an exception or a stack trace for diagnostics, throw instead, so the diagnostics reach the handler at the top.
4. Where no caller reads the reason, return an option.

## Before and after

```
function first_port(service_description):   -- the caller falls back to a default port
    lines = lines_with(service_description, "port")
    if lines is empty: return -1
    port = to_number(value_after(first(lines), "="))
    if port == null: return -1
    return port
```

```
function first_port(service_description):   -- the caller falls back to a default port
    lines = lines_with(service_description, "port")
    if lines is empty: return failure("no port line")
    return to_number(value_after(first(lines), "="))   -- success(port) or failure(reason)
```

In the second form `to_number` has been changed the same way: it returns success(port) or failure(reason) instead of null. The checks are still explicit in the second form. Moving them out of the sequence is the next step, in [[handle-errors-in-stages-or-in-the-pipeline]].

The reverse shape, where a user's email may already be registered and the caller reports that, while a lost database connection is nobody's business but the top of the program:

```
function save_user(user):
    try:
        db.insert(user)
        return success(user)
    catch any failure as problem:
        return failure(problem.message)
```

```
function save_user(user):
    try:
        db.insert(user)
    catch DuplicateKey on email:
        return failure(EMAIL_TAKEN)
    return success(user)      -- other failures propagate to the entry point
```

The after catches the named case at the insert rather than checking for the email first: a check before the insert leaves a window in which a concurrent insert takes the email, and its failure would then reach the top as an unexpected one. The callee is a driver the project does not own, which is the limit of [[exceptions-for-the-exceptional]] that lets this catch stand.

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 30, pp. 194-196. The rule and the first repair step are the book's; the third step generalises the book's single example and is this wiki's own. Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018, [[elegant-objects]], pp. 209-210, for the rejection of Optional-style wrappers. Wlaschin, "Railway oriented programming", fsharpforfunandprofit.com, 2013, [[railway-oriented-programming]]: the one-output argument, `map` and the catching adapter. Wlaschin, "Against Railway-Oriented Programming", fsharpforfunandprofit.com, 2019, [[against-railway-oriented-programming]]: the expected-only reading, the three classes of error, the quotations under the reverse signs, and the limits on fail fast, diagnostics, I/O, apathy, performance and interop, with the word-processor and config-file settings. The signs as worded, the test that selects the wrapper (distilled from the post), the reading of the option as the form for an absence, the per-setting resolution between the two posts, the repair of the reverse shape, the throw that replaces a sentinel under an exceptions convention, the race argument for catching the named case at the insert, the assignment against [[strict-accept-narrow-promise]], the remark that the empty-result choice goes undiscussed and the test for that choice are this wiki's own, as is the pseudocode. Related: [[programs-transform-data]].
