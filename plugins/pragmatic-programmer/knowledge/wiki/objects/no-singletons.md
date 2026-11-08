---
title: No singletons
category: objects
summary: "A class declares a static INSTANCE of its own type, a non-public constructor and a static getInstance() (or setInstance() for tests): it is a global variable; create the object once where the application is assembled and pass it through constructors."
tags: [rule, singleton, global-state, dependency-injection, encapsulation, gof, lazy-initialization]
paradigm: oop
sources: [elegant-objects, pragmatic-programmer, object-oriented-thought-process, larman-applying-uml-and-patterns]
created: 2026-11-03
updated: 2026-11-07
---

Bugayenko calls the Singleton pattern a terrible anti-pattern and says the rule against it has no exceptions (*Elegant Objects*, section 3.2, pp. 133, 138). His argument proceeds by comparing it with a utility class (see [[no-static-methods]]).

## Rule

Do not use singletons. Everything a class needs to work is passed through its constructor and encapsulated in the class; an object touches nothing but its encapsulated properties (p. 137). The book's example: if most classes must know the logged-in user, encapsulate the user into every object that needs it (p. 137).

**Singleton versus utility class.** The usual answer to "why a singleton rather than static methods" is that a singleton encapsulates state. The book rejects this: a utility class with a static field holds the same state, and the two are equivalent (pp. 134-135). The answer the author accepts is that a singleton is a dependency that can be broken, because a `setInstance()` can sit beside `getInstance()` and a test can install a fake, while a utility class is a hard-coded coupling that cannot be broken at all (pp. 135-136). So a singleton is better than a utility class, but still bad (p. 136). This wiki reads that as the discriminating criterion between the two shapes: both are global; only the singleton can be replaced, and only by mutating global state.

**Why it is still wrong.** Logically and technically a singleton is a global variable, «ни больше, ни меньше» (p. 136). The book's position is that OOP has no global scope and that global variables violate encapsulation (pp. 136-137); the static method is what makes the trick possible in a language that forbids globals (p. 137).

This wiki adds what the book's test example implies: replacing the instance through `setInstance()` changes it for every user in the process, so tests that do this interfere with each other unless each one restores it.

**The pattern as Weisfeld teaches it.** *The Object-Oriented Thought Process* takes the opposite stance and picks Singleton as its example of a creational pattern. The class «регулирует создание объектов»: however often it is asked, only one object exists (p. 292). The example is a site-visit `Counter`, where every visit should increment one shared counter (p. 290). The book grounds the class-controlled form in the principle «что объект должен отвечать за себя», so that lifecycle questions are settled inside the class and not left to language constructs such as `static` (p. 290). In the same passage it grants that an external factory (Factory, Abstract Factory, Bridge) is often useful or even necessary (p. 290). Several references to the one object are allowed, and every reference sees a change made through any other: after two increments through `counter1` and one through `counter2`, both read 3 (pp. 292-293). This wiki notes a tension the book leaves open: its listing does the regulating through a static field and a static `getInstance()` (p. 291), so its principle holds only in the sense that the class, not its callers, owns the decision.

