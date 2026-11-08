---
title: A local variable should not shadow a field
category: naming
summary: "A local variable declared in a method with the same name as a field of its class, so a bare name means the local and the field is reached only through this.count; or one method writing both count and this.count."
tags: [rule, scope, shadowing, this]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Weisfeld describes attributes at three scopes: local to a method, per object, and per class (ch. 3, p. 78). Inside a method a local variable can carry the same name as an object attribute. His `Number` class has a field `count` and a local `count` in each of two methods, which makes «трех полностью отдельных областях памяти» named `count` (p. 81). In a method, the bare name refers to the local, and the field is reached only as `this.count`. The author himself finds the keyword choice odd: «Выбор слова this в качестве ключевого, возможно, является неудачным» (p. 81).

## Rule

The book presents shadowing as one of the things scope allows (p. 81), not as a rule against it. This wiki draws the rule: inside a method, do not give a local variable the name of a field it is not meant to stand for. This wiki's reasoning: a reader who sees `count = 1` has to check the enclosing scopes to know which memory changes, and an edit that deletes the local declaration silently redirects every bare use to the field.

## Sign in code

- A local variable declared in a method body with the same name as a field of the class.
- A method that writes both `count` and `this.count`.

This wiki assigns the neighbouring cases as follows. Two different names that differ by one character are [[names-differ-by-more-than-a-character]]; a local whose declaration is wider than its uses is [[smallest-scope-first]]. This page owns one name bound at two scopes in one method.

## When not to apply

- A constructor or setter parameter named after the field it initialises (`this.name = name`). This is a widespread convention, the link between the two is intended, and the field is set at once. The project's convention decides.
- A language that reaches fields only through an explicit receiver (`self.count`) has no bare-name ambiguity; the rule does not apply.
- A language or linter in the project that already forbids or flags shadowing of fields: the tool owns the check, and this page adds nothing.

## Repair

Rename the local after what it holds in this method (`start`, `delta`, `partialCount`). If the local was meant to be the field, delete the declaration and use the field.

## Before and after

```
class Number
  field count

  method reset()
    var count = 0
    count = count + 1      // the local
    this.count = count     // the field
```

```
class Number
  field count

  method reset()
    var start = 0
    count = start + 1      // only the field is named count
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 3, pp. 78-81, via [[object-oriented-thought-process]]: the three scopes, the `Number` example and the remark about `this`. The rule, its reasoning, the signs, the owner split, the limits, the repair and the pseudocode are this wiki's own, because the source describes shadowing without prescribing against it.
