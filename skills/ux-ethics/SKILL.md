---
name: ux-ethics
description: Design and review interfaces for honesty, consent, privacy, fair pricing, attention, inclusion and safety, using evidence-graded research and pointers to regulation. Use for sign-up, consent, pricing, subscription, cancellation, notification, feed, data-collection and AI-facing flows, or when asked whether a pattern is manipulative or a dark pattern.
license: MIT
metadata:
  version: "0.2.0"
---

# UX ethics: designing and reviewing for the person's interests

This skill is a catalogue of research on how interface design can work against the people using it, and what to do instead. Each entry is traced to its original published source. It is organised by what a product asks of a person: their decisions, their data, their money, their time and attention, their ability to take part, their safety, and their trust in what the system tells them.

It complements a psychology-based design skill: that kind of guidance explains how perception, memory and choice work; this one sets limits on how those mechanisms may be used.

## Grades and rules

Every entry carries an evidence grade:

- **Strong**: replicated, including in field studies or at scale.
- **Moderate**: real effect, with boundary conditions or limited evidence.
- **Contested**: mixed results or disputed size. State both sides; do not assert.
- **Framework**: a way of reasoning or a professional standard, not an experimental finding.

Some entries also carry a **Rules** line naming laws or standards that touch the topic. These are pointers for further checking, not legal advice. Laws differ by country and change often, so say "check with your legal team" and never tell someone a design is or is not lawful.

The finding and sources behind each entry are in `references/evidence.md`. Open it, if it is available, when reviewing (to back each issue raised) or when someone asks why a rule exists. If it is not available, give the entry name and its grade. It is not needed for designing.

## Three tests to apply everywhere

1. **Understanding test.** Would this still work if the person fully understood what it was doing and why? If it only works because they don't notice, it is manipulation.
2. **Symmetry test.** Is saying no as easy as saying yes, and leaving as easy as joining? Same number of steps, same visual weight, same channel.
3. **Whose interest test.** If the person thought carefully, is this what they would choose for themselves? If the benefit goes only to the business, redesign it.

## Two ways to use this

Decide which task this is first. Making or changing a design: follow Designing and use each entry's **Do** line. Assessing existing work: follow Reviewing and use each entry's **Check** line; where an entry has none, review against its Do line. If asked to review and then fix, review first, then apply the Do lines to what was found.

### Designing

1. **Name who is affected.** The user, and also people who are not the user: the person being messaged, tracked, rated or shown. Note anyone likely to be vulnerable in this context (children, people in distress, people under financial pressure, people new to the language or the technology).
2. **Name what the product is asking for** on this screen: a decision, data, money, time, or trust. Go to those sections.
3. **Apply the three tests** to every default, prompt, price and exit.
4. **Design the exits and the refusals** with the same care as the main path: decline, skip, cancel, delete, unsubscribe, turn off.
5. **When the brief asks for a pattern this skill warns against**, say plainly what the problem is and offer an honest design that pursues the same business goal. Do not silently comply and do not lecture.

### Reviewing

1. **Look at the real design**, including the paths for declining, cancelling and leaving. Ask for them if they were not supplied; their absence is a finding.
2. **Walk it as a hurried, distracted person**, then as someone trying to say no, then as someone trying to leave.
3. **Match what you see to the Check lines.** Do not issue a verdict per entry.
4. **Rank by harm**: how serious, how many people, how vulnerable they are, and whether it can be undone.
5. **Report** each finding as: where it is, what the person will experience, the entry behind it with its grade (and its finding from `references/evidence.md`, if available), any Rules pointer, and a concrete alternative that keeps the legitimate business goal. Finish with what the design gets right.
6. Describe designs, not motives. Say "this checkbox is pre-ticked", not "the team is trying to trick users".

## The catalogue

### 1. Their decisions: deceptive and coercive patterns

**Deceptive patterns are common and they work** · Strong
- Do: treat the families below as off limits: obstruction, sneaking, interface interference, forced action, nagging, false urgency, false scarcity and false social evidence.
- Note: mild versions work without provoking complaints, so an absence of complaints is not evidence that a pattern is acceptable.
- Rules: EU Digital Services Act Art. 25; FTC staff report 2022; California CPRA (agreement obtained through dark patterns is not consent).
- Check: any of the patterns in the rest of this section.

**Unequal choices** · Strong
- Do: give accept and decline the same size, contrast, position and number of steps. A recommendation is fine when it is labelled as one and serves the user.
- Check: a bright "Accept" beside a grey text link; "Manage options" as the only alternative to "Agree".

**Guilt-worded and trick-worded options** · Moderate
- Do: neutral labels that state the action: "No thanks", "Cancel subscription". One meaning for a ticked box throughout.
- Check: "No, I don't want to save money"; "Untick to not opt out".

**Nagging** · Framework
- Do: every prompt needs a durable "no". Ask once, at a moment when the request makes sense, and respect the answer.
- Check: "Not now" with no "Never"; a permission prompt that returns every session.

