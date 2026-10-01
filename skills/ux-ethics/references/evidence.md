# Evidence for ux-ethics

The finding and sources behind each entry in `SKILL.md`, in the same order. Open this when a review finding needs backing, or when someone asks why a rule exists. It is not needed for designing. Full references are in `sources.md`.

## Three tests

### Understanding test
- Grade: Framework
- Sources: Susser, Roessler & Nissenbaum 2019

## 1. Their decisions: deceptive and coercive patterns

### Deceptive patterns are common and they work
- Grade: Strong
- Finding: A crawl of about 11,000 shopping sites found dark patterns on roughly 11% of them, with outright deceptive ones on 183 sites, and a study of 240 popular mobile apps found them in 95%, mostly unnoticed by users. In experiments, mild versions more than doubled sign-ups to a paid service and aggressive versions nearly quadrupled them; only the aggressive versions caused a backlash.
- Sources: Gray et al. 2018; Mathur et al. 2019; Di Geronimo et al. 2020; Luguri & Strahilevitz 2021

### Unequal choices
- Grade: Strong
- Finding: Making one option more prominent, or putting the refusal a click deeper, shifts choices substantially. Removing "reject all" from the first layer of a consent notice raised consent by over 20 percentage points.
- Sources: Nouwens et al. 2020; Utz et al. 2019; Mathur, Mayer & Kshirsagar 2021

### Guilt-worded and trick-worded options
- Grade: Moderate
- Finding: Confusing wording such as double negatives, and decline options phrased to shame the person, are documented pattern types; confusing wording increased acceptance in experiments.
- Sources: Gray et al. 2018; Mathur et al. 2019; Luguri & Strahilevitz 2021

### Nagging
- Grade: Framework
- Finding: Repeated requests that persist across interactions are a documented pattern type. That work did not measure their effect; the concern is that people give in to make the prompts stop.
- Sources: Gray et al. 2018

### False urgency, scarcity and social evidence
- Grade: Strong for prevalence
- Finding: Countdown timers that reset, low-stock warnings that ticked down on a fixed schedule, and activity notices generated at random were found on live shopping sites, some supplied by third-party plugins built for the purpose.
- Sources: Mathur et al. 2019

### Friction used against the person
- Grade: Framework
- Finding: The same tools that help people follow through can be used to block what they want. Friction that serves the business against the person's intent has been named "sludge".
- Sources: Thaler 2018; Susser, Roessler & Nissenbaum 2019

### Optimisation drifts toward manipulation
- Grade: Framework
- Finding: Repeated testing against a single growth or engagement metric selects for whatever moves the number, including deception. Engagement can rise because people are being drawn against their own considered preferences.
- Sources: Narayanan et al. 2020; Kleinberg, Mullainathan & Raghavan 2024

## 2. Their data: consent and privacy

### Notice and consent does not inform
- Grade: Strong
- Finding: Reading the privacy policies a person encounters was estimated to take roughly 200 to 250 hours a year, and in one study most participants skipped the policy and almost all agreed to terms containing absurd clauses. Consent by click is not evidence of understanding.
- Sources: McDonald & Cranor 2008; Obar & Oeldorf-Hirsch 2020; Solove 2013

### Collect less, default to private
- Grade: Framework
- Finding: People's privacy choices are heavily shaped by defaults and context; defaults tend to stick and are read as recommendations. The protective setting therefore has to be the starting one.
- Sources: Cavoukian 2009; Acquisti, Brandimarte & Loewenstein 2015

### Data should flow as the context leads people to expect
- Grade: Framework
- Finding: Privacy harm comes less from data being known than from it moving to a place that breaks the norms of where it was shared.
- Sources: Nissenbaum 2004

### Timely, specific, declinable requests
- Grade: Framework, with field evidence on placement
- Finding: A review of the research sets out timing, channel, modality and control as the dimensions that decide whether a privacy notice is effective. In a field study, the position and wording of a consent notice strongly changed how many people interacted with it at all.
- Sources: Schaub et al. 2015; Utz et al. 2019

### Controls can create false comfort
- Grade: Moderate
- Finding: Giving people more control over publishing their information made them disclose more, including more sensitive information, even when the risk of others using it was higher.
- Sources: Brandimarte, Acquisti & Loewenstein 2013

### Leaving with your data
- Grade: Framework
- Basis: established practice; no study cited.

## 3. Their money: prices, subscriptions and cancellation

### Fees revealed late
- Grade: Strong
- Finding: In a large field experiment on a ticket marketplace, showing fees only at checkout instead of up front made people spend about a fifth more and buy more expensive tickets.
- Sources: Blake et al. 2021

### Subscriptions exploit inattention
- Grade: Strong
- Finding: People overestimate how much they will use a subscription and are slow to cancel ones they no longer use; a meaningful share of subscription revenue depends on people not noticing renewals.
- Sources: DellaVigna & Malmendier 2006; Einav, Klopack & Mahoney 2025

