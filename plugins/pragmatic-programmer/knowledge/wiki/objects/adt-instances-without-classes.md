---
title: Multiple ADT instances without classes
category: objects
summary: "Procedural module exposes `SetCurrentX(id)` and then operations that act on a hidden 'current' instance; choose between passing an id, passing the data record, or implicit current state."
tags: [decision-rule, procedural, global-state, adt, interface]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

In a language without classes, an [[abstract-data-type]] that must handle several instances needs explicit services to create and destroy instances, and every other service must be designed to work with more than one instance (p. 127). McConnell names three ways to tell a service which instance to use (pp. 128-129):

1. **Pass an instance id on every call,** for example `SetSize(fontId, points)`. There is no "current font". The ADT keeps all the data and the client keeps only the id. The cost is an extra parameter on every routine.
2. **Pass the data record on every call.** The client holds a `Font` record and hands it to each service. Its fields are reachable but are to be touched only through the services, which McConnell calls keeping the structure «в закрытом виде». The services need no lookup by id. The cost is that client code can see, and come to depend on, implementation details.
3. **Implicit current instance:** `SetCurrentFont(fontId)`, then calls without an id. McConnell's advice is to use it «с большой осторожностью». It may ease a simple application, but in a complex one the whole call graph must track which font is current. He adds that a better alternative can always be found, whatever the size of the application (p. 129).

This wiki states the deciding question: which party should hold the instance's state, and how much of the representation may leak? With option 1 the ADT holds it and nothing leaks. With option 2 the client holds it and the representation is visible. With option 3 hidden global state holds it.

## Sign in code

- A module exposes `SetCurrentX(id)` or `SelectX(id)`, and its other operations take no instance argument and act on whatever was selected last.
- Callers wrap calls in select/restore pairs, such as saving the current id, selecting another and restoring it, to use a second instance.
- Under option 2: callers read or write fields of the record that the module's functions are meant to own.

This wiki assigns the neighbouring case as follows. A hidden current instance selected through the module's own API is this page's; a function reaching a module-level variable or singleton that no select call sets is [[global-data]].

## When not to apply

- In an object-oriented language the choice is made for you: each object is an instance (p. 127).
- A module that holds exactly one instance and offers no create/destroy services, such as process-wide configuration, needs none of the three. This limit is this wiki's own; even then, option 3's hidden state is the thing to keep out of other modules.
- How the ADT stores instances internally is free. The three options constrain only its outside (p. 129).

## Repair

Replace option 3 with option 1 (an id) or option 2 (an opaque record). Remove `SetCurrentX` and add the instance argument to each service. Under option 2, keep the record's layout out of the callers' reach by whatever means the language offers. This wiki suggests an incomplete type or a handle, not a public struct, as the closest procedural equivalent of a closed structure.

## Before and after

```
// before: hidden current instance
selectFont(titleFont)
setBoldOn()
selectFont(bodyFont)
setSizeInPoints(10)
```

```
// after: instance passed explicitly
setBoldOn(titleFont)
setSizeInPoints(bodyFont, 10)
```

## Related

- [[abstract-data-type]]
- [[uniform-access]]

## Source

[[code-complete]], ch. 6.1, Russian edition, pp. 127-129: the three options and their costs. This wiki adds the deciding question, the signs, the owner assignment, the second limit and the handle suggestion in Repair.
