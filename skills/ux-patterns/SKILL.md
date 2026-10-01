---
name: ux-patterns
description: Choose and apply proven interface patterns for navigation, forms, tables, filters, loading, errors, empty states, dialogs, onboarding and mobile layouts, with an evidence grade for each. Use when designing or reviewing any screen or flow and deciding which component or layout to use, or when asked which of two patterns is better.
license: MIT
metadata:
  version: "0.2.0"
---

# UX patterns: choosing and applying concrete solutions

This skill is a catalogue of recurring interface problems and the solutions that published studies and openly documented design systems support. It is organised by what the person is trying to do: find their way, enter information, read and compare, understand what happened, get started, and do all of that on a small screen.

It is the practical companion to the other skills in this suite: `ux-psychology` explains why people behave as they do, `ux-ethics` sets limits, `ux-accessibility` makes each pattern work for everyone. Where an entry depends on one of those, it says so. Each skill also works alone.

## Grades

Evidence for interface patterns is thinner than most design advice admits, so each entry is graded:

- **Strong**: replicated in controlled studies.
- **Moderate**: supported, but by few studies, by survey-form research applied to interfaces, or by industry studies that were not peer-reviewed.
- **Contested**: studies disagree, or the common claim goes beyond the evidence.
- **Framework**: established practice documented by public design systems, without a controlled study behind it. Treat as a sensible default, not a fact.

The finding and sources behind each entry are in `references/evidence.md`. Open it, if it is available, when reviewing (to back each issue raised) or when someone asks why a rule exists. If it is not available, give the entry name and its grade. It is not needed for designing.

## How to choose a pattern

1. **State the problem, not the component.** "People need to pick one of four plans" comes before "radio buttons or cards".
2. **Use the plainest standard pattern that solves it.** People already know standard controls. A custom one has to be learned, built, and made accessible.
3. **Check a public design system before inventing.** The GOV.UK Design System, the US Web Design System and the W3C ARIA Authoring Practices Guide document patterns together with the research or accessibility reasoning behind them.
4. **Design the whole pattern.** Every pattern has states: empty, loading, error, success, disabled, and its small-screen form.
5. **Say how sure you are.** When recommending one pattern over another, give the grade. For Contested and Framework entries, suggest testing with users instead of asserting.

## Two ways to use this

Decide which task this is first. Making or changing a design: follow Designing, using each entry's Use when, **Do** and Check lines. Assessing existing work: follow Reviewing, using Use when, Avoid when and **Check**; where an entry has no Check line, review against its Do line. If asked to review and then fix, review first, then apply the Do lines to what was found.

### Designing

Work through the sections that match the screen. For each problem, pick the pattern from its "Use when" line, apply the Do line, and run the Check line before moving on.

### Reviewing

For each component on the screen, ask what problem it is solving and whether the catalogue suggests a plainer or better-supported pattern. Report: where it is, what the pattern is costing the user, the alternative, and the grade of the evidence (with the finding from `references/evidence.md`, if available). Do not recommend replacing a working pattern on Framework-grade evidence alone; say it is a judgement call.

## The catalogue

### 1. Finding their way

**Broad, shallow menus** · Strong
- Use when: organising any navigation of more than a handful of destinations.
- Do: prefer two levels to three or more. Group items under clear headings so a long level is still scannable. Do not flatten everything into one very long level either; about eight items per level over two levels did best in testing.
- Check: three or more levels of fly-out menus; a top level with two or three vague categories.

**Labels that predict what is behind them** · Moderate, theory with supporting studies
- Do: use the words users use for the thing, specific over clever. A label should let someone guess the first thing they will see after clicking.
- Check: brand names for sections; "Solutions", "Resources", "More".

**Visible navigation over hidden** · Moderate, industry study
- Do: show top-level destinations when there is room. On phones, a bottom bar for three to five main destinations, with a menu for the rest.
- Check: a desktop layout with all navigation behind an icon.

**Breadcrumbs** · Moderate, small studies
- Use when: the site has three or more levels and people arrive deep from search.
- Do: optional; few people use them, but they cost little. Show the path through the hierarchy, not the click history. The current page is the last item and is not a link.

**Search** · Framework
- Use when: there is more content than navigation can expose, or people arrive knowing what they want.
- Do: an open, labelled field where space allows. Tolerate typos and plurals. Keep the query visible on the results page. A no-results page explains why and offers alternatives.
- Check: search hidden behind an icon on a content-heavy site; "No results" as a dead end.

**Tabs and accordions** · Framework
- Use when: tabs for a few parallel views of the same thing, where people need one at a time. Accordions when people need only a few sections out of many.
- Avoid when: people need to compare across sections or read most of them; then show it all with headings.
- Check: content everyone needs hidden behind a click; tabs that wrap onto two lines.

