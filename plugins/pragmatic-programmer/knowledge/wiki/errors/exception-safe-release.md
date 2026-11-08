---
title: Release resources safely under exceptions
category: errors
summary: "A resource is acquired inside a try whose finally releases it; its release sits after the use with no finally or scope binding; or a class holding a file, stream or connection has no close protocol, or leaves release to a finalizer or the garbage collector."
tags: [rule, resources, exceptions, raii]
paradigm: any
sources: [pragmatic-programmer, elegant-objects]
created: 2026-11-01
updated: 2026-11-03
---

Exceptions complicate [[finish-what-you-start]]: everything allocated before an exception must still be cleaned up (p. 160 of [[pragmatic-programmer]]). *Elegant Objects* ends on the same point, as RAII, Resource Acquisition Is Initialization: an object takes its resource when it is created and gives it back when it is destroyed. «Мы захватываем ресурс при инициализации объекта и освобождаем его, когда объект больше не нужен…» (p. 237 of [[elegant-objects]]).

## Rule

*The Pragmatic Programmer* gives two usual means: tie cleanup to a variable's scope, so a destructor runs when the scope ends by any route, or use `finally` in a try block (p. 160). With `finally`, acquire the resource before the `try`, not inside it (p. 161). A resource wrapped in a class is especially useful in languages where exceptions can interfere with release (p. 159). The reasoning: if allocation is inside the `try` and fails, the `finally` tries to release something that was never allocated (p. 161).

*Elegant Objects* makes the class form the rule wherever real resources are involved, such as files, streams and database connections: tie the resource to an object's lifetime, with a destructor where the language has one, and elsewhere with the close protocol and a scoped block (p. 238). Its reasoning is that a garbage-collected language has no destructors and may keep a dead object in memory long after its last use, until memory runs short (pp. 237-238). There, the scoped `close` of a try-with-resources block plays the destructor's part (p. 238).

*The Pragmatic Programmer* allows release when the collector runs (p. 159); *Elegant Objects* does not (pp. 237-238). This wiki follows the second for external resources, whose shortage the collector does not see.

## Sign in code

- The allocation is the first line inside a `try`, and the matching release is in its `finally`.
- A release call follows the use on the normal path, with no `finally` or scope binding around it. Where the resource is a lock, the shape belongs to [[release-lock-on-every-path]]. Where a branch leaves with no release at all, it belongs to [[finish-what-you-start]].
- A `finally` block guards its release with a check for null or a flag, a sign the allocation sits on the wrong side of the `try`.
- A class that holds a file handle, stream or connection does not implement the language's close protocol, so callers cannot put it in a scoped block and must remember a separate cleanup call.
- The release of such a resource is left to a finalizer, or to the object simply becoming garbage.

This wiki assigns the neighbouring cases as follows. This page owns where the release sits and whether a class offers one. A constructor that acquires a resource the class releases in its own close or destructor is the RAII form, owned by [[exception-safe-release]] and not a finding of [[constructors-without-code]]. Several acquisitions combined in the caller belong to [[composite-resource]].

## When not to apply

- This wiki adds that memory in a garbage-collected language needs no such handling. External resources still do, and a collector's timing is not a guarantee of prompt release.
- This wiki adds that a resource whose lifetime a framework or container manages, such as a request-scoped object, a pooled connection or an injected resource the container closes, is released by that owner; the class needs no close protocol of its own, and a release in the class would break the owner's protocol.
- This wiki allows several resources under one `try` with guarded release where nesting would be worse, as a known trade-off against the third sign.
- *Elegant Objects* contradicts itself here without remarking on it: its RAII example opens the file in the constructor (p. 237), while section 1.3 asks for constructors that do no I/O (see [[constructors-without-code]]). This wiki resolves the two by setting. Where a class exists to own a resource for its lifetime and releases it in its close or destructor, acquiring in the constructor is allowed, because the scoped block then guarantees the release.

## Repair

1. Move acquisition directly above the `try`. Give each resource its own nested `try` or scope. Prefer a scope-bound form where the language has one.
2. Make a resource-holding class implement the close protocol, release the resource in `close` or the destructor, and have callers create it in a scoped block (p. 238 of [[elegant-objects]]). Replace any finalizer-based release.

## Before and after

```
# before
try:
    session = open_session(host)
    send(session, message)
finally:
    close(session)
```

```
# after
session = open_session(host)
try:
    send(session, message)
finally:
    close(session)
```

```
# before
class Text:
    field handle
    constructor(path): this.handle = open_file(path)
    method content(): return read_all(this.handle)

t = Text("/tmp/test.txt")
print(t.content())
# the handle stays open until the collector runs, if ever
```

```
# after
class Text implements Closeable:
    field handle
    constructor(path): this.handle = open_file(path)
    method content(): return read_all(this.handle)
    method close(): close_file(this.handle)

using t = Text("/tmp/test.txt"):
    print(t.content())
# close() runs when the block ends, normally or by exception
```

## Source

- Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 159-161 for the first rule, its reasoning and the first sign.
- Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018, [[elegant-objects]], section 4.4, pp. 237-238, for RAII, the close protocol and the recommendation for real resources. The quotation, on p. 237, was checked against the page image; it stops mid-sentence, marked by the ellipsis.
- This wiki's own parts are: the other signs, including the two drawn from section 4.4, which states the technique and gives no sign; the ownership split with [[constructors-without-code]], [[release-lock-on-every-path]], [[finish-what-you-start]] and [[composite-resource]]; the limits, including the one for lifetimes a framework or container manages; the choice of *Elegant Objects* over *The Pragmatic Programmer* on release by the collector; the resolution of the book's tension with code-free constructors; the nesting step of the repair; and the examples.
