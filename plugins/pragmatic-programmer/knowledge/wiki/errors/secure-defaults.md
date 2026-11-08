---
title: Secure defaults
category: errors
summary: "An option's default is its less safe value, such as verification off or debug on, so the caller has to opt in to safety."
tags: [rule, errors, security, configuration, defensive-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

This wiki's reasoning for the rule is that most values are never changed from their defaults, so the default is the setting most users actually run with.

## Rule

«Значения настроек по умолчанию приложения или веб-сайта для пользователей должны быть самыми безопасными.» (p. 287). These may not be the most convenient, but each user should then make the trade-off between safety and convenience personally. The book's example: password entry shows asterisks by default, which suits public places and large audiences, while users who need accessibility features may have to reveal the text (p. 287).

This wiki carries the rule from user-facing settings to parameter and flag defaults in code. The book speaks only of settings for users.

## Sign in code

- A boolean option for verification, encryption, or access control defaults to the off state.
- A debug or verbose flag defaults to on in code that ships.
- A permission or visibility parameter defaults to its most open value.

## When not to apply

The book states no limit beyond leaving each user the choice (p. 287). These limits are this wiki's own.

- The safest value makes the feature unusable, as a deny-all default on something that must be opened before anything works. The default is then the narrowest value that still works.
- A development-only convenience lives in a development configuration and not in the shipped default.

## Repair

Make the safe value the default, and require the less safe value to be stated explicitly at the call site or in configuration, under a name that says what is given up.

## Before and after

Before: forgetting the argument disables verification.

```
function fetch(url, verify_certificate = false):
    ...

fetch(billing_url)
```

After: the unsafe choice is visible where it is made.

```
function fetch(url, verify_certificate = true):
    ...

fetch(billing_url)
fetch(local_stub_url, verify_certificate = false)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 287. This wiki's own: the opening reasoning, the transfer from user-facing settings to parameter and flag defaults in code, the signs, the limits, the repair and the pseudocode. Related: [[attack-surface]].
