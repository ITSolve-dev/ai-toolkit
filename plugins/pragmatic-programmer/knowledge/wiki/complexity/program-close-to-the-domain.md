---
title: Program close to the problem domain
category: complexity
summary: "The same call sequence repeated four or more times with no branch on a key and only literals changing, together stating one table of facts such as routes, rules or test cases."
tags: [rule, dsl, declarative, vocabulary]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

## Rule

The tip is «Программируйте близко к предметной области» (p. 94). The source's premise is that a language shapes how a problem is thought about, and that the language of the problem domain may suggest a programming solution, which it considers more important than the features of the programming language (p. 93). The authors always try to write code in the vocabulary of the application domain, and sometimes go a level further and program in the domain's vocabulary, syntax and semantics (p. 94). Their examples include a web framework's routing table, in which each line states a path, a handler and an action (p. 95).

This page concerns the notation of code. Modelling a business domain is out of this wiki's scope.

## Sign in code

The same sequence of calls, repeated four or more times, in which only literals differ, and which together state one table of facts: routes, validation rules, permissions, test cases. The facts are spread across the mechanics and cannot be read as a list.

The count alone does not establish the sign. Whether the entries really form one table is a judgement the reader makes from the code in front of them.

This page owns repeated statements with no branch. An `if` or `switch` over a key chosen at run time is [[drive-repeated-dispatch-from-a-table]]'s shape.

## When not to apply

- The source's own limit is cost: «Написание предметно-ориентированного языка так или иначе увеличивает затраты на проект» (p. 98), so it must pay for itself, potentially over the long term (p. 98). See [[internal-vs-external-dsl]].
- This wiki adds: entries that look alike but each carry their own logic are not one table. Forcing them into a notation pushes that logic into flags and special cases.
- This wiki adds: a few entries that read clearly as plain code need no notation. The threshold of four, which [[drive-repeated-dispatch-from-a-table]] shares, is a floor for looking, not a verdict.

## Repair

The source gives the direction; the steps are this wiki's own.

1. Extract the entries as data, or as calls to functions named in the domain's words.
2. Put the mechanics in one place that reads that data.
3. Take the cheapest form that works, in the order given by [[internal-vs-external-dsl]], and prefer [[internal-dsl-from-plain-functions]] over metaprogramming.

## Before and after

```
// before: the routes are buried in the mechanics
server.on("GET", "/", function(r): auth(r); log(r); return pages.index(r))
server.on("GET", "/users", function(r): auth(r); log(r); return users.list(r))
server.on("POST", "/users", function(r): auth(r); log(r); return users.create(r))
server.on("DELETE", "/users/{id}", function(r): auth(r); log(r); return users.remove(r))
```

```
// after: the table can be read as a table
routes = [
    get("/", pages.index),
    get("/users", users.list),
    post("/users", users.create),
    delete("/users/{id}", users.remove),
]
install(server, routes, through = [auth, log])
```

## Source

[[pragmatic-programmer]], Topic 14, pp. 93-98: the rule, its premise, the routing example and the cost limit. The sign, its threshold of four, the split with [[drive-repeated-dispatch-from-a-table]], the two added limits, the repair steps and the pseudocode are this wiki's own.
