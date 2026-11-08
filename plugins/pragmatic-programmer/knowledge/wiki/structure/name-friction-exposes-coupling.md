---
title: Name friction exposes needless coupling
category: structure
summary: "A local bound to a whole object from a lookup, read for one field and dropped, in a module that uses the object's type nowhere else: the code depends on more than it needs, so ask for the value itself."
tags: [rule, coupling, naming, interfaces]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A name that refuses to settle can mean that the code is holding the wrong thing. *The Pragmatic Programmer* shows a small rename ending in a different function call, with less [[coupling]] than before: the trouble with the name was trouble with the dependency.

## Rule

Thomas and Hunt walk through one line of code (p. 317). The developer fetches the account owner, renames the variable because the first name seems useless, finds the second name redundant, and then asks what the code is actually for. The user story says to send that person an email, so the code needs an address: «Может быть, сам владелец счета мне вообще не нужен?» (p. 317). The call changes to one that returns the address directly.

The authors state the result: the feedback loop at the level of a variable name improved the design, «сократив связывание данного фрагмента кода с фрагментом, который оперирует счетами» (p. 317).

This wiki takes the rule as: when a name will not settle, stop renaming and state what the code needs, and if it needs a part of what it fetches, ask for that part.

The authors say the rename improved the architecture of the whole system. This wiki reads that more narrowly. The fragment still calls the accounts code; what falls away is its knowledge of the owner as a concept and of how to get from an owner to an address.

## Sign in code

The rename history is not visible in code, so the source's trigger cannot serve as a sign. The signs below are this wiki's own.

- A local receives a whole object from a lookup, one field of it is read, the local is then dropped, and the module uses that object's type nowhere else, so narrowing removes an import or a type reference.
- The same shape in a parameter, with the same condition: a function takes an object and reads one field of it, and that is the module's only use of the type.
- The name of that local is the generic name of its type (`user`, `item`, `data`) while the next line uses it for something narrower. This strengthens the first two signs and is not a sign alone.

## When not to apply

The source states no limit. The limits here are this wiki's own.

- The code reads several fields of the object. The object is then what it needs.
- The narrower query would be a new method on the owning module, written for one caller and repeated per field (`email_of_x`, `phone_of_x`). The caller's coupling falls while the module's interface grows. This wiki sets the line at the second such query on one object: from there, the caller keeps the object.
- The object is also used for a check on the way, such as whether the record exists or the actor may see it. Narrowing the query has to keep that check.

## Repair

1. State the purpose of the line in one sentence, taken from the task and not from the code.
2. Name the value that sentence needs.
3. Replace the lookup and the field read with a query returning that value, and put the path to it behind the module that owns it.
4. Remove any import or type reference the caller no longer uses.

The cost is one more function on the owning module, and the trade-off is the second limit above.

## Before and after

Before:

```
customer = customer_of(order_id)
send_sms(customer.phone, text)
```

After:

```
phone = contact_phone_of(order_id)
send_sms(phone, text)
```

The step is one turn of [[small-steps-with-feedback]].

## Source

[[pragmatic-programmer]]: Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, p. 317 (the worked example and the claim of reduced coupling).

This wiki's own: the generalisation into a rule, the narrowed reading of the authors' claim, all of `## Sign in code`, all of `## When not to apply`, the numbered repair, and the pseudocode. The book gives one worked example and states no rule beyond the feedback loop itself. Related: [[name-by-role]], [[train-wreck]].
