---
title: Access routines at the level of the problem domain
category: structure
summary: "Callers mix direct access to a shared structure (node = node.next, queue[front], stack.array[stack.top], count = count - 1) with access routines like PushStack() on the same data, or the routines are named in the implementation's terms, so the code speaks in the implementation's terms and the routines' checks are skipped at the direct sites."
tags: [rule, access-routines, information-hiding, abstraction-level, encapsulation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* asks two things of the routines that guard shared or global data (section 13.3): name them in the problem domain's terms, and route **every** operation on the data through them, never only some. The book presents them as the main approach to the problems of [[global-data]] (Russian edition, p. 330) and as the basic technique of abstract data types and [[information-hiding]] (p. 331).

## Rule

«Разрабатывайте методы доступа в области определения задачи, а не на уровне деталей реализации.» (p. 333). Keep all access to a structure at one level of abstraction: if it is initialised with `InitStack()` and filled with `PushStack()`, it is also read with `PopStack()` and not with `array[stack.top]` (p. 333).

The book's reasoning (pp. 331-334):

- **Each check lives in one place.** Writing `stack.array[stack.top] = newElement` invites forgetting the overflow check. Written once inside `PushStack()`, the check runs every time without anyone remembering it.
- **The representation can change.** If a better implementation of the structure turns up, only the access routines change.
- **The code says what it means.** `node = node.next` states what the structure does and, implicitly, which entity it stands for (the next account, employee or rate). The book calls that too heavy a burden for one assignment. `NextAccount(account)` states only the latter. `if PageFull()` in place of `if lineCount > MAX_LINES` documents the purpose of the test.
- **Inconsistency costs comprehension.** When the hard operations (inserting into a priority queue) sit in routines and the easy ones (`eventCount = eventCount - 1`) are written inline, the book calls the result an ugly, non-parallel use of the structure (Table 13-2, pp. 333-334). It names the same mix of routine and direct access an inconsistent representation that is harder to understand (p. 333).

## Sign in code

- Where access routines for a structure exist, code outside its owner still indexes its array, follows its links or adjusts its counter: `x = x.next`, `queue[front]`, `count = count - 1`.
- The same structure is used through routines at some sites and by direct field or index access at others.
- An access routine's name repeats the representation (`GetNodeNext`, `ArrayAt`) where callers are asking a domain question (`NextEmployee`, `HighestPriorityEvent`).

This wiki assigns neighbouring cases as follows. Whether data should be global at all is [[global-data]]. A structure made global so routines can reach it is [[global-data]]. Once access routines exist, their naming and their consistency are this page's. Fields of a structure with no routines of its own written from several call sites: [[replace-direct-data-manipulation-with-adt]]. Direct access beside access routines that already exist, or routines named in the implementation's terms: [[access-routines-at-domain-level]]. An object with methods of its own whose field is read or written outside it: [[uniform-access]]. One body of stored data whose schema or layout is known in several modules is [[single-owner-of-data-access]]. A status flag read from outside its owner is [[status-variable-as-enumeration]]. A getter that exposes an object's state for the caller to decide with is [[tell-dont-ask]] or [[no-getters-and-setters]]; this page is about who walks a data structure, not about objects handing out their fields. An accessor named after where its data is stored (`RateFile.Read()`) is [[storage-independent-names]].

## When not to apply

The book gives no limit; these are this wiki's own:

- Inside the class or module that owns the structure, direct access is how the access routines themselves are written.
- A generic container whose domain *is* the data structure (a linked-list library) has no domain level beyond `next`; its routine names describe the structure correctly.
- A plain record with no invariant to protect and no representation likely to change gains little from routines in front of each field.

## Repair

Move each direct operation on the structure into a routine on its owner, name the routine after the question the caller asks in the domain, and replace every remaining direct site, including the easy ones, so that no caller reads or writes the representation. The book's short recipe: hide the data in a class, keep it in one instance, write routines to read and change it, and require code outside the class to use them (p. 331).

## Before and after

```
event = queue.items[queue.front]
queue.front = queue.front + 1
add_event(queue, urgent)           // the hard part already sits in a routine

employee = employee.next
```

```
event = queue.remove_highest_priority()
queue.add(urgent)

employee = staff.next_employee(employee)
```

## Source

McConnell, *Code Complete*, 2nd edition, Russian edition, via [[code-complete]], section 13.3, pp. 330-334: access routines as the main approach (p. 330), the advantages of access routines, the `PushStack` and `PageFull` examples, the domain-level rule with Table 13-1, the one-level rule with `InitStack`/`PushStack`/`PopStack`, and Table 13-2. The quotation of p. 333 is transcribed from `raw/` and needs the page-image check. This wiki's own: the signs as worded, the ownership split, the limits and the pseudocode. Related: [[class-invariant]].