**Carousels** · Moderate, single-site analytics
- Do: do not put anything important in a slide after the first. Prefer a single static panel. If a carousel is required, no auto-advance and visible controls (see `ux-accessibility`).

**Pages, "load more" and endless scroll** · Framework
- Use when: pages for goal-directed finding and comparing, where people need a sense of position and a reachable footer. "Load more" as a middle course. Endless scroll only for casual browsing.
- Do: whichever is used, returning from an item restores the previous position.
- See also: `ux-ethics` on feeds and stopping points.

### 2. Entering information

**Follow the basic form guidelines together** · Strong
- Do: the entries below cover the guidelines that matter most. The gains come from applying them together.

**One column, in the order people think** · Framework
- Do: one field per row, top to bottom. Group related fields under a heading. For long or branching forms, one question or topic per page, so each page can validate and save.
- Check: two-column forms where the reading order is unclear; unrelated fields on one row.

**Ask for less** · Framework
- Do: remove every field the task does not need. Mark the remaining optional ones. Never ask twice for something already given.
- See also: `ux-ethics` on collecting less; `ux-accessibility` on redundant entry.

**Label position** · Contested
- Do: labels above fields is a sound default because it survives narrow screens, long labels and translation. A label is always visible; placeholder text is never the label (see `ux-accessibility`).
- Note: eye-tracking studies conflict on labels above versus beside fields, so do not report labels beside fields as an error on speed grounds.

**Required and optional fields** · Moderate
- Do: mark required status in words, not by an asterisk or colour alone. If most fields are required, label the few optional ones "(optional)". If few are required, label those "(required)".
- Check: an asterisk with no explanation; required status shown only by colour.

**Choosing a selection control** · Moderate, from web survey research
- Do: radio buttons for one choice from a few options, checkboxes for several, a drop-down only for long, familiar lists, and a type-ahead field for very long ones. A switch only for a setting that takes effect immediately. Options that show without opening or scrolling get chosen more, so show all of them or none.
- Check: a drop-down with three options; a drop-down as the first field on mobile; a switch inside a form that needs saving.

**Sliders** · Moderate, from web survey research
- Use when: the value is approximate and feedback is immediate (volume, a price range on a results page).
- Do: pair with a text input or buttons for exact values (also required for accessibility).

**Fields that match the data** · Framework
- Do: size a field to its expected content. Three short fields for a date people know, such as a birthday; a calendar for dates near today. One field for things people paste (phone, card number, code). Accept spaces, dashes and case, and tidy up afterwards. Set the right keyboard and autofill type.
- Check: a calendar picker for date of birth; a phone number split into parts; rejection of valid input over formatting.

**When to show errors** · Moderate
- Do: validate on submit and show the messages inside the form, beside each field, not in a separate dialog. Validating on leaving a field is common practice but performed worst when tested, so keep it for cases where an early answer saves real effort, such as a username that is taken. Never validate while someone is still typing their first attempt, and clear an error as soon as the input becomes valid.
- Check: "invalid email" after one keystroke.

**What an error says** · Framework with early empirical basis
- Do: on submit, a summary at the top listing each problem and linking to its field, and a message beside each field. Say what is wrong and how to fix it. Keep everything the person typed.
- See also: `ux-accessibility` on error identification.

**Passwords and sign-in** · Moderate
- Do: one password field with a "show" option. Require length, not character-mix rules (current US federal guidance says not to impose them); a strength meter helps people choose longer passwords. State the rule before typing, not after failure. Allow paste and managers. Offer sign-in that needs no password where possible.
- Check: character-mix rules at all, or rules revealed one error at a time; paste blocked; a confirm-password field with masking and no show option.

**Progress through a multi-step form** · Contested
- Do: when steps are few and known, name them and show the current one. Put short, easy steps first. Progress shown must be real (see `ux-ethics`).
- Note: a steadily advancing progress bar did not reduce drop-out in survey experiments, and one that starts slowly increased it. Do not add one expecting it to keep people going.
- Check: a percentage bar on a long form that crawls at the start.

**Review before committing, confirm afterwards** · Framework
- Do: before a submission that is hard to reverse, show every answer with a way to change each one. Afterwards, a page that says it worked, what happens next, and a reference to keep.
- See also: `ux-accessibility` on error prevention.

### 3. Reading and comparing

**Tables** · Framework; zebra striping Contested
- Use when: people compare items across the same attributes.
- Do: left-align text and right-align numbers, with units in the header. Keep headers visible when scrolling. Sort by the most useful column by default. Shading alternate rows is optional; the evidence that it helps is weak. On small screens, turn each row into a stacked card or scroll the table sideways inside its own container.
- Check: centred numbers; a table that forces the whole page to scroll sideways.

