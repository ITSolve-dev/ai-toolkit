# Synthesis

The evolving thesis of this wiki: what DDD's patterns mean taken together.

## Current thesis

With Vernon's canonical text ingested, the earlier "aggregate is the unit of consistency" reading is
subsumed into a larger frame: **DDD is one interdependent pattern language whose binding thread is the
[[ubiquitous-language]], scoped by the [[bounded-context]].** You cannot pull one pattern out on its
own — [[aggregate]] presupposes [[entity]] and [[value-object]] and Repository; [[ubiquitous-language]]
presupposes [[bounded-context]]. That interdependence is *why* partial adoption fails as [[ddd-lite]].

The language sits at the centre because it is what makes every other boundary precise. A
[[bounded-context]] is defined as a *linguistic* boundary, not a technical one; the same word
("Order", "Client", "Account", "Book") legitimately means different things across it; and the whole
[[domain-model]] is just that Language expressed as code. Get the linguistics wrong and the model is
wrong even when it compiles ([[blending-models-in-one-context]]).

## The two poles, and a third axis

DDD runs between two poles held together by that shared language:

- **The strategic pole — where you *divide*.** The problem space is assessed with [[subdomain]]s
  (a [[core-domain]] you must excel at, plus supporting and generic subdomains you needn't); the
  solution space realizes it as [[bounded-context]]s ([[problem-space-and-solution-space]]). A context
  is sized by the completeness of its Language, not by technology ([[bounded-context-sizing]]), and
  contexts relate through the [[context-map]] patterns — the [[upstream-downstream]] axis, the
  organizational relationships ([[partnership]], [[shared-kernel]], [[customer-supplier-development]],
  [[conformist]]), and the integration techniques ([[anticorruption-layer]], [[open-host-service]],
  [[published-language]], [[separate-ways]]) — with [[big-ball-of-mud]] as the honest label for the
  legacy tangle you must integrate but not model.
- **The tactical pole — where you *build*.** An [[aggregate]] clusters [[entity]]s (identity that
  endures) and [[value-object]]s (self-validating, identity-free) behind a consistency boundary drawn
  around a *true invariant* ([[model-true-invariants-in-consistency-boundaries]]), kept as small as that
  invariant allows ([[design-small-aggregates]]) and holding other aggregates by identity
  ([[reference-other-aggregates-by-identity]]) so everything outside the boundary is reconciled by
  [[eventual-consistency]]. A root enforces those invariants in its own behaviour; a [[factory]] births
  it, a [[repository]] persists it, a [[domain-service]] carries behaviour that spans aggregates, and
  [[modules]] package the language into cohesive containers. A thin [[application-service]] coordinates
  use cases over it — never holding domain logic ([[application-service-vs-domain-service]]) — and a
  [[domain-event]] records what happened. The aggregate-as-consistency-boundary idea still holds and
  still propagates outward — its events mark context edges ([[domain-events-vs-integration-events]]).

Vernon adds a **third, orthogonal axis: architecture.** The domain model is deliberately
*architecturally neutral* and takes priority over any surrounding style; architecture is chosen
**risk-driven, not coolness-driven** ([[architecture-selection]]), and — the load-bearing DDD rule —
must never dictate the *size* of the model or a context. [[hexagonal-architecture]] (reached from
[[layered-architecture]] via [[dependency-inversion-principle]]) is the recommended host precisely
because it keeps the model at the centre while [[cqrs]], [[event-driven-architecture]],
[[event-sourcing]], [[long-running-process]] and [[rest-and-ddd]] plug in around it as specific risks
demand. [[event-sourcing]] (A+ES) is the deepest of these: it makes an aggregate's ordered stream of
[[domain-event]]s the *source of truth*, reconstituting state by replay rather than storing it — the
tactical thesis "the aggregate is a consistency boundary whose events are what actually happened" taken
to its logical end. Because event streams are hard to query it all but forces [[cqrs]] read models
([[read-model-projection]]), and it comes with its own discipline — [[optimistic-concurrency-control]],
[[aggregate-snapshot]], and versioned, enrichment-aware event contracts
([[domain-event-contract-design]]).

## The unifying discipline

What unites all three axes is one discipline: **push behaviour and meaning onto the objects and
boundaries that own them** — and let language, not technology, decide where the boundaries fall. Its
violations each have a name: the [[anemic-domain-model]] (behaviour drained out of the model into
services), [[ddd-lite]] (the strategic half skipped), and [[blending-models-in-one-context]] (two
Languages fused into one). Every building block and boundary above is, in part, a defence of that one
rule.

## The Cosmic Python confirmation — "keep the model free of infrastructure"

Percival & Gregory's [[web-page-cosmic-python-book|Cosmic Python]], now ingested end to end, arrives at
the same thesis from Python and states its corollary sharply: the whole tactical apparatus exists to
*write* data, so a "**domain model is a write model**." That single observation ties the Cosmic Python
half of this wiki together. It justifies keeping the model pure via the [[dependency-inversion-principle]]
and [[ports-and-adapters]] (details depend on abstractions; adapters are injected at a composition root),
and it justifies the read side: because reads are conceptually different — cacheable, stale-tolerant,
often on different entities — they get their own [[read-model]] under [[cqrs]], and forcing them back
through the write model is the [[reusing-the-write-model-for-reads]] anti-pattern. The same "write model"
insight is why the event architecture ([[domain-event]] recorded on the aggregate, [[message-bus]],
[[commands-and-events]]) keeps dispatch *out* of the model, and why [[infrastructure-leaking-into-the-domain-model]]
is named as a failure.

Cosmic Python's other distinctive contribution is the pragmatic "**how do I get there from here?**" thread
that the canonical texts mostly omit: the [[big-ball-of-mud]] as the honest starting state, escaped either
by [[refactoring-toward-ddd]] in place (extract use cases behind a service layer, pull I/O out, then
identify [[aggregate|aggregates]]) or by the [[strangler-fig-pattern]] wholesale, begun with
[[collaborative-domain-modeling]]. Its abiding message is that all of this is **incremental** — adopt the
patterns bit by bit, tolerate temporary mess — and that discipline extends to [[validation]], placed by
subtype (syntax and semantics at the edge, pragmatics in the domain) precisely to keep the model clean.

*Now anchored in two full-length texts — Vernon's canonical *Implementing DDD* (front matter through
Appendix A) and Percival & Gregory's *Cosmic Python* (front matter through Appendix E) — alongside the
practitioner sources and Fowler's anti-pattern statement. The tactical pole is filled out in depth
(Entities, Value Objects, Aggregates and their design rules, Repositories, Unit of Work, Factories, Domain
Services, Modules, the application tier, Event Sourcing, the message-bus/CQRS read side, and the
legacy-refactoring playbook). The two texts corroborate each other closely; the open frontier is now
sources beyond them — notably Evans' original "blue book" — for contrast and any genuine disagreement.*
