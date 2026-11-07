# `.claude/task-master.toml`

The plugin's own file in a project. `init` writes it; every board skill reads it first. It records what
the plugin cannot learn by looking at the board each time. Process rules stay in the team's process
document; this file only says where that document is.

```toml
version = 1                      # format of this file

[project]
process_doc = "docs/process.md"  # the team's process document; absent: none found, and say so
setup = "iterations"             # iterations | flow
wip_control = true               # a stated bound on started work; its numbers, if process_doc has them, in [limits]
executor = "agent"               # who does the work: agent | people | mixed
timezone = "+03:00"              # day boundaries for dates: a UTC offset, "UTC" or an IANA name; absent: UTC
started_kinds = ["active", "handed_off"]  # kinds past the started point: what counts as WIP
commitment = "goal"              # iterations only: goal | selection; absent: not stated, asked per review
period_days = 14                 # iterations only
sle = "9 days at 85%"            # flow, or iterations that keep one; absent: none
scale = [1, 2, 3, 5, 8]          # absent: the project keeps no estimates
scale_far = [13, 20, 40, 100]    # coarse steps for work not yet near
ceiling = 8                      # the size above which a task is cut

[scale.meaning]                  # what each step means, one short line each
1 = "a change a reviewer reads in minutes"

[board]
tool = "the command or server name the project uses"
access = "adapter"               # adapter | tracker-cli | mcp | none
tool_version = "0.1.0"           # as found at init; checked on every run
found_from = "workflow.toml"     # where init learned it: a config file, CLAUDE.md, the environment

# How each obligation is met: "native" when the tool does it, otherwise the fallback named in the
# design's table "Чего инструмент не умеет". A skill reads this and never probes again.
[board.capabilities]
snapshot = "composed"            # native | composed
history = "native"               # native: the list carries status_since, started_at, finished_at,
                                 # transitions, or a `history` command returns them per task | none
guarded_move = "read-then-move"  # native | read-then-move
batch = "sequential"             # native | sequential
sprints = "native"               # native | caller

# The exact commands, with {placeholders}. Written by init from the tool's own help, so the skills
# carry no tool's syntax. Every list returns the whole scope, never the tool's default page.
[board.commands]
version = "<tool> version --json"
list = "<tool> issue list --category all --limit all --json"
list_sprint = "<tool> issue list --category all --limit all --sprint {sprint} --json"
list_parent = "<tool> issue list --category all --limit all --parent {id} --json"
list_label = "<tool> issue list --category all --limit all --label {label} --json"   # optional
view = "<tool> issue view {id} --comments --json"
statuses = "<tool> status list --json"
sprints = "<tool> sprint list --json"
labels = "<tool> label list --json"
move = "<tool> issue move {id} {status} --json"
create = "<tool> issue create --title {title} --body-file {body_file} --json"
create_child = "<tool> issue create --title {title} --body-file {body_file} --parent {parent} --json"
edit = "<tool> issue edit {id} --body-file {body_file} --json"
add_label = "<tool> issue edit {id} --add-label {label} --json"
remove_label = "<tool> issue edit {id} --remove-label {label} --json"
set_type = "<tool> issue edit {id} --type {type} --json"
set_priority = "<tool> issue edit {id} --priority {priority} --json"
link = "<tool> issue link add {id} {other} --type {type} --json"
comment = "<tool> issue comment add {id} --body-file {body_file} --json"
close = "<tool> issue close {id} --reason {reason} --json"
assign = "<tool> issue edit {id} --assignee {assignee} --json"   # optional; without it no assignment is proposed
history = "<tool> issue history {id} --json"   # returns {status_since, started_at, finished_at, transitions}
reads = ["version", "list", "list_sprint", "list_parent", "list_label", "view", "statuses", "sprints",
         "labels", "history"]
# Only where the capability above is native: snapshot = "... {scope} ... {out}",
# preview = "... {file}", apply = "... {file}"; and move then carries {expected}.

[board.exit_codes]               # from the tool's help; absent: unknown, and every failed write is
partial = 6                      # treated as possibly partial. partial: wrote, then failed; never retried
unsupported = 3                  # the board cannot do it; not retried

[board.notes]                    # what the help says a command also does, keyed by command
link = "type duplicates also closes {other} on some boards"
list = "the reply's `total` is the count the query matches"   # where the read reports its total

[board.close_reasons]            # the tool's value for each reason the plugin closes with; absent: none
duplicate = "duplicate"
abandoned = "canceled"

[board.categories]               # optional: the tool's status category -> unstarted | started | finished
todo = "unstarted"
in_progress = "started"
done = "finished"

# The tool's link type for each relation the plugin reads or proposes. Absent: that relation is
# neither read nor proposed, and the dimension that needs it reports it not covered.
[links]
duplicates = "duplicates"
duplicated_by = "duplicated-by"
blocks = "blocks"
blocked_by = "blocked-by"
relates = "relates"

# Board status name → the plugin's kind. Kinds come from
# wiki/work-states/distinguishable-work-states.md: before_start, queued, active, handed_off, finished.
# A status missing here is reported on the first read, never guessed.
[states]
"Backlog" = "before_start"
"Ready" = "queued"
"In Progress" = "active"
"In Review" = "handed_off"
"Done" = "finished"
"Canceled" = "finished"          # with the abandoned marker below

# Markers sit on tasks, not columns: how this board shows each. Absent: the board cannot show it.
[markers]
blocked = "label:blocked"
waiting = "label:waiting"
untriaged = "label:needs-triage"
abandoned = "status:Canceled"

# Where the board keeps these per task: "field:<name>" or "label:<prefix>{value}". Absent: nowhere.
[fields]
estimate = "label:size-{value}"
type = "field:type"
priority = "field:priority"
theme = "label:theme-{value}"     # optional: what groups tasks into themes, for a parking-lot chart

[labels.meaning]                 # each label the plugin may set, with what it means
"needs-triage" = "nobody has read this yet"

# Optional. The numbers behind wip_control, where process_doc states them: the most issues allowed
# at once, keyed by a board status or a kind (a key that is a kind name is read as the kind). A
# status key counts every issue in it, whatever its kind. Present implies wip_control = true.
# scripts/board_metrics.py reports each count above its limit. Absent: no numbers, none invented.
[limits]
"In Progress" = 3
handed_off = 4

[checks]
acceptance_headings = ["Acceptance criteria"]  # headings that mark acceptance criteria; the default
```

