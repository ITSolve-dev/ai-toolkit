---
title: Prefer deep copy unless shallow is proven necessary
category: types-and-state
summary: "A copy constructor or clone assigns the original's mutable reference fields to the copy (often with reference counting or 'still shared' checks around it), with no measurement in view justifying the sharing; or, the reverse, a copy deep-copies immutable values or independent entities such as a shared customer."
tags: [rule, copying, aliasing, performance]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

A deep copy copies an object's data members; a shallow copy usually just points or refers to the original, though the exact meanings vary (p. 148). Fowler calls the two reference objects and value objects (p. 148).

Weisfeld's *The Object-Oriented Thought Process* frames the same choice from the reference side: «Просто скопировав ссылку, вы не скопируете структуры данных или объект, к которому она ведет» (p. 85). A bitwise (shallow) copy duplicates only the references, so original and copy point at the same sub-objects; a deep copy follows every reference and copies what it reaches, possibly across many levels, and the copy itself can carry significant overhead (p. 85). Getting a full copy means writing code that creates all the sub-objects (p. 85). He cites Meyers' *Effective C++* and Gilbert and McCarthy here. His class-design guidelines return to it: a plain bitwise copy may not be what the class needs, so how its objects are copied has to be designed (ch. 5, p. 108). The comparison side of the same problem is [[object-equality]].

## Rule

When in doubt, make deep copies (p. 148). The motive for shallow copies is usually speed, but several copies of large objects rarely slow a program noticeably, and programmers are poor at guessing which code causes problems: «Повышение сложности едва ли можно оправдать сомнительным улучшением быстродействия кода» (p. 148). Deep copies are easier to write and maintain; a shallow copy also needs reference counting, safe comparison, safe destruction and so on, and that code is a source of errors (p. 148).

Weisfeld adds the cost McConnell discounts: McConnell holds that deep copies rarely slow a program noticeably, Weisfeld that a deep copy of a wide tree of references can carry significant overhead. This wiki resolves them by what each reference points to, which neither book states: an owned mutable part is copied deeply, whatever the cost, unless a measurement shows the copy is the bottleneck; an immutable part or an independent entity is shared, so the overhead Weisfeld warns of is paid only where sharing would be wrong.

This wiki adds: where the language's memory manager removes the release half of the cost, the aliasing half remains, so the rule still applies to mutable members.

## Sign in code

- A copy constructor or clone that assigns reference fields of the original to the copy, where those fields are mutable.
- Reference counts or "is it still shared" checks written around such copies.
- The reverse: a copy that follows references to immutable values or to independent entities (a shared customer, a parent, a service), paying Weisfeld's overhead (p. 85) and duplicating an identity that should stay shared.

This wiki assigns the neighbouring case as follows. Who frees nested parts of a container is [[ownership-of-nested-structures]].

## When not to apply

- This wiki adds: when the shared members are immutable, sharing them is safe and is not a shallow copy in the harmful sense. See [[immutable-objects]].
- A measurement shows the deep copy is the bottleneck; the book's own condition is «если не доказано обратное» (p. 148).
- This wiki adds: a member that refers to an independent entity or collaborator (the order's customer, a parent, a service), not to a part the object owns, is shared by design; deep-copying it would duplicate an identity. Only owned mutable parts are copied. A project's stated copy semantics overrides the rule.

## Repair

Copy mutable members when copying the owner; drop the reference-counting code that becomes unnecessary; or make the members immutable so sharing them is safe.

## Before and after

```
class Order { lines: MutableList ; copy(): Order(lines = this.lines) }   // shared
o2 = o1.copy(); o2.lines.add(x)   // o1 changes too
```

```
class Order { lines: MutableList ; copy(): Order(lines = this.lines.copy()) }
```

## Source

- [[code-complete]], p. 148: definitions, the rule, the performance argument, the cost of shallow copies, Fowler's terms.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 3, p. 85, and ch. 5, p. 108 (copying designed, not left bitwise): copying a reference does not copy the object, shallow and deep copy, the overhead, the need to write code that creates the sub-objects, the citations of Meyers and of Gilbert and McCarthy. The quotation was checked against `raw/`. This wiki's own for that part: the resolution of the cost disagreement by what each reference points to, and the reverse sign.
- This wiki's own: the signs, the immutable-member and shared-collaborator limits, the memory-manager remark, the repair's third option and the pseudocode.
