---
title: Liskov substitution principle
category: objects
summary: "A subclass method keeps the base method's name and signature but changes what the result means (sign, unit, direction), or throws 'not supported', so callers holding the base type branch on the subtype or correct the result."
tags: [rule, inheritance, lsp, contracts, protected-variations]
paradigm: oop
sources: [code-complete, object-oriented-thought-process, larman-applying-uml-and-patterns]
created: 2026-11-06
updated: 2026-11-07
---

Public inheritance is a claim that the derived class *is* a more specialised version of the base. McConnell grounds this on Liskov (1988) and quotes Hunt and Thomas's wording: «Клиенты должны иметь возможность использования подклассов через интерфейс базового класса, не замечая никаких различий» (p. 141). He restates it as: «все методы базового класса должны иметь в каждом производном классе то же значение» (p. 141). The base class states expectations and constraints the derived class must meet (p. 141, after Meyers).

Larman's *Applying UML and Patterns* gives Liskov's formal statement, in English: "If for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T" (25.4, p. 594). He places it under [[protected-variations]], as the principle that formalizes protection across "different implementations of an interface, or subclass extensions of a superclass" (p. 594). His informal reading is that software referring to a type T "should work properly or as expected with any substituted implementation or subclass of T" (p. 594), and his example is `addTaxes(calculator, sale)`, which must keep working whichever `ITaxCalculatorAdapter` it is passed. This wiki draws the consequence: the protection that polymorphism gives callers holds only while every implementation honours what the callers of T rely on, so the rule applies to implementations of an interface as much as to subclasses.

## Rule

Derive only when the derived class keeps the whole contract of the base interface. «Если производный класс не собирается полностью придерживаться контракта, определенного интерфейсом базового класса, наследование выполнять не стоит» (p. 141). The book's reason: with LSP kept, inheritance lets a reader think about the common attributes and forget the details; once the reader must remember semantic differences between subclasses, inheritance only adds complexity (p. 141).

The worked case: `Account` with `CheckingAccount`, `SavingsAccount` and `AutoLoanAccount`. `InterestRate()` on the first two returns what the bank pays the client; on the loan account it returns what the client pays the bank, so a caller would have to flip the sign. By LSP, `AutoLoanAccount` should not derive from `Account` (p. 141).

Weisfeld's *The Object-Oriented Thought Process* gives the same failure for an action rather than a result. A Basenji is a dog that yodels instead of barking (p. 135). Overriding `bark()` so that it yodels is rejected: the result «не окажется интуитивно понятным, поскольку некоторые люди ожидают, что метод, позволяющий выполнять соответствующее действие, будет иметь имя bark()» (p. 138). The is-a sentence (a Basenji is a dog) holds; the behaviour behind the inherited name does not.

## Sign in code

This wiki reads the sign as any of these, all visible in the code at hand:

- An overriding method returns a value with the same type but a different meaning: opposite sign, other unit, other direction of a flow.
- A caller holding the base type tests the runtime subtype and then corrects or reinterprets the result of a base method.
- An override throws "not supported" or narrows the accepted inputs of the base method.
- An override's body does something other than what the inherited method's name says (`bark()` whose body yodels, p. 138).

This wiki assigns the neighbouring cases as follows. An override that does nothing or returns a neutral value is owned by [[override-that-does-nothing]]; a type test that only corrects or reinterprets the result of a base method, such as flipping its sign for one subtype, is [[liskov-substitution-principle]], and any other branch whose key is an object's runtime type or class name is [[avoid-introspection-and-casting]], however many arms. A non-empty override of a method the parent implements is owned by [[final-or-abstract]]; one that throws "not supported", narrows the inputs the base method accepts, changes what the result means, or does something other than what the inherited method's name says is [[liskov-substitution-principle]]. A superclass member of the project's own that only one subclass, or a few, read, write or call, with no override in the others, is [[push-down-method-and-field]]; an empty override of it in the other subclasses is [[override-that-does-nothing]], and an override that throws or rejects is [[liskov-substitution-principle]].

## When not to apply

- An empty override where doing nothing *is* that kind's correct behaviour, and callers of the base rely on no effect, is not a violation: Larman gives `RegularSquare.landedOn` an empty body on purpose (25.1, p. 582). The test of whether callers rely on an effect is this wiki's; the empty override as a shape is owned by [[override-that-does-nothing]].
- Subtypes that differ in how they compute a result but not in what it means (each account computes interest differently, all return what the bank pays) satisfy the rule; differing implementation is the point of overriding. This limit is this wiki's reading.
- The rule governs public inheritance used as a type relation. A class that shares code without ever being used through the base type is classified by [[choose-an-alternative-to-inheritance]] instead. This limit is this wiki's own.
- Where the base contract itself documents the operation as optional (it may throw 'unsupported'), throwing is within the contract. This limit is this wiki's own.

## Repair

Take the class out of the hierarchy and give it its own interface, or move the change higher in the hierarchy so the base no longer promises the meaning the subclass breaks; the book names containment or a change at a higher level of the hierarchy (p. 141). For an action only some kinds perform, Weisfeld moves it into intermediate classes or an interface (p. 136), the repair [[override-that-does-nothing]] lays out. For the account case this wiki's repair is a separate loan type, or a base method whose name states the direction (`interestPaidToClient`).

## Before and after

```
class Account        { rate(): Percent }      // paid by bank to client
class LoanAccount extends Account { rate(): Percent }  // paid by client to bank

total = 0
for a in accounts:
    r = a.rate()
    if a is LoanAccount: r = -r
    total += r
```

```
class DepositAccount { rateEarned(): Percent }
class LoanAccount    { rateCharged(): Percent }   // not a subtype of DepositAccount

total = sum(d.rateEarned() for d in deposits) - sum(l.rateCharged() for l in loans)
```

## Source

- [[code-complete]], ch. 6.3, Russian edition, p. 141: the rule, the quotation of Hunt and Thomas, the Account example and the verdict on `AutoLoanAccount`; the repair "containment or a change higher in the hierarchy".
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 7, pp. 135-138: the Basenji, the rejected bark-to-yodel override, the split into intermediate classes or an interface. The quotation was checked against `raw/`. This wiki's own for that part: the different-action sign as worded.
- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 25.4 Protected Variations, subsection on LSP, PDF p. 594: the Liskov quotation, the informal reading, the `addTaxes` example and the placement under Protected Variations; 25.1, PDF p. 582: the empty `landedOn`. Larman gives no violation; this wiki's own for that part: the extension to interface implementations and the test of whether callers rely on an effect.
- This wiki's own: the first three signs, the owner assignment, the limits on differing implementations, on public inheritance as a type relation and on documented optional operations, the renamed methods in the repair, and the pseudocode.
- Quotations restored from a noisy text layer (line-break hyphens joined); check against the page image.
