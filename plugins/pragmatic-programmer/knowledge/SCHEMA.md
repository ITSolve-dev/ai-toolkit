# Code Quality Rules — SCHEMA

<!--
This file is the CHARTER and the ROOT MARKER: its presence marks this directory as a wiki
root, and its contents are the lens ingest uses to decide what to keep.

Per Karpathy, the schema is "what makes the LLM a disciplined wiki maintainer rather than a
generic chatbot" — and it is a LIVING document you and the LLM co-evolve as you learn what
works for this domain. The generic structure/conventions/workflows live in the llm-wiki
plugin; this file holds the DOMAIN-SPECIFIC charter and any local overrides. Fill every
section, then keep refining it.
-->

## Purpose

A working reference of rules for writing good code in any language. It serves two readers: the
agents of the plugin that bundles this wiki, which apply a rule to a piece of code and cite it, and
the people who open the cited page to check that decision and learn the rule.

The model already knows these rules by name, so a retelling of a book adds nothing. What it lacks is
the judgement on a specific piece of code: is the rule broken here, does it apply, what exactly
changes. A page earns its place by supplying that judgement.

A claim belongs here only if it changes what the expert writes, changes or reports about a specific
piece of code.

## Scope — the ingestion lens

Ingest judges every candidate fact from a source against this. A rule is recorded as its source
states it, whatever language the source's examples use, and is not transferred to any other
language: how it applies in the language of a project is decided at work time.

**In scope (keep):**
- **Complexity:** accidental complexity, depth of nesting, duplication, abstraction that does not
  pay for itself.
- **Structure:** cohesion and coupling between classes and functions inside a module, and the
  direction of dependencies between them.
- **Objects:** responsibilities, encapsulation, composition and inheritance, class interfaces.
- **Functions:** size, arguments, side effects, composition, functional style.
- **Errors:** failure handling, contracts, assertions, defensive code, including code that faces
  hostile input.
- **Types and state:** making invalid states unrepresentable, mutation, state machines.
- **Testing:** what a test should pin, test design, what makes a test brittle.
- **Debugging:** finding a cause by method rather than by guessing.
- **Naming:** names that carry meaning.
- **Documentation in code:** what a comment or a docstring owes the reader, and when it lies.
- **Change:** refactoring, changing code safely, reversibility.

**Out of scope (drop):**
- Career, team, process and estimation advice: it has no sign in code.
- Rules of a particular language, its idioms and its style: they are taken at work time from the
  project's tooling, conventions and current documentation.
- Mechanical style: formatting and whatever a linter or a type checker catches.
- Documentation of particular libraries and frameworks: it goes stale faster than this wiki.
- Modelling a business domain: that is `domain-driven-guide`.
- Project documents such as design docs and decision records: that is `spec-driven-guide`.
- Architecture: system design, splitting an application into modules or services, the shape chosen
  for a module (layers, ports and adapters, transaction script, domain model), how modules talk and
  which way they depend. The expert takes it as given from the project's conventions or the brief, and
  reports code that contradicts it. A page that applies a rule inside a module may name the
  architecture as a setting; it does not prescribe one.

## Domain extraction schema

From each source, extract these kinds of knowledge:

- **Rules**, each with the sign by which a violation shows in code.
- **Limits** — when the rule does not apply. A rule without limits gets applied everywhere, and a
  misapplied rule looks grounded.
- **Repairs** — what exactly to change once the sign is found.
- **The reasoning under a rule** — what specifically breaks when it is ignored. A rule without its
  reasoning cannot be applied to a case its author did not foresee.
- **Discriminating criteria** — what separates two neighbouring cases: duplicated knowledge from a
  chance likeness, one reason to change from two.
- **Trade-offs** — what a rule costs when it is followed.
- **Procedures** — a method to run against code, such as a way to narrow down a failure.
- **Before/after pairs**, wherever a source shows code rewritten.

## Grouping principle

Pages live in subdirectories of `wiki/`, grouped by **the problem someone arrives with in the code**,
not by source and not by paradigm. The starting groups are `complexity`, `structure`, `objects`,
`functions`, `errors`, `types-and-state`, `testing`, `debugging`, `naming`, `documentation` and
`change`. A page's `category` frontmatter equals its folder name.

Groups are flat. The index reads only direct children of `wiki/`, so a nested folder drops out of it
without any error. There are no groups per language or per book.

