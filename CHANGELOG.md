# Changelog

## 0.2.0

- Each `SKILL.md` now holds only what the assistant needs to act: a grade, a Do line and a Check line per rule, with notes where popular advice is wrong. Findings and citations moved to `references/evidence.md`, one block per rule.
- Each skill decides whether it is designing or reviewing before it starts.
- Skills moved into `skills/`. Added plugin and marketplace manifests for Claude Code.
- Added `dist/`: a plain single-file version of each skill, and a combined checklist.
- Added `scripts/build.py`, `scripts/check.py` and an automated check on pull requests.
- Added `ux-patterns` and `ux-writing`. Added an inclusive design section to `ux-accessibility`.

## 0.1.0

- First versions of `ux-psychology`, `ux-ethics` and `ux-accessibility`.
