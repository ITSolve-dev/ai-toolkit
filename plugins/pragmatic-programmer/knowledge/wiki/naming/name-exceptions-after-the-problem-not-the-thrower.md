---
title: Name an exception after the problem, not after the thrower
category: naming
summary: "A thrown exception class is named for the component, class or layer that throws it (PersistenceSubsystemException, OrderServiceError) rather than for the cause, so its name says who failed and not why; name each thrown type for the cause (DbUnavailable, ProductNotFound)."
tags: [rule, exceptions, naming]
paradigm: any
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Larman records the pattern **Name The Problem Not The Thrower** [Grosso00]. Explaining why his persistence code throws `DBUnavailableException` rather than `PersistenceSubsystemException`, he says to give an exception "a name that describes why the exception is being thrown, not the thrower" (35.3, p. 791).

## Rule

Name an exception class for the condition that caused it. Larman gives two benefits: it "makes it easier for the programmer to understand the problem", and it "highlights the essential similarity of many classes of exceptions (in a way that naming the thrower does not)" (p. 791).

This wiki reads the second benefit like this: two components that both fail because a resource is unavailable can throw exceptions with the same kind of name, and a handler can treat them alike, while a name built on the thrower hides that likeness behind two different nouns.

## Sign in code

This wiki's reading of the sign:

- A thrown exception class is named for the component, class or layer that throws it, a component name plus `Exception` or `Error` (`PersistenceSubsystemException`, `OrderServiceException`, `RepositoryError`), rather than for the cause. Larman's own case has one cause: database unavailable (p. 791).

This wiki assigns the neighbouring cases as follows. How many exception types a library needs, including whether a handler that reads a code or message field to choose its action needs distinct types, is decided on [[chain-exceptions]]; what each thrown type is called is [[name-exceptions-after-the-problem-not-the-thrower]]. Whether a type belongs to the level of abstraction of the routine that throws it is [[exception-at-the-interface-abstraction]].

## When not to apply

- A base class that exists only to group a component's exceptions, so callers can catch them all at once, may carry the component's name, as long as the subclasses actually thrown are named for the problem. This limit is this wiki's own.
- Where one type covers several causes and no handler branches on them, one type is enough by [[chain-exceptions]]; this page then asks only that the name state the kind of failure the causes share. This limit is this wiki's own.
- A project or framework convention for exception names overrides this page.

## Repair

Rename each thrown type for its cause (`DbUnavailable`, `ProductNotFound`), and update the handlers that catch it. Whether to split one type into several is decided on [[chain-exceptions]].

## Before and after

```
class PersistenceSubsystemException

// thrower, when the database cannot be reached
throw PersistenceSubsystemException("database unavailable", cause = e)

// handler
catch PersistenceSubsystemException e
  useLocalCache()
```

```
class DbUnavailable

throw DbUnavailable("database unavailable", cause = e)

catch DbUnavailable e
  useLocalCache()
```

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.3, PDF p. 791: the pattern name and the two benefits.
- This wiki's own: the reading of the second benefit, the signs, the owner assignments, the limits, the repair and the pseudocode.
