# Evidence for ux-patterns

The finding and sources behind each entry in `SKILL.md`, in the same order. Open this when a review finding needs backing, or when someone asks why a rule exists. It is not needed for designing. Full references are in `sources.md`.

## 1. Finding their way

### Broad, shallow menus
- Grade: Strong
- Finding: In menu experiments, deep hierarchies with few choices per level were the slowest, and people felt most lost in them. The best results came from moderate breadth: two levels of eight for 64 items, and two levels beating three for 512 items. One very long single level was not best either.
- Sources: Miller 1981; Larson & Czerwinski 1998

### Labels that predict what is behind them
- Grade: Moderate, theory with supporting studies
- Finding: Information foraging theory models people as following cues, such as the wording of a link, that signal the value of what lies behind them, and leaving when that signal weakens. It was developed and tested on document-search tasks, not on navigation menus.
- Sources: Pirolli & Card 1999

### Visible navigation over hidden
- Grade: Moderate, industry study
- Finding: In a large usability study, navigation hidden behind a menu icon was used less, and made tasks slower and content less discoverable, than visible navigation, most clearly on desktop.
- Sources: Pernice & Budiu 2016

### Breadcrumbs
- Grade: Moderate, small studies
- Finding: In an exploratory study breadcrumb use was low overall, and using them made no significant difference to clicks, searches or time. They cost little space and show location.
- Sources: Lida, Hull & Pilcher 2003

### Search
- Grade: Framework
- Basis: established practice; no study cited.

### Tabs and accordions
- Grade: Framework
- Sources: GOV.UK Design System

### Carousels
- Grade: Moderate, single-site analytics
- Finding: On one university home page about 1% of visitors clicked a carousel item, and the great majority of those clicks were on the first slide.
- Sources: Runyon 2013

### Pages, "load more" and endless scroll
- Grade: Framework
- Basis: established practice; no study cited.

## 2. Entering information

### Follow the basic form guidelines together
- Grade: Strong
- Finding: When real web forms were revised to follow a set of 20 research-based guidelines, people completed them faster, needed fewer attempts to submit, and rated them higher.
- Sources: Bargas-Avila et al. 2010; Seckler et al. 2014

### One column, in the order people think
- Grade: Framework
- Sources: Bargas-Avila et al. 2010; GOV.UK Service Manual

### Ask for less
- Grade: Framework
- Basis: established practice; no study cited.

### Label position
- Grade: Contested
- Finding: An informal eye-tracking test suggested labels above fields need fewer eye movements than labels to the left. A later small eye-tracking study contradicted the usual advice and favoured right-aligned labels beside fields, at least in multi-column forms.
- Sources: Penzo 2006; Das, McEwan & Douglas 2008

### Required and optional fields
- Grade: Moderate
- Finding: Marking required fields with a coloured background led to fewer errors and faster completion than asterisks.
- Sources: Pauwels et al. 2009

### Choosing a selection control
- Grade: Moderate, from web survey research
- Finding: Options visible without opening or scrolling a list are chosen more often than hidden ones, and drop-down lists produced accidental answer changes among people using scroll mice, more skipped questions and slower answers than radio buttons.
- Sources: Couper et al. 2004; Healey 2007

### Sliders
- Grade: Moderate, from web survey research
- Finding: Slider scales increased drop-out and response time compared with radio buttons, most for people with less formal education.
- Sources: Funke, Reips & Thomas 2011

### Fields that match the data
- Grade: Framework
- Sources: GOV.UK Design System

### When to show errors
- Grade: Moderate
- Finding: In two experiments, showing each error as soon as the person left the field led to more errors than showing them after the whole form was submitted, with no difference in completion time. Showing all errors at once in a separate dialog was as bad as showing them immediately.
- Sources: Bargas-Avila et al. 2007

### What an error says
- Grade: Framework with early empirical basis
- Finding: Early experiments found that more specific and constructive system messages improved error correction and were preferred over terse or cryptic ones. A positive, non-blaming tone was recommended but not tested on its own.
- Sources: Shneiderman 1982

### Passwords and sign-in
- Grade: Moderate
- Finding: Password strength meters led people to create longer passwords, and stricter meters produced stronger passwords at the cost of annoyance. US federal guidance favours length, tells services not to impose composition rules, requires them to allow password managers, and recommends allowing paste.
- Sources: Ur et al. 2012; NIST 2025

### Progress through a multi-step form
- Grade: Contested
- Finding: A meta-analysis of web survey experiments found that a steadily advancing progress indicator did not reduce drop-out. Indicators that moved fast at first and slowed later reduced it; ones that started slow increased it.
- Sources: Villar, Callegaro & Yang 2013

### Review before committing, confirm afterwards
- Grade: Framework
- Sources: GOV.UK Design System

## 3. Reading and comparing

### Tables
- Grade: Framework; zebra striping Contested
- Finding: An experiment on shading alternate rows found no gain in accuracy and a speed gain on only one of six questions, though nearly half of participants preferred it. A larger informal follow-up found an accuracy benefit on some questions.
- Sources: Enders 2007; Enders 2008

### Filters and facets
- Grade: Moderate
- Finding: For browsing an image collection, most participants preferred an interface with category facets to a keyword-search baseline and judged it more useful, though it was slower on some structured tasks.
- Sources: Yee et al. 2003

### Lists or cards
- Grade: Framework
- Basis: established practice; no study cited.

## 4. Understanding what happened

### Loading
- Grade: Framework; skeleton screens unproven
- Finding: One small study rated a placeholder "skeleton" layout slightly higher than a spinner for perceived speed and ease, but no difference was statistically significant.
- Sources: Mejtoft, Långström & Söderström 2018

### Success and status messages
- Grade: Framework
- Basis: established practice; no study cited.

### Undo before confirm
- Grade: Framework
- Finding: The argument, supported by research on habituation to repeated warnings (see `ux-psychology`), is that confirmation dialogs seen often are dismissed without reading.
- Sources: Raskin 2000

### Dialogs
- Grade: Framework
- Basis: established practice; no study cited.

### Empty states
- Grade: Framework
- Basis: established practice; no study cited.

### Disabled buttons
- Grade: Framework
- Finding: The GOV.UK Design System advises avoiding disabled buttons where possible, because they have poor contrast and can confuse people.
- Sources: GOV.UK Design System

## 5. Getting started

### Let people start on a real task
- Grade: Moderate
- Finding: Learners given a short, task-oriented manual that got them working immediately learned more efficiently and performed better than those given a standard commercial manual (Carroll et al. 1987). The companion paper explains why: new users want to act, not read.
- Sources: Carroll & Rosson 1987; Carroll et al. 1987

### Reveal complexity in stages
- Grade: Moderate
- Sources: Carroll & Carrithers 1984

### Ask at the moment of need
- Grade: Framework
- Basis: established practice; no study cited.

### Help where the question arises
- Grade: Framework
- Basis: established practice; no study cited.

## 6. On a small screen

### Reach
- Grade: Moderate, observational
- Finding: In observations of more than 1,300 people using phones in public places, about half of those touching the screen did so one-handed, and grips changed often.
- Sources: Hoober 2013

### Typing as little as possible
- Grade: Framework
- Basis: established practice; no study cited.

### One column, one primary action
- Grade: Framework
- Basis: established practice; no study cited.
