---
title: Provide operations with their opposites
category: objects
summary: "A public operation has no counterpart where the domain implies one: `add` without `remove`, `turnOn` without `turnOff`, `enable` without `disable`, `open` without `close`."
tags: [rule, class-interface, completeness]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

Most operations have opposites. If one operation turns a light on, you will probably need one that turns it off. If one adds an item to a list, items will likely need removing. If one activates a menu item, another should probably deactivate it. When designing a class, check each public method for whether its opposite is needed. McConnell adds that you should not create opposites without reason, but you should check (p. 133).

This wiki adds the reasoning, which the book does not spell out. A missing opposite forces callers to undo an effect by reaching around the interface: resetting a field directly, rebuilding the object, or calling a lower-level routine. That leads straight into [[semantic-encapsulation-violation]].

## Sign in code

- A class has `add`, `open`, `acquire`, `enable`, `subscribe` or `push` with no matching `remove`, `close`, `release`, `disable`, `unsubscribe` or `pop`, and callers undo the effect by other means: they reassign a collection, set a flag directly, or construct a fresh object to get back to the initial state.

This wiki reads the missing counterpart alone as a question, not a finding; the workaround at a call site is what makes it one. A direct write that undoes the effect of a public operation with no counterpart is [[provide-opposite-operations]]; any other bare write of a field is [[uniform-access]]. A resource acquired and never released on some path is [[finish-what-you-start]]. An existing counterpart of an operation in use (`remove` beside a used `add`, `close` beside a used `open`) is kept even with no caller: [[minimal-but-complete-functionality]] does not report it. Whether to add a missing counterpart is [[provide-opposite-operations]], which requires a caller's workaround first.

## When not to apply

- The domain forbids the reverse. A posted ledger entry is corrected by a new entry, not removed, and an append-only log has no delete. The missing opposite is then the rule, and adding it would break an invariant. This limit is this wiki's own.
- Immutable values: the "opposite" is a new value, not a mutating method. This limit is this wiki's own.
- No caller needs the reverse. The book warns against adding opposites without reason (p. 133). This limit is about adding one; this wiki does not read it as a reason to delete a counterpart that already exists.

## Repair

Add the counterpart operation to the class's interface, keeping it at the same level of abstraction. Then replace the callers' workarounds with calls to it.

## Before and after

```
// before
menu.activate(item)
...
item.state = INACTIVE      // caller reaches around the class
```

```
// after
menu.activate(item)
...
menu.deactivate(item)
```

## Related

- [[class-interface-coherent-abstraction]]

## Source

[[code-complete]], ch. 6.2, Russian edition, p. 133. The reasoning paragraph, the workaround condition on the sign, the owner pointers (including the split with [[uniform-access]]), the first two limits and the reading of the third as about adding only are this wiki's own.
