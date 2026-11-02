---
title: Prioritization Factors
category: ordering
summary: Cohn's four things to weigh when ordering work are financial value, cost, new knowledge and risk removed; value against today's cost gives a first order, and learning and risk then move items, forward if the item will be built regardless and back if it could be dropped, with each move written down. High-value high-risk work comes first and low-value high-risk work is avoided; an order by one factor leaves a trace in history; a trade-off needs both cost and benefit; money measures apply only when a person supplies cash figures, and the capacity share of an item is read from board history instead.
tags: [concept, ordering, prioritization, risk, learning, method, failure-mode, decision-rule, rule, estimation, value, trade-off]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Prioritization Factors

Cohn ([[cohn-agile-estimating-planning]]) replaces the instruction to prioritize on business value with four factors. He calls that instruction "the vague and mostly useless advice of “prioritize on business value.”" (L1710), because it does not say what business value is.

## The four factors

| Factor | Cohn's wording | Question it asks | Read from |
|---|---|---|---|
| Value | "The financial value of having the features" (L1712) | What would be made or saved? If that cannot be priced, how much do users want it? | The person steering. It is a task-only fact ([[recoverable-versus-task-only-facts]]) |
| Cost | "The cost of developing (and perhaps supporting) the new features" (L1714) | What does it take, now and later? | The size estimate, its share of capacity (*Money Figures*, below), [[cost-now-versus-cost-later]] |
| New knowledge | "The amount and significance of learning and new knowledge created by developing the features" (L1716) | What will we know afterwards that we do not know now? | [[ordering-for-early-user-feedback]] |
| Risk | "The amount of risk removed by developing the features" (L1718) | What could still derail this, and does doing this settle it? | *Risk-Value Quadrants* (below) |

This wiki notes a detail of the wording. The last two factors measure what doing the work removes, not how alarming the work looks. A risky feature that settles nothing else, and that could simply be dropped, scores low on this definition.

## Why four and not two

> Because most projects are undertaken to either save or make money, the first two factors often dominate prioritization discussions. However, proper consideration of the influence of learning and risk on the project is critical if we are to prioritize optimally.
>
> — [[cohn-agile-estimating-planning]], L1720

This wiki reads that as naming the failure directly: an order built from value and cost alone looks complete and has two inputs missing (*Ordering by One Factor* (below)). The two-sided form of the argument is on *A Trade-Off Needs Cost and Benefit* (below).

## Value when it cannot be priced

A financial estimate usually covers a period of "the next few months, quarters, or possibly years" (L1726). It needs a new number of sales, the average sale including follow-on sales and maintenance agreements, and the timing of sales increases (L1734). Where such figures exist, what survives of Cohn's forecast and comparison is in *Money Figures, When a Person Supplies Them* below. Because that is hard, Cohn allows a substitute: "it is possible to use non-financial measures of desirability to represent value." (L1734). [[ordering-by-value-and-urgency]] is this wiki's existing substitute for a project with no revenue to point at.

## Relation to cost of delay

Cohn's list has no urgency factor. In this chapter, timing appears only as an input to a value estimate (L1734), whereas [[cost-of-delay]] treats how fast value drains as an ingredient of its own. This wiki resolves the difference by setting, and the resolution is ours:

- If waiting changes little, because the work ships in one release and its value does not leak before then, value over cost gives the base order.
- If waiting drains value, [[ordering-by-value-and-urgency]] and [[cost-of-delay-over-duration]] give the base order.
- In both settings, knowledge and risk then move items, because the cost-of-delay pages have no slot for them. The procedure is *Combining Prioritization Factors* (below).

## Money Figures, When a Person Supplies Them

Cohn's Chapter 10 turns a theme's value into a cash flow and compares themes by net present value, internal rate of return and payback (L1926-L1932), and prices a theme's cost per story point (L1740, L2087-L2128). This wiki does not keep that chain as method. Money measures apply only when a person supplies cash figures, and none lives on a board; a task on a small board cannot carry a cash flow of its own. Where nobody supplies them, ordering stays with [[ordering-by-value-and-urgency]], and the plugin does not invent a figure. Four points carry over.

