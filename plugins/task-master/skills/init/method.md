# init: method

Bring the project's workflow config file and its board to what `settings.md` describes, adding
only what is missing, every value confirmed by the person. "This method's own rule" marks a step no
page of the base stands behind.

## A rerun

A skill reported an unmapped status, an undeclared marker label or a missing `[process]` key, or
the person says the board changed. Redo only the steps the change touches (an unmapped status is
step 4 alone), and show the difference before writing it. Values already in the file are not asked
again (this method's own rule: a rerun that re-asks everything gets answered carelessly).

## Steps

1. **Find the workflow config file.** As `settings.md` says: the file the agent instructions name,
   else `workflow.toml` at the root. None: propose creating `workflow.toml` at the root; only if the
   person declines, `.claude/task-master.toml` with the same sections. Either way, propose one line
   in the agent instructions naming the file as the workflow config file.
   *Wrong if:* a second settings file is created beside an existing one.

2. **The board.** `[board]` present: its values stand and are not asked again; run the tool's own
   check, if its help names one, and go on.
   Absent: find the tool (the agent instructions, the tools on the path, the MCP servers configured)
   and the board, show both and where they were found, and let the person confirm; ids look alike
   across boards, and the error shows up as work on the wrong one. Then use the tool's own command
   that declares a board in this file, if its help names one, and check afterwards that it kept
   the rest of the file; otherwise write `[board]` as the tool's help describes it. Nothing found and the person names nothing: say the board skills will
   do only what needs no board, and stop after step 6.

3. **Read the board as it is.** Read the tool's help (as `skills/board/method.md`, Before any job),
   then its statuses, labels and the list of the whole board into `.task-master/`. Write nothing
   to the board yet. A failure, or a sign of truncation, goes to the person before going on. Until
   the rules of step 10 are in, each board command prompts, and so does every write to the
   settings file: that is intended.

4. **Statuses.** Each status needs a kind (`settings.md`, How a task's kind is decided). Write
   the settings drafted so far to `.task-master/settings-draft.toml` (on a first run, `[board]` and
   whatever the file already holds), run `snapshot.py` on the reads of step 3 with that file
   (`--empty-ok` if the board has no tasks, said to the person), and take `unmapped_statuses`. For each status the
   tool gives no category, propose one in the tool's own status table where the file has one,
   else an entry in `[process.kinds]`; the person confirms. A status the team will add (a review
   column the board lacks) is declared the same way, with category `in_progress`. Then ask which statuses hold work
   handed off rather than being done: `review_statuses`. Read the started and finished points first,
   since every count hangs from them (`wiki/work-states/started-and-finished-points.md`).
   - A status that is a condition, not a stage (Blocked, On Hold) is a marker: declare it as
     `status:<name>` in `[process.markers]` and say once that it fails the column test
     (`wiki/work-states/column-versus-attribute.md`). It still needs a kind; say which one
     miscounts least.
   - A status covering two kinds is said so, never mapped to the nearer one (the design's
     "Значение состояний принадлежит плагину"): the person splits it on the board, or picks one kind
     knowing what it miscounts.
   - A ready column counts as started only if it is WIP-limited: then propose it as `queued` in
     `[process.kinds]` with its limit in `[process.wip]`; an unlimited one is a backlog under
     another name, left as it is (`wiki/work-states/started-and-finished-points.md`, The decision).
   *Wrong if:* a status got a kind without the person's word.

5. **Labels and sizes.** The markers `blocked`, `waiting`, `untriaged`
   (`wiki/work-states/waiting-versus-blocked.md`, The test; `wiki/intake/triage-procedure.md`,
   step 1): reuse an existing label of that meaning, else propose the default name; each goes into
   `[board.labels]` with a one-line meaning, since a list of names alone breeds a second label for
   the same thing (the design's "Объявление несёт значение"). Then whether the team estimates: if
   so, `[board.size]`, one label per step with its number, and the same labels in `[board.labels]`
   with what each step means, fixed before estimating (`wiki/sizing/estimation-scale.md`).

6. **`[process]`.** Find the process document (agent instructions, the docs folder, contributor
   guides) and take what it states, citing where; never create or edit it, and where the person
   contradicts it, say so and propose the edit. Ask only `setup`, plus `period_days` under
   iterations and `[process.wip]` under flow. Every other key is written only when the document
   states it or the person brings it up; otherwise it stays absent, and the report lists the
   defaults in one line. What each key means:
   - `setup`: a fixed period, a bound on started work, or both; neither is no setup the base
     supports (`wiki/moving-work/board-rules-by-setup.md`). Under iterations, check the board can
     list its iterations; where it cannot, say every period-based skill will need them from the
     caller, and let the person choose.
   - `period_days` under iterations: a month or less, held, not fitted to the work
     (`wiki/periods/period-length.md`); `commitment`: the goal or the selected tasks
     (`wiki/periods/commitment-over-a-period.md`).
   - `[process.wip]`: only numbers the team states; never invent one
     (`wiki/moving-work/wip-control.md`). Under flow, ask for them.
   - `sle`: a time and a probability, or absent (`wiki/periods/service-level-expectation.md`).
   - `ceiling`: a `[board.size]` step (`wiki/sizing/size-ceiling.md`).
   - `review_statuses`: asked in step 4.
   - `doc`: the process document found, if any.
   - `executor`, `timezone`, `acceptance_headings` (search the raw list for the headings task
     bodies use).
   Velocity and throughput are never asked: the scripts compute them from history.
   *Wrong if:* a value was written without the person's word. An absent key is not a value.

7. **Write.** Show every addition to the file in full (on a rerun, the difference), and write after
   the person confirms. Add `.task-master/` to `.gitignore` if absent.

8. **Bring the board to the file.** init does this itself; a changeset has no op for it. Create
   each label of `[board.labels]` and `[board.size]`, and each status the person added, that the
   board lacks, with the tool's commands, one prompt each. Only add: never
   rename or delete, which the person does. What the tool cannot do (statuses that need an
   administrator, say) goes to the person as steps to take by hand.

9. **Check.** Read again as in step 3 and run `snapshot.py`: no unmapped status, no undeclared
   marker. What remains goes to the person.

10. **Propose permission rules** for `.claude/settings.json`, as a fragment the person edits in:
    allow each read the skills run by its fixed prefix; leave every write to a prompt; allow a move
    only if the tool guards it, because a move allowed in advance must refuse on the wrong state
    (the design's "Перевод состояния стоит один вызов"). Never allow a read whose arguments reach
    beyond reading, such as an expression evaluator or a pass-through to the raw API. If the tool
    accepts flags before the subcommand, say that ask or deny rules can be passed around and only
    the prompt on writes protects the board.
