---
title: Hide third-party APIs behind your own layer
category: change
summary: "A vendor's client, query dialect or exception type named outside one adapter class, in code that also holds business logic or in the application's own signatures; application code branching on which vendor is configured, each branch calling a different API; or an adapter that hands the wrapped vendor object back out through an accessor."
tags: [rule, reversibility, third-party, abstraction, coupling, adapter, gof, protected-variations]
paradigm: any
sources: [pragmatic-programmer, object-oriented-thought-process, larman-applying-uml-and-patterns]
created: 2026-11-01
updated: 2026-11-07
---

**Hiding a third-party API** means confining a vendor's product to one adapter class of your own, so that replacing the vendor changes that class and not the code that uses it. Which modules may import the vendor is the project's architecture, taken as given; this page applies inside the code in view. This page concerns where a vendor's calls sit; the shape a product forces on your objects is [[framework-intrusion]].

## Rule

The source's instruction is «скрывайте сторонние API за собственными уровнями абстракции» (p. 81). Its worked case is a database: calls to third-party products are often «глубоко вплетены в исходный код» (p. 80), but if the idea of a database is abstracted to the point where it simply provides persistence as a service, you can «поменять лошадей на переправе» (p. 80). In that case, a late performance test shows vendor A's database is too slow and vendor B's document database is faster, and the seam is what makes the switch possible (p. 80).

The reasoning is that a vendor is a decision that may be reversed from outside: the vendor gets bought by a competitor, skills turn out to be unavailable, requirements move (p. 80). This wiki reads what breaks when the rule is ignored as the cost of that reversal, which then grows with every call site. See [[reversibility]].

Weisfeld's *The Object-Oriented Thought Process* works the same case through as its example of [[interface-and-implementation]]. A `DataBaseReader` class has public methods written from what its users need: open, close, go to the first or last record, count records, check whether more remain, position at a key, fetch by key, fetch next (p. 55). The book calls these methods wrappers around the database system's functionality, kept so that the engine itself can be changed without changing the code (p. 56). Its users need not know how the database is opened, how a record is fetched, or how the engine decides whether records remain (p. 57). The public `open(name)` does application-specific work, calls the Oracle API, then does more application-specific work (p. 58). After an overnight move to SQL Anywhere only the vendor call in that body changes, and «К нашему великому разочарованию, этим утром не поступило ни одной жалобы» (p. 59). The book concedes that wrappers can look like overkill, and holds that writing them has many advantages (p. 57). It also names the condition the swap rests on: the replacement must meet the same specification as the original, as two power stations behind one socket must both deliver the current the socket specifies (p. 55). This wiki reads that condition as part of the repair: the adapter's contract includes the observable behaviour callers rely on, not only its signatures. In chapter 6 the book adds the case where the outside class cannot be changed at all, because its author has left or the vendor no longer ships updates: the wrapper then changes its interface or implementation, not just its form, and the book points back to the database example and to object-relational middleware as such wrappers (p. 129).

Chapter 15 names the shape: the Adapter pattern, «инструмент, с помощью которого вы можете создать отличающийся интерфейс для уже существующего класса», in essence a class wrapper that joins the existing class's functionality with a new and ideally better interface (p. 294). The example is a purchased `MailTool` that does what the company needs, while the company wants every client to call `getMail()` rather than `retrieveMail()`. A `MailInterface` declares `getMail()`, and `MyMailTool` implements it, holds a `MailTool` and calls `retrieveMail()` inside (pp. 295-296). The book adds that the wrapper may also extend the interface with functionality of its own (p. 296). Its listing gives `MyMailTool` a public `getYourMailTool()`/`setYourMailTool()` pair (pp. 295-296). This wiki reads that pair as a leak: callers can reach the vendor's names past the adapter, and the adaptee can be replaced from outside. The example is also a pure rename at one call site, which the limit below on one-to-one wrappers would not admit; this wiki takes it as a teaching example, not as the threshold.

