---
title: Anticipate likely changes
category: change
summary: "Method for placing interfaces: list what is likely to change (business rules, hardware, I/O formats, non-standard language features, hard design areas, status variables, sizes), give each its own class, keep the class interface free of it; effort inversely proportional to probability. Review form: find where each area's decisions are made."
tags: [method, change, information-hiding, isolation, interfaces, versioning]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell calls accommodating change one of the hardest parts of design and frames its goal as isolating unstable areas, so that the effect of a change stays inside one routine, class or package (p. 94). The method comes from Parnas (1979). This wiki reads it as [[information-hiding]] applied to secrets that hide sources of change.

*Code Complete* also names version numbers in data files and fields reserved for the future as a simple way to prepare for a change of format (p. 49). Where the boundaries between subsystems fall is the project's architecture and is taken as given; this method works on the classes inside them.

## The three steps

1. **Identify items likely to change.** Good requirements list potential changes with their likelihood; when they do not, use the list of usual areas below (p. 94).
2. **Separate them.** Give each volatile item its own class, or group volatile items likely to change together (p. 94).
3. **Isolate them.** Design the interfaces between classes to be insensitive to the potential change, so a change stays inside the class and is invisible to the others (p. 94).

## Areas the book says change most often

- **Business rules**, such as tax law or contract terms; hidden, they sit in one corner until it is time to change them (pp. 94-95). See [[business-rules-are-metadata]].
- **Hardware dependencies**: screens, printers, devices. The book allows a separate subsystem or a separate class; this page takes the class, and where a subsystem boundary falls is the project's architecture. Isolating them also lets work proceed against a simulated device until the real one is stable (p. 95). See [[isolate-volatile-dependencies-behind-a-layer]].
- **Input and output**: file formats the application owns, and the user-level layout of fields; the book advises reviewing every external interface for likely change (p. 95).
- **Non-standard language features and environment-specific library calls**: hide them in a class that can be swapped when porting (p. 95). See [[isolate-volatile-dependencies-behind-a-layer]] and, for a vendor's product, [[hide-third-party-apis]].
- **Difficult design and construction areas**: they are often reimplemented, so a bad first attempt must not spread (p. 95).
- **Status variables**: see [[status-variable-as-enumeration]].
- **Data-structure sizes**: see [[hide-secrets-behind-one-access-point]] (p. 96).

## Scaling the effort

The book: «проектируйте ее так, чтобы влияние изменений было обратно пропорционально их вероятности» (p. 96). A likely change must be easy; a wide impact across several classes is tolerable only for a very unlikely one. Cost of anticipating counts too: an unlikely change that is cheap to plan for may deserve more attention than a likely one that is hard to plan for (p. 96).

To find the areas, the book suggests defining first the minimal subset users need, the core, which is unlikely to change, and then the smallest increments on top of it, including quality changes such as thread safety and localisation. The increments are the potential changes, to be designed with information hiding (p. 96).

## Where this stops

The book's cross-reference states that this approach does not mean designing or writing code in advance (p. 96, pointing to section 24.2). This wiki resolves the apparent conflict with [[replaceable-code-over-forecast]] by setting. Placing an interface boundary around code already being written, so a likely change stays inside one class, is [[anticipate-likely-changes]] and adds no code; a hook, parameter or registry added for a change that has not come is [[replaceable-code-over-forecast]]. Making every constant configurable is not this method either; see [[over-configuration]].

## Running it against code

This wiki's procedure for a review: for each area above that the code touches, find where its decisions are made. If they are made in more than one class or routine, or appear in a public signature (a file format's field order in a public method, a device call inside a routine that computes business results), the area is not isolated, and the finding belongs to the page that owns that shape:

- the same value or case list as literals or branches in several routines: [[dry]] or [[business-rules-are-metadata]];
- a chain of four or more branches mapping a key to constants: [[drive-repeated-dispatch-from-a-table]];
- a value that needs a rebuild to change: [[parameterize-with-external-configuration]];
- a persisted or exchanged format with no version marker, while the code already branches on an old and a new layout: this method's own finding, repaired by adding a version field (p. 49), and see [[plain-text-for-persistent-data]].

## Source

[[code-complete]], Russian edition, ch. 5, section 5.3, pp. 94-96, and ch. 3, section 3.5, p. 49, for version numbers and reserved fields in data files. The reading as information hiding for sources of change, the choice of the class over the subsystem, the resolution against [[replaceable-code-over-forecast]], the review procedure and its routing to owner pages, and the version-marker finding as a check against code are this wiki's own.
