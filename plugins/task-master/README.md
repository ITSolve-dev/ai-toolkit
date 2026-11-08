# task-master

Board management and planning as an expert the working agent calls. The agent hands over a problem
and its context: a design doc to cut into tasks, a backlog to size, a sprint to review. The plugin
works in its own context, grounded in a curated knowledge base, and returns a result with the page
each judgement rests on. What to do with that result stays the caller's decision.

Status: 0.1.0, first release. Design:
[`docs/specs/2026-08-24-task-master-design.md`](../../docs/specs/2026-08-24-task-master-design.md).

## Install

```
/plugin marketplace add ITSolve-dev/ai-toolkit
/plugin install task-master@ai-toolkit
```

On Claude Code 2.1.275 or later this works in one step:

```
/plugin install task-master --marketplace ITSolve-dev/ai-toolkit
```

## Use it

```
/task-master:ask how do I tell whether a task is too big?
/task-master:decompose docs/specs/notifications.md
/task-master:init                          # once per project, before any board skill
/task-master:tend-board sprint:24
/task-master:board apply .task-master/changeset-tend-board-sprint-24.json
```

## Skills

| Skill           | For                                                                     | Board                        |
| --------------- | ----------------------------------------------------------------------- | ---------------------------- |
| `ask`           | Any question about organizing work on a board, answered with citations  | No                           |
| `decompose`     | A document or description into a tree of tasks an agent can each finish | No                           |
| `estimate`      | Relative sizes, what each rests on, which tasks to cut again            | No                           |
| `schedule`      | Order estimated tasks over periods; the date as a range                 | No                           |
| `init`          | Find the board tool, bring the workflow config and the board in line    | Finds it                     |
| `board`         | Read, snapshot, apply a changeset, show how a single move looks         | Yes                          |
| `tend-board`    | Check an area of the board, one dimension at a time                     | Yes                          |
| `triage`        | Read and sort incoming items, draft questions to reporters              | Yes, or items as text        |
| `review-period` | A past sprint or flow window against what was promised at its start    | Yes, or a snapshot passed in |
| `visualize`     | One question about the board, answered with one Mermaid chart           | Yes, or figures passed in    |

The four planning skills need no board because they work on what they are handed. A board skill
running on text or a passed-in snapshot says which checks that left out: on items given as text,
`triage` cannot look for duplicates already on the board.

## Agents

| Agent             | Tools                     | Input → output                                    |
| ----------------- | ------------------------- | ------------------------------------------------- |
| `guide`           | `Read, Grep, Glob`        | a question → an answer citing the pages it read   |
| `planner`         | `Read, Grep, Glob, Write` | work to organize → tasks, estimates, a layout     |
| `board-inspector` | `Read, Grep, Glob, Write` | a snapshot and one question → findings or a chart |

None of them can touch the board: none has `Bash` or an MCP tool, and the tool list is the boundary,
not the prompt. `Write` lets two of them leave their result in a file instead of passing it back
through your context. The skills that read the board run in your context, take a snapshot into a
file and fork the judging into an agent, which sees only that file. A command against the board
therefore always runs where you can see it.

## The board

The plugin names no board tool. A project may reach its board through an adapter, its tracker's own
CLI or an MCP server, and its own scripts use the same tool, so the plugin uses what the project
already has rather than carrying a tool of its own. The plugin keeps no file of its own: it reads the
project's workflow config file, the one `CLAUDE.md` or `AGENTS.md` names, else `workflow.toml` at
the root. `[board]` there belongs to the board tool, `[board.labels]` and `[board.size]` are the
project's labels and estimate scale, and `[process]` is how the team works, which the plugin owns.
`init` finds the tool, shows what it found for you to confirm, asks only for what is missing, and
brings the board to the file. Each board skill reads the tool's `--help` on every run and uses only
what it documents. A task's kind comes from its status's category on the board, or from
`[process.kinds]` where the tool gives none; a status with neither is named on the first read, not
guessed into a kind; the fix is a rerun of `init`. Full list: `skills/init/settings.md`.

### Where the tool falls short

Where the tool lacks a capability, the skill takes a named fallback and says in its reply what was
done differently and what it costs. No fallback fills a gap with something plausible: what neither
the tool nor a fallback can do, the skill does not do, and says so.

| Capability                          | Without it                                                                                    | Cost                                                                         |
| ----------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Snapshot of a scope                 | Composed from separate reads by the plugin's script                                           | Not atomic: an edit between reads lands in it partly                         |
| History and time in state           | Analysis that needs it is declared unavailable; age counts from creation and is labelled so   | A task stuck in a state looks the same as one long open                      |
| Move that checks the expected state | Read the task, refuse on mismatch, then move; never allowed in advance                         | Another step can land between the read and the move                          |
| Batch with preview                  | One write per operation, in order, each under its own prompt; ids written back after each, so a rerun skips what is done | As many prompts as operations; the set cannot be refused whole before the first write |
| Link to a task not yet created      | Create first, then link by the ids in the changeset file                                       | A failure between the two leaves tasks unlinked until the rerun              |
| List of iterations                  | The caller or the person names them                                                            | —                                                                            |
| Contract version                    | The tool's help is read on every run; only what it documents is used                           | A behaviour change the help does not show goes unnoticed                     |

