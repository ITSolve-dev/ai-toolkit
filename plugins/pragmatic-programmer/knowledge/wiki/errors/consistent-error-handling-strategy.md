---
title: One error-handling strategy per application
category: errors
summary: "Peer modules of one layer, or the functions of one module, signal the same kind of failure by different mechanisms (one returns a code or null, one throws, one clamps, one shows a dialog), the same input is validated at its entry in one module and nowhere in its peer, or user-facing error messages are composed in many places across domain code."
tags: [rule, error-handling, validation, exceptions, consistency, conventions]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell asks that an application handle errors one way throughout, decided once for the whole system rather than separately in each module. He puts this decision at the architecture level, not in a coding convention, because error handling makes up a large share of the code and affects the whole system (p. 46). He cites an estimate that up to 90% of code deals with exceptional cases and errors, leaving about 10% for the normal path (Shaw in Bentley, 1982; p. 46).

This wiki takes the strategy itself as given, from the project's conventions or brief: choosing it is architecture, which is outside this base. What this page checks is code that departs from the strategy, and code whose units report one kind of failure by mechanisms a caller must tell apart with no rule stated between them.

## Rule

Follow the project's error-handling strategy in every unit, and do not mix mechanisms for one kind of failure without a stated rule. McConnell lists the questions one strategy has to answer for the whole system (pp. 46-47). This wiki uses them as what to read from the project's conventions before judging code, not as choices to make here:

- **Corrective or detect-only.** Does the program try to recover, or only detect the error and then continue or stop? Either way the user must be told.
- **Active or passive detection.** Does it anticipate errors, for example by validating user input, or react only after one happens, for example after a numeric overflow?
- **What happens on detection.** Drop the offending data, switch to an error-handling state, or finish the rest of the work and then report that errors were found.
- **Message conventions.** Without one strategy, the UI looks like a confusing mix of the interfaces of different parts of the program.
- **Exceptions.** When code may throw them, where they are caught, how they are logged and documented.
- **Where errors are handled.** At the point of detection, in an error-handling class, or passed back up the call chain.
- **Who validates input.** Does each class validate its own data, or does a group of classes validate for the whole system? «Могут ли классы конкретного уровня полагать, что полученные ими данные корректны?» (p. 47; a word rejoined across a hyphenation break).
- **Built-in or own mechanism.** That the programming environment has its own approach to error handling does not mean it suits your requirements best (p. 47).

In a cross-reference he adds that a consistent way of handling invalid parameters also belongs to this strategy (p. 47, pointing to ch. 8).

### What chapter 34 adds

The closing chapter lists the same decision among the tools for managing complexity: one deliberately chosen approach to error handling instead of an arbitrary mix of techniques, and systematic use of the built-in exception mechanism, because undisciplined exceptions become a non-linear control structure almost as hard to follow as `goto` (p. 818). Error-handling conventions add expressive structure and make code easier to follow for anyone who knows them (p. 825). See [[managing-complexity]] and [[coding-conventions]].

### What chapter 8 adds

Chapter 8 returns to the decision. The way a program reacts to bad data determines whether it meets its correctness, robustness and other non-functional requirements (p. 192), so: respond to invalid parameters the same way throughout the program, choose the approach during architecture or high-level design, and «Выбрав подход, придерживайтесь его неукоснительно.» (p. 192). Which reaction to choose is decided on [[robustness-versus-correctness]].

The policy must say which parts of the system handle errors directly and which only report them; the book holds that this matters more than the reporting mechanism (status variable, return value or exception) (pp. 190-191). If low-level code reports and high-level code handles, make sure the high-level code really does handle (p. 192). Check every returned error, including from system calls: «Даже если вы считаете, что ошибка в функции возникнуть не может, все равно проверяйте.» (p. 192). On a failed system call, report its number and description (p. 192). If the system must be secure, callers always check return codes (p. 191).

The book weighs where handling sits:

- A central error-handling routine or object concentrates control and eases debugging, but the whole program then depends on it, and reusing a part elsewhere drags the whole mechanism along. After a buffer overflow an attacker may learn the handler's address (pp. 191-192).
- Displaying a message wherever an error occurs has the least overhead, but spreads user-interface code through the application, which hurts a consistent interface, separating the UI, and localisation; and messages can tell an attacker too much (p. 191).
- Handling locally at the programmer's discretion gives flexibility but risks the system as a whole failing its correctness and robustness requirements, and can spread UI code in the same way (p. 191).

For exceptions, the book asks the project to standardise: what may be thrown (in languages that allow any type, only objects derived from a base exception class), a project base exception class, when throw-catch may handle an error locally, when an exception may leave a routine uncaught, whether a central exception reporter is used, and whether constructors and destructors may throw (pp. 197-198). A central reporter keeps the knowledge of which exceptions exist, how each is handled and how messages are formatted (p. 196).

## Sign in code

This wiki reads the following as the sign. Within one application, peer modules at the same layer, handling the same kind of failure, do at least two of these, where the project states a strategy or most peers visibly follow one:

- some return an error code or null for the failure while others throw;
- some catch and log, then continue, while others let the failure propagate;
- the same kind of input is validated at its entry point in one module and nowhere in its peer.

The same shape inside one module counts too: its functions, or one class's methods, report failure in two or more of these ways (a status code to check, a thrown exception, a `null` sentinel, an error logged and swallowed, a global error variable set) with no stated rule separating them, so a caller handles each function differently.

A second sign is a failure that reaches the user in several unrelated formats, depending on which module raised it. Its usual cause, after McConnell's warning on p. 191, is calls to a message-box, print or UI routine inside domain or library code, each composing its own error text.

