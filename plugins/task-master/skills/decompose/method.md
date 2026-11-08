# decompose: method

Turn a document, requirements or a description into a tree of tasks an agent can each finish and
present once. Leaves are board tasks; nodes above them only group. Every cut, edge and size cites
the page it came from; open each page named in a step before making that step's decision.

## Input

The work (a path or text); optionally neighbouring and finished tasks and the project setup.
Existing tasks given as the work mean a re-cut recommendation. A missing input does not stop the
run: record in `assumptions` what replaced it.

## Output

Always written whole to `.task-master/decompose-<slug>.md` in the caller's project (slug from the
input's file name or title), and the path returned: `board` reads the file, not a retelling. The
file holds the tree, the questions and the assumptions, in this shape:

- **Group node:** id, title, purpose. No size.
- **Leaf:** id, title, then five headings under these names: `Purpose`, `Boundaries`,
  `Out of scope`, `Links`, `Acceptance criteria` (or the first of `[process].acceptance_headings`
  where the caller names the project's), then `Size: <step> — <what it rests on>`.
- **Placeholder:** marked as one; title, purpose and a coarse size only.
- **Links:** only direct edges, each marked `sequence` or `wait`, then the siblings and
  neighbours the leaf overlaps (step 7); `board` copies this line verbatim. Drop a `sequence` edge
  another path already implies: it adds a link to keep true and no order.
- **Question:** names the leaf ids it touches, or `all`, so `board` holds back only those.
- **Hold:** only where the piece before an outside wait has nothing to show, the leaf stays whole
  and its Boundaries say "Not to start until <party> delivers <what>"; otherwise cut at the wait.

Ask, rather than assume, about: an unresolved wait, a decision only a person can make, the choice
between enumerating and first slices, and where the work lands.

## Process

1. **Read the setup.** Classify it as flow, iterations with an SLE, or iterations without one, since
   the size ceiling depends on it (`wiki/moving-work/board-rules-by-setup.md`). Absent: assume
   iterations with no SLE and say so. Record the scale, capacity, finished tasks and where the work
   lands (repositories, teams taking separate requests). One leaf never spans two such places; input
   touching several with no stated split is a question. Mark each fact given or assumed.
2. **Decide how far to cut now.** Read `wiki/cutting-work/how-far-to-split-up-front.md` and
   `wiki/cutting-work/choosing-between-splits.md`. Return "enumerate" or "first slices" with the
   reason; with first slices, the rest stays placeholders (`wiki/sizing/size-ceiling.md`).
3. **List coarsely first.** Read `wiki/cutting-work/initial-task-inventory.md` and
   `wiki/cutting-work/compound-task-text-signs.md`. A component the input assumes exists, with
   nothing showing it does, becomes an entry or a question, never only an assumption
   (`wiki/task-content/all-work-to-finished-is-in-the-plan.md`).
4. **Cut entries into vertical slices.** Read `wiki/cutting-work/vertical-slice.md`,
   `wiki/cutting-work/component-task-masquerading.md`, `wiki/cutting-work/story-splitting-patterns.md`
   and `wiki/cutting-work/choosing-between-splits.md`. A spike only as
   `wiki/cutting-work/spike-as-last-resort.md` allows, with a placeholder for the follow-on.
5. **Test every leaf: finishes without waiting, presented once.** Read
   `wiki/cutting-work/unit-of-work.md`, `wiki/ordering/sequence-versus-wait.md` and
   `wiki/cutting-work/compound-task-text-signs.md`. A concern (consent, audit, error handling, a
   performance target) leaves its parent only when the person steering would accept the parent
   without it and it is what puts the parent over the ceiling
   (`wiki/cutting-work/story-splitting-patterns.md`, Mixed priority and Deferred Concern Slice).
   Otherwise it stays: a result review would reject is not presented. An outside wait is cut at,
   except as *Hold* says. Write the verdict ("can ship alone" or "presented once", and why) into
   Boundaries.
6. **Mark dependencies.** Read `wiki/ordering/sequence-versus-wait.md`,
   `wiki/ordering/independent-tasks.md` and `wiki/ordering/handling-a-sequence-dependency.md`.
   Before keeping a `sequence` edge, check whether a stand-in lets the leaf start now; if so, the
   stand-in goes into the leaf, the edge goes, and the stub gets its follow-up task. The user's path
   order is no edge, and a spike gates only the leaves whose build needs its answer. A cycle means
   a wrong link or two leaves that are one; two leaves changing the same behaviour name the one
   that holds it. Rules no page states:
   - A chain whose head is not near work is a sign to break it.
   - What a leaf's acceptance needs and no leaf builds is a missing entry (step 3).
   - Acceptance that needs what a later leaf builds is wrong: reorder or re-cut.
7. **Fill the five headings.** Read `wiki/task-content/underspecified-task.md`, then per heading:
   Purpose `wiki/task-content/task-must-justify-itself.md`; Boundaries
   `wiki/task-content/conversation-moves-into-the-task.md` and
   `wiki/task-content/recoverable-versus-task-only-facts.md`; Out of scope
   `wiki/cutting-work/related-changes-temptation.md`; Acceptance
   `wiki/task-content/testable-acceptance.md` and `wiki/task-content/conditions-of-satisfaction.md`.
   Three rules no page states:
   - Leave a decision to the executor only when either answer keeps the leaf's size and touches no
     other leaf; otherwise it is a question, or its own leaf or spike.
   - Links also name siblings and passed-in neighbours the leaf touches, so an overlap shows to
     whoever reads one task alone.
   - A condition several leaves share is written into each one's criteria, never cited by id:
     each leaf is read alone on the board. Testing and documentation the project's done asks for
     go into the criteria.
8. **Size every leaf relatively.** Read `wiki/sizing/estimation-scale.md`,
   `wiki/sizing/estimating-by-horizon.md`, `wiki/sizing/triangulation.md` and
   `wiki/sizing/estimating-underspecified-work.md`. No project scale: assume 1, 2, 3, 5, 8 near and
   13, 20, 40, 100 for placeholders, and say so. A leaf used as a reference must itself pass the
   ceiling. Pieces are not adjusted to total their parent (`wiki/sizing/estimation-scale.md`).
   Example: `Size: 5 — like T-12 (3) plus a second data source; smaller than T-7 (8)`.
9. **Check the ceiling; re-cut at most twice.** Read `wiki/sizing/size-ceiling.md` and
   `wiki/sizing/hidden-wip-in-large-items.md`. With no SLE, capacity or fixed step, the ceiling is
   the top of the near scale (8), as an assumption. A leaf over goes back to step 4; after two
   rounds, what still fails becomes a question naming what blocks the cut. Stop and combine as
   `wiki/sizing/over-disaggregation.md` and `wiki/cutting-work/combining-small-tasks.md` say.
10. **Check the whole.** All leaves together deliver the request and nothing it did not ask for
    (`wiki/task-content/task-must-justify-itself.md`). Every leaf passed step 5 after the last
    re-cut. A question about an assumed component also carries a placeholder sized as work, so its
    cost stays in the totals.

## Common pitfalls

- **Don't** pass an entry into the tree in the input's wording. **Do** cut it by the pages in steps 3–4.
- **Don't** cut by layer or activity ("add table", "write endpoint"). **Do** cut slices a reviewer can observe.
- **Don't** put a condition on releasing the result as a `wait` edge. **Do** write it into
  Boundaries and let the leaf start (`wiki/ordering/sequence-versus-wait.md`, A handoff at the end).
- **Don't** fill a heading with words no reader could disagree with ("robust", "as needed").
- **Don't** present a placeholder as a task, or size a group node by summing its leaves.
