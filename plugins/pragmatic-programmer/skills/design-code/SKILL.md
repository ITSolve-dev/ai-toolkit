---
name: design-code
description: >-
  Compare designs for code inside a module and recommend one, with cited pages; edits no files. Use
  when concrete code is to be structured or restructured: how to split it into functions and
  classes, where a piece of logic should live, "classes or functions here?". An abstract question
  about a rule goes to ask. Not for modelling a business domain (that is domain-driven-guide), nor
  for architecture: splitting a system into modules or services, or choosing how a module is built.
argument-hint: "<what to design, and the code in scope>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Grep, Glob
---

# Design code

One designer left alone produces the average structure, and the base then only tunes its details.
This skill forces the alternatives into the open, compares them, and recommends one.

Base root: `${CLAUDE_PLUGIN_ROOT}/knowledge`. Designers cite `wiki/...` paths relative to it;
resolve them there in step 4.

**Where a designer reports a denied read or `BLOCKED` on the base, say so before any result.** Its
design then reads exactly like a grounded one and is not. Interactively the fix is approving the
prompt; headlessly, passing the plugin directory with `--add-dir`.

## Steps

1. **Write down the frame.** Read `.claude/pragmatic-programmer.md` if present; pass the convention
   paths it names, not copies. Then state, briefly:
   - the problem and goals;
   - the constraints — behaviour to keep, invariants, performance or compatibility limits;
   - the consumers — the code, tests and public interfaces that depend on the result, found in the
     code rather than inferred;
   - the changes expected — from the request, the history of the code in scope, or the user. Every
     candidate is scored against this one list, so it goes into every brief.

   If the question is what the domain concepts are and where their boundaries fall, stop and point
   to `domain-driven-guide`: this skill takes the concepts as given.

   Architecture is given too: the split into modules or services, how a module is built (layers,
   ports and adapters, transaction script, domain model), and how modules talk and depend. Take it
   from the conventions or the brief and put it in the frame. If the question is the architecture
   itself, say it is out of scope and stop; if the code in scope contradicts it, report that rather
   than design around it.

2. **Choose one designer or several.** A single `pragmatic-programmer:designer`, with no constraint,
   only when the decision stays inside one unit (one function, or one file's internals), its
   interface to consumers stays as it is, and no expected change reaches past it. Having consumers
   does not by itself call for the full comparison; changing what they see does. When unsure, run
   the full comparison.

3. **Dispatch in parallel**, in one message, one `pragmatic-programmer:designer` per constraint:
   - behaviour on data / objects;
   - pipeline of pure transformations, effects at the edge;
   - plain data and procedures / table dispatch;
   - keep the current structure — only when existing code is in scope.

   Skip a constraint the project's conventions rule out, and say which and why. Each brief carries
   the same frame, the paths in scope, the base groups to search (`structure`, `objects`,
   `functions`, `types-and-state`, `complexity`, `change`) and its one constraint — not your
   preference and not the other designs. A designer that knows what you expect drifts toward it, and
   the options stop differing.

   `NEEDS_INFO`: collect the questions from all designers, ask the user once, add the answers to the
   frame, and continue each affected designer (`SendMessage`) so the frames stay identical. With
   nobody to ask, answer under the most likely reading and mark each answer as assumed. A designer
   still `BLOCKED` leaves the comparison; report it as incomplete.

4. **Compare** the candidates on:
   - **Grounding.** Decisions on an opened page versus `model opinion`. For the pages behind the
     points that decide the recommendation, open them and confirm their `## Sign in code` is in this
     code and their `## When not to apply` does not hold; otherwise count them as opinion.
   - **Cost of later change.** For each expected change, whether the candidate confines it to one
     place or spreads it across units and consumers.
   - **Consumers.** What each candidate breaks or forces to change.
   - **Conventions.** A candidate that breaks a project convention loses unless the user overrides
     it.
   - **Strain.** Where a designer said its constraint fits badly.

   Candidates that converge despite different constraints are a finding: the problem forces the
   structure.

5. **Recommend one.** A hybrid only when its parts are independent; mark it as composed here, name
   which part comes from which candidate, and treat the seam as `model opinion` unless a page covers
   it. **The current structure wins** when no candidate lowers the cost of the expected changes
   enough to pay for the migration and the consumer risk, and when that gain is unclear. Then
   propose no change; that is a full answer.

## Deliver

- The recommendation in one or two sentences, and whether one designer or the full comparison ran.
- The winning design as its designer returned it — signatures or pseudocode, data flow — with its
  citations attached, not rewritten.
- Why it wins: the points from step 4 that decided it, each with its page or `model opinion`.
- Each rejected candidate in one line: what it would have cost.
- Conflicts with project conventions, and which way the recommendation went.
- What is unverified: assumed answers, consumers not traced, a designer that was `BLOCKED`.
