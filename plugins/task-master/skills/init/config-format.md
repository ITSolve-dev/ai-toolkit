# `.claude/task-master.toml`

The plugin's own file in a project. `init` writes it; every board skill reads it first. It records what
the plugin cannot learn by looking at the board each time. Process rules stay in the team's process
document; this file only says where that document is.

```toml
version = 1                      # format of this file

[project]
process_doc = "docs/process.md"  # the team's process document; absent: none found, and say so
setup = "iterations"             # iterations | flow
wip_control = false              # a stated bound on started work; the bound itself is in process_doc
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
history = "none"                 # native | none
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
reads = ["version", "list", "list_sprint", "list_parent", "view", "statuses", "sprints", "labels"]
# Only where the capability above is native: snapshot = "... {scope} ... {out}", history = "... {id} ...",
# preview = "... {file}", apply = "... {file}"; and move then carries {expected}.

[board.exit_codes]               # from the tool's help; absent: unknown, and every failed write is
partial = 6                      # treated as possibly partial. partial: wrote, then failed; never retried
unsupported = 3                  # the board cannot do it; not retried

[board.notes]                    # what the help says a command also does, keyed by command
link = "type duplicates also closes {other} on some boards"

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

[labels.meaning]                 # each label the plugin may set, with what it means
"needs-triage" = "nobody has read this yet"

# Optional. The numbers behind wip_control, where process_doc states them: the most issues allowed
# at once, keyed by a board status or a kind (a key that is a kind name is read as the kind).
# scripts/board_metrics.py reports each count above its limit. Absent: no limits, none invented.
[limits]
"In Progress" = 3
handed_off = 4

[checks]
acceptance_headings = ["Acceptance criteria"]  # headings that mark acceptance criteria; the default
```

The scripts read a marker given as `label:<name>` or `status:<name>`; any other form stays `null` in
the snapshot, because the board reads it is built from do not carry it.

The `<tool>` and command shapes above are an example of one adapter; `init` writes whatever the
project's tool takes. A command the tool lacks is left out, and the capability row says how its
absence is covered. Under `access = "mcp"` an entry names the server's tool and its arguments as JSON
with the same placeholders. Text such as a task body always goes through `{body_file}`, never an
argument. Moves, types and links go only through the adapter where the project has one; another
operation the adapter lacks may be recorded from the tracker's own CLI or MCP.