**False urgency, scarcity and social evidence** · Strong for prevalence
- Do: show time limits, stock and popularity only when true and verifiable, and without countdown pressure on decisions that deserve thought.
- Check: a timer that restarts on reload; "3 people are looking at this" with no data source.

**Friction used against the person** · Framework
- Do: add friction only to protect the person (confirming an irreversible deletion, pausing before a large payment). Remove it from refusing, cancelling, exporting and deleting.
- Check: a form to join and a phone call to leave.

**Optimisation drifts toward manipulation** · Framework
- Do: pair every growth metric with a guardrail the person would endorse (refund and complaint rates, cancellations soon after sign-up, regret, successful task completion).
- Check: success defined only as time spent, clicks or conversion.

### 2. Their data: consent and privacy

**Notice and consent does not inform** · Strong
- Do: do not rely on a policy link to make a practice acceptable. Make the practice itself reasonable, and explain the few things that matter in the interface, in plain words.
- Check: a surprising data use justified only by "it's in the terms".

**Collect less, default to private** · Framework
- Do: ask only for data the feature needs, at the moment it needs it, and say why. Optional fields marked optional. Sharing, tracking and visibility off until chosen.
- Rules: GDPR Art. 5(1)(c) data minimisation and Art. 25 data protection by design and by default.
- Check: date of birth or phone number with no stated purpose; a profile public by default.

**Data should flow as the context leads people to expect** · Framework
- Do: for each data use, ask whether a person in that context would expect it. If not, either don't do it or make it an explicit, separate, declinable choice.
- Check: contacts uploaded to "find friends" then used for marketing; health or location data reused for advertising.

**Timely, specific, declinable requests** · Framework, with field evidence on placement
- Do: ask for a permission at the moment its feature is used, in a sentence, with an equal "no", and keep the product working as far as possible if declined.
- Rules: GDPR Art. 7 (consent must be as easy to withdraw as to give).
- Check: all permissions requested at first launch; a feature wall for declining an unrelated permission.

**Controls can create false comfort** · Moderate
- Do: do not treat a settings page as a substitute for safe defaults and restrained collection.
- Check: extensive privacy settings sitting on top of permissive defaults.

**Leaving with your data** · Framework
- Do: make export, deletion and account closure findable from settings, completable in the product, and confirmed clearly. State what is deleted and what is retained.
- Rules: GDPR Arts. 17 and 20 (erasure, portability).
- Check: no delete option; deletion that requires emailing support.

### 3. Their money: prices, subscriptions and cancellation

**Fees revealed late** · Strong
- Do: show the full price, including unavoidable fees, the first time a price is shown. Itemise at checkout without adding anything new.
- Check: a total that grows at the last step; pre-added extras in the basket.

**Subscriptions exploit inattention** · Strong
- Do: before a trial converts or a plan renews, say so in advance with the date, amount and a direct way to cancel. Make pausing and downgrading available. Cancel in the same place and with the same effort as joining.
- Rules: US Restore Online Shoppers' Confidence Act; many jurisdictions have automatic-renewal laws.
- Check: a trial that needs a card with no reminder; cancellation hidden, split across screens, or moved to phone or chat.

**Pay-to-win chance mechanics** · Moderate
- Do: show odds, show real-money prices, offer spending limits, and do not aim such mechanics at children.
- Note: the link to problem gambling is a correlation. Do not say the mechanic causes it.
- Check: paid random rewards with hidden odds; virtual currencies that obscure real cost.

### 4. Their time and attention

**Interruptions cost more than their duration** · Strong
- Do: notify only for things the person asked to know or would regret missing. Off by default for marketing. Group low-priority items into a digest. Give per-type controls.
- Check: notifications to re-engage; one master switch for everything; badges for non-events.

**Batching helps; silence can backfire** · Moderate
- Do: offer scheduled summaries and quiet hours as well as on and off.
- Check: all-or-nothing notification settings.

**Autoplay, endless feeds and the loss of intent** · Moderate
- Do: give natural stopping points (pages, "you're caught up", end of episode). Make autoplay a visible, remembered setting. Let people land on what they came for.
- Check: no end state; autoplay on by default with the control buried; the home screen is always a feed.

**Screen time and well-being** · Contested
- Do: do not claim a design "improves well-being" without evidence. Equally, do not assert that screen time itself harms well-being: the measured association is negative but very small and its cause is disputed. Support the person's own goals: usage information, limits they set, easy breaks.
- Check: wellness claims with nothing behind them; no way to see or limit one's own use.

**Technology that stays in the background** · Framework
- Do: prefer ambient status over alerts, and completion over continued engagement. A product that helps someone finish and leave has done its job.
- Check: features whose only purpose is to bring people back.

### 5. Their ability to take part: inclusion and access

**Disability is common and access is a baseline** · Framework with strong demographic basis
- Do: sufficient contrast, text that scales, full keyboard and screen-reader operation, captions, no meaning carried by colour alone, generous targets, no time limits that cannot be extended.
- Rules: WCAG 2.2 is the reference standard used by many accessibility laws. The `ux-accessibility` skill in this suite covers it criterion by criterion.
- Check: low contrast; unlabeled icons; drag-only interactions; timed sessions with no extension.

