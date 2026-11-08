---
title: Shared state is incorrect state
category: types-and-state
summary: "A thread or task body, or a callback handed to a scheduler, pool or event loop, touches a variable or object captured from outside, two tasks receive the same mutable object, or concurrent code temporarily changes process-wide state such as the current directory: each works from a view it cannot guarantee is current."
tags: [rule, concurrency, mutation, shared-state]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Shared state is any mutable thing two pieces of running code can reach at the same time. The book names it one of the main culprits in why concurrent code is hard: languages have features that are safe sequentially and become unsafe as soon as two events can happen at once (p. 214).

## Rule

The book's definition is wider than global variables: «Такое состояние возникает в любой момент времени, когда два или несколько фрагментов кода содержат ссылки на один и тот же фрагмент изменяемых данных.» (p. 214). Its tip states the conclusion: shared state is incorrect state (p. 219).

The reasoning is not that two processes can write to the same memory. It is that «ни один из них не может гарантировать, что его представление о данной области памяти согласовано с другими» (p. 220). A read copies the value into the reader's own memory; if the original then changes, a decision is being made on a stale copy (pp. 220-221).

Memory is only the best-known case. The book extends this to files, databases and external services: «Всякий раз, когда два или более фрагмента прикладного кода могут одновременно получить доступ к некоторому ресурсу, следует усматривать потенциальное осложнение.» (p. 225). And it warns: «Иногда ресурс не вполне очевиден.» (p. 225). Its example is its own build toolchain, where two places temporarily changed the current directory. That was fine sequentially, but once threads were added the directory, being shared between threads, was changed under another thread (p. 225). The failures this produced are the subject of [[random-failures-suspect-concurrency]].

The book's closing advice is that «добиться параллельности в среде с общими ресурсами нелегко» (p. 226), and that the way out is the old joke: if it hurts when you do that, do not do that (p. 226). This wiki reads that as an order of preference: remove the sharing first, and guard it only if it has to stay.

## Sign in code

The book gives the reference definition and the cases of files, databases, services and the current directory. The shapes below are this wiki's own.

- A concurrent construct (thread start, task spawn, pool submit, callback handed to a scheduler or event loop) whose body reads or writes a variable or object from an enclosing or module scope.
- The same mutable object passed to two tasks.
- A module-level or static mutable field written by a request handler. This page owns that field where concurrent code writes it. With no concurrency, the hidden input is [[global-data]].
- Process-wide state changed and restored around a call: the current directory, an environment variable, a locale, a global setting.
- A file at a fixed path written by code that can run in two instances.

Whether two paths really overlap may not be visible from one function. If no concurrent construct is in view, the page needs to know how the callers run, and the honest report is a question rather than a finding.

## When not to apply

- The data is not modified after it is shared. The book's definition requires mutable data; the conclusion that immutable sharing is safe is this wiki's own.
- Only one piece of code can reach the resource at a time. On one thread with cooperative tasks, this wiki warns that the condition holds only between suspension points: state read before an await can be stale after it.
- The resource offers its own atomic operation and the code uses it, as in [[lock-belongs-to-the-resource]].
- Functional style is not an exemption. The book grants that immutable data makes concurrency easier to argue for, but notes the same difficulties return: «в какой-то момент им все равно приходится вступать в реальный изменчивый мир» (p. 226).

## Repair

The sequence is this wiki's own; the book supplies the guarded and actor options.

1. Stop sharing: give each task its own copy, or pass values rather than references.
2. Replace process-wide state with an explicit parameter.
3. Give the data one owner that others message: [[actor-model]].
4. If sharing has to stay, make access atomic inside the resource: [[check-then-act-must-be-atomic]], [[lock-belongs-to-the-resource]]. The book lists mutexes, monitors and semaphores as the usual library means, and notes that some languages build the discipline in, by letting only one variable or parameter hold a reference to a piece of mutable data at a time (p. 226).

## Before and after

```
function build(target):
    previous = current_directory()
    change_directory(target.path)   // process-wide, seen by every worker
    run("compile")
    change_directory(previous)

for target in targets:
    pool.submit(build, target)
```

```
function build(target):
    run("compile", working_directory = target.path)

for target in targets:
    pool.submit(build, target)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: definition, p. 214; the tip and the restaurant and bank cases, pp. 219-221; other resources and the current-directory case, p. 225; other forms of exclusive access, functional languages and the closing advice, p. 226.

This wiki's own: the items under `## Sign in code` beyond the book's named cases, the first two limits' reasoning, the order of repairs, and the fix of passing the directory as a parameter. The book reports the cause of its build failure but not this fix.
