---
title: Do not disclose through output
category: errors
summary: "A stack trace reaches a user-facing response, an error reveals another account's state, a full identifier is returned or a diagnostic route has no access check."
tags: [rule, errors, security, error-messages, defensive-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

This wiki reads what a program says as much an access point as what it accepts: error messages, exception output and debug views can hand an attacker the facts needed for the next step.

## Rule

«Не разглашайте секретные данные.» (p. 286). The book's possibly apocryphal story is a system that reported that a password was in use by another user. Ensure the data reported is fit for that user's authorization, and truncate or hide risky details such as social security or other identification numbers (p. 286). Debug information falls under the same rule: a stack trace on a public terminal or a failing web page helps intruders too, so any test window and any runtime exception message must be protected from prying eyes (p. 286).

## Sign in code

- An exception's text or stack trace is written into a response to the caller.
- An error message distinguishes states the caller has no right to know, such as a fact about another account.
- A full identifier or card number is returned where a masked form would do, or is written to a log read by people with no right to it.
- A diagnostic route or status view has no authentication or authorization check.

This wiki assigns the neighbouring case as follows. Where the message carries an exception's text, a stack trace or data the user may not see, [[do-not-disclose-in-output]] owns it; [[defensive-code-in-production]] owns the tone and audience of a message that discloses nothing.

## When not to apply

The rule concerns the audience. This wiki's reading is that detail stays welcome in logs and views restricted to people authorized to see it, and that stripping it there only damages diagnosis, which [[test-window]] exists to serve. This wiki still keeps a card number or a secret inside exception text out of the log. A production assertion's report follows the same audience rule: see [[leave-assertions-on]].

## Repair

1. Log the full exception on the server side, under a correlation identifier, with sensitive fields masked.
2. Return a generic message that carries only that identifier.
3. Mask sensitive fields at the output boundary.
4. Put an access check in front of every diagnostic view.

## Before and after

Before: the caller receives the internals.

```
on error e:
    respond(500, body = e.message + e.stack_trace)
```

After:

```
on error e:
    id = new_correlation_id()
    log_error(id, e)
    respond(500, body = "Request failed, reference " + id)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 286. This wiki's own: the opening, the signs, the split with [[defensive-code-in-production]], the limit, the repair steps and the pseudocode. Related: [[attack-surface]].
