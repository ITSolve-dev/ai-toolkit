---
title: A method either builds or manipulates, never both
category: functions
summary: "A method or function that changes state and also returns a value (bytes written, a 'changed' flag, the previous value, the new value it just set, as roll() returning the face value; or a finder that also raises an alarm, as alertForMiscreant returning the name it found); split it into a command and a query, or return an operation object."
tags: [rule, command-query-separation, side-effects, return-values, separate-query-from-modifier]
paradigm: any
sources: [elegant-objects, code-complete, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-02
updated: 2026-11-07
---

*Elegant Objects* (section 2.4) divides methods into **builders**, which construct and return a new object, and **manipulators**, which change the real-world entity the object represents and return `void`. The author notes that this matches Bertrand Meyer's division of methods into queries and commands (p. 54, footnote). The naming half of the section is [[builder-and-manipulator-names]].

Larman states the same principle under Meyer's name, Command-Query Separation, in chapter 18 (18.5, pp. 506-507).

Fowler's *Refactoring* gives the step-by-step way to split such a function, **Separate Query from Modifier** (2nd ed., ch. 11, PDF pp. 342-346), and a precise limit on what counts as a side effect. His statement covers any function, not only methods: "any function that returns a value should not have observable side effects" (PDF p. 343).

## Rule

There is no third kind. A method may not both manipulate and return something, and may not both build and manipulate: «Он либо строитель, либо манипулятор. И ни в коем случае не может выполнять обе роли.» (p. 64).

The book bans a manipulator that returns anything at all: «Не должно быть … методов, которые манипулируют и возвращают что-то» (p. 55). This wiki narrows the sign below to a returned value that describes the operation or the state it has just set, or a computed result returned by a method named for its action; that narrowing is its own.

The reasoning, in the book's terms:

- **A returned value from a command is a hidden second responsibility.** `int write(InputStream)` on `Document` writes and also counts bytes. Neither a verb nor a noun names it cleanly, because its purpose is ambiguous: «Он расплывчат, несфокусирован.» (p. 62). The builder/manipulator test thus exposes a method that does too much (pp. 61-62).
- **Asking for a change and demanding a report back** is what the book calls disrespectful toward the object. Its picture is asking a barman to turn the music up and tell you the volume. A manipulator may even be ignored, because nothing is expected in return (p. 60).
- **A query that changes state is a surprise.** Larman, after Meyer: every method should be either a command that performs an action, often has side effects, and is void, or a query that returns data and has no side effects, and "a method should not be both" (18.5, pp. 506-507). His reason: "you can more easily reason about a program's state without simultaneously modifying that state"; in an application that follows it consistently, a query or getter "isn't going to modify anything" and a command "isn't going to return anything" (p. 507). Breaking it is a "nasty surprise" against the Principle of Least Surprise; his deliberately extreme example is a `getName` that launches a missile before returning the name (p. 507).
- **A pure query can be used freely.** Fowler: a function that gives a value without observable side effects can be called as often as wanted, moved elsewhere in the caller, and is easier to test (PDF p. 343). He does not hold the rule as absolute: "I’m not 100 percent pure on this (as on anything), but I try to follow it most of the time" (PDF p. 343).
- **Multiple return values make it worse.** The author calls Go's multiple returns a mistake. A `write` returning `(int, int)` keeps the programmer inside `Document` and grows its method, where the point of OOP is to isolate the smallest concept, here "writing bytes to the document file", in its own class (p. 62).

## Sign in code

A method that mutates state (writes, stores, sets, removes, sends) and also returns a value describing the operation, or the new value it has just set; or a method named for its action that also returns a result it computed (an item found). Examples from the books:

- `int save(content)`, returning the number of bytes saved
- `boolean put(key, value)`, returning whether the map changed
- `float speed(val)`, setting the speed and returning the previous one (p. 56)
- `int roll()` on a `Die`, setting the face value and returning it (Larman, 18.5, p. 506)
- a function that searches a list, raises an alarm when it finds a match, and returns what it found (Fowler's `alertForMiscreant` calling `setOffAlarms()`, PDF p. 344); a caller assigns the result of a call named as an action (`found = alertFor...(people)`)

A method whose name's part of speech does not match whether it returns belongs to [[builder-and-manipulator-names]]. A method that mutates and returns a value describing that mutation (a count, a flag, a previous value), or a method named for its action that also returns a result it computed (an item found), belongs to [[command-query-separation]]; a method whose name promises a read or a result and which also writes as a side job belongs to [[rename-when-meaning-drifts]]. `speed(val)` returning the previous value is this page's.

A bug fix applied to one of several copies of the same logic is [[preparatory-refactoring]]; a function that both updates state and returns a value is [[command-query-separation]], whatever fix lands in it.

*Code Complete* allows a procedure to return a success/failure status (pp. 177-178). This wiki resolves that on [[function-or-procedure]]; the condition that selects the page, in the words both pages use: whether the value a mutating routine returns is a success/failure status in a project that reports failure through return values. If it is, [[function-or-procedure]] applies; any other returned value is this page's.

## When not to apply

*Elegant Objects* and Larman give no limits; Fowler gives the caching one, marked below. The others are this wiki's own:

- **Atomic operations under concurrency.** Compare-and-set, pop from a shared queue, or put-returning-previous on a concurrent map cannot be split into a command and a query without a race between the two calls. The combined form is the contract; see [[check-then-act-must-be-atomic]].
- **Consuming reads.** `pop()` on a stack or `next()` on an iterator removes what it returns, even single-threaded; the returned value is the result, not a report on the change.
- **Transfer counts.** `read(buffer)` returning how many bytes it filled tells the caller which part of the buffer to use, and the count cannot be asked for afterwards.
- **A generated identity the caller needs.** An insert that returns the identifier the store assigned hands back what the caller cannot get any other way without a second lookup.
- **A fluent builder returning `this`.** The returned value carries no state to read, only the same object for the next call. This limit is this wiki's own.
- **Lazy caching inside a query**, invisible to callers, is not a change of the state they can observe. Fowler states this limit: caching a query's value in a field changes the object's state, but "the change is not observable. Any sequence of queries will always return the same results for each query" (PDF p. 343).
- **Builder-style methods on immutable objects** (`withTitle(t)` returning a new `Book`) are builders, not manipulators. The book accepts their names as nouns (pp. 60-61), then says of the Builder pattern itself «не применяйте этот паттерн» (p. 61). Only mutation plus return fires this page.
- **Platform and library APIs** whose signatures you implement or call, such as collection `add` returning a boolean, are fixed by their owner. The rule applies to methods you design.

## Repair

The book gives three repairs (pp. 56, 61-62):

1. If the caller does not need the value, return `void`.
2. If the method is really a query, rename it as one (`bytesSaved()`) and make it stop mutating.
3. If the caller needs to know the outcome of a change, redesign so that a builder returns an operation object. That object has a manipulator that performs the change and builders that report on it: `PutOperation` with `save()` and `success()`, `SaveSpeed` with a setter and a previous-value query, `Document.output()` returning an `OutputPipe` with `write()`, `bytes()` and `time()`. The operation object can then report more than the one value the original method returned, such as the time taken.

Fowler's mechanics for the split (PDF p. 344): copy the function and name the copy as a query, using the name of the variable callers assign the result to as a clue; remove every side effect from the copy; at each call that uses the return value, call the query and then the original below it, testing after each; remove the return values from the original; then remove the duplication left between the two, which in his example leaves the modifier calling the query (PDF p. 346; [[substitute-algorithm]]).

Larman's repair is to split the method into a void command and a side-effect-free query on the same object: `roll()` changes the face value, `getFaceValue()` reads it (18.5, pp. 506-507). The two repairs differ on where the report lives. This wiki resolves it by whether the returned value is state the object keeps after the command. If it is (the face value, the current speed), split into a command and a query on the same object, as Larman does. If the value describes only the operation and the object keeps nothing of it (bytes written, time taken), use *Elegant Objects*' operation object, or return `void` when no caller needs it. If the value is a result computed from state the side effect does not change (the intruder found in a list, before the alarm), use Fowler's split: a query that computes it and a modifier that calls the query.

## Before and after

```
class Document
  write(content): int        // writes, then returns bytes written

n = doc.write(content)
```

```
class Document
  output(): OutputPipe       // builder: nothing written yet

class OutputPipe
  write(content): void       // manipulator
  bytes(): int               // builder
  time(): long               // builder

pipe = doc.output()
pipe.write(content)
n = pipe.bytes()
```

Larman's case, where the value is state the object keeps:

```
class Die
    roll(): int
        faceValue = random(1..6)
        return faceValue

total = die1.roll() + die2.roll()
```

```
class Die
    roll(): void               // command
        faceValue = random(1..6)
    faceValue(): int           // query
        return faceValue

die1.roll()
die2.roll()
total = die1.faceValue() + die2.faceValue()
```

Fowler's case, where the value is computed and the side effect is separate:

```
function alertForIntruder(people)
    for p in people
        if p is on watchlist
            raiseAlarm()
            return p
    return none

found = alertForIntruder(people)
```

```
function findIntruder(people)
    for p in people
        if p is on watchlist
            return p
    return none

function alertForIntruder(people)
    if findIntruder(people) is not none
        raiseAlarm()

found = findIntruder(people)
alertForIntruder(people)
```

## Source

[[elegant-objects]], section 2.4: builders and manipulators and the Meyer footnote, p. 54. No third kind, p. 55. The bad `save`/`put`/`speed` and their `PutOperation`/`SaveSpeed` repairs, p. 56. The barman analogy, p. 60. `Document.write` and `OutputPipe`, the critique of Go, pp. 61-62. Summary, p. 64. The ban on manipulators returning anything, p. 55, and the rejection of the Builder pattern, p. 61; both quotations were checked against the page image. McConnell, *Code Complete*, Russian edition, [[code-complete]], pp. 177-178, for the status-returning procedure. This wiki's own: the narrowing of the sign to a value describing the operation, the splits with [[builder-and-manipulator-names]] and [[rename-when-meaning-drifts]], and all of *When not to apply*. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 18.5 "The Command-Query Separation Principle", PDF pp. 506-507: the rule after Meyer, the reasoning, the Missile example, the `roll`/`getFaceValue` pair. This wiki's own for that part: the resolution between the operation object and the command-plus-query split, the fluent-builder limit, and the `Die` pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 11, "Separate Query from Modifier", PDF pp. 342-346: the rule for any function, the "most of the time" qualification, the reasons a pure query is worth having, the observable-change limit and the caching example, the mechanics, the alarm example. This wiki's own for that part: the third case of the resolution between repairs, the sign of a caller assigning the result of an action, and the intruder pseudocode, after the book's example. Fowler's unnamed exceptions to "most of the time" are read here as the atomic-operation limit above, which is this wiki's. The selecting sentence against [[preparatory-refactoring]] is this wiki's own.
