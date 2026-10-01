---
name: ux-writing
description: Write and review interface text so it is understood, usable and inclusive, with an evidence grade for each guideline. Use when writing or reviewing labels, buttons, headings, instructions, form questions, error messages, confirmations, empty states, notifications or any product copy, or when asked about plain language, tone or inclusive language.
license: MIT
metadata:
  version: "0.2.0"
---

# UX writing: words people can understand and act on

This skill is a catalogue of research on how people read and respond to the words in an interface, turned into guidance for writing and reviewing them. It is organised by what the words have to do: be understood, name things, guide, respond, include everyone, and carry numbers and translation.

It belongs to a suite with `ux-psychology`, `ux-ethics`, `ux-accessibility` and `ux-patterns`, and points to them where they cover the same ground. It also works alone.

## Grades

- **Strong**: replicated in controlled studies.
- **Moderate**: supported, but by few studies, older studies, or industry studies that were not peer-reviewed.
- **Contested**: studies or the people concerned disagree. Say so, and do not present one side as settled.
- **Framework**: established practice in public style guides, without a controlled study behind it.

The finding and sources behind each entry are in `references/evidence.md`. Open it, if it is available, when reviewing (to back each issue raised) or when someone asks why a rule exists. If it is not available, give the entry name and its grade. It is not needed for writing.

## Two ways to use this

Decide which task this is first. Writing or rewriting text: follow Writing and use each entry's **Do** line. Assessing existing work: follow Reviewing and use each entry's **Check** line; where an entry has none, review against its Do line. If asked to review and then fix, review first, then apply the Do lines to what was found.

### Writing

1. **Know the reader and the moment.** Who is reading, what are they trying to do, and what state are they in (hurried, anxious, mid-task)?
2. **Write the plain version first.** Say what you mean in the words the reader would use. Then cut.
3. **Put the important words first** in headings, labels, links and sentences.
4. **Read it aloud as if to the user.** If it would sound odd, cold or evasive said to a person, rewrite it.
5. **Run the closing check.**

### Reviewing

1. Read every piece of text on the screen in the order a user would meet it, including errors and empty states if supplied.
2. For each problem, report: the text as written, what it will cost the reader, **a rewritten version**, and the grade of the evidence behind the change (with the finding from `references/evidence.md`, if available). A review without rewrites is not finished.
3. Rank by harm to the task: unclear actions and unhelpful errors first, style last.
4. Do not impose a brand voice. If the product has a style guide, follow it unless it conflicts with clarity or inclusion, and say where it does.

## The catalogue

### 1. Being understood

**People scan before they read** · Moderate, industry study
- Do: short paragraphs, meaningful headings, lists for parallel items, the conclusion first. Cut every word that does not help the task. Keep the tone neutral, not promotional.
- Check: a welcome paragraph before the content; instructions buried mid-paragraph.

**Many adults find reading hard** · Strong
- Do: short sentences, common words, one idea per sentence. This is the baseline for a general audience, not a simplification for a minority.

**Plain language works for experts too** · Moderate
- Do: prefer the everyday word (use, not utilise; help, not facilitate). Define a technical term the first time, or replace it.
- Check: internal names, acronyms and legal phrasing at decision points.

**Readability scores are a rough check, not a target** · Contested
- Do: use a score to spot very long sentences. Judge the result by whether a real reader can act on it.

**Say it positively and directly** · Strong
- Do: state what to do or what is true. Avoid "not un-", "do not disable" and questions where "No" means yes.
- Check: "Uncheck to not receive", "Don't forget to not".
- See also: `ux-ethics` on trick wording.

**Headings that say what follows** · Moderate, studies with schoolchildren
- Do: a heading for each section, written as a statement or a question the reader has. Avoid clever or generic headings ("Overview", "More info").
- See also: `ux-accessibility` on heading structure.

**Capital letters** · Moderate, old print studies
- Do: no sentences in all capitals. Between sentence case and title case for buttons and headings there is no good evidence; pick one and be consistent.

### 2. Naming things

**People do not agree on names** · Strong
- Do: do not trust your own term. Find the words users say (search logs, support messages, interviews), use the most common one, and make search and help recognise the others.
- Check: a feature name only the team would know.

**One name for one thing** · Framework
- Do: once a thing has a name, use it everywhere: navigation, headings, buttons, messages, help. Two names suggest two things.
- Check: "Sign in" on one screen and "Log in" on another; "basket" and "cart".

**Buttons and links that say what happens** · Framework
- Do: a verb and, where needed, its object: "Save changes", "Delete account", "Download report". The label should make sense read alone and match the heading of what it opens.
- Check: "OK", "Submit", "Yes", "Click here", "Learn more".
- See also: `ux-patterns` on labels and confirmation; `ux-accessibility` on link purpose.

**Important words first** · Framework
- Do: start labels, headings, list items and notifications with the word that distinguishes them, because scanning eyes catch the first two or three words.
- Check: every item in a list starting "How to" or "Manage your".

### 3. Guiding

**One question at a time** · Strong, from survey research
- Do: each question asks one thing, in words the person would use, with the answer options matching the question. Say how the answer will be used when it is not obvious.
- Check: "Do you want updates and offers?"; options that do not fit the question.

**Instructions where and when they are needed** · Framework
- Do: before the thing they apply to, in the order the steps happen, one action per sentence, starting with the verb. Give an example for any format.
- Check: instructions after the field; a paragraph that must be remembered three steps later.
- See also: `ux-patterns` on help in context.

