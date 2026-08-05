---
title: Command-Query Separation (CQS)
category: read-models
summary: The rule that a method must either change state (a command) or return data (a query), but never both — the seed principle from which CQRS grows.
tags: [principle, cqs, cqrs, read-model, domain-model, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Command-Query Separation (CQS)

**Command-Query Separation** is a design principle stating that a method must be **either a command that changes state, or a query that answers a question — never both**. Cosmic Python phrases the rule as: functions "should either modify state or answer questions, but never both. This makes software easier to reason about: we should always be able to ask, 'Are the lights on?' without flicking the light switch." (raw L5498). CQS is the small, uncontroversial seed from which the larger [[cqrs]] pattern grows: "reads (queries) and writes (commands) are different, so they should be treated differently (or have their responsibilities segregated, if you will)" (raw L5420).

## Why it matters for a domain model

When a method both mutates and returns derived data, callers can no longer tell read code from write code, and the two concerns leak into each other. In a DDD codebase this matters because writes go through the rich, invariant-enforcing machinery (the [[aggregate]], the [[unit-of-work]], the [[domain-model]]) while reads want none of it. Keeping the two apart lets "you… see which code modifies state (the event handlers) and which code just retrieves read-only state (the views)" (raw L5587). The book recommends this split even for teams that never adopt full CQRS: "Splitting out your read-only views from your state-modifying command and event handlers is probably a good idea, even if you don't want to go to full-blown CQRS." (raw L5589)

## The familiar example: Post/Redirect/Get

A classic web instance of CQS is Post/Redirect/Get: an endpoint accepts a POST (the command), then redirects the browser to a separate GET (the query) to view the result, instead of returning data in the response to the write. This avoids double-submission on refresh and broken bookmarks — both symptoms of "returning data in response to a write operation" (raw L5495). The book notes the same logic applies to APIs via `201 Created` / `202 Accepted` with a `Location` header: "What's important here isn't the status code we use but the logical separation of work into a write phase and a query phase." (raw L5502)

## A CQS violation and its fix

Cosmic Python calls out its own violation: an `allocate` endpoint that performed the allocation (a command) *and* returned the resulting batch reference (a query) in one call. "That's led to some ugly design flaws so that we can get the data we need." (raw L5508). The fix is to have the write endpoint return a bare acknowledgement (a `202`) and add a **separate read-only endpoint** to retrieve allocation state — cleanly separating the write phase from the query phase.

## Relationship to CQRS

CQS is the method-level rule; [[cqrs]] (Command-Query *Responsibility Segregation*) pushes the same insight up to the architecture, potentially using entirely separate models — and even separate data stores — for reads versus writes. You can apply CQS everywhere at almost no cost; CQRS is a heavier commitment justified only when the [[read-model-projection|read model]] genuinely diverges from the write model.

## Related

[[cqrs]] · [[commands-and-events]] · [[read-model-projection]] · [[aggregate]] · [[unit-of-work]] · [[domain-model]]
