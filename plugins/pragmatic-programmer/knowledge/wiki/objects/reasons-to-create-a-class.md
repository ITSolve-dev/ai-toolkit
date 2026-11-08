---
title: Reasons to create a class
category: objects
summary: "A class that cannot be justified by any of the listed reasons (hiding a detail, isolating complexity or a likely change, a central point of control, grouping parameters passed together) is a candidate to remove."
tags: [concept, responsibilities, information-hiding, abstraction]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell argues that modelling real-world objects is not the only reason to create a class, nor the main one (p. 148). «Снижение сложности — самая важная причина создания класса» (p. 149): create a class to hide information so you need not think about it once the class is written (p. 149).

## The reasons

The book's list (p. 152, explained on pp. 148-151):

- **Model real-world objects** and **abstract objects**: `Shape` abstracts `Circle` and `Square`; finding good abstractions is one of the main problems of object-oriented design (p. 149).
- **Reduce complexity** and **isolate complexity**: a tangled algorithm, large data set or intricate protocol kept in one class is easier to debug and to replace (p. 149).
- **Hide implementation details**, from a database access path to whether a field is a number or a string (p. 149). See [[information-hiding]].
- **Limit the effect of changes**: isolate areas of likely change such as hardware dependencies, input/output, complex data types and business rules (p. 149). See [[anticipate-likely-changes]].
- **Hide global data** behind access methods, which lets the structure change, lets access be monitored, and often reveals the data is really some object's data (p. 150). See [[global-data]].
- **Streamline parameter passing**: one parameter passed to several routines suggests those routines belong in a class that holds it as data (p. 150).
- **Make central points of control**: one class that reads and writes the database means a switch to files or memory touches one class (p. 150). See [[single-owner-of-data-access]].
- **Facilitate reusable code**, with the NASA note that reusable classes were identified at the end of projects rather than designed for reuse, to avoid gold-plating (pp. 150-151).
- **Plan for a family of programs**: put each part expected to vary in its own class (Parnas, 1976); the author's insurance programs were customised per client by rewriting a few such classes (p. 151).
- **Package related operations** where no stronger reason exists, noting that packages, namespaces or modules can do this too (p. 151).
- **Accomplish a specific refactoring**, such as splitting a class, hiding a delegate, removing a middle man (p. 151).

The classes to avoid on p. 152 are on [[god-class]] and [[class-with-only-data-or-only-behaviour]].

## How this wiki uses the list

This wiki reads the list as a test for a class under review rather than a menu for creating one: if a reviewer cannot name which reason a class serves, the class is a candidate to merge or inline. This wiki also gives the parameter-passing reason a concrete sign: the same argument passed through several functions of one module (its reading of p. 150; see [[limit-parameter-count]]). The likely-change, reuse and family-of-programs reasons rest on a forecast (areas of likely change, p. 149; whether another program may need the code, p. 150; a family of programs, p. 151), so by the charter this wiki does not accept them as a sign; a class kept only for one of them is justified by a variation or a second user that already exists, not by one predicted (see [[replaceable-code-over-forecast]]). "Package related operations" is the book's catch-all, so nearly any class passes with it; this wiki does not accept that reason alone as passing the test when the class holds state.

## Source

- [[code-complete]], pp. 148-152: the list and each reason's explanation; quotation from p. 149 restored from a line-break hyphen.
- This wiki's own: reading the list as a review test, the parameter-passing sign, the remark on forecasts, the restriction on the packaging reason.
