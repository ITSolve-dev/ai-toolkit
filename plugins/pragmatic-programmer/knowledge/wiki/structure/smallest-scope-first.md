---
title: Start with the smallest scope
category: structure
summary: "A variable declared wider than its uses: a routine-level local read only inside one loop, a field read and written only within a single method call, a non-public field nothing outside its class (and no subclass) touches."
tags: [rule, scope, visibility, information-hiding, encapsulation]
paradigm: any
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Scope is the stretch of a program in which a variable is known and can be used (p. 238). McConnell's rule is to pick the narrowest scope that works and widen it only when a use demands it. The reason is an asymmetry: scope is «гораздо сложнее сжать, чем расширить» (p. 244). Turning a global into a class variable is harder than the reverse, and so is turning protected members into private ones (p. 244).

Weisfeld's *The Object-Oriented Thought Process* (ch. 5) ties minimal scope to abstraction and hiding implementation: the idea is to «локализовать атрибуты и поведения настолько, насколько это представляется возможным», so classes become easier to maintain, test and extend (p. 108). His example is a class-level `temp` that only `swap()` uses: «Нет никаких причин для того, чтобы он был на уровне класса» (p. 109), and it moves into the method (p. 109). On static attributes his claim that object-oriented code has no global data (p. 108) is read cautiously on [[global-data]].

## Rule

The book's order of preference, from narrowest to widest (p. 244): local to one loop, then local to one routine, then a private member of a class, then protected, then package (where the language has packages), and only as a last resort global. Where data must be shared with other classes, the book prefers access routines to exposing the data, and bare global data is rarely needed, if ever (p. 244).

The book frames the choice as two philosophies, "convenience" and "intellectual manageability" (p. 244). Some programmers make many variables global so they need not worry about parameter lists and scope rules. The book's answer is that this optimizes the writing of a program over its reading: «Максимизация области видимости может облегчить написание программы» (p. 244). A program in which every routine can touch any variable at any time is harder to understand. To understand one routine you then have to understand every other routine sharing the same data, which makes the program hard to read, debug and change (pp. 244-245). The book ties this to information hiding: the more you hide, the less you must keep in mind at once (p. 244). See [[information-hiding]].

## Sign in code

- A local is declared at the top of a routine and every reference to it falls inside one loop or block.
- A field is written and read only within a single call of a single method, and starts each call from a value that method sets. It is a local variable stored on the object.
- A field marked protected or package-visible is referenced only from inside its own class, with no subclass or other module in the code base touching it.

This wiki assigns the neighbouring cases as follows. This page owns a declaration whose scope is wider than every use of it in the code in view. A `for` index declared outside its loop and not read after it is [[smallest-scope-first]]; one read after the loop is [[do-not-use-loop-index-after-loop]]. A field written and read only within a single call of a single method is [[smallest-scope-first]]; a field written by one method only so that a later method can read it is [[pass-state-dont-hoard-it]]. A protected field a subclass reads or writes is [[private-data-not-protected]] or [[inheritance-tax]]. A protected field referenced only from inside its own class, with no subclass touching it, is [[smallest-scope-first]]. A bare read or write of a field is [[uniform-access]], and a public method that does not fit the class's abstraction is [[minimize-member-accessibility]]. A function body that reaches a mutable module-level name, a static field or a singleton is [[global-data]], and this page adds only the order in which to narrow it. Distance between references within one scope is [[keep-variable-live-time-short]].

## When not to apply

The limits below are this wiki's own:

- A library's public or protected member exists for callers and subclasses outside the code in view. Its use cannot be seen from the repository, and the sign needs knowledge of who else uses it, which the charter does not accept as a sign. Judge it from the published interface instead.
- A field that caches an expensive value across calls is state the object owns, even if one method reads and writes it.
- A framework may require members to be visible for injection, serialization or test access. That is the framework's convention, and the project's tooling decides it.
- Moving a loop variable to the narrowest block can conflict with a value that must survive the block. Narrow to the scope the value really needs.

## Repair

1. Move a routine-level local into the loop or block that uses it.
2. Turn a field that lives within one call into a local of that method, passing it as a parameter to the helpers that need it.
3. Lower the visibility of a field to private when nothing outside the class uses it.
4. Where several classes must share a value, put it behind access routines on one owner rather than exposing it (p. 244). See [[global-data]] and [[uniform-access]].

## Before and after

Before:

```
class Exporter
    protected buffer

    function export(rows)
        this.buffer = ""
        for row in rows
            this.buffer = this.buffer + format(row)
        write(this.buffer)
```

After:

```
class Exporter
    function export(rows)
        buffer = ""
        for row in rows
            buffer = buffer + format(row)
        write(buffer)
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 5, pp. 108-109: localising attributes and behaviour, the class-level `temp` moved into `swap()`; the quotations were checked against `raw/`.

McConnell, *Code Complete*, Russian edition, via [[code-complete]], section 10.4: the definition of scope (p. 238); start with the most restricted scope, the shrink-versus-widen asymmetry and the order of preference (pp. 243-244); convenience against intellectual manageability, writing against reading, information hiding, access routines and bare globals (pp. 244-245). This wiki's own: the signs as worded, the assignment against the neighbouring pages, all the limits, repair steps 1-3, and the pseudocode.
