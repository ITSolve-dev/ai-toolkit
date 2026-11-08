---
title: Representational duplication
category: structure
summary: "A hand-written structure mirrors an external schema field by field, or error codes and API shapes are copied by hand where a machine-readable definition exists."
tags: [rule, boundaries, duplication, integration, schemas]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Representational duplication is the form of [[dry]] violation that arises at every boundary: both sides of an interaction must know the shape of the interface between them, so a change on one side breaks the other (p. 67).

## Rule

The book says this duplication is inevitable and can only be reduced (p. 67). The knowledge in question includes an API, a database schema and error codes (p. 67). This wiki states the rule as: keep the knowledge of an external shape in one machine-readable place, and derive from it rather than retyping it. The authors' preferred option for data sources, under *Repair*, keeps no fixed structure at all, so it avoids the copy rather than deriving it.

## Sign in code

- A type or class whose fields repeat, one to one, a table or a response format that could be read by a tool.
- Error codes of an external system retyped as local constants.
- A hand-written client or stub for a service that publishes a formal specification.

This wiki's signs need a fact that is not in the code: whether a machine-readable definition exists. The reader needs the schema or specification within reach of the repository, and without it the honest report is a question rather than a finding.

## When not to apply

- The duplication cannot be removed altogether (p. 67). This wiki therefore reports a copy only where a definition is within reach and the copy already differs from it, or where one shape is kept by hand in two places.
- This wiki adds that where no machine-readable definition exists and none can be introspected, there is nothing to derive from. The book's answer for external APIs is to consider writing and publishing a specification yourself (p. 67).

## Repair

By kind of boundary, per the book (pp. 67-68):

- **Internal APIs:** specify the interface in a neutral format, and let tools generate documentation, mock APIs, functional tests and clients. Ideally it is kept in a central repository.
- **External APIs:** import the formal specification into local tooling.
- **Data sources:** use schema introspection to generate data containers directly from the schema.
- **Data sources, the authors' preferred option:** skip the fixed structure, load external data into a key-value map, and add a second layer, a simple table-driven validation suite that checks whether the map holds the required data in the required format.

## Trade-offs

The authors say the map alone is risky, because the code must know what data it is handling and much of the safety is lost, which is why the validation layer is part of the option (p. 68). They note that an API documentation tool may be able to generate the suite.

This wiki adds two points. A validation table typed by hand is itself a copy of the shape. A map also gives up the compile-time guarantees that a fixed type provides. Where the data flows far into the application, this wiki reads generation from the schema as the cheaper of the two options. Where only a small part of the record is used, and at the edge, the map with validation costs less.

## Before and after

Before:

```
# typed by hand from the table definition
record CustomerRow
    id: Integer
    full_name: Text
    city: Text
    created_at: Time
```

After, generated:

```
CustomerRow = generate_type_from_schema("customers")
```

After, the map with a validation table:

```
row = fetch_as_map("customers", id)
check_fields(row, spec_for("customers"))
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 9, pp. 67-68, via [[pragmatic-programmer]]. This wiki's own: the rule's phrasing, the signs and what they need, the conclusions drawn in both limits, the two added points and the setting-based reading under *Trade-offs*, and the pseudocode.
