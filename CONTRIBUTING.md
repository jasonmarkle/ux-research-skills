# Contributing

Corrections, new rules and better guidance are welcome. The rules below keep the skills accurate, small and free for anyone to use.

## Before you open a pull request

```
python scripts/build.py     # regenerate dist/
python scripts/check.py     # must report 0 errors
```

The same check runs automatically on every pull request. If you use Claude Code, `claude plugin validate .` also checks the plugin manifests.

## Ground rules

1. **Cite the original source.** Every graded rule needs at least one primary publication, standard or peer-reviewed review. Blog posts and other collections of design principles are not acceptable as the basis for a rule. Industry studies may be cited if labelled as such.
2. **Write in your own words.** Do not copy or closely paraphrase papers, books, websites or standards. Refer to a standard by its criterion number and official name, and describe the requirement yourself.
3. **Check the citation** against the publisher's page or a library record: authors, year, title, venue.
4. **Grade honestly.** If you know of failed replications or a meta-analysis that weakens a finding, say so and cite it. Framework is the right grade when no controlled study exists.
5. **Do not add manipulation.** Guidance must serve the user. Techniques that mislead or pressure people belong here only as things to avoid.

## Where things go

A rule lives in three places inside its skill folder.

**1. `SKILL.md`**: what the assistant should do. No citations and no study descriptions.

```markdown
**Plain descriptive name** · Grade
- Do: what to do when designing.
- Check: observable symptoms when reviewing.
- Note: only if popular advice on this is wrong, or a condition limits the rule.
```

Other allowed lines: `Caution`, `Ethics`, `Rules`, `Requirement`, `Formula`, `Use when`, `Avoid when`, `See also`, `Verify`. Anything the assistant needs in order to act correctly (a threshold, a boundary condition, a correction) must be here, because this is often the only file it loads.

**2. `references/evidence.md`**: why. One block per rule, with the same name and grade, in the same order.

```markdown
### Plain descriptive name
- Grade: Grade
- Finding: what the research found, including where it stops applying.
- Sources: Author Year; Author Year
```

A rule with no study behind it gets `- Basis: established practice; no study cited.` instead of Finding and Sources.

**3. `references/sources.md`**: the full reference for each source.

## Grades

| Grade | Meaning |
|---|---|
| Strong | Replicated, including in applied settings |
| Moderate | Real effect, with boundary conditions or limited evidence in interfaces |
| Contested | Failed replications, mixed results, or disagreement among the people concerned |
| Framework | Established practice or a useful way of thinking, not an experimental finding |

A grade may carry a short qualifier, such as "Strong in the lab, Moderate for menus". In `ux-accessibility`, most rules carry a WCAG success criterion and level instead of a grade.

## Which skill

- `ux-psychology`: how people perceive, remember, decide and act.
- `ux-ethics`: how design can work against people, and what to do instead.
- `ux-accessibility`: what people with disabilities need from each layer of a design. Check every number against the current standard.
- `ux-patterns`: concrete solutions to recurring interface problems.
- `ux-writing`: the words in an interface. Where the people described disagree about a term, grade it Contested.

## Size

Keep each `SKILL.md` under 500 lines and, where possible, under about 5,000 tokens. The check warns above that and fails above about 6,000. If a skill outgrows the budget, shorten before splitting.

## Naming

Name rules by what they describe ("Pointing time", "Defaults") so they are understandable without knowing an eponym. Put the researcher's name in the sources.

## Versions

When a change alters what a skill tells the assistant to do, raise `metadata.version` in that skill's frontmatter and the version in `.claude-plugin/plugin.json`, and add a line to `CHANGELOG.md`.

## Corrections

If a citation is wrong, a finding is misdescribed, or newer research changes a grade, open an issue or pull request with the source that shows it. Corrections are the most valuable contribution.

## Licence of contributions

By contributing you agree that your contribution is your own original work and is released under the MIT licence in this repository.
