---
title: Externally controlled identifier
category: types-and-state
summary: "A phone number, email, postal code, passport or tax number serves as the key of a record or as the reference between records."
tags: [rule, identity, data-modelling, decoupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

An identifier issued by someone else can change for reasons that have nothing to do with your system. The book raises this while asking how decoupled a design is from changes in the real world (p. 74).

## Rule

The book's wording is «не полагайтесь на свойства объектов, неподвластные вашему контролю» (p. 74). Its example is a phone number used as a customer identifier, and what happens when the phone company reassigns area codes. Its list of such identifiers: postal codes, social security or passport numbers, email addresses and internet domains, all of which can change at any moment for any reason (p. 74).

## Sign in code

- A phone number, email, postal code, national number or domain is the primary key of a record.
- Other records reference a record through such a value.
- A cache or map is keyed by such a value and used as identity.

## When not to apply

The limits are this wiki's own, since the source states none:

- The value itself is the subject, as in a list of email addresses to unsubscribe, where a record for each address is what the code means.
- A lookup by the external value is not identity. Finding a customer by phone number is fine, so long as records then refer to each other by an identifier the system owns.

## Repair

The source names the danger and not the change. This wiki's repair: issue an internal identifier that means nothing and is never reassigned, make it the key and the target of references, and keep the external value as an ordinary attribute that may be updated.

## Before and after

Before:

```
record Customer
    phone: Text              # key

record Order
    customer_phone: Text
```

After:

```
record Customer
    id: CustomerId           # issued here, never reassigned
    phone: Text

record Order
    customer_id: CustomerId
```

A renumbered phone now changes one attribute of one record.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 10, p. 74, via [[pragmatic-programmer]]. This wiki's own: the signs, the limits, the repair, and the pseudocode. Related: [[representation-that-fits-by-coincidence]].
