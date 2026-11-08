---
title: Collect the failures of independent validations
category: errors
summary: "Several checks of one input that do not depend on each other are chained so the first failure ends the chain (early returns, or bind between validation steps), and that one failure goes back to the person who must correct the input, who then fixes errors one round trip at a time."
tags: [rule, validation, result-type, pipeline]
paradigm: any
sources: [railway-oriented-programming]
created: 2026-11-07
updated: 2026-11-07
---

A chain of fallible steps stops at the first failure: that is what makes it a chain ([[handle-errors-in-stages-or-in-the-pipeline]]). For validation that is not always wanted. Wlaschin raises it after chaining three validations in series: «You might be wondering if there is a way to run all three validations in parallel, rather than serially, so that you can get back all the validation errors at once.» His answer is a combiner, `plus`, that applies the input to both checks, succeeds only if both succeed, and joins the two failures where both fail ([[railway-oriented-programming]]).

## Rule

Run checks that do not depend on each other against the same input, and combine their results: success only if all succeed, otherwise a failure that holds every failure found. The article's logic for a pair, which then chains to any number: «First, take the input and apply it to each switch», both successful gives success, and «If either output is a failure, then the overall result is `Failure` as well». How two failures are joined is left to the caller, because «The method of combining values might change in different contexts»; for validation messages the article concatenates them. This wiki reads the rule as the article's technique made a rule where the failures go back to whoever supplied the input; the article offers it as an option, not as a rule.

## Sign in code

This wiki reads the sign as all of these together:

- Two or more checks of one input, none of which reads a value another computed or relies on another having passed (name not blank, email not blank, age in range).
- They are joined so the first failure ends the run: an early return after each check, or bind between them.
- The single failure is what the routine returns to the submitter of the input: a form, a reply read by the person who sent the request, an import report.

Where the stages of a chain are independent checks of one input whose failures go back to the person who supplied it, [[collect-independent-validation-failures]] decides whether they run in series or all together; [[handle-errors-in-stages-or-in-the-pipeline]] decides where the pass-through check lives once they run in series.

## When not to apply

The article states no limit. The limits below are this wiki's own.

- A later check needs an earlier one to have passed: a length check on a value that may be missing, a format check on a field that may be blank, a lookup on an identifier not yet parsed. Those stay in series; only the independent ones are collected.
- The input comes from another program whose interface, by the project's convention, rejects on the first error; [[validate-exchanged-data-against-a-declared-schema]] owns how the document is checked.
- A check is expensive (a database or network call) and would run for input already known to be bad. Run the cheap independent checks together first, then the expensive one only if they pass.
- The checks are not validation but successive work on the value: a chain of transformations is meant to stop at the first failure.

## Repair

1. Separate the independent checks from those that depend on an earlier one.
2. Run every independent check on the same input and gather all failures; return success only if there are none. Use the language's or project's form for combining results where one exists.
3. Decide how failures are joined: a list of reasons rather than one concatenated string, where the caller shows them per field.
4. Keep the dependent checks after the collected group, in series.

## Before and after

```
function validate_signup(form):
    if form.name is blank: return failure("name must not be blank")
    if form.email is blank: return failure("email must not be blank")
    if form.age < 13: return failure("age must be at least 13")
    return success(form)

function handle_signup(form):
    result = validate_signup(form)
    if result is failure: return reply_with_errors([result.reason])
    return register(result.value)
```

```
function validate_signup(form):
    reasons = []
    if form.name is blank: append(reasons, "name must not be blank")
    if form.email is blank: append(reasons, "email must not be blank")
    if form.age < 13: append(reasons, "age must be at least 13")
    if reasons is empty: return success(form)
    return failure(reasons)

function handle_signup(form):
    result = validate_signup(form)
    if result is failure: return reply_with_errors(result.reasons)
    return register(result.value)
```

## Source

Wlaschin, "Railway oriented programming", fsharpforfunandprofit.com, 2013, [[railway-oriented-programming]]: the part on combining switches in parallel (`plus`, and the validation combiner modelled on a binary AND). The technique, its logic and the caller-supplied join are the article's; making it a rule for input that a person corrects, the signs, all the limits, the repair steps and the pseudocode are this wiki's own.
