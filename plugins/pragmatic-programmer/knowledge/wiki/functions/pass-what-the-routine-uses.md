---
title: Pass what the routine uses, or the whole object
category: functions
summary: "A routine takes a whole domain object but reads only one or two of its fields, so a caller that holds those values elsewhere must create or fake the object to call it; a caller fills an object by setters only to make one call and copies its fields back after; or, the other way, every caller passes several fields of one object in the same positions (low = r.range.low; high = r.range.high; plan.withinRange(low, high)), or an object passes several of its own fields to another object: decide by what abstraction the routine's interface forms."
tags: [decision-rule, coupling, parameters, flexibility, interfaces, abstraction, setup-code, aggregate, preserve-whole-object]
paradigm: any
sources: [code-complete, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

This test decides between a routine taking a whole object and taking only the values it needs. It is McConnell's worked example of the *flexibility* criterion of [[coupling]] (pp. 97-98).

## Rule

The book's case: `LookupVacationBenefit()` computes leave from an employee's hire date and job classification and takes an `employee` object. By size and visibility the coupling looks loose: one obvious connection. Then a third module holding hire date and classification, but not in an `employee`, needs the routine. It must either know about the `Employee` class and fake an instance with two fields set, which also requires knowing that the routine reads only those two (the book calls this sloppy and ugly), or the routine must be changed to take the two values. Either way the routine was far less flexible than it looked (pp. 97-98). The book's resolution is that the routine becomes usable once it accepts classification and hire date (p. 98), and it ranks object-parameter coupling as tighter than primitive-parameter coupling (p. 98).

Chapter 7 states the general question (p. 175). Take an object with 10 accessors, of which a routine needs three. One camp passes only the three values: it minimises coupling and eases understanding and reuse, and passing the whole object breaks encapsulation by exposing all 10 accessors. The other camp passes the whole object: the interface stays stable if the routine later needs more members, and naming three specific elements is what breaks encapsulation, because it reveals which data the routine uses. McConnell calls both rules oversimplified and asks instead: «какую абстракцию формирует интерфейс метода?» (p. 175). If the routine expects three particular values that happen to belong to one object, pass the values; if its job is to operate on that object, pass the object. He gives two observable tests (p. 175): if the caller creates an object, fills in the elements the routine needs and takes them out again after the call, pass the elements, and code that prepares data before a call or unpacks an object after it generally signals poor routine design; if the parameter list keeps changing, each change adding another member of the same object, pass the object. The checklist asks whether the parameter list as a whole forms a consistent interface abstraction (p. 181).

Chapter 24 returns to the question as a pair of opposite refactorings, pass a whole object instead of separate fields and pass separate fields instead of a whole object (p. 561), and decides it the same way: «Каждый из этих подходов может быть как верным, так и неверным: все зависит от того, какую абстракцию формирует интерфейс метода ProcessWithdrawal()» (p. 557). It lists setup code before a call and takedown code after it as a warning sign of a poor interface abstraction, annotating its example with «Подготовительный код — дурной знак» (pp. 556-557): a `Withdrawal` object is created, filled by three setters, passed to `ProcessWithdrawal`, and its balance read back with a getter. A special constructor that takes a subset of the normal initialisation data only so that one method can be called is the same sign (p. 557). The book's repair passes the values as parameters (p. 557). It also reads a long parameter list in itself as a sign of a poor abstraction: well-factored programs have many small routines that need few parameters (p. 554).

Larman's *Applying UML and Patterns* describes the object side as an idiom that "does not have a name" and suggests calling it "Pass Aggregate Object as Parameter" (p. 625): "Avoid extracting child objects out of parent or aggregate objects, and then passing around the child objects. Rather, pass around the aggregate object that contains child objects" (26.8, p. 625). In his pricing design `Sale` calls `factory.addCustomerPricingStrategy(this)`, and the factory asks the sale for its `Customer` and its current pricing strategy, rather than `Sale` passing those two objects. His reason is flexibility: with the whole `Sale`, "the factory can collaborate with the entire Sale in ways we may not have previously anticipated", which "reduces the need to anticipate what the factory object needs" (p. 625). He relates it to Low Coupling and [[protected-variations]].

Fowler's *Refactoring* frames the same choice in the motivation of Change Function Declaration (2nd ed., ch. 6, PDF pp. 142-143). Passing the value widens where the function can be used: a phone formatter that takes a person cannot format a company's number, and one that takes the number can, without knowing about people at all (PDF p. 142). Passing the object couples the function to the object's interface, and in return callers need not change if the logic later needs more of it; he calls that "increasing the encapsulation of the function" (PDF p. 142). His example is an overdue check: pass the payment, or only its due date? He gives no fixed answer: "The only right answer to this puzzle is that there is no right answer, especially over time" (PDF p. 143). His practical conclusion is to be fluent in [[change-function-declaration]], so the choice can be reversed as understanding changes. After narrowing `inNewEngland(customer)` to `inNewEngland(stateCode)` he notes that the function no longer depends on the customer and can be used in more contexts (PDF p. 148).

Fowler's own refactoring for the object side is **Preserve Whole Object** (ch. 11, PDF pp. 356-362), and there he leans toward the whole record. When code derives a couple of values from a record and passes them into a function, he replaces them with the record itself, letting the function body derive the values it needs (PDF p. 356). His reasons (PDF pp. 356-357): if the callee later needs more of the whole, the parameter list does not change; the list is shorter; and where many functions take the same parts, they often duplicate logic on those parts that could move to the whole. He names one condition that stops him: he does not want the callee to depend on the whole, "which typically occurs when they are in different modules" (PDF p. 357). This wiki reads that condition as agreeing with McConnell's test: a callee in another module is a general function using values, not an operation on the object.

This wiki states the decision: take the values when the routine reads a few fields and computes from them; take the object when the routine needs the object's behaviour or most of its state, or when its meaning is "for this object". Larman's case falls on the object side by this test, and this wiki names the setting: the callee is a collaborator of the aggregate's own family (a factory or strategy working on its behalf, as the context of [[strategy-for-varying-algorithms]] passes `this`), and it needs several of the aggregate's parts or must change the aggregate. A general function that uses one or two values stays on the values side, because passing the aggregate couples it to a type it does not need and it cannot be called or tested without building that type.

## Sign in code

- A routine's parameter is a domain object and the body reads one to three of its fields and calls none of its methods.
- A call site constructs a throwaway instance of that type just to call the routine (the faked object, the book's "sloppy" option). This wiki assigns that call-site shape to [[semantic-coupling]], which owns the partly built argument; this page owns the routine's signature.
- Around one call, the caller creates an object, fills it through setters, calls the routine, and copies fields back through getters, and the object is not used after; or a constructor taking a subset of the normal data is used only before one call (pp. 556-557). This wiki assigns that shape here. Where the object is passed with some fields left empty because the callee reads only the others, [[semantic-coupling]] owns it; where the object lives on and must be completed by setters before later use, [[temporal-coupling]] owns it.
- The aggregate side, after Larman: a method passes two or more parts of one aggregate (`customer, this.pricing, this.preDiscountTotal()` from a `Sale`) to a collaborator of that aggregate's family, such as its factory or strategy. This sign as worded is this wiki's. Where a caller outside the aggregate reads its parts and writes the result back into it, [[tell-dont-ask]] owns it and comes first; [[pass-what-the-routine-uses]] owns the signature of a collaborator that receives parts it could take as the whole aggregate.
- An object calling another object with several of its own fields as arguments. Fowler says many people miss this case, and the repair is to pass a self-reference (PDF p. 357).
- The other direction (where no structure holding the values exists yet, the loose variables are [[group-related-data-into-a-structure]]): every call site passes several values read from one object in the same positions (`ShippingLabel(order.id, order.recipient, order.address, order.priority)`; Fowler's `low = aRoom.daysTempRange.low` and `high = ...high` read only to call `aPlan.withinRange(low, high)`, PDF p. 358), and the routine's job is about that object. The book's test of a list growing one member at a time needs the version history; this wiki notes it is a sign only where that history is in front of the reader, and otherwise the sign is the call-site shape alone.

A field that already lives in an existing record but always travels with one other record is [[move-field]]: the repair there moves the field rather than changing the signature. Where callers read several fields of one existing object and the routine's job is about that object, [[pass-what-the-routine-uses]] owns the signature; where those fields form a value the source object does not model on its own (a range or a period held as two fields of a plan), [[group-related-data-into-a-structure]] owns it.

## When not to apply

- The routine calls methods on the object or reads most of its fields: unpacking would lengthen the parameter list and raise the *size* criterion the book lists first (p. 97).
- The values form a concept of their own that recurs together: this wiki suggests a small value type for them rather than loose primitives.
- Every caller does hold the object and the routine is a method of the object's own module; the book's failure needs a caller without it. This wiki notes that whether such a caller exists is a fact about other code, so in review the sign is the shape above and the finding should say the cost appears only for such a caller.
- Object designs that keep data behind behaviour ([[tell-dont-ask]], [[no-getters-and-setters]]) resolve the same smell the other way: move the computation into the object. Where the project follows that style, that page's repair wins; the condition is whether the routine belongs to the object's responsibility.

- **The project's architecture forbids the dependency.** This wiki adds a limit. Where the project's conventions place the routine in a module that may not depend on the caller's type, that architecture is taken as given and the routine takes values, whatever the call sites look like.

- Larman's reason rests on a forecast that the callee will need more than it does today. This wiki does not accept the forecast alone as a sign; the aggregate-side sign above refers only to code that already exists.
- Passing the aggregate hands the callee the ability to change everything in it. Where the callee should only read, a narrower parameter states that in the signature. This limit is this wiki's own.
- A builder that assembles a complex immutable value step by step is a deliberate creation interface, not setup for a call, when the built value is used beyond one call. This limit is this wiki's own.
- **Feature Envy instead.** If code pulls several values from the object only to compute on them, Fowler calls that a smell and "usually a signal that this logic should be moved into the whole itself" (PDF p. 357). The finding is then [[information-expert]]'s and the move is [[move-function]], not a change of the parameter.
- If several pieces of code use the same subset of an object's features, Fowler sees a chance to extract that subset into a class of its own rather than pass the whole (PDF p. 357).
- A parameter list that is long because the routine does too much is not fixed by bundling the values into an object; split the routine ([[routine-cohesion]]). This limit is this wiki's own.

## Repair

Change the signature to the fields actually read, with the migration mechanics of [[change-function-declaration]] where callers are many, and have callers that hold the object pass its fields; or move the computation onto the object where it belongs to it. For setup and cleanup around a call, change the routine's signature to accept what it needs directly and return what the caller then reads, so neither preparation nor teardown is left at the call site (p. 557). For the other direction, change the routine to take the object and read the members inside it, with Fowler's mechanics (PDF p. 357): create an empty function with the desired parameter under an easily searchable temporary name (his `xxNEWwithinRange`); make its body call the old function, mapping the whole to the old parameters; move each caller to the new function, testing after each, and remove the derivation code left dead; inline the old function into the new one, then rename it and its callers, which the prefix makes a plain global replace even without rename support (PDF pp. 359-360). A variation builds the new function from refactorings alone, by extracting a variable and a function from the call and moving the function, which suits tools with robust extract and inline (PDF pp. 360-362). Then ask, as [[tell-dont-ask]] would, whether the routine belongs on the object.

## Before and after

```
function vacationDays(e: Employee): int
    return table[e.jobClass][yearsSince(e.hireDate)]

-- contractor module has the two values, not an Employee
fake = Employee(jobClass = c.jobClass, hireDate = c.started)
days = vacationDays(fake)
```

```
function vacationDays(jobClass: JobClass, hireDate: Date): int
    return table[jobClass][yearsSince(hireDate)]

days = vacationDays(employee.jobClass, employee.hireDate)
days = vacationDays(c.jobClass, c.started)
```

Setup and cleanup around a call, after the book's withdrawal example:

```
w = new Withdrawal()
w.setCustomer(customerId)
w.setBalance(balance)
w.setAmount(amount)
processWithdrawal(w)
balance = w.getBalance()
```

```
balance = processWithdrawal(customerId, balance, amount)
```

Children extracted from one parent, after Larman's pricing case:

```
class Sale
  method enterCustomer(customer)
    this.customer = customer
    this.pricing = factory.withCustomerDiscount(customer, this.pricing, this.preDiscountTotal())
```

```
class Sale
  method enterCustomer(customer)
    this.customer = customer
    factory.addCustomerPricingStrategy(this)

class PricingStrategyFactory
  method addCustomerPricingStrategy(sale)
    sale.addPricingStrategy(strategyFor(sale.getCustomer()))   // Sale adds it to its composite
```

One field path read from the whole object, after Fowler's New England example:

```
function inNewEngland(customer)
    return NEW_ENGLAND_STATES.contains(customer.address.state)
```

```
function inNewEngland(stateCode)
    return NEW_ENGLAND_STATES.contains(stateCode)

caller: inNewEngland(customer.address.state)
```

The other direction:

```
label = ShippingLabel(order.id, order.recipient, order.address, order.priority)
```

```
label = ShippingLabel(order)
```

After Fowler's heating-plan example:

```
low  = room.todaysRange.low
high = room.todaysRange.high
if not plan.covers(low, high)
    alerts.add("temperature out of range")
```

```
if not plan.covers(room.todaysRange)
    alerts.add("temperature out of range")

plan.covers(range)
    return range.low >= self.range.low and range.high <= self.range.high
```

## Source

[[code-complete]], section 5.3, Russian edition, pp. 97-98. The `LookupVacationBenefit` case and its resolution are the book's; the stated decision, the signs, the owner assignment, the limits and the reconciliation with [[tell-dont-ask]] are this wiki's own.

[[code-complete]], section 7.5, p. 175, and the checklist, p. 181: the two camps, the abstraction question and the two observable tests are the book's. This wiki's own: the second sign as phrased, the note on version history, the architecture limit and the second pair.

[[code-complete]], section 24.2, pp. 554, 556-557, and section 24.3, p. 561: the two opposite refactorings, the `ProcessWithdrawal` quotation, setup and takedown code as a warning sign, the special constructor, and the long parameter list as a sign. This wiki's own: the third sign as phrased and its assignment against [[semantic-coupling]] and [[temporal-coupling]], the builder and bundling limits, and the third pair, which is written in this wiki's pseudocode after the book's example.

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.8, PDF p. 625: the idiom, its proposed name, the pricing-factory case and the flexibility reason. This wiki's own for that part: placing his case under the abstraction test, the family-collaborator setting, the aggregate-side sign, the forecast and read-only limits, and the pair.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 6, "Change Function Declaration", PDF pp. 142-143 and 148: the two sides of the trade-off, the phone and overdue examples, the no-right-answer verdict, fluency in the refactoring as the conclusion, and the New England example. This wiki's own for that part: placing his trade-off under the abstraction test above, and the pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 11, "Preserve Whole Object", PDF pp. 356-362: the rule, its reasons, the different-modules limit, Feature Envy and the extracted subset, the self-reference case, both mechanics. This wiki's own for that part: reading the different-modules limit as agreeing with McConnell's test, the routing of Feature Envy to [[information-expert]] and [[move-function]], and the heating-plan pseudocode.

Related: [[limit-parameter-count]], [[tramp-data]], [[refactoring-warning-signs]].
