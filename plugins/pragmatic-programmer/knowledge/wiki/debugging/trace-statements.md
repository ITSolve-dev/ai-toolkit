---
title: Trace statements in a uniform format
category: debugging
summary: "Diagnostic output differs in format at each call site, or only one side of a paired event such as open/close is traced, so a log cannot be processed by a tool."
tags: [rule, debugging, logging, tracing]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A debugger shows the state of a program now. A trace shows it over time. The two answer different questions, and the format of a trace decides whether a tool can read it.

## Rule

The book says debuggers concentrate on current state, while some problems require watching the state of a program or data structure over time (p. 130). A stack trace shows how the program directly reached the present state, and usually not what happened before that call chain, especially in event-driven systems (p. 130). Tracing is therefore invaluable where time itself matters: concurrent processes, real-time systems and event-driven applications (p. 131). It also helps drill down by adding statements while descending the call tree (p. 131). The format is part of the rule: «Сообщения трассировки должны быть представлены в обычном согласованном формате, чтобы их можно было анализировать автоматически» (p. 131).

## Sign in code

- Diagnostic lines for the same kind of event are built from different free-form strings at different call sites, so no one pattern matches them all.
- One side of a paired operation is traced and the other is not, for example `open` logged and `close` silent.
- Bare position markers such as `print("here 2")`, which say neither what happened nor to which object.
- A log line carries a value without saying what it is.

This wiki assigns the two neighbouring shapes by whether a line exists. This page owns lines that exist in a form no tool can read. State that no line or view exposes at all belongs to [[test-window]].

## When not to apply

The book gives the first limit by contrast. The others are this wiki's own.

- The state at one moment is enough, so a debugger or stack trace answers the question more directly (p. 130).
- Tracing a hot path or a race can change the timing that causes the fault, so a missing failure under tracing proves nothing.
- A short-lived print used once during a session and removed before commit does not need a format.

## Repair

1. Give every trace line the same fields: event name, the identity of the object, then the values.
2. Trace both sides of any paired event.
3. Process the log with a script. The book's example finds a resource leak by tracing each `open` and `close` to a log file, then using text tools or shell commands to find the `open` that broke the balance (p. 131).

## Before and after

```
// before: only the opening is traced, in a one-off wording
function read(path):
    print("opening " + path)
    file = open(path)
    if file.isEmpty:
        return []           // leaves the file open
    result = parse(file)
    close(file)
    return result
```

```
// after: both sides are traced in one shape, and a tool can pair them
function read(path):
    file = open(path)
    trace("open", file.id, path)
    if file.isEmpty:
        return []           // the leak is still here, and the log now shows it
    result = parse(file)
    close(file)
    trace("close", file.id)
    return result
```

```
// checking the log: report every id with an open and no close
for each line in log:
    if line.event == "open":  pending.add(line.id)
    if line.event == "close": pending.remove(line.id)
report pending
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 130-131. The rule, the systems it fits and the open/close example are the book's. The signs and their assignment against [[test-window]], the second and third limits, the field layout and the pseudocode are this wiki's own. The book's own description of a trace statement includes a message that execution reached a given place (p. 130), so the objection to bare position markers is this wiki's and concerns format only.
