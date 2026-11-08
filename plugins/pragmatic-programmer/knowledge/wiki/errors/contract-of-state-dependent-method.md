---
title: Contract of a method whose behaviour depends on control state
category: errors
summary: "A client-facing postcondition, docstring or test that names a class's private control state (\"if in state 2, the alarm hours increase\") leaks the state to clients and over-specifies; a per-state branch that does what the method's general contract excludes breaks it, as a weakening override would."
tags: [concept, design-by-contract, state-machine, polymorphism]
paradigm: oop
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

An [[automated-class]] owes its clients a contract of the same kind ordinary classes in the system carry. The book: «Если обыкновенные классы в системе снабжены контрактами, то и автоматизированные классы должны иметь контракты точно такого же вида» (p. 110). The difficulty is that each method's specification has to cover the reaction in every control state, while the control states are an implementation detail (p. 110). The general discipline is [[design-by-contract]].

## The dilemma

The book's example is the alarm clock's `h` ("hours") button. One possible postcondition: if the clock is in the first or third state, the hours of the current time increased, and if it is in the second, the hours of the alarm increased. The book grants that this is very informative, but «он раскрывает внутреннюю информацию об управляющих состояниях», and for clients it «скорее всего, будет являться чрезмерной спецификацией» (p. 110). It offers weaker versions that name no state: either the current hours or the alarm hours increased; or the minutes did not change and the two hour counts did not both increase. It then leaves open what a client actually needs to know: «Стандартных рекомендаций по этому поводу не существует» (p. 110).

## The relation that does hold

Whatever the general contract is, behaviour in one control state is a special case of the complex behaviour. So a contract written for one state «должен быть сильнее, чем общий контракт на сложное поведение» (p. 110). The book compares this with the substitution principle, where a descendant's specification must be stronger than its ancestor's (pp. 110-111; see [[liskov-substitution-principle]]). It draws two conclusions (p. 111):

- complex behaviour can be seen as a special form of polymorphism: an entity with complex behaviour resembles a polymorphic reference to which objects of different subtypes are attached at run time, one subtype per control state;
- this view leads straight to the State pattern ([[switch-on-state-vs-state-pattern]]), in which the subtypes are of a class describing the control state, not of the entity itself. The book says the extra indirection is needed because «иначе невозможно реализовать механизм переходов между состояниями» (p. 111).

The book calls the fit between automated classes, contracts and inheritance unexplored. It considers "inheritance of automata" an incorrect notion, because an automaton is not an abstraction in its own right, and the inheritance of automated classes a fruitful open field (p. 111).

## Using it on code

This wiki reads the book's two points as review checks. The book poses them as questions, not as rules.

- A client-facing postcondition, docstring or test that names the private control state (`if state == 2`) ties clients to the implementation, as the book's first postcondition does. A state-neutral statement of what can and cannot change, like the book's weaker versions, is the alternative it sketches.
- Each per-state branch must satisfy the method's general postcondition. A branch that does something the general contract excludes breaks the contract, in the same way an overriding method that weakens its ancestor's guarantee does.
- This wiki's own limit: where the control state is part of the interface on purpose, for example a protocol whose clients are expected to query the stage, naming it in the contract is not a leak. The book does not discuss this case.
- This wiki's own limit: a unit test of the automated class itself may name its states, since it pins the implementation; the leak concerns contracts, and tests of other classes or acceptance tests, that name the state.
- This wiki assigns the neighbouring case as follows. An assertion on incidental output or internal state is [[brittle-tests]], including a test that reads the private control-state field. A client-facing contract or docstring stated in terms of a class's control state is [[contract-of-state-dependent-method]].

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, ch. 3, section 3.2, pp. 110-111 ([[automata-based-programming]]). The "Using it on code" section, including its two limits and the assignment against [[brittle-tests]], is this wiki's own transfer; the book leaves the choice of contract as an open question.
