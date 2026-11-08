---
title: Railway oriented programming (Wlaschin, 2013)
category: errors
summary: "Source page, no rules of its own: a web article on chaining result-returning functions (success or failure) with a small set of adapters (bind, map, tee, a catching adapter, parallel validation), whose pages here own the chained pass-through check, a stage that cannot fail wrapped only to fit a chain, and independent validations that stop at the first failure."
tags: [summary, errors, result-type, pipeline, railway-oriented-programming]
sources: [railway-oriented-programming]
created: 2026-11-07
updated: 2026-11-07
---

Scott Wlaschin's "Railway oriented programming" (fsharpforfunandprofit.com, 2013) is part of a series on building a use case as a chain of steps whose errors are shunted onto a separate track. The article shows how to connect those steps when each can fail.

## Edition and authority

Read in English from the web page at https://fsharpforfunandprofit.com/posts/recipe-part2/, retrieved 2026-11-07. A web page has no printed pages: citations name the article and its part (the adapter being described, the guidelines, the operator advice). The examples are in F#; this wiki keeps none of them and writes its own pseudocode. The article argues from one worked example (validate a request, canonicalize an email, update a database, log) and from a railway analogy, not from measurement.

The author later qualified it himself. A note at its head warns not to overuse the idea and points to [[against-railway-oriented-programming]] (2019), which limits where a result type belongs. This wiki reads the two together: the 2013 article supplies the plumbing, the 2019 post the limits, and where they pull apart the pages resolve it by setting, below.

## Thesis

- A step that can fail returns one value with two cases, success or failure; «A function can only have one output, so we must use the `Result` type». Once on the failure track, the flow «never (normally)» gets back onto the happy path and bypasses the remaining steps.
- Steps are connected by adapters, not by checks inside each step: `bind` turns a step that can fail into one that accepts a two-track input; `map` lifts a step that cannot fail; `tee` turns a step done only for its side effect into one that passes its input on; a catching adapter turns an exception into a failure; `doubleMap` takes one function per track (success and failure), for logging both.
- Independent validations can run "in parallel" with `plus`, so all failures come back at once instead of the first only.
- The failure track carries one type all the way through, since most adapters leave it alone or pass an incoming failure on.

## Scope and limitations

- Kept: the plumbing as a code shape, the lift of a step that cannot fail, parallel validation, and the advice on operators. Dropped: the F#-specific forms (currying, the `function` keyword, operator definitions), the argument from generic type signatures that «we can’t introduce bugs», which depends on a type system, and the configuration-injected identity function, which carries no rule.
- The article's catching adapter turns every exception into a failure (`ex -> Failure ex.Message`). Its own author's later post rejects that use, so this wiki does not carry it as a rule: [[wrap-values-between-transformations]] decides which failures belong in a result.
- The article presents its techniques as a recipe, not as rules, and states no sign of their violation and no limit; its one stated cost is that the guidelines «may result in code that is not particularly concise or elegant». The signs and limits on its pages are this wiki's own, marked in each `## Source`.

## Key takeaways

This wiki reads the article as making three claims that change code:

1. **The check for a failure lives in the chain, not in each step.** It joins the book's form on [[handle-errors-in-stages-or-in-the-pipeline]], with `map` for steps that cannot fail.
2. **Independent validations report every failure.** [[collect-independent-validation-failures]].
3. **A consistent model over a clever one.** Plain composition with named adapters, and unfamiliar operators only where everyone knows them or they are defined at the top of the module or function where they are used; recorded on [[handle-errors-in-stages-or-in-the-pipeline]].

## Where it disagrees with the other sources

- With its own author, 2019: the article wraps a database exception into a failure; [[against-railway-oriented-programming]] says not to model every I/O error and to let the rest be exceptions. Resolved per setting on [[wrap-values-between-transformations]].
- With *The Pragmatic Programmer*: none of substance. The book's `and_then` is this article's `bind` ([[pragmatic-programmer]], p. 197).

## Source

Wlaschin, "Railway oriented programming", fsharpforfunandprofit.com, 2013, https://fsharpforfunandprofit.com/posts/recipe-part2/. Reader comments were not fetched. The reading of the two posts together and the assignment of claims to pages are this wiki's own.
