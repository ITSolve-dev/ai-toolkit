# decompose: method

Turn a document, requirements or a description into a tree of tasks. Leaves are board tasks; nodes
above them only group. Open a cited page when a case is borderline. "This wiki's reading" below
means the base marks the rule as its own, not a source's.

## Inputs and output

- **Passed by the skill:** the work (a path or text); optionally neighbouring and finished tasks
  and the project setup. Existing tasks given as the work mean a re-cut recommendation.
- **Missing inputs do not stop the run**; each absence goes to `assumptions` with what replaced it.
  Questions instead: an unresolved wait, a decision only a person can make, a choice between
  enumerating and first slices, where the work lands.
- **`changeset`:** the tree. Per group node: id, title, purpose. Per leaf: id, title, the five
  headings of step 7 (Links carries the edges, each marked `sequence` or `wait`), `Size` (a step
  and what it rests on). Placeholders (step 2) are marked as such and carry a title, purpose and a
  coarse size. Each question names the leaf ids it touches, or `all`, so `board` holds back only
  those. `board` maps the tree to ops (*From decompose*).
- **Written whole:** the result (tree, questions, assumptions) always goes to
  `.task-master/decompose-<slug>.md`, the slug from the input's file name or title, and the path
  is returned: `board` reads it there, not a retelling.

## Steps