### Pay-to-win chance mechanics
- Grade: Moderate
- Finding: Spending on randomised paid rewards in games was linked to problem-gambling severity in a large survey. The direction of cause is not established.
- Sources: Zendle & Cairns 2018

## 4. Their time and attention

### Interruptions cost more than their duration
- Grade: Strong
- Finding: Interrupted people worked faster but reported more stress, frustration and time pressure. Merely receiving a phone notification, without responding, impaired performance on an attention task, and a week with alerts on and the phone within reach produced more self-reported inattention than a week with alerts off and the phone away.
- Sources: Mark, Gudith & Klocke 2008; Stothart, Mitchum & Yehnert 2015; Kushlev, Proulx & Dunn 2016

### Batching helps; silence can backfire
- Grade: Moderate
- Finding: Delivering notifications in a few batches a day improved well-being measures, while turning them off entirely raised anxiety about missing out.
- Sources: Fitz et al. 2019

### Autoplay, endless feeds and the loss of intent
- Grade: Moderate
- Finding: People report that autoplay and recommendation feeds undermine their sense of control, while search and their own playlists support it. Endless feeds are associated with absorbed, unremembered use, and removing a feed shortened visits, cut scrolling and helped people stay on task.
- Sources: Lukoff et al. 2021; Baughan et al. 2022; Lyngs et al. 2020

### Screen time and well-being
- Grade: Contested
- Finding: Across large surveys the association between adolescents' technology use and well-being is negative but very small. In a randomised experiment, adults paid to deactivate a social network for four weeks reported small improvements in well-being. The size and causes of harm remain disputed.
- Sources: Orben & Przybylski 2019; Allcott et al. 2020

### Technology that stays in the background
- Grade: Framework
- Finding: A long-standing design goal is for technology to inform without demanding focus, moving to the centre of attention only when needed.
- Sources: Weiser & Brown 1996

## 5. Their ability to take part: inclusion and access

### Disability is common and access is a baseline
- Grade: Framework with strong demographic basis
- Finding: About one person in six worldwide lives with significant disability. Published standards define what accessible design requires.
- Sources: WHO 2022; W3C 2023; Story, Mueller & Mace 1998

### Design research samples are narrow
- Grade: Strong
- Finding: Most behavioural research draws on a small, unrepresentative slice of humanity, and results often differ elsewhere.
- Sources: Henrich, Heine & Norenzayan 2010

### Systems can perform unevenly across groups
- Grade: Strong
- Finding: Commercial face-analysis systems had error rates below 1% for lighter-skinned men and up to about a third for darker-skinned women. Bias can come from existing social attitudes built into a system, from technical constraints, and from use in settings the system was not built for.
- Sources: Buolamwini & Gebru 2018; Friedman & Nissenbaum 1996

### Asking about identity
- Grade: Framework
- Sources: Spiel, Haimson & Lottridge 2019

### Constrained conditions
- Grade: Framework
- Basis: established practice; no study cited.

## 6. Their safety: misuse, vulnerable people and children

### Features are used to harm people close to the user
- Grade: Strong, qualitative
- Finding: Abusers in intimate relationships mostly use ordinary features, not hacking: shared accounts, location sharing, device access and account recovery. Standard security assumptions about a remote attacker miss this.
- Sources: Freed et al. 2018

### Plan for misuse before launch
- Grade: Framework
- Finding: Structured methods exist for identifying everyone a technology affects, including people who never use it, and the values at stake for each.
- Sources: Friedman & Hendry 2019

### Children meet manipulative design early
- Grade: Strong for prevalence
- Finding: In a study of apps used by children aged three to five, most contained manipulative features such as pressure to keep playing, lures to purchase and characters urging the child on, and these were more common in apps used by children from families of lower socioeconomic status.
- Sources: Radesky et al. 2022

### Protective friction
- Grade: Moderate
- Finding: Briefly prompting people to think about accuracy improved the quality of the news they went on to share.
- Sources: Pennycook et al. 2021

## 7. Their trust: honesty about what the system is and does

### People often do not know a system is curating
- Grade: Moderate
- Finding: In one study most participants were unaware their social feed was filtered by an algorithm, and some had blamed themselves or their friends for what it hid.
- Sources: Eslami et al. 2015

### Over-reliance on automation
- Grade: Strong
- Finding: People working with automated aids miss problems the aid fails to flag and follow its advice when it is wrong.
- Sources: Parasuraman & Riley 1997; Skitka, Mosier & Burdick 1999

### Explanations can increase misplaced trust
- Grade: Moderate
- Finding: Adding explanations to AI recommendations made people more likely to accept them whether or not the recommendation was correct.
- Sources: Bansal et al. 2021

### Say what the system is
- Grade: Framework
- Finding: Published guidelines for human-AI interaction begin with making clear what the system can do and how well.
- Sources: Amershi et al. 2019
