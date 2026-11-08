---
title: Against Railway-Oriented Programming (Wlaschin, 2019)
category: errors
summary: "Source page, no rules of its own: the author's own critique of his 2013 article, listing when not to return a result type (diagnostics needed, reinventing try/catch, fail fast, private control flow, nobody cares about the reason, I/O, performance, interop) and splitting errors into domain errors, panics and infrastructure errors."
tags: [summary, errors, result-type, exceptions, against-railway-oriented-programming]
sources: [against-railway-oriented-programming]
created: 2026-11-07
updated: 2026-11-07
---

Scott Wlaschin's "Against Railway-Oriented Programming" (fsharpforfunandprofit.com, 2019) returns to his own [[railway-oriented-programming]] six and a half years on. He still thinks the analogy good, but says it is «often used thoughtlessly», so the post lists reasons «why you shouldn’t use the `Result` type everywhere (because ROP is just the plumbing that is used to connect `Result`-returning functions)».

## Edition and authority

Read in English from the web page at https://fsharpforfunandprofit.com/posts/against-railway-oriented-programming/, retrieved 2026-11-07. Citations name the post and the reason in its closing list. The post is short and argued from examples (a tree traversal, a file read, a config file, an event-sourcing command), not from measurement. Its weight is that the advocate of the technique states its limits himself.

## Thesis

- A result type is «a glorified boolean with extra information. It’s only for *expected* control-flow, not for unexpected situations.»
- Eight reasons not to use it, in the post's closing list: diagnostics (a stack trace or the location of an error), reinventing try/catch, fail fast, local exceptions for private control flow, apathy (nobody cares about the reason), I/O, performance, interop.
- Three classes of error: **domain errors**, expected in the business process and modelled in the result; **panics**, which leave the system in an unknown state (out of memory, divide by zero, a null reference) and are best handled by abandoning the workflow and raising an exception caught and logged at the highest appropriate level; **infrastructure errors** (a network timeout, an authentication failure), sometimes modelled and sometimes treated as panics.
- «No matter how many exceptions you convert into `Result`s, some will always leak out. You will always need to handle exceptions appropriately in the highest parts of the system.»

## Scope and limitations

- Kept: every reason except the event-sourcing example, which concerns one architectural style's signature. The microservice remark (exceptions are fine inside a few hundred opaque lines if they do not escape the service boundary) is architecture and was dropped; the same condition at the scale of a module is kept on [[exceptions-for-the-exceptional]].
- The post says the result type is «a tool for domain modeling». Modelling a business domain is outside this base; this wiki keeps only the code-level consequence, which failures a routine's result carries.
- The post links to Microsoft's F# style guide and to a blog post as further advice; neither was read.

## Key takeaways

This wiki reads the post as limits, recorded on the pages that own the shapes:

1. **A result carries only the failures its caller is meant to handle.** Unexpected failures, failures the program cannot continue after, I/O failures nobody models, and failures whose diagnostics matter stay exceptions; a reason nobody reads becomes an option: [[wrap-values-between-transformations]].
2. **Exceptions are caught at the top.** It agrees with [[recover-only-at-entry-points]] and with [[crash-early]] for panics.
3. **A private exception may be cleaner than threading a result through complex private control flow.** A per-setting limit on [[exceptions-for-the-exceptional]].

## Where it disagrees with the other sources

- With its 2013 predecessor, over wrapping every exception into a failure: resolved per setting on [[wrap-values-between-transformations]].
- With *Code Complete* on exceptions for control flow ([[code-complete]], p. 194): resolved per setting on [[exceptions-for-the-exceptional]].
- With *Elegant Objects* on null, which the post allows «on occasion» for callers in object-oriented languages: [[wrap-values-between-transformations]] defers to the callers' convention and to [[never-return-null]].

## Source

Wlaschin, "Against Railway-Oriented Programming", fsharpforfunandprofit.com, 2019, https://fsharpforfunandprofit.com/posts/against-railway-oriented-programming/. Reader comments were not fetched. The assignment of the reasons to pages and the resolutions are this wiki's own.
