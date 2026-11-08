---
title: Throw exceptions at the interface's level of abstraction
category: errors
summary: "A domain-level method declares or lets escape a low-level exception from its implementation (an end-of-file, socket, SQL or disk error from a getter like get_tax_id), so callers depend on how the class stores its data."
tags: [rule, exceptions, encapsulation, abstraction, wrapping]
paradigm: any
sources: [code-complete, larman-applying-uml-and-patterns]
created: 2026-11-06
updated: 2026-11-07
---

An exception thrown out of a routine is part of its interface, just like the data types it uses; the interface of a class should present one coherent abstraction (p. 194; see [[class-interface-coherent-abstraction]]).

## Rule

When passing an exception on, make sure its level of abstraction matches the routine's (p. 195). The book's counter-example is an `Employee` class whose `GetTaxId()` declares `EOFException`: it exposes an implementation detail and ties client code not to `Employee` but to the code inside it that throws the end-of-file error. «Инкапсуляция нарушена, управляемость кода ухудшается.» (p. 195). The repair throws an exception that belongs to the class's interface, `EmployeeDataNotAvailable`, with the handling inside `GetTaxId()` perhaps just mapping a disk-not-ready exception onto it, which preserves the interface's abstraction (p. 195).

Larman's *Applying UML and Patterns* records the same rule as the pattern **Convert Exceptions** [Brown01], also known as Exception Abstraction [Renzel97]. His case: a `java.sql.SQLException` from the persistence code should not travel up to the presentation layer, because "It is at the wrong level of abstraction" (35.3, p. 791). The pattern: "Within a subsystem, avoid emitting lower level exceptions coming from lower subsystems or services. Rather, convert the lower level exception into one that is meaningful at the level of the subsystem. The higher level exception usually wraps the lower-level exception, and adds information" (p. 791). He adds at once: "This is a guideline, not an absolute rule" (p. 791). The conversion repeats at every boundary: the persistence code catches `SQLException` and throws `DBUnavailableException`, which holds it; the product-information adapter catches that and throws `ProductInfoUnavailableException`, which wraps the database one (p. 791). Each level converts only when it "can't handle it" (p. 791). Which layers and subsystems exist is the project's architecture, taken as given; this page applies the rule at the interface of a class. The names in his chain follow [[name-exceptions-after-the-problem-not-the-thrower]]; the terms for cause, detection and denied service are on [[fault-error-failure]].

## Sign in code

- A method named in domain terms whose signature declares, or whose documentation lists, an exception from the storage, transport or parsing layer it happens to use.
- Callers of a domain object catch I/O, network or database exception types around calls that are not themselves I/O.

This wiki assigns the neighbouring cases as follows. A catch that translates but drops the caught exception as cause is [[chain-exceptions]]. A third-party product's exception type in any signature or catch outside the adapter's body, the adapter's own signatures included, is [[hide-third-party-apis]]; an exception of the standard library or of the project's own lower code escaping a class's interface is [[exception-at-the-interface-abstraction]].

## When not to apply

- A routine whose abstraction is the low-level operation itself: a file reader may throw end-of-file.
- A thin adapter whose whole contract is to expose the wrapped library unchanged.
- The code can handle the failure where it happens (retry, fall back, use a default). Then it should handle it, not convert it. Larman calls handling an exception near the level at which it was raised laudable but difficult, "because the requirement for how to handle an error is often application-specific" (35.3, p. 791).
- A thin pass-through helper that is not the boundary of any abstraction gets no exception type of its own. Converting at every method, rather than at each abstraction boundary, multiplies types and wrapping. This limit is this wiki's own; Larman's chain converts once per layer.
- Larman leaves checked versus unchecked exceptions aside, because not every popular OO language has them (35.3, p. 791). Whether a converted exception is checked is decided by the project's language and conventions; [[chain-exceptions]] holds *Elegant Objects*' position on it.
- Translating does not mean discarding. Larman: the higher-level exception usually wraps the lower one (p. 791); keep it as the cause of the new one ([[chain-exceptions]]).

## Repair

Define an exception in the vocabulary of the class's interface. Catch the low-level exceptions at the class boundary and throw the interface exception, passing the original as its cause. Update callers to catch the new type.

## Before and after

```
# before
class Employee:
    function tax_id() -> TaxId throws EndOfFile, DiskNotReady:
        return parse_tax_id(record_file.read_field("tax_id"))
```

```
# after
class Employee:
    function tax_id() -> TaxId throws EmployeeDataNotAvailable:
        try:
            return parse_tax_id(record_file.read_field("tax_id"))
        catch EndOfFile, DiskNotReady as low_level:
            throw EmployeeDataNotAvailable("tax id", self.id, cause = low_level)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: pp. 194-195 for the rule, the Employee example and its repair. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.3 "Handling Failure", PDF pp. 790-791: the Convert Exceptions pattern and its other name, the SQL / DBUnavailable / ProductInfoUnavailable chain, "a guideline, not an absolute rule", converting only what a level cannot handle, the remark on handling near the source, and leaving checked exceptions aside, and wrapping the lower exception. The signs, the split with neighbouring pages, the limits other than Larman's, applying his subsystem-level pattern at a class interface, and the pseudocode are this wiki's own.