Larman's *Applying UML and Patterns* takes the case where the second vendor is already there: the point-of-sale system must support several tax calculators and accounting systems, each with its own API that cannot be changed. His Adapter problem: "How to resolve incompatible interfaces, or provide a stable interface to similar components with different interfaces?"; the solution: "Convert the original interface of a component into another interface, through an intermediate adapter object" (26.1, p. 601). The application owns one interface in its own terms, such as `ITaxCalculatorAdapter.getTaxes(sale)`, and each vendor gets one adapter class implementing it, "a level of indirection with objects that adapt the varying external interfaces to a consistent interface used within the application" (p. 601). In his design `getTaxes` returns a list of `TaxLineItem`s (26.3, p. 605); this wiki reads that as the rule that the operation returns the application's types, not the vendor's. He reads the pattern as a specialization of GRASP, supporting [[protected-variations]] "through the use of an Indirection object that applies interfaces and Polymorphism" (26.2, p. 603); see [[patterns-as-specializations-of-grasp]]. Two further specifics: include the pattern name in the type name, as in `TaxMasterAdapter`, because it tells a reader which pattern is in use (26.1, p. 602); and the adapters are created by a factory, which decides which one to build ([[factory-object-for-creation]]). This wiki reads Larman's case as the point at which step 6 of the repair below declares the interface: a second implementation exists.

## Sign in code

Any of these, all of which can be counted:

