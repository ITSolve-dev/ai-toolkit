---
title: Polymorphism or type switch
category: objects
summary: "A switch over an object's type code that calls a type-specific method or routine in each arm (drawCircle, drawSquare; processDeposit(t), processWithdrawal(t)) on the same object or data, the same type code switched on in several routines, one special case (zone == china and has china history) tested in several functions of one calculation, or two hierarchies whose subclasses mirror each other; distinguish it from a switch dispatching genuinely different commands, and from the one creation switch in a factory."
tags: [decision-rule, polymorphism, switch, dispatch, factory, type-codes, parallel-change, grasp, base-and-variant]
paradigm: oop
sources: [code-complete, object-oriented-thought-process, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell: prefer polymorphism to extensive type checking, though many case blocks only *may* indicate that inheritance would have been better, and not always (p. 144). In section 19.4 he carries one example past nesting reduction: a transaction loop that switches on the transaction type and calls a per-type routine becomes an abstract `Transaction` with subclasses `Deposit`, `Withdrawal` and `Transfer`, created in one place and then asked to `Complete()` (pp. 445-447). There he cites Meyer's view that `case` statements in object-oriented programs almost always signal poorly factored code and should be used as rarely as possible (p. 447).

Weisfeld's *The Object-Oriented Thought Process* gives the polymorphic side as a responsibility: «на индивидуальный объект, будь то Circle, Star или Square, возлагается обязанность по рисованию фигуры, которая ему соответствует» (p. 43). `Shape` declares `getArea()` abstract and carries no implementation, because nobody can compute the area of a shape without knowing which shape it is; `Circle` and `Rectangle` override it (pp. 44-45). Popping shapes off a stack, the caller calls `getArea()` and the result depends on the actual subclass (pp. 46-47). A subclass that inherits an abstract method must implement it or is itself abstract (p. 45). His reasons: one interface standardised across classes (p. 47), and a mechanism for adding new classes fairly easily (p. 45). This wiki reads the second reason in code: a new kind is a new class, and no caller changes.

Later chapters of the same book do show the conditional. In chapter 5, under the principle that a class must be responsible for itself (after Tyma, Torok and Downing), the non-object `print(circle)` and `draw` each need a `switch` or `if/else` on the shape passed in, calling `printCircle` or `printSquare`, and «Каждый раз при добавлении новой фигуры вам потребуется добавить соответствующий параметр в операторы case всех функций» (p. 109). In the object version `shape.print()` stays the same call for every shape, and the shape's context decides the response (p. 110). Chapter 7 restates the ground, «Как правило, объект должен быть ответственным за себя» (p. 144), and the payoff: a new `Triangle` is written, compiled, tested and used, and «Базовому классу Shape не пришлось бы претерпевать изменения, равно как и любому другому коду» (p. 147); a method taking a `Shape` can draw any shape, including one added later (p. 148). Chapter 8 names the alternative outright: a `Shape` holding the drawing code for every present and future shape would need «условный оператор (вроде case)», and maintaining all that code would become very tangled (p. 159).

Larman gives the same idea as the GRASP principle **Polymorphism**: when related behaviour varies by type, assign the responsibility for it to the types, using polymorphic operations (25.1, p. 578). Its corollary is the part a reviewer applies: "Do not test for the type of an object and use conditional logic to perform varying alternatives based on type" (p. 578). His reason: with case logic, "if a new variation arises, it requires modification of the case logic", often in many places (p. 578), while with polymorphism "New implementations can be introduced without affecting clients" (p. 584). He also lists the pattern as *Choosing Message* and *Don't Ask "What Kind?"* (p. 584). His Monopoly example replaces a switch on `square.type` with `landedOn(player)` on each kind of square (pp. 579-582). In chapter 35 he applies it again to payments: credit, debit, cash and check payments are authorized differently, "a classic case for Polymorphism", so each `Payment` subclass gets its own `authorize` and `Sale` asks the payment it created to authorize itself (35.8, p. 809); the infrastructure each one needs is reached through an adapter, as [[information-expert]] records.

## Rule

The book contrasts two switches (pp. 144-145):

- A switch on `shape.type` whose arms call `shape.DrawCircle()` and `shape.DrawSquare()`. These should become a single polymorphic `shape.Draw()`.
- A switch on `ui.Command()` whose arms call `OpenFile()`, `Print()`, `Save()`, `ShutDown()`. It could become a Command hierarchy with `DoCommand()`, but in a simple case that is inappropriate: «имя метода DoCommand() было бы настолько туманным, что почти утратило бы всякий смысл» (p. 145), while the case labels are informative.

Where polymorphism fits, the type code is examined once, where the object is created, and the rest of the code calls a polymorphic method (the code on p. 446; the wording is this wiki's). In a system of any size the creation `switch` itself moves into a factory method that can be reused wherever such objects are made (p. 446); the factory body is the old `switch`, returning a new object in each branch (p. 447).

Chapter 24 lists the repeated form as a refactoring warning sign: similar case statements in several parts of the program that must be changed together, and parallel inheritance hierarchies, where every new subclass of one class forces a new subclass of another (p. 554). The book adds that a single case statement is not bad in itself: «В самих по себе блоках case ничего плохого» (p. 554). The matching refactorings are replacing conditionals, especially repeated case statements, with polymorphic routines, and replacing a set of type codes with a base class and a subclass per code (p. 560); where subclasses then differ only in returned constants, the book's reverse refactoring replaces the virtual routines with data initialisation (p. 562), which [[subclass-that-differs-only-in-data]] owns.

Larman adds three details on the polymorphic side (25.1, pp. 580-582):

- A kind whose behaviour is "nothing happens" still gets the operation, with an empty body. Larman: "to make the magic of polymorphism work, we need to use this approach to avoid special case logic" (p. 582).
- Unless the supertype has a real default behaviour, the polymorphic operation is declared abstract there (p. 580).
- The operation takes as parameters the objects each implementation needs: `landedOn(player)` lets each square act on the player without reaching for it.

Fowler's *Refactoring* gives the reason the repeated switch is the stronger sign and a criterion for when the hierarchy pays. Conditional logic of this kind "tends to decay as further modifications are made unless it's reinforced by more structural elements of the programming language" (2nd ed., ch. 1, PDF p. 43), and "The more functions there are that depend on the same type of polymorphism, the more useful this approach becomes" (PDF p. 54). In his example, switches on `play.type` in two functions (the charge and the volume credits) became one switch in a factory. Where most kinds share one behaviour and only some vary, he keeps the common case as a default in the superclass and overrides it only in the variants (PDF p. 51). His step-by-step procedure is [[replace-conditional-with-polymorphism]].

In chapter 3 Fowler and Beck record that they revised the smell between editions. The first edition had "switch statements", written when polymorphism was underused. The second edition's smell is **Repeated Switches**: the same conditional switching logic, in a switch or a cascade of if/else statements, in different places (ch. 3, Repeated Switches, PDF pp. 93-94). They reject the view that every switch begs for polymorphism, and gives two reasons for narrowing the smell: polymorphism is no longer underused, and many languages now have richer switch forms that do not rest on a primitive code (PDF p. 93). The cost that remains is the repeated form: "whenever you add a clause, you have to find all the switches and update them" (PDF p. 94). A big switch inside one long function they treat under Long Function, by turning each leg into a single call (PDF p. 88; see [[keep-case-arms-short]]).

The catalogue entry *Replace Conditional with Polymorphism* (ch. 10, PDF pp. 302-320) names two situations (pp. 302-303). **A set of types**, each handling the conditional logic differently: "This is made most obvious when there are several functions that have a switch statement on a type code." (p. 302). **A base case with variants**: the base case goes into a superclass, "which allows me to reason about it without having to worry about the variants" (p. 303), and each variant into a subclass written as its difference from the base. His rating example moves a repeated test for a voyage to China by a captain who has been there out of two scoring functions into a subclass whose code "reads as a set of variations on the base" (p. 320). He calls it particularly useful "if I'm about to introduce more special logic for this case" (p. 311), and notes that the textbook generalization hierarchy "probably isn't the most common or best way" inheritance is used in practice (p. 309).

The same entry sets his limit: polymorphism is "prone to overuse", and to those who argue that all conditional logic should be replaced, "I don't agree with that view. Most of my conditional logic uses basic conditional statements—if/else and switch/case." (p. 303).

This wiki draws the discriminating criterion from the pair: polymorphism fits when every arm does *the same operation* on *one object or record* whose kind varies, so one honest name covers all arms. It does not fit when the arms are different operations that share no name better than "do it".

## Sign in code

- A switch or if-chain on a type tag of an object, each arm calling a method on that same object whose name repeats the operation plus the type (`drawCircle`, `drawSquare`), or a differently named routine taking that same data (`processDeposit(t)`, `processWithdrawal(t)`, `makeTransfer(t)`), or arms that do inline, on the caller's own data, the work each kind of the switched-on object should do (Larman's switch on `square.type`).
- The same type tag switched on in more than one place, the arms of each switch listing the same set of codes.
- A special-case guard in front of a call, testing a type tag for the one kind that does nothing (`if square.type != REGULAR: square.apply(player)`), where that kind could carry an empty method. This sign is this wiki's reading of Larman's NO-OP advice (p. 582). The same guard written as a runtime type test (`square is RegularSquare`) is [[avoid-introspection-and-casting]].
- The same compound test for one special case repeated in several functions of one calculation, each adjusting its result when the test holds (`zone == "china" and hasChinaHistory` in both the risk and the profit functions, Fowler pp. 309-312).
- Two hierarchies whose subclasses correspond one to one (`PdfReport` / `PdfExporter`, `HtmlReport` / `HtmlExporter`), so adding a kind to one means adding it to the other (p. 554).

This wiki assigns the neighbouring cases as follows. A switch on a type code, in one routine or repeated in several, is [[polymorphism-or-type-switch]]; fields or methods meaningful only for some values of a type code, and the choice between subclassing the class itself or a separate type object, are [[replace-type-code-with-subclasses]]. A type test with casts on a parameter is [[avoid-introspection-and-casting]]; [[drive-repeated-dispatch-from-a-table]] owns a branch over a data value chosen at run time, whose arms hold the varying values or calls themselves; where each arm instead constructs or calls a per-variant unit whose body is a fixed list of fields, [[describe-variants-in-data-not-subclasses]] owns it; where the key is a public constant or enum passed in from outside to select behaviour, [[no-public-constants]] owns the branch; nested switches on state and event are [[finite-state-machine]]; a routine whose flag parameter selects unrelated jobs it performs inline is [[routine-cohesion]]; a switch dispatching genuinely different commands over data is [[case-or-if-chain]]. The depth of decisions around such a switch is [[tame-deep-nesting]]; this page owns the switch itself. A switch on a type tag of an object whose arms call per-kind behaviour of one operation is [[polymorphism-or-type-switch]]. A switch over a control state that the object's own methods reassign is [[switch-on-state-vs-state-pattern]]; a switch over a type code fixed for the object's life is [[polymorphism-or-type-switch]]. A branch whose key names what kind of thing the switched-on object is (a shape, a square, a transaction) is [[polymorphism-or-type-switch]]; a branch whose key names a policy the object applies to compute one result, with that policy's parameters stored as fields of the object, is [[strategy-for-varying-algorithms]]. A branch whose key names which third-party product is configured, its arms calling that product's own API, is [[hide-third-party-apis]]; a branch whose arms only choose which concrete class to instantiate is [[factory-object-for-creation]]; several creation sites that each switch on the same discriminator to build different members of one family are [[abstract-factory]]. A switch whose arms only construct subclasses that override nothing but constants is [[subclass-that-differs-only-in-data]]; any other switch that only chooses which class to instantiate is [[factory-object-for-creation]].

The same type code switched on in several functions is [[polymorphism-or-type-switch]], which owns the sign; [[replace-conditional-with-polymorphism]] is the procedure for the repair. A special case tested in several functions of one calculation is [[polymorphism-or-type-switch]]; one sentinel value compared by several clients that mostly give it the same default answer is [[introduce-special-case]].

## When not to apply

- The arms are distinct operations (commands, menu actions) and the only common name would be vague; the book keeps such a switch.
- One `switch` on the type code where objects are created, in a factory, is the book's intended result (p. 447), not a finding.
- Outside an object-oriented setting the book stops at extracted routines dispatched by a `case` (p. 445). This wiki adds: in code organised around data and functions rather than objects, a closed set of variants matched in one place is the idiom; this page is `paradigm: oop`.
- **The variation is not real.** Larman's contraindication covers designing with interfaces and polymorphism for speculative future-proofing against an unknown possible variation (25.1, p. 584). A conditional in one place over a set of kinds that is not expected to grow is cheaper than a hierarchy. Hierarchy scaffolding with one implementation is [[do-not-force-a-design-pattern]]; code justified by a future need is [[replaceable-code-over-forecast]].
- This wiki reads Meyer's "almost always" as the book's citation of one expert, not as a measured rule. Fowler takes the opposite default: most conditional logic stays as `if/else` and `switch/case` (p. 303). This wiki resolves the two by the key and the arms. A switch on a type tag of an object whose arms are the per-kind versions of one operation (the first sign) is a finding even once, as McConnell, Weisfeld and Larman show it. A conditional on anything else, such as an input value, a flag or a range, is the ordinary conditional Fowler keeps, and the neighbour pages named under the signs own it.
- A special case tested in one place only. Fowler's motive for the base-and-variant refactoring is more special logic for the case (p. 311); this wiki notes that "about to introduce" is a forecast, not a sign, and applies the page where the repetition is already in the code.
- Fowler's criterion counts the functions sharing the dispatch (PDF p. 54); this wiki reads it as the strength of the finding, not its condition: a switch repeated across functions is the stronger case, and a single one is reported with the cheaper alternative, keeping that one switch, named beside the repair. Fowler sets no threshold.
- Where the set of operations grows more often than the set of kinds, putting each operation into every subclass spreads one change across all of them, and a switch in one place may be the cheaper shape. Neither book discusses this trade-off; it is this wiki's own, and it holds only while the switch on that type code stays in one place.

## Repair

1. Give the varying kinds one method with the operation's name (`draw()`, `complete()`), implemented per kind; where the arms were routines over a record, introduce a base class or interface and move each arm's body into the matching subclass.
   Name the operation after what varies, not after a type (`landedOn`, `getTaxes`); declare it abstract on the supertype unless there is a real default; give a kind that does nothing an empty method; pass in, as parameters, the objects the arms used. These details are Larman's (25.1, pp. 580-582).
2. Keep one `switch` on the type code where the object is built; in a larger system put it in a factory method (p. 446).
3. Replace the dispatching switch with a call to the polymorphic method. Where the same codes were switched on in several routines, each switch's arm becomes a method of the matching subclass.
4. For parallel hierarchies, let one hierarchy hold a reference to its counterpart, so a kind is added once, or merge them. This step is this wiki's own.
5. For a base case with variants: create the variant subclass and a factory that returns it when the special-case test holds, and override only the part that varies; the steps are on [[replace-conditional-with-polymorphism]].

## Before and after

```
switch shape.type:
    case CIRCLE: shape.drawCircle()
    case SQUARE: shape.drawSquare()
```

```
shape.draw()      // Circle.draw, Square.draw
```

Routines over a record, with creation moved into a factory:

```
while not done()
    data = read()
    switch data.kind
        DEPOSIT:    processDeposit(data)
        WITHDRAWAL: processWithdrawal(data)
        TRANSFER:   makeTransfer(data)
        default:    logError("unknown kind", data)
```

```
while not done()
    transaction = TransactionFactory.create(read())
    transaction.complete()

TransactionFactory.create(data)
    switch data.kind
        DEPOSIT:    return new Deposit(data)
        WITHDRAWAL: return new Withdrawal(data)
        TRANSFER:   return new Transfer(data)
        default:    return new UnknownTransaction(data)   // complete() logs the error
```

Larman's case, with a kind that does nothing:

```
takeTurn()
    ...
    switch location.type
        GO:          cash = cash + 200
        INCOME_TAX:  cash = cash - min(200, netWorth() * 0.10)
        GO_TO_JAIL:  location = board.jail()
        REGULAR:     // nothing
```

```
takeTurn()
    ...
    location.landedOn(this)

GoSquare.landedOn(player)        player.addCash(200)
IncomeTaxSquare.landedOn(player) player.reduceCash(min(200, player.netWorth() * 0.10))
GoToJailSquare.landedOn(player)  player.setLocation(jail)
RegularSquare.landedOn(player)   // empty: no special case at the caller
```

The remaining `switch` sits in the factory, which the limits above name as the intended result.

Fowler's base and variant, abridged:

```
class Rating
    captainRisk()
        r = 1 + (if history.size < 5 then 4 else 0) + losses()
        if voyage.zone == "china" and hasChinaHistory() then r = r - 2
        return max(r, 0)
    profitFactor()
        f = 2 + zoneBonus()
        if voyage.zone == "china" and hasChinaHistory() then
            f = f + 3 + (if history.size > 10 then 1 else 0)
        else
            f = f + (if history.size > 8 then 1 else 0)
        return f
```

```
function createRating(voyage, history)
    if voyage.zone == "china" and hasChina(history) then
        return ExperiencedChinaRating(voyage, history)
    return Rating(voyage, history)

class Rating
    captainRisk():  return max(1 + (if history.size < 5 then 4 else 0) + losses(), 0)
    profitFactor(): return 2 + zoneBonus() + historyLengthFactor()
    historyLengthFactor(): return if history.size > 8 then 1 else 0

class ExperiencedChinaRating extends Rating
    captainRisk():  return max(super.captainRisk() - 2, 0)
    profitFactor(): return super.profitFactor() + 3
    historyLengthFactor(): return if history.size > 10 then 1 else 0
```

## Source

- [[code-complete]], section 24.2, p. 554, and section 24.3, pp. 560 and 562: repeated case statements and parallel hierarchies as warning signs, the single case statement as no fault, and the two refactorings.
- [[code-complete]], pp. 144-145: the rule, both examples and the verdict on `DoCommand()`. Section 19.4, pp. 445-447: the subclass-plus-factory repair, the single creation switch and the Meyer citation.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 43 (each shape responsible for drawing itself), pp. 44-45 (abstract `getArea`, overriding, new classes added easily), pp. 46-47 (the stack of shapes, the standardised interface). Ch. 5, pp. 109-110 (the print/draw switch, the edit to every function's case for each new shape, after Tyma, Torok and Downing); ch. 7, pp. 144-148 (an object responsible for itself, `Triangle` added with no other code changed, `drawMe(Shape)`); ch. 8, p. 159 (the case statement a `Shape` holding all drawing code would need). The quotations were checked against `raw/`. This wiki's own for that part: the reading of "new classes easily" as no caller changing, and the operations-against-kinds trade-off.
- This wiki's own: the discriminating criterion, the parallel-hierarchy sign as phrased, repair step 4, the second sign and the routine-per-type wording of the first, the owner assignments, the paradigm limit, the reading of Meyer, and the pseudocode (the `UnknownTransaction` arm replaces the book's error branch so that `create` always returns an object).
- Fowler and Beck, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Repeated Switches", PDF pp. 93-94, with "Long Function", PDF p. 88, and "Primitive Obsession", PDF p. 93: the revision between editions, the reasons for narrowing the smell to the repeated switch, and the cost of adding a clause. The routing of a single big switch to [[keep-case-arms-short]] is this wiki's own.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 1, "Reorganizing the Calculations by Type" through "Status: Creating the Data with the Polymorphic Calculator", PDF pp. 43-54: the decay argument, the usefulness criterion, the two switches reduced to one factory, and the default in the superclass. This wiki's own for that part: the reading of the criterion as the strength of a finding.
- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.8, PDF p. 809: the payment case. 25.1 Polymorphism, PDF pp. 578-584: the principle and its corollary, the reasons, the other names, the NO-OP method, the abstract operation, the parameter passed to `landedOn`, and the contraindication on speculative future-proofing. This wiki's own for that part: the special-case-guard sign and the pseudocode, rewritten from Larman's pseudocode `SWITCH ON square.type`.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 10, "Replace Conditional with Polymorphism", PDF pp. 302-320: the two situations, the overuse limit, the remark on how inheritance is used, the base-and-variant example; the steps of extracting only the varying part are on [[replace-conditional-with-polymorphism]]. The e-book text layer drops minus signs, so the pseudocode restores them from the book's logic. This wiki's own for that part: the special-case sign as worded, the resolution against Meyer by key and arms, the reading of the usefulness criterion as strength, the forecast limit and the assignment against [[introduce-special-case]].
