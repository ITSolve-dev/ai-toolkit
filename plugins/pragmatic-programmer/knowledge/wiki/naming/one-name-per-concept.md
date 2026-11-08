---
title: One name per concept, one concept per name
category: naming
summary: "Two identifiers for one thing (client and customer on the same type) with no difference of role between them, sibling operations using different verbs for one action, or one identifier meaning two things, with no glossary settling which is meant."
tags: [rule, naming, glossary, consistency, vocabulary]
paradigm: any
sources: [pragmatic-programmer, object-oriented-thought-process]
created: 2026-11-01
updated: 2026-11-06
---

A project needs one vocabulary shared by the people who ask for the software and the code that implements it. *The Pragmatic Programmer* makes this a requirement of the project and treats the glossary as its instrument; in code the same demand shows as identifiers that map to concepts one to one.

## Rule

Every project builds up its own vocabulary, and it is very important that all members of a team know the terms and use them consistently. The book's example is `order`, which means a purchase to a shop's team and a religious order to a team charting the origins of religious groups (p. 294). Once a vocabulary is second nature, it serves as shorthand for expressing complex ideas exactly and briefly (p. 294).

Thomas and Hunt also observe that users and domain experts use terms with a specific meaning, and that they may distinguish a client from a customer, so using either word at random in the system is unwise (pp. 305-306). They recommend a project glossary «как единое место, где определяются все конкретные термины, употребляемые в проекте» (p. 306), used by everyone from end users to support staff.

Their reason is stated as a condition of success: «В проекте нельзя достичь успеха, если пользователи и разработчики называют один и тот же предмет по-разному (или, что еще хуже, называют разные предметы одинаково).» (p. 306). The book ranks the two failures: one name for different things is worse.

Weisfeld's *The Object-Oriented Thought Process* (ch. 8) gives the operation-level case. `Planet`, `Car` and `Dog` each store a name but expose it as `getplanetName()`, `getCarName()` and `getDogName()`, so anyone using them must look each one up (p. 166). It would be better, he writes, if for all classes in a project (or company) «применялось одно и то же соглашение об именовании» (p. 166). His means is a contract: an interface `Nameable` with `getName()`/`setName()` that all three implement (pp. 166-167). The classes are unrelated, so it is an interface and not a base class ([[prefer-interfaces-for-polymorphism]]).

This wiki reads the ranking this way. Two names for one thing cost a reader a lookup. One name for two things produces code that compiles and reads correctly while mixing the two meanings.

## Sign in code

The source names the failures but gives no sign in code. The signs below are this wiki's own.

- Two identifiers refer to one type or record: `client_id` and `customer_id` holding the same key, or `Client` and `Customer` related by a field-for-field copy.
- Two names are used for one parameter along a single call chain, with the value passed unchanged.
- Sibling operations use different verbs for the same action: `fetch_order`, `get_invoice`, `load_customer`.
- Classes offering the same operation under names that repeat the owning class (`getCarName`, `getDogName`), with callers branching on the type only to call the right spelling (after Weisfeld, p. 166).
- One identifier in two modules has different fields or units, such as `account` meaning a login in one place and a ledger in another, and a function receives one where the other is expected.
- A comment explains which of the meanings a name carries at this spot.

This wiki assigns the neighbouring cases as follows. This page owns two names for one and the same thing or value, including one quantity named in two word orders (`pointTotal` and `totalPoints`). Qualifier order across different quantities is [[computed-value-qualifier-at-end]]. Two names for different values whose words mean nearly the same thing are [[similar-meaning-names]].

## When not to apply

The limits here are this wiki's own, except the first, which the book's example implies.

- The domain really distinguishes the two terms. Two names are then correct and merging them is the error; the check is whether the two have different rules or data, not whether they sound alike. A prospect and a paying customer may well differ.
- The same word differs across separate parts of a system that do not share a model. A term may legitimately mean different things on either side of a boundary, and that boundary is the business of `domain-driven-guide`.
- The name comes from an external interface. A wire format or a third-party field keeps its own name at the edge; the translation happens once, at that edge.
- The second name narrows the concept to a role in a scope, such as `buyer` for an authenticated `user`. That is not a second name for the concept, and [[name-by-role]] owns it. The signs here fire only where the two names differ with no difference of role.

## Repair

1. Settle which concept each name stands for, by asking whoever owns the term when the code cannot answer.
2. For one concept under two names, keep the term the glossary or the project already uses most, rename the rest in one change, and delete the copying between the two types.
3. For one operation spelled per class, rename it to one spelling. Where a caller treats the classes alike (the type branching in the sign), declare it once in an interface the classes implement and delete the type checks that picked the spelling (after Weisfeld, pp. 166-167); otherwise the rename suffices, which is this wiki's. Where the classes come from outside code, wrap them in an adapter rather than rename them; this is this wiki's.
4. For two concepts under one name, give each a distinct name and let the type system keep them apart if it can.
5. Record the term in the single shared place the project keeps for this.

The trade-off, in this wiki's words: renaming a public interface breaks its callers, so a rename across a published boundary needs an alias period. See [[rename-when-meaning-drifts]] for naming as work that continues after the first draft.

## Before and after

Before:

```
function place_order(client, items):
    customer = to_customer(client)      // copies the same fields
    charge(customer, total(items))

function report(account):               // here: a login
    print(account.last_seen)

function statement(account):            // here: a ledger
    print(account.balance)
```

After:

```
function place_order(customer, items):
    charge(customer, total(items))

function report(login):
    print(login.last_seen)

function statement(ledger):
    print(ledger.balance)
```

## Source

[[pragmatic-programmer]]: Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, p. 294 (project vocabulary, the `order` example) and pp. 305-306 (the client and customer example, the glossary, the two failures and their ranking).

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 8, pp. 166-167: `Planet`, `Car` and `Dog` before and after, `Nameable` as a naming contract; the quotation was checked against `raw/`. This wiki's own for that part: the per-class-spelling sign as worded, the condition for an interface in step 3 and the adapter remark.

This wiki's own: the other signs in `## Sign in code`, the limits on boundaries, on external names and on role names, the numbered repair, the explanation of why the second failure is worse, and the pseudocode. The authors argue at the level of a project's vocabulary; carrying it to identifiers is our transfer. The book's means of spreading a vocabulary through a team are process and are left out.