A group is also one review dimension: the plugin runs one `inspector` per group, and that inspector
searches the group's summaries and opens the pages the code calls for. A new group therefore adds a
dimension, so create one only for a problem no existing group covers.

## Languages

- **Wiki language:** English — pages, summaries, and synthesis are written in English.
- **Communication language:** Russian — the LLM converses in Russian (questions, surfaced takeaways,
  reports).
- **Quotation language:** a quotation stays in the language of the source that was read. See
  *Quotations and citations*.

## Conventions

- Pages, frontmatter, and `[[wikilinks]]` follow the `llm-wiki` plugin's page conventions.
- Link style: `[[slug]]` (Obsidian-style).
- Keep `sources:` as an inline list: lint reads top-level scalars only.
- `summary` names the sign in code rather than the topic, because agents find pages by searching
  summaries inside a group and do not read the whole index.
- Every page except a `summary` page carries `paradigm: any`, `paradigm: oop` or `paradigm: fp`.
  Otherwise the expert applies a rule for objects to functional code.

### Page kinds

The first entry in `tags` is the page's kind.

| Kind | What it holds |
|---|---|
| `summary` | One per ingested source |
| `concept` | An idea the rules rest on, defined and situated |
| `rule` | A prescription, with its sign in code |
| `decision-rule` | A test deciding between two courses, or between two sources that disagree |
| `method` | A procedure to run against code |

### Rule pages

`rule` and `decision-rule` pages carry these sections, in this order. `scripts/check_pages.py`
enforces them.

| Section | What it answers |
|---|---|
| `## Rule` | What to do, in the source's terms |
| `## Sign in code` | How a violation shows in code that a reader has in front of them |
| `## When not to apply` | The conditions under which the rule does not hold |
| `## Repair` | What exactly to change |
| `## Before and after` | Pseudocode in fenced blocks with no language tag |
| `## Source` | Book, edition and page of each claim, as a link to the source's summary page, and which parts are this wiki's own |

Examples are this wiki's own pseudocode, so a page stays independent of any language and the
repository does not republish a book's listings.

The pair shows the rule's sign and its repair on the same code. A page whose sign cannot be shown in
code has failed the rule below, whatever its other sections say.

### Quotations and citations

- A verbatim quotation matches the source character for character, so it exists only in the language
  of the edition that was read. Six of the seven starting books were read in Russian: a short
  quotation from one stays in Russian inside an English page. Typographic variants count as equal:
  a straight or curly apostrophe or quote mark, a dash lost or a hyphen dropped by text extraction.
  A word or letter lost to extraction is quoted around, never restored by guess.
- English text about such a book is a paraphrase. It carries no quotation marks and names the page
  of the edition.
- Quotations are short. Pages are written in this wiki's own words, because the repository is public
  and `raw/` stays out of it.
- Where extraction is noisy, a quotation is checked against the page image, not against `raw/`. If it
  was transcribed, the page says so.
- `raw/` marks printed pages as `<!-- p. N -->`, or `<!-- pp. A-B -->` where one scanned page holds two. A citation names that page, and not a line of the
  raw file, because the raw file is not published and a reader holds the book.

### Pages this wiki authored itself

Some pages carry `sources: []` and an explicit provenance note. They exist where the charter names
something in scope and no ingested source treats it. They say what would have to be found to ground
them. Their number should go down, not up.

## Workflow customizations

- **Ingest: a rule is kept only with a sign in code.** Advice that cannot be checked against a piece
  of code is commentary, not knowledge for this wiki. A source that says "keep it simple" yields a
  rule only once someone names what the opposite looks like in code. Source summaries, concepts and
  methods are exempt.
- **Review: a sign is something a reader can point at.** It names a construct, a shape, a count or a
  relation in code that is in front of the reader. A sign needing a forecast of how the code will
  change, or knowledge of who else uses it, is not a sign; such a page says what it would need. Two
  tests for a vague sign: could it be true of nearly any code, and could an honest reader fail to
  find it where it applies? A vague sign is never absent, so it also hides false applications. This
  is judged by page review. `check_pages.py` catches only an empty or token section.
- **Ingest: a page states when its rule does not hold.** A source rarely says so.
- **Ingest: what the source does not state is marked.** A sign, limit or repair that is this wiki's
  own reasoning is named as such in `## Source`. A reader who checks a decision has to see whether it
  rests on a book or on the model that wrote the page.
- **Ingest: where sources disagree, the page resolves it per setting.** It states the condition under
  which each side holds. Recording that the books disagree returns to the expert the very hard case
  it came to the page for.
