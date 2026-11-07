# board: method

This method's own procedure for the design's "Доступ к доске" and "Запись", unless a page is
named. `{cmd:<name>}` is the entry `<name>` of `[board.commands]`, run as recorded. Every board
command, read or write, runs under the permission rules `init` proposed; one no rule allows prompts
each time. `<scope>` in a file name is its slug: `:` and `/` become `-` (`sprint-<name>`).

## Before any job

1. **Read `.claude/task-master.toml`.** Absent, or `access = "none"`: the board is not set up.
   Say so, point to `init`, and stop; what needs no board goes on in the caller's skill.
2. **Check the tool version.** Run `{cmd:version}` against `tool_version`. Different: name both;
   reads go on, and before a write ask whether to go on or rerun `init`, since the recorded
   commands may no longer hold. No `version` entry: say a changed tool goes unnoticed.
   *Wrong if:* a write ran on a changed version without the person's word.

## Reads and the snapshot

A single read (one task, the statuses) is its command run once; a task in a status not in
`[states]` names that status. A **snapshot** of a scope goes to the path the calling skill names,
else `.task-master/snapshot-<scope>.json`. The scope is `board`, `sprint:<name>`, `label:<name>` or
`parent:<id>`, read by `{cmd:list}`, `{cmd:list_sprint}`, `{cmd:list_label}` or `{cmd:list_parent}`;
none given, the whole board, said in the reply; no recorded command for it, say so and offer the board.

Every snapshot run passes the scope record (`<scope flags>` below): `--scope "<scope>"`;
`--includes-finished true`, or `false` where `[board.notes]` says the list leaves finished work out;
`--reported-total` and `--complete` from the reply fields `[board.notes].list_total` and
`list_complete` name, found by searching the raw list, not reading it (a field not recorded: pass
neither, and the snapshot records completeness unknown); `--empty-ok` only when the person
confirms the scope is empty.

- **`snapshot = "native"`:** run `{cmd:snapshot}` into `.task-master/raw-<scope>.json`, then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --native <raw> --config .claude/task-master.toml <scope flags> [--history <dir>] --out <snapshot>`.
  The tool's snapshot carries its own read time.
- **`snapshot = "composed"`:** note the time of the first read (ISO 8601 with its zone), then run
  the list into `.task-master/raw-<scope>-issues.json`, `{cmd:statuses}` into `raw-statuses.json`
  and, under iterations, the sprints into `raw-sprints.json`: `{cmd:sprints}` where
  `sprints = "native"`; where `sprints = "caller"`, the iterations the caller or the person gives,
  written as `[{"id", "name", "state", "start_date", "end_date"}]`. Then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --issues <..> --statuses <..> [--sprints <..>] --taken-at <time> --config .claude/task-master.toml <scope flags> [--history <dir>] --out <snapshot>`.
  Say the snapshot is not atomic: an edit between the reads lands in it partly.
- **History**, where `history = "native"` and `{cmd:history}` exists: one read per issue the
  calling skill names (started tasks for age, finished ones for cycle time; none named, every issue
  of the raw list), picked by status through `[states]`, each into
  `.task-master/history-<scope>/<id>.json` (a character outside `A-Za-z0-9._-` becomes `_`), then
  `--history` that directory. Before running, give the count in the caveats; over about 50, ask.
  An issue left out shows in `history.missing`: say it was scoped out, not lost.

Redirect each read into its file, never into the conversation: the board does not pass through the
caller's context. A read that warns it returned less than the scope is not a snapshot: say so, stop.

