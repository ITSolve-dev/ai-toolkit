---
title: Distrust external input
category: errors
summary: "A value from a request, a file or a user is concatenated into a shell command, a query or markup without being sanitized first, or a secret is silently cut or stripped before hashing or storing."
tags: [rule, errors, security, input-validation, defensive-code]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

This wiki's reasoning is that data from outside the program can be crafted by someone who wants it to be misread as instructions, and that treating it as plain text at the moment it meets an interpreter is how injection happens.

## Rule

«Никогда не доверяйте данным из внешнего источника» and always sanitize it before storing it in a database, rendering it for display or processing it (p. 285). The book's example passes a user-supplied file name into a shell command; a name with an appended second command then runs that command too (p. 285). Its footnote points to injection through database queries as well (p. 285).

This wiki reads sanitizing as never damaging a secret. The book says not to truncate a password the user chose, and that a special character able to compromise the system signals a much larger problem (p. 289).

## Sign in code

- A string built by concatenation or interpolation reaches a shell, a database query or an HTML template, and one of its parts comes from a request, a file, a message or an environment the program does not control.
- A command runs through a shell when an external value is part of its text.
- A value read from storage is treated as safe, although it entered the system from outside. Judging this needs a trace of what writes that storage, and this wiki gives no verdict without one.
- A password or other secret is cut to a fixed length or stripped of characters before hashing or storing, with no error to the user.

## When not to apply

These limits are this wiki's own.

- A value computed entirely inside the program from constants has no external part. A value's origin counts, not the module that happens to hold it, so data that once came from outside stays external after being stored.
- The value comes from the same operator whose rights the command already runs under, as in a developer's local script. Injection there gives that operator nothing new, so it is reported as a bug and not as a breach.
- A stage with a real length limit may refuse a longer secret. It rejects the value and never cuts it silently.

## Repair

1. Pass the value through a channel that keeps data apart from code: an argument list instead of a shell string, a parameterized query, an escaping template.
2. Where the valid set is known, check against it and reject the rest.
3. Do this at the point where the value meets the interpreter, not at some earlier point that another path can bypass.
4. Keep a secret whole: pass it through unaltered, and reject what a stage cannot take.

The book notes that some languages help by marking external values as tainted (p. 285). How that applies in a given language is settled at work time.

## Before and after

Before: a report name such as `x; delete-everything` runs a second command.

```
name = request.field("report")
run_shell("cat reports/" + name)
```

After: the name is checked and never interpreted by a shell.

```
name = request.field("report")
if name not in known_report_names():
    reject("unknown report")
run_program("cat", ["reports/" + name])
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 285, 289. This wiki's own: the opening, the reach of the first sign beyond a shell command and a database query, the second, third and fourth signs, the reading of sanitizing as sparing a secret, the limits, the repair steps and the pseudocode. The book's Ruby-specific taint mechanism is not recorded. Related: [[attack-surface]].
