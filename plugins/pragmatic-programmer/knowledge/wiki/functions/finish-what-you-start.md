---
title: Finish what you start
category: functions
summary: "A resource is opened in one routine and closed in another, shared through a field the orchestrating routine never mentions, so an added branch skips the close."
tags: [rule, resources, coupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Memory, transactions, threads, connections, files and timers are most often used by one predictable pattern: allocate, use, release (p. 156). Many developers have no consistent plan for allocating and releasing them, and the tip is «Завершайте то, что начали» (p. 156).

## Rule

The function or object that allocates a resource is responsible for releasing it (p. 156). The book states it as a general pattern for every kind of resource: «тот, кто выделяет ресурс, должен отвечать за его освобождение» (p. 159).

Then shrink the resource's lifetime. A second tip, «Действуйте локально», goes with the advice «Если же гложут сомнения, то всегда стоит сократить область действия» (p. 159). Binding a resource to an enclosing block means nothing has to be remembered (pp. 158-159).

The idea reaches beyond transient resources. The book suggests considering balance for anything created that consumes a finite resource, and poses it as questions: log files rotated and cleaned, debug files deleted, database log records expired (p. 160).

## Sign in code

- One routine opens, another closes, and they share the handle through a field. The routine that calls both does not mention it.
- A release call appears on only some branches of a routine. An exception is not a branch here: a release with no `finally` or scope binding around it is [[exception-safe-release]].
- A special-case release has been added in an `else`: «Это и есть признак несбалансированности!» (p. 158).
- A routine appends to a log table or temporary directory, and no code near it removes or expires anything. Retention often lives elsewhere, so this wiki's sign needs a search of the repository and its scheduled jobs before it is reported.

The failure this causes is delayed. In the book's example, a new condition around the write step means the closing routine sometimes never runs. The change passes testing, then fails hours into production with too many open files (p. 157). Patching the branch to close the file ties all three routines to the shared variable, and tracking whether the file is open becomes a mess (pp. 157-158).

## When not to apply

- Dynamic data structures, where a routine allocates memory and links it into something larger that outlives the routine (p. 161). See [[ownership-of-nested-structures]].
- This wiki adds factories and pools, whose job is to hand a resource to someone else. The hand-over must be stated in the contract.

## Repair

1. Move acquisition and release into one routine and pass the handle to helpers as a parameter (p. 158).
2. Remove the shared field (p. 158).
3. Where the language allows, tie the lifetime to a block so release is automatic (pp. 158-159).
4. Or wrap the resource in a class that acquires it on construction and releases it in its destructor, which the book presents as a development of the same pattern (p. 159).

For several resources, see [[resource-acquisition-order]]; for exceptions, see [[exception-safe-release]]. To prove that release happens, see [[resource-balance-check]].

## Before and after

```
# before
class ReportJob:
    method load():
        self.conn = connect(database)
        self.rows = self.conn.query(sql)

    method store():
        self.conn.save(summarise(self.rows))
        self.conn.close()

    method run():
        load()
        if not is_empty(self.rows):
            store()
```

```
# after
class ReportJob:
    method load(conn):
        return conn.query(sql)

    method store(conn, rows):
        conn.save(summarise(rows))

    method run():
        with connect(database) as conn:
            rows = load(conn)
            if not is_empty(rows):
                store(conn, rows)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 156-161 for the rule, the first three signs, the failure, the first limit and the repair. The fourth sign, the assignment against [[exception-safe-release]], the factory limit and the example are this wiki's own.
