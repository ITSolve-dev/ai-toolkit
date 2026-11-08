---
title: Replace direct data manipulation with an abstract data type
category: objects
summary: "Client code sets fields, flag bits or unit-ambiguous numbers of a shared structure directly (`font.attribute = font.attribute or 0x02`, `font.size = 16`) in several places, or digs into a widely used map or nested record on both sides of an assignment (`customers[id].usages[y][m] = v`), instead of calling named operations."
tags: [rule, abstraction, encapsulation, duplication, adt]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

## Rule

When several parts of a program manipulate the fields of one data structure directly, group the data with the routines that operate on it into an [[abstract-data-type]], and have the rest of the program call those routines. McConnell calls the alternative the ad hoc approach. He says it is not bad in itself, only replaceable by something better (p. 123). Its cost is that client code must control the data members directly, which spreads similar lines across the whole program (p. 123).

Two corollaries from the same section:

- Name the wrapper for what the low-level structure represents, not for its mechanism: a set of employees, not a stack (p. 126).
- Size does not exempt a type. Two operations, on and off, already justify an ADT (p. 127).

Fowler's *Refactoring* gives the same move as **Encapsulate Record** (2nd ed., ch. 7, PDF pp. 183-194). An object hides what is stored and what is calculated: "The user of the object doesn’t need to know or care which is stored and which is calculated" (PDF p. 184), and it allows a field to be renamed gradually, by offering the old and new names until callers have moved (PDF p. 184). He singles out records that do not declare their fields, such as hashmaps and dictionaries, whose shape can be learned only from the code that builds and uses them: "This isn’t a problem if they are only used in a small section of a program, but the wider their scope of usage, the greater problem I get from their implicit structure" (PDF p. 184). For a large nested structure, the part that matters most is the updates: "Getting them visible and gathered in a single place is the most important part of the encapsulation" (PDF p. 191).

## Sign in code

- The same structure's fields are assigned from several unrelated routines: `x.field = ...` with no routine of the structure in between.
- Bit operations with literal masks on a shared field, such as `flags = flags or 0x02`, appear at call sites.
- A numeric field whose unit is not stated is assigned in several places, as in `size = 16` (pixels or points?), or a second field holding the same quantity in another unit has been added beside it (`sizeInPixels`, `sizeInPoints`) (p. 123).
- The structure is passed into every routine that works with it (p. 124).
- A nested map or list structure that callers dig into on both sides of an assignment (`customers[id].usages[year][month] = amount`), repeating the same path in several functions. This sign is this wiki's reading of Fowler's customer-usage example (PDF pp. 189-191).
- A map with no declared fields, used outside the small section that builds it, whose shape (start and end, or start and length?) can be learned only by reading where it is created. This sign is this wiki's reading of Fowler (PDF p. 184).

This wiki assigns the neighbouring cases as follows. Fields of a structure with no routines of its own written from several call sites: [[replace-direct-data-manipulation-with-adt]]. Direct access beside access routines that already exist, or routines named in the implementation's terms: [[access-routines-at-domain-level]]. An object with methods of its own whose field is read or written outside it: [[uniform-access]]. A structure made global so routines can reach it is [[global-data]]. A collection field leaking through one object's getter or setter is [[encapsulate-collection]]. Loose values passed together, with no structure yet, are [[group-related-data-into-a-structure]]. Free functions or client code deriving values from a record that is not yet a class are [[combine-functions-into-class]]; fields of a structure with no routines of its own written from several call sites are [[replace-direct-data-manipulation-with-adt]]. A path of indexing into a plain data structure with no routines of its own is [[replace-direct-data-manipulation-with-adt]]; a chain of steps through objects returned by other objects is [[train-wreck]].

## When not to apply