**Design research samples are narrow** · Strong
- Do: do not assume one culture's names, addresses, calendars, reading direction, family structures or payment methods. Test with people unlike the team.
- Check: required "first name / last name"; forms that reject valid names or addresses.

**Systems can perform unevenly across groups** · Strong
- Do: check outcomes by group before launch, give a non-automated route, and never make an automated judgement the only path to something important.
- Check: identity or eligibility checks with no fallback.

**Asking about identity** · Framework
- Do: ask about gender or similar characteristics only when the product needs the answer, and say why. For gender, published guidance recommends options beyond a binary, a self-describe option, a prefer-not-to-say option, and making the question optional.
- Check: a required binary gender field with no purpose stated.

**Constrained conditions** · Framework
- Do: make the core task work on a slow connection, an old device, a small screen, in bright light, in a second language and with one hand. Write at a plain reading level.
- Check: a core task that fails without high bandwidth; dense legal or technical language at decision points.

### 6. Their safety: misuse, vulnerable people and children

**Features are used to harm people close to the user** · Strong, qualitative
- Do: for any feature that reveals location, activity or content to another person, make sharing visible to the person being shared, periodically reminded, and easy to stop without alerting the other party. Show active sessions and linked devices.
- Check: silent location sharing; no list of who has access; account recovery through questions a partner could answer.

**Plan for misuse before launch** · Framework
- Do: for each feature, write down who could be harmed, how someone could abuse it, and what the reporting, blocking and recovery paths are. Design those paths as real screens.
- Check: no block, report or undo; no thought for the person on the receiving end.

**Children meet manipulative design early** · Strong for prevalence
- Do: if children may use the product, apply the strictest version of everything in this skill: no pressure mechanics, no purchases without an adult, high privacy by default, no profiling for advertising.
- Rules: UK Age Appropriate Design Code; US COPPA; similar codes elsewhere.
- Check: characters that plead; timers and streaks in children's products; purchases a child can make alone.

**Protective friction** · Moderate
- Do: a short pause or prompt before actions that affect others (sharing, posting, sending to many) can help without blocking. Use sparingly so it does not become noise.
- Check: one-tap resharing to large audiences with no moment to reconsider.

### 7. Their trust: honesty about what the system is and does

**People often do not know a system is curating** · Moderate
- Do: say when content is ranked, recommended or sponsored and on what broad basis; offer a way to adjust or switch to a simple order.
- Rules: EU Digital Services Act Art. 27 (recommender transparency).
- Check: advertising styled as content; a ranked list presented as neutral.

**Over-reliance on automation** · Strong
- Do: show the basis and uncertainty of automated output, keep the person able to check and override, and make errors easy to report and reverse.
- Check: automated decisions presented as fact; no route to a human; no way to correct the record.

**Explanations can increase misplaced trust** · Moderate
- Do: do not add explanation as decoration. Show what would help a person catch an error: sources, confidence, what the system did not consider.
- Check: a confident rationale with nothing checkable in it.

**Say what the system is** · Framework
- Do: disclose when people are interacting with an automated system or reading generated content. State limits up front. Do not give software a human name, face or feelings in order to increase trust or spending.
- Rules: EU AI Act Art. 50 (transparency for AI systems that interact with people).
- Check: a chatbot presented as a person; generated content with no label.

## When goals conflict

- **Business target vs. honest design.** Find the honest design that serves the same goal: clearer value, better timing, a real incentive. If none exists, say so.
- **Safety friction vs. ease.** Friction is justified when it protects the person or a third party and is proportionate. It is not justified when it protects revenue.
- **Personalisation vs. privacy.** Prefer on-device and session-only signals, and let people see and reset what is used.
- **Transparency vs. overload.** Explain the few things a person would want to know before deciding, at the moment of deciding. Put the rest one step away.
- **One group's convenience vs. another's access.** Access wins. Then look for a design that serves both.

## Closing check

1. Does every prompt have an equal, neutral, lasting way to say no?
2. Is everything preselected in the person's interest?
3. Is the first price shown the full price?
4. Is cancelling, deleting or leaving as easy as joining, and was that path designed?
5. Is each piece of data needed, explained, and asked for at the moment of use?
6. Would any data use surprise a person in this context?
7. Does every notification pass "they asked for it or would regret missing it"?
8. Is there a place to stop?
9. Can the core task be done by keyboard, by screen reader, at 200% text size, and on a slow connection?
10. Who could use this feature against someone else, and what stops them?
11. Is it clear what is automated, ranked, sponsored or generated?
12. Would it still work if the person understood exactly what it was doing?

## Limits of this skill

This skill covers interface design. It does not replace legal review, a full accessibility audit, a privacy impact assessment, or research with the people affected. Where it names a law or standard, that is a prompt to check, not a statement of what the law requires.
