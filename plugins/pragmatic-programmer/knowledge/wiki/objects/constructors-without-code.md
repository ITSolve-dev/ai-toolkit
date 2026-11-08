---
title: Constructors hold no code
category: objects
summary: "A constructor body parses, converts, validates, calls methods on its arguments or does I/O, instead of only assigning arguments, raw, or wrapped in objects by a secondary constructor, to fields."
tags: [rule, constructors, laziness, composition]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-07
---

*Elegant Objects* holds that a constructor should only assign its arguments to fields, either as received or wrapped in other objects, and leave all work on them to the object's methods. The book's rule of thumb is «Не трогайте аргументы» (p. 34).

## Rule

Object initialisation must contain no code and must not touch its arguments. Instead it wraps them where needed or encapsulates them raw (p. 35). The book's `Cash(String)` that calls `Integer.parseInt` in the constructor is rewritten to store `new StringAsInteger(dlr)`, an object that parses only when its `intValue()` is called (p. 35). Under [[one-primary-constructor]] the wrap then moves into a secondary constructor, and the primary one only assigns (pp. 35-36). In C++ the constructor body stays empty and the member initialiser list does the wrapping (p. 37).

The book gives three reasons:

- **Building and working are separate steps.** Instantiating composes smaller objects into a larger one under a new contract (p. 36). The constructor should not ask its arguments to do anything, since nobody has yet asked the object itself to do anything (p. 37). See [[object-as-representative]].
- **The client controls when the work happens.** A constructor that parses always parses, even when the object is never used, as when an exception is thrown between construction and the first call (p. 38). Deferred work runs only when asked. Where repeated work is the concern, the client wraps the object in a caching decorator, `CachedNumber`, and gets one parse without the class deciding for every client (p. 39). The author calls such objects lazy: «Они очень ленивы — в хорошем смысле» (p. 40).
- **Refactoring.** A class may change after the next refactoring, and logic placed in the constructor has to be moved into methods before real changes can be made: «Помещая все манипуляции в конструктор, мы существенно усложняем рефакторинг» (p. 40).

The author says he tried to find a second technical reason and could not (p. 40). The same idea at application scale is `new App(new Data(), new Screen()).run()`: while the application is being assembled it connects to no database and opens no port, and only `run()` lets the objects work (pp. 40-41).

On errors the book is explicit. Asked whether an object built from a JSON response of a web API should throw, the author replies: «Должен, но только тогда, когда с ним начинают работать, а не тогда, когда его собирают» (p. 41).

## Sign in code

- A constructor body contains a call on an argument (`text.trim()`, `parse(text)`, `list.sort()`), a computation, a loop or a branch, rather than only assignments.
- A constructor opens a connection, reads a file, starts a thread or makes a request.
- A secondary constructor computes the argument it passes to the primary one, as in `this(parse(text))`.

This page owns any computation in a constructor. A class in which more than one constructor assigns the fields is [[one-primary-constructor]]. `new` in the constructor that assigns the fields, including wrapping an argument, is [[new-only-in-secondary-constructors]]. A check in the constructor that rejects an impossible internal state, raised by a bug rather than by input, is still a computation in a constructor; whether to keep it eagerly is decided by the limits below. Where the eager check stays, its form is owned by [[crash-early]]. I/O or a call to a global service inside a constructor body belongs to this page; the same call inside a method belongs to [[global-data]]. A repository or catalogue lookup in a constructor body, as in Fowler's step towards a shared kind, is this page's; [[replace-superclass-with-delegate]] does that lookup at the creation site. A constructor that acquires a resource the class releases in its own close or destructor is the RAII form, owned by [[exception-safe-release]] and not a finding of [[constructors-without-code]]. The book recommends that form for real resources in section 4.4 (p. 238).

## When not to apply

The book concedes that work which obviously happens exactly once may go in the constructor, while advising against it for uniformity (p. 40). A reader objected that in most cases deferring object-building work breaks the fail-fast principle, and granted laziness only for infinite streams and heavy objects, citing the Virtual Proxy pattern (p. 41). The author rejects the objection: failure belongs to use, not to building (p. 42). Asked about an empty `EnglishName`, he says the constructor should not check its input even for NULL (p. 42). This wiki's per-setting limits below override that answer where the object escapes or the input is external, resolving the disagreement with [[crash-early]] per setting:

- **Defer**, as the book says, where the object is used in the same call chain that built it: a failure on first use then surfaces next to the place of construction, and the book's gain is real, since unused objects never pay.
- **Validate when building** where the object escapes the frame that built it: it is stored in a long-lived field, put on a queue, persisted, cached or handed to another thread. A deferred failure there surfaces far from its cause and long after, which is the harm [[crash-early]] exists to prevent (p. 149 of [[pragmatic-programmer]]). The check need not live in the constructor of the value. It can be a separate step at the boundary that builds the object, which keeps the constructor empty.
- **Validate when building** where input comes from outside and the sender must be told before anything happens on its behalf. See [[distrust-external-input]].

This wiki adds two further limits:

- Deferred work runs on every call unless a decorator caches it, so a hot path that calls the method many times pays repeatedly. The repair is the book's decorator, and the cost is an extra class and a mutable cache inside an otherwise immutable design (see the caching limit on [[immutable-objects]]).
- A project or framework convention that initialises in the constructor, such as dependency injection that validates configuration at startup, overrides this page for those classes. Startup validation is often the very point of such frameworks.

## Repair

1. Replace each computation on an argument with an object that wraps the argument and performs the computation in a method (`StringAsInteger` for parsing).
2. Leave the constructor body with assignments only; in a secondary constructor, pass the wrapping object to the primary one.
3. If the work is expensive and repeated, let the client wrap the object in a caching decorator rather than restoring eager work.
4. Move I/O and start-up from constructors into a method such as `run()`, called after the object graph is assembled.

## Before and after

```
class Price:
    constructor(text: string)
        this.cents = to_int(text.strip("$")) * 100
        this.rates = http_get("/rates")
    cents()
        return this.cents

p = Price("$5")
print(p.cents())
```

```
class Price:
    constructor(text: string)
        this(CentsIn(text), RemoteRates("/rates"))
    constructor(cents: Number, rates: Rates)
        this.cents = cents
        this.rates = rates
    cents()
        return this.cents.value()

p = Price("$5")
print(p.cents())
```

The after assigns only. The parse runs in `CentsIn` when `p.cents()` asks for it, and the request in `RemoteRates` when rates are first asked. `p` is used where it is built, so the deferral limit does not call for eager validation.

## Source

[[elegant-objects]]: pp. 34-42, including the reader discussion on pp. 41-42, and p. 238 for the RAII recommendation that this wiki reads as an exception to the rule. The book's `StringAsInteger`, `CachedNumber` and `App` examples are summarised, not reproduced. The quotation on p. 40 was checked against the page image. This wiki's own: the signs as worded, the ownership split with [[one-primary-constructor]], [[crash-early]] and [[global-data]], the per-setting resolution of the fail-fast disagreement (defer within the building call chain; validate where the object escapes or input is external), the hot-path and framework limits, the repair steps and the pseudocode.
