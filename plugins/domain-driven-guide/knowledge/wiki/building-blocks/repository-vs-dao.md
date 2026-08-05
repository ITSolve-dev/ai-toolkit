---
title: Repository versus Data Access Object
category: building-blocks
summary: A Repository has object/collection affinity and belongs with a domain model; a DAO is expressed in database tables with CRUD interfaces and belongs to Transaction Script; using DAO-style fine-grained CRUD on Aggregate parts undermines the domain model.
tags: [concept, repository, dao, aggregate, transaction-script, ubiquitous-language]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A [[repository]] and a Data Access Object (DAO) are both abstractions over a persistence mechanism, but they are not interchangeable — and not every persistence abstraction is a DAO (an object-relational mapper, for instance, is neither a Repository nor a DAO). What distinguishes them is *what they are expressed in terms of* and *which application style they serve*.

## The distinction

> "Basically, a DAO is expressed in terms of database tables, providing CRUD interfaces to them." (raw L11255)

Drawing on Fowler's *Patterns of Enterprise Application Architecture*, DAO-like facilities — **Table Module**, **Table Data Gateway**, **Active Record** — "are patterns that would typically be used in a Transaction Script application" because they "tend to serve as wrappers around database tables." By contrast, "Repository and Data Mapper, having object affinity, are typically the patterns that would be used with a domain model" (raw L11255).

So the split is:

| | Repository / Data Mapper | DAO / Table Gateway / Active Record |
|---|---|---|
| Expressed in terms of | objects, collections of [[aggregate]]s | database tables, rows, columns |
| Interface flavor | collection-mimicking (add/save, finders) | CRUD |
| Belongs to | a domain model | Transaction Script |

## Why DAO-style CRUD is corrosive to a domain model

Because DAOs offer fine-grained CRUD, they let clients read and write data that would otherwise be *parts* of an Aggregate directly:

> "Since you can use DAO and related patterns to perform fine-grained CRUD operations on data that would otherwise be considered parts of an Aggregate, this would be a pattern to avoid with a domain model. Under normal conditions you want the Aggregate itself to manage its business logic and other internals and keep everyone else out." (raw L11259)

This directly threatens the [[aggregate]] contract and invites an [[anemic-domain-model]].

## Stored procedures vs. data-grid entry processors

Moving code to the data (for a demanding nonfunctional requirement) is sometimes essential, but the two options differ in how disruptive they are to DDD:

- A **Data Fabric Function / Entry Processor** is written in Java, "would adhere to the Ubiquitous Language ... The only difference from the core model is where the Function/Entry Processor is executed, which is not disruptive" (raw L11261). See [[ubiquitous-language]].
- **Prolific stored procedures** are "potentially very disruptive to DDD because the programming language is generally not well understood by the modeling team and implementations are generally 'safely' tucked away from their view. If so, that is exactly the opposite of what DDD is trying to accomplish" (raw L11261).

## Bottom line

You may loosely think of a Repository as a DAO in a general sense, but "as much as possible you should try to design your Repositories with a collection orientation rather than a data access orientation. That will help keep you focused on the domain as a model rather than on data and any CRUD operations" (raw L11263). See [[collection-oriented-repository]].

## Related

[[repository]] · [[aggregate]] · [[collection-oriented-repository]] · [[ubiquitous-language]] · [[domain-service]] · [[anemic-domain-model]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
