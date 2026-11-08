---
title: A class interface presents one coherent abstraction
category: objects
summary: "A class's public methods serve unrelated purposes (command stack + report printing + global data init), or groups of methods each touch a disjoint half of the fields, or validators of another concept's values have been bolted onto a domain class."
tags: [rule, cohesion, abstraction, class-interface, maintenance]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-07
---

## Rule

A class's public interface should be a group of methods that clearly belong together: ideally the implementation of exactly one [[abstract-data-type]]. If a class implements more than one ADT, or you cannot say which ADT it implements, McConnell's advice is to reorganise it into one or more well-defined ADTs (p. 131). Related guidance from the same section:

- **Move unrelated information to another class.** If some methods work with one half of the data and others with the other half, there are two classes posing as one: «Разделите их!» (p. 134).
- **Beware of eroding the interface under modification.** Functionality discovered during maintenance often fits the original interface poorly but is hard to put elsewhere. McConnell's `Employee` grows `IsZipCodeValid`, `IsPhoneNumberValid` and `GetQueryToCreateNewEmployee`. Validation of zip codes has no logical link to employees, and the SQL methods sit at a much lower level than the class (pp. 134-135).
- **Do not add public members inconsistent with the abstraction.** For each new method ask whether it fits the abstraction of the existing interface. If not, find another way to make the change (p. 135).
- **Consider abstraction and cohesion together.** A good abstraction usually has high cohesion, and the converse holds more weakly. McConnell reports getting better designs by focusing on the abstraction than on [[cohesion]]. When a class has low cohesion and you do not know how to fix it, ask whether it presents a consistent abstraction (p. 135).

Weisfeld's *The Object-Oriented Thought Process* reaches the same split from composition, under the name of mixing domains. Composed objects should not depend heavily on each other, and mixing domains is one way to make them do so: «Объект в одном домене не должен смешиваться с объектом в другом домене за исключением определенных ситуаций» (p. 187). In his stereo, a receiver and a CD player in separate domains let a broken player go for repair alone while the rest keeps working, and let it be replaced by another maker's (pp. 183-184, 187). He does not make this absolute: a combined TV and VCR is a legitimate convenience, the choice is between convenience and stability, and «Одного правильного ответа не существует» (p. 187). The integrated unit is preferable where its benefits outweigh the risk and the downtime of the separate parts (p. 188). His reason for leaning towards separation is that preferences in technology change fast, VCR then DVD then streaming (p. 187). The concept under the split is [[near-decomposability]].

The test is applied to public methods only. A class with a good overall abstraction can still contain individual methods that are poor abstractions; that is judged per routine (p. 131).

## Sign in code

- Public methods fall into clusters that share no fields and do not call one another. McConnell's `Program` class has `PushCommand`/`PopCommand`, `FormatReport`/`PrintReport` and `InitializeGlobalData` side by side (p. 130).
- Two groups of methods each read and write a disjoint subset of the fields (p. 134).
- A domain class exposes validation of values that belong to another concept (`IsZipCodeValid` on `Employee`) (p. 134).
- A class name joined with "and" is a prompt to look for the clusters above. This prompt is this wiki's own heuristic; a name with a doer suffix is reported on [[name-classes-for-what-they-are]].

This wiki assigns the neighbouring cases as follows. This page owns a class whose public methods serve different purposes; [[mixed-abstraction-levels-in-interface]] owns a class whose methods serve one purpose at two levels, domain and mechanism. A fragment where both the purposes and the vocabularies differ goes first to this page. Persistence methods or SQL on a domain class are [[delegate-to-services]]; this page owns validators of another concept's values. A split of the fields into groups used by disjoint methods is owned by [[class-interface-coherent-abstraction]] at any method count; [[fewer-than-five-public-methods]] owns the count and applies that page's split. Dozens of methods of one class writing the same field are [[class-data-versus-global-data]]. A count of public methods alone, with no split in purpose, is [[class-size]] or [[fewer-than-five-public-methods]]. Where a class whose public methods serve unrelated purposes is the one that receives the program's incoming requests or system operations, [[controller]] owns it; any other such class is [[class-interface-coherent-abstraction]].

## When not to apply

- A facade or application entry point whose purpose is to expose a few high-level operations, each delegating to its own class. McConnell's repaired `Program` keeps `InitializeUserInterface` and `InitializeReports` together (p. 131); this wiki reads that as one abstraction, starting the program, and the facade limit is this wiki's own.
- The combination is the product: callers always use both halves together and none needs one half alone or a replacement for it. That is Weisfeld's TV/VCR convenience (p. 187); this wiki reads it as one abstraction whose name joins two nouns, and checks it against the callers in view.
- Clusters that share an invariant over the same fields are one abstraction even if their names look unrelated. Check shared state before splitting. This limit is this wiki's own.

## Repair

1. Group the public methods by the data they touch and the purpose they serve.
2. Move each foreign cluster to a class whose abstraction it fits. Validators go to the value type they validate.
3. Turn methods that serve only the class's own high-level operations into private helpers (p. 131).
4. Re-read the remaining public list and check that every method serves one purpose.
5. Where callers want one handle on both halves, keep a thin class that holds the split parts and delegates, so each part stays replaceable (after Weisfeld's stereo, pp. 183-184; the step is this wiki's own).

## Before and after

```
// before
class Program
  pushCommand(c); popCommand()
  formatReport(r); printReport(r)
  initGlobalData(); shutdownGlobalData()
```

```
// after
class Program
  initUserInterface(); shutDownUserInterface()
  initReports(); shutDownReports()
class CommandStack
  push(c); pop()
class Report
  format(); print()
class GlobalData
  init(); shutdown()
```

Two domains in one class (after Weisfeld's stereo, whose receiver and CD player he keeps apart, pp. 184, 187):

```
// before
class StereoUnit
  field band, volume
  field track, isSpinning
  tune(b); setVolume(v)       // touch band, volume
  play(); eject()             // touch track, isSpinning
```

```
// after
class Receiver
  tune(b); setVolume(v)
class CdPlayer                // another maker's player can stand here
  play(); eject()
class Stereo                  // only if one handle is wanted
  constructor(receiver, player)
  playDisc()
    receiver.tune(CD_INPUT); player.play()
```

## Related

- [[minimize-member-accessibility]]
- [[provide-opposite-operations]]: the other completeness check on a class interface.
- [[abstract-data-type]]

## Source

[[code-complete]], ch. 6.2, Russian edition, pp. 129-135. The "and" naming prompt, the owner assignments, the reading of the repaired `Program` as one abstraction, the facade and shared-invariant limits, the `GlobalData` class in the pair and the pseudocode are this wiki's own reasoning. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 9: the stereo as integrated against modular (pp. 183-184), avoiding dependencies, mixing domains, convenience against stability (p. 187), the boxed note (p. 188). The quotations were checked against `raw/`. This wiki's own for that part: reading mixing domains as this page's disjoint-fields sign, the convenience limit as worded, repair step 5 and the `StereoUnit` pair; the book gives only device analogies and no code.
