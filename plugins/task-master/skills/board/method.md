# board: method

Everything here is this method's own procedure for the design's "Доступ к доске" and "Запись",
unless a page is named. `{cmd:<name>}` below means the entry `<name>` of `[board.commands]`.

## Before any job

1. **Read `.claude/task-master.toml`.** Absent, or `access = "none"`: the board is not set up.
   Say so, point to `init`, and stop; what needs no board goes on in the caller's skill.
2. **Check the tool version.** Run `{cmd:version}` and compare with `tool_version`. Different: name
   both. Reads go on with that said; before a write, ask whether to go on or rerun `init`, because
   the recorded commands and capabilities may no longer hold.
   *Wrong if:* a write ran on a changed version without the person's word.

## Reads and the snapshot

A single read (one task, the statuses) is its command, run once, its output returned. A view of a
task in a status not in `[states]` names that status.

A **snapshot** of a scope, taken for another skill, goes to `.task-master/snapshot-<scope>.json`.
The scope picks the list: the whole board `{cmd:list}`, a sprint `{cmd:list_sprint}`, a parent's
children `{cmd:list_parent}`. A scope with no recorded command: say so and offer the whole board.

- **`snapshot = "native"`:** run `{cmd:snapshot}` into `.task-master/raw-<scope>.json`, then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --native <raw> --config .claude/task-master.toml --out <snapshot>`.
- **`snapshot = "composed"`:** note the time, then run the list into `.task-master/raw-<scope>-issues.json`,
  `{cmd:statuses}` into `raw-statuses.json`, and, where `sprints = "native"` and the setup has
  iterations, `{cmd:sprints}` into `raw-sprints.json`. Then
  `python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py --issues <..> --statuses <..> [--sprints <..>] --taken-at <time> --config .claude/task-master.toml --out <snapshot>`.
  Say the snapshot is not atomic: an edit between the reads lands in it partly.

Redirect each read's output into its file rather than reading it into the conversation: the point
of a snapshot is that the board does not pass through the caller's context. A read that warns it
returned less than the scope is not a snapshot: say so and stop.

Then search the snapshot (do not read it whole) for `unmapped_statuses`,
`mapping_unknown_statuses` and `issues_without_status`, and name every entry in the reply: a status
the mapping lacks is never guessed into a kind, and the fix is a rerun of `init` (the design's
"Состояние, которого нет в соответствии, названо при первом же чтении"). Also say:
`history = "none"`: ages count from creation and are named so; `sprints = "caller"`: the iterations
must come from the caller or the person.
*Output:* the snapshot path and those lines. *Wrong if:* the reply is silent on a non-empty list.

## Applying a changeset

The input is a changeset from another skill's result. Write it as
`.task-master/changeset-<slug>.json`:

```json
{"source": "decompose", "snapshot": ".task-master/snapshot-sprint-12.json", "ops": [
  {"ref": "n1", "op": "create", "title": "…", "body_file": ".task-master/body-n1.md", "done": null},
  {"ref": "n2", "op": "create_child", "parent": "n1", "title": "…", "body_file": "…", "done": null},
  {"ref": "l1", "op": "link", "id": "n2", "other": "n1", "type": "blocks", "done": null},
  {"ref": "m1", "op": "move", "id": "T-4", "status": "In Review", "expected": "In Progress", "done": null}]}
```

`op` is a `[board.commands]` key, the other keys fill its placeholders, and a value equal to a
`ref` stands for that op's created id. Task text goes into body files, never into an argument.
Edits to an existing task carry its `updated_at` from the snapshot.

1. **Check before the first write.** Every op has a recorded command; every ref resolves to an
   earlier op. A delete, or any op the tool says cannot be undone, stays only if the person asked
   for it: dropped work is closed, not deleted (`wiki/reading-history/non-standard-departure.md`,
   Abandoned work). Anything failing these: say which ops, and write nothing until the person
   decides. Show a short summary (counts per op, the file path), plus each `[board.notes]` entry
   for a command used, so a side effect is not a surprise.
2. **`batch = "native"`:** translate the file into the tool's batch input as its help describes,
   run `{cmd:preview}` on it, and show its output verbatim, not retold. An error or unsupported op
   in the preview: stop. Otherwise run `{cmd:apply}`; its prompt is the person's approval.
3. **`batch = "sequential"`:** order the ops: creates, parents before children; then edits,
   labels, type, priority, comments; then links; then moves and closes. Run one recorded command
   per op, each under its own prompt. After each success write its id or result into `done` in the
   file at once, so a rerun skips it. Before an edit, read the task with `{cmd:view}`; an
   `updated_at` later than the snapshot's means someone changed it since: refuse that op. Say the
   cost: as many prompts as ops, and no refusing the set as a whole before the first write.
4. **Stop on the first failure.** Record the exit code and stderr in the op, write nothing more,
   and report three lists: applied (with ids), failed (with the tool's message verbatim), not
   attempted. An exit `[board.exit_codes]` calls `partial`, or any failed write where the codes are
   unknown, is never retried: the write may have landed. A failed create stays failed on a rerun
   until a read shows the task absent and the person confirms. An `unsupported` exit is not retried.
   Tasks created before a failed link sit unlinked until the rerun: say so.
   *Wrong if:* a rerun creates a task the file already shows `done`, or one marked `partial`.

## Moves

A move inside a changeset, and the single-task move below, check the expected state:

- **`guarded_move = "native"`:** `{cmd:move}` carries `{expected}`; the tool refuses on mismatch.
- **`guarded_move = "read-then-move"`:** run `{cmd:view}`, compare its status with the expected
  one, refuse on mismatch, then `{cmd:move}`. Say the window remains: another step can land
  between the read and the move.

The target status is the name in `[states]` mapped to the target kind; where several map to it,
the one the process document names, else ask. **A single-task move is not run through this
skill**: the working agent runs `{cmd:move}` itself at the step that caused it (the design's
"Перевод состояния стоит один вызов"), with the guard above. When asked how a move looks, answer
with the filled-in command, and whether it runs without a prompt: only when `guarded_move` is
native and the person allowed it.