### Permissions

`init` proposes rules for `.claude/settings.json` as a fragment you add yourself:

- every read the skills run is allowed by its fixed prefix;
- every write is left to a prompt;
- a single-task move is allowed in advance only where the tool itself checks the expected state,
  because a move nobody is asked about must refuse when the task has already moved on.

A read whose arguments reach beyond reading, such as a pass-through to the raw API, is never allowed.
Where the tool accepts flags before the subcommand, a rule on the command's prefix can be passed
around, and `init` says that only the prompt on writes then protects the board.

### Writes

What the plugin works out itself (tasks from `decompose`, closings from `triage`, fixes from
`tend-board`) comes back as a changeset file in `.task-master/`, with a short summary and the file's
path. Nothing reaches the board until `board` applies it. Where the tool previews a batch, `board`
shows that output verbatim and the apply command's prompt is your approval. On the sequential path,
each operation runs as its own command under its own prompt.

The prompt is what a model cannot answer for you. A subagent's reply reaches the leading agent, not
you, so a changeset approved by passing it along would be the model approving its own write. In
modes that skip permission prompts this protection is gone, and the plugin cannot replace it.

`.task-master/` lives for one run and is not a store: the board stays the only record. `init` adds it
to `.gitignore`.

## The base

180 pages in ten groups, distilled from sixteen sources: Cohn's *Agile Estimating and Planning*,
Vacanti's *Actionable Agile Metrics for Predictability*, Vacanti and Seele's *Flow Metrics for Scrum
Teams*, the 2020 Scrum Guide, the Kanban Guide, two Kanban Playbook articles, Wester on board design,
Radzikowska on waiting and blocked work, the Humanizing Work guide to splitting stories, Wake on
INVEST, Black Swan Farming on qualitative cost of delay, the Kubernetes issue triage guidelines,
Zimmermann et al. on bug reports, Montgomery et al. on tracker smells, and Ambig-SWE on
underspecified tasks.

Grouped by the question someone organizing work arrives with: how to cut this, what a task must
carry, what it costs, what comes first, what to do with what came in, what state this is, what may
move, what fits in a period, what actually happened, how to show it. Every rule page carries the sign
by which its violation shows in a task's text, the board's state or its history, so the same page
advises and audits.

**Its known weakness: about half the base rests on one book.** 94 of the 180 pages cite Cohn, 66 of
them cite nothing else, so estimation and planning carry one author's view more than any other topic
does. Reinertsen's *Principles of Product Development Flow* was considered and rejected, because the
file offered was a third-party summary, not the book; ordering by cost of delay rests on the
qualitative source instead.

Pages are not compressed. A pilot showed compression drops the words that say who claims something,
how sure, and where it applies, and on this base those words are the claim. `knowledge/SCHEMA.md`
holds the charter and the record of these decisions.

## What has been checked live

Run on four sandbox boards (GitLab Free, GitHub Projects, Linear, Jira Cloud), with the board
command line at 0.2.1 for the GitLab rerun: `init` on all four, `decompose` → `board` on all four,
`tend-board` on GitLab, GitHub and Jira. Not yet run on a live board: `triage`, `review-period`,
`visualize`, and `estimate`/`schedule` with board history; they use the same snapshot and
metrics path `tend-board` exercised. Also unchecked: permission rules built on
`${CLAUDE_PLUGIN_ROOT}` on Windows.

## Requires

- **Python 3.11 or later** for the snapshot and metrics scripts, which read TOML with `tomllib`.
- **`llm-wiki`**, a declared dependency, enabled with this plugin. The bundled base is an
  [llm-wiki](../llm-wiki): it powers answering (`wiki-query`) and maintaining the base
  (`wiki-ingest`, `wiki-lint`, `wiki-serve`, `wiki-keeper`).

## Extending tend-board

A dimension exists only where a base page states a rule with a sign readable from a snapshot. Its
file names that page at each step, says what does not count, and gets a row in
`skills/tend-board/dimensions/README.md`.

Two rules have a page and no dimension yet: backward moves (`wiki/moving-work/backward-movement.md`),
which now have transitions to read, and work in progress per assignee
(`wiki/moving-work/wip-per-executor.md`, `wip.by_assignee` in the metrics).

## Layout

```
task-master/
├── agents/
├── skills/
├── scripts/         # snapshot and metrics
└── knowledge/       # a wiki root — holds SCHEMA.md
```

`knowledge/raw/` is gitignored (copyright); `knowledge/wiki/` is committed.
