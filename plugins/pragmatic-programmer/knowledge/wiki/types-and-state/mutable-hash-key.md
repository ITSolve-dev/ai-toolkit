---
title: Mutable hash key
category: types-and-state
summary: "An object used as a key in a hash map or set has a mutator called on it after insertion, or its class computes equality and hash from fields that are not final or that hold a mutable container, so the container holds duplicate or unreachable keys."
tags: [rule, identity-mutability, hashing, mutation]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-03
---

Bugayenko calls this problem identity mutability: two objects compare as equal, or unequal, and then one of them changes state, so the earlier comparison is no longer true (p. 78). The case with the worst consequences is a key inside a hash container. The container computed its slot from the key's old state and is never told about the change.

## Rule

An object used as a key in a hash map or set must not change after insertion. The book's way to guarantee that is to make the key class immutable (see [[immutable-objects]]). Then the only way to change what is in the map is to put in a new key object (p. 79).

In the book's example, keys `$5` and `$10` go into a `HashMap`, then `five.mul(2)` is called, and the map prints two `$10` keys: «Ассоциативный массив стал некорректным после нашего вмешательства» (p. 78). After that, `map.get(five)` may return either value (p. 79). The book stresses that, with all but the last line removed, a reader could not work out why the map holds duplicates (p. 79).

## Sign in code

- A class that overrides equality and hash from fields that are not final, or from final fields that hold a mutable container, and that is used as a map key or set element in the code at hand.
- A mutator call on a variable that was earlier passed to `put`/`add` of a hash container, with no remove-and-reinsert around it.

This page owns a mutation of an object that is a hash key: the mutated object was put into a hash map or set earlier in the code at hand, or its class's equality/hash reads the mutated field and the class is used as a key in the code at hand: [[mutable-hash-key]]. The general sign "a field reassigned after construction", where that condition does not hold, belongs to [[immutable-objects]].

## When not to apply

- This wiki's own limit: if equality and hash are identity-based (not overridden), mutation does not move the key, and this defect does not arise, although [[immutable-objects]] may still apply.
- Likewise, if the mutated fields take no part in equality or hash, the container stays consistent. This limit is also this wiki's own.
- This wiki's own limit: an ORM or framework entity whose equality reads mutable fields because the framework requires it. There the first sign alone is no finding; only the second, a mutation after insertion into a hash container, is.

## Repair

1. Make the key class immutable, so that "changing" a key means creating a new object and putting it into the container.
2. If that is impossible, remove the key, mutate it and reinsert it, and confine this to one place.

## Before and after

```
map = new HashMap()
five = new Cash(5)
map.put(five, "five")
map.put(new Cash(10), "ten")
five.mul(2)           // the key changes in place; the map now holds two $10 keys
```

```
map = new HashMap()
five = new Cash(5)     // Cash is immutable
map.put(five, "five")
map.put(new Cash(10), "ten")
ten = five.mul(2)      // a new object; the map is untouched
```

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 2.6, pp. 78-79; see [[elegant-objects]]. This wiki's own: the signs about equality and hash fields, the ownership condition, all three limits and the pseudocode. The book shows only the corrupted map. Related: [[keep-objects-small]], where state is identity.