Then search the snapshot (never read it whole) for `unmapped_statuses`, `mapping_unknown_statuses`,
`issues_without_status`, `markers_unreadable`, `scope` and `history.missing`, and name every
non-empty entry: an unmapped status is never guessed into a kind; the fix is rerunning `init` (the
design's "Состояние, которого нет в соответствии, названо при первом же чтении"). Also say: under
`history = "none"` ages run from creation and Work Item Age is unavailable; with no comments in the
snapshot, a check on comments is `not_covered`. *Output:* the path and these caveat lines.
*Wrong if:* the reply is silent on a non-empty list.

## Applying a changeset

The input is the changeset file another skill's result names, `.task-master/changeset-<slug>.json`
(one given only as text is first written to this form):

```json
{"source": "triage", "snapshot": ".task-master/triage-snapshot.json", "ops": [
  {"ref": "n1", "op": "create", "title": "…", "body_file": ".task-master/body-n1.md", "done": null},
  {"ref": "n2", "op": "create_child", "parent": "n1", "title": "…", "body_file": "…", "done": null},
  {"ref": "l1", "op": "link", "id": "T-7", "other": "T-3", "type": "<[links].duplicates>",
   "why": "one change closes both", "page": "wiki/intake/duplicate-reports.md", "done": null},
  {"ref": "c1", "op": "close", "id": "T-7", "reason": "<[board.close_reasons].duplicate>",
   "updated_at": "…", "why": "…", "page": "…", "decide": "Close T-7 as a duplicate of T-3?", "done": null},
  {"ref": "m1", "op": "move", "id": "T-4", "status": "In Review", "expected": "In Progress", "done": null}]}
```

`op` is a `[board.commands]` key, the other keys fill its placeholders, and a value equal to a
`ref` stands for that op's created id. Three keys are not placeholders: `why` and `page` (the
reason and the base page behind a proposal) and `decide` (the question that makes the op the
person's decision). A `link`'s `type` is a value of `[links]` and a `close`'s `reason` one of
`[board.close_reasons]`, copied as written. Task text goes into body files, never into an argument;
an `edit` body file holds the whole new text. Edits, closes and label changes to an existing task
carry its `updated_at` from the snapshot; a move carries `expected`, its status there.

1. **Check before the first write.** Every op has a recorded command; every ref resolves to an
   earlier op; every guarded op carries its `updated_at` or `expected`. A delete, or any op the
   tool says cannot be undone, stays only if the person asked for it: dropped work is closed, not
   deleted (`wiki/reading-history/non-standard-departure.md`, Abandoned work). Anything failing
   these: say which ops, and write nothing until the person decides. Show a short summary (counts
   per op, the file path), plus each `[board.notes]` entry for a command used, so a side effect is
   not a surprise. Put each op with `decide` to the person by its question, with its `why`; drop
   from the file every one they decline, before any write.
2. **`batch = "native"`:** translate the file into the tool's batch input as its help describes,
   run `{cmd:preview}` on it, and show its output verbatim, not retold. Where the batch input takes
   no `updated_at` guard, first read each guarded task with `{cmd:view}` and drop, saying so, every
   op whose task changed since. An error or unsupported op in the preview: stop. Otherwise run
   `{cmd:apply}`; its prompt is the person's approval.
3. **`batch = "sequential"`:** order the ops: creates, parents before children; then edits,
   labels, type, priority, comments; then links; then moves and closes. Run one recorded command
   per op, each under its own prompt. After each success write its id or result into `done` in the
   file at once, so a rerun skips it. Before an edit, close or label op, read the task with
   `{cmd:view}`; an `updated_at` later than the op's means someone changed it since: refuse that op.
4. **Stop on the first failure.** Record the exit code and stderr in the op, write nothing more,
   and report three lists: applied (with ids), failed (with the tool's message verbatim), not
   attempted. A `partial` or `unsupported` exit (`[board.exit_codes]`), or any failed write where
   the codes are unknown, is never retried: the write may have landed. A failed create stays failed
   until a read shows the task absent and the person confirms. Name tasks a failed link left unlinked.
   *Wrong if:* a rerun creates a task the file already shows `done`, or one marked `partial`.

## From decompose

`decompose` returns a tree as text; write it into a changeset before applying. A group node is a
`create`; a leaf a `create_child` with `parent` its node's ref (a leaf with no node, a `create`); a
placeholder a `create` whose text says it is one. The leaf's five headings, verbatim, are its
`body_file`. A `sequence` edge is a `link` of `[links].blocks` from the prerequisite to the leaf; a
`wait` edge stays in the text only, since what it waits for is off the board. `Size` is the estimate
by `[fields].estimate`: `add_label` for a `label:` form, its own recorded command for a `field:`
form; neither, the size is reported as not applied. decompose's questions are put to the person
before the apply, not written as ops.

## Moves

A move inside a changeset, and the single-task move below, check the expected state:

- **`guarded_move = "native"`:** `{cmd:move}` carries `{expected}`; the tool refuses on mismatch.
- **`guarded_move = "read-then-move"`:** `{cmd:view}`, refuse on a status other than the expected
  one, then `{cmd:move}`; say another step can land between the two.

The target status is the name in `[states]` mapped to the target kind; where several map to it,
the one the process document names, else ask. **A single-task move is not run through this
skill**: the working agent runs `{cmd:move}` itself at the step that caused it, with the guard
above (the design's "Перевод состояния стоит один вызов"). Asked how a move looks: the filled-in
command, and that it runs unprompted only when `guarded_move` is native and the person allowed it.

## The reply

Every board skill answers the person in this order. **Caveats:** each fallback taken and its cost
(`[board.capabilities]`), a tool version mismatch, a snapshot not atomic, a scope not complete
(`scope_reason`), the age basis, the lines *Reads and the snapshot* produced, any non-empty
`timestamp_problems` or `naive_timestamps`, and the envelope's `assumptions` and `not_covered`.
**Findings**, per dimension or item, each with its page. **Questions**: the envelope's
`questions`, for the person to answer. **The changeset**: its path, its ops by `op`, and that
`board` applies it, each close the person's decision. **What you need to do**: `needs_caller`.
