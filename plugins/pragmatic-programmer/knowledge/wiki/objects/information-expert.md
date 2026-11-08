---
title: "Information Expert: give a responsibility to the class that has the information"
category: objects
summary: "A method in class X computes a derived value (total, subtotal, status) only from data class Y holds, reading it out through getters and writing nothing back, when Y could compute it from its own state; a read followed by a write back into Y is tell-dont-ask."
tags: [rule, responsibilities, grasp, encapsulation, coupling, do-it-myself]
paradigm: oop
sources: [larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Information Expert** (Expert for short) is the GRASP principle Larman calls "one of the most basic responsibility assignment principles in object design" (17.8, p. 426). It covers knowing and doing responsibilities alike. The book lists other names for it: "Place responsibilities with data", "That which knows, does", and Coad's "Do It Myself" (17.11, p. 443). In chapter 18 Larman says "Expert should be the first pattern considered unless the problem is a controller or creation problem" (18.4, p. 483); those two cases are [[controller]] and [[creator]]. The frame is [[responsibility-driven-design]].

## Rule

"Assign a responsibility to the class that has the information needed to fulfill it" (17.8, p. 427). The information may be the object's own state, the objects it is related to, or what it can derive.

Larman's reason is [[low-coupling]]. If the responsibility is placed anywhere else, "the overall coupling will be higher because more information or objects must be shared away from their original source or home" (p. 429). He also names the benefits as kept encapsulation and behaviour spread over lightweight, more cohesive classes (17.11, p. 443).

Larman turns the rule into a procedure, worked on the sale total (17.11, p. 439; 18.4, pp. 480, 484-485):

1. **State the responsibility as a question**, such as "Who should be responsible for knowing the grand total of a sale?"
2. **Summarise the information it needs.** The total is the sum of the line subtotals; a subtotal is quantity times product price.
3. **List each piece of information and the class that knows it.** Price is on ProductDescription, quantity on SalesLineItem, the set of line items on Sale.
4. **Give the top responsibility to the class holding the aggregate, and recurse for each sub-result.** `Sale` knows the total, `SalesLineItem` its subtotal, `ProductDescription` the price.

Larman calls the classes in such a chain "partial" information experts that collaborate through messages, and calls the whole idea the ordinary intuition that "objects do things related to the information they have" (17.11, p. 442). A software Sale computes its own total although a real sale is inert; Larman calls this the "animation" principle (p. 442). He says the elaboration is excessive for a trivial case, but "the same reasoning strategy to find an Expert can and should be applied in more difficult situations" (18.4, p. 485).

In chapter 35 Larman returns to Coad's name. Do It Myself reads: "I (a software object) do those things that are normally done to the actual object that I'm an abstraction of" (35.8, p. 808), which he calls "the classic object-oriented design style": circles and squares draw themselves, a text object spell-checks itself (p. 808). "Do It Myself and Information Expert usually lead to the same choice", and so do Do It Myself and Polymorphism (p. 808). He gives one more reason to prefer it when it fits, support for "low representational gap" (p. 808); this wiki reads that as code that reads like the domain the reader already knows. His worked case is payments: credit, debit, cash and check payments are authorized differently, so each `Payment` subclass authorizes itself and handles its own completion after the reply (pp. 809-813); the per-type side of that is [[polymorphism-or-type-switch]].

### Choosing among partial experts

When several classes each hold part of the needed data, Larman gives guidelines in order (18.5, p. 502):

1. Place the responsibility in "the dominant information expert", the object with most of the information. He says this tends to best support Low Coupling.
2. Where alternatives remain, "consider the coupling and cohesion impact of each, and choose the best". In Monopoly, MonopolyGame already runs the game loop, so more work there costs cohesion, while Player and Board do nothing yet.
3. Where there is still no clear winner, consider the probable evolution of the objects. Later Monopoly rules make taking a turn depend on the player's cash and strategy, which Player holds, so Player takes the turn.

This wiki reads the third guideline as usable only when the coming requirement is known, as the full game rules are in Larman's example. A forecast is not a sign, so in review it cannot carry a finding on its own. The coupling comparison of the second guideline is worked on [[low-coupling]].

Fowler and Beck's chapter on smells in *Refactoring* names the code-side shape **Feature Envy**: a function that "spends more time communicating with functions or data inside another module than it does within its own module", the classic case being a function that calls half a dozen getters on another object to calculate one value (2nd ed., ch. 3, Feature Envy, PDF p. 91). Underneath they put "the fundamental rule of thumb", "put things together that change together": data and the behaviour that references it usually change together (PDF p. 92). This wiki reads Feature Envy as this page's sign stated from the code, and keeps the split with [[tell-dont-ask]] by whether anything is written back.

## Sign in code

Larman states the rule on interaction diagrams; Fowler and Beck's Feature Envy (above) is the code-side shape. The sign as worded here, including that nothing is written back, is this wiki's: a method in class X computes a derived value (a sum, a subtotal, a status) only from data held by class Y. It reads Y's fields or Y's collection through getters and writes nothing back to Y. Y could produce the same value from its own state, and X does nothing else with the parts it read.

The shape to point at is a run of `y.getA()`, `y.getB()` or a loop over `y.getItems()` whose only product is one value computed in X.

This wiki assigns the neighbouring cases as follows. Whether the outside code writes back into the object it read decides between [[information-expert]] and [[tell-dont-ask]]: a read followed by a write back, or a collection fetched from an object to be searched, is [[tell-dont-ask]]; a read-only computation of a derived value from another class's data is [[information-expert]]. A computation from another class's data alone is [[information-expert]]; one that mixes the computing class's own data with another's, where either class could hold it, is compared on [[low-coupling]]. A loop that commands each element of a group the class holds and accumulates a value kept only in a local is [[pure-fabrication]]; a read-only computation of a derived value from another class's data is [[information-expert]]. One class computing from several data-only classes' data in this way is [[god-class]]. Where the class computing it is the one that receives the program's incoming requests or system operations, [[controller]] owns it. A reach through a chain of returned objects is [[train-wreck]]. A field-less class whose methods all take the same one record and read or write only its fields, while the record has only fields or accessors, is [[class-with-only-data-or-only-behaviour]]; where its methods each read and write several data-only classes, [[god-class]] owns it. A method in class X that computes from data class Y already holds is [[information-expert]]; free functions or client code deriving values from a record that is not yet a class are [[combine-functions-into-class]].

## When not to apply

- **The computation is a different concern from what the expert holds.** Larman's own contraindication is saving a Sale to a database: most of the information is in Sale, so Expert argues for `Sale.save`, but if every class saved itself that "leads to problems in cohesion, coupling, and duplication" (17.11, pp. 442-443). The decision between the expert and a made-up class is [[pure-fabrication]]. Where the project's convention keeps persistence out of domain classes, [[delegate-to-services]] owns the sign.
- **Larman's own limit on Do It Myself.** It "is often contraindicated due to problems in coupling and cohesion, and instead, a designer uses pure fabrications such as strategies, factories, and the like" (35.8, p. 808). His payment design shows the split: the payment authorizes itself, but the protocol, message format and connection belong to an authorization-service adapter the payment asks for (pp. 811-812). This wiki reads that as: the object owns the decision, a fabricated object ([[pure-fabrication]], [[hide-third-party-apis]]) owns the technical work.
- **The data holder must not depend on what the computation needs.** This limit is this wiki's extension of the same contraindication: formatting for display, or a calculation that needs a service the holder should not know. Expert would add that dependency to the holder, and [[low-coupling]] decides.
- **The information is spread and no class holds most of it.** Then no single class is the expert. Each class computes the part it holds and a coordinator combines the parts, as `Sale` combines the subtotals. Moving the whole computation into whichever object holds most of the fields is not this page's repair.
- **The behaviour varies independently of the data.** Fowler and Beck name this exception themselves: Strategy, Visitor and Beck's Self Delegation keep behaviour away from its data on purpose, to fight divergent change. They "isolate the small amount of behavior that needs to be overridden, at the cost of further indirection" (PDF p. 92). Keeping such behaviour apart is the design, not the sign.
- **A function whose job is to convert or present data for another context**, such as a mapper or a formatter at a boundary, reads another object by design. This limit is this wiki's own.
- **The holder is a plain data carrier by the project's design**, such as a record passed between layers or a message, where behaviour sits elsewhere by convention. That is a setting taken from the project. This limit is this wiki's own.
- **Code organised as functions over records.** Where the project uses a functional or data-oriented style, the computation may sit in a function over the record; this page is `paradigm: oop`. This limit is this wiki's own.

## Repair

Move the computation into the class whose data it uses, as a method named for the answer (`total`, `subtotal`), and replace the getter-walking code with one call. Where the data sits on several classes, give each class the part it can compute from its own data and let the outer class combine the results. If X used the getters only for that computation, remove them or stop exposing the internal collection.

Fowler's mechanics (PDF pp. 91-92): Move Function to the data the function envies ([[move-function]]). If only part of the function envies, Extract Function on that part first, then move it. Where the function uses features of several modules, he puts it with the module that has most of the data, and extracting first lets the pieces go to different places. This wiki reads his tie-break together with the limit above on spread information: where extraction can split the function, each piece goes to the class holding its data, and only a piece that cannot be split goes to the module with most of the data.

Larman gives a second repair for a caller that keeps needing another object's data: "when object A keeps needing the data in object B it implies either 1) object A should hold that data, or 2) object B should have the responsibility (by Expert) rather than object A" (25.1, p. 583). In Larman's case Player kept getting its square from Piece, so Player came to hold the square itself, "since the Player keeps collaborating with its Square" (p. 583). That case is a read followed by a write back, and the choice between moving the data and moving the responsibility is [[tell-dont-ask]].

## Before and after

```
class ReceiptPrinter
    saleTotal(sale)
        total = 0
        for item in sale.getLineItems()
            total = total + item.getQuantity() * item.getProduct().getPrice()
        return total
```

```
class Sale
    total()
        return sum of item.subtotal() for item in lineItems

class SalesLineItem
    subtotal()
        return quantity * product.price()

class ProductDescription
    price()
        return price

// caller
sale.total()
```

In the "after" no class reads another class's fields in order to compute, and `ReceiptPrinter` no longer depends on `SalesLineItem` or `ProductDescription`.

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.8, PDF pp. 426-429 (the rule as first stated, the coupling reason); 17.11, PDF pp. 439-443 (stating the responsibility first, partial experts, the animation principle, the persistence contraindication, the benefits, the other names); 18.4, PDF pp. 480-485 (Expert first unless creation or control, the four-step procedure); 18.5, PDF p. 502 (the guidelines for partial experts); 25.1, PDF p. 583 (move the data or the responsibility).
- Larman, 35.8, PDF pp. 808-813: the Do It Myself quotation, its links to Expert and Polymorphism, low representational gap, the contraindication and the payment design. This wiki's own for that part: the reading of representational gap and of the contraindication as decision in the object, technical work in an adapter.
- This wiki's own: the sign in code, the owner split with neighbouring pages, the limits on dependencies of the holder, data carriers and functional style, the reading of the third guideline as needing a known requirement, and the pseudocode, which follows Larman's Figures 17.15-17.17.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Feature Envy", PDF pp. 91-92: the smell, the rule of thumb, the Strategy and Visitor exception, and the mechanics with the tie-break. This wiki's own for that part: reading Feature Envy as this page's sign, the mapper limit, and the note on the tie-break.