1. **Read the setup.** Classify it as flow, iterations with an SLE, or iterations without one,
   because the size ceiling differs by setup (`wiki/moving-work/board-rules-by-setup.md`). Absent:
   assume iterations with no SLE (this method's own default) and say so. Also record a scale,
   capacity, finished tasks, and where the work lands (repositories, teams taking separate
   requests): one leaf cannot span two such places (this method's own rule), so input touching
   several with no stated split is a question.
   *Output:* one line per setup fact, each marked given or assumed. *Wrong if:* a ceiling in step 9
   is computed from a quantity this step recorded as absent, or one leaf's scope lands in two places.

2. **Decide how far to cut now.** Will starting the work teach what the work is? If yes, cut one or
   two first slices through the part most likely to surprise and leave the rest as placeholders;
   if no, enumerate (`wiki/cutting-work/how-far-to-split-up-front.md`;
   `wiki/cutting-work/choosing-between-splits.md`, Find the Core Complexity). Treat it as "yes"
   when the outcome hangs on people's behaviour or a new external dependency and no similar work is
   among the finished tasks (this wiki's reading, so the choice goes to `assumptions`). Work far
   from starting may stay a placeholder (`wiki/sizing/size-ceiling.md`, When to Split a Task).
   *Output:* "enumerate" or "first slices", with the reason. *Wrong if:* a placeholder is presented
   as a task, or enumerated leaves depend on answers only the first slice will give.

3. **List coarsely first.** Walk the user's path through the work (before, during, after) to find
   candidate entries, then discard the frame (`wiki/cutting-work/initial-task-inventory.md`). A
   catch-all title ("fast", "polished") is listed out: standalone items become tasks, the rest
   conditions on the tasks needing them (`wiki/cutting-work/compound-task-text-signs.md`). A
   component the input assumes exists, and no neighbour, finished task or setup fact shows
   existing, is an entry too, or a question, never only an assumption: work no leaf holds is
   missing from every total (`wiki/task-content/all-work-to-finished-is-in-the-plan.md`).
   *Wrong if:* an entry passes to the tree unchanged from the input's wording.

4. **Cut entries into vertical slices.** Each leaf changes something a reviewer can observe; it need
   not be releasable alone (`wiki/cutting-work/vertical-slice.md`), which never licenses cutting
   out a concern step 5 keeps in. A layer, activity or artifact is combined with its neighbours,
   not cut smaller (`wiki/cutting-work/component-task-masquerading.md`). Cut with the patterns and
   their triggers (`wiki/cutting-work/story-splitting-patterns.md`), never one task per workflow
   step. Where several cuts fit, prefer the one exposing a piece to drop, then the one with more equal
   pieces (`wiki/cutting-work/choosing-between-splits.md`; the order is this wiki's). A spike only
   when the implementation is poorly understood and no pattern applies, its acceptance written as
   questions, with a placeholder for the follow-on (`wiki/cutting-work/spike-as-last-resort.md`).
   *Wrong if:* leaves read as a list of layers or activities ("add table", "write endpoint").

5. **Apply the two tests to every leaf** (`wiki/cutting-work/unit-of-work.md`; the tests are the
   charter's). *Finishes without waiting:* list what the leaf needs during work. A decision only
   another person can make, or anything an outside party holds, is cut out so it falls between
   tasks (`wiki/ordering/sequence-versus-wait.md`, this wiki's rule). A predecessor finished first,
   and review of the presented result, are not waits. If the piece before the wait has nothing to
   show, keep the task whole: its Boundaries read "Not to start until <party> delivers <what>", and
   its Links carry the `wait` edge. A
   condition on releasing or enabling the result comes after the executor's part, so it is no
   `wait` edge: write it into Boundaries and let the leaf start (this method's reading of the same
   page, A handoff at the end). *Presented once:*
   read title, text and criteria for conjunctions, separators, unnamed plurals and criteria that
   could each ship alone; split only if each part can be delivered alone
   (`wiki/cutting-work/compound-task-text-signs.md`). A concern (throttling, consent, audit, error
   handling, a performance target) leaves the parent only if the person steering would accept the
   parent's result without it (`wiki/cutting-work/story-splitting-patterns.md`, Mixed priority: the
   test) and it is what puts the parent over the ceiling (same page, Deferred Concern Slice, When
   it applies). Otherwise it stays: a result review would reject is not presented, whatever the
   parent's acceptance omits or a "not released without" note says (this method's rule). Write the
   verdict ("can ship alone" or "presented once", and why) into the leaf's Boundaries, so a later
   check sees it was considered.
   *Wrong if:* a leaf's scope includes both obtaining something from outside and building on it,
   a `wait` edge names a condition on release, or a leaf may not be released without another.

6. **Mark dependencies.** Who holds the prerequisite: the project (`sequence`) or an outside party
   (`wait`) (`wiki/ordering/sequence-versus-wait.md`). What a leaf's acceptance needs to exist and
   no leaf builds is a missing entry (step 3). Before making a need a `sequence` edge, ask whether
   a stand-in (stub, fixture, test double, data put in directly, a developer command) lets the leaf
   start and be checked now with a presentable result; if so it goes into the leaf and the edge
   goes (`wiki/ordering/independent-tasks.md`, scaffold it;
   `wiki/ordering/handling-a-sequence-dependency.md`, The test, What leaving the order costs).
   Keep an edge the wanted order already meets, stating what the estimate assumes exists (same
   page). A chain whose head is not near work is a sign to break it (this method's reading of
   that page's Which remedy, when, branch 3, and the chain sign on `independent-tasks.md`, Why).
   The user's path order is no edge; a spike gates only leaves whose build needs its answer. Keep
   only direct `sequence` edges: one another path already implies is dropped, since it adds a link
   to keep true and no order. A stub gets a follow-up task, sized 0 if the scale has one, its
   criteria saying it is a stub (same page, The zero-point task). *Wrong if:* the edges form a cycle (a link is wrong, or the two are
   one task); acceptance needs what a later leaf builds; two leaves change the same behaviour (name
   the one holding it); an edge stands where a stand-in would let the leaf start.

7. **Fill the headings.** Every leaf carries, in its text, these five headings, because an agent
   fills a gap by guessing (`wiki/task-content/underspecified-task.md`):
   - **Purpose:** who it serves and why, not a restatement of the action
     (`wiki/task-content/task-must-justify-itself.md`).
   - **Boundaries:** the decisions it depends on, made and written, or explicitly left to the
     executor; no "as discussed", "TBD", "the usual way"
     (`wiki/task-content/conversation-moves-into-the-task.md`, this wiki's conclusion). A decision
     is left to the executor only when either answer keeps the leaf's size and touches no other
     leaf; otherwise it is a question, or its own leaf or spike, sized as work (this method's own
     rule). Task-only facts are required; facts the repository shows are included when known
     (`wiki/task-content/recoverable-versus-task-only-facts.md`, this wiki's extension).
   - **Out of scope:** nearby work that is not this task's, each item pointing at the leaf or
     placeholder that holds it, so the executor does not absorb it
     (`wiki/cutting-work/related-changes-temptation.md`); a concern step 5 let out is named here
     with the leaf carrying it.
   - **Links:** the step 6 edges with their kind, plus siblings and passed-in neighbours this leaf
     touches (this method's own rule, so an overlap is visible to whoever reads one task alone).
   - **Acceptance criteria:** (the first of `[process].acceptance_headings` where the caller
     names the project's) observable checks a reader could pass or fail; a graded word in the title gets
     a condition pinning it; a threshold covers its edges; testing and documentation the project's
     done asks for are included (`wiki/task-content/testable-acceptance.md`,
     `wiki/task-content/conditions-of-satisfaction.md`). A condition several leaves share is
     written into each one's criteria, never cited by id: each leaf is read alone on the board.
   *Wrong if:* a heading is filled with words no reader could disagree with ("robust", "as needed").

8. **Size every leaf relatively.** Use the project's scale; with none, assume 1, 2, 3, 5, 8 for
   near work and 13, 20, 40, 100 for placeholders, and say so (`wiki/sizing/estimation-scale.md`,
   `wiki/sizing/estimating-by-horizon.md`). Size is relative, not days or hours
   (`wiki/sizing/ideal-days.md`). Place each leaf between a finished task one step smaller and one
   a step larger (`wiki/sizing/triangulation.md`); with none, against several other leaves, not
   one, marked unanchored (same page, Failure signs). A reference leaf must itself pass the step 9
   ceiling; one over is re-cut before anything is sized against it (this method's rule, from that
   page's Limit). A vague leaf still gets a size, its assumption stated
   (`wiki/sizing/estimating-underspecified-work.md`). Group nodes get no sum, and pieces are not
   adjusted to total their parent (`wiki/sizing/estimation-scale.md`).
   *Output:* `Size: 5 — like T-12 (3) plus a second data source; smaller than T-7 (8)`.
   *Wrong if:* a value off the scale, or a size with no stated basis.

9. **Check the ceiling; re-cut at most twice.** The ceiling depends on setup
   (`wiki/sizing/size-ceiling.md`, this wiki's resolution): an SLE given, likely to finish inside
   it; iterations with capacity given, capacity ÷ 6, never more than one period; otherwise the
   step fixed at setup, else the top of the near scale (8: this method's own default, drawn from
   the near test in `wiki/sizing/estimating-by-horizon.md`). Under every setup a leaf whose
   contents cannot be listed is over. A list does not pass a leaf either: one naming several
   results that could each be presented alone, or that would reach review as several unrelated
   changes, is over (`wiki/sizing/hidden-wip-in-large-items.md`). A leaf over returns to step 4;
   after two rounds, what still fails goes to `questions` with what blocks the cut (this method's
   own rule). Stop cutting once
   a piece compares with known tasks (`wiki/sizing/over-disaggregation.md`). A leaf below the
   smallest step with a related sibling of equal priority is combined with it
   (`wiki/cutting-work/combining-small-tasks.md`). *Wrong if:* a near leaf sits above the ceiling
   without a question, or a leaf was cut only to make sizes look equal (`wiki/sizing/size-spread.md`).

10. **Check the whole.** All leaves done would deliver the input's request and nothing it did not
    ask for (`wiki/task-content/task-must-justify-itself.md`, across tasks). Every leaf passed step
     5 after the last re-cut. A question about an assumed component also carries a placeholder sized
    as work, so its cost stays in the totals (this method's rule). *Wrong if:* part of the request,
    or a component it assumes, maps to no leaf or placeholder.
