---
name: init
description: >-
  Set task-master up in a project: find how the project reaches its board, record the tool's
  commands and what it can and cannot do, map every board status to the plugin's kinds, and record
  the setup, period, SLE, estimation scale with its ceiling, and where the team's process document
  is. Writes `.claude/task-master.toml` and proposes permission rules. Use on first use of a board
  skill in a project, when a skill reports the board is not set up, an unmapped status or a changed
  tool version, or when the board or its tool has changed. Questions about how to set a board up go
  to ask; applying changes to the board is board.
argument-hint: "[what changed, if this is a rerun]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.claude/task-master.toml), Edit(./.gitignore), Edit(./.task-master/**)
---

# init

Runs in your context, because it runs commands and asks the person. Follow
`${CLAUDE_PLUGIN_ROOT}/skills/init/method.md`; the file it writes is specified in
`${CLAUDE_PLUGIN_ROOT}/skills/init/config-format.md`. A `wiki/<group>/<page>.md` path is under
`${CLAUDE_PLUGIN_ROOT}/knowledge/`.

What holds throughout:

- **Nothing found is recorded unconfirmed.** Show what you found and where, and let the person
  confirm or correct it. A guessed tool, board or status mapping fails later as work on the wrong
  board or a rule firing wrongly, not as an error.
- **Ask what only the person knows; look up the rest.** Help output, config files and the board's
  own lists are read, not asked. Ask one topic at a time, offering what you found as the default.
- **Read the process document; never create or edit it.** Where it lacks something init needed,
  propose the addition to the person, who decides.
- **Propose permission rules; never write settings.** The person edits them.
- **Write the config only after the person has seen all of it**, or on a rerun the diff against the
  current file.

Report at the end: the file written, each capability and its fallback with what the fallback costs,
statuses left unmapped, the permission rules proposed, and what the person declined to give.
