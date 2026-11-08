---
title: Throw only for truly exceptional situations
category: errors
summary: "A catch wrapped round a single call, to an exception the callee throws for an ordinary outcome (not found, end of input, invalid entry), whose body returns a normal result or chooses the next step; or a throw-catch pair inside one routine used as a goto."
tags: [rule, exceptions, control-flow]
paradigm: any
sources: [code-complete, elegant-objects, against-railway-oriented-programming]
created: 2026-11-06
updated: 2026-11-07
---

Exceptions pass an error up to code that knows its context: a routine that meets an unexpected situation it does not know how to handle throws, effectively washing its hands of it (p. 193). Their main advantage is that they cannot be ignored, unlike other ways of signalling an error (Meyers, 1996, as cited on p. 194).

## Rule

Use exceptions to notify other parts of the program about errors that must not be ignored (p. 194), and «Генерируйте исключения только для действительно исключительных ситуаций» (p. 194): for situations no other coding technique can address, in the same circumstances as assertions, for events that should never happen rather than merely rare ones (p. 194).

The reasoning is a trade-off: exceptions buy handling of unexpected situations at the price of complexity. «Исключения ухудшают инкапсуляцию» (p. 194), since callers must know what the routine can throw, which adds complexity against software's primary technical imperative of managing complexity (p. 194). Used wisely, like inheritance, they reduce complexity; used to excess, they make code unreadable (p. 194). A sidebar from Hunt and Thomas: programs that use exceptions as part of normal processing suffer from the same readability and maintenance problems as classic spaghetti code (p. 194).

Further rules from the same section:

- «Не используйте исключения по мелочам»: if an error can be handled locally, handle it there, and do not throw an uncaught exception for something that can be fixed on the spot (p. 194).
- Avoid throwing from constructors and destructors unless you catch it later: the rules get complicated fast, and in C++ a destructor is not called for an object whose constructor threw, so resources may leak (p. 194).
- Know what exceptions the libraries you use throw; an uncaught library exception crashes the program as easily as your own. If they are undocumented, write prototype code to find out (p. 196).
- Consider the alternatives: local handling, an error code, logging, shutdown. Using exceptions only because the language offers them is programming in a language rather than into it (p. 198; see [[program-into-the-language]]). And consider whether the program needs to handle exceptions at all: sometimes the best response to a serious run-time error is to release resources and stop, letting the user restart with correct input (Stroustrup, 1997, as cited on p. 198).

### Where this meets *Elegant Objects*

*Elegant Objects* prefers an exception to a returned null ([[never-return-null]]) and so throws for an absence McConnell would call ordinary. On the shape this page names it agrees with him: exceptions are not made to replace conditional statements, and catching in order to choose the next step is control flow (*Elegant Objects*, p. 216). This wiki resolves the two by what the code in view does with the exception. The condition that selects the page: whether the catch around the call turns the exception into ordinary flow. If it does, the exception is a branch, and this page applies. If the exception travels on to an entry point, it is a failure report, and the form for an absence is chosen on [[null-object-or-optional]].

## Sign in code

- A catch wrapped round a single call, to an exception the callee throws for an ordinary outcome, whose body returns a normal result or chooses the next step (a lookup that throws NotFound, caught to return a default).
- A throw and its catch in the same routine, used to jump out of nested logic.
- A constructor that acquires a resource and then calls something that can throw, with no release on that path. [[exception-safe-release]] owns the release shape; this page owns the decision whether the constructor should throw at all.

This wiki assigns the neighbouring cases as follows. This page owns the throw. The catch that swallows a failure a correct program can meet below an entry point is [[recover-only-at-entry-points]]. The condition that selects between the two, in the words both pages use: whether the catch around the call turns the exception into ordinary flow, for an outcome the callee throws though a correct program meets it as a normal result. Then this page owns it and its repair replaces the throw; otherwise that page's repair (rethrow) applies. A catch that turns an exception into a failure value of a result type, rather than into a sentinel or a default, is [[wrap-values-between-transformations]], which decides whether that failure belongs in the result at all.

## When not to apply

- The book itself names one legitimate non-error use: exceptions can simplify tangled logic, as in its try-finally rewrite (p. 193).
- A project or language convention that carries expected outcomes as exceptions (for example a convention that the end of an iterator is signalled by an exception). This wiki adds: follow the convention, and apply this page to the project's own code paths.
- A project standard that names the cases where code may use throw-catch for local error handling (p. 198) overrides the second sign for those cases.
- Where failures are carried as values, see [[wrap-values-between-transformations]] for the shape of the alternative.
- The callee is code the project does not own (a driver, a library) that reports an expected outcome only by an exception, and no check before the call can settle it without a race (a unique key on insert): catch that named exception at the call; [[wrap-values-between-transformations]] decides its form. This limit is this wiki's own.
- **Complex private control flow.** Wlaschin's *Against Railway-Oriented Programming* allows exceptions for control flow «If the control flow is complicated and private». His example is a traversal of a tree that must exit early: threading a result through each node with bind makes the logic hard to get right, while a private local exception, thrown when the traversal must stop and caught at the top, «can often make the code clearer», «As long as the code is not too long, and the exception is defined locally»; «if no consumers ever see the internals, then no harm, no foul» ([[against-railway-oriented-programming]]). This wiki resolves that against McConnell's rule by setting: the limit holds where the exception type is defined locally, the code is short, and the exception is thrown from inside a recursive or nested traversal that no single return or break can leave, and is caught by the one function that starts the traversal, so no caller sees it; where a return, a break or a loop condition exits as directly, or the exception escapes that function, this page's rule holds.

## Repair

For an expected outcome, return it in the form chosen on [[null-object-or-optional]] (an optional, a result, a null object, a status) and let the caller branch. Handle locally what can be fixed locally. Move resource-acquiring work out of the constructor into a factory or an explicit open step, or release on the throwing path. Wrap a library whose exceptions are undocumented behind a boundary that catches what it throws and translates it ([[exception-at-the-interface-abstraction]]).

## Before and after

```
# before
function find_customer(id):
    row = db.lookup(id)
    if row is none: throw CustomerNotFound(id)
    return to_customer(row)

function greeting(id):
    try:
        return "Hello, " + find_customer(id).name
    catch CustomerNotFound:
        return "Hello, guest"
```

```
# after (project convention: a checked optional type)
function find_customer(id) -> optional Customer:
    row = db.lookup(id)
    if row is none: return empty
    return of(to_customer(row))

function greeting(id):
    customer = find_customer(id)
    if customer is empty: return "Hello, guest"
    return "Hello, " + customer.value.name
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 193 for what exceptions do and the try-finally use, p. 194 for the rule, its trade-off and the constructor/destructor rule, p. 196 for library exceptions, p. 198 for alternatives, the Stroustrup remark and the project standard for local throw-catch. Bugayenko, *Elegant Objects*, [[elegant-objects]], p. 216 for exceptions not replacing conditionals. Wlaschin, "Against Railway-Oriented Programming", fsharpforfunandprofit.com, 2019, [[against-railway-oriented-programming]], for the limit on complex private control flow; the conditions that resolve it against McConnell are this wiki's own. The resolution between the two books, the signs, the split with [[recover-only-at-entry-points]], the convention limit, the repair and the example are this wiki's own.
