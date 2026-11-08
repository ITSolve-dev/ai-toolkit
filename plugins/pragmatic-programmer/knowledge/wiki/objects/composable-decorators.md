---
title: Composable decorators
category: objects
summary: "Small objects that each wrap one other object and add one behaviour, nested into a single expression (new Sorted(new Unique(new Capitalized(...)))) instead of a long method doing all steps in sequence."
tags: [concept, decorator, composition, declarative]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-07
---

Bugayenko uses the term, which he believes he coined, for wrapper objects around other objects that become composable when stacked in layers (*Elegant Objects*, section 3.2, pp. 139-140). His example declares a sorted collection of unique capitalised file names, after a regular-expression replacement, from the files of a directory. This wiki's pseudocode of its shape:

```
names = Sorted(
  Unique(
    Capitalized(
      Replaced(
        FileNames(Directory("/var/users/*.xml")),
        "([^.]+)\\.xml", "$1"
      )
    )
  )
)
```

## What makes something a composable decorator

- Its behaviour is entirely determined by the object it encapsulates, to which it adds some behaviour; its state coincides with the state of that object (p. 140).
- It sometimes exposes the same interface as the object it wraps, but not necessarily: `Unique` is an iterable of strings wrapping an iterable of strings, while `FileNames` is an iterable of strings wrapping an iterable of files (p. 140).
- The expression does nothing when built; it only declares what `names` is. In a whole program, the pyramid of objects starts working when `app.run()` is called (p. 140). This wiki adds that, short of that, work starts when something asks the expression for its contents. See [[declarative-style]].

The book says most code in pure object-oriented software should look like this, and defines object-oriented programming as assembling large objects from smaller ones (pp. 140, 142). Static methods cannot be composed at all, which the book gives as one more reason against them (p. 142; see [[no-static-methods]]).

The book's discriminating criterion against a smart class: a decorator strengthens the methods of the interface it implements, a smart class adds methods (p. 111; see [[small-interface-with-smart-class]]). This wiki reads the caching decorator on [[constructors-without-code]] as the same device applied to repeated work.

## Using it

The book's working instruction, while languages lack the rest of the vision, is to stay away from long methods and complex procedures and to design micro-classes so they can be reused as elements of composition in larger objects (p. 142).

This wiki reads the pattern as a repair for a long method that performs a fixed sequence of transformations on one collection or value: each step becomes a class wrapping the previous one, and the order of steps is fixed by nesting rather than by line order, which removes the risk of reordering noted under [[temporal-coupling]].

## Trade-offs and failure modes

These are this wiki's own, except the one attributed to the reader's comment:

- Deep nesting is read inside out: the first step is the innermost. Readers used to pipelines that read top to bottom may misread the order.
- Each layer is a class, often in its own file. A reader's comment in the book objects that this spreads simple code across classes and files and adds throwaway objects (p. 144). This wiki adds that a transformation used once may not repay a class.
- Because nothing runs at construction, an error in an inner layer appears only when the outermost is consumed, and the stack trace runs through every layer.
- In a language with function composition or stream pipelines, the same decomposition is often expressed with functions; the book regards that as outside OOP (p. 127, footnote), and this wiki does not treat it as a violation. See [[transformation-pipeline-over-method-chain]].

This wiki assigns the neighbouring shapes as follows. A wrapper that holds one object of the same interface and adds one behaviour is [[composable-decorators]]; a wrapper that holds a list of them and combines their results is [[composite-same-interface-as-part]]. A wrapper with the subject's interface that may skip the subject or send the call elsewhere (a cache hit, a failover, a refused permission) is [[proxy]]; one that always calls the subject and adds to what goes in or comes out is [[composable-decorators]].

## Source

- [[elegant-objects]], section 3.2, subsection on composable decorators, pp. 139-142; reader comment p. 144; footnote p. 127; section 2.9, p. 111 for the smart-class contrast. The example is this wiki's pseudocode of the book's listing; the regular expression is reconstructed from noisy OCR and not checked against the page image.
- This wiki's own: reading the pattern as a repair for a long transformation method, the link to the caching decorator, and all trade-offs except the reader's objection.
