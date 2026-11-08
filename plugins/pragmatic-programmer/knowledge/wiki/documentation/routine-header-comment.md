---
title: Keep routine headers brief and near the code
category: documentation
summary: "A routine carries a fixed-field header block (Name, Purpose, Algorithm, Inputs, History, Author) out of scale with its body, its purpose line joins unrelated actions, or a parameter it writes to is declared like the ones it only reads."
tags: [rule, comments, functions, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**A routine header comment**, by *Code Complete*'s account, should be one or two sentences of description plus only those items that matter for that routine. The book calls the advice to put a full template above every routine, whatever its size, one of the worst in typical programming textbooks (p. 787).

## Rule

The book shows a monolithic header over a trivial `CopyString`: name, purpose, algorithm, inputs, outputs, interface assumptions, history and author. It then parodies the template with eye colour and blood type. The routine has perhaps five lines. Its purpose and algorithm are made up, because nothing can be said about something this simple between "copies a string" and the code itself, and the author data is already in version control. Requiring all this pushes programmers to write inaccurate comments and makes maintenance harder: «Эти лишние усилия не окупятся никогда» (p. 788). Heavy headers also «мешают факторизовать код» (p. 788): a new routine costs so much that programmers create fewer of them.

The book's positive advice:

- **Keep comments close to the code they describe** (p. 788). A large prologue sits far from the parts of the routine it talks about, so it is less likely to be updated with them.
- **Describe each routine in one or two sentences** before it. If you cannot, rethink the routine: «Если краткое описание придумать трудно, значит, проект метода не так хорош» (p. 789). Simple get and set accessors are the exception.
- **Document parameters where they are declared** (p. 789). This is a sanctioned use of end-of-line comments, and good names may make it unnecessary. When a documentation tool extracts comments, the benefit outweighs moving the description away from the declaration (p. 790).
- **Distinguish input from output parameters** where the language does not (p. 790). Short routines with a clear separation can skip this.
- **Document interface assumptions** (p. 791): valid values, sorted arrays, initialised members. Do it at once, as you make the assumption. Global data the routine uses is part of its interface, and a more dangerous part, because it does not look like one.
- **Comment the routine's limitations** (p. 791): the precision of a returned number, conditions under which the result is undefined, default behaviour on failure, size limits, and changes known to break it.
- **Document global effects** (p. 791). Changing global data is at least an order of magnitude more dangerous than reading it. If documenting it becomes a burden, rewrite to reduce the global data.
- **Name the source of an algorithm** taken from a book or paper, with the page (p. 791).

## Sign in code

- A header with fixed fields (Name, Purpose, Algorithm, Inputs, Outputs, History, Author, Date) sits over a routine whose body is shorter than the header or says the same thing.
- The header repeats the routine's name, or lists history and authorship that version control holds.
- The header's purpose line joins unrelated actions with "and".
- A parameter the routine writes to is declared like the read-only ones, in a language that does not mark direction, and neither its name nor a comment says it is an output.
- A routine reads or writes global data that its header does not mention.

This wiki assigns the neighbouring cases as follows. This page owns a header template on a routine and what a routine's header owes. Free-text comments inside a body that restate steps or names are [[comment-why-not-how]]. A precondition the body relies on and nothing states is [[state-the-contract]]. A missing doc comment on an exported routine is [[documentation-in-the-source]]. The header of a file or class, and what it owes about the unit's design, is [[design-notes-in-code-headers]]. A purpose that will not fit one sentence because the routine does two jobs is also a sign for [[routine-cohesion]], which owns the split. Whether the routine should touch global data at all is [[global-data]]; this page owns only a global access that stays, under a project convention or within that page's limits, and that the header does not name. A global's own declaration comment is [[comment-data-declarations]].

## When not to apply

- A documentation tool or a public API convention requires tags for each parameter. The book accepts the tool's format (p. 790), and project tooling decides it at work time.
- Get and set accessors need no summary sentence (p. 789).
- Short routines with clearly separated inputs and outputs need no direction markers (p. 790).

## Repair

1. Reduce the header to one or two sentences of purpose, and delete the fields that restate the body or duplicate version control.
2. If the sentence will not come, split the routine until each part has one.
3. Move notes on each parameter to the parameter's declaration, or to the tool's tags where one is used.
4. Add only the items this routine actually has: assumptions, limits, global effects, the algorithm's source.

## Before and after

```
// before
// ****************************************
// Name:      copy_string
// Purpose:   copies the source string into the target string
// Algorithm: gets the length of source, then copies each char
// Inputs:    source
// Outputs:   target
// History:   none
// Author:    D. K. Coder, 01.10.04
// ****************************************
function copy_string(target, source)
```

```
// after
// Copies source into target, including the terminator.
function copy_string(
    target,   // out: receives the copy; must hold length(source) + 1
    source    // in
)
```

## Source

[[code-complete]], ch. 32.5, pp. 787-791. The book's parts: the criticism of monolithic headers, the cost to factoring, the proximity principle, the one-or-two-sentence test with its exception for accessors, documenting parameters, marking inputs and outputs, assumptions, limitations, global effects and the sources of algorithms. The same chapter-9 demand for a header sentence that is easy to write is on [[pseudocode-programming-process]]. This wiki's own parts: the signs, the assignments against neighbouring pages (including the split with [[global-data]]), the order of the repair, and the pseudocode, including the capacity note. The quotations were transcribed from the extracted text and should be checked against the page image.
