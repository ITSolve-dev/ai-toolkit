---
title: "Transitions of a state machine: every state reachable, conditions from one state consistent and complete"
category: types-and-state
summary: "In one state's handler, two branches whose conditions can both be true at once (outcome decided silently by textual order or by which assignment runs last), a branch chain with no fallback so some input falls through with no defined transition, a fallback spelled as the negation of every other condition, or a state value that no transition ever assigns."
tags: [rule, state-machine, automata-based-programming, conditions, completeness, reachability, static-check]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

The set of conditions on the transitions leaving one state of a state machine should be **consistent** (non-contradictory) and **complete**. Consistent means that for no input are two conditions true at once. Complete means that for every input at least one condition is true. Polikarpova and Shalyto define both properties (p. 70, footnotes 9-10). A transition graph that breaks the first is «некорректным» (p. 70): at run time the automaton «не сможет определить, по какой из дуг ему перейти». They give two notational repairs. **Priorities** settle a contradiction explicitly. The **«иначе»** (else) arc guarantees completeness.

Chapter 4 returns to the same graph as a correctness check and adds a third property. Reachability, consistency and completeness are behavioural properties that are «несложно проверить по графу переходов автомата», and the authors say these checks remove errors «которые было бы трудно обнаружить без использования автоматного подхода» (p. 138). They apply to any code shaped as `switch (state)` with guarded transitions, hand-written or generated.

Why the order of an `if / else if` chain matters at all is on [[spontaneous-and-guarded-transitions]]: a diagram checks the conditions leaving a state at once, a chain checks them one after another (p. 22).

## Rule

For the whole graph, check reachability (pp. 138-139). A path of transitions must lead from the initial state to every state. Otherwise the state «не имеет смысла, так как автомат никогда не сможет в нем оказаться». An unreachable state does no harm by itself, but it «скорее всего, свидетельствует об ошибке при построении автомата». Below the three behavioural properties the source puts a syntactic one: every transition must lead from a state to a state (p. 138).

For each state, check its outgoing conditions together, not one at a time:

- **Contradiction.** If several conditions can hold at once, either make them mutually exclusive or give the arcs an explicit priority. The arc with the higher priority is checked first. Arcs of equal priority are allowed only if they do not contradict each other (pp. 69-70).
- **Incompleteness.** If some input satisfies no condition, add a transition for "none of the others". The source rejects two ways of writing it. One is the negated disjunction of all the other conditions, which is bulky and, in the book's words, such bulky conditions «покушаются на святая святых автоматного программирования – наглядность» (p. 70). The other is an unconditional arc with the lowest priority. That arc forces priorities onto every other arc, and its priority must be renumbered whenever arcs change. The source prescribes an explicit **else** instead. It fires only when every other condition from that state is false: «Это его свойство сохраняется при добавлении любых новых дуг и любом изменении приоритетов» (p. 70).

Chapter 4 restates the two per-state properties (pp. 138-139). With the usual implementations one of two overlapping transitions is taken, but which one «невозможно определить по диаграмме»; the source calls this nondeterminism useless and usually a sign of error. Without completeness, «во время выполнения может сложиться ситуация, когда автомат не сможет совершить переход», and the whole model breaks.

The source cites the valve automata's self-loops, which carried exactly such a negated disjunction, as the case this construct removes (p. 70; [[event-driven-vs-polled-state-machine]]).

## Sign in code

This wiki's own translation of the diagram properties into code:

- Inside one state's case arm, a sequence of independent `if` statements, each of which can change the state. Two of them can match the same input, and the final state depends on which assignment runs last.
- An `if / else if` chain whose conditions overlap. The order silently acts as the priority, and nothing marks it as deliberate.
- A state's branch chain that ends with no `else`, so some input leaves the machine with no defined behaviour. Or a final branch spelled as the negation of all the preceding conditions, `if not (a or b or c)`, which must be edited every time a branch is added. The same holds for a transition table with a missing cell.
- A value of the state enumeration, or a `case` label, that no assignment `state = X` makes, or that only an unreachable state assigns.

