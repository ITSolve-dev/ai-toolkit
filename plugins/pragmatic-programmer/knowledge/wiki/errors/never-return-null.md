---
title: Never return null
category: errors
summary: "A method declared to return an object returns null (None, nil) on a not-found path, and its callers compare the result with null before using it."
tags: [rule, null, return-values, null-object]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-07
---

*Elegant Objects* treats a null return as the same fault as a null argument ([[no-null-arguments]]), approached from the other side (p. 203). A method that may return null makes every result it hands out suspect. Each caller then has to test whether it got an object at all before talking to it: «Мы должны проверить, является ли объект объектом в принципе.» (p. 203). The book's verdict on the method itself is «Метод, возвращающий NULL, ведет себя неуважительно.» (p. 205).

## Rule

Do not return null. When the thing asked for is not there, the book allows three answers: «либо бросьте исключение, либо верните коллекцию или пустой объект» (p. 211).

The reasoning in the book has three parts:

- **Lost trust spreads.** A caller cannot tell from the call which methods may return null, so it spends reading time finding out and checks results twice. Sooner or later one check is forgotten (pp. 203-204). The book's main charge is this loss of trust; the forgotten check is one consequence of it.
- **Null is a fail-safe move.** Returning null instead of failing hands the problem to somebody further away, in the hope that nobody dereferences the result (pp. 206-207). The book's example is a directory listing that returns null for a missing directory, so every caller writes the throw that the method should have done (p. 205). See [[crash-early]] for the fail-fast position behind this.
- **A scalar sentinel is the same thing.** The book calls returning -1 instead of a size semantically close to null, and in the end identical to it: the caller must compare with `==` before using the number, and forgetting the comparison feeds -1 into the next computation (p. 216). In the book that -1 stands for a failure to read the file, not for an absence; carrying the point over to absence is this wiki's own.

## Sign in code

- A method whose declared result is an object has a `return null` (or `None`, `nil`) on a path where the object was not found or could not be produced.
- Its call sites test the result with `== null` or `!= null` straight after the call, often with a message and an early return.
- A method that returns a number or other value hands back an in-band marker, such as -1, 0 or an empty string, meaning "there is no value", and callers compare the result with that marker.

This wiki assigns the neighbouring cases as follows. [[crash-early]] owns a sentinel or default returned for a state only a bug can produce. This page owns a null or sentinel returned for an absence that a correct program can meet, such as a lookup that finds nothing. A sentinel returned from a catch below an entry point, for a failure a correct program can meet, is [[recover-only-at-entry-points]]; [[never-return-null]] owns a null or sentinel returned with no catch, for an absence such as a lookup that finds nothing. Where the project carries failures as values (a result or option type), [[wrap-values-between-transformations]] owns a sentinel or marker returned for a failure; where it carries them as exceptions, [[recover-only-at-entry-points]] owns a sentinel returned from a catch; a null or marker returned for an absence, rather than a failure, is [[never-return-null]]. Null passed in as an argument is [[no-null-arguments]]; a field left null is [[null-field-hides-another-class]]. Which replacement to choose once null is gone is decided on [[null-object-or-optional]]. An exception thrown for an ordinary absence and caught round the call is [[exceptions-for-the-exceptional]]: whether the catch around the call turns the exception into ordinary flow. One sentinel value compared by several clients that mostly give it the same default answer is [[introduce-special-case]]; this page owns the return statement, and that page supplies the replacement when the callers repeat one default.

## When not to apply

The book allows no exceptions. The limits below are this wiki's own.

- **The project uses a typed optional result that the checker enforces**, such as Option, Maybe or a nullable type the compiler will not let a caller dereference unchecked. The book rejects `Optional` as an envelope foreign to object thinking (pp. 209-210). This wiki holds that the practical harm the book names, a forgotten check (p. 204), does not arise when the type system refuses the unchecked use. This wiki resolves the disagreement by setting: where the convention is a checked optional type, follow it and name the method for what it returns (`find_user`, not `user`). Where absence is an unchecked null, this page applies.
- **A boundary with a library that returns null.** That null cannot be removed. It is converted once, at the wrapper, into one of the alternatives below, and does not travel further. See [[hide-third-party-apis]].
- **A Null Object suits only callers that need what the stub can answer.** The book calls it object-minded but of limited use (p. 210). This wiki adds a failure mode: a stub that silently does nothing, instead of failing on the requests it cannot serve, recreates the fail-safe behaviour this page removes. The book's own stub throws on those requests (p. 210).

## Repair

Replace the null with the form chosen on [[null-object-or-optional]]: an exception, a collection, a null object or, where the project's convention allows it, an option type.

The book also lists splitting the method into `exists()` plus a getter that fails, and drops it because it queries the store twice (pp. 208-209). This wiki adds a second cost: between the two calls the record may appear or vanish. See [[check-then-act-must-be-atomic]].

## Before and after

```
# before
function user(name):
    row = store.find_user_row(name)
    if row is absent:
        return null
    return User(row)

# caller
u = user(name)
if u == null:
    print("no such user")
    return
print(u.name())
```

```
# after: absence means the request cannot be honoured
function user(name):
    row = store.find_user_row(name)
    if row is absent:
        fail("user not found: " + name)
    return User(row)

print(user(name).name())

# after: the caller is searching, and zero results are normal
function users(name):
    return [User(row) for row in store.find_user_rows(name)]

for u in users(name):
    print(u.name())
```

## Source

- Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018, section 4.1, pp. 202-211; section 4.2 for -1 as a sentinel (p. 216). Summary page: [[elegant-objects]].
- The quotations from pp. 205 and 211 were checked against the page image; the one from p. 203 is OCR text and has not been.
- This wiki's own: the whole of `## When not to apply` (the resolution with typed optionals, the conversion at a library boundary, and the failure mode of a silent Null Object), the transfer of the -1 sentinel from a read failure to an absence, the race in the split-method alternative, and the assignment of neighbouring cases, including the condition that divides this page from [[crash-early]].
