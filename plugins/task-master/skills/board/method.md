# board: method

How every board skill reads the board, takes a snapshot, applies a changeset and replies. Settings
are those `skills/init/settings.md` describes; `<settings>` is the path of the project's workflow
config file. A `wiki/<group>/<page>.md` path is under `${CLAUDE_PLUGIN_ROOT}/knowledge/`. Every
board command runs under the permission rules `init` proposed; one no rule allows prompts each
time. `<scope>` in a file name is its slug: `:` and `/` become `-`.

## Before any job

1. **Find the settings** as `settings.md` says. No file, or no `[board]` in it: the board is not set
   up. Say so, point to `init`, and stop; work that needs no board goes on in the calling skill.
2. **Learn the tool from its help.** The tool is the board command the project's `CLAUDE.md` or `AGENTS.md` names.
   Read its `--help` and each subcommand's this job runs, before running any; use only what the
   help documents, and its capabilities command where it names one. Never ask for the help of a
   command that changes the tool itself: if it ignored the help flag, it would run.
3. **Decide each obligation from the help**, and name every fallback with its cost:

   | Obligation | Met when the help shows | Otherwise, and its cost |
   |---|---|---|
   | snapshot | one command writes a scope with its read time | composed from reads; not atomic |
   | history | a per-issue read returning `since` and `moves`, or the list carrying `status_since`, `started_at`, `finished_at`, `transitions` | none: age counts from creation; Work Item Age and cycle time unavailable |
   | guarded write | move and close take the expected status and refuse on mismatch, with an exit code for it | read, then write; a step can land between the two, and no move may be allowed in advance |
   | dry run | each write takes a dry-run flag | the prompt shows the command, not its effect |
   | batch | one command applies many operations, with a preview | one prompted command per operation |
   | batch refs | a later batch line may use an id an earlier line created | creates run first, in waves (*Applying a changeset*) |
   | sprints | a command lists them | the caller gives them |

   Also find: how a list returns the whole scope (every status, no page limit: a default page
   silently truncates a snapshot) and how it warns when more exist; the fields reporting a list's
   total and completeness; what a command does besides its name (a link that also closes a task);
   where comments are read, if the list leaves them out; whether the list fills `parent` only under
   a parent filter; the exit codes for a partial write, an unsupported operation, a guard refusal.

## Reads and the snapshot

A single read (one task, the statuses) is one command; a task whose status has no kind names that
status. A **snapshot** of a scope goes to the path the calling skill names, else
`.task-master/snapshot-<scope>.json`. The scope is `board`, `sprint:<name>`, `label:<name>` or
`parent:<id>`; none given, the whole board, said in the reply; the tool unable to read that scope,
say so and offer the board.

Every snapshot run passes the scope record (`<scope flags>`): `--scope "<scope>"`;
`--includes-finished true`, or `false` where the help says the list leaves finished work out;
`--reported-total` and `--complete` from the reply's total and completeness fields, found by
searching the raw list, not reading it (no such fields: pass neither, and the snapshot records
completeness unknown); `--empty-ok` only when the person confirms the scope is empty.

- **Native snapshot:** run it into `.task-master/raw-<scope>.json`, then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --native <raw> --settings <settings> <scope flags> [--history <dir>] --out <snapshot>`.
- **Composed:** write the list into `.task-master/raw-<scope>-issues.json`, the statuses into
  `raw-statuses.json` and, under iterations, the sprints into `raw-sprints.json` (from the caller
  where the tool has none, as `[{"id", "name", "state", "start_date", "end_date"}]`; from neither:
  omit `--sprints` and say every sprint-based check is not covered). Then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --issues <..> --statuses <..> [--sprints <..>] --settings <settings> <scope flags> [--history <dir>] --out <snapshot>`.
  Pass no `--taken-at`: the script stamps its own run time (basis `script_run_time`), and a typed
  time is a guess every age runs from. Say the snapshot is not atomic.
- **History reads**, where the tool returns history per issue: one read per issue the calling
  skill names (started tasks for age, finished ones for cycle time; none named, every issue of the
  raw list). Give the count in the caveats first; over about 50, ask.
- **History files:** each read as returned into `.task-master/history-<scope>/<id>.json` (a
  character outside `A-Za-z0-9._-` becomes `_`), then `--history` that directory; the script takes
  either shape, so convert nothing. An issue left out shows in `history.missing`: say it was scoped
  out, not lost. A history read whose status differs from the list's stops the script: the task
  moved between the reads; read both again.

