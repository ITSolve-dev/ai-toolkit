---
title: Which defensive code stays in production
category: errors
summary: "A release build keeps a debug-time abort that can lose the user's unsaved work, drops a check on a calculation whose error would go unnoticed, or shows the user a message written for the developer; decide per check what the release keeps, removes or turns into a log entry."
tags: [decision-rule, assertions, production, defensive-programming]
paradigm: any
sources: [code-complete, pragmatic-programmer]
created: 2026-11-06
updated: 2026-11-06
---

McConnell names a paradox: during development an error should be as obnoxious as possible, so it is not missed; in production it should be as unobtrusive as possible, so the program can continue or stop gracefully (p. 204). He gives guidelines for what the release keeps.

## Rule

- Keep code that checks for important errors. Decide which parts may have hidden errors and which may not: in a spreadsheet, errors in screen updating can stay hidden, since the worst outcome is a wrong display, but the calculation engine may not hide errors, because they produce wrong results (p. 204).
- Remove code that checks for trivial errors; "remove" means compiling it out through version control, precompiler switches or the like, not deleting it. If space allows, keep it but make it log quietly (p. 205).
- Remove code that results in hard crashes. During development, printing a diagnostic and stopping is often best, even for minor errors; in production users need to save their work before the program fails: «Если ваша программа содержит отладочный код, способный привести к потере данных, уберите его из промышленной версии.» (p. 205)
- Leave in code that helps the program crash gracefully. On the Mars Pathfinder, engineers left some debug code in deliberately; it let them diagnose a problem after landing and upload fixed code, and the mission was completed (March, 1999, as cited on p. 205).
- Log errors for technical support: rather than removing assertions that halt in development, make them write to a log in production (p. 205).
- Make the error messages you leave in friendly: a common approach tells the user of an internal error and gives a phone number and e-mail address for reporting it (p. 205).

### Disagreement with [[leave-assertions-on]], resolved per setting

*The Pragmatic Programmer* says keep assertions on in production and turn off only those that really hurt performance (p. 154); McConnell assumes assertions are compiled out of production (pp. 185-186) and then argues for keeping the important ones as checks or logs. This wiki resolves the two as follows:

- A check on a computation whose wrong result would not be noticed (money, measurements, stored data): keep it in production in either book's reading; how it stops is decided by the next bullet where users hold unsaved work.
- A check whose failure in production should not stop the program, in an interactive program where users hold unsaved work: keep the check, change its reaction to logging and a graceful path. Both books agree that the check stays; they differ only on the reaction, and McConnell's reaction applies where stopping loses user work.
- A check on trivial effects (display) that costs measurably: compile it out, which both books allow.

The condition that selects the reading, in the words both pages use: what a failure of the check costs the user in production, and what the check costs to run.

## Sign in code

- An assertion or debug check in production that terminates the process with no chance to save, in an interactive program holding user data.
- A message left in from development that addresses the developer, uses internal terms, or insults the user (the book's own example, p. 205).

This wiki assigns the neighbouring case as follows. A release configuration that removes all checks, including those on calculation or persistence code, is [[leave-assertions-on]], and this page supplies the per-check classification of its repair. Where the message carries an exception's text, a stack trace or data the user may not see, [[do-not-disclose-in-output]] owns it; this page owns the tone and audience of a message that discloses nothing.

## When not to apply

- Safety-critical code at the correctness end of [[robustness-versus-correctness]]: stopping is the right production reaction, as with the radiation machine (p. 191). This wiki adds: even if work is lost.
- This wiki adds: server processes without unsaved user work, where the data-loss reason for avoiding hard stops does not arise. There [[crash-early]] governs.

## Repair

Classify each check by what its failure would cost in production: important, trivial, or fatal. Keep important checks; make halting checks log and take a graceful path where stopping would lose user work; compile trivial checks out through one switch ([[switchable-debug-aids]]). Rewrite surviving messages for the user and keep the internal detail in the log, not on screen ([[do-not-disclose-in-output]]).

## Before and after

```
# before (release build of a spreadsheet)
function recalculate(sheet):
    totals = compute(sheet)
    assert totals.balance == sum(sheet.cells)    # aborts, unsaved work lost
    ...

function on_internal_error(e):
    abort("pointer allocated wrong, damn it!")
```

```
# after (release build)
function recalculate(sheet):
    totals = compute(sheet)
    if totals.balance != sum(sheet.cells):
        support_log.write("balance mismatch", sheet.id)
        offer_save_and_exit("An internal error occurred. Please report it to support@example.org")
    ...

function on_internal_error(e):
    support_log.write(e)
    offer_save_and_exit("An internal error occurred. Please report it to support@example.org")
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: pp. 185-186 for assertions compiled out of production, p. 191 for the radiation example, p. 204 for the paradox and the spreadsheet example, p. 205 for the remaining guidelines and the Pathfinder story. Thomas, Hunt, *The Pragmatic Programmer*, [[pragmatic-programmer]], p. 154. The resolution against [[leave-assertions-on]], the signs, the splits with [[leave-assertions-on]] and [[do-not-disclose-in-output]], the extension of the first limit, the second limit, the repair and the example are this wiki's own.
