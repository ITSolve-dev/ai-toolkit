---
title: Parameterize with external configuration
category: change
summary: "Hosts, ports or tax rates as literals in source; branches on environment or customer name; a rebuild needed to change such a value. A literal that grants access is keep-secrets-out-of-source."
tags: [rule, configuration, hard-coding, environments]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Values that vary by environment or customer, or that may change once the application is running, are kept outside it, so the same code adapts to where it runs (p. 208). The book states the payoff this way: configuration determines behaviour at run time, and a changed value does not need a rebuild (p. 210). It is also one of the practices the book says keep decisions reversible (p. 80): see [[reversibility]].

## Rule

«Параметризируйте свое приложение, используя внешнюю конфигурацию» (p. 208).

The book's list of what usually belongs there (p. 208):

- credentials for external services such as databases and third-party APIs
- logging levels and destinations
- ports, IP addresses, machine and cluster names
- environment-specific validation parameters
- externally set parameters such as tax rates
- site-specific formatting details
- license keys

## Sign in code

This wiki reads the sign as any of these:

- A literal of one of the kinds listed above sits in source code.
- A branch tests an environment name or a customer name, such as `if env == "prod"` or `if customer == "acme"`.
- Commented-out alternative values sit beside a literal, one for each deployment.
- A rate or threshold is a constant in code, and a name, comment or requirement in hand says it is set from outside, such as by a regulator. Without that, the code does not show where a value comes from, so report the literal and ask.

A key that already exists and holds one value everywhere belongs to [[over-configuration]]. The condition that selects between them is who sets the value: set from outside the code, or changed while the application runs, it stays configuration under this page.

This wiki assigns the credentials on the list as follows. A literal that grants access, such as a password, token, API key, license key or a connection string with credentials, is [[keep-secrets-out-of-source]], which owns that sign and its repair. This page owns every other kind of value on the list. A branch that only detects running under test is [[test-environment-matches-production]].

## When not to apply

The book warns against its own earlier advice: in the first edition it recommended configuration over code without enough precision, and any advice can be taken to an extreme (p. 211). See [[over-configuration]]. This wiki's own limits follow.

- A value that is a fact of the problem and not of the deployment, such as seconds in a minute or a limit fixed by a protocol, stays in code as a named constant.
- A value with one setting, no environment or customer that differs, and nobody outside the code who sets it is not yet configuration.
- Credentials are a special case of this rule. Moving them out of source is necessary but does not settle how they are stored, and a committed configuration file does not qualify. [[keep-secrets-out-of-source]] settles that.

## Repair

1. Move the value into a configuration store. The book notes plain text formats such as YAML and JSON are the usual choice, and a database table suits structured data the customer is likely to change, such as sales tax rates. Both can be used, split by purpose (pp. 208-209). This wiki keeps credentials out of this step: their repair is on [[keep-secrets-out-of-source]].
2. Load it at startup into a data structure (p. 209).
3. Do not make that structure global: [[configuration-behind-a-thin-api]].
4. Replace an environment or customer branch with the value or behaviour that the branch was selecting.

The book's own preference has moved on to fetching configuration from a separate service, for sharing and dynamic updates (p. 209). That is operations, outside this wiki's scope. The rule here holds in either form.

## Before and after

```
function connect():
    if env == "prod":
        return open_db("10.0.0.5", 5432)
    return open_db("localhost", 5432)

function price_with_tax(net):
    return net * 1.20
```

```
function connect(settings):
    return open_db(settings.db_host, settings.db_port)

function price_with_tax(net, settings):
    return net * (1 + settings.tax_rate)
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 32, pp. 208-211, and p. 80 for the link to reversibility. The rule, the list of values, the storage options and the first edition's caution are the book's. The signs, the splits with [[over-configuration]], [[keep-secrets-out-of-source]] and [[test-environment-matches-production]], the limits, the exclusion of credentials from repair step 1 and repair step 4 are this wiki's own. The pseudocode is this wiki's.