A third sign: in a language allowing any thrown type, the project throws strings, integers and objects of unrelated classes.

This wiki assigns the neighbouring cases as follows. This page owns the mismatch between peers, or between the functions of one module, and needs two units to compare. A single returned `null` on its own is [[never-return-null]]; a single log-and-continue on its own is [[recover-only-at-entry-points]]. A single catch below an entry point that swallows a failure is [[recover-only-at-entry-points]]; a bug's failure turned into a default is [[crash-early]]. A routine that clamps or defaults bad input on its own is [[caller-owns-the-precondition]]. A call whose returned status is discarded because it "cannot fail" is [[assert-the-impossible]]; this page owns a discarded status only where the strategy says that layer reports and its caller is the one that should handle. Uneven validation of the same input is [[consistent-error-handling-strategy]]; uneven retry, timeout and fallback around the same dependency is [[uniform-robustness-level]]. User-facing handling for a value already checked at a door on the same path is [[barricade]]; user-facing messages composed in domain code for a real failure are [[consistent-error-handling-strategy]].

## When not to apply

This wiki's own limits:

- **A boundary that has to translate.** Code at a boundary may use a different mechanism on purpose, as long as it translates there: an adapter over a library that returns codes, or a process boundary that serialises failures. Two mechanisms meeting at one translation point is not this sign.
- **A documented project convention.** A convention already in place, such as errors as values in one layer and exceptions in another, is the strategy. Code that follows it is not a violation.
- **A small script with one path.** It has no peers to disagree.
- **A consistent codebase using a different convention than you would pick.** The rule asks for one convention and does not prescribe which, so it does not justify moving consistent code from codes to exceptions or back.
- **A boundary between subsystems with different requirements.** Two strategies are then correct, one per subsystem, as long as each is applied consistently inside it ([[robustness-versus-correctness]]).
- **A deliberate, documented decision to ignore particular system-call failures,** which the book allows as part of the architecture (p. 192).
- **Different exposure.** Validation repeated inside a module that faces hostile input is a deliberate defensive choice, not inconsistency; see [[distrust-external-input]].

## Repair

This wiki's own:

1. Take the strategy from the project's conventions or brief: which mechanism signals failure, where failures are caught, how they are logged, which code validates external input, and how failures reach the user. Where none is stated, report the mismatch and the options found in the code rather than choosing layers.
2. Convert the odd unit to that strategy, adding a translation at the one boundary where a foreign mechanism comes in. Code the strategy treats as already validated asserts its assumptions instead of re-validating; see [[assertion-or-error-handling]].
3. Move a message composed in domain code to wherever the strategy presents failures, and give every discarded status a handler or an explicit, commented decision.
4. Where the language admits arbitrary thrown types and the project has a base exception class, throw only its subtypes; where it has none, report that rather than inventing one.
5. Within one module with no stated rule, pick the mechanism most of its functions already use and state it at the module's head.

## Before and after

```
// before: two importers in one layer, each handling failure its own way
function importCsv(file):
    rows = parse(file)
    if rows == null: return -1          // error code
    for row in rows:
        if not valid(row): log("bad row"); continue
        save(row)
    return 0

function importJson(file):
    rows = parseJson(file)              // throws on bad input
    for row in rows:
        save(row)                       // no validation at all
```

```
// after: one error type, validation in one place, the caller decides how to report
function importCsv(file):
    rows = parse(file) or raise ImportError(file, "unreadable")
    importRows(rows)

function importJson(file):
    rows = parseJson(file) or raise ImportError(file, "unreadable")
    importRows(rows)

function importRows(rows):
    bad = [r for r in rows if not valid(r)]
    if bad not empty: raise ImportError("invalid rows", bad)
    for row in rows: save(row)          // save assumes valid rows
```

Neither importer in the "after" has the sign: both raise the same error type, and validation sits in one place.

One module mixing mechanisms:

```
// before
module accounts:
    function load(id):
        if not found: return null
    function debit(account, amount):
        if amount > account.balance: return -1
    function rename(account, name):
        if name is empty: log("bad name"); return
```

```
// after: stated at the module's head, every operation throws an AccountError subtype
module accounts:
    function load(id):
        if not found: throw AccountNotFound(id)
    function debit(account, amount):
        if amount > account.balance: throw InsufficientFunds(account, amount)
    function rename(account, name):
        if name is empty: throw InvalidName(name)
```

Message boxes in domain code, and a status nobody reads:

```
// before
function loadInvoice(id):
    if id <= 0: showMessageBox("Invoice id is wrong!")
    ...
file.close()                            // result ignored
```

```
// after, under a project strategy where domain code raises and the presenting code formats messages
function loadInvoice(id):
    if id <= 0: raise InvalidArgument("invoice id", id)
    ...
status = file.close()
if status is failure:
    raise StorageError("close failed", file.name, status.code, status.description)
```

## Source

[[code-complete]], ch. 3, section 3.5 («Обработка ошибок»), Russian edition, pp. 46-47: the list of questions, the 90% estimate, and why the strategy is set at the architecture level. Ch. 34.1, p. 818 (one approach, systematic exceptions) and 34.5, p. 825 (error-handling conventions add structure). Ch. 8, Russian edition, pp. 190-192 for the options, consistency and checking return codes, pp. 196-198 for standardising exceptions and the central reporter. The signs (including the within-one-module form and the second and third read from pp. 191 and 197), the assignment of neighbouring cases, the limits other than the system-call one, the repair and the pseudocode are this wiki's own. McConnell states the questions as matters for an architecture specification; taking the strategy as given from the project, and moving the questions to a check of code against it, is this wiki's.
