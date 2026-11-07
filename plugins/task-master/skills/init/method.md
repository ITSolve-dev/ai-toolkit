# init: method

Produce `.claude/task-master.toml` as `config-format.md` specifies it, with every field confirmed by
the person or marked absent. "This method's own rule" marks a step no page of the base stands behind.

## A rerun

If the file exists, this is a rerun: a skill reported an unmapped status or a changed tool version,
or the person says the board or tool changed. Redo only the steps the change touches (a new status
is step 5 alone; a new tool version is steps 2-4 and 9), build the new file in
`.task-master/task-master.toml.new`, and show the difference field by field before writing it.
Unchanged fields are not asked again (this method's own rule: a rerun that re-asks everything gets
answered carelessly). *Wrong if:* the file is overwritten before the person saw the difference.

## Steps

1. **Find how the project reaches its board.** Look, in this order: the project's configuration
   (a declaration file of a board tool, a workflow or tool config, environment variables it names),
   `CLAUDE.md` and similar agent instructions, the tools installed on the path, and the MCP servers
   configured for the project. Prefer a board adapter; then the tracker's own CLI; then an MCP server
   (the design's ladder). Show the person what you found and where; they confirm the tool and the
   board. Nothing found and the person names nothing: `access = "none"`, skip to step 7, and say the
   board skills will do only what needs no board.
   *Output:* `[board]` `tool`, `access`, `found_from`. *Wrong if:* a board was picked because its
   id looked familiar; ids look alike across boards, and the error shows up as work on the wrong one.

2. **Read the tool's help and record the commands.** Read the help of the tool and of every
   subcommand an entry in `[board.commands]` would use; record the tool's version. Each entry is the
   exact command with placeholders. Rules for each (this method's own, from what the skills need):
   - a list returns the whole scope, every status and no page limit; a tool's default page silently
     truncates a snapshot;
   - flags come after the subcommand, so a permission rule on the command's prefix matches it;
   - text goes through a file placeholder, never an argument;
   - an operation the adapter lacks may come from the tracker's CLI or MCP, except moves, types and
     links, which stay with the adapter where there is one (the design's "Запись").
   Also record the exit codes the help documents, especially a partial write and an unsupported
   operation, and, in `[board.notes]`, anything a command does besides what it is named for (a link
   that closes a task, a move that closes it). Note how a task with no status comes back: if the tool
   fills one in, say so in `[board.notes]`, because the snapshot cannot name what the tool hid.
   Never run a command to see what it does, and never ask for the help of one that changes the tool
   itself: if it ignored the help flag it would run.
   *Wrong if:* an entry was written from memory of a tool rather than from its help.

3. **Decide each capability.** `native` only when a recorded command delivers it as the help
   documents; otherwise the fallback from the design's table, and tell the person its cost:
   snapshot composed from reads, not atomic; no history, so age counts from creation and the analyses
   that need history are unavailable; read-then-move leaves a window between the read and the move,
   and the move is not allowed in advance; sequential batch asks once per operation and cannot be
   refused as a whole before the first write; sprints from the caller.
   *Output:* `[board.capabilities]`. *Wrong if:* a row says `native` for a command that exists but
   lacks the obligation, such as a move with no expected-state check.

4. **Check the reads work.** Run `version`, `statuses`, and `list` once. A failure, a sign of
   truncation, or a version different from the help's goes to the person before going on. Write
   nothing to the board. *Wrong if:* a read command is recorded that was never run.

5. **Map every status to a kind** with the person (`wiki/work-states/distinguishable-work-states.md`,
   What the plugin can treat as canonical). Take statuses from the `statuses` read and from the
   tasks the `list` returned. For each, propose a kind with its reason; the person confirms. Read off
   the started and finished points first, because every count hangs from them
   (`wiki/work-states/started-and-finished-points.md`). Where history is readable, check proposals
   against recent tasks of different kinds (`wiki/work-states/mapping-workflow-states.md`).
   - A column that is a condition and not a stage (Blocked, On Hold) is a marker: record it in
     `[markers]` as `status:<name>`, ask which kind its tasks hold, and say once that it fails the
     column test (`wiki/work-states/column-versus-attribute.md`).
   - A status covering two kinds is said so, never mapped to the nearer one (the design's
     "Значение состояний принадлежит плагину": a silent approximation gives rules that fire wrongly
     and look as if they work). The person splits it on the
     board, picks one kind knowing what it miscounts (recorded with a comment), or leaves it unmapped,
     and then every read names it.
   - A status for dropped work is `finished` with the `abandoned` marker, so counts of finished work
     can filter it (`wiki/reading-history/non-standard-departure.md`, Abandoned work).
   - Then record the kinds past the started point, `started_kinds`: `active` and `handed_off`, plus
     `queued` where the queued status is a WIP-limited arrivals column or a queue between working
     stages. An unlimited first column is a backlog under another name: propose `before_start` for
     it (`wiki/work-states/started-and-finished-points.md`, The decision; Where the clock starts on
     such a board). A board with both kinds of queue cannot be told apart by kind: say so.
   *Output:* `[states]`, `[project].started_kinds`. *Wrong if:* a status is in `[states]` without
   the person's word, or `queued` is counted as started on a column with no limit.

6. **Markers, fields, labels.** Ask how the board shows each marker: `blocked` and `waiting`
   (`wiki/work-states/waiting-versus-blocked.md`, The test), `untriaged`
   (`wiki/intake/triage-procedure.md`, step 1), `abandoned`; absent means it cannot. Record a marker
   as `label:<name>` or `status:<name>` where the board allows: the scripts read no other form, and
   say so when it is another. Ask where the board keeps a task's estimate, type and priority, and
   which headings in a task's text mark its acceptance criteria (read a few tasks' text), and
   whether something groups tasks into themes (`[fields].theme`, optional: only the parking-lot
   chart reads it). Run
   `labels`, and give each label the plugin may set a one-line meaning, reusing an existing label of
   that meaning: a list of names alone breeds a second label for the same thing (the design's
   "Объявление несёт значение").
   *Output:* `[markers]`, `[fields]`, `[checks].acceptance_headings`, `[labels.meaning]`.

7. **Find the process document.** Look for it in agent instructions, the docs folder and contributor
   guides; show what you found; the person confirms, or names it, or says there is none. Read it and
   take what it states about setup, period, SLE, scale and limits as the defaults in step 8, citing
   where. Never create it (the design's "Правила процесса живут там, где их читают все").
   *Output:* `process_doc`, or absent with that said. *Wrong if:* a path was assumed.

8. **Ask the setup.** Where the process document already states a value, offer it; where the person
   contradicts it, the document is the team's truth: say so and propose the edit to it.
   - `setup` and `wip_control`: a fixed period, a stated bound on started work, or both; neither is
     no setup the base supports, so ask again (`wiki/moving-work/board-rules-by-setup.md`). The
     bound is a team agreement: copy into `[limits]` only the numbers the process document states,
     keyed by status or kind, and propose adding them there if it has none; never invent one
     (`wiki/moving-work/wip-control.md`).
   - `period_days` under iterations: one month or less, held, not fitted to the work
     (`wiki/periods/period-length.md`).
   - `commitment` under iterations: the goal or the selected tasks
     (`wiki/periods/commitment-over-a-period.md`, The decision); not stated: absent, and a review
     asks it per period.
   - `sle`: a time and a probability, or absent (`wiki/periods/service-level-expectation.md`).
   - `scale`, `scale_far` and a one-line meaning per step, fixed before estimating, one per project
     (`wiki/sizing/estimation-scale.md`); no estimates kept: absent.
   - `ceiling`: a step, chosen by setup (`wiki/sizing/size-ceiling.md`, Which figure applies under
     which setup); under flow with an SLE, the SLE question replaces it and the step is optional.
   *Wrong if:* a value was filled from a default without the person's word, and not marked absent.

9. **Propose permission rules.** For `.claude/settings.json`, as a fragment the person edits in:
   allow each recorded read by its fixed prefix; leave every write to a prompt; allow `move` only if
   `guarded_move = "native"`, because a move allowed in advance must refuse on the wrong state (the
   design's "Перевод состояния стоит один вызов"). Never allow a read whose arguments reach beyond
   reading, such as an expression evaluator or a pass-through to the raw API. If the tool accepts
   flags before the subcommand, say that ask or deny rules can be passed around and only the
   prompt on writes protects the board.

10. **Write.** Show the whole file (on a rerun, the difference), write it after the person confirms,
    and add `.task-master/` to `.gitignore` if absent.
