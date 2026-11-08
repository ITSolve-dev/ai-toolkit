# Log

Append-only record of operations. One line per operation, newest at the bottom:

`## [YYYY-MM-DD] <op> | <description>`  —  `<op>` is a short lowercase verb naming the operation.

<!-- entries below -->
## [2026-11-01] ingest | pragmatic-programmer -- large-source workflow, 154 proposals
## [2026-11-01] review | pragmatic-programmer -- every page checked against raw by independent agents; repairs applied, 4 pages folded (formalize-ad-hoc-tests, impossible-cases-happen, password-policy-anti-patterns, prototype-to-learn)
## [2026-11-02] review | pragmatic-programmer -- random sample of 24 pages re-reviewed, cross-group sweep of signs, owner assignments walked with hard fragments and repaired
## [2026-11-02] fix | pragmatic-programmer -- residual review items: global-data names its split with know-when-to-stop; the after examples on wrap-values-between-transformations and pass-state-dont-hoard-it no longer show the sign of process-values-not-their-source
## [2026-11-03] ingest | elegant-objects -- large-source workflow, 40 proposals
## [2026-11-03] review | elegant-objects -- 49 pages (34 new, 15 edited by the ingest) reviewed independently against raw/ in six groups, 91 quotations checked against page images; blockers on 35 pages (owner conflicts, misreported book, signs needing caller knowledge), all findings applied by six sequential writers, one rejected against the image; check_pages and lint clean, 175 pages
## [2026-11-06] ingest | code-complete -- large-source workflow, 277 proposals
## [2026-11-06] review | code-complete -- 244 touched pages reviewed independently in 21 groups against raw/ and the narrowed scope; blockers on about 110 pages, mostly owner conflicts with pages already in place; architecture pages removed (layering, split-into-components-in-one-deployable, one-class-per-file, incremental-integration) or rewritten to name the architecture as a setting; duplicates merged (name-conditions-with-boolean-variables, error-prone-routines, public-data-members, design-goals-checklist, write-dirty-tests); fixes applied by the reviewers one at a time; 377 pages, check_pages and lint clean
## [2026-11-06] ingest | object-oriented-thought-process -- large-source workflow, 59 proposals
## [2026-11-06] review | object-oriented-thought-process -- 46 touched pages reviewed independently in 4 groups; blockers on 21, almost all owner conflicts with pages from the three earlier books; hide-third-party-apis rewritten (module-dependency rules out of scope), the 'spread over modules' sentence unified on five pages; fixes applied by the reviewers one at a time; check_pages and lint clean
## [2026-11-06] ingest | automata-based-programming -- large-source workflow, 31 proposals
## [2026-11-06] review | automata-based-programming -- 26 touched pages reviewed independently in 2 groups; blockers on 14, nearly all owner conflicts inside the state-machine area (22 pages across three books): one finite-state-machine/switch resolution sentence now identical everywhere, flags/mode/state-reading shapes each given one owner; fixes applied by the reviewers one at a time; check_pages and lint clean
## [2026-11-07] ingest | larman-applying-uml-and-patterns -- large-source workflow, 44 proposals
## [2026-11-07] review | larman-applying-uml-and-patterns -- 50 pages reviewed by 4 independent reviewers against raw/ (23 blockers, mostly owner conflicts with existing pages; 2 merges: software-objects-are-not-people into responsibility-driven-design, keep-fine-grained-classes into keep-objects-small); fixes applied one writer at a time; an existing non-pattern single-implementation layer assigned to minimal-but-complete-functionality. 438 pages.
## [2026-11-07] ingest | railway-oriented-programming -- Wlaschin 2013 web article; summary page, new [[collect-independent-validation-failures]], bind/map/tee plumbing and operator advice merged into [[handle-errors-in-stages-or-in-the-pipeline]]
## [2026-11-07] ingest | against-railway-oriented-programming -- Wlaschin 2019 self-critique; summary page, limits on Result (expected-only test, fail fast, diagnostics, I/O, apathy, performance, interop) and three reverse signs on [[wrap-values-between-transformations]], per-setting resolution against the 2013 catch-all adapter; private-control-flow limit on [[exceptions-for-the-exceptional]]; [[recover-only-at-entry-points]] and [[crash-early]] corroborated, catch-to-failure-value sentence identical on three pages
## [2026-11-07] ingest | fowler-refactoring -- large-source workflow, 113 proposals
## [2026-11-07] review | railway-oriented-programming, against-railway-oriented-programming -- 8 pages reviewed against raw/ (4 blockers: catch-all vs result-value sentences without precedence, a check-then-insert race in a pair); fixes applied.
## [2026-11-07] review | fowler-refactoring -- 111 pages reviewed by 9 independent reviewers (about 37 blockers, mostly owner conflicts and pairs showing a neighbour's sign; 2 pages rewritten to drop architecture: divergent-change-vs-shotgun-surgery, logic-testable-without-ui); fixes applied one writer at a time. SCHEMA: typographic variants in quotations count as equal. 498 pages.
