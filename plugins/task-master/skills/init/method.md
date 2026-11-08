# init: method

The steps that bring the project's workflow config file and its board to what `settings.md`
describes. Each step adds only what is missing; the person confirms every value.

## A rerun

A skill reported an unmapped status, an undeclared marker label or a missing `[process]` key, or
the person says the board changed. Redo only the steps the change touches (an unmapped status is
step 4 alone) and show the difference before writing it. Do not ask again for values already in
the file: a rerun that re-asks everything gets answered carelessly.

## Steps

1. **Find the workflow config file** as `settings.md` says: the file the agent instructions name,
   else `workflow.toml` at the root. None: propose creating `workflow.toml` at the root; only if the
   person declines, `.claude/task-master.toml` with the same sections. Either way, propose one line
   in the agent instructions naming the file as the workflow config file.

2. **The board.**
   - `[board]` present: its values stand. Run the tool's own check if its help names one, and go on.
   - Absent: find the tool (the agent instructions, the tools on the path, the configured MCP
     servers) and the board, show both and where they were found, and let the person confirm; ids
     look alike across boards. Then declare the board with the tool's own command where its help
     names one, and check afterwards that it kept the rest of the file; otherwise write `[board]` as
     the help describes it.
   - Nothing found and the person names nothing: say the board skills will do only what needs no
     board, and stop after step 6.

3. **Read the board as it is.** Learn the tool as `skills/board/method.md`, *Before any job*, says,
   then read its statuses, labels and the list of the whole board into `.task-master/`. Write
   nothing to the board yet. A failure, or a sign of truncation, goes to the person before going on.
   Until the rules of step 10 are in, each board command and each write to the settings file
   prompts; that is intended.

4. **Statuses.** Read `wiki/work-states/started-and-finished-points.md` first: every count hangs
   from those two points. Write the settings drafted so far to `.task-master/settings-draft.toml`
   (on a first run, `[board]` and whatever the file already holds) and run `snapshot.py` on the
   reads of step 3 with it (`--empty-ok` if the board has no tasks, said to the person). Take
   `unmapped_statuses`.
   - **Each status needs a kind** (`settings.md`, *How a task's kind is decided*). For a status the
     tool gives no category, propose one in the tool's own status table where the file has one,
     else an entry in `[process.kinds]`. A status the team will add (a review column the board
     lacks) is declared the same way, with category `in_progress`.
   - **Handed off:** ask which statuses hold work handed off rather than being done:
     `review_statuses`.
   - **A condition, not a stage** (Blocked, On Hold) is a marker: declare it as `status:<name>` in
     `[process.markers]` and say once that it fails the column test
     (`wiki/work-states/column-versus-attribute.md`). It still needs a kind; say which one
     miscounts least.
   - **A status covering two kinds** is said so, never mapped to the nearer one
     (`wiki/work-states/distinguishable-work-states.md`, criterion 3): the person splits it on the
     board, or picks one kind knowing what it miscounts.
   - **A ready column** counts as started only if it is WIP-limited: then propose it as `queued` in
     `[process.kinds]` with its limit in `[process.wip]`. An unlimited one is a backlog under
     another name, left as it is (`wiki/work-states/started-and-finished-points.md`, The decision).

5. **Labels and sizes.**
   - **Markers** `blocked`, `waiting`, `untriaged` (`wiki/work-states/waiting-versus-blocked.md`,
     The test; `wiki/intake/triage-procedure.md`, step 1): reuse an existing label of that meaning,
     else propose the default name. A default name stays out of `[process.markers]`, since absent
     means the default. A marker step 4 declared as a status gets no label.
   - **Meanings:** each label goes into `[board.labels]` with a one-line meaning, since a list of
     names alone breeds a second label for the same thing.
   - **Sizes:** ask whether the team estimates. If so, `[board.size]`, one label per step with its
     number, and the same labels in `[board.labels]` with what each step means, fixed before
     estimating (`wiki/sizing/estimation-scale.md`). Draft each meaning from that page and show
     them for the person to confirm or edit.

6. **`[process]`.** Find the process document (agent instructions, the docs folder, contributor
   guides) and take what it states, citing where. Never create or edit it; where the person
   contradicts it, say so and propose the edit. Where the document is silent, ask only `setup`,
   `executor` (agent, people or mixed: tend-board's dimensions branch on it), `period_days` under
   iterations and `[process.wip]` under flow. Write any other key only when the document states it
   or the person brings it up; the report lists the defaults left in place in one line. Read the
   page behind each key before proposing a value:
   - `setup`: a fixed period, a bound on started work, or both; neither is no setup the base
     supports (`wiki/moving-work/board-rules-by-setup.md`). Under iterations, check the board can
     list its iterations; where it cannot, name the choices: enable them as the tool's help says,
     give the sprints on each run, or switch setup to flow.
   - `period_days`: a month or less, held, not fitted to the work (`wiki/periods/period-length.md`).
   - `commitment`: the goal or the selected tasks (`wiki/periods/commitment-over-a-period.md`).
   - `[process.wip]`: only numbers the team states; never invent one
     (`wiki/moving-work/wip-control.md`).
   - `sle`: a time and a probability, or absent (`wiki/periods/service-level-expectation.md`).
   - `ceiling`: a `[board.size]` step (`wiki/sizing/size-ceiling.md`).
   - `doc`: the process document found, if any.
   - `timezone`; `acceptance_headings` (search the raw list for the headings task bodies use).

   Never ask for velocity or throughput: the scripts compute them from history. An absent key is
   not a value; nothing is written without the person's word.

7. **Write.** Show every addition to the file in full (on a rerun, the difference) and write after
   the person confirms. Add `.task-master/` to `.gitignore` if absent.

8. **Bring the board to the file.** init does this itself; a changeset has no op for it. Create
   each label of `[board.labels]` and `[board.size]`, and each status the person added, that the
   board lacks, with the tool's commands, each shown by its dry run where the tool has one, one
   prompt each. An add-only bulk command the help documents (a sync that creates declared labels
   and never deletes) may replace them, previewed before it runs. Where the help says labels come
   into existence on first use, report that and create none. Never rename or delete; the person
   does that. What the tool cannot do (statuses that need an administrator) goes to the person as
   steps to take by hand.

9. **Check.** Read again as in step 3 and run `snapshot.py`: no unmapped status, no undeclared
   marker. What remains goes to the person.

10. **Propose permission rules** for `.claude/settings.json`, as a fragment the person edits in.
    - Allow each read the skills run by its exact prefix, up to its first variable argument, and
      say what may follow it, since a prefix rule admits whatever does.
    - Leave every write to a prompt. Allow a move in advance only if the tool guards it with the
      expected status, because a move that runs unprompted must refuse on the wrong state.
    - The risk: a read whose arguments reach beyond reading (an expression evaluator, a
      pass-through to the raw API). Where the help shows a global flag that evaluates expressions
      (a jq-like filter), or the tool accepts flags before the subcommand, any prefix admits one,
      and flags before the subcommand get around ask or deny rules.
    - Tell the person: never propose such a rule unsaid; name what it admits, and say that only
      the prompt on writes then protects the board.
