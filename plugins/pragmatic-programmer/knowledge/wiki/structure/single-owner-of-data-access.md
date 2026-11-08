---
title: One owner for direct access to stored data
category: structure
summary: "The same table name, file path, key prefix or record layout (column order, field offsets) appears in query or parse code in two or more classes or modules that are not its declared owner, instead of behind one class that owns it."
tags: [rule, information-hiding, data-access, coupling, encapsulation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Direct access to a body of stored data should belong to one class, and everyone else reaches the data through that owner's interface. McConnell states this twice. Among his reasons to create a class is a central point of control: using one class to read and write the database means that a switch to a flat file or in-memory data changes only that class (p. 150, paraphrase). In the architecture chapter he states it for a subsystem or class: «Прямой доступ к данным обычно следует предоставлять только одной подсистеме или классу» (p. 44; a word rejoined across a hyphenation break). The exception he allows is access classes or methods that present the data abstractly. He treats this as a case of [[information-hiding]] (p. 44, pointing to section 5.3).

## Rule

Give one class direct access to each body of data. Other code goes through access routines that present the data abstractly (pp. 44, 150).

The subsystem form of the rule (p. 44) is architecture, which this wiki takes as given from the project; this page applies the rule inside the module.

## Sign in code

This wiki reads the following as the sign:

- the same table name, file path, key prefix or record layout (column order, field offsets) appears in query or parse code in two or more classes or modules that are not the data's declared owner;
- or code outside the owner builds raw queries or byte layouts against data that the owner also writes.

This wiki assigns the neighbouring cases as follows. A table or record layout known by several modules is [[single-owner-of-data-access]], whatever product stores it; when both fire, one module is both the adapter and the owner. A vendor's client, query dialect or exception type named outside one adapter class, in code that also holds business logic or in the application's own signatures, is [[hide-third-party-apis]]. A single function reaching a database with the dependency hidden from its signature, with no second module knowing the same data, is [[global-data]]. A hand-written structure mirroring an external schema field by field is [[representational-duplication]].

## When not to apply

This wiki's own limits:

- **Reporting or migration code.** A read-only migration script or ad-hoc report, deliberately coupled to the schema and kept apart, may touch the data directly when it is the only such reader and is marked as such.
- **One small module.** A program small enough that the owner would be the whole program gains nothing from an extra owner class.
- **Data defined as a published contract.** An exchange file format with a schema is a public contract on purpose; readers depend on the published format, not on each other, and the format is the abstraction.

## Repair

This wiki's own:

1. Name the owner: the module that holds the schema or the layout.
2. Move every direct read and write into it, behind operations named for what callers need rather than for the storage.
3. Callers then depend on those operations, and a change of storage touches only the owner.

## Before and after

```
// before: billing and notifications both know the customer table
// billing
row = db.query("SELECT email, plan FROM customers WHERE id = ?", id)
if row.plan == "pro": charge(row.email, 30)

// notifications
row = db.query("SELECT email FROM customers WHERE id = ?", id)
send(row.email, message)
```

```
// after: one owner; callers ask for what they need
// customers (owner, the only module that names the table)
function contactOf(id): return db.query("SELECT email FROM customers WHERE id = ?", id).email
function planOf(id):    return db.query("SELECT plan FROM customers WHERE id = ?", id).plan

// billing
if customers.planOf(id) == PRO: charge(customers.contactOf(id), 30)

// notifications
send(customers.contactOf(id), message)
```

In the "after", the table name and its columns appear only inside the owner. How the owner itself gets `db` is the concern of [[global-data]], not of this page.

## Source

[[code-complete]], ch. 3, section 3.5 («Организация данных»), Russian edition, p. 44: the rule for a subsystem or class and its exception; ch. 6, section 6.4, p. 150: one class reading and writing the database as a central point of control. McConnell states the p. 44 rule as an architectural requirement; applying it inside the module is this wiki's own, as are the sign, the assignment of neighbouring cases, the limits, the repair and the pseudocode.
