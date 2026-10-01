# Evidence for ux-accessibility

The finding and sources behind each entry in `SKILL.md`, in the same order. Open this when a review finding needs backing, or when someone asks why a rule exists. It is not needed for designing. Full references are in `sources.md`.

## Background

- **Failures are nearly universal and mostly basic.** An annual automated audit of the top million home pages found detectable WCAG failures on 95.9% of them in 2026, averaging 56 per page. Low-contrast text, missing image alternatives, missing form labels, empty links, empty buttons and missing page language account for the great majority (WebAIM 2026). · Strong
- **Meeting the standard is necessary, not sufficient.** In a study with blind users, only about half of the problems they ran into were covered by WCAG 2.0 success criteria (Power et al. 2012). · Moderate, single study
- **Any single automated tool finds a minority of problems.** In one government test of ten tools against a page with 143 known barriers, individual tools found between 17% and about 40% (Vigo, Brown & Conway 2013; Government Digital Service 2017). · Moderate
- **Many people are affected.** About one person in six lives with significant disability (WHO 2022); at least 2.2 billion have a vision impairment (WHO 2019); and red-green colour deficiency affects roughly 1 in 12 men of European ancestry (Birch 2012). · Strong

## 1. Colour and contrast

### Text contrast
- Finding: The single most common detectable failure, present on 83.9% of top home pages (WebAIM 2026).

### Contrast of controls and graphics
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Colour is never the only signal
- Finding: Roughly 8% of men and under 1% of women of European ancestry have red-green colour deficiency (Birch 2012). · Strong

## 2. Text and reading

### Text that scales and reflows
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Room for user text spacing
- Finding: Wider letter spacing improved reading speed and accuracy for children with dyslexia (Zorzi et al. 2012). · Moderate

### Typeface claims
- Grade: Contested
- Finding: Typeface choice affects reading for people with dyslexia, but fonts marketed as designed for dyslexia have not shown a benefit beyond what their wider spacing provides.
- Sources: Rello & Baeza-Yates 2013; Marinus et al. 2016; Kuster et al. 2018

### Plain language and predictable structure
- Grade: Framework
- Basis: established practice; no study cited.

### Real text, declared language
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 3. Structure and navigation

### Headings and regions
- Finding: In a large survey of screen reader users, navigating by headings was by far the most common way of finding information on a page (WebAIM 2024). · Strong, self-reported

### Order that makes sense without the layout
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Titles and link text that stand alone
- Finding: Misleading links were among the frustrations reported in a study of 100 blind users (Lazar et al. 2007). · Moderate

### Consistency and more than one route
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 4. Keyboard and focus

### Everything works by keyboard
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Focus you can see, and that is not covered
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### No surprises on focus or input
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Dialogs and overlays
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 5. Pointer and touch

### Target size
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Alternatives to gestures and dragging
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Hover and focus content
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Works in either orientation
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 6. Forms and errors

### Every field has a visible, connected label
- Finding: Missing form labels were found on 51% of top home pages (WebAIM 2026), and unlabelled or poorly designed forms were among the leading frustrations for blind users (Lazar et al. 2007). · Strong

### Say what kind of data a field wants
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Errors in words, next to the field, with a way to fix them
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Do not ask twice
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Signing in without memory tests or puzzles
- Finding: Visual and audio puzzles used to tell people from bots exclude many people with disabilities (W3C 2019, Inaccessibility of CAPTCHA). · Framework

## 7. Images, media and motion

### Text alternatives
- Finding: Missing alternatives were found on 53.1% of top home pages (WebAIM 2026). · Strong

### Captions, transcripts and description
- Finding: Captions improve comprehension and memory of video for many groups, including hearing viewers and people watching in a second language (Gernsbacher 2015). · Strong

### Nothing that flashes
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

### Movement the user controls
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 8. Time

### Time limits people can extend
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 9. Custom components

### Native elements first; names, roles and states for everything else
- Finding: Home pages that used ARIA had more detected errors on average than those that did not (59.1 against 42; WebAIM 2026). This is a correlation, but it fits the standing advice that a native element is safer than a rebuilt one. · Moderate

### Changes that are announced
- Basis: requirement of the standard; see the success criteria named in `SKILL.md`.

## 10. Beyond the checklist: the range of people and situations

### Disability is a mismatch between a person and what a design demands
- Grade: Framework
- Finding: The World Health Organization's framework treats disability as the result of the interaction between a person's health condition and their context, both environmental and personal, not as a property of the person alone. A design can therefore create a barrier or remove one.
- Sources: WHO 2001

### Limits can be permanent, temporary or situational
- Grade: Framework
- Finding: The concept of situationally induced impairment holds that context (glare, noise, movement, cold, a hand occupied, stress, divided attention) can reduce what people can do in ways that resemble lasting impairments. Ability-based design proposes designing for what people can do in their situation instead of expecting them to adapt.
- Sources: Sears et al. 2003; Wobbrock et al. 2011

### Estimate and reduce exclusion, with the people excluded
- Grade: Framework
- Finding: The inclusive design literature frames the work as measuring how many people a design excludes through its demands on vision, hearing, thinking, reach and dexterity, and reducing that number through design choices made with those people involved.
- Sources: Clarkson et al. 2003; Waller et al. 2015

### Features built for some help many
- Grade: Moderate
- Finding: Captions, made for deaf and hard-of-hearing viewers, improve comprehension for many other viewers. Similar spillover is often claimed for other features with less evidence.
- Sources: Gernsbacher 2015