**Filters and facets** · Moderate
- Do: show the number of results behind each option. Keep applied filters visible and removable one at a time. Never let a filter combination end in an empty page without a way back. Keep keyword search alongside facets; facets suit browsing more than looking up a known item.
- Check: filters that reload and lose scroll position; no indication of what is applied.

**Lists or cards** · Framework
- Use when: lists for scanning and comparing text; cards or a grid when the image is what people choose by.
- Check: cards used for text-heavy items, which slows scanning.

### 4. Understanding what happened

**Loading** · Framework; skeleton screens unproven
- Do: for very short waits, show nothing new. For page content, a placeholder in the shape of what is coming (a reasonable choice, though not shown to feel faster than a spinner). For long operations, a real progress indicator and the option to carry on with something else. Never block the whole screen for a partial update.
- See also: `ux-psychology` on waiting.

**Success and status messages** · Framework
- Do: confirm an action where the person is looking. A message that disappears on its own is only for things that do not matter if missed; never put the only copy of important information, or an action such as undo, in one that vanishes quickly.
- See also: `ux-accessibility` on status messages and time limits.

**Undo before confirm** · Framework
- Do: for reversible actions, do it and offer undo. Reserve confirmation for irreversible actions, and make the dialog name the specific thing and consequence, with the action verb on the button ("Delete 3 files", not "OK").
- Check: "Are you sure?" on routine actions; Yes and No buttons.

**Dialogs** · Framework
- Use when: a decision must be made before anything else can continue.
- Avoid when: the content is promotional, or could sit on the page.
- See also: `ux-accessibility` on dialog focus; `ux-ethics` on interruptions.

**Empty states** · Framework
- Do: there are three kinds, and each needs its own message. First use: say what will appear here and offer one action to create it. No results: say what was searched and how to widen it. Error: say what failed and how to retry.
- Check: a blank area; "No data".

**Disabled buttons** · Framework
- Do: prefer an active button that explains what is missing when pressed over a disabled one that explains nothing. If a control must be disabled, say why nearby.

### 5. Getting started

**Let people start on a real task** · Moderate
- Do: no tour before the product. The first screen offers a real, small task, with sample content if an empty product would be confusing.
- Check: a multi-screen introduction; a mandatory tutorial.

**Reveal complexity in stages** · Moderate
- Do: common path first, advanced options on request and findable.
- See also: `ux-psychology` on staged complexity.

**Ask at the moment of need** · Framework
- Do: ask for an account, a permission or personal details when the feature that needs them is used, with the reason.
- See also: `ux-ethics` on consent and data.

**Help where the question arises** · Framework
- Do: hint text under the label for anything most people need. Tooltips only for supplementary detail, never for instructions required to complete the task.

### 6. On a small screen

**Reach** · Moderate, observational
- Do: main actions and navigation in the lower part of the screen; destructive actions away from the easiest spot.
- See also: `ux-psychology` on pointing; `ux-accessibility` on target size.

**Typing as little as possible** · Framework
- Do: the right keyboard for each field, autofill, sensible defaults, pickers for known sets, and camera or paste for codes and card numbers.

**One column, one primary action** · Framework
- Do: a single column; one primary action per screen, visible without scrolling or fixed at the bottom; secondary actions in a menu.

## When patterns pull against each other

- **Fewer steps vs. simpler steps.** Several short pages usually beat one long page for long or branching forms; a short form does not need splitting.
- **Hiding to simplify vs. showing to inform.** Hide only what few people need. If most need it, show it.
- **Consistency vs. the better pattern.** Inside an existing product, matching what is already there usually wins. Raise the better pattern as a change to the whole system.
- **Evidence vs. convention.** Where the evidence is Contested or Framework and a platform convention exists, follow the convention.

## Closing check

1. Is each component the plainest standard one that solves the problem?
2. Can someone predict what each navigation label leads to?
3. Is the main navigation visible where there is room?
4. Is the form one column, with only the fields the task needs?
5. Does each choice use the right control for its number of options?
6. Do errors appear after input, say how to fix the problem, and keep what was typed?
7. Is there a review step before anything hard to reverse, and a confirmation after?
8. Are loading, empty, error and success states all designed?
9. Is undo offered where possible, and confirmation kept for the irreversible?
10. Can a new person do something real on the first screen?
11. On a phone, is the primary action within reach and typing kept to a minimum?
12. For each recommendation graded Contested or Framework, is that stated?

## Limits of this skill

Pattern evidence is uneven. Much of it comes from web survey research, small studies or industry reports, and results depend on context. This skill gives defaults and the strength of the evidence behind them; it does not replace testing the design with the people who will use it.