- calls to the vendor's client or its query dialect inside a class or function that also holds business logic;
- a vendor type appears in the signature of a function the application defines (a parameter, a return value, a stored field);
- the vendor's query dialect, as string literals, appears next to business logic;
- `catch` clauses naming the vendor's exception types appear outside the adapter class;
- application code holds an `if` or `switch` on which vendor or service is configured, each branch calling a different API with its own argument shapes, or two call sequences of the same shape that differ only in which vendor's API they call (both signs are this wiki's reading of Larman's case);
- the adapter has a public accessor that returns the wrapped vendor object, or one that replaces it (Weisfeld's `getYourMailTool()`, pp. 295-296).

The vendor here means a third-party product that fills a role a rival could fill behind the same need, such as a database, a payment gateway or a message broker.

Adapter and Facade both fire on a class that wraps something. **Selecting condition:** if the wrapper exists so that a third-party product, or several of them with different interfaces, reach the application through the application's own interface, [[hide-third-party-apis]] owns it; if it exists to give one entry point to a group of the project's own classes, [[facade-single-entry-point]] owns it. Larman draws the same split: a resource adapter "may also be considered a Facade", but the name Adapter is chosen "when the wrapping object provides adaptation to varying external interfaces" (26.1, p. 602). A surrogate with the vendor's own interface that adds failover, caching or access checks in front of it is [[proxy]].

This page owns a layer that confines such a product. It has one implementation, which is not the sign of [[know-when-to-stop]]: that page counts layers around the application's own code, while this one is justified by the reversal it keeps cheap.

This wiki assigns the neighbouring cases as follows. A hidden input where no sign of this page fires is [[global-data]], vendor or not. A table or record layout known by several modules is [[single-owner-of-data-access]], whatever product stores it; when both fire, one module is both the adapter and the owner. The program's own legacy code or a non-portable platform API spread over modules is [[isolate-volatile-dependencies-behind-a-layer]]. A domain class carrying storage methods is [[delegate-to-services]]; this page owns a free function that mixes the dialect with business logic. A third-party product's exception type in any signature or catch outside the adapter's body, the adapter's own signatures included, is [[hide-third-party-apis]]; an exception of the standard library or of the project's own lower code escaping a class's interface is [[exception-at-the-interface-abstraction]]. A branch whose key names which third-party product is configured, its arms calling that product's own API, is [[hide-third-party-apis]]; a branch whose arms only choose which concrete class to instantiate is [[factory-object-for-creation]]. A branch whose key names what kind of thing the switched-on object is (a shape, a square, a transaction) is [[polymorphism-or-type-switch]]; a branch whose key names a policy the object applies to compute one result, with that policy's parameters stored as fields of the object, is [[strategy-for-varying-algorithms]]. Two call sequences of the same shape that differ only in which third-party product's API they call are [[hide-third-party-apis]], and [[dry]] defers to it.

## When not to apply

This wiki's own limits; the source states none.

- The language's standard library and runtime: there is no vendor decision to keep reversible. Whether a function should reach the file system or another mutable resource directly at all is a separate question, which [[global-data]] owns (p. 175).
- A utility library of pure functions, such as one for dates or collections: nothing outside the project can force its replacement at a cost a wrapper would reduce.
- A module whose whole purpose is that product, such as a plugin for it or an adapter: it is the place where the vendor is allowed to be.
- A vendor already confined to one adapter class: the confinement is the seam, and an extra interface adds nothing until a second implementation is needed.
- A wrapper that repeats the vendor's API one to one, with the vendor's types in its signatures, does not satisfy the rule. It should not be added, because every signature would still have to change with the vendor. The source asks for the idea to be generalised, not for its calls to be renamed.
- A vendor-specific capability the application truly depends on cannot be hidden by a generic interface. Hiding it costs either that capability or a leak. The cost should be named in the interface.

## Repair

The source gives the layer; the steps are this wiki's own.

1. Name what the application needs from the product, in the application's own terms (`find`, `save`, not `query`, `execute`).
2. Write those operations using the application's own types.
3. Move every call to the vendor, its types and its query dialect into one adapter class.
4. Translate vendor exceptions at the adapter's edge into errors of the application. Give the adapter no accessor that returns the wrapped object; this departs from Weisfeld's listing (pp. 295-296).
5. Write down what callers rely on beyond the signatures (ordering, error cases, units), so that a replacement vendor can be checked against it (after Weisfeld, p. 55).
6. Pass the adapter in, so the callers name only its operations. Declare a separate interface only once a second implementation or a test double needs one.
7. With several vendors, give each its own adapter class implementing that interface, named for the vendor and the pattern (`SapAccountingAdapter`), and move the choice of which one to build into one factory, so no call site branches (after Larman, 26.1-26.4, pp. 601-606).

## Before and after

```
// before: the vendor is in the business logic
function close_order(id):
    conn = VendorDb.connect(DSN)
    row = conn.query("SELECT status FROM orders WHERE id = ?", id)
    if row.status == "paid":
        conn.execute("UPDATE orders SET status = 'closed' WHERE id = ?", id)
```

```
// after: the application speaks of storing orders
function close_order(id, store):
    order = store.find(id)
    if order.is_paid():
        order.close()
        store.save(order)

// the only class that names VendorDb
class VendorDbOrderStore:
    find(id) -> Order: ...
    save(order): ...
```

Several vendors already in the code, after Larman's accounting case:

```
// before: the caller branches on the vendor
class Register:
    method postSale(sale):
        if config.accounting == "SAP":
            soapClient.send(SapPostRequest(sale.id, sale.total.cents))
        else if config.accounting == "GreatNorthern":
            gnApi.post(sale.toGnRecord())
```

```
// after: one interface the application owns, one adapter per vendor
interface AccountingAdapter:
    method postSale(sale)

class SapAccountingAdapter implements AccountingAdapter:
    method postSale(sale): soapClient.send(SapPostRequest(sale.id, sale.total.cents))

class GreatNorthernAccountingAdapter implements AccountingAdapter:
    method postSale(sale): gnApi.post(toGnRecord(sale))

class Register:
    field accounting: AccountingAdapter      // built by a factory
    method postSale(sale): accounting.postSale(sale)
```

## Source

[[pragmatic-programmer]], Topic 11, pp. 80-81: the rule, the database case and the reasoning. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 2, pp. 55-59, and ch. 6, p. 129 (wrapping classes that cannot be changed): the `DataBaseReader` methods, wrappers so the engine can change, what users need not know, `open()` before and after the vendor change, the specification both sides must meet; the quotation was checked against `raw/`. The book's survey of object-relational mapping products and object databases (pp. 57-58) is not carried, because it describes a product market. Ch. 15, pp. 294-296: the Adapter pattern, the `MailTool` example, extending the interface, the accessor pair in the listing; the quotation was checked against `raw/`. This wiki's own for that part: the reading of the specification condition as part of the adapter's contract, step 5, the reading of the accessor pair as a leak, its sign and the instruction in step 4. The book states the rule under flexible architecture (p. 81); applying it to one adapter class inside the code in view, and leaving which modules may import the vendor to the project's architecture, is this wiki's reading. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.1-26.3, PDF pp. 601-605: the Adapter problem and solution, the per-vendor adapters behind one interface, application types in the result, the naming guideline, the Adapter/Facade remark and the GRASP reading. This wiki's own for that part: the reading of `TaxLineItem` as the application's type in the result, the branching and same-shape signs, the split of branches with [[factory-object-for-creation]], [[strategy-for-varying-algorithms]] and [[polymorphism-or-type-switch]], the split with [[dry]], the reading of his case as the moment the interface is declared, the selecting condition against [[facade-single-entry-point]] and [[proxy]] as worded, repair step 7 and the second pair. The reading of what breaks, the sign, the meaning given to a vendor, the splits with [[know-when-to-stop]], [[global-data]], [[delegate-to-services]] and [[exception-at-the-interface-abstraction]], all limits, the repair steps and the pseudocode are this wiki's own.
