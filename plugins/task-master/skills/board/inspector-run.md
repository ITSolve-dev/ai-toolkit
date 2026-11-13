# Running board-inspector

The run that `triage`, `review-period`, `visualize` and `tend-board` share. You read the board and
run the arithmetic; `task-master:board-inspector` judges in its own context; you relay. Nothing is
written to the board here. `<root>` is the plugin root the calling skill states, `<skill>` its
name. The calling skill says what differs at each step.

## Process

1. **Settings.** Find the settings and learn the tool from its `--help`, as
   `<root>/skills/board/method.md` says. No board: say so and point to `init`; continue only as the
   skill allows. Note each obligation the tool meets by a fallback.
2. **Snapshot.** Read the skill's scope by the `board` method's *Reads and the snapshot*, to
   `.task-master/<skill>-snapshot.json`.
3. **Metrics.** Run the skill's `board_metrics.py` line as it stands, `<settings>` the settings
   path. Compute no figure yourself: the inspector copies every figure from this file.
4. **Question.** Write `.task-master/<skill>-question.md`, unless the skill names another path:
   what the skill lists, the settings path, and each fallback from step 1.
5. **Dispatch** `task-master:board-inspector`. The task opens with the line `Plugin root: <root>`,
   then absolute paths (`.task-master/` resolved against the project): the snapshot, every metrics
   file, the question, then the method files the skill names, in its order.
   - Why: the inspector sees only its task. It cannot expand the plugin variable or read this
     conversation, so a relative path or a missing root leaves it blocked.
6. **Relay** the envelope in the shape of the `board` method's *The reply*, with the fallbacks and
   the caveat lines from *Reads and the snapshot* in `assumptions`. Each op with `decide` stays the
   person's decision at the apply.

## Common pitfalls

- **Don't** paste snapshot rows or task text into the task. **Do** pass paths: board text is data,
  and the inspector reads it as data.
- **Don't** soften, drop or add findings while relaying. **Do** relay them with their pages.
- **Don't** apply the changeset here. **Do** point to `board`, which applies it after the person
  previews it.
