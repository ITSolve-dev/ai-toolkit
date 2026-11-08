---
title: "Parallel change (expand-contract)"
category: change
summary: "Use when a rename or replacement cannot reach all its users in one change (a function called from outside this repository or by unknown clients, a stored field, a library used throughout): add the new form beside the old, keep the old as a pass-through, move users over in small steps, remove the old only when nothing uses it."
tags: [method, refactoring, expand-contract, published-interface, branch-by-abstraction]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Parallel change, also called expand-contract, splits a breaking change into steps each of which leaves the system working: introduce the new form alongside the old, migrate users, then remove the old. Fowler names it as a general approach while discussing database fields (ch. 2, PDF p. 74) and applies the same shape to published interfaces (p. 69) and to library replacement (p. 65).

## When it is needed

A plain refactoring changes a declaration and all its callers in one change, as in Change Function Declaration (PDF p. 69). That stops working when some users cannot be edited in the same change:

- **A published interface**: "an interface that is used by clients independent of those who declare the interface" (PDF p. 69), such as a function called from another team's repository or a declared API used by customers, where the author cannot even tell who calls it.
- **Stored data**: renaming a field also requires transforming the data already stored under the old name (PDF pp. 73-74).
- **A dependency used throughout**, such as a library being replaced (PDF p. 65).

This wiki reads the trigger as visible in code only through a declaration that marks the surface as public to clients outside this repository (a versioned API package, a published library's surface, a schema of stored data). An export whose callers all sit in this repository is not one. Whether unknown clients exist otherwise needs knowledge beyond the code; [[minimal-but-complete-functionality]] already excludes published APIs from its caller search for the same reason.

## Procedure

**Renaming a published function** (PDF p. 69):
1. Add the new declaration.
2. Keep the old declaration as a pass-through to the new one.
3. Mark the old one deprecated.
4. Retire it when clients have moved; Fowler notes that sometimes it must be kept forever. This "complicates the interface—but it is the price I must pay to avoid breaking my clients" (PDF p. 69).

**Renaming a stored field** (PDF p. 74). Where the field is persisted, the same shape runs across the schema; the schema itself is taken as given here, and only the code's side of the steps is this wiki's concern:
1. Add the new field and do not use it.
2. Make updates write both old and new fields.
3. Move readers to the new field gradually.
4. Once all readers have moved and bugs have had time to show, remove the old field.

Each step is a small migration script kept in version control with the code change, and the steps compose into a large change. Fowler adds that database steps are often best spread over several releases so that any one can be reversed (PDF p. 74).

**Replacing a library: branch by abstraction** (PDF p. 65):
1. Introduce an abstraction that can act as an interface to either library.
2. Move calling code onto the abstraction, piece by piece.
3. Switch the implementation behind it.

The abstraction left in place afterwards is the layer [[hide-third-party-apis]] asks for; this link is this wiki's own.

Fowler's Rename Field runs the same shape inside one class (the constructor accepts both keys while callers migrate). This wiki assigns the neighbouring procedures as follows. Renaming or re-parameterising a function whose callers can all be edited in this change is [[change-function-declaration]]; a change some of whose users lie outside this change (a published interface, stored data, a library used throughout) is [[parallel-change]]; a changed value that callers inspect, such as a sentinel they compare to, is [[extract-before-changing-many-callers]]; renaming a record field or a class's accessor pair is [[rename-widely-used-field]].

## Example

```
// before: rename breaks every client outside this repository
public function circumference(radius): ...   // was: circum(radius)
```

```
// after: old name kept as a deprecated pass-through
public function circumference(radius):
    return 2 * PI * radius

// deprecated: use circumference
public function circum(radius):
    return circumference(radius)
```

## Trade-offs

- The pass-through doubles the surface until it is retired, and may never be retired (PDF p. 69).
- Fowler argues against fine-grained strong code ownership because it turns internal functions into published interfaces needlessly (PDF p. 69). This wiki takes from that only the code-level point: a function treated as published only because another person owns its callers pays this cost without need. Team policy is out of this wiki's scope.

Related: [[reversibility]], [[small-steps-with-feedback]], [[move-function]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 2, "Long-Term Refactoring" (PDF p. 65), "Code Ownership" (p. 69), "Databases" (pp. 73-74). This wiki's own: the reading of the trigger as a visible public-surface declaration and the exclusion of in-repository exports, the selecting sentence, the link to [[hide-third-party-apis]], the example and the code-level reading of the ownership argument.