**Say why you are asking** · Framework
- Do: when asking for personal information or permission, give the reason in one plain sentence beside the request.
- See also: `ux-ethics` on consent and data.

### 4. Responding

**Errors: what happened and what to do** · Framework with early empirical basis
- Do: say what went wrong in the user's terms, then how to fix it. No codes alone, no jargon, no blame ("Enter a date in the future", not "Invalid date"). If the fault is the system's, say so and say what happens to their work.
- Check: "Something went wrong"; "Error 4032"; "You entered an invalid value".
- See also: `ux-patterns` on when errors appear; `ux-accessibility` on error identification.

**People respond to products as they do to people** · Moderate
- Do: wording that would be rude, evasive or patronising from a person reads the same from a product. Be courteous without gushing; keep praise for real achievements.
- Check: scolding ("You failed to"), false cheer on bad news, guilt on opt-outs (see `ux-ethics`).

**Confirmations that close the loop** · Framework
- Do: say what happened, in the past tense, with the specific thing ("Invoice sent to Dana"), and what happens next if anything.
- Check: "Success!"; a confirmation that does not say what succeeded.

**Personality in its place** · Framework
- Do: humour and brand voice are for low-stakes moments. Never in errors, payments, security, health, or anything that may be read by someone under stress. A joke read for the tenth time is noise.

### 5. Including everyone

**Masculine words used as generic are not read as generic** · Strong
- Do: use "they" for an unspecified person, or write in the second person ("you"). Use role names without gender ("chair", "salesperson"). For a known person, use the pronouns they use.
- Check: "the user ... he", "manpower", "guys" in interface text.

**Wording changes who feels invited** · Moderate
- Do: describe what is done, not a personality type. Review examples, names and scenarios for a narrow picture of who the user is.
- Check: stereotypically masculine wording in descriptions of who the product or role is for.

**Disability language** · Contested
- Do: follow the usage of the people being described, and ask when you can. Mention disability only when relevant. Avoid pity or heroism ("suffers from", "brave"), and avoid disability words as metaphors ("blind to", "crippled by").
- Note: neither person-first ("person with epilepsy") nor identity-first ("autistic person", "Deaf person") is correct everywhere. Do not change one to the other without knowing the community's preference.
- Check: "the disabled"; "wheelchair-bound"; "sanity check".

**Terms with loaded origins** · Framework
- Do: public style guides recommend replacing technical terms built on racial, militaristic or violent metaphors with descriptive ones, for example an allow list and a block list, or primary and replica. Google's developer documentation style guide also suggests "stop" or "end" in place of "kill". Descriptive terms are also clearer and translate better.

**Do not assume who is reading** · Framework
- Do: no assumptions about gender, family, age, religion, location or season in examples and messages. Use varied names and situations in sample content. Do not treat one country or culture as the default.
- Check: "Happy holidays" in one tradition; "ask your wife"; examples with only one kind of name.
- See also: `ux-ethics` on narrow research samples and on asking about identity.

**Idioms, slang and cultural references** · Framework
- Do: write literally. Idioms, sports metaphors and slang fail for people reading in a second language, for some neurodivergent readers, and in translation.
- Check: "hit it out of the park", "low-hanging fruit", "ping me".

### 6. Numbers and other languages

**Counts of cases are understood better than probabilities** · Strong for reasoning problems
- Do: for risk and likelihood, give counts of people or cases out of a stated total and keep that total the same throughout. Give the absolute figure, not only a relative change.
- See also: `ux-ethics` on framing.

**Unambiguous numbers, dates and units** · Framework
- Do: write dates with the month as a word ("4 March 2027"), since 04/03 means different days in different countries. Always give the unit and currency. Use the reader's local formats where known.

**Writing for translation** · Framework
- Do: translated text is often much longer, especially short labels, so leave room. Write whole sentences; never build a sentence by joining fragments or inserting variables mid-phrase, because word order differs between languages. Keep text out of images.
- Check: a button sized exactly to its English label; "You have " + n + " new " + thing.

## When guidelines pull against each other

- **Short vs. clear.** Clear wins. "Save changes" beats "Save"; a specific error beats a short one.
- **Plain vs. precise.** In legal, medical or financial text, keep the precise term and explain it in plain words beside it.
- **Friendly vs. respectful of time.** In a task, be brief and neutral. Warmth belongs at the start and the end, not at every step.
- **Brand voice vs. inclusion or clarity.** Clarity and inclusion win; say so when a house style conflicts with them.
- **Inclusive vs. imposed.** Where the people described prefer a term, use theirs, even if a guide says otherwise.

## Closing check

1. Could a hurried reader act on this after reading only the headings, labels and first words?
2. Is every sentence about one thing, in words the reader would use?
3. Are there any negatives, double negatives or jargon that can be removed?
4. Does each thing have exactly one name throughout?
5. Does every button and link say what will happen?
6. Does every question ask one thing, with options that fit?
7. Does every error say what happened and how to fix it, without blame?
8. Would any line sound rude, evasive or patronising if a person said it?
9. Does anything assume the reader's gender, family, culture or location?
10. Are there idioms, slang or metaphors a second-language reader would miss?
11. Are numbers, dates and units unambiguous?
12. Will the layout survive text that is much longer in another language?

## Limits of this skill

This skill covers the words in an interface. It does not write marketing campaigns or long-form content, and it does not replace legal review of terms, medical review of health information, or checking wording with the people it describes. Language norms change and differ by place; treat the inclusive-language entries as a starting point, not a rulebook.
