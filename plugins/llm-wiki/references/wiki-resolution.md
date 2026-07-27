# Wiki resolution

How any skill, script, or the [`wiki-keeper`](../agents/wiki-keeper.md) agent finds *which*
wiki it is operating on. This is what makes "one convention, many wikis" work: many wikis
coexist as many `SCHEMA.md`-rooted directories, and resolution picks the right one from the
current location.

## The rule

**The directory containing `SCHEMA.md` is the wiki root.** To resolve:

1. Start at the current working directory.
2. If it contains `SCHEMA.md`, that directory is the wiki root. Done.
3. Otherwise move up one directory and repeat.
4. **Mandatory stop.** Never ascend into — or treat as a candidate — the user's home
   directory or a filesystem/drive root (`/`, `C:\`, `~`). If the walk reaches that boundary
   without finding `SCHEMA.md`, the answer is **"not in a wiki"**. Never search from, or
   create a wiki at, a home/drive root — that is how a wiki accidentally swallows an entire
   machine.

## Outcomes

| Result | Meaning | What callers do |
|--------|---------|-----------------|
| **Found** | wiki root = the dir with `SCHEMA.md` | proceed, reading [`SCHEMA.md`](../assets/SCHEMA.md.template) as the charter |
| **Not found** | cwd is not inside any wiki | hooks **no-op (exit 0)**; skills offer to initialize a new wiki from [`assets/`](../assets) templates |

## For scripts

The bundled scripts accept an `--auto` flag: self-resolve the wiki root from the current
directory using the rule above, and **exit 0 silently if not in a wiki**. This is why the
[Stop hook](../hooks/hooks.json) can run on every session without effect unless you are
actually inside a wiki.

## Multiple wikis

Nothing is global. A machine can hold any number of independent wikis — each is just a
directory with its own `SCHEMA.md`. A domain-expert agent points at its own wiki simply by
working from (or passing) a path inside it; resolution does the rest. There is no registry and
no single "main" wiki — every wiki is independent and equal.