`started_kinds` places the started point (`wiki/work-states/started-and-finished-points.md`, The
decision): `queued` belongs in it only where the board's queued status is a WIP-limited arrivals
column or a queue between working stages. `scripts/board_metrics.py` reads it for every WIP count,
cycle time and Work Item Age; absent, it is `["active", "handed_off"]`, and a skill treats absence
the same way.

The scripts read a marker given as `label:<name>` or `status:<name>`; any other form stays `null` in
the snapshot and is listed in its `markers_unreadable`. An op takes the name without the prefix:
`add_label` of `blocked` for `label:blocked`. A `status:` marker is a column, never set by a proposed
move: a skill asks instead.

The `<tool>` and command shapes above are an example of one adapter; `init` writes whatever the
project's tool takes. A command the tool lacks is left out, and the capability row says how its
absence is covered. Under `access = "mcp"` an entry names the server's tool and its arguments as JSON
with the same placeholders. Text such as a task body always goes through `{body_file}`, never an
argument. Moves, types and links go only through the adapter where the project has one; another
operation the adapter lacks may be recorded from the tracker's own CLI or MCP.

A changeset's `op` is a key of `[board.commands]` (`skills/board/method.md`, Applying a changeset).
A value in `[fields]` given as `label:` is set with `add_label`; one given as `field:` needs an entry
of its own, such as `set_estimate = "... {id} {value}"`, and without one it cannot be proposed.
