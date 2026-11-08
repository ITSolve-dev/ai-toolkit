---
title: Function or command object
category: functions
summary: "A long function whose locals are so entangled that Extract Function would need most of them as parameters, so it is turned into an object with an execute method; or, the other way, a small class built and called once per use (new ChargeCalculator(a, b, c).charge) with no undo, queueing, staged setup or subclassing, which is just a function in disguise."
tags: [decision-rule, command-object, replace-function-with-command, replace-command-with-function, decomposition]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler gives two inverse refactorings, **Replace Function with Command** (formerly Replace Method with Method Object) and **Replace Command with Function** (*Refactoring*, 2nd ed., ch. 11, PDF pp. 376-387). A command object here is an object mostly built around a single method, whose request and execution is the purpose of the object (PDF p. 377), the GoF command pattern. Fowler warns that the word is not the command of [[command-query-separation]]; for that sense he says "modifier" or "mutator" (PDF p. 378).

## Rule

Prefer a function. Given the choice between a first-class function and a command, Fowler says: "I’ll pick the function 95% of the time" (PDF p. 378). Use a command only for a facility simpler means cannot give.

What a command offers, in Fowler's list (PDF p. 377): complementary operations such as undo; methods that build up its parameters over a richer lifecycle; customisation through inheritance and hooks; function-like values in a language without first-class functions; and, the case his example shows, breaking down a complex function with methods and fields even without nested functions, while being able to call those methods directly in tests and debugging.

The cost, in Fowler's words: this flexibility comes "at a price paid in complexity" (PDF p. 378). Hence the inverse: when the caller only wants to invoke a function and have it do its job, and the function is not too complex, a command "is more trouble than its worth" (PDF p. 384; spelling as printed).

## Sign in code

Toward a command:

- A long function with many locals read and written across its length, where extracting any part would need most of those locals as parameters and results. The Long Function smell sends this case here: when temps and parameters remain after the other repairs, it is "time to get out the heavy artillery: Replace Function with Command" (ch. 3, PDF p. 88).

This wiki assigns the length itself to [[routine-length]]; this page owns only the choice of the command object as the means of splitting it. Where extracting a fragment would need most of the routine's locals as parameters or results, the temps are removed first ([[replace-temp-with-query]]); where they still tangle, [[function-or-command-object]] owns the choice of a command object; where the routine is to stay whole, the intent comment is split into finer steps ([[extract-routine-to-name-a-step]]).

Toward a function:

- A class whose constructor only stores its arguments, with one public method, and every use is construct-then-call on one line (`new ChargeCalculator(c, u, p).charge`, PDF p. 385), with no undo, queueing, staged setup or subclassing.

## When not to apply

- Where nested functions or closures serve the decomposition, either works: Fowler calls nested functions a reasonable alternative, and still picks the command, partly out of familiarity and partly so that the subfunctions can be tested and debugged directly (PDF p. 383). This wiki prefers the closure when the subfunctions need no direct test.
- Not back to a function when the command uses any facility from the list above, or when its methods are still too complex to inline into one function.
- Where the project follows *Elegant Objects*, a small object built and asked once is the norm rather than a disguise, and the project convention governs ([[object-as-representative]]). This limit is this wiki's own reading.

## Repair

Function to command (PDF pp. 378-383): create an empty class named after the function; Move Function into it, keeping the original as a forwarding function; name the execute method by the language's convention, else `execute` or `call`; move arguments to the constructor so `execute` takes none, which matters when commands with different parameters are queued together (PDF p. 380); then turn locals into fields one at a time, after which [[extract-function]] works without tangling over scopes (PDF p. 383).

Command to function (PDF pp. 384-388): extract a function wrapping construction and the call; inline each supporting method (Extract Variable first if it returns a value); move the constructor's parameters onto the execute method; switch each field reference to the parameter, testing after each; inline construction and call into the wrapper; delete the class. Fowler removes each field assignment as he goes, so that a missed reference fails a test, and if no test fails, he considers adding one (PDF p. 388).

## Before and after

```
class FeeCalculator
    constructor(account, units, tariff)
        self.account = account
        self.units = units
        self.tariff = tariff
    fee()
        return self.account.rate * self.units + self.tariff.fixedFee

monthly = new FeeCalculator(account, units, tariff).fee()
```

```
function fee(account, units, tariff)
    return account.rate * units + tariff.fixedFee

monthly = fee(account, units, tariff)
```

## Source

- [[fowler-refactoring]], ch. 11, Replace Function with Command, PDF pp. 376-383, and Replace Command with Function, PDF pp. 384-388: the definition, the facilities, the 95% preference and its cost, the two senses of "command", nested functions as alternative, both mechanics.
- Ch. 3, "Long Function", PDF p. 88: Replace Function with Command as the heavy artillery when temps and parameters remain.
- This wiki's own: the signs as worded, as Fowler's motivations restated as shapes in code (the book's example is deliberately too short to need the refactoring, PDF p. 378), the assignment against [[routine-length]] and the shared selection with [[replace-temp-with-query]] and [[extract-routine-to-name-a-step]], the preference for a closure when no direct test is needed, the *Elegant Objects* limit, and the pseudocode pair, after the book's charge example.