- This wiki adds these limits; McConnell states none. The structure is a plain record of values with no invariant, no unit and no encoding to protect, and it is built and read in one place: wrapping it adds a layer that hides nothing.
- The data crosses a boundary as data, such as a message, a row or a serialised payload, and the code at that boundary is the only code touching it. The ADT belongs in the code that works with the data past that boundary.
- **A map used only in a small section.** Fowler says implicit records are not a problem "if they are only used in a small section of a program" (PDF p. 184).
- **Immutable values.** Fowler: "If I have an immutable value, I can just have all three values in my record", and copying a field is enough to rename it (PDF p. 184).
- **Full recursive encapsulation of a large structure.** Turning every nested level into its own class is "a lot of effort for a large data structure", and "not really needed if I don’t access that much of the data structure" (PDF p. 194). Encapsulating the updates and handing out copies for reads is the lighter option.
- In functional code the same goal is met by an opaque type with a module of functions over it. Mutating setters are not the point; hiding the representation behind named operations is.

## Repair

1. Collect every direct access to the structure.
2. Name each distinct intent: `SetBoldOn`, `SetSizeInPoints`, `SetSizeInPixels` (pp. 124-125).
3. Move the data inside the ADT and make those operations its only access.
4. Express units in operation names, or pick one unit for the interface.
5. Rename the type from its mechanism to what it holds.

Fowler's order for Encapsulate Record (PDF pp. 185-194):

1. Encapsulate the variable holding the record behind functions with deliberately ugly, searchable names (`getRawDataOfOrganization`); they are meant to have a short life ([[encapsulate-variable]]).
2. Replace its content with a class that wraps the record, with an accessor returning the raw record. Test.
3. Move callers to the object one by one, the writers first: extract each update into a function and move it onto the class (`setUsage(id, year, month, amount)`). For readers, move read functions as well, or hand out a copy or a read-only view.
4. Remove the raw accessor and the searchable functions. Test.
5. For a shallow record, fold the wrapped data into the object's own fields. That breaks the link to the input record, which matters "if a reference to it runs around"; if the data stays wrapped, copy it on assignment (PDF p. 188).

To check that every update was found, make the raw accessor return a deep copy: with good tests, a missed modification breaks one (PDF p. 192). Trade-offs, as Fowler gives them: one method per kind of read gives the class "an explicit API that captures all the uses made of it", but "this can be a lot of code for lots of special cases" (PDF p. 193); handing out a copy is simple, but it costs the copying, which he would measure before worrying about, and it confuses a client that expects its changes to reach the original (PDF pp. 193-194).

## Before and after

```
// before: callers in many places
font.attr = font.attr or 0x02
font.size = 16            // pixels? points?
```

```
// after: callers only name the intent
font.setBoldOn()
font.setSizeInPoints(12)
```

In the after version a typo can only be a wrong operation name. In the before version it can be a wrong field, operator or mask (p. 124).

A nested structure, after Fowler's customer-usage example:

```
customers = loadJson(file)

function recordUsage(id, year, month, amount)
    customers[id].usages[year][month] = amount

function compareUsage(id, laterYear, month)
    later   = customers[id].usages[laterYear][month]
    earlier = customers[id].usages[laterYear - 1][month]
    return (later, later - earlier)
```

```
class CustomerData
    private data
    setUsage(id, year, month, amount): data[id].usages[year][month] = amount
    usage(id, year, month): return data[id].usages[year][month]
    rawData(): return deepCopy(data)

function compareUsage(customerData, id, laterYear, month)
    later   = customerData.usage(id, laterYear, month)
    earlier = customerData.usage(id, laterYear - 1, month)
    return (later, later - earlier)
```

## Related

- [[abstract-data-type]]
- [[uniform-access]]: the same problem seen from the class side.
- [[storage-independent-names]]

## Source

[[code-complete]], ch. 6.1, Russian edition, pp. 122-127: the font example, the list of benefits, the guidance on low-level types and simple items. The signs as worded, the `## When not to apply` section and the owner assignments are this wiki's own reasoning, except the three limits attributed to Fowler.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 7, "Encapsulate Record", PDF pp. 183-194: stored versus calculated, gradual renaming, records without declared fields and their scope (also the small-section limit), the updates-first priority, the immutable-value and recursive-encapsulation limits, the mechanics, the deep-copy check and the read options with their trade-offs. This wiki's own for that part: the nested-path and implicit-map signs, and the second pair of pseudocode, after his example.
