---
title: "Barricade: validate at the boundary, assume inside"
category: errors
summary: "Raw external values reach internal routines unchecked (including a server handler that stores a request field because the client form already checked it), or the opposite: private helpers re-validate and repair the same parameter the public entry already checked, so no one place is the boundary of trusted data."
tags: [rule, defensive-programming, validation, boundaries]
paradigm: any
sources: [code-complete, object-oriented-thought-process, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

A barricade is a deliberately placed boundary in the code: data is checked where it crosses into a "safe" region, and code inside the region treats it as already clean. McConnell compares it to sealed compartments in a ship's hull and to a fire wall (p. 198).

## Rule

The book asks the designer to choose which routines sit outside the barricade, which inside, and which act as its doors, and to validate at the doors: «Проверяйте корректность данных, пересекающих границу безопасной области» (pp. 198-199). Where the barricade runs between subsystems is architecture, and this wiki takes it as given from the project's conventions or brief. Inside a module this page asks that one call path have one door that validates, with code behind it that assumes. The same holds within one class: its public methods treat incoming data as unsafe and are responsible for checking and correcting it, and its private methods may assume it is safe (p. 199). The book's analogy is an operating theatre: everything is sterilised before it comes in, and the design question is what goes inside, what stays outside, and where the doors are (p. 199).

The barricade also decides the tool. Routines outside it use error handling, because no assumption about the data is safe; routines inside use assertions, because a bad value there is «ошибкой в программе, а не в данных» (p. 200). Which code is inside is, in the book's words, decided at the level of architecture (p. 200); this page applies the rule along the path in view once that decision is made.

The simplest form checks external data as it arrives, but data often needs checking at several levels, so a barricade may be layered (p. 199). External data means anything from a file, a user, the network or any other external interface: check ranges, that numbers have allowed values, that strings are short enough to process, and that a value from a fixed set (such as a transaction id) is valid here (p. 183). For hostile input (buffer overflow, injected SQL, HTML or XML, integer overflow, data passed to system calls), see [[distrust-external-input]].

The reasoning: without a barricade, every routine must validate everything, and the book warns that checking parameters everywhere and in every way makes a program large, slow and more complex, and the extra code carries defects of its own (p. 206). This wiki reads the book's figure of the barricade (p. 199, fig. 8-2) as the answer to that cost: most of the program is freed from validation.

Fowler's *Refactoring* draws the same line from the testing side. If the input comes from an external source, such as an encoded request, validation checks are needed and should be tested. If it comes from a trusted source, such as another part of the same codebase, there may be valid reasons to leave it unchecked (PDF p. 115): "lots of validation checks between modules in the same code base can result in duplicate checks that cause more trouble than they are worth, especially if they duplicate validation done elsewhere" (2nd ed., ch. 4, Probing the Boundaries, PDF p. 115). Inside, where a bad value could let corrupt data spread and cause failures that are hard to debug, he might add an assertion to fail fast, and he does not write tests for assertion failures, "as they are themselves a form of test" (PDF p. 116).

### The door is on the side that owns the data

Weisfeld's *The Object-Oriented Thought Process* adds where the door must stand when the caller runs code the system does not control. Its example is an `Age` field on a web registration form. Without validation the server writes whatever Mary typed, so even a wrong value «попадет в базу данных» (p. 249). With validation, the server's code checks the range, and the database may check it too (p. 249). The client never reaches the database directly: anyone can run a browser, so the client asks the server for each operation (p. 249). A sidebar makes the rule explicit: «валидация должна проводиться на обеих сторонах для всех веб-приложений», because a client can send its results straight to the server past its own validation, or switch the client script off (p. 250). The book also lists what a round trip to the server costs (time, network traffic, server resources, more chance of error) and sets the aim of doing most validation on the client (p. 250).

This wiki reads the two statements together: the client check is for responsiveness, and the check on the side that owns the data is the guarantee. Neither replaces the other. In this page's terms a client is always outside the barricade, and a check that runs only in client code is no door.

## Sign in code

- A value read from a request, file, socket or user flows into internal routines that neither check it nor are documented as requiring it, and no routine on the path checks it.
- The opposite shape: a public method validates a parameter, and the private helpers it calls validate and repair the same parameter again with their own error handling. Where the repeated check carries the same reaction at each level, [[caller-owns-the-precondition]] owns the shape; this page supplies its repair.
- A handler or service method receives a request field and passes it to storage or a state change with no check of range, format or presence, while a check of the same field exists only in client code (a form script, a mobile view), or a comment or name on the server defers to it ("validated by the form", `trustedAge`).
- Internal routines contain user-facing error handling (prompts, messages, fallbacks) for values that only a bug inside the program could produce.

This wiki assigns the neighbouring cases as follows. User-facing handling for a value already checked at a door on the same path is [[barricade]]; user-facing messages composed in domain code for a real failure are [[consistent-error-handling-strategy]]. Peer modules of one layer of which one validates its input and its peer does not is [[consistent-error-handling-strategy]]; this page owns the line between outside and inside along one path. Input that crosses the door still as raw text is [[convert-input-at-entry]]. A clamp or default of an argument already checked upstream on the same path is [[barricade]]; one with no check upstream is [[caller-owns-the-precondition]]. A missing or misnamed required field of a structured document from another system is [[validate-exchanged-data-against-a-declared-schema]]; the range or format of a present value, and where on the path the check stands, is [[barricade]].

## When not to apply

- A program too small to have an inside: a script that reads input and computes in one routine needs one check, not a designed boundary.
- Data that changes meaning between layers. A layered barricade is then correct: each layer validates what it newly depends on, and this is not duplication (p. 199).
- A database constraint that enforces the check and whose violation the handler reports as an error is a door (p. 249); the rule then holds for the constraint, not for code in the handler.
- This wiki adds: a library whose internal routines are also public entry points for other callers has more doors than one, and each public entry is a door.
- This wiki adds: a client that runs in a process the system controls and that owns the data, such as a desktop application over a local store, is not outside the barricade. The client-only sign applies where users can run or alter the client.
- This wiki adds: a framework or schema layer that rejects the request before the handler runs is the door, and the handler behind it is inside.

## Repair

Take the entry points from the project's structure; on the path in view, put validation and the reaction to bad data at the first one. Behind them, replace re-validation with assertions that document the assumption ([[assertion-or-error-handling]]). Make the helpers that assume clean data private, so that nothing bypasses the door. Convert the input to its proper type at the door ([[convert-input-at-entry]]). Where a client also checks the value, keep its check for fast feedback, and where the project already shares code between client and server, use one definition of the rule on both sides so the two checks cannot drift apart.

## Before and after

```
# before
function handle_order(request):
    save_order(request.get("quantity"), request.get("sku"))

function save_order(quantity, sku):
    if not is_number(quantity) or quantity <= 0:
        show_error("bad quantity")
        return
    reserve(quantity, sku)

function reserve(quantity, sku):
    if quantity <= 0:
        quantity = 1
    stock.take(sku, quantity)
```

```
# after
function handle_order(request):            # door of the barricade
    quantity = parse_positive_int(request.get("quantity"))
    sku = parse_sku(request.get("sku"))
    if quantity is failure or sku is failure:
        return reject(request, "quantity and sku are required")
    save_order(quantity, sku)

private function save_order(quantity, sku):  # inside
    assert quantity > 0
    reserve(quantity, sku)

private function reserve(quantity, sku):
    assert quantity > 0
    stock.take(sku, quantity)
```

A check that exists only on the client:

```
# before
# client
on submit(form):
    if form.age < 0 or form.age > 150:
        show "invalid age"; return
    send("/register", form)

# server
function register(request):
    record = customers.find(request.customer_id)
    record.age = request.age
    customers.save(record)
```

```
# after
# shared
function check_age(age):
    if age is not integer or age < 0 or age > 150:
        return failure("age out of range")
    return ok(age)

# client
on submit(form):
    result = check_age(form.age)
    if result is failure: show result.message; return
    send("/register", form)

# server: the door
function register(request):
    result = check_age(request.age)
    if result is failure:
        return bad_request(result.message)
    record = customers.find(request.customer_id)
    record.age = result.value
    customers.save(record)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 183 for checking external data, pp. 198-200 for the barricade and its relation to assertions, p. 206 for the cost of excess checks. Taking the barricade's place between subsystems as given from the project, and applying the rule along one call path, is this wiki's reading. The reading of the figure as the answer to that cost, the signs, the split with neighbouring pages, the limits other than the layered case, the repair and the example are this wiki's own. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 13: the `Age` form, the client not touching the database, server and database checks (p. 249); both-sides validation, the client bypassing its own check, the cost of round trips and the aim to validate mostly on the client (p. 250). The quotations were checked against `raw/`. This wiki's own for that part: the reading of the client check as responsiveness and the server check as the guarantee, the client-only sign, the constraint limit as worded, the controlled-client and framework-door limits, the splits with [[caller-owns-the-precondition]] and [[validate-exchanged-data-against-a-declared-schema]], the shared-definition repair and the second pair.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 4, "Probing the Boundaries", PDF pp. 115-116: validation for external input and its tests, duplicate checks between trusted modules, assertions inside, and no tests for assertion failures.
