---
name: init
description: >-
  Set up spec-driven-guide for this project — writes .claude/spec-driven-guide.md with the language
  documents are written in, where design docs and decision records live, and any house conventions.
  Use on first use of the plugin in a repository, when the writing skills ask where to put a file,
  or when the project's documentation conventions have changed and the config is stale.
---

# Initialise the project config

The config exists so the writing skills stop asking the same questions in every session. It is
**committed**, not local: these are the team's conventions, not one person's preferences, and a
document written to a different convention by whoever ran the skill last is the problem it prevents.

## Steps

1. **Infer before asking.** Look at the repository: existing `docs/` layout, any `adr/` or
   `decisions/` directory and the numbering already in use, the language existing documents are
   written in, whether records carry a status field. Most of the config is already visible.

2. **Confirm and fill the gaps.** Present what you inferred and ask only about what you could not
   see. Where the repository has no documents at all, propose defaults and say they are proposals.

3. **Write `.claude/spec-driven-guide.md`**:

   ```markdown
   ---
   language: <the language documents are written in>
   design-docs: <path, e.g. docs/specs>
   decision-records: <path, e.g. docs/adr>
   ---

   # spec-driven-guide — project conventions

   <House conventions the skills should follow: file naming, whether records carry a status field,
   anything this project does differently. One line each. Omit the section where there is nothing
   to say — an empty heading is load with no content.>
   ```

   Keep it to what changes behaviour. A convention the skills would follow anyway costs a line and
   buys nothing.

4. **Tell the user to commit it**, and why: uncommitted, it silently stops applying for everyone
   else, and the divergence shows up as inconsistent documents rather than as a missing file.

   Mention once that the bundled base sits outside the project, so the first skill to read it asks
   for permission — approving once is all it needs. Offer to add
   `permissions.additionalDirectories` only where the project runs Claude headlessly, since a
   headless session cannot answer that prompt.

## Done when

- The file exists with language and both paths filled.
- Every convention in it would change what a skill does.
- The user knows it is meant to be committed.