- **Ingest: one code shape, one owner.** Pages from different topics of a source converge on the same
  shape in code, and with no rule between them one fragment earns several findings, sometimes with
  opposite repairs. Where two pages fire on one shape, one owns the sign, and both state the condition
  that selects the page, in the same words. A summary states the sign, because that is what agents
  search. This holds across sources: a new source's page joins the owner rather than standing beside
  it. An assignment stands only after a second reader has walked a hard fragment through both pages:
  of eight made without that, seven still split on a concrete fragment.
- **Ingest: a page's own limit is checked against its own pair.** The "after" has no sign of this page
  or of a neighbour, and the "before" falls outside the page's limits.
- **Ingest: the held-out material below is never read.** A page written with the test in view makes
  the base the answer key.
- **Writing: any sentence extending a quotation or a paraphrase opens with an explicit subject.**
  "This wiki reads that as…", "the transfer here is ours…". Unbroken declarative prose makes the
  extension read as the source's, which is the failure most damaging to a base whose value is that a
  reader can go and check. Paraphrase is the default here, so the risk is larger than behind a block
  quote.
- **Compression: a light pass follows an ingest whose pages show filler.** Read a sample of ten pages
  first, because the pass costs a full read of the wiki. It removes filler and keeps full sentences,
  because people read these pages. Before the pass the wiki is copied aside, and afterwards
  `scripts/check_pages.py <wiki-root> --baseline <copy>` must pass: frontmatter, headings, code,
  quotations, wikilinks, the `## When not to apply` and `## Source` sections, and every sentence
  holding a negation or a number match the copy exactly. A damaged quotation reads like ordinary text,
  so reading the page will not reveal it. `log.md` and `wiki/index.md` are not compressed.

### Held-out material

Reserved for checking the plugin. Scout and ingest skip these.

- The tasks of the pilot and of the repeat evaluation. They stay outside this repository; the person
  running the check knows which they are. A symptom's example on a page must never be reused as a
  test case for that symptom.

## Notes

Starting sources, with what extraction needs:

- Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition (Russian translation, Dialektika,
  2020, 370 pages) — the pilot source. Its text layer has recognition noise. `read-book --fast` fails
  with `pymupdf4llm` 2.0, which ships no module, so the raw file was built page by page.
- McConnell, *Code Complete* (Russian edition, 889 pages).
- Weisfeld, *The Object-Oriented Thought Process* (Russian translation, Piter, 2014, 304 pages) — clean text layer, headings from the PDF outline, so quotations can be checked against `raw/`.
- Larman, *Applying UML and Patterns*, 3rd ed. (English, Addison-Wesley, 2004) — the Russian edition
  is a scan without a text layer, so the English e-book is used instead. Only chapters 17, 18, 25, 26
  and 35 (GRASP and GoF) are in `raw/`; the rest is analysis, UML, process or architecture. The e-book
  has no printed page numbers: pages cite chapter or section numbers (for example 17.11) plus the PDF
  page from the `<!-- p. N -->` markers. Quotations are in English.
- Polikarpova, Shalyto, *Automata-Based Programming* (Russian, 168 pages) — only the `--fast` mode
  of `read-book` extracts it cleanly.
- Bugayenko, *Elegant Objects*, Java Edition (Russian translation, Piter, 2018; 120 PDF pages holding
  two printed pages each, about 240 printed pages) — OCR with heavy noise. Check every quotation
  against the page image. Its markers read `<!-- pp. A-B (pdf page N) -->`: a citation names the one
  printed page of the pair that holds the claim. The book is deliberately radical (no getters, no
  static methods, no `NULL`, no names ending in -er, only checked exceptions) and disagrees with common
  practice and with *The Pragmatic Programmer* in places. Its pages resolve each disagreement per
  setting, and its limits name the project convention that overrides it.
- Fowler, *Refactoring: Improving the Design of Existing Code*, 2nd ed. (English, Addison-Wesley,
  2018) — e-book PDF with a clean text layer but no printed page numbers: cite the chapter and the
  refactoring or smell name plus the PDF page from the `<!-- p. N -->` markers. Examples are
  JavaScript; pages take the ideas only, in pseudocode. Quotations are in English. It overlaps
  heavily with *Code Complete* on refactoring and smells; merge into the existing owners.
