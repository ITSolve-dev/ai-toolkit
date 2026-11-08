---
title: "Observer: the publisher knows its subscribers only by interface"
category: structure
summary: "A model or domain class holds a field typed as a concrete window, mailer or other reacting class and calls it after changing state, so each new reaction means editing the publisher; make it notify registered listeners through an interface it owns."
tags: [rule, observer, publish-subscribe, gof, low-coupling, events]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Observer, also called Publish-Subscribe or the Delegation Event Model, is the GoF pattern for this problem: "Different kinds of subscriber objects are interested in the state changes or events of a publisher object, and want to react in their own unique way" while "the publisher wants to maintain low coupling to the subscribers". The solution: "Define a 'subscriber' or 'listener' interface. Subscribers implement this interface. The publisher can dynamically register subscribers ... and notify them when an event occurs" (26.10, p. 631).

## Rule

Larman's case is a window that must refresh when a sale's total changes. He rejects having `Sale` call the window directly. His setting is Model-View Separation, which this wiki takes as the project's architecture rather than prescribing it; under it, model objects "should not know about view or presentation objects" (p. 630). With Observer, `Sale` keeps a list of `PropertyListener`s; the window registers itself through `addPropertyListener`, and `Sale` notifies every listener when the total changes. The window then updates its own widget.

What the pattern buys and what it does not:

- Coupling remains, but "it is a loose coupling to an interface independent of the presentation layer" (p. 633).
- No subscriber has to be present, so the list can be empty, and subscribers can be added or removed at run time. Larman says "coupling to a generic interface of objects that do not need to be present, and which can be dynamically added (or removed), supports low coupling" (p. 633).
- One publisher may have zero to many subscribers of many classes, each reacting in its own way. His alarm-clock example notifies windows, beepers and a watchdog from one event (p. 635).
- The event is usually a class filled with event data (source, property name, old value, new value) and passed as the parameter of the notification message (pp. 635-636).

The use is not limited to UI; Larman names GUI widget event handling as the most common use (p. 634). The pattern "is based on Polymorphism, and provides Protected Variations" by protecting the publisher from knowing the class and number of the objects it notifies (pp. 636-637). See [[protected-variations]] and [[low-coupling]].

## Sign in code

This wiki's reading of the sign:

- A domain or model class holds a field typed as a concrete window, mailer or other reacting class and calls it after changing state.
- Adding another reaction to the same change means editing the publisher's method.
- The publisher's module imports UI or infrastructure classes only to tell them something changed.

This wiki assigns the neighbouring cases as follows. Domain code that calls a dialog or reads widgets in the middle of a computation is [[logic-testable-without-ui]]; a model that pushes a finished state change into a concrete reacting object it holds is [[observer-publisher-knows-only-interface]]. A model that calls concrete reacting classes directly, with no listener interface yet, is [[observer-publisher-knows-only-interface]]; once a publisher has listeners, how the notification runs is [[observer-vs-publish-subscribe]]. Choosing among an observer, publish-subscribe, a state machine or an event stream for reacting code is [[event-driven-code]].

## When not to apply

- There is one fixed reaction, and it is part of the publisher's own job. An explicit call is easier to follow than an indirection. A log or metrics call a class makes about its own work is such a reaction, not a subscriber. This limit is this wiki's own.
- The order of reactions or their failures matter to the publisher's correctness. Observer hides who is called and in what order, so a failure in one listener can leave the others unnotified or the publisher half-updated; an explicit sequence of calls makes that order visible. This limit is this wiki's own; Larman does not discuss failures in listeners.
- A registered listener list with one subscriber registered at one place is [[do-not-force-a-design-pattern]].

## Repair

1. Define a listener interface in the publisher's own terms (`onPropertyEvent(event)`), not the subscriber's.
2. Give the publisher `addListener` and `removeListener`, and a private method that notifies every listener with an event object.
3. Replace the direct calls with that notification. Have each former callee implement the interface and register itself.
4. Whoever subscribes owns unsubscribing: registration without de-registration keeps subscribers alive as long as the publisher lives, which leaks objects such as closed windows. This step is this wiki's own.

## Before and after

```
class Sale
  field frame: SaleFrame
  method addLineItem(item)
    lineItems.add(item)
    frame.totalField.setText(getTotal())
```

```
interface PropertyListener
  method onPropertyEvent(event)

class Sale
  field listeners: List<PropertyListener>
  method addPropertyListener(l)     listeners.add(l)
  method removePropertyListener(l)  listeners.remove(l)
  method addLineItem(item)
    old = getTotal()
    lineItems.add(item)
    publish(PropertyEvent(this, "total", old, getTotal()))
  private method publish(e)
    for l in listeners  l.onPropertyEvent(e)

class SaleFrame implements PropertyListener
  method onPropertyEvent(e)  totalField.setText(e.newValue)
```

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.10, PDF pp. 630-637. The problem, the solution, the loose coupling to an interface, the empty listener list, many subscribers and event objects are Larman's. Model-View Separation is named here only as the setting of his example. The signs, the owner assignments, the limits, repair step 4 (the de-registration failure mode) and the pseudocode are this wiki's own.
