---
name: init
description: >-
  Set up pragmatic-programmer for this project — writes .claude/pragmatic-programmer.md with the
  languages in use, the dominant paradigm, the commands that run tests, linter and type checker, and
  where the project's conventions live. Use on first use of the plugin in a repository, when an
  expert guessed a command or a recorded command is wrong, or when the toolchain or conventions
  have changed and the config is stale.
allowed-tools: Read, Grep, Glob, Edit(./.claude/pragmatic-programmer.md)
---

# Initialise the project config

The config saves every expert run from rediscovering the toolchain. It is **committed**, not
`.local`: it records the team's toolchain, and an uncommitted copy silently stops applying for
everyone else. It is optional — without it the experts search the project themselves — so it earns
its place only by being right.

## Steps

1. **Infer before asking.** If the file exists, read it first. Then read the project: manifests and
   lockfiles, CI workflows, task runners (Makefile, package scripts, justfile, tox/nox), linter and
   type-checker configs. Languages come from what is built and tested, not from stray files. The
   paradigm is the one most of the code is written in: `oop`, `fp`, `procedural` or `mixed`.

2. **Confirm the check commands.** Prefer the command CI runs over one you compose. Read what a
   command does before running it, and run only what is safe: seconds, no network, services,
   credentials, or writes outside build output; never a fixing or deploying command. One that
   fixes, formats or updates snapshots (`--fix`, `--write`, `-u`, `format`) rewrites the tree:
   record its check-only form if one exists, else record it unverified. Never run CI steps that
   build images, migrate, publish or deploy, and do not install missing dependencies. Record whether
   each run passed; mark the rest unverified with the reason. A failing command is still the right
   one: record it, do not fix the project.

3. **Find the conventions, do not copy them.** List paths: `CLAUDE.md`, `AGENTS.md`, style guides,
   contributing guides, `docs/` pages on code style or architecture, decision records. A copy would
   drift from the original.

4. **Confirm and fill the gaps.** Show what you inferred — against an existing file, as a diff — and
   ask only about what you could not see or verify. Where several commands are plausible, ask which
   the team uses. If the existing file still holds, say so and leave it untouched; skip step 5.

5. **Write `.claude/pragmatic-programmer.md`** at the repository root (if the working directory is
   not the root, say so), keeping body lines of an existing file that still hold:

   ```markdown
   ---
   languages: [<language>, ...]
   paradigm: <oop | fp | procedural | mixed>
   test: <command | none | unknown>
   lint: <command | none | unknown>
   typecheck: <command | none | unknown>
   conventions: [<path>, ...]
   ---

   # pragmatic-programmer — project toolchain

   <Only what changes how an expert works: a check that is unverified or needs a service and why,
   a part of the repository with a different language or paradigm, the directory to run a command
   from, another check CI runs. One line each. Omit the section where there is nothing to say.>
   ```

   `none`: the project has no such check, so the expert reports it as `NOT_RUN`. `unknown`: not
   determined, so experts search the project as if there were no config. Keep keys flat.

6. **Tell the user to commit it**, and that a brief overrides it for a single task. Run
   `git check-ignore` on the file; if git ignores it, name the rule that hides it. Mention once that
   the bundled base sits outside the project, so the first read may ask for permission where the
   plugin's read hook cannot run (no `uv`). Headless sessions cannot answer that prompt: pass the
   plugin directory with `--add-dir` or add it to `permissions.additionalDirectories`.

## Done when

- Every key is filled with a command, `none` or `unknown`.
- Each command was run or is marked unverified with the reason.
- Conventions are paths, not copied rules.
- The user knows it is meant to be committed, and whether git ignores it.