- Wlaschin, "Railway oriented programming" (2013) and "Against Railway-Oriented Programming" (2019),
  fsharpforfunandprofit.com — web articles; the second is the author's own limits on the first.
- Hombergs, *Get Your Hands Dirty on Clean Architecture* — removed from this base: it is about
  application architecture, which is out of scope.

Author names and editions above are from memory: confirm them at ingest.

The list has almost no functional programming and no core source on changing code safely. Those two
are scouted against this charter.

Books beyond the pilot are ingested only after the pilot succeeds. The design explains why.

<!-- Co-evolution log: record decisions about how THIS wiki is run as they emerge. -->

- 2026-11-01 — Charter written before the first source, from the plugin's design. Pages are grouped by
  problem in code, and each group doubles as a review dimension, so the dimension set is never
  maintained on its own. Language pages were ruled out by the owner: the sources are not tied to any
  language, and a chosen set of languages would stop the plugin being general.

- 2026-11-01 — A second opinion on this charter changed four things, before any source. **Authored
  parts are marked:** books rarely state a sign or a limit, so most of what the expert applies may be
  the ingesting model's own, and the base must not present that as a book. **The strict reading of a
  sign came back:** `spec-driven-guide` learned it after its audit, this charter had dropped it, and
  "premature abstraction" was its own counterexample. **The explicit-subject rule now covers
  paraphrase,** because six of seven books arrive that way. **`## When not to apply` is protected from
  compression,** because a lost limit turns into a false application and reads fine.

  One prediction to check rather than a rule: signs are written for code that exists, so they may
  help `inspector` and `improve` more than `write`. The pilot records this per mode.

- 2026-11-01 — First source in. 145 pages, every quotation matching `raw/`, and `check_pages.py` clean,
  yet an independent review of every page against `raw/` left 26 pages without findings. The ingest's
  own checks catch form and verbatim text; they do not catch hardened paraphrase, a book's reason
  retold as its limit, signs true of nearly any code, or pairs that keep the sign. Independent review
  is therefore a required step of each ingest, not a spot check. The worst class was convergence
  without a selection rule, hence "one code shape, one owner". Security pages stayed, under defensive
  code, because they have signs in code; the password policy page went, because it was a dated digest
  of an outside standard, which is what this charter excludes for libraries.

  The compression pass removed 50 bytes of 620 KB for about 300k tokens. The pages were written tight,
  and nearly every remaining sentence carries a negation, a page number or a protected section, so the
  check leaves nothing to take. The pass now runs only where a sample shows filler.

- 2026-11-02 — A showcase on nine tasks (four from scratch, five refactors of the owner's projects),
  three variants each, did not show the gain the pilot asks for: a blind model grader ranked the base
  over the same agent without it in 5 of 9, and over a plain session in 7 of 9; the owner's quick
  ranking split evenly. The three variants chose the same algorithm and structure nearly every time,
  and the base changed details. The owner judged all three weak on object design and chose to go on
  with the remaining books, Elegant Objects included, since the first source holds almost nothing on
  objects. Books beyond the pilot are therefore ingested by the owner's decision, not by a passed
  pilot; the repeat evaluation after them is what decides the format.

- 2026-11-03 — Second source in (*Elegant Objects*). The ingest again passed its own checks, and the
  independent review again found blockers on most touched pages: 35 of 49. Two thirds were owner
  conflicts that a new radical source creates against pages already in place, so a later source costs
  more review than the first did. OCR quotations matched `raw/` and still differed from the print in
  13 of 83 (a hyphen for a dash, a neighbouring page of the spread): matching `raw/` is not enough for
  a scanned book, and the image check stays part of the review.

- 2026-11-06 — Scope narrowed by the owner: the base covers code inside a module — classes,
  functions, their interfaces and data flow. Application and module architecture (splitting into
  modules, layers, ports and adapters, the shape of a module, how modules talk) is out of scope and is
  taken as given. Hombergs' book left the source list for that reason. Pages already in the base that
  prescribe an architecture are rewritten to name it as a setting or removed.

- 2026-11-06 — Third source in (*Code Complete*), the largest so far: 277 proposals, 244 touched pages.
  The review again found blockers on about half of them, and again most were owner conflicts with pages
  already in place, now across three books. Applying fixes one reviewer at a time, each re-reading
  the page and reusing a selecting sentence already written, kept the shared sentences identical; the
  cost is a sequential tail of about two hours for this source. Nine pages left the base: four on
  architecture under the narrowed scope, five folded into the page that already owned their shape.
