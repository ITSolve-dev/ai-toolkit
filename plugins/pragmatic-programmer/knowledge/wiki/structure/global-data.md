---
title: Global data
category: structure
summary: "A function's body reaches a non-constant module-level name, static field, singleton accessor or `Config.x`, or calls a database, file system or service directly, or an instance method or static setter assigns a static field that every instance reads, so its dependencies are hidden from the signature and its test must first build a global environment; also a global passed as an argument to a routine that writes it by name (aliasing), intermediate results stored in a global, or one oversized context object passed to every routine."
tags: [rule, coupling, global-state, singleton, dependency-passing, external-resources, access-routines, aliasing, tramp-data]
paradigm: any
sources: [pragmatic-programmer, elegant-objects, code-complete, object-oriented-thought-process, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Global data is any data reachable from everywhere, whatever it is wrapped in; the book speaks of data and not variables on purpose (p. 174). The book calls it an insidious source of [[coupling]], because each piece behaves as though every method in the application had suddenly gained an extra parameter (p. 173). It also lists avoiding it among the practices that keep a system [[orthogonality|orthogonal]] (p. 75).

*Code Complete* (section 13.3) adds a catalogue of how global variables fail, the cases where it accepts them, and a ladder of alternatives that ends in access routines. It treats a class field used by several methods of that class as **not** global, and warns against calling such fields global data (Russian edition, p. 326); when such fields start to behave like globals is [[class-data-versus-global-data]].

## Rule

«Избегайте глобальных данных» (p. 174). Pass the context a module needs explicitly: each reference to global data binds the code to the other components sharing it, and explicit context makes code easier to understand and maintain (p. 75). If data truly has to be global, put it behind an API: «Если данные настолько важны, чтобы быть глобальными, заключите их в оболочку API» (p. 175).

The book gives two reasons, and says the second shows in unit tests (p. 174):

- Changing how the global is implemented can touch all the code. The book says the real effect is usually limited, and the true problem is knowing every place that must change.
- It blocks extraction. Code made reusable has a clear interface, so a method or module can be taken out without dragging the rest along, and global data defeats that. This shows up in tests, since a unit test must write a good deal of setup just to create a global environment.

*Code Complete* reaches the same rule by a ladder: declare every variable local first, widen it to a private or protected class field only when another routine needs it, and make it global only once that turns out to be required (p. 330). Where data has to stay global, reach it only through access routines: «Все, что вы можете сделать с глобальными данными, вы можете сделать лучше, используя методы доступа.» (p. 331). It lists six failures, each with something specific that breaks (pp. 327-329):

- **Unintended change.** A routine changes a global its caller assumed stable. The book's example averages `theAnswer` with `GetOtherAnswer()`, which quietly rewrites `theAnswer`, so the average is wrong.
- **Aliasing.** A global passed by reference to a routine that also writes the global under its own name gives one variable two names. In the book's `WriteGlobal(globalVar)` both message boxes print 5.
- **Re-entrancy.** Multithreaded code can reach the same global from several threads at once.
- **Reuse.** A class that reads globals cannot be moved to another program. The book says the right repair is to change the old class so it stops using them, and the wrong one is to recreate the same globals in the new program, which spreads them «как вирус» (p. 328).
- **Initialisation order.** In some languages the order in which globals in different files are initialised is undefined, so one global initialised from another is unpredictable.
- **Modularity.** «Глобальные данные проделывают дыры в возможности модуляризации.» (p. 329) A reader cannot think about one routine without every other routine that touches the same globals.

The term is deliberately broader than mutable global variables, and it has three extensions in this book, and a fourth from *Elegant Objects*.

**Read-only data.** «Даже глобальные переменные, предназначенные только для чтения, могут привести к осложнениям» (p. 75). The book's example is code that suddenly has to become multithreaded.

**Singletons.** Many developers use them as global variables, particularly where the language has no other form of global, and they can bring needless coupling (p. 75). «Синглтоны также являются глобальными данными» (p. 174). A singleton exporting instance variables is global data, «просто с более длинными именами» (p. 174).

**External resources.** «Любой изменяемый внешний ресурс считается глобальными данными.» (p. 175) The book lists a database, a data store, the file system and a service API.

**The class that encapsulates nothing.** *Elegant Objects* reaches the same shape from the object side (section 2.2). A class with no fields still has behaviour, and with no fields that behaviour can only come from static or global calls: «Класс без свойств похож на статический метод» (p. 47). The book's example is a `Year` whose `read()` divides `System.currentTimeMillis()`. Its rule is that every object that does something encapsulates the objects it works with: «Мы всегда должны что-то инкапсулировать, за исключением тех случаев, когда объект ничтожен или близок к таковому.» (p. 48). A trivial object is one with no coordinates in the universe; the book's example is `Universe`, which could exist only once and which the author sees no practical reason to write (pp. 48-49). By the book's own rule that state is identity ([[keep-objects-small]]), all instances of a stateless class are equal to each other. The author admits the case is partly philosophical: such objects can be written and are common, and he calls them wrong from both a philosophical and a practical point of view (p. 48).

**Static attributes.** Weisfeld's *The Object-Oriented Thought Process* reaches global data first from the structured side: data separated from procedures and often global is easy to change from outside the code's scope, its access is uncontrolled and unpredictable, and with no control over who reaches it testing and debugging become much harder (p. 24). A side box claims that a properly designed object model has no global data at all (p. 24), and a box in chapter 5 repeats it: static attributes and methods are shared by the objects of one class and are not reachable by other objects (p. 108). Inside objects, a class (static) attribute is one block of memory shared by every instance, which Weisfeld calls «почти настолько близко к глобальным данным, насколько представляется возможным при объектно-ориентированном проектировании» (p. 82). An object attribute is different: «Изменение значения атрибута count объекта number1 никоим образом не повлияет на копию count в объекте number2 или number3» (p. 81). His warning about the static one: «вам следует знать о возможных проблемах синхронизации» (p. 82). In his example two `Count` objects share a static `count`, one counting pixels and one sheep: «В тот момент, когда Count2 запишет данные о первой овце, информация, сохраненная Count1, будет потеряна» (p. 83). In chapter 4 he adds that 500 `Cabbie` objects still hold a single static `companyName` (p. 91), and «Если атрибут является статическим, а класс обеспечивает для него сеттер, то любой объект, вызывающий этот сеттер, будет изменять единственную копию» (p. 96). This wiki reads a writable static attribute as global data scoped to a class: any instance changes what every other instance sees. Weisfeld allows that class attributes have legitimate uses without naming them (p. 82). This wiki adds that a static field shared on purpose, such as an instance counter, is still global data and goes behind access routines, and that where concurrent code writes it [[shared-state-is-incorrect-state]] owns it.

**Fowler's account.** Fowler's *Refactoring* counts **Global Data** among the most pungent smells, for one reason: "The problem with global data is that it can be modified from anywhere in the code base, and there’s no mechanism to discover which bit of code touched it" (2nd ed., ch. 3, Global Data, PDF p. 89). The resulting bugs are a "spooky action from a distance" whose source is hard to find, and the smell covers global variables, class variables and singletons alike (PDF p. 89). His first move is always Encapsulate Variable, because once all access goes through a function, the places that modify the data can be seen and access can begin to be controlled (PDF p. 89). He grades the harm by amount: small doses can be got away with, but global data "gets exponentially harder to deal with the more you have", and even small doses he keeps encapsulated (PDF p. 89).

## Sign in code

- A function body reads or writes a name that is not a parameter, a local, a field of its own object or a compile-time constant: a module-level variable, a static field, `Singleton.instance().field`, `Config.level`.
- A function obtains a collaborator through a global accessor such as `X.instance()` inside its body.
- A static, non-constant field assigned by an instance method or by a public setter (`static count` incremented in `increment()`, `static companyName` beside `setCompanyName(v)`), so instances used for different purposes overwrite each other's value (Weisfeld, pp. 83, 96).
- A class declares no instance fields while its methods call the system clock, the environment, a singleton or a static utility. *Elegant Objects* names this shape (p. 47).
- A function calls a database driver, the file system or a service client directly, with no project-owned wrapper in between.
- A test assigns to global state, or starts an environment, before it can call the function under test.
- A call passes a module-level variable as an argument to a routine whose body also names that variable directly (*Code Complete*'s aliasing, p. 328).
- A module-level variable is assigned an intermediate value partway through a computation, before its final value (p. 334).
- One large object or record is a parameter of most routines in a module, and each routine uses a different few of its fields. *Code Complete* counts it as global data in disguise (p. 335).
- All the program's globals sit in one module or class behind one set of get/set routines, unrelated to each other (p. 332).

This wiki assigns the neighbouring cases as follows. This page owns a function with an input its signature does not show. A value the callee could derive from another of its parameters or from its own object is [[parameter-or-query]], which also gives the stepwise mechanics for passing a global in as a parameter. Whether the routine should touch global data at all is [[global-data]]; a global access that stays, under a project convention or within this page's limits, and that the header does not name is [[routine-header-comment]]. Where the complaint is that many sites spell configuration's key paths or names, [[configuration-behind-a-thin-api]] owns it. Where a reusable module assumes something about its surroundings, even at one site, [[do-not-rely-on-unguaranteed-context]] owns it. A test that patches a global before it can run stays here, and [[test-is-first-client]] sends it here. A test that patches a member to substitute a collaborator belongs to the page that owns the patched shape: a static method is [[no-static-methods]], new inside a method is [[new-only-in-secondary-constructors]], a static field or singleton is [[global-data]], and a final or non-overridable method of a collaborator typed by a concrete class is [[public-methods-implement-interfaces]]. A test double that scripts or verifies calls on a collaborator through a mocking library, with no member patched, is [[prefer-fakes-over-mocks]]. A function whose parameter names the source, such as a file name, and which opens it for a computation is [[process-values-not-their-source]]. A hidden input where a sign of [[hide-third-party-apis]] fires is that page's, and the repair is the same: pass in a wrapper. The program's own legacy code or a non-portable platform API spread over modules is [[isolate-volatile-dependencies-behind-a-layer]]. Every other hidden input, and a single such call, stays here, vendor or not, including the language's own file system and the project's own service clients. A module-level field that concurrent code writes is [[shared-state-is-incorrect-state]]. A class that declares a static instance of itself is [[no-singletons]]; the body that reaches that instance stays here. A read of the wall clock is [[test-is-first-client]], whatever its syntax, except a zero-field class whose methods read the clock, which is [[global-data]] (*Elegant Objects*' `Year`). Any other static call is decided by whether it reaches a mutable external resource ([[global-data]]) or not ([[no-static-methods]]). A call that reaches a mutable external resource (file system, database, network, service) is [[global-data]] whatever its syntax, static or not. [[no-static-methods]] owns static calls to computation that reaches no external resource. A public constant or enum read by classes that each wrap it, or passed in to select behaviour, is [[no-public-constants]]. A mutable or run-time-loaded static value is [[global-data]]. A hidden "current instance" chosen through a module's own select call is [[adt-instances-without-classes]]; the fields of one large class shared by dozens of its methods are [[class-data-versus-global-data]]. A static method declared is [[no-static-methods]]; a collaborator built with `new` inside the class that uses it is [[new-only-in-secondary-constructors]]. I/O or a call to a global service inside a constructor body belongs to [[constructors-without-code]]; the same call inside a method belongs to [[global-data]]. The order in which to narrow a declaration that is wider than its uses is [[smallest-scope-first]]. Access routines named after the implementation, or mixed with direct access to the same data, are [[access-routines-at-domain-level]]. Fields of a structure with no routines of its own written from several call sites: [[replace-direct-data-manipulation-with-adt]]. A structure made global so routines can reach it is [[global-data]]. The oversized context object passed everywhere stays here; [[group-related-data-into-a-structure]] defers to this page whenever a structure is passed to routines that each use a different subset of it. A wrapper around an external resource has one implementation as a rule, and that is not the sign of [[know-when-to-stop]]: that page counts layers around the application's own code and leaves this shape here. The cases of semantic coupling: a documented call the caller skips, or another class's constant it borrows, because it knows the implementation belongs to [[semantic-encapsulation-violation]]; a reliance on runtime type to [[avoid-introspection-and-casting]]; on shared mutable state to [[global-data]]; a reliance on what the callee does with a value the caller passes belongs to [[semantic-coupling]].

## When not to apply

The book's rule has a built-in exit: data important enough to be global stays global behind an API. The rule then becomes a requirement on access, and not a ban. It also says to use singletons carefully and does not ban them (p. 75). *The Pragmatic Programmer* cautions (p. 75); *Elegant Objects* bans (pp. 136-138). This wiki resolves it: a singleton that holds state or reaches resources is reported (its declaration on [[no-singletons]], the reach on [[global-data]]). A stateless class reached through a static accessor still carries the declaration sign of [[no-singletons]]. A single instance created at the entry point and passed through constructors, or managed by a container that injects it, is neither page's sign. An immutable stateless instance exposed as a constant (a null object, a comparator) carries no hidden input and is outside both. The further limits are this wiki's own:

- A true constant that never varies at run time and carries no behaviour, such as a mathematical value, couples nothing that could change. The extra hidden parameter the book describes then carries no information. Read-only data loaded at run time does not qualify, given the book's caution on p. 75. Fowler draws the same line: global data "that you can guarantee never changes after the program starts is relatively safe—if you have a language that can enforce that guarantee" (*Refactoring*, PDF p. 89). This wiki reads his condition as part of the limit: a value only documented as never changing, with nothing in the language enforcing it, still carries the sign.
- A static constant, or a class-wide value set once at start-up by one owner and written by no instance afterwards, as Weisfeld's `companyName` is used with only a static getter (pp. 91, 96). The sign is the instance-reachable write, not the static keyword. This reading is this wiki's own.
- Weisfeld's absolute, no global data in a properly designed object model (pp. 24, 108), is a design ideal and not a sign: this page fires on the signs above, and wrapping a global in a class with a public setter leaves it global (p. 96). This reading is this wiki's own.
- At the program's entry point something has to create the objects and read configuration and resources. Global lookups there are the place from which context is passed down, not a violation.
- Plain functions in a module are not data, so calling them is not covered by this rule.
- A stateless strategy or function object with no configuration, such as a comparator or a pure formatter taking all its input as arguments, calls nothing global, so the sign is absent; the book's "near trivial" exception covers it (p. 48). This reading is this wiki's own.
- The project-owned wrapper itself has to call the driver. That is where the direct call belongs.
- A small script, or code whose whole job is to drive the resource, has no independent logic to shield. A library adopted on purpose as a foundation is judged on [[framework-intrusion]].

*Code Complete* names the cases where it accepts global variables when they are handled carefully (pp. 329-330): data that conceptually belongs to the whole program, such as its current mode or a table every routine reads; standing in for named constants or enumerations in a language that lacks them; a variable that would otherwise appear in nearly every parameter list, which the book adds is usually used by a limited set of routines that can be gathered into a class with it; and **tramp data**, data a routine receives only to hand it to the next one, such as an error-handling object passed down a chain of calls. The book also notes that database records, configuration files and named constants are global data in the broad sense, and that purists who ban all globals overlook this (p. 329). This wiki resolves the three books as follows. *Code Complete*'s accepted cases are still global data, so they go behind access routines or are passed in, and only the true constants are exempt. Tramp data ([[tramp-data]]) is a real cost, but this wiki does not count it as a reason to make data global; the book's own repair for frequently used data, gathering the routines into a class with the data, applies here too.

## Repair

From weakest to strongest:

1. Hide exported fields behind methods. The book calls this better, because representation can now change while the old form is converted for compatibility. It also warns that there is still only one set of configuration data (p. 174), so this step addresses representation and not the sharing itself. For configuration, see [[configuration-behind-a-thin-api]].
2. Wrap an external resource in code you control (p. 175). For a vendor's product, see [[hide-third-party-apis]].
3. Pass context as parameters, which makes the hidden parameter visible. In object-oriented code the book suggests passing it to constructors, and elsewhere building structures that hold the context and passing references to them (p. 75).

Fowler's order for data that stays global (*Refactoring*, PDF p. 89): Encapsulate Variable first ([[encapsulate-variable]] gives the mechanics), then narrow the scope by moving the variable and its accessors into a class or module so that only its code can see the data, and, where possible, make it immutable after start-up ([[immutable-objects]]). This wiki notes that encapsulation alone leaves the data mutable and shared; it is the first step, not the end state.

*Elegant Objects* gives the same repair for the stateless class: turn each global or static call into a collaborator taken as a constructor argument and stored as a field, as in `Year(Millis msec)` (p. 49). Its "ideal" version goes further and composes the whole computation out of objects in the constructor, with `read()` only returning the result, a style the book develops later (pp. 49-50).

*Code Complete*'s ladder, for data that is still global (pp. 330-335):

1. Make the variable local; if more routines need it, make it a field of the class those routines belong in.
2. Hide what must remain global inside a class, held once, with routines to read and change it, and require all code outside to use them. In a language without classes, a naming convention that marks globals plus a rule that only access routines touch them does the job.
3. Split the globals by the class each one belongs to, rather than putting them all in one pile.
4. For code still under development, the book suggests a simple check-out/check-in lock in the access routines that reports a second simultaneous user, and says it must be replaced with something more robust before release (p. 332).
5. For the remaining true globals: a naming convention that marks them, an annotated list of all of them, and only final results assigned to them, never intermediate ones (p. 334).
6. If the program does use global data, «делайте это открыто» (p. 335), rather than hiding it inside one oversized object passed everywhere.

Trade-off, as this wiki states it: explicit parameters lengthen signatures and have to be threaded through intermediate calls that do not use them. That is often a useful report of how far the dependency reaches. Access routines add a layer and a class per group of data; *Code Complete* says they pay off even in small programs (p. 334).

## Before and after

Before:

```
config = load_config()

function send_invoice(invoice)
    mailer = Mailer.instance()
    if config.sandbox
        return
    mailer.send(invoice.recipient, render(invoice))
```

After:

```
class InvoiceSender
    constructor(mailer, sandbox)
        this.mailer = mailer
        this.sandbox = sandbox

    function send(invoice)
        if this.sandbox
            return
        this.mailer.send(invoice.recipient, render(invoice))
```

The same repair for an external resource, before:

```
// two hidden inputs, and a test needs a live database and global settings
function monthlyReport(month):
    rows = Database.instance().sales_for(month)
    if Settings.verbose:
        print(rows.count)
    return summarize(rows)
```

After:

```
// the dependencies are visible, and `sales` is a project-owned wrapper
function monthlyReport(month, sales, log):
    rows = sales.forMonth(month)
    log.debug(rows.count)
    return summarize(rows)
```

The zero-field class from *Elegant Objects*, before:

```
class Year
  read(): int
    return System.currentTimeMillis() / MILLIS_PER_YEAR - 1970
```

After:

```
class Year
  constructor(millis: Millis)
    this.millis = millis

  read(): int
    return this.millis.read() / MILLIS_PER_YEAR - 1970
```

Aliasing (*Code Complete*), before:

```
global total

function reset_and_bump(ref value)
    value = 0
    total = value + 5
    print(value, total)      // prints 5, 5: value and total are one variable

reset_and_bump(total)
```

After:

```
class Totals
    private total

    function reset_and_bump()
        this.total = 0 + 5
        return this.total

print(totals.reset_and_bump())
```

A static field written through instances (Weisfeld's pixels and sheep, p. 83), before:

```
class Counter
  static field count = 0
  method increment()
    count = count + 1

pixels = new Counter()
sheep  = new Counter()
sheep.increment()     // also changes what pixels reports
```

After:

```
class Counter
  field count = 0
  method increment()
    count = count + 1

pixels = new Counter()
sheep  = new Counter()
sheep.increment()     // pixels unaffected
```

The oversized context object, before:

```
function print_header(ctx)  -> uses ctx.title, ctx.page
function bill(ctx)          -> uses ctx.customer, ctx.rate
function log_error(ctx)     -> uses ctx.logger
```

After:

```
function print_header(title, page)
function bill(customer, rate)
function log_error(logger)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), via [[pragmatic-programmer]]. Topic 10, p. 75: the case for explicit context, the caution on read-only data and singletons, and repair 3. Topic 28, pp. 173-175: the extra-parameter image, the two reasons, the singleton and external resource extensions, the API exit, and repairs 1 and 2. This wiki's own: the wording of the signs (the test sign rests on p. 174), the assignment of neighbouring cases, the split with [[know-when-to-stop]], the limits listed as its own, the order of the repairs, the trade-off and the pseudocode. Bugayenko, *Elegant Objects*, Russian translation (Piter, 2018), via [[elegant-objects]], section 2.2, pp. 46-50: the stateless `Year`, its comparison to a static method, the trivial-object exception, the injected and the "ideal" `Year`; the book notes its own `Year` arithmetic is incorrect and beside the point. This wiki's own for that part: the zero-field sign as worded, the constructor split with [[constructors-without-code]] and the stateless-strategy limit. McConnell, *Code Complete*, 2nd edition, Russian edition, via [[code-complete]], section 13.3, pp. 326-335: class fields not being global, the six failures and their examples, the accepted uses and tramp data, the local-first ladder, access routines, not piling globals together, the development lock, naming, the annotated list, no intermediate results, and the oversized object. The quotations from pp. 328, 329, 331 and 335 are transcribed from `raw/` and need the page-image check. This wiki's own for that part: the aliasing, intermediate-result, oversized-object and one-pile signs as worded, the splits with [[smallest-scope-first]], [[access-routines-at-domain-level]] and [[group-related-data-into-a-structure]], the resolution against the other two books and the tramp-data reading, and the pseudocode. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 24 (global data in structured programs, testing and debugging, the side box), p. 108 (the box on scope and global data), pp. 80-83 (object against class attributes, the closest thing to global data, synchronisation, pixels and sheep), pp. 91, 96 (one static `companyName`, a setter on a static attribute). The quotations were checked against `raw/`. This wiki's own for that part: the reading of a writable static as class-scoped global data, the static-field sign as worded, the three limits drawn from it, the split with [[isolate-volatile-dependencies-behind-a-layer]] and the `Counter` pseudocode. Related: [[train-wreck]]. Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Global Data", PDF pp. 88-89: the untraceable modification, spooky action at a distance, the scope of the smell, Encapsulate Variable as the first move, narrowing the scope, the enforced-immutability exception and the dose. This wiki's own for that part: the reading of the enforcement condition as part of the constant limit, and the note that encapsulation is not the end state.
