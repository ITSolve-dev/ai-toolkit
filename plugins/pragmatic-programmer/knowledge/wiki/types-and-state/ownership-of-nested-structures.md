---
title: Ownership of nested structures
category: types-and-state
summary: "A container's release routine frees only its top node with no statement about children, or different release sites treat the same children differently."
tags: [decision-rule, resources, ownership]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

The basic pattern of [[finish-what-you-start]] does not fit dynamic data structures, where a routine allocates memory and links it into a larger structure that outlives it (p. 161).

## Rule

Establish a [[semantic-invariant]] for allocation: decide who is responsible for the data in an aggregate structure (p. 161). The book gives three options for releasing the top-level structure (p. 162):

1. It releases the substructures it contains, which release their own data, and so on.
2. It is simply released, and whatever it pointed to that nothing else references is left dangling.
3. It refuses to be released while it holds any substructures.

The choice depends on each structure, but «ее необходимо выразить явно для каждой структуры данных» and implement it consistently (p. 162).

This wiki offers a test the book leaves open. Choose the first when children belong to the parent alone. Choose the second only when something else provably holds the children. Choose the third when removing children that are in use would be a bug that should surface.

## Sign in code

- A destroy routine for a container touches only the top node, and nothing says what happens to its children.
- Two release sites for one structure treat the children differently.
- Callers walk a structure's internals to clean up before calling its release.

## When not to apply

- This wiki notes that in a garbage-collected language, a structure holding only plain objects needs no policy, because the second option leaks nothing.
- The same language still needs a policy if children hold files, connections or other external resources.
- A structure that holds values by copy has no children to own.

## Repair

Pick one option and write it on the structure. Where the language does not help, as in procedural languages whose structures are inert, the book prefers one module per major structure with standard allocation and release (p. 162). This wiki adds: route every release site through that module. To confirm the policy holds at run time, see [[resource-balance-check]].

## Before and after

```
# before
function destroy_playlist(list):
    free(list)

function clear_and_destroy(list):
    for track in list.tracks:
        free(track)
    free(list)
```

```
# after
# ownership: a playlist owns its tracks; destroying it destroys them
function playlist_destroy(list):
    for track in list.tracks:
        track_destroy(track)
    free(list)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 161-162 for the rule, the three options and the module. The test for choosing, the signs, the limits and the example are this wiki's own.

Related: whether a copy shares mutable members with its original is [[prefer-deep-copy]].