This wiki assigns the shape as follows: overlapping guards, or a missing fallback, among the transitions leaving one state are [[transition-conditions-consistent-and-complete]]. A missing or hand-negated stay case in a polled machine is [[transition-conditions-consistent-and-complete]]. The same transition copied into several states is [[state-grouping-for-shared-transitions]]; inputs tested before the state is selected are [[state-machine-as-switch-on-state]]. A `switch` on a state machine's state variable with no `default` is [[default-branch-catches-the-unexpected]]; a state whose guards leave some input with no transition is [[transition-conditions-consistent-and-complete]].

## When not to apply

- Not every chain needs an `else`. In the source's own template a Moore machine's self-loop needs no branch (p. 81): a chain without `else` that leaves the state unchanged is a defined stay, not a gap, and so is any implicit fall-through that the language or a project convention makes a stay. This wiki reads the sign as firing only where an unmatched input does something other than stay, or where the machine is meant to report it. Marking a stay (an `else` that keeps the state, or a comment) remains this wiki's preference.
- Overlapping conditions are not a defect where the priority is the intended semantics and the order is the documented priority (the source allows priorities as a legitimate tool, pp. 69-70). The sign is an overlap nobody chose, not overlap as such.
- **The control object has a specification that rules inputs out.** The source says the checks are formal and ignore what the input variables mean, which is usually enough; but if the specification says, for example, that some inputs can never be true together, «Такая информация способна повлиять на результаты проверки всех трех перечисленных свойств» (p. 139). Two guards that overlap only on an input combination the specification forbids are not a consistency defect. This wiki adds that the exclusion should then be stated where the guards are, for example as an assertion.
- Outside an explicit state machine (ordinary validation chains, for example), this page does not own the shape. It applies only where branches select a next state.

## Repair

1. List the conditions leaving the state and check them pairwise for joint satisfiability.
2. For each overlap, either narrow a condition so the two exclude each other, or state the priority: an ordered `if / else if` chain with a comment that the order is the priority.
3. Replace a hand-written negated disjunction with a final `else`, so that adding a branch later does not require editing the fallback.
4. Make the `else` say what happens: stay, go to a fault state, or report.
5. For an unreachable state, add the missing transition into it, or delete the state and its `case`.

## Before and after

```
// before: two ifs can both fire; the fallback restates every other condition
case OPENING:
    if sensor_open: state = OPEN
    if timeout: state = FAULT          // sensor_open and timeout together -> last one wins
    if not (sensor_open or timeout): state = OPENING
```

```
// after: priority is explicit, the fallback survives new branches
case OPENING:
    // order is the priority: a confirmed open beats a timeout
    if sensor_open: state = OPEN
    else if timeout: state = FAULT
    else: state = OPENING             // nothing happened yet: keep waiting
```

Reachability, on the whole switch:

```
// before: nothing ever assigns PAUSED
switch state
  case IDLE:    if start: state = RUNNING
  case RUNNING: if stop: state = IDLE
  case PAUSED:  if resume: state = RUNNING
```

```
// after: PAUSED is entered from RUNNING, every chain ends in an explicit else
switch state
  case IDLE:    if start: state = RUNNING
                else: stay                  // IDLE ignores other input
  case RUNNING: if stop: state = IDLE
                else if pause: state = PAUSED
                else: stay
  case PAUSED:  if resume: state = RUNNING
                else: stay
  default:      fail "unknown state"
```

## Source

- Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]). The properties of contradiction and completeness, p. 70, footnotes 9-10. Priorities on arcs and smaller numbers checked first, pp. 69-70. The case for an «иначе» arc over a negated disjunction or a lowest-priority unconditional arc, p. 70. Sequential against simultaneous checking, p. 22. A Moore self-loop needing no branch in the template, p. 81.
- The same book, ch. 4.2, pp. 138-139: reachability, consistency and completeness as checks on the graph, the syntactic rule, and the limit from the control object's specification.
- This wiki's own: the signs in code (independent `if` statements, an overlapping `else if` chain, a negated-disjunction fallback, a state value never assigned), the assignment of neighbouring shapes, the limits other than the specification one, the repair and the pseudocode. The source states these properties for transition diagrams, not for code, and does not say how to repair a violation.