- **The requester quantifies the reason.** "At a minimum, whoever is requesting the theme should be able to quantify the reasons for developing it." (L1918). The sign is a request whose stated benefit carries no number and no unit, and no one who can give one. This wiki reads it with [[incomparable-tasks]]: asking comes first ([[clarifying-questions]]), and what remains unquantified counts as no shown benefit, so it is neither ranked on a guess nor closed for that reason alone. Cohn's four headings for a return are new revenue, incremental revenue, retained revenue and operational efficiencies (L1950). This wiki reads the last two as the ones a small project usually has: what stops working for existing users if the work is not done, and effort avoided, stated roughly by the person steering.
- **Between two pieces of work with similar return, prefer the one that pays sooner.** "We cannot compare projects and make prioritization decisions by simply summing the total row of a worksheet" (L1920). This wiki recomputed Cohn's own illustration at 12% a year and found the reversed stream worth about 3% more, not "far less", so the mechanism stands and the size does not; on a small project timing arrives through [[cost-of-delay]], not through a discount rate.
- **Compare sets that fit one capacity, not single rows.** Of Cohn's three themes, custom reporting "could be combined with partner integration and done with the same cost as the overnight service theme" (L2324). By this wiki's arithmetic on Table 10.15 the pair sums to ¤64,546 of NPV against ¤46,341 for overnight alone, at the same ¤101,250.
- **Scarcity beats rate.** A 45% return on a small project that "ties up a critical developer" can lose to a 25% one needing the same developer: "You may choose to make more money by doing the second project, the one with the lower IRR." (L2258). This wiki reads the steering person's attention as the scarce resource here.

The capacity form of cost is this wiki's. Where money is not the deciding unit, the division behind cost per story point gives a share of capacity instead: an item of thirty points, against 120 points finished in the last twelve weeks, is a quarter of that stretch, or three weeks. The question becomes whether the item is worth three weeks of what could otherwise be done. It needs only board history, and it needs a point scale that stayed stable over the stretch; with no stable points there is no share to report.

## Agent executor note

This wiki reads value and cost as concerning the result and its price, so they survive. The two factors that need a closer look are knowledge and risk, because part of what Cohn counts depends on who the people are. See [[ordering-for-early-user-feedback]].

## Combining Prioritization Factors

This is Cohn's two-step procedure for turning the four *Prioritization Factors* (above) into one order ([[cohn-agile-estimating-planning]]). Cost and value set the position, and learning and risk adjust it.

### The procedure

1. Compare value with what the item would cost today: "This gives you an initial priority order for the themes. Those themes with a high value-to-cost ratio are those that should be done first." (L1821).
2. Then "think of the other prioritization factors as moving themes forward or backward." (L1823). Cohn's example is a medium-priority theme, due midway through the release, whose technology is very risky: "This would move the theme forward in priority and on the schedule." (L1827).

The source's summary repeats this: value and cost sort the themes into an initial order, and the other factors move them (L1875). The unit is the [[theme]].

The chapter's first step uses cost "today" (L1821). The way cost shifts over time is a separate judgement ([[cost-now-versus-cost-later]]), so this wiki treats it as one of the things that can move an item in step 2.

Chapter 22 restates the procedure as a guideline:

> Work on features in the order that optimizes the total value of the project. In addition to the value and cost of features when prioritizing consider also the learning that will occur and the risk that will be reduced by developing the feature.
>
> — [[cohn-agile-estimating-planning]], L4933

Its strength is modest. Early elimination of a significant risk "can often justify developing a feature early", and if a feature would give significant knowledge "about the product or their effort to develop it, they should consider developing that feature early." (L4933). This wiki reads the two kinds of knowledge as the two on [[ordering-for-early-user-feedback]]: about the product is end uncertainty, and about the effort is means uncertainty. Cohn's example fits, since finding out early that a third-party component cannot meet performance requirements (L4899) is cheaper than finding out late. That comparison of cost is this wiki's.

### Which way risk moves an item

Cohn's two statements point in different directions. A medium-priority risky theme moves forward (L1827), yet low-value, high-risk items are deferred "right out of the project" (L1817). The chapter's first discussion question poses this very case, a low-priority feature that might be dropped and needs a language nobody on the team knows, and leaves it for the reader (L1879).

This wiki resolves it with one test, and the test is ours: **will this item be built regardless?** If yes, its risk has to be met at some point, and meeting it early costs less, so risk moves it forward. If it could be dropped, dropping it removes the risk for nothing, so risk moves it back. On this reading the feature in the discussion question moves back. See *Risk-Value Quadrants* (below).

### Who moves an item, and the limit

The fictional case study in Chapter 23 (L4961) splits the two roles. It tells the product manager what happens at the next planning:

> The others may ask you to reconsider and move in one or two that they want to do because they’re risky or because they’ll learn a lot by doing them. But the ultimate prioritization decision will be up to you.
>
> — [[cohn-agile-estimating-planning]], L6211

