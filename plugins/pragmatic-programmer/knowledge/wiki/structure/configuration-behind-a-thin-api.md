---
title: Keep configuration behind a thin API
category: structure
summary: "A global config map read at many call sites; raw key paths, environment variable names or file format details spread outside one module."
tags: [rule, configuration, global-state, coupling, decoupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Configuration is commonly read at startup into a data structure that is then made global, so that any code can reach it. The book says this is the usual practice and advises against it (p. 209). This wiki reads the harm as [[global-data]] in its plainest form: global access to a structure ties every reader to how configuration is represented.

## Rule

«вынесите всю конфигурационную информацию в отдельный (тонкий) API» (p. 209). The purpose stated is to decouple code from the details of how its configuration is represented (p. 209).

## Sign in code

This wiki reads the sign as any of these:

- A global, singleton or module-level configuration object is read from many unrelated places.
- Call sites spell raw key paths, such as `CONFIG["db"]["primary"]["host"]`.
- Environment variable names or the configuration file format appear outside one module.

This wiki assigns the neighbouring cases as follows. This page owns knowledge of how configuration is stored, spread across sites. A function that reaches any module-level value with no parameter showing it, configuration included, is [[global-data]]. A reusable module that reads its surroundings, even at one site, is [[do-not-rely-on-unguaranteed-context]].

## When not to apply

The book gives no limit. These are this wiki's own.

- A small script with a single reader has no representation to hide. The API would only repeat the structure.
- A framework may own configuration loading and supply an accessor. That accessor already serves as the API, so another layer duplicates it.

## Repair

1. Put the loading in one module.
2. Expose named accessors that say what the value means to the caller, not where it is stored.
3. Replace raw reads at call sites with those accessors.
4. Where practical, pass values as parameters to the code that uses them, so the dependency shows in its signature.

This wiki adds a constraint on the API itself: it stays free of logic. Once it computes behaviour, it is a different module with a different reason to change.

This wiki reads one further benefit from the book's move to a configuration service (p. 209): if callers use an API and not a structure, the storage behind it can change without touching them.

The values that belong here are listed on [[parameterize-with-external-configuration]].

## Before and after

```
CONFIG = parse_yaml(read_file("app.yml"))

function send_report(report):
    host = CONFIG["mail"]["smtp"]["host"]
    port = CONFIG["mail"]["smtp"]["port"]
    deliver(host, port, report)
```

```
module settings
    function mail_server():
        data = load_once("app.yml")
        return (data.mail.smtp.host, data.mail.smtp.port)

function send_report(report, server):
    deliver(server, report)

send_report(report, settings.mail_server())
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 32, p. 209. The rule and its purpose are the book's. The reading of the harm, the signs, the assignment of neighbouring cases, the limits, the repair steps, the constraint on the API and the note on swapping storage are this wiki's own, as is the pseudocode.
