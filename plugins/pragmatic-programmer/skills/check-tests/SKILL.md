---
name: check-tests
description: >-
  Report what a project's tests actually catch: the break each test would detect, the tests that
  cannot fail, and the conditions no test guards, proven by running deliberate mutants in a scratch
  copy. Use when someone asks whether tests are good enough, "would these tests catch a bug", "are
  these tests real", or what a change leaves untested. Not for running the tests or checking that
  they pass. Report-only: it edits no project file.
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**), Grep, Glob
---

# Check tests

A green suite says the tests ran, not that they can fail. Read what each test pins, then break the
code on purpose and see whether a test notices. Each mutant is an edit and a run outside the
project: expect permission prompts, or ask the user once to allow the scratch directory. Headless
without Bash, Edit or Write permission, only the reading runs; mutants are `NOT_RUN`.

Base root: `${CLAUDE_PLUGIN_ROOT}/knowledge`; the group is `wiki/testing`.

**If a read of the base fails, yours or the inspector's, say so before any result.** Interactively,
approve the prompt; headlessly, pass the plugin directory with `--add-dir`.

## Steps

1. **Scope**: the tests and the code they cover. The test command comes from
   `.claude/pragmatic-programmer.md`, else the project. No runnable command: mutants are `NOT_RUN`;
   the reading still runs.

2. **Read the tests.** Dispatch `pragmatic-programmer:inspector` in the background: dimension
   `testing`, the absolute base root, tests and code under test as scope, the conventions. Ask for
   findings on tests that cannot fail or pin too little, as the `testing` pages define them.
   `NEEDS_INFO` goes to the user; continue the same inspector. `BLOCKED`, or no report: the reading
   goes under not checked. Wait for it before step 5.

3. **Pick conditions to mutate**: those the change touches, else the guards, boundaries and branches
   the code's purpose rests on. Cap at about ten and say where you cut. Run only the tests covering
   the mutated file where the runner allows it, within a time budget; list what it stopped under not
   checked.

4. **Make a scratch copy** in a temp or scratchpad directory, with uncommitted changes, without
   `.env` or other secrets. Never mutate the working tree or use `git stash`: an interrupted run
   would leave the user's code broken. Record the copy's absolute root; check every edit path starts
   with it.
   - Mutate only code whose tests are hermetic: no network, database, containers, credentials or
     paths outside the copy. Mark the rest `NOT_RUN` with the reason.
   - Run the suite unmutated; exclude a test already red and say so.
   - Plant one mutant that must break, such as raising at the entry of a function under test. If the
     suite stays green, the copy runs other code (editable install, shared environment, absolute
     alias): mark mutants `NOT_RUN`. If it needs dependencies installed, do not install them; same.

5. **Mutate one condition at a time** as `wiki/testing/sabotage-your-tests.md` describes. Record
   which test failed and whether for that reason; revert by copying the original back from the
   project, not by a reverse edit, and confirm it matches. A mutant that does not compile is not
   killed. A surviving mutant is a gap — name the missing test, its input and expected result —
   unless it does not change behaviour: record it as equivalent, with the reason. A run beats an
   inspector finding it contradicts.

6. **Delete the copy**: only the recorded root, only if it is outside the project and inside the
   temp or scratchpad directory, never a path from an empty variable. Report it if deletion failed.

## Report

- **Per test**: the break it catches, from the mutant runs; "not exercised" where no mutant reached
  it; "cannot fail" with reason and page, from the inspector.
- **Mutants**: `file:line`, the change, killed (by which test), survived (missing test) or
  equivalent (reason).
- **Checks**: each command run, with the output lines that carry the result; unrun is `NOT_RUN`
  with the reason.
- **Not checked**: conditions cut, red tests, the non-hermetic part, what the budget stopped.

Tests that catch every mutant are a valid result; say so plainly. Never propose weakening a test —
loosening an expectation, removing an assertion, skipping it — to improve a result. A test that
cannot fail gets a repair that lets it fail.