The same division appears on [[value-order-versus-technical-necessity]], for sequencing. The case then gives its limit, from the other side:

> If the programmers were selecting a bunch of technical mumbo-jumbo or features you wouldn’t be able to see, I would have stopped that and had them work on other stories.
>
> — [[cohn-agile-estimating-planning]], L6215

This wiki reads that as a test with two outcomes. A task argued up for risk or learning, with a result the owner can be shown, goes to the owner to decide. A task with no result the owner can be shown also goes to the owner, with the risk or the knowledge it is meant to settle named; a preference for invisible work alone does not carry it, and where the task can be cut until it has a result to show, it is ([[vertical-slice]]). This wiki does not read the coach's line as stopping such work outright, because Cohn's own exposition moves invisible work up for knowledge alone: the LDAP stories "were moved up to around the middle of a project rather than being left near the end" (L1841-L1845), and the failure of infrastructure "may be enough to warrant moving development sooner than would be justified solely on the basis of value" (L1847). Infrastructure and spikes are handled on [[cost-now-versus-cost-later]] (its section on prioritizing infrastructure) and [[spike-as-last-resort]]. The case's first iteration passes that test: the rings story opens because "That’s our biggest risk." (L5686), and the product manager's reaction is "It is great to think that we’ll make so much visible progress so quickly." (L5935).

**The evidence is thin.** The case does not test the rule. The rings story was both the riskiest and a mandatory feature, so risk and value pointed the same way, and the source offers no way to trade one against the other when they diverge. That reading is this wiki's. It is also why the test on *Risk-Value Quadrants* (below) stays a judgement.

### Keeping it on paper

Cohn lets the procedure stay informal: "It can (and often does) take place entirely in the head of the product owner." (L1829). The team may then ask for small changes (L1829). This wiki does not keep that part. An order held in one head cannot be read back when it proves wrong. So the plugin writes, for each item that moved, the factor that moved it and the direction. Running the discussion itself is outside this base.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Value of each item | The person steering, or [[ordering-by-value-and-urgency]] |
| Cost today | The item's size, or its share of recent capacity (the capacity form in *Money Figures, When a Person Supplies Them*, above) |
| Whether doing it produces needed knowledge | [[ordering-for-early-user-feedback]], the task's open questions |
| Whether doing it removes a named risk | *Risk-Value Quadrants* (below) |
| Whether the item is certain to be built | The person steering |
| Whether its result can be shown | The task's acceptance ([[testable-acceptance]]) |

The source does not say what would show an order wrong, so these tests are this wiki's.

- **A forward move was wrong** if the risk or question named for it was not one that, had it gone badly, would have changed other work: nothing else rested on its answer. This tests the judgement available when the move was made. A risk retired early with no surprise is what a successful probe looks like, and is not by itself a sign that the move was wrong.
- **Failing to move an item was wrong** if a late item revealed a problem that forced finished work to be redone or dropped.
- **A backward move was wrong** if the deferred item turned out to be required and its risk arrived with no time left.

Two candidate signs follow, and both are this wiki's. A task carrying the plan's largest unverified assumption sits late in the order while work resting on it goes first. And a period's selection contains tasks whose results the owner could not be shown. A sign raises a question: the risk may be accepted knowingly.

### Cost

This wiki notes that the method is a judgement with no weights. Two people can apply it and reach different orders, and Cohn gives no rule for how far a factor may move an item. A written reason lets the result be checked, but it does not make it reproducible. A risky item placed early also delivers less value now, and if the risk does not materialise the value was deferred for nothing. Cohn leaves it at "consider" and "often" (L4933), so the weight comes from the case, and [[incomparable-tasks]] applies where it cannot be compared.

### Agent executor note

This wiki reads the procedure as concerning the order of results, so it survives. Writing down each move matters more here, because an agent has no memory of why an order was set unless the reason is on the board. The value input and the build-regardless answer stay with the person steering.

With a few people steering an agent, the owner and the builder may be one person. The split of authority then falls away and the visibility test stays, since an agent left to choose can also prefer invisible technical work. This wiki also expects an agent to make probes cheaper, which would favour trying a risky task early, though the result is only worth what the people steering can verify. No source measures this. Where the question can be answered without building a feature, see [[spike-as-last-resort]].

## Ordering by One Factor

This defect is an order that lets one input of the *Prioritization Factors* (above) decide. Cohn ([[cohn-agile-estimating-planning]]) describes the first two forms as the drawbacks of two opposite approaches (L1793). The signs are this wiki's derivation from those consequences. A sign raises a question, because either trace can have another cause ([[smell-is-not-a-finding]]).

