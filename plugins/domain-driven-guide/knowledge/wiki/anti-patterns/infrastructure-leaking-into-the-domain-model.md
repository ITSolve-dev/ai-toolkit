---
title: Infrastructure Leaking Into the Domain Model
category: anti-patterns
summary: The failure mode where side-effect / infrastructure code (sending email, calling external services) gets dumped into the web controller, the domain model, or the service layer, tangling orchestration concerns with domain rules and violating the single-responsibility and dependency-inversion principles.
tags: [anti-pattern, domain-model, single-responsibility-principle, dependency-inversion, domain-event, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Infrastructure Leaking Into the Domain Model

A recurring failure mode: a mundane cross-cutting requirement (send an email when we run out of stock) has *nothing to do with the core domain*, yet has no obvious home, so it gets dumped somewhere it doesn't belong — the web controller, the domain model, or the [[application-service|service layer]]. The book calls this unwelcome side-effect code **goop**, and walks through three wrong homes before fixing it with [[domain-event|domain events]].

> "it's not the obvious features that make a mess of our codebases: it's the goop around the edge. It's reporting, and permissions, and workflows that touch a zillion objects." (raw L3752)

## The three tempting-but-wrong homes

1. **In the web controller.** Wrapping the `allocate` endpoint in a `try/except` that calls `send_mail`. "As a one-off hack, this *might* be OK... but it's easy to see how we can quickly end up in a mess. Sending email isn't the job of our HTTP layer, and we'd like to be able to unit test this new feature." (raw L3777..3799)
2. **In the domain model.** Calling `email.send_mail(...)` from inside `Model.allocate()` — described as *even worse*: "We don't want our model to have any dependencies on infrastructure concerns like `email.send_mail`." (raw L3813..3814) The model should stay focused on the rule "You can't allocate more stuff than is actually available." (raw L3817..3818)
3. **In the service layer.** Catching `OutOfStock` and re-raising after sending mail. "Catching an exception and reraising it? It could be worse, but it's definitely making us unhappy." (raw L3843)

## Why every home feels wrong: it's an SRP violation

> "Really, this is a violation of the *single responsibility principle* (SRP). Our use case is allocation. Our endpoint, service function, and domain methods are all called `allocate`, not `allocate_and_send_mail_if_out_of_stock`." (raw L3846..3851)

The diagnostic smell:

> "Rule of thumb: if you can't describe what your function does without using words like 'then' or 'and,' you might be violating the SRP." (raw L3851)

And the underlying reason it matters:

> "each class should have only a single reason to change. When we switch from email to SMS, we shouldn't have to update our `allocate()` function, because that's clearly a separate responsibility." (raw L3853..3855)

The requirement "try to allocate, and send an email if it fails" is really **workflow orchestration** — a sequence of steps — that has been tangled into the allocation rule (raw L3821).

## The fix: dependency inversion + domain events

Apply the *dependency inversion principle* to notifications so the [[application-service|service layer]] depends on an abstraction, not on email infrastructure — the same move used to avoid depending on the database via the [[unit-of-work]] (raw L3864). Concretely: the model records a [[domain-event]] (`OutOfStock`) instead of calling infrastructure, and a handler on the [[message-bus]] owns the email side effect. This lets you turn the notification on/off or switch email → SMS without changing the domain model or the `allocate()` use case.

## Symptoms that reveal this anti-pattern

- A domain method or entity imports an infrastructure module (`email`, an HTTP client, an ORM session for unrelated work).
- A function name would need an *and* / *then* to describe it honestly (`allocate_and_send_mail_if_out_of_stock`).
- Adding a notification channel (SMS) forces edits to core domain or use-case functions.
- Exceptions used to signal a normal domain outcome (using `OutOfStock` for control flow), which the book flags as a related smell to retire alongside this cleanup.

Contrast with the related failure mode of a model with *no* behavior at all — see [[anemic-domain-model]]. Here the model has the right behavior but is polluted with the wrong dependencies.

See also: [[domain-event]], [[message-bus]], [[application-service|service layer]], [[unit-of-work]], [[anemic-domain-model]], [[dependency-inversion-principle]], [[decoupling-domain-logic-from-infrastructure]].
