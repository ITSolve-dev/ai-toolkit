---
title: Minimise the accessibility of classes and members
category: objects
summary: "A method is public though it does not fit the class's abstraction: made public 'because it only uses public methods', added to the interface to make one particular client's code easier to write, or a step of a public operation (turnRight under giveDestination) declared public though only the class's own methods call it."
tags: [rule, encapsulation, class-interface, access-modifiers, information-hiding, minimal-interface]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

Minimising accessibility is one of the rules that support encapsulation. When unsure whether a member should be public, private or protected, some authors advise the strictest level that works (Meyers 1998, Bloch 2001). McConnell endorses that, but holds a different question more important: which choice best preserves the integrity of the interface's abstraction? If exposing the method fits the abstraction, make it public. If unsure, hiding more is generally better than hiding less (p. 135).

Two corollaries from the same section:

- **Do not make a method public just because it uses only public methods.** That fact is irrelevant. Ask whether exposing it fits the abstraction (p. 138).
- **Favour read-time convenience over write-time convenience.** Even during initial development, code is read far more often than written. Adding a method that fits the abstraction poorly, just to make work on one client easier, is in McConnell's words «первый шаг к беде» (p. 138).

McConnell also warns against friend classes in general. They are occasionally useful in disciplined form, for example in the State pattern, but usually they break encapsulation and enlarge the code you must hold in mind at once (p. 137). That warning is recorded here only as a pointer, because the construct is tied to particular languages.

### Weisfeld: start from the minimal interface

Weisfeld's *The Object-Oriented Thought Process* states the same rule from the side of the class's users, and more strictly. The interface should be designed so that it comes out «самым минимальным из возможных» (p. 91). Give users only what they will definitely need; start from a minimal interface; it is better to add interfaces later, once users really need them, than to give them more at the start (p. 62). His "extreme" version is to start with no public interface at all and wait for users to come back saying «Эй, мне нужна эта функциональность». He adds: «Никогда не предполагайте, что определенному пользователю что-то требуется» (p. 57). In chapter 5 he calls providing the minimal public interface perhaps the most important task in designing a class, and names its two failures: an **incomplete** interface, with which users cannot finish their work, and an **unrestricted** one, which lets them reach unnecessary or even dangerous behaviour and leads to debugging and to problems with integrity and security (pp. 101-102). «Пользователи вашего кода не должны ничего знать о его внутренней работе» (p. 102).

The steps of the work are implementation. In his `Cabbie` the public `giveDestination` calls private `turnRight` and `turnLeft`; a second example is an internal encryption method called only from inside the class: «закрытые методы являются строго частью реализации и недоступны другим классам» (p. 97). What a cabbie had for breakfast is behaviour a `Supervisor` has no need of, so it stays private (p. 103). The minimal set is a starting point, not a goal: a PC system unit with no monitor or keyboard is minimal and useless, so interfaces are added at once (pp. 62-63). Where the interface turns out too narrow for a new application, the book notes that a new class built by inheritance or composition over the existing one can extend the interface (p. 102).

The two books disagree on one case, and this wiki resolves it per setting. McConnell makes a member public when it fits the abstraction, even with one caller (p. 135); Weisfeld adds nothing until a user asks. Where a caller in view uses a member that fits, both books keep it public. Where a member fits the abstraction but nothing calls it, Weisfeld's rule decides: it is not added in new code, and in existing code it is [[minimal-but-complete-functionality]]. Where a new need does not fit the abstraction, McConnell's corollary above forbids the widening, and this wiki takes Weisfeld's extension in a new class as the repair. The concept under both is [[interface-and-implementation]].

## Sign in code

- A public method is called from exactly one outside caller in the codebase and does something that caller needed, in that caller's terms, not the class's.
- A public helper is called in the codebase only from inside the class, such as a step of another public method's work (`turnRight()` called by `giveDestination()` in Weisfeld's `Cabbie`, p. 97).
- In a diff: a member's visibility was widened, for example private to public or internal, in the same change that added a new client.

This wiki assigns the neighbouring cases as follows. A bare read or write of a field is [[uniform-access]]; a public method serving a different purpose from the rest of the interface is [[class-interface-coherent-abstraction]]. This page owns a public method that fits no caller but one, or that has callers only inside the class. A public operation with no caller anywhere, inside the class or out, is [[minimal-but-complete-functionality]] (delete it). One whose only callers are inside its own class, or that serves one outside caller in that caller's terms, is [[minimize-member-accessibility]] (narrow it). Such a method is not reported on [[public-methods-implement-interfaces]] until it has been narrowed or found to fit the abstraction. The other shapes of a too-wide interface have their own owners: a public field, or one written from outside, is [[uniform-access]]; an accessor pair for every field is [[no-getters-and-setters]]; a setter or a returned mutable collection that lets a caller break a rule between fields is [[class-invariant]]; a sequence of public steps that callers repeat to reach one goal is [[abstract-intent-revealing-interface]].

## When not to apply

- A method of an API published to clients outside the codebase: its callers cannot be counted from the code in view. This limit is this wiki's own.
- Visibility widened only for tests is a separate trade-off, decided by the project's testing convention, not by this rule. This limit is this wiki's own.
- A method that fits the abstraction is public even if only one caller uses it today. The test is fit, not the number of callers (p. 135).
- A member that a real caller uses is not a violation because the interface grew past its first minimal set; Weisfeld expects the first set to need widening (p. 62).
- A member that a framework, serializer or injector reaches by reflection or convention has a caller the reader does not see. The project's convention decides. This limit is this wiki's own.

## Repair

Make helpers private, leaving public only the operation that clients ask for (p. 97). For a method added for one client, move the logic to that client, or to a class whose abstraction it fits, and keep the original interface unchanged.

## Before and after

```
// before: added so ReportScreen could format a row
class Employee
  name(); address()
  public formatForReportRow() -> string
```

```
// after
class Employee
  name(); address()
class ReportScreen
  private formatRow(employee)
```

A step of a public operation made public (Weisfeld's `Cabbie`, p. 97):

```
class Cabbie
  public giveDestination(place)
    turnRight()
    turnLeft()
  public turnRight() ...
  public turnLeft() ...

// no caller outside Cabbie calls turnRight or turnLeft
```

```
class Cabbie
  public giveDestination(place)
    turnRight()
    turnLeft()
  private turnRight() ...
  private turnLeft() ...
```

## Related

- [[public-methods-implement-interfaces]]

## Source

- [[code-complete]], ch. 6.2, Russian edition, pp. 135, 137-138. The signs, the owner assignments, the published-API limit and the test-visibility limit are this wiki's own.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 57 (start with no public interface, never assume a user needs something), pp. 62-63 (the rules for a minimal interface, the PC example), p. 91 (the interface as minimal as possible), p. 97 (private implementation methods, `turnRight`, encryption), pp. 101-103 (the most important task, incomplete against unrestricted, users knowing nothing of the internals, extending in a new class, the breakfast example). The quotations were checked against `raw/`. This wiki's own for that part: the per-setting resolution against *Code Complete*, the `Cabbie` sign as worded, the owner assignments of the other too-wide shapes, the framework limit and the `Cabbie` pseudocode.
