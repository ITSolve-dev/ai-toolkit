---
title: Over-configuration
category: complexity
summary: "Every new field bringing a config key plus admin code to store and edit it; an option switching between rival behaviours of one feature; keys holding the same value in every environment and set by nobody outside the code."
tags: [rule, configuration, accidental-complexity, yagni]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Configuration has a cost per setting, and past some point it makes a system slower to change than the code it replaced. The book's warning corrects its own first edition, which recommended configuration over code without enough precision (p. 211). It is the limit on [[parameterize-with-external-configuration]], and this wiki treats it as a special case of [[know-when-to-stop]].

## Rule

«Не переусердствуйте» (p. 211). The book's case is a client who decided every field in the application should be configurable. The smallest changes took weeks, because each needed the field plus all the administrative code to save and edit its contents. The application reached up to «40 тысяч переменных конфигурации» (p. 211), which the book calls a nightmare for developers.

The second caution is about motive: «Не принимайте решения относительно конфигурирования из лени» (p. 211). When there is a real debate about how a feature should work, and whether users should choose, build one option and get feedback on it (p. 211).

## Sign in code

This wiki reads the sign as any of these:

- Adding one field requires a matching configuration key plus administrative code to store and edit it.
- An option selects between two implementations of the same feature, with both paths kept in code.
- A configuration key holds the same value in every environment file in the repository.
- A key is read with a default and is set in no configuration file in the repository.

Whether a setting is ever changed in production, and who sets it, cannot be seen in the code. Deciding that needs the deployed values or their change history, and this page asks for them instead of guessing.

This wiki assigns the neighbouring case as follows. A configuration key read once at load that holds one value everywhere is [[over-configuration]]; the same value re-read at object creation or on each call or redraw is [[binding-time]].

## When not to apply

The book gives none directly, though its base rule covers values that differ across environments and clients (p. 208). These limits are this wiki's own.

- The value is set from outside the code, such as a tax rate. One value everywhere then shows only that it has not changed yet, and [[parameterize-with-external-configuration]] keeps it a key.
- Configurability is the product: a platform whose customers define their own fields, or a system that differs by contract per client.
- A setting exists to allow a change without a redeploy during an incident or a rollout. Its value is the ability to change it, not how often it does.
- Removing a key from a released product breaks those who set it, so the removal itself has a cost.

## Repair

1. For a key with one value everywhere and nobody outside the code who sets it, replace it with a named constant in code and delete the key along with its administrative code.
2. For an option standing in for an undecided question, choose one behaviour, ship it and get feedback (p. 211). This wiki adds: then delete the other path.
3. For a field made configurable by policy, ask who changes it and why. If nobody does, treat it as in step 1.

## Before and after

```
settings:
    invoice_title_label: "Invoice"
    use_new_rounding: false

function total(lines, settings):
    if settings.use_new_rounding:
        return round_half_even(sum(lines))
    return round_half_up(sum(lines))

function heading(settings):
    return settings.invoice_title_label
```

```
INVOICE_TITLE = "Invoice"

function total(lines):
    return round_half_up(sum(lines))

function heading():
    return INVOICE_TITLE
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 32, p. 211, with p. 208 for the base rule. The rule, the client's case and the advice to try one option are the book's. The signs, the limits, the link to [[know-when-to-stop]], repair steps 1 and 3 and the deletion in step 2 are this wiki's own, as are the assignment against [[binding-time]] and the pseudocode.
