---
title: Chain exceptions
category: errors
summary: "A catch block throws a new exception built from a message alone, without passing the caught exception as its cause, so the low-level reason is lost; or a library throws or demands catching the language's root exception class."
tags: [rule, exceptions, diagnostics, exception-types]
paradigm: any
sources: [elegant-objects, larman-applying-uml-and-patterns]
created: 2026-11-03
updated: 2026-11-07
---

Catching an exception and throwing a new one is correct practice in the book, provided the new exception wraps the old one (pp. 217, 219). Each layer then adds what it was trying to do, and the final report reads like nested bubbles. The innermost bubble says too many files are open, the next that a size could not be computed, the next that a profile photo could not be read (pp. 218-219). Without the wrap, the low-level message is lost: «делайте цепочки исключений и никогда не игнорируйте исходную проблему» (p. 219).

## Rule

When a catch throws a new exception, pass the caught exception to it as its cause, and say in the new message what this level was doing. The book gives the meaning a lower level lacks as the reason to wrap at all. A message such as "Too many open files (24)" alone is too low-level to explain why a user cannot open a photo (p. 219). Larman's *Applying UML and Patterns* states the same practice inside the Convert Exceptions pattern: "The higher level exception usually wraps the lower-level exception, and adds information" (35.3, p. 791); converting the type is [[exception-at-the-interface-abstraction]].

The book's own maximum is that every method should catch everything, chain it and rethrow at once: «ловите все, объединяйте в цепочки и немедленно перебрасывайте» (p. 219). The limits below narrow that.

On exception types, the book argues that if nobody catches in order to branch, nobody needs the type, so one type is enough (p. 224).

In a language with checked exceptions, the book's rule is to declare every failure as checked. Its reason does not depend on the language: a checked failure stays visible in the signature, while an unchecked `IllegalArgumentException` is hidden from the caller (pp. 213-215). In a language without them, the book gives no rule (p. 211), and how a failure shows in a routine's contract (a declared result type, a documented raise) is decided at work time from the project's convention. The sign that survives in any language is [[wrap-values-between-transformations]]'s second sign: a declared result that cannot represent a failure its body has. In the reader discussion, a reader describes one exception class of his own per application or library and never throwing or catching the base class, and Bugayenko replies: «Я бы тоже не рекомендовал бросать или ловить исключения типа Exception. Определяйте собственный тип.» (p. 227).

## Sign in code

- Inside a handler, a new exception is raised without the caught one attached as its cause, by whatever means the language offers, and the runtime does not attach it implicitly.
- The caught exception's message is pasted into the new message as text (`"failed: " + e.message`) while the exception object itself is dropped, so its type and stack are lost.
- Library code throws or declares the root exception class of the language, or callers of a library must catch it.

This page owns a catch that throws a new exception. A catch that does not throw at all is [[recover-only-at-entry-points]] or, for a failure only a bug can produce, [[crash-early]]. A catch that logs and rethrows the same exception is [[log-and-rethrow]]. Whether the new exception's type matches the level of abstraction of the routine's interface is [[exception-at-the-interface-abstraction]]; this page owns whether the cause is kept. What the first throw records is [[exception-message-carries-context]].

This wiki assigns the neighbouring cases as follows. How many exception types a library needs, including whether a handler that reads a code or message field to choose its action needs distinct types, is decided on [[chain-exceptions]]; what each thrown type is called is [[name-exceptions-after-the-problem-not-the-thrower]].

## When not to apply

- **Wrapping that adds nothing.** The book's "catch everything in every method" conflicts with [[log-and-rethrow]], which prefers the bare call. This wiki resolves the two by setting: wrap where this level can add something the final reader needs, such as the identifier it was working on, or the exception crosses a layer boundary. Where a new message would only restate the callee's, let the exception pass untouched. A wrap that would add nothing is no reason to catch.
- **Output to an untrusted party.** The chain is for the program and its operators. At the point where a failure is shown to an outside user, the inner causes may disclose internals. Keep the chain in the log and show a reduced message: [[do-not-disclose-in-output]]. This limit is this wiki's own.
- **Exception types where some handler branches.** A reader objects that a form needs to tell "not a number" from "too big" (pp. 226-227). This wiki reads the book's "one type" as holding only while no handler chooses its action by kind. Where one does, the kinds that handler distinguishes need distinct types, or a distinct field, and no others.
- **Outside Java.** The author says almost everything in section 4.2 gives no practical advice outside Java or a new OOP language (p. 211). This wiki applies chaining in any language because its reason, the lost low-level message (p. 219), does not depend on exceptions being checked. That transfer is this wiki's own.

## Repair

1. Pass the caught exception as the cause argument of the new one. Where the runtime has no cause field, carry the cause's type and message in a field rather than in the message string.
2. Rewrite the new message to state what this method was attempting, with its identifying data.
3. Replace a thrown or declared base exception class with the library's own exception type.
4. A handler that logs and then throws a wrapped exception still logs twice: delete the log line.

## Before and after

```
# before
function length(file):
    try:
        return size_of(read_all(file))
    catch IoFailure as e:
        throw Failure("cannot compute size")
```

```
# after
function length(file):
    try:
        return size_of(read_all(file))
    catch IoFailure as e:
        throw StorageFailure("cannot compute size of " + file.path, cause = e)
```

## Source

- Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018, section 4.2: chaining on pp. 217-219, checked exceptions and their visibility on pp. 213-215, one exception type on p. 224, the reader discussion on pp. 226-227 (Bugayenko's reply on p. 227), and the scope of the section on p. 211. Summary page: [[elegant-objects]].
- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.3, PDF p. 791: wrapping the lower exception and adding information; the quotation is in English and was checked against `raw/`.
- The quotations from pp. 219 and 227 were checked against the page image.
- This wiki's own parts are: the signs as worded; the ownership split with [[recover-only-at-entry-points]], [[crash-early]], [[log-and-rethrow]], [[exception-at-the-interface-abstraction]] and [[exception-message-carries-context]]; the resolution against [[log-and-rethrow]]; the limit on disclosure to outside users; the reading of "one type" as holding while no handler branches on kind; the fallback for runtimes without a cause field; the transfer of chaining to languages other than Java; the rule that a language without checked exceptions takes the form of a failure in a contract from the project's convention; and the log-line step of the repair.