Redirect each read into its file, never into the conversation. A read that warns it returned less
than the scope is not a snapshot: say so and stop. A list that fills `parent` only under a parent
filter gives no hierarchy: say so; every parent and child check is `not_covered`.

Then search the snapshot (never read it whole) for `unmapped_statuses`, `mapping_unknown_statuses`,
`issues_without_status`, `category_conflicts`, `markers_undeclared`, `markers_unknown_statuses`,
`scope` and `history.missing`, and name every non-empty entry. Never guess an unmapped status into
a kind; the fix is a category on the board or an entry in `[process.kinds]`, through `init`. Also
say: with no history, ages run from creation and Work Item Age is unavailable
(`wiki/reading-history/work-item-age.md`); with no comments in the snapshot, a check on comments
is `not_covered`. **Output:** the snapshot path and these caveat lines.

## Applying a changeset

The input is the changeset file another skill's result names, `.task-master/changeset-<slug>.json`
(one given only as text is first written to this form):

```json
{"source": "triage", "snapshot": ".task-master/triage-snapshot.json", "ops": [
  {"ref": "n1", "op": "create", "title": "…", "body_file": ".task-master/body-n1.md", "labels": ["M"], "done": null},
  {"ref": "n2", "op": "create_child", "parent": "n1", "title": "…", "body_file": "…", "done": null},
  {"ref": "l1", "op": "link", "id": "T-7", "other": "T-3", "relation": "duplicates",
   "why": "one change closes both", "page": "wiki/intake/duplicate-reports.md", "done": null},
  {"ref": "c1", "op": "close", "id": "T-7", "reason": "duplicate",
   "updated_at": "…", "why": "…", "page": "…", "decide": "Close T-7 as a duplicate of T-3?", "done": null},
  {"ref": "m1", "op": "move", "id": "T-4", "status": "Review", "expected": "In Progress", "done": null},
  {"ref": "a1", "op": "add_label", "id": "T-4", "label": "M", "updated_at": "…", "done": null},
  {"ref": "k1", "op": "comment", "id": "T-4", "body_file": ".task-master/body-k1.md", "done": null},
  {"ref": "e1", "op": "edit", "id": "T-4", "body_file": ".task-master/body-e1.md", "updated_at": "…", "done": null}]}
```

The ops are the plugin's: `create`, `create_child`, `edit`, `comment`, `add_label`,
`remove_label`, `set_type`, `set_priority`, `assign`, `link` (relation `blocks`, `duplicates` or
`relates`; it reads `id` <relation> `other`: for `blocks` the prerequisite is `id`, for `duplicates`
the duplicate), `close` (reason `done`, `duplicate` or `abandoned`), `move`. Each becomes the
tool's command from its help; an op or relation the tool lacks is reported unsupported, never
approximated. A value equal to a `ref` stands for that op's created id. `why` and `page` carry the
reason and the base page behind a proposal, `decide` the question that makes the op the person's
decision. Task text goes into body files, never into an argument; an `edit` body file holds the
whole new text.

Close reasons are a defined translation, not an approximation:

- `done`: the tool's done close.
- `abandoned`: the tool's canceled or abandoned close
  (`wiki/reading-history/non-standard-departure.md`, Abandoned work).
- `duplicate`: a `duplicates` link where the tool has one, plus the canceled close.
- Only a tool with no close but done reports `abandoned` and `duplicate` unsupported.

Freshness, so a write never lands on a task changed since the snapshot:

- Edits, closes and label changes to an existing task carry its `updated_at` from the snapshot.
- A move carries `expected`, its status there; a guarded close expects its status in the
  changeset's `snapshot`.
- An op on a task this changeset creates carries neither and skips the check.

1. **Check before the first write.** Every op maps to a command the help documents; every ref
   resolves to an earlier op; every guarded op carries its `updated_at` or `expected`. A delete, or
   any op the tool says cannot be undone, stays only if the person asked for it: dropped work is
   closed, not deleted (`wiki/reading-history/non-standard-departure.md`, Abandoned work). Anything
   failing: name the ops and write nothing until the person decides.
2. **Put the decisions to the person.** A short summary (counts per op, the file path) and each
   side effect the help names. Ask each op with `decide` by its question, with its `why` and
   `page`; every close is theirs to decide. Drop each op they decline from the file before writing.
