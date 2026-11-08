---
title: Handle errors in the stages or in the pipeline
category: errors
summary: "The same pass-through check, if input is failure return it, repeated at the top of several stages or between them; each stage accepts a wrapper though it works only on the unwrapped value; or a stage that cannot fail returns success(...) on every path only to fit the chain."
tags: [decision-rule, error-handling, result-type, pipeline, bind]
paradigm: any
sources: [pragmatic-programmer, railway-oriented-programming]
created: 2026-11-01
updated: 2026-11-07
---

Once values travel in a wrapper ([[wrap-values-between-transformations]]), something must look inside it. The book gives two places: inside each transformation, or outside them, in the pipeline itself (p. 194). It prefers the second.

## Rule

**In each stage:** a stage accepts the wrapper. If it holds a success, the stage does its work. If not, it returns the wrapper unchanged, so an error anywhere becomes the chain's result (pp. 195-196). The chain itself stays clean, and later stages are skipped in effect. A footnote corrects that: later functions are in fact called, and only their code does not run (p. 195). The cost is that the burden of error handling has moved onto every stage. Even with pattern matching in function calls, the book says, «последствия подобного переноса смягчаются, но они все равно скверные» (p. 196).

**In the pipeline:** a bind function, `and_then` in the book, takes a wrapped value and a function. On success it calls the function with the unwrapped value. Otherwise it returns what it was given (p. 197). Stages then take a plain value, plus any extra parameters, and return a new wrapper. Code further down the chain no longer needs to know an error happened (p. 197).

Wlaschin's [[railway-oriented-programming]] gives the same pipeline form under the name `bind`: an adapter that takes a step that can fail and returns a function accepting the two-case input, so the step is bypassed on a failure. He adds adapters for the other kinds of step a chain meets. A step that cannot fail is lifted with `map`: on success it calls the function and wraps its output as a success, on failure it bypasses the function. A step done only for its side effect, such as a database update, is turned by `tee` into one that returns its input, so it can sit in the chain. A step that may throw is wrapped by an adapter that catches the exception and returns a failure; which exceptions belong in that failure is decided on [[wrap-values-between-transformations]]. Two consequences follow, in his words: once on the failure path «we never (normally) get back onto the happy path», and «the failure track must be *same type* all the way through».

His guidelines ask for a consistent model over a concise one: use plain composition to connect steps, `bind` to insert a step that can fail and `map` to insert one that cannot. He states the cost: they «may result in code that is not particularly concise or elegant, but on the other hand, you will be using a consistent model, and it should be understandable to other people when it needs to be maintained».

**The test:** do the stages do anything with the error, or only pass it on? If they only pass it on, put the check in the pipeline. This test is this wiki's distillation. The book argues from the burden on the stages.

## Sign in code

This wiki reads the sign of the in-stage form as:

- The same pass-through line or clause, if the input is a failure then return it, appears in two or more stages of one chain.
- A stage's parameter is the wrapper type, while all its work is done on the unwrapped value.
- A stage cannot be called or tested on a plain value without first being wrapped.
- A pass-through check on a wrapped result sits between every two stages of one function, so the chain cannot be read as a chain. This page owns that shape. [[wrap-values-between-transformations]] owns a stage that returns no wrapper at all.
- A stage that cannot fail returns success(...) on its only path, so its declared result promises a failure it never produces.

A stage that cannot fail but returns success(...) on every path only to fit a chain is [[handle-errors-in-stages-or-in-the-pipeline]], whose repair lifts it at the chain with map; [[wrap-values-between-transformations]] owns a stage that can fail and returns no wrapper.

Where the stages of a chain are independent checks of one input whose failures go back to the person who supplied it, [[collect-independent-validation-failures]] decides whether they run in series or all together; [[handle-errors-in-stages-or-in-the-pipeline]] decides where the pass-through check lives once they run in series.

## When not to apply

The book's only stated cost is extra punctuation to turn calls into function values, in a language that requires it to be explicit, and it says the simpler stages repay this (p. 197). The limits below are this wiki's own.

- A stage acts on the failure: it recovers, retries or adds context. It must see the wrapper, so that stage is not a pass-through. It should be a separate handler and not a reason to wrap all stages.
- The chain has only one or two fallible stages. A bind helper can cost more than the checks it replaces.
- The language cannot treat functions as values, because the pipeline form depends on deferring calls until the earlier stages have succeeded (p. 197).
- A stage that cannot fail is called from code outside any chain too, and the project's convention is that every routine of the module returns the wrapper. Follow the convention; the last sign does not fire there. This limit is this wiki's own.
- The language or a library already has a form of this. Use that form and do not write a new one. The book expects something similar to work in other languages (p. 194). This wiki does not transfer the Elixir form: how it applies in a project is decided at work time.

## Repair

1. Remove the failure branch from each stage and make its parameter the plain value.
2. Keep each stage returning the wrapper.
3. Write one bind function, or use the one the language provides.
4. In the chain, pass each stage to bind as a function value instead of calling it. Deferring the call is the point (p. 197).
5. A stage that cannot fail returns its plain value; lift it at the chain with a map function instead of wrapping its result inside it ([[railway-oriented-programming]]).
6. Name the helpers. Wlaschin advises a team of non-experts: «Don’t use any “strange” operators other than `>>` and `|>`», and not operators like `>>=` or `>=>` «unless everyone is aware of them»; an exception is an operator defined at the top of the module or function where it is used. This wiki reads that as: write bind and map as named functions unless the project already uses operator forms for them.

## Before and after

```
function find_lines(result, pattern):
    if result is failure: return result
    lines = matching(result.value, pattern)
    if lines is empty: return failure("no line matches " + pattern)
    return success(lines)

function shorten(result):
    if result is failure: return result
    return success(cut_to_20(result.value))

function search(path, pattern):
    return shorten(find_lines(read_file(path), pattern))
```

```
function and_then(result, next):
    if result is failure: return result
    return next(result.value)

function map_value(result, transform):
    if result is failure: return result
    return success(transform(result.value))

function find_lines(text, pattern):
    lines = matching(text, pattern)
    if lines is empty: return failure("no line matches " + pattern)
    return success(lines)

function shorten(lines):
    return cut_to_20(lines)

function search(path, pattern):
    result = read_file(path)
    result = and_then(result, text -> find_lines(text, pattern))
    return map_value(result, shorten)
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 30, pp. 194-197. The two placements, the preference and the bind function are the book's, with language specifics left out. The decision test, the signs and the limits are this wiki's own, except the limit on function values, which follows from p. 197. The pseudocode is this wiki's; the failure on no matching line follows the book's search stage (pp. 195-196).

Wlaschin, "Railway oriented programming", fsharpforfunandprofit.com, 2013, [[railway-oriented-programming]]: `bind`, `map`, `tee` and the catching adapter, the two quoted consequences, the guidelines and their cost, and the advice on operators. Reading `map` as the repair of a stage that cannot fail, the last sign, the convention limit and the reading of the operator advice as named helpers are this wiki's own. Related: [[programs-transform-data]], [[collect-independent-validation-failures]].
