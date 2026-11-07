---
name: init
description: >-
  Set task-master up in a project: find the workflow config file (or propose one), add the missing
  board, label, size and [process] settings by asking, then bring the board to them. Use on first
  use of a board skill, or when a skill reports the board not set up, an unmapped status, an
  undeclared marker label or a missing setting. Questions go to ask; applying a changeset to tasks
  is board.
argument-hint: "[what changed, if this is a rerun]"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Read(${CLAUDE_PLUGIN_ROOT}/skills/**), Edit(./.gitignore), Edit(./.task-master/**), Bash(python ${CLAUDE_PLUGIN_ROOT}/scripts/snapshot.py *)
---

# init

Runs in your context, because it runs commands and asks the person. Follow
`${CLAUDE_PLUGIN_ROOT}/skills/init/method.md`; what the settings hold is in
`${CLAUDE_PLUGIN_ROOT}/skills/init/settings.md`. A `wiki/<group>/<page>.md` path is under
`${CLAUDE_PLUGIN_ROOT}/knowledge/`.

What holds throughout:

- **One settings file: the project's.** Add to it; never create a second one beside it.
- **Nothing found is recorded unconfirmed.** Show what you found and where; the person confirms or
  corrects it. A guessed board or status kind fails later as work on the wrong board or a rule
  firing wrongly, not as an error.
- **Ask only what is missing, one topic at a time**, offering what you found as the default. Help
  output, the file and the board's own lists are read, not asked.
- **Read the process document; never create or edit it.** Propose additions to the person.
- **Only add to the board.** Labels and statuses the file declares are created; nothing is renamed
  or deleted.
- **Propose permission rules; never write settings.** The person edits them.

Report at the end: what was added to the file, what was created on the board, what is left for the
person by hand, each fallback the tool forces and its cost, and the permission rules proposed.
