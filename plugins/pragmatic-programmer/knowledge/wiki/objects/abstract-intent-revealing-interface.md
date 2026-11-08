---
title: Abstract, intent-revealing interface
category: objects
summary: "Two or more call sites drive one object through the same fixed sequence of its low-level public calls (go, turnRight, turnLeft, stop; open, seek, read, close) to reach one outcome, instead of one call naming the caller's goal (takeTo(airport))."
tags: [rule, interface, abstraction, reuse]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Weisfeld argues that reusable classes tend to have interfaces that are more abstract than concrete: concrete interfaces are very specific, abstract ones more general (ch. 2, pp. 59-60). His example is a taxi. "Take me to the airport" is a far more useful interface than separate "turn right", "turn left", "go" and "stop", because the customer needs only to get to the airport (p. 60). The passenger may not know the route, and which route the driver takes does not matter to the passenger (p. 61). The abstract request can be reused in any city, while its implementation «будет разной в Чикаго, Нью-Йорке и Кливленде» (p. 61). The concept behind this page is [[abstraction]]; the split it protects is [[interface-and-implementation]].

The book hedges the claim: a very abstract interface is not always more useful than a very concrete one, though often it is (p. 60), and a very useful concrete class that is not reusable at all can be built, which in some situations is fine (p. 60). It also warns that designers too often shape a class to fit a technology model, so that it works technically rather than being convenient for its users (p. 63).

## Rule

Give callers operations that state what they want done, at the level of their goal, and keep the steps inside the class (pp. 60-61, 63). This wiki's reasoning: when every caller spells out the steps, the route is fixed at each call site, so a change of route (a new city, a new storage) edits every caller instead of one method.

## Sign in code

- Two or more call sites invoke the same sequence of one object's public methods, in the same order, to reach one outcome, and nothing between the calls depends on the caller.

This wiki assigns the neighbouring cases as follows. A comment that tells callers to call one method before another is [[temporal-coupling]] or [[semantic-interface-to-programmatic]], as those pages divide it. A public interface that mixes domain operations with the container's or library's own is [[mixed-abstraction-levels-in-interface]]. Public methods named after storage or mechanism rather than outcome are [[storage-independent-names]] and [[name-by-role]]. A method whose name names one behaviour while its body also performs a second one, as the book's `enterTaxi()` that also takes the fare (p. 65), is [[routine-names]], which owns a name that omits what the body does; splitting it is [[routine-cohesion]]. Outside code that reads the object, decides and writes back is [[tell-dont-ask]]. This page owns a repeated sequence of the object's own calls. A repeated sequence of one object's own public calls at several call sites is [[abstract-intent-revealing-interface]], whose repair moves it into that class; any other fragment repeated verbatim at several call sites is [[dry]]. The same call sequence repeated with only literals changing, stating a table of facts, is [[program-close-to-the-domain]].

## When not to apply

The book's hedges on p. 60 are the first limit; the rest are this wiki's own.

- **The callers combine the steps differently.** If different callers use the steps in different orders or subsets, the steps are the right interface, and one goal-level method would fix a single combination. The sign requires the same sequence repeated.
- **A deliberately low-level class.** A class whose job is to expose primitives, such as a driver or a byte buffer, is concrete by design (p. 60).
- **One call site.** With a single caller there is no repeated sequence, and lifting it into the class has no second user to justify it yet.
- **The project's convention fixes the abstraction level of a layer.** That convention decides.

## Repair

Move the repeated sequence into the class as one public method named for the caller's goal. Make the steps private where no other caller uses them ([[minimize-member-accessibility]]). Replace each call site's sequence with the one call.

## Before and after

```
// caller A
cab.go()
cab.turnRight()
cab.turnLeft()
cab.stop()

// caller B: the same four calls
cab.go()
cab.turnRight()
cab.turnLeft()
cab.stop()
```

```
// caller A and caller B
cab.takeTo(airport)

class Cab
  public takeTo(destination)
    route = planRoute(destination)   // differs per city
    drive(route)
  private planRoute(destination)
  private drive(route)
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 2, pp. 60-61 (abstract against concrete interfaces, the taxi), p. 63 (the user's point of view against the technology model) and p. 65 (one behaviour per interface, `enterTaxi()`), via [[object-oriented-thought-process]]. This wiki's own: the reasoning about the fixed route, the sign, the owner assignments (including sending the bundled-behaviour shape to [[routine-names]]), the limits other than the p. 60 hedge, the repair and the pseudocode.
