---
title: Object persistence
category: objects
summary: "Concept: what saving an object stores is its state (attribute values), not its behaviour or its invariants; a composite saved without its parts comes back incomplete, and a native serialized form ties every reader to the class definition and its private fields, while a mapped portable form is a contract declared apart from them."
tags: [concept, persistence, serialization, encapsulation, coupling]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

**Object persistence** means saving an object's state so that the same application, or another one, can rebuild the object later. Weisfeld starts from an ordinary object's lifetime: an object created by an application lives exactly as long as that application runs, and goes out of scope when it ends unless it has been written to some persistent store (p. 229). He calls the result a «постоянный объект», one that can be restored and used «независимо от того или иного приложения» (p. 229).

## What is saved: state, not behaviour

The book defines an object's state as the values of its attributes (p. 229), and that is what is persisted. Methods are not stored: the class definition has to be present at both ends of the channel, so both the program that writes a `Person` and the one that restores it need the `Person` class (p. 235). Conceptually nothing changes for the programmer, the book adds: attributes and behaviour stay encapsulated together even where the physical implementation does not match the conceptual model (p. 235).

This wiki reads that as follows: a persisted record is data only. The record does not carry the object's invariants; they hold again only if the code that rebuilds the object enforces them, as a constructor does ([[class-invariant]]).

## Decomposition, reconstruction, object graphs

An object is not a flat list of primitive variables, so it cannot be written the way a variable can. It has to be decomposed into pieces a store can hold and reassembled, and the book calls reconstruction the remaining big problem (p. 231). Composition makes it harder: a `Car` that contains `Engine`s and `Wheel`s has to be saved and restored as a whole (p. 231). Who owns the nested parts is the question [[aggregation-vs-association]] and [[ownership-of-nested-structures]] settle.

The book counts it a gain when a built-in mechanism writes the whole object in one call: «Это намного проще, чем записывать каждый атрибут поодиночке» (p. 233). Weisfeld presents this as another case of separating interface from implementation ([[interface-and-implementation]]): the caller needs only two guarantees, that the object is written as one unit and that it comes back exactly as saved (p. 234).

## Trade-off: native format against portable format

The book compares two strategies (pp. 232, 236-238):

- **A language's native serialization** is quick to write, and proprietary: the same language has to be at both ends of the channel (p. 232). A proprietary approach can be efficient and fast, but «переносимость будет отсутствовать» (p. 236).
- **A neutral document format** (the book's example is XML) can in theory be read by any language or platform. The cost is a more complex class, because each persisted field gets an explicit mapping to the document (p. 236).

The book also shows a field excluded from the stored form: in its C# listing `Score` is marked to be ignored (p. 244). The class therefore decides which of its fields form the persisted state.

This wiki's own reading of the choice is that the stored form is an interface. With a native format every reader is coupled to the class definition itself, so renaming or restructuring a private field can break files written earlier. With an explicit mapping the stored form becomes a contract declared apart from the private fields, which costs more code and leaves the class free to change. Weisfeld does not discuss versioning or schema evolution. Whether the stored form should be readable text at all is [[plain-text-for-persistent-data]]; checking a stored document against its declared structure on the way back in is [[validate-exchanged-data-against-a-declared-schema]].

## Relational databases

The book notes a mismatch between objects composed of other objects and relational stores built of tables (p. 239). Object databases fit the object model better but lost out, because converting existing relational data is too expensive and too risky: migration is painful, its effect on code cannot be predicted, and when something fails it is hard to tell whether the database or the code is at fault (pp. 239-240). Mapping between objects and tables is presented as the way out (p. 240). How an application is split around its database is architecture and is out of scope here.

## Failure modes

- **Partial save of a composite.** The outer object is saved and the objects it contains are not, so it comes back incomplete (p. 231).
- **Reader without the class.** Data in a native format is handed to a program that lacks the same class definition, or is written in another language (pp. 232, 235).
- **Silently swallowed input in a mapped accessor.** The book's sample setter returns without doing anything when it receives `null` (p. 237), and the book calls this validation. This wiki's own observation is that a setter which ignores an invalid value hides the failure from the caller; the repair is [[crash-early]].

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 12, pp. 229-244, via [[object-oriented-thought-process]]. Page 229 is inferred, because `raw/` marks the chapter opener only by its PDF page. The quotations were checked against `raw/`. This wiki's own: the reading of a persisted record as data without invariants, the stored form as an interface and its coupling to private fields, the criticism of the silently ignoring setter and the routing to neighbouring pages.
