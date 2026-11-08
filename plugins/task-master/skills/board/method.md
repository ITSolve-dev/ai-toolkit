# board: method

This method's own procedure for the design's "Доступ к доске" and "Запись", unless a page is
named. The settings are those `skills/init/settings.md` describes; `<settings>` is the path of the
project's workflow config file. Every board command, read or write, runs under the permission rules
`init` proposed; one no rule allows prompts each time. `<scope>` in a file name is its slug: `:` and
`/` become `-` (`sprint-<name>`).

## Before any job

1. **Find the settings.** As `settings.md` says. No file, or no `[board]` in it: the board is not
   set up. Say so, point to `init`, and stop; what needs no board goes on in the caller's skill.
2. **Learn the tool from its help.** The tool is the one `settings.md` names (the board command the
   agent instructions name).
   Read its `--help`, then the help of each subcommand this job will run, before running any; use
   only flags and outputs the help documents, never a tool remembered from elsewhere. Where the help
   names a capabilities command, run it. Never ask for the help of a command that changes the tool
   itself: if it ignored the help flag it would run.
3. **Decide each obligation from what the help documents**, and say every fallback with its cost:

   | Obligation | Met when | Otherwise |
   |---|---|---|
   | snapshot | one command writes a scope with its read time | composed from reads; not atomic |
   | history | the list carries status_since, started_at, finished_at, transitions, or a command returns them per task | none: age counts from creation; history analyses unavailable |
   | guarded move | the move takes the expected status and refuses on mismatch | read, then move; a window between the two, and no move is allowed in advance |
   | batch | one command applies a file of operations, with a preview | one prompted command per operation, recorded as done in the file |
   | sprints | a command lists them | the caller gives them |

   A list must return the whole scope, every status and no page limit: find in the help how, since
   a default page silently truncates a snapshot. Note what the help says a command does besides its
   name (a link that also closes a task), the fields of a list's reply that report its total and
   completeness, and the exit codes for a partial write and an unsupported operation.
   *Wrong if:* a command or flag was used that the help does not show.

## Reads and the snapshot

