# The project's settings

task-master keeps no file of its own. It reads the project's workflow config file: the file the
project's agent instructions (`CLAUDE.md`, `AGENTS.md`) name for tool and workflow settings, else a
`workflow.toml` at the project root, else `.claude/task-master.toml`. A project with no such file
gets `workflow.toml` proposed by `init`; only if the person declines does `init` propose
`.claude/task-master.toml`, with the same sections. Every board skill finds the file the same way
and passes its path to the scripts as `--settings`.

## What is read

| Section | Owner | What task-master takes from it |
|---|---|---|
| `[board]` | the board tool | which board; its own keys are left to the tool |
| `[board.labels]` | the project | `"<label>" = "<what it means>"`, one line each |
| `[board.size]` | the project | `"<label>" = <number>`, numbers only |
| `[process]` | task-master | how the team works; below |

`[board]`'s own keys and tables belong to the board tool and follow its format; task-master reads
them and never adds keys of its own there. `[board.labels]` and `[board.size]` are the project's,
and `init` writes them; every `[board.size]` label is also in `[board.labels]`, with its meaning. A
status's category (`todo`, `in_progress`, `done`, `canceled`) comes with each task from the
tool; where the tool keeps its own status table in the file (such as `[board.statuses]`), that
table is where a status gets its category. Status names are spelled as the tool returns them.

The tool is the board command the agent instructions name. A command in `[board]` may be the
tracker's own CLI the tool runs underneath; where the two differ and the instructions do not say
which to use, ask.

## `[process]`

```toml
[process]
setup = "iterations"            # iterations | flow; the one required key
period_days = 14                # iterations
sle = "5 days at 85%"           # optional: the team's declared SLE, a time and a probability
review_statuses = ["Review"]    # optional: statuses where work is handed off, not being done
ceiling = "L"                   # optional: the largest [board.size] step one task may carry
doc = "docs/process.md"         # optional: the team's process document
commitment = "goal"             # optional, iterations: goal | selection
executor = "agent"              # optional: agent | people | mixed
timezone = "+03:00"             # optional: where the team's days begin; absent: UTC
acceptance_headings = ["Acceptance criteria"]   # optional; this is the default

[process.wip]                   # optional: WIP limits by status, or by kind; absent: none stated
"In Progress" = 3

[process.markers]               # optional; these values are the defaults
blocked = "blocked"
waiting = "needs-info"
untriaged = "needs-triage"
# abandoned = "status:Dropped"  # optional; a canceled category is abandoned anyway

[process.kinds]                 # optional: status → kind, where the tool gives no category or to
                                # declare queued over a category
"Ready" = "queued"
```

Under `flow`, `period_days` and `commitment` do not apply, and `[process.wip]` is expected: a flow
setup with no stated bound on started work is one the base cannot check
(`wiki/moving-work/board-rules-by-setup.md`).

The declared `sle` is a team agreement, revised rarely. The scripts compute the observed
percentile on every run; a skill that finds it far from the declared one says so and proposes a
revision, which the person makes.

The snapshot script runs without `[process]`, as `init` needs before the section exists; the
metrics script needs `[process]` with `setup`. Where `[process]` is present, an unknown key or
value stops the scripts with its name: a misspelling never falls back to a default.

## How a task's kind is decided

The scripts decide it, so two runs never disagree:

1. a status in `[process.kinds]`: that kind;
2. a status in `review_statuses`: `handed_off`;
3. otherwise by category: `todo` → `before_start`, `in_progress` → `active`, `done` and
   `canceled` → `finished`;
4. no category and no entry: unmapped, named on the first read, never guessed.

A `canceled` task is `finished` with the `abandoned` marker. `queued` comes only from
`[process.kinds]`; a ready column the team limits is declared there, and counted as started only
if `[process.wip]` names it.

## Markers and estimates

`blocked`, `waiting` and `untriaged` are labels: the names in `[process.markers]`, else
`blocked`, `needs-info` and `needs-triage`. A value `status:<name>` declares a column instead of a
label. A marker whose label is missing from `[board.labels]` is reported: the board cannot show it.

A task's estimate is its label that is a key of `[board.size]`, read as that key's number. No
`[board.size]`: the project keeps no estimates. Two size labels on one task: unreadable, named.

## Commands

No commands are recorded. A skill reads the board tool's `--help` (and the help of each
subcommand it will run) before the first board command of a run, and uses only what the help
documents. Where the tool reports its capabilities as a command, that is read instead of guessing.
