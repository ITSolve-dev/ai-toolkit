# pragmatic-programmer

A code expert the working agent delegates to. The agent hands over one part of a task; the expert
works in a clean context, applies rules from a curated knowledge base, cites the rule behind each
decision, and reports back. What to accept stays the caller's decision.

Language-agnostic: the base holds rules for object-oriented, functional and procedural code, with
examples in pseudocode. How a rule applies in your language is decided at work time, from your
project's tools and conventions. Conventions recorded in your project win over the books; the
expert names the conflict in its report.

The name refers to the book the base starts from. This plugin is unofficial and is not affiliated with
the authors or publishers of any book it cites.

## Install

```
/plugin install pragmatic-programmer --marketplace ITSolve-dev/ai-toolkit
```

## Use it

```
/pragmatic-programmer:init                 # once per repository
/pragmatic-programmer:ask when is a boolean parameter a smell?
/pragmatic-programmer:design-code          # compare designs before writing
/pragmatic-programmer:write-code
/pragmatic-programmer:improve-code src/billing/invoice.py
/pragmatic-programmer:debug-code the nightly export drops the last row
/pragmatic-programmer:review-code          # the current diff
/pragmatic-programmer:check-tests tests/billing
```

"No changes needed" is a valid result of `improve-code` and `review-code`: good code is left as it is.

## Skills

| Skill         | For                                                                         |
| ------------- | --------------------------------------------------------------------------- |
| `init`        | Writes `.claude/pragmatic-programmer.md`: languages, paradigm, check commands, where conventions live |
| `ask`         | A question about a rule, with citations. Read-only                          |
| `design-code` | Several designs for code inside a module, one recommendation. Edits nothing |
| `write-code`  | New code or changed behaviour, then an independent check                    |
| `improve-code`| Same behaviour, better structure, then an independent check                 |
| `debug-code`  | Failing command, ranked hypotheses, a fix and a regression test             |
| `review-code` | Findings, each backed by a page; a separate check against the ticket        |
| `check-tests` | What the tests would catch, proven by mutants in a scratch copy             |

## Agents

| Agent       | Tools                                 | Input → output                          |
| ----------- | ------------------------------------- | --------------------------------------- |
| `guide`     | Read, Grep, Glob                      | a question → an answer with citations   |
| `designer`  | Read, Grep, Glob                      | a design task and a constraint → a design |
| `inspector` | Read, Grep, Glob                      | one group of rules → findings           |
| `craftsman` | Read, Grep, Glob, Edit, Write, Bash   | a brief → edits, check results, a report |

The tool list is the boundary, not the prompt. `craftsman` is the only agent that changes files. It
changes only what the brief covers, runs the project's checks and reports each with its command and
output, warns when no test covers the behaviour, and never discards work through git: an undo is an
edit. Its report ends with a status: `DONE`, `NEEDS_INFO` (questions for the caller) or `BLOCKED`.

## Scope

Classes and functions inside a module: their composition, interfaces, data flow, errors, state,
tests, naming and comments. Out of scope: the architecture of an application (splitting it into
modules or services, layers, ports and adapters, dependencies between modules), which the plugin
takes as given; a language's idioms; domain modelling (`domain-driven-guide`); documents
(`spec-driven-guide`).

## The base

498 pages in eleven groups (`change`, `complexity`, `debugging`, `documentation`, `errors`,
`functions`, `naming`, `objects`, `structure`, `testing`, `types-and-state`), grouped by the problem
a reader arrives with, not by book. Sources:

- Thomas, Hunt — *The Pragmatic Programmer*, 20th anniversary ed.
- McConnell — *Code Complete*, 2nd ed.
- Fowler — *Refactoring*, 2nd ed.
- Larman — *Applying UML and Patterns*, 3rd ed. (GRASP and GoF chapters)
- Weisfeld — *The Object-Oriented Thought Process*
- Bugayenko — *Elegant Objects*
- Polikarpova, Shalyto — *Automata-Based Programming*
- Wlaschin — "Railway Oriented Programming" and "Against Railway-Oriented Programming"

Every rule page carries a **sign in code** that a reader can point at, the settings where the rule
does not hold, a repair, and a before/after pair. Where books disagree, the page says which applies
in which setting. One code shape has one owning page, so one fragment does not earn two findings with
different repairs. Quotations stay in the language of the edition read; the rest is paraphrase with a
page reference. `knowledge/SCHEMA.md` holds the charter.

`knowledge/raw/` (the extracted book text) is gitignored for copyright; `knowledge/wiki/` is committed.

## Reading the base

The base lives in the plugin's install directory, outside your project. A hook approves reads of
`knowledge/`, so background agents do not stop on a permission prompt, and denies writes to it, so an
agent holding `Write` cannot change the installed base. Your own deny rules still take precedence.

The hook needs [`uv`](https://docs.astral.sh/uv/), which `llm-wiki` already requires. Without it the
first read asks for permission instead, and the write guard does not run. The hook starts a process
on every Grep, Glob and shell call in a session with the plugin enabled; that costs about 0.5 s per
call on Windows. The shell check matches text: it denies a command naming the installed plugin, and
cannot stop a command that builds the path at run time.

The guard also applies when the plugin is loaded from a source checkout with `--plugin-dir`, so
maintain the base with the plugin loaded from an install.

## Headless runs

`claude -p` cannot answer a permission prompt, and Claude Code denies `Bash` there unless it is
granted. The writing skills run your project's checks, so grant exactly those commands, for example
`--allowedTools "Bash(uv run pytest:*)" "Bash(uv run ruff check:*)"`. `init` records the commands in
`.claude/pragmatic-programmer.md`, which is meant to be committed so the whole team shares it. Without
the grant the expert reports each check as `NOT_RUN` instead of guessing a result.

## Requires

- `llm-wiki`: the bundled base is an llm-wiki.
- `spec-driven-guide`: comments and docstrings follow its writing discipline.

## Credits

The order of steps in the skills draws on ideas from open skills published under the MIT licence:
Matt Pocock's skills, `superpowers`, Addy Osmani's skills, `what-could-break`,
`agentic-verification` and `obsess`. The text here is this plugin's own; it installs none of them and
does not depend on them.

## Maintaining

Check pages with `uv run --no-project scripts/check_pages.py knowledge`. Run the tests with
`uv run --no-project -m unittest discover -s tests` from the plugin root.

`scripts/run_pilot.py` runs the blind comparison from the design doc: its docstring gives the task
format and the commands. The tasks stay outside this repository, because the base must be written
without seeing them.

Design: [`docs/specs/2026-11-01-pragmatic-programmer-design.md`](../../docs/specs/2026-11-01-pragmatic-programmer-design.md).