### Value to the exclusion of risk

> a team that focuses on value to the exclusion of risk may develop a significant amount of an application before hitting a risk that jeopardizes the delivery of the product.
>
> — [[cohn-agile-estimating-planning]], L1793

**Sign:** finished work is mostly easy, high-value items, while the items with an unproven dependency are still open late in the period. Or a late item blocks or invalidates work already done.

**Check:** was the risky item's position decided, or was it merely never reached?

### Risk to the exclusion of value

> The risk-driven team accepts the chance that work they perform will turn out to be unneeded or of low value. They may develop infrastructural support for features that turn out unnecessary as the product owner refines her vision of the project based on what she learns from users as the project progresses.
>
> — [[cohn-agile-estimating-planning]], L1793

**Sign:** finished infrastructure has no feature using it, or features it was built for were later dropped or closed. Tasks that exist only to support other work outlive what they supported.

**Check:** was the supporting work tied to a feature that was still wanted when it was finished?

### Time without money

> Themes often seem worthwhile when viewed only in terms of the time they will take.
>
> — [[cohn-agile-estimating-planning]], L1740

This wiki reads this as a third form: a size is compared with a benefit without ever being turned into the same terms, so the comparison feels cheaper than it is. Cohn's remedy is to convert the size into money as a cost per story point (L1740). This wiki keeps the capacity form of that conversion, in *Money Figures, When a Person Supplies Them* (above).

**Sign:** an item was included on its size and benefit alone, and a higher-valued item was then left out for lack of capacity.

**Check:** what would the same capacity have bought instead?

### Why it happens

Cohn says money makes the first two factors dominate discussions (L1720). This wiki adds that an order can therefore look reasoned while two of its inputs were never asked for. This wiki's remedy is *Combining Prioritization Factors* (above), and *Risk-Value Quadrants* (below) for the first two forms. Ordering for the builders' convenience is a different fault, on [[order-by-value-not-convenience]].

### Agent executor note

The consequences concern work products, so this wiki reads them as surviving. Risk to the exclusion of value may be the likelier form with an agent, since this wiki expects supporting work to look cheap when an agent does it, but the source says nothing on this. Cheap construction would not remove the later cost of work nobody uses, because that cost is in [[cost-now-versus-cost-later]].

## Risk-Value Quadrants

This rule settles the "classic struggle" (L1791) between building what could derail a project and building what pays soonest. Cohn ([[cohn-agile-estimating-planning]]) refuses both extremes: "The solution, of course, is to give neither risk nor value total supremacy when prioritizing." (L1795).

### What counts as a risk

Cohn defines a risk as "anything that has not yet happened but might and that would jeopardize or limit the success of the project" (L1781). He lists schedule risk, cost risk and functionality risk, and also divides risks into technological and business (L1783-L1791). His signs of a high-risk feature are reliance on "unproven technologies, integration with unproven sub-contractors, technical innovation (such as the development of a new algorithm)" (L1795).

### The sequence

| Value | Risk | Cohn's label | Why |
|---|---|---|---|
| High | High | Do first | "These features deliver the most value and working on them eliminates significant risks." (L1806) |
| High | Low | Do second | Equal value and less risk, so they "can therefore be done later in the schedule" (L1806) |
| Low | Low | Do last | "they will have less impact on the total value of the product if they are dropped and because they are low risk" (L1815) |
| Low | High | Avoid | "There is no reason to take on a high degree of risk for a feature of limited value." (L1817) |

The quadrant labels are from Figure 9.3 (L1811). The rule in a sentence is his: "use the guideline to work first on high-value features but use risk as a tie-breaker." (L1806).

This wiki notes what the table implies. Value is the primary sort; risk breaks ties and, for an item certain to be built, can move it forward across bands, as Cohn's own medium-priority example does (L1827; *Combining Prioritization Factors*, above). For a low-value item that could be dropped, risk is a reason to drop it rather than to raise it, so its direction flips with value: it pulls an item that will be built forward and pushes one that need not be built out. Cohn's instruction for the last row is "Try to defer low-value, high-risk items right out of the project." (L1817). The test that decides between the two directions, whether the item will be built regardless, is in *Combining Prioritization Factors* (above).

### Positions change