A single read (one task, the statuses) is one command; a task whose status has no kind names
that status. A **snapshot** of a scope goes to the path the calling skill names, else
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
- **Composed:** write the list into
  `.task-master/raw-<scope>-issues.json`, the statuses into `raw-statuses.json` and, under
  iterations, the sprints into `raw-sprints.json` (from the caller where the tool has none, written
  as `[{"id", "name", "state", "start_date", "end_date"}]`; sprints from neither: omit `--sprints`
  and say every sprint-based check is not covered). Then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --issues <..> --statuses <..> [--sprints <..>] --settings <settings> <scope flags> [--history <dir>] --out <snapshot>`.
  Pass no `--taken-at`: the script stamps its own run time (basis `script_run_time`), and a typed
  time is a guess every age runs from. Say the snapshot is not atomic: an edit between the reads
  lands in it partly.
- **History**, where a command returns it per task: one read per issue the calling skill names
  (started tasks for age, finished ones for cycle time; none named, every issue of the raw list),
  each into `.task-master/history-<scope>/<id>.json` (a character outside `A-Za-z0-9._-` becomes
  `_`), then `--history` that directory. Before running, give the count in the caveats; over about
  50, ask. An issue left out shows in `history.missing`: say it was scoped out, not lost.

Where the help says the list leaves `parent` or `subtasks` empty unless filtered by a parent, the
snapshot holds no hierarchy: say so, and every check on parents and children is `not_covered`.

Redirect each read into its file, never into the conversation: the board does not pass through the
caller's context. A read that warns it returned less than the scope is not a snapshot: say so, stop.

Then search the snapshot (never read it whole) for `unmapped_statuses`, `mapping_unknown_statuses`,
`issues_without_status`, `category_conflicts`, `markers_undeclared`, `markers_unknown_statuses`,
`scope` and `history.missing`, and name every
non-empty entry. An unmapped status is never guessed into a kind; the fix is a category on the
board or an entry in `[process.kinds]`, through `init`. Also say: with no history, ages run from
creation and Work Item Age is unavailable; with no comments in the snapshot, a check on comments is
`not_covered`. *Output:* the path and these caveat lines. *Wrong if:* the reply is silent on a
non-empty list.

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
`relates`; it reads `id` <relation> `other`: for `blocks` the prerequisite is `id`, for
`duplicates` the duplicate), `close` (reason `done`, `duplicate` or `abandoned`), `move`. Each is
turned into the
tool's command from its help when applied; an op, relation or reason the tool lacks is reported
unsupported, never approximated. A value equal to a `ref` stands for that op's created id. `why`
and `page` carry the reason and the base page behind a proposal, and `decide` the question that
makes the op the person's decision. Task text goes into body files, never into an argument; an
`edit` body file holds the whole new text. Edits, closes and label changes to an existing task
carry its `updated_at` from the snapshot; a move carries `expected`, its status there. An op whose
`id` is a ref created in this changeset carries no `updated_at` and skips the freshness read: the
task did not exist when the snapshot was taken.

1. **Check before the first write.** Every op maps to a command the help documents; every ref
   resolves to an earlier op; every guarded op carries its `updated_at` or `expected`. A delete, or
   any op the tool says cannot be undone, stays only if the person asked for it: dropped work is
   closed, not deleted (`wiki/reading-history/non-standard-departure.md`, Abandoned work). Anything
   failing these: say which ops, and write nothing until the person decides. Show a short summary
   (counts per op, the file path), plus each side effect the help names for a command used. Put each
   op with `decide` to the person by its question, with its `why`; drop from the file every one
   they decline, before any write.
2. **Batch by the tool:** translate the file into its batch input, run its preview, and show the
   output verbatim, not retold. Where the batch takes no `updated_at` guard, first read each guarded
   task and drop, saying so, every op whose task changed since. An error or unsupported op in the
   preview: stop. Otherwise apply; its prompt is the person's approval.
3. **One by one:** order the ops: creates, parents before children; then edits, labels, type,
   priority, assignment, comments; then links; then moves and closes. Run one command per op, each
   under its own prompt. After each success write its id or result into `done` in the file at
   once, so a rerun skips it. Before an edit, close or label op, read the task; an `updated_at`
   later than the op's means someone changed it since: refuse that op.
4. **Stop on the first failure.** Record the exit code and stderr in the op, write nothing more,
   and report three lists. One exception: an unsupported exit wrote nothing, so the ops of the same
   op and relation are marked unsupported with it, and the rest go on. The lists: applied (with ids), failed (with the tool's message verbatim), not
   attempted. A partial exit, or any failed write where the help gives no codes, is
   never retried: the write may have landed. A failed create stays failed until a read shows the
   task absent and the person confirms. Name tasks a failed link left unlinked.
   *Wrong if:* a rerun creates a task the file already shows `done`, or one marked partial.

## From decompose

`decompose` returns the path of its result, `.task-master/decompose-<slug>.md`; write its tree
into a changeset before applying, with `snapshot` null, since no board read preceded it. A group
node is a `create` (under another node, a `create_child` of it) whose body is its purpose and the
list of its leaves' titles, with no size. A leaf is a `create_child` with `parent` its node's ref
(a leaf with no node, a `create`). A placeholder is a `create_child` under its group node (no
node, a `create`) whose text says it is one and keeps its coarse size, with no size label: it is
not sized as near work. A title carries no decompose ref. A leaf's `body_file` holds its five
headings, under the names decompose used, each as a `## <heading>` section with its text
verbatim, except: a ref to another leaf becomes that leaf's title; every id from decompose's reply
is replaced by its text, since the board does not hold the reply; a `sequence` edge in Links reads
"after <title>". A `sequence` edge is a `link` of relation `blocks` with the prerequisite as `id`;
a `wait` edge stays in the text only, since what it waits for is off the board. A leaf's `Size`
goes only to the size label, never the body: the `[board.size]` key whose number equals it, in the
create where the help's create command takes a label, else an `add_label`; no `[board.size]`, or
no key with that number, is reported as not applied. decompose's questions are put to the person
before the apply, not written as ops. The leaves a question names (`all`: every leaf) are held
back while it is unanswered, unless the person says to apply on the stated assumptions, which are
then copied into those bodies. A held-back group node holds back its leaves; a link to a held-back
leaf is dropped and named.

Where the help says `blocks` is unavailable on this board (a plan or tier note), ask before the
first write: leave the order in the bodies' Links sections only, or link as `relates`, which keeps
the pair but loses the direction. Never choose for the person.

## Moves

A move inside a changeset, and the single-task move below, check the expected state:

- **Guarded by the tool:** the move carries the expected status; the tool refuses on mismatch.
- **Read, then move:** read the task, refuse on a status other than the expected one, then move;
  say another step can land between the two.

The target status is one whose kind is the target kind; where several have it, the one the
process document names, else ask. **A single-task move is not run through this skill**: the
working agent runs it itself at the step that caused it, with the guard above (the design's
"Перевод состояния стоит один вызов"). Asked how a move looks: the filled-in command, and that it
runs unprompted only when the tool guards it and the person allowed it.

## The reply

Every board skill answers the person in this order. **Caveats:** each fallback taken and its cost,
a snapshot not atomic, a scope not complete (the snapshot's `scope`; `scope_reason` where metrics
ran), the age basis, the lines *Reads and
the snapshot* produced, any non-empty `timestamp_problems` or `naive_timestamps`, and the
envelope's `assumptions` and `not_covered`. **Findings**, per dimension or item, each with its
page. **Questions**: the envelope's `questions`, for the person to answer. **The changeset**: its
path, its ops by `op`, and that `board` applies it, each close the person's decision. **What you
need to do**: `needs_caller`.
