---
title: Least privilege
category: errors
summary: "Code holds elevated rights from entry to exit when only one call needs them, a service uses administrator credentials, or a single admin/user flag guards every resource."
tags: [rule, errors, security, privileges, defensive-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

This wiki's reasoning is that privilege held is damage available if the code is subverted. The book adds that reducing how much is held, and for how long, shrinks the [[attack-surface]] in both scope and time (p. 287).

## Rule

Use the least privilege for the shortest time. When a high level is required, take it for the minimum work and release it quickly (pp. 286-287). The book attributes the principle to Jerome Saltzer in 1974 and uses Unix `login` as its example: it runs as root, and drops to the user's privileges as soon as authentication succeeds (p. 287).

The principle reaches beyond the operating system. An application with administrator and user levels should provide finer gradations, dividing sensitive resources into categories and granting users rights only to some of them (p. 287).

## Sign in code

- Elevation occurs at the top of a function and is released at the end, while only one statement in between needs it.
- A connection string or config in view names an administrator or owner account, and the code performs ordinary reads and writes.
- A single `is_admin` check guards unrelated sensitive operations.

## When not to apply

This wiki's reading of the trade-off is that fine-grained roles cost code and review effort. An application with one kind of sensitive resource and a handful of operators gains little from a role matrix, and a matrix nobody can reason about is its own risk. This wiki finds the time-limiting half cheaper, with one exception: where a dropped privilege cannot be taken back, elevation cannot be scoped to a block, and the privileged call moves to a separate helper that holds it.

## Repair

1. Move elevation to the narrowest block that needs it, and release it there, including on the error path.
2. Give the service an account limited to the tables or operations it uses.
3. Replace the broad flag with a permission named after the resource and the action.

## Before and after

Before: rights are held across unrelated work.

```
function rotate_logs():
    elevate()
    files = list_logs()
    report = summarize(files)
    chown_archive(files)
    send(report)
    release()
```

After:

```
function rotate_logs():
    files = list_logs()
    report = summarize(files)
    with elevated():
        chown_archive(files)
    send(report)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 286-287. This wiki's own: the opening reasoning, the signs, the limit, the repair steps and the pseudocode. Related: [[business-rules-are-metadata]], for holding who may do what as data.