This wiki observes, and the book does not say, that in concurrent code the lazy form (`if instance == null then instance = new ...`, Weisfeld's listing, p. 291) can create two instances under simultaneous first calls: one more reason for creating the instance once at the assembly point.

**The pattern as Larman uses it.** Larman's *Applying UML and Patterns* uses Singleton to give global access to one factory instance: "Define a static method of the class that returns the singleton" (26.5, p. 608). His reason is convenience: passing the instance as a parameter, or storing a reference in every object that needs it, is "possible but inconvenient" (p. 608). Given that choice, he makes two decisions about how it is built:

- **Instance methods behind `getInstance`, not a class of static methods** (p. 611). Static methods "are not polymorphic (virtual) and don't permit overriding in subclasses in most languages"; remote-call mechanisms usually support only instance methods; and "A class is not always a singleton in all application contexts", since it is not uncommon to start out thinking an object will be a singleton and then discover a need for multiple instances in the same process, so "the instance-side solution offers flexibility." This wiki notes that his first and third reasons overlap those [[no-static-methods]] gives against utility classes.
- **Lazy initialization, guarded under threads.** He prefers lazy creation because creation work, and perhaps holding expensive resources, is skipped if the instance is never used, and because the creation logic is sometimes complex and conditional (pp. 610-611). In multi-threaded code "the creation step of the lazy initialization logic is a critical section requiring thread concurrency control" (p. 610).

This wiki resolves Weisfeld's goal and Larman's convenience against *Elegant Objects*' ban per setting, and the resolution is the one under *When not to apply*. Where one instance is a fact of the problem (one device, one process-wide registry), Weisfeld's goal holds, and *Elegant Objects*' repair still serves it: create the one instance at the assembly point and pass it in. Where a project convention or framework keeps a static access point (the limit below), Larman's two decisions apply, as repair step 4 says. The class-controlled static accessor is reported in either case, because the shared mutable state that the book's own output shows (p. 293) is reached by every caller that names the class.

## Sign in code

- A class holding a static field of its own type and a static accessor returning it, with a non-public constructor, the instance created eagerly or on first call (p. 133; the lazy, protected-constructor form is Weisfeld's listing, p. 291).
- A class offering a static `setInstance(...)` beside the accessor, so tests can swap it (p. 136).

This wiki assigns the neighbouring cases as follows. This page owns the declaration of a singleton. A method body that reaches `X.getInstance()`, and a test that calls `X.setInstance(fake)` or otherwise assigns global state before it can run, are [[global-data]], whose repair is the same: pass the object in. A class made only of static methods, with or without a static field, is [[no-static-methods]]. A lazy `getInstance` whose `if instance == null` check and assignment are not atomic, in code several threads run, is [[check-then-act-must-be-atomic]] for the race; this page owns the declaration.

## When not to apply

*Elegant Objects* allows no exception (p. 138). *The Pragmatic Programmer* cautions (p. 75); *Elegant Objects* bans (pp. 136-138). This wiki resolves it: a singleton that holds state or reaches resources is reported (its declaration on [[no-singletons]], the reach on [[global-data]]). A stateless class reached through a static accessor still carries the declaration sign of [[no-singletons]]. A single instance created at the entry point and passed through constructors, or managed by a container that injects it, is neither page's sign. An immutable stateless instance exposed as a constant (a null object, a comparator) carries no hidden input and is outside both.

The limits below are this wiki's:

- A container or framework that manages one shared instance and injects it through constructors is not this shape: the class receives the object, it does not reach for it, and no static accessor is declared.
- A project convention or a framework that requires a static entry point (an application's main object, a platform callback registry) governs at that boundary; keep the static reach to that one place.
- A singleton the language itself provides (an object declaration, a module) is a language question decided at work time.

## Repair

1. Add a constructor parameter for the dependency to each class that calls `getInstance()`, store it in a field, and use the field.
2. Create the single instance once, where the application is assembled, and pass it down.
3. Remove the static field and accessor once no caller remains.
4. Where a static access point stays because the project's convention or framework requires it, build it as Larman does (26.5, pp. 610-611): one static `getInstance` returning an instance whose services are instance methods, and creation made atomic with the language's lock or once-only mechanism, or eager where creation is cheap and unconditional. The eager alternative is this wiki's reading; Larman only says lazy is "usually preferred".
5. If the constructor parameter list grows too long because a class needs the database, the current user, command-line arguments and more, the book says the class is too big and not cohesive enough, and should be made smaller (pp. 137-138). See [[keep-objects-small]].

## Before and after

```
class CurrentUser
  static INSTANCE = new CurrentUser()
  private constructor()
  static getInstance() return INSTANCE
  name()

class Greeting
  text()
    return "Hello, " + CurrentUser.getInstance().name()
```

```
interface User
  name()

class CurrentUser implements User
  constructor(name)
  name()

class Greeting
  field user: User
  constructor(user)
  text()
    return "Hello, " + this.user.name()

// where the application is assembled
greeting = new Greeting(new CurrentUser(loginName))
```

## Source

- [[elegant-objects]], section 3.2, subsection on the Singleton pattern, pp. 133-138: the shape, the equivalence with a stateful utility class, the breakable dependency as the only real advantage, `setInstance` for tests, singleton as a global variable, constructor encapsulation as the replacement, too many dependencies as a sign of a class too large, no exceptions. The quotation of p. 136 was checked against the page image.
- [[pragmatic-programmer]], p. 75: the caution on singletons that the resolution weighs against this book's ban.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 15: the `Counter` example, self-responsibility and the factory concession (p. 290), the listing (p. 291), creation control and several references (p. 292), the shared output (p. 293). The quotations were checked against `raw/`. This wiki's own for that part: the tension with the static listing, the per-setting resolution and the concurrency observation.
- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.5, PDF pp. 608-611: Singleton for a factory, the convenience reason, instance methods over static with three reasons, lazy creation preferred, the critical section. This wiki's own for that part: the resolution against *Elegant Objects*, the link to [[no-static-methods]], the owner line with [[check-then-act-must-be-atomic]], and the eager alternative in repair step 4.
- This wiki's own: the discriminating reading of breakable versus hard-coded, the test-interference observation, the split of signs with [[global-data]] (including the stateless-accessor case), the widened constructor sign, the resolution with *The Pragmatic Programmer*, the limits, the repair steps 1-3, the pseudocode.