"Be aware that a feature’s risk and value profile changes over time." (L1817). Cohn's example has a slip: he places a low-value, low-risk feature in the Avoid quadrant, which Figure 9.3 gives to low-value, high-risk items (L1811, L1817). This wiki reads the point as surviving the slip: a feature set aside today can become the next thing to do once everything above it is finished. So a rating expires, as a [[cost-of-delay]] rating does.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Value band | The person steering, or [[ordering-by-value-and-urgency]] |
| Named risk: what might happen and what it would stop | The task's text, the design it came from, or the person steering |
| Whether doing the work settles the risk | The task: does it exercise the unproven thing? |
| Date of the rating | Board history |

This wiki adds that a risk band needs a named event, because a bare sense that something is hard gives nothing to check later. The tests below are this wiki's, since the source states none.

- **Risk was overrated** if the event named for it would not, had it occurred, have changed any other work. A high-risk item that finished with no surprise is not by itself evidence of overrating: a risk retired early is what doing it first was for.
- **Risk was underrated** if a low-risk item stalled, or changed the plan for other work.
- **Avoid was wrong** if a deferred item proved necessary and its risk arrived late in the work.

### Cost

Doing high-risk work first means accepting what Cohn says of a risk-driven team: "work they perform will turn out to be unneeded or of low value" (L1793). This wiki notes that restricting that to high-value items reduces the exposure and does not remove it, since the value rating may itself be wrong. The ordering also leaves the easy, high-value wins until second, so visible progress can come later.

### Agent executor note

This wiki reads the rule as concerning results, so it survives. What changes is the reading of risk. This wiki reads "unproven technologies" (L1795) in Cohn's setting as partly meaning unproven for these people. With an agent, this wiki reads the question as whether the thing has been shown to work in this system, not whether anyone present has done it before. That transfer is ours, and the source does not test it.

## A Trade-Off Needs Cost and Benefit

Cohn's rule is that a trade-off cannot be decided on one side of the ledger:

> In order to make these decisions we need estimates of both the costs and benefits.
>
> — [[cohn-agile-estimating-planning]], L447

The decisions he means are of the form: is a feature worth delaying the release, should the release be held for more features, should a tool be bought (L447). He says "Many of the decisions made while planning a project are tradeoff decisions." (L445).

### Inputs and where they are read

This wiki's reading, since Cohn states the rule without a procedure:

- **Cost:** the task's estimate, as a range where the work is unresolved. See [[forecast-range-and-probability]].
- **Benefit:** the value stated in the task's purpose or by whoever requested it ([[task-must-justify-itself]]). Chapter 1 gives no benefit scale; the bands this wiki uses when value cannot be put in numbers are on [[ordering-by-value-and-urgency]].
- **Scarce people:** Cohn says "Sometimes the staffing profile of a project can be more important than its schedule." (L439). His example is a project worth starting only if a plan avoids the fully committed chief architect (L439). This wiki reads that, for a few people steering an agent, as: the steering person's attention can be the scarce input, not the agent's capacity.

**What later fact would show the choice wrong.** A chosen item delivered little of the value claimed for it, or a deferred one kept returning as a request.

### How much of a feature

Estimates also size a feature, not only rank it:

> Rather than investing twenty days and getting everything, perhaps ten days of effort will yield 80% of the benefit.
>
> — [[cohn-agile-estimating-planning]], L451

This wiki reads the numbers as an illustration, since Cohn writes "perhaps" and reports no measurement. It keeps the mechanism: a task can be compared against a cheaper version of itself, which also feeds decomposition ([[story-splitting-patterns]]).

### The precondition

> Customers are reluctant to make these types of tradeoff decisions early in a project unless the developers’ estimates have proven trustworthy.
>
> — [[cohn-agile-estimating-planning]], L451

Cohn states this as reluctance, not as a gate. This wiki reads it as saying that a comparison by cost carries weight with the person deciding only as far as the estimates' record does, so a record that fails [[good-plan-test]] weakens the comparison without forbidding it. In this setting the person steering plays the customer's role.

### Failure sign

This wiki's question to check: tasks ordered with size recorded but no statement of what each is for, or the reverse, tasks ordered by claimed importance with no size. Either way the comparison had one side. The charter does not accept an omission as the sign of a rule that chooses, so this only supports the later-fact test above, and it is no proof of a bad order: a board cannot show a wrong order directly.

### Trade-off

This wiki notes that a rough benefit estimate on every task costs effort and can give false confidence. Chapter 1 does not say how rough is acceptable; it shows only that a comparison made without both sides is not one. Where the benefit is expressed as a rate and durations vary widely, the comparison is made on [[cost-of-delay-over-duration]]. See also [[planning-horizons]].
