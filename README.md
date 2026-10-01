# ux-research-skills

Five skills that help an AI assistant design and review interfaces, built from published research and standards. They follow the open [Agent Skills](https://agentskills.io/specification) format, so they work in Claude Code, the Claude apps and other agents that read that format, and each one is also provided as a plain file for tools that do not.

| Skill | Use it for | Covers |
|---|---|---|
| [`ux-psychology`](skills/ux-psychology/SKILL.md) | Making an interface easy to understand and use | Perception, attention, memory, decisions, movement, waiting, motivation, learning |
| [`ux-ethics`](skills/ux-ethics/SKILL.md) | Making an interface honest, fair, inclusive and safe | Deceptive patterns, consent and privacy, pricing and subscriptions, attention, inclusion, misuse, honesty about automation |
| [`ux-accessibility`](skills/ux-accessibility/SKILL.md) | Making an interface usable by people with disabilities | WCAG 2.2 AA by design layer, and inclusive design |
| [`ux-patterns`](skills/ux-patterns/SKILL.md) | Choosing the right component or layout for a problem | Navigation, forms, tables and filters, loading, errors, empty states, dialogs, onboarding, small screens |
| [`ux-writing`](skills/ux-writing/SKILL.md) | Writing interface text people understand and can act on | Plain language, naming, instructions, errors and confirmations, inclusive language, numbers, translation |

Each skill works alone. Together: psychology explains how people behave, ethics sets limits, accessibility makes the result work for everyone, patterns turns that into components, and writing covers the words.

## How each skill is built

```
skills/<name>/
  SKILL.md                  the rules the assistant follows
  references/evidence.md    the finding and sources behind each rule
  references/sources.md     full references
```

- **`SKILL.md` is the only file the assistant needs.** Every rule has a grade, a **Do** line for designing and a **Check** line for reviewing, plus a note where popular advice is wrong. It contains no citations, which keeps it small: about 3,000 to 5,700 tokens each.
- **`evidence.md` is for people, and for reviews.** It holds one block per rule with the finding and its sources. The assistant opens it when a review finding needs backing or when someone asks why a rule exists.
- **Grades** say how far to trust a rule: Strong, Moderate, Contested or Framework. Contested rules are presented as open questions, not facts.
- **Designing and reviewing are separate tasks.** Each skill decides which one it is doing first, and uses the matching lines.

## Using the skills

### Claude Code

Install all five as a plugin:

```
claude plugin marketplace add <owner>/ux-research-skills
claude plugin install ux-research-skills@ux-research-skills
```

They then appear as `ux-research-skills:ux-psychology` and so on. To use a single skill without the plugin, copy its folder into `.claude/skills/` in a project, or `~/.claude/skills/` for yourself.

### Claude apps

Zip a skill folder (for example `skills/ux-writing/`) and add it as a skill. On Team and Enterprise plans an organization owner can provide it to everyone; see [Anthropic's help article](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization).

### Other agents that read Agent Skills

Point the agent at the folders in `skills/`. Nothing in them is specific to Claude.

### Tools without skill support

`dist/` has a plain single-file version of each skill with no frontmatter. Paste one into a rules file, project instructions or a system prompt.

`dist/ux-checklist.md` is the shortest form: the closing checks from all five skills, about 1,200 tokens. Use it where the instruction budget is small.

### Design tools

When an agent is connected to a design tool, for example through Figma's MCP server, the skills run in the agent and apply to whatever it reads from or writes to the design. Where a tool only accepts a rules or guidelines file, use the files in `dist/`.

## What makes these different

- **Sourced from the original research and standards**, not from other collections of design principles.
- **Evidence-graded**, so well-replicated results are not mixed up with popular claims that did not hold up.
- **Checked.** Each reference, claim and success criterion was compared against the published record, and wording was corrected where it overstated a source.
- **Honest about limits.** The accessibility skill marks what can be judged from a mockup and what needs a built page. Laws are named as pointers only. None of this is legal advice.

## Repository layout

```
skills/                    the five skills
dist/                      generated single-file versions and the combined checklist
scripts/build.py           regenerates dist/
scripts/check.py           validates every skill; run before opening a pull request
.claude-plugin/            plugin and marketplace manifests for Claude Code
.github/workflows/         runs scripts/check.py on every pull request
CONTRIBUTING.md            how to add or correct a rule
CHANGELOG.md
LICENSE                    MIT
```

## Planned

- `ux-experiments`: how to test a design claim before relying on it.

## Independence and originality

The skills were written from the primary research literature and published standards, in original wording and with their own selection and structure. They are not derived from any other published collection of design principles. Findings belong to the scientific record and are credited to their authors in each `evidence.md`. Standards are referred to by criterion number and official name and described in original words; the standards themselves remain the authority.

## Licence

MIT. Use it, change it and redistribute it, including commercially, as long as the licence notice is kept.