3. **Order:** creates, parents before children; edits, labels, type, priority, assignment,
   comments; links; moves and closes. Before an edit, close or label op the tool cannot guard by
   `updated_at`, read the task: a later `updated_at` means it changed since; drop the op, say so.
4. **Write, preview first.** Show every preview or dry run verbatim, not retold; an error or
   unsupported op in a preview stops the apply. The tool's prompt on the real write is the
   person's approval.
   - **Batch with refs:** the whole file as one batch.
   - **Batch without refs:** creates go in waves, each wave every create whose refs already have
     ids, as a batch, or one by one where a create's id must be read from its output. After each
     wave write the new ids into `done` and into the later ops' refs; the rest goes as one batch.
   - **No batch:** one command per op, in order, each under its own prompt.

   After each success write its id or result into `done` at once, so a rerun skips it.
5. **On a failure**, record the exit code and stderr in the op, then:

   | Exit | Mark | Then |
   |---|---|---|
   | guard refusal | that op refused (changed since) | go on with the rest |
   | unsupported | every op of the same op and relation unsupported | go on with the rest |
   | anything else (a partial write; any failure where the help gives no codes) | that op failed | stop writing; never retry; read the tasks back before marking more `done` |

   A failed create stays failed until a read shows the task absent and the person confirms; a
   rerun never creates a task the file shows `done` or partial.
6. **Report three lists:** applied (with ids), failed (the tool's message verbatim), not attempted.
   Name tasks a failed link left unlinked.

## From decompose

`decompose` returns the path of its result, `.task-master/decompose-<slug>.md`; write its tree
into a changeset before applying, with `snapshot` null, since no board read preceded it.

- **Group node:** a `create` (under another node, a `create_child` of it) whose body is its purpose
  and its leaves' titles, with no size.
- **Leaf:** a `create_child` with `parent` its node's ref (no node: a `create`). Its `body_file`
  holds its five headings under decompose's names, each a `## <heading>` section with its text
  verbatim, except: a ref to another leaf becomes that leaf's title; every id from decompose's
  reply is replaced by its text; a `sequence` edge in Links reads "after <title>". A title carries
  no decompose ref.
- **Placeholder:** like a leaf, but its text says it is one and keeps its coarse size, with no
  size label: it is not sized as near work.
- **Edges:** a `sequence` edge is a `link` of relation `blocks`, the prerequisite as `id`; a `wait`
  edge stays in the text only, since what it waits for is off the board
  (`wiki/ordering/sequence-versus-wait.md`).
- **Size** goes only to the size label: the `[board.size]` key whose number equals it, in the
  create where the help's create takes a label, else an `add_label`. No `[board.size]`, or no key
  with that number: report it not applied.
- **Questions** go to the person before the apply, not into ops. Leaves a question names (`all`:
  every leaf) are held back until it is answered or the person says to apply on the stated
  assumptions, then copied into those bodies. A held-back group node holds back its leaves;
  a link to a held-back leaf is dropped and named.

Where the help says `blocks` is unavailable on this board (a plan or tier note), ask before the
first write: keep the order in the bodies' Links only, or link as `relates`, which keeps the pair
but loses the direction. Never choose for the person.

## Moves

Every move and close checks the expected state. **Guarded by the tool:** the command names the
expected status and the tool refuses on mismatch. **Read, then move:** read, refuse on another
status, then move, and say another step can land between the two.

The target status is one whose kind is the target kind; where several have it, the one the process
document names, else ask. **A single-task move is not run through this skill:** the working agent
runs it itself at the step that caused it, with the guard above. Asked how a move looks: the
filled-in command; it runs unprompted only when the tool guards it and the person allowed it.

## The reply

Every board skill answers the person in this order. **Caveats:** each fallback taken and its cost,
a snapshot not atomic, a scope not complete (the snapshot's `scope`; `scope_reason` where metrics
ran), the age basis, the lines *Reads and the snapshot* produced, any non-empty
`timestamp_problems` or `naive_timestamps`, and the envelope's `assumptions` and `not_covered`.
**Findings**, per dimension or item, each with its page. **Questions:** the envelope's
`questions`, for the person to answer. **The changeset:** its path, its ops by `op`, and that
`board` applies it, each close the person's decision. **What you need to do:** `needs_caller`.
