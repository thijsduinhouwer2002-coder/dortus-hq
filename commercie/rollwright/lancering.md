# Rollwright: lanceerberichten (concepten)

Door Chris, 7 nov 2026. Posten onder de naam van Thijs doet Thijs zelf. Deze berichten gaan pas naar `organisatie/lijst-thijs.md` als Rollwright echt in Community plugins staat (anders kan niemand het met één klik installeren). Daarvoor moet Thijs eerst de aanmelding doen (lijst-thijs, 7 nov 21:45).

## Volgorde en waarom
1. **Obsidian-forum, categorie Share & showcase** (forum.obsidian.md). Daar kondigen makers nieuwe plugins aan; mensen die Obsidian goed kennen lezen het.
2. **r/ObsidianMD** (Reddit). Groot publiek van Obsidian-gebruikers.
3. **r/Solo_Roleplaying**, één of twee dagen later. Solo-spelers houden vaak een logboek bij in notities en rollen veel op tabellen; dat is onze kerngebruiker (GOK).
4. **Obsidian Discord, kanaal #updates** (alleen als de regels van dat kanaal een nieuwe plugin toestaan).

Niet tegelijk overal posten: dan kan Thijs niet op vragen reageren. Eén plek per dag.

Let op (GOK, niet kunnen lezen): de regels van de subreddits over eigen werk en over plugins die met AI gemaakt zijn. Reddit gaf geen antwoord op curl. Thijs: lees de regels in de zijbalk voor je post. Is er een regel over AI, zet dan de zin "Built with the help of AI tools, tested in the real Obsidian app before every release." onderaan. Eerlijk zijn gaat voor bereik.

## 1. Forum, Share & showcase

**Titel:** Rollwright: roll dice and random tables inside your notes

**Tekst:**
Hi all,

I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. You write a formula in a note, read the result, and click it to roll again.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.
- A roll history panel. Reading view and Live Preview look the same.

All rolling is free. Two extra looks are a one-time $6 purchase, which is how I hope to keep working on it. No account and no telemetry.

Install: Settings, Community plugins, search "Rollwright".
Full reference and source: https://github.com/thijsduinhouwer2002-coder/rollwright
Page: https://dortus.com/rollwright/

I'd love to hear what you roll on and what is missing. Bugs and ideas are welcome here or on GitHub.

[plaatje: lijst-2-live-preview.png uit `platformen/obsidian/lijst-plaatjes/`]

## 2. r/ObsidianMD

**Titel:** I made a dice roller plugin that rolls on your own tables and uses your frontmatter

**Tekst:** zelfde als het forumbericht, zonder de eerste regel "Hi all". Voeg toe als eerste zin na de titel: "Rollwright is now in Community plugins." Plaatje: lijst-2-live-preview.png en lijst-3-geschiedenis.png.

## 3. r/Solo_Roleplaying

**Titel:** For solo players who journal in Obsidian: a plugin to roll dice and oracle tables inside your notes

**Tekst:**
I play and keep my session logs in Obsidian, so I made a plugin for it: Rollwright.

You keep your oracles and random tables as normal notes. Then, in your journal, `dice: [[Oracles^yesno]]` picks a row, and a click rolls again. A lookup table can have a formula in its header (`dice: 1d20`) and Rollwright finds the matching row. You can roll a random line from a list, a block from a note, or a note with a tag. The roll history shows what you rolled and where it came from.

It is free (two optional skins cost $6 once) and needs no account. It is in Obsidian's Community plugins as "Rollwright".

More: https://dortus.com/rollwright/

[plaatje: lijst-1-lezen.png]

Let op Thijs: de eerste zin "I play and keep my session logs in Obsidian" alleen gebruiken als dat klopt. Zo niet, begin met: "Many solo players keep their session logs in Obsidian, so I made a plugin for it: Rollwright."

## 4. Discord #updates (kort)
Rollwright 0.2.0 is in Community plugins: roll dice and random tables inside your notes. Uses the `dice:` notation, rolls on your tables, lists, sections and tags, reads numbers from frontmatter, keeps a roll history. Free, two optional $6 skins. https://github.com/thijsduinhouwer2002-coder/rollwright

## Na het posten
- Reageer binnen een dag op vragen; een bug gaat als issue naar de repo, Olaf pakt hem op.
- Chris telt op dag 7 de downloads per bericht-dag (sprongen in community-plugin-stats.json) in `cijfers.md`.

## Bijwerking 8 nov 2026: concepten voor 0.3.0 (vervangen 1 tot 4 hierboven)

Door Chris. Waarom opnieuw: (a) we lanceren met 0.3.0, niet 0.2.0; (b) het nieuwe uiterlijk is het verhaal, niet de notatie; (c) bij Bison & Flex besloot ik dat Thijs niet "I made" zegt over code die hij niet zelf schreef (logboek 8 nov 00:40). Dat geldt hier net zo. De oude concepten 1 tot 4 blijven staan voor de geschiedenis, gebruik deze.

Volgorde en regels blijven gelijk: één plek per dag, eerst het forum, regels in de zijbalk van een subreddit lezen voor het posten. Pas posten als Rollwright in Community plugins staat. Het bewegende plaatje (GIF uit klus 8 van Daan) gaat mee waar dat kan: forum en Reddit tonen een GIF, de listing niet.

Thijs: vervang `[GIF]` door de GIF uit de README zodra die er is, en lees elke tekst na. Klopt een zin niet voor jou, haal hem weg.

### 1. Forum, Share & showcase

**Titel:** Rollwright: roll dice and random tables inside your notes (and make a natural 20 feel like one)

**Tekst:**
Hi all,

My small studio, Dortus, made Rollwright: a dice roller for people who run or play tabletop games in Obsidian. You write a formula in a note, read the result, and click it to roll again.

[GIF]

What we cared about most is the moment of the roll. Click a result and it tumbles and lands. The highest possible roll lights up gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened. Roll animations turn off if your system asks for reduced motion.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. Two extra skins, Parchment and Arcane, are a one-time $6 purchase, which is how we hope to keep working on it. No account and no telemetry. It was built with the help of AI tools and is tested in the real Obsidian app before every release.

Install: Settings, Community plugins, search "Rollwright".
Source and full reference: https://github.com/thijsduinhouwer2002-coder/rollwright
Page: https://dortus.com/rollwright/

I'd love to hear what you roll on and what is missing. Bugs and ideas are welcome here or on GitHub.

### 2. r/ObsidianMD

**Titel:** A dice roller plugin where a natural 20 actually lights up, and every roll you click goes into a Roll log

**Tekst:** zelfde als het forumbericht, zonder "Hi all". Eerste zin: "Rollwright is now in Community plugins." GIF bovenaan als het plaatje van de post. Waarom deze titel: op Reddit stemmen mensen op wat ze zien; de oude titel ging over frontmatter, dat zie je niet (GOK).

### 3. r/Solo_Roleplaying (een of twee dagen later)

**Titel:** For solo players who journal in Obsidian: roll dice and oracle tables in your notes, with a log of every roll

**Tekst:**
Many solo players keep their session logs in Obsidian, so my small studio, Dortus, made a plugin for it: Rollwright.

You keep your oracles and random tables as normal notes. Then, in your journal, `dice: [[Oracles^yesno]]` picks a row, and a click rolls again. A lookup table can have a formula in its header (`dice: 1d20`) and Rollwright finds the matching row. You can roll a random line from a list, a block from a note, or a note with a tag.

Every roll you click lands in a Roll log, grouped by note and session, with where it came from, so the log reads like the session. A natural 20 lights up gold, a 1 turns red.

It is free (two optional skins cost $6 once) and needs no account. It is in Obsidian's Community plugins as "Rollwright". Built with the help of AI tools, tested in the real Obsidian app before every release.

More: https://dortus.com/rollwright/

[plaatje: Roll log naast een notitie, plaatje 3 van de nieuwe reeks]

Let op: in deze subreddit zijn eerder plugins voor solo-spel getoond (Solo RPG Toolkit 39.327 downloads, Lonelog 6.196, Solo Oracle 83, GEZIEN in community-plugin-stats.json 8 nov). Rollwright is geen oracle of GM-emulator; de tekst zegt daarom alleen wat het doet: dobbelen en tabellen, met een logboek.

### 4. Discord #updates (kort)
Rollwright 0.3.0 is in Community plugins: roll dice and random tables inside your notes. Click to roll again, a natural 20 lights up gold, every roll you click goes into a Roll log by note and session. Uses the `dice:` notation, rolls on your tables, lists, sections and tags, reads numbers from frontmatter. Free, two optional $6 skins. Made by Dortus with the help of AI tools. https://github.com/thijsduinhouwer2002-coder/rollwright

### Wat Thijs nodig heeft om te posten (komt op lijst-thijs na de aanmelding)
1. Rollwright staat in Community plugins (aanmelding door Thijs).
2. De GIF uit de README (Daan en Olaf, klus 8).
3. Deze vier teksten, één per dag.

## Bijwerking 8 nov 2026 (run 6): twee momenten, skins pas in het tweede

Door Chris. Aanleiding: Thijs 8 nov 08:40: skins nee (te weinig verschil), aanmelden mag nu met het gratis deel, betere skins in een 0.3.x. De concepten 1 tot 4 van 0.3.0 hierboven blijven de basis, met deze wijzigingen.

### Waarom twee momenten
De eerste berichten geven de grootste piek aan aandacht (GOK). Op dat moment is het betaalde deel nog zwak. Alles in één keer posten betekent: de piek zonder iets wat het waard is om te kopen. Daarom:
- **Moment 1 (na de aanmelding, als Rollwright in Community plugins staat):** forum (Share & showcase) en een dag later r/ObsidianMD. Het verhaal is het gratis deel: de worp, de NAT 20, het Roll log, tabellen. Doel: bereik.
- **Moment 2 (als de nieuwe skins uit zijn en Thijs ze zag):** r/Solo_Roleplaying en Discord #updates, plus een antwoord onder het eigen forumbericht ("Update: two new skins ..."). Het verhaal: hoe je sessie eruit kan zien. Doel: geld. Solo-spelers bekijken hun notities het langst (GOK); daar telt het uiterlijk het meest.

Zo krijgt elk bericht een eigen reden en hoeft Thijs niet twee keer in dezelfde subreddit over hetzelfde te posten. Komen de nieuwe skins niet binnen ±2 weken na de aanmelding, dan gaat moment 2 toch door zonder skins (concept 3 hierboven, met de zin hieronder); bereik wachten heeft ook een prijs.

### Wijzigingen in de concepten van moment 1 (forum en r/ObsidianMD)
- De zin `All rolling is free. Two extra skins, Parchment and Arcane, are a one-time $6 purchase, which is how we hope to keep working on it.` wordt: `All rolling is free. There are optional paid skins, which is how we hope to keep working on it.`
  Waarom: eerlijk melden dat er iets te koop is, zonder reclame voor iets wat Thijs zelf zijn geld niet waard vindt. Geen belofte over nieuwe skins.
- Bij moment 2 zonder nieuwe skins: in concept 3 wordt "It is free (two optional skins cost $6 once) and needs no account." dan "It is free (optional paid skins) and needs no account."; in concept 4 wordt "Free, two optional $6 skins." dan "Free, with optional paid skins."
- Plaatje bij het bericht: de GIF (forum en Reddit tonen die), daarna de poster. Geen skins-plaatje.
- Verder ongewijzigd.

### Concept voor moment 2: aanvulling onder het eigen forumbericht (pas na de nieuwe skins)
Schrijf ik pas als de skins er zijn en ik ze in de schermen van Daan zie. Een tekst over iets wat nog niet bestaat, is een gok over het product; die zet ik niet klaar.

### Voor Thijs (komt op lijst-thijs zodra Olaf meldt dat Rollwright in Community plugins staat)
1. Dag 1: forumbericht (concept 1 van 0.3.0, met de wijziging hierboven).
2. Dag 2: r/ObsidianMD (concept 2, met de wijziging hierboven). Lees eerst de regels in de zijbalk.
3. r/Solo_Roleplaying en Discord pas bij moment 2.

## Bijwerking 8 nov 2026 (run 7): skins v2 zijn er, moment 2 wacht toch

Door Chris. Skins v2 mogen mee in 0.3.1 (Thijs 12:33), maar hij vindt het verschil nog te klein en wil dat Daan doorgaat; "geen haast: eerst komen de gebruikers voor het gratis deel".

**Beslissing:** moment 2 (r/Solo_Roleplaying, Discord #updates, update onder het forumbericht) gaat **niet** door op skins v2. Waarom: moment 2 verkoopt het uiterlijk, en de eigenaar zegt zelf dat dat uiterlijk nog niet af is; een bericht over skins die volgende week weer anders zijn, verspilt de enige keer dat we in r/Solo_Roleplaying iets nieuws brengen. De regel uit run 6 blijft: komt er binnen ±2 weken na de aanmelding geen skins-versie waar Thijs volmondig ja op zegt, dan gaat moment 2 door met het gratis deel als verhaal (concept 3 met de rustige zin).

**Moment 1 verandert niet.** De zin `All rolling is free. There are optional paid skins, which is how we hope to keep working on it.` blijft. Plaatje bij het bericht: GIF, dan poster. Geen skins-plaatje: het bericht gaat over het gratis deel. Wie de plugin opent, ziet de skins in de instellingen.

**Gelijktrekken met de vaste vorm (regel "Elk product"):** in concept 1 tot 4 van 0.3.0 wordt "lights up gold" overal "lands in gold", zoals in README, manifest en productpagina. In concept 4 (Discord) wordt "Rollwright 0.3.0 is in Community plugins" gewoon "Rollwright is in Community plugins", zonder versie. `[[#^id]]` uit 0.3.1 zet ik er niet bij: de berichten zijn al lang genoeg en het is geen reden om te klikken.

## Bijwerking 8 nov 2026 (run 8): Rollwright staat live, de berichten van moment 1 zijn klaar om te plakken

Door Chris. Aanleiding: Thijs 8 nov 13:04: Rollwright staat live op https://community.obsidian.md/plugins/rollwright (GEZIEN 8 nov: pagina laadt, 4 downloads, versie 0.3.0, knop "Add to Obsidian" opent `obsidian://show-plugin?id=rollwright`). Hij vraagt de berichten voor het forum, een dag later r/ObsidianMD, en Discord.

**Dit deel vervangt alle concepten hierboven voor moment 1.** De teksten hieronder zijn af: alle wijzigingen van run 6 en 7 zitten erin, Thijs hoeft niets meer samen te voegen. De oude concepten blijven staan voor de geschiedenis.

### Wat er veranderd is ten opzichte van de concepten
- **Discord gaat mee in moment 1**, op dag 3. Thijs noemt het zelf in zijn bericht; dat gaat voor mijn plan uit run 6 (Discord pas bij moment 2). Het verhaal blijft het gratis deel. r/Solo_Roleplaying blijft bij moment 2 (run 7).
- **Installeren via de link**, niet alleen "zoek in Community plugins". Rollwright staat (nog) niet in het oude bestand `community-plugins.json` van obsidian-releases (GEZIEN 8 nov: 10.096 plugins, Rollwright er niet bij). Of het zoekvak in de app al uit de nieuwe directory leest, kon ik niet nagaan (GOK). De link met de knop "Add to Obsidian" werkt in elk geval, dus die staat vooraan.
- **Eerlijk over AI (keuring controleur).** "Built with the help of AI tools" was te zacht: de code is geschreven door Claude-agents, niet door Thijs met hulp. Andere makers op het forum zeggen het ook zo (topic 121684: "An AI coding agent wrote much of it under my direction"). Daarom staat er nu op alle drie de plekken dat AI-agents de code schrijven en dat Thijs stuurt en test. Klopt "I direct and test" niet voor Thijs, dan past hij het aan; zachter maken mag niet.
- **Het blok "Disclaimer" van het forum.** Berichten in Share & showcase beginnen met drie vaste vragen (GEZIEN in twee recente berichten, 117125 en 118862; vermoedelijk het sjabloon van het forum): open bron, helemaal gratis, en "vibe-coded beyond the author's ability to comprehend how it works?". Ik heb ze ingevuld; de derde vraag gaat over Thijs als maker, dus hij leest die extra goed na.
- **Dezelfde woorden als README en listing:** "A natural 20 lands in gold", "Roll log", "Optional skins are a one-time purchase".
- Geen versienummer in de berichten: 0.3.1 kan elk moment komen, dan klopt een getal niet meer.

### Dag 1: forum, categorie Share & showcase (forum.obsidian.md)

**Titel:** `Rollwright: roll dice and random tables in your notes, where a natural 20 lands in gold`

**Tekst:**
```
Disclaimer
Is this plugin open source? Yes (MIT)
Is this plugin completely free? All rolling is free. Optional skins are a one-time purchase.
Is this plugin vibe-coded beyond the author's ability to comprehend how it works? No. The code is written by AI agents that our small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, in reading view and Live Preview, and the full source is on GitHub.
Community Directory: https://community.obsidian.md/plugins/rollwright

Hi all,

Rollwright is a dice roller for people who run or play tabletop games in Obsidian. You write a formula in a note, read the result, and click it to roll again.

[GIF]

What we cared about most is the moment of the roll. Click a result and it tumbles and lands. The highest possible roll lands in gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened. Roll animations turn off if your system asks for reduced motion.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are optional paid skins, which is how we hope to keep working on it. No account and no telemetry.

Install: open https://community.obsidian.md/plugins/rollwright and choose "Add to Obsidian".
Source and full reference: https://github.com/thijsduinhouwer2002-coder/rollwright
Page: https://dortus.com/rollwright/

I'd love to hear what you roll on and what is missing. Bugs and ideas are welcome here or on GitHub.
```

**Plaatjes:** sleep op de plek van `[GIF]` de GIF in het bericht: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/demo.gif (eerst opslaan, dan slepen). Onderaan mag de poster: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/poster.png . Geen skins-plaatje (run 7).

### Dag 2: r/ObsidianMD

**Titel:** `A dice roller plugin where a natural 20 lands in gold, and every roll you click goes into a Roll log`

**Tekst:**
```
Rollwright is now in Obsidian's community directory. It is a dice roller for people who run or play tabletop games in Obsidian: you write a formula in a note, read the result, and click it to roll again.

What we cared about most is the moment of the roll. Click a result and it tumbles and lands. The highest possible roll lands in gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are optional paid skins, which is how we hope to keep working on it. No account and no telemetry. The code is written by AI agents that our small studio, Dortus, runs; I direct and test it. Every release is tested in the real Obsidian app.

Install: https://community.obsidian.md/plugins/rollwright ("Add to Obsidian")
Source: https://github.com/thijsduinhouwer2002-coder/rollwright

Happy to answer questions here.
```

**Plaatje:** maak er een post met media van en zet de GIF als eerste (zelfde link als dag 1). Op Reddit stemmen mensen op wat ze zien (GOK). Lees vóór het posten de regels in de zijbalk (zelfpromotie, flair, AI). Reddit gaf curl geen antwoord, dus die regels heb ik niet kunnen lezen (GOK). Vraagt de subreddit een flair, kies iets als "Plugins" of "Showcase".

### Dag 3: Obsidian Discord

**Kanaal:** het kanaal waar makers nieuwe plugins mogen tonen. Ik kan Discord niet lezen; mijn eerdere aanname was `#updates` (GOK). Lees de beschrijving bovenaan het kanaal; staat er niet dat nieuwe plugins welkom zijn, sla Discord dan over.

**Tekst:**
```
Rollwright is now in the community directory: roll dice and random tables inside your notes. Click a result to roll again, a natural 20 lands in gold, and every roll you click goes into a Roll log by note and session. Uses the `dice:` notation, rolls on your tables, lists, sections and tags, reads numbers from frontmatter. All rolling is free, with optional paid skins. Code written by AI agents at our studio Dortus, tested in the real Obsidian app.
https://community.obsidian.md/plugins/rollwright
```
(Plak de GIF erbij als dat in het kanaal mag.)

### Na het posten
- Reageer binnen een dag op vragen. Een bug: open een issue op GitHub of zet het in `berichten/olaf.md`, dan pakt Olaf hem op.
- Chris meet op dag 1, dag 7 en dag 30 de downloads (listing en `community-plugin-stats.json`) en kijkt of er een sprong zit op de dag van elk bericht (`cijfers.md`).
- Moment 2 (r/Solo_Roleplaying, een update onder het forumbericht) blijft wachten op skins waar Thijs volmondig ja op zegt, uiterlijk ±22 nov (twee weken na de aanmelding); dan gaat het toch door met het gratis deel als verhaal (run 6 en 7).

## Bijwerking 8 nov 2026 (run 9): forumregels gelezen, forumtekst volgens de regels van Thijs van 13:47

Door Chris. Aanleiding: Thijs mag (13:47) de lanceerberichten nu door mij laten plaatsen, met vaste regels. Twee daarvan raken de tekst: lees eerst de regels van de plek, en zeg eerlijk dat Thijs de maker is ("I made this" en "Made by Thijs at Dortus").

### Regels van het forum (GEZIEN met curl, 8 nov ±12:45 UTC)
- Categorie Share & showcase (id 9): "Showcase your plugins, themes, CSS snippets, workflows, templates, and nifty hacks." Een nieuwe plugin tonen is dus precies waar de categorie voor is.
- De forumrichtlijnen (forum.obsidian.md/guidelines) zijn de gewone Discourse-richtlijnen: geen spam, niet dubbel posten, bijdragen aan het gesprek. Geen aparte regel tegen zelfpromotie, geen regel over AI, geen verplichte vermelding gevonden. Ook in de gebruiksvoorwaarden (forum.obsidian.md/tos) niets over reclame voor eigen plugins.
- Tags zijn niet verplicht, maar gebruikelijk: `plugin-release` (982 berichten) en `ttrpg` (4) bestaan. Kies die twee.
- Het blok "Disclaimer" bovenaan (drie vragen) staat in recente berichten in de categorie (run 8); we vullen het in.
- Dubbel posten: er is nog geen bericht over Rollwright in de categorie (GEZIEN, laatste 30 onderwerpen).

### Wat er verandert in de forumtekst van run 8
- Eerste zin wordt "I made Rollwright" en onderaan staat "Made by Thijs at Dortus", zoals Thijs eist. Om eerlijk te blijven over de code staat er direct bij dat AI-agents de code schrijven en dat Thijs stuurt en test (dat stond er al in de Disclaimer). Dit vervangt mijn besluit uit de bijwerking voor 0.3.0 (logboek 8 nov 00:40) dat Thijs geen "I made" zegt: de eigenaar heeft het nu zelf zo bepaald, en met de zin over AI is het waar.
- Verder ongewijzigd. Dit is de tekst die geplaatst wordt, door mij of door Thijs.

### Dag 1: forum, Share & showcase, tags `plugin-release` en `ttrpg`

**Titel:** `Rollwright: roll dice and random tables in your notes, where a natural 20 lands in gold`

**Tekst:**
```
Disclaimer
Is this plugin open source? Yes (MIT)
Is this plugin completely free? All rolling is free. Optional skins are a one-time purchase.
Is this plugin vibe-coded beyond the author's ability to comprehend how it works? No. The code is written by AI agents that my small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, in reading view and Live Preview, and the full source is on GitHub.
Community Directory: https://community.obsidian.md/plugins/rollwright

Hi all,

I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. You write a formula in a note, read the result, and click it to roll again.

[GIF]

What I cared about most is the moment of the roll. Click a result and it tumbles and lands. The highest possible roll lands in gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened. Roll animations turn off if your system asks for reduced motion.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are optional paid skins, which is how I hope to keep working on it. No account and no telemetry.

Install: open https://community.obsidian.md/plugins/rollwright and choose "Add to Obsidian".
Source and full reference: https://github.com/thijsduinhouwer2002-coder/rollwright
Page: https://dortus.com/rollwright/

I'd love to hear what you roll on and what is missing. Bugs and ideas are welcome here or on GitHub.

Made by Thijs at Dortus
```

**Plaatjes:** op de plek van `[GIF]` de GIF: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/demo.gif (bestaat, GEZIEN in de README). Onderaan mag de poster: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/poster.png .

**Dag 2 en 3 (r/ObsidianMD, Discord):** zelfde aanpassing als hierboven toepassen voordat ze geplaatst worden: "I made Rollwright" vooraan, "our small studio" wordt "my small studio", en de regel "Made by Thijs at Dortus" onderaan. Pas na minstens één dag en alleen als het forumbericht goed ging (regel 2 van Thijs).

## Bijwerking 8 nov 2026 (run 10): forumbericht staat, r/ObsidianMD klaar voor 9 nov

Door Chris. Het forumbericht is goedgekeurd en zichtbaar (GEZIEN 13:42 UTC, link in `berichten-geplaatst.md`). Volgens regel 2 van Thijs mag r/ObsidianMD op zijn vroegst een dag na de goedkeuring: **9 nov vanaf 13:45 UTC**, en alleen als er tot dan geen klacht of verwijdering op het forum kwam.

### Regels van r/ObsidianMD: nog niet gelezen
Reddit weigert curl (403 op `about/rules.json` en de wiki, GEZIEN 13:43 UTC). Ik heb dat niet omzeild. Wie plaatst, leest dus eerst in de browser de regels in de zijbalk en de wiki: zelfpromotie, verplichte flair, regels over AI. Staat er iets wat twijfel geeft (bijvoorbeeld "geen AI-projecten" of "zelfpromotie alleen in een vaste draad"): niet plaatsen en de vraag op de lijst van Thijs zetten (regel 3 van Thijs).

### Dag 2: r/ObsidianMD, definitieve tekst (zelfde beweringen als het forumbericht)

**Titel:** `I made a dice roller plugin where a natural 20 lands in gold, and every roll you click goes into a Roll log`

**Soort post:** met media, de GIF als eerste: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/demo.gif . Flair: wat de subreddit voor plugins voorschrijft.

**Tekst:**
```
I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. It is now in the community directory. You write a formula in a note, read the result, and click it to roll again.

What I cared about most is the moment of the roll. Click a result and it tumbles and lands. The highest possible roll lands in gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are optional paid skins (a one-time purchase), which is how I hope to keep working on it. No account and no telemetry. Open source (MIT).

To be upfront: the code is written by AI agents that my small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, and the full source is on GitHub.

Install: https://community.obsidian.md/plugins/rollwright ("Add to Obsidian")
Source: https://github.com/thijsduinhouwer2002-coder/rollwright

Happy to answer questions here.

Made by Thijs at Dortus
```

Wat anders is dan run 8: "I made" vooraan en in de titel, "I" in plaats van "we", "a one-time purchase" en "Open source (MIT)" zoals in de disclaimer op het forum, de AI-zin letterlijk gelijk aan het forum, "Made by Thijs at Dortus" onderaan. Geen nieuwe beweringen over het product, dus geen nieuwe keuring nodig (alles stond al in de gekeurde tekst van run 8 of in het forumbericht).

### Wie plaatst
Mijn geplande runs draaien in de cloud zonder Claude in Chrome (runs 8, 9 en nu 10: geen browser). Plaatsen gaat dus via de hoofdchat op de HP of door Thijs zelf, zoals bij het forum. Reddit is ook niet met curl te volgen, dus reacties onder de Reddit-post kan alleen iemand met de browser zien.

## Bijwerking 8 nov 2026 (run 15): plek 5 (r/Solo_Roleplaying) en plek 6 (awesome-dnd) klaargezet

Door Chris, op het besluit van Hans (8 nov 20:44, advies 24): plek 5 en 6 klaarzetten. De oude Solo-tekst (deel "Bijwerking 8 nov", punt 3) vervalt: die zei nog "my small studio made", "lights up gold", "two optional skins cost $6" en "with the help of AI tools". Alles hieronder is getoetst aan de README van 0.3.2 (GEZIEN, curl 8 nov 20:50 UTC) en zegt niets wat het forumbericht of de Reddit-tekst van run 10 niet ook zegt, behalve de twee zinnen over orakels uit je eigen notities (die staan letterlijk in de README: `[[Note^id]]` geeft "a random row of that table, or a random item of that list", en lookup tables).

### Plek 5: r/Solo_Roleplaying, op zijn vroegst ±16 nov

**Voorwaarden (alle vijf, anders niet plaatsen):**
1. r/ObsidianMD (9 nov) en de Discord (op zijn vroegst 10 nov) zijn gelukt zonder klacht, waarschuwing of verwijdering (regel 2 en 7 van Thijs).
2. Een week na r/ObsidianMD, zodat het effect per plek te meten is.
3. De afrekenpagina van Polar is af (punt op de lijst van Thijs). Wie op "one-time purchase" klikt, moet een nette pagina zien.
4. Wie plaatst, leest eerst in de browser de regels in de zijbalk en de wiki (Reddit geeft 403 op curl, GEZIEN ook nu 20:52 UTC, niet omzeild). Let vooral op: een regel over zelfpromotie (bijvoorbeeld alleen in een vaste draad, of een verhouding meedoen en promoten), een regel over AI, en de flair. Verwacht is "tool-questions-and-sharing" (DERDEN, https://gummysearch.com/r/Solo_Roleplaying/). Kijk in dezelfde zijbalk of er eisen aan het account zijn (karma, leeftijd). Twijfel: niet plaatsen, vraag op de lijst van Thijs (regel 3).
5. **Wie plaatst:** de hoofdchat (met Chrome op de HP) of Thijs zelf. Mijn geplande runs hebben geen browser.

**Titel:** `I made a dice and random table roller for solo players who journal in Obsidian, with a log of every roll you click`

**Soort post:** met media, het plaatje van de Roll log naast een notitie eerst: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/roll-log.jpg (staat in de README, GEZIEN). Flair: wat de subreddit voor tools voorschrijft.

**Tekst:**
```
I made Rollwright, a plugin for people who keep their solo sessions in Obsidian. You write a roll in your journal, read the result, and click it to roll again.

For solo play the useful part is that your oracles can just be notes. Keep a yes/no list or a table with a block id, then `dice: [[Oracles^yesno]]` in your journal picks a random row or item. A lookup table can have a roll in its first header, like `dice: 1d20`, and Rollwright picks the matching row. You can also roll a random line, a block from a note, or a note with a tag.

Every roll you click goes into a Roll log, grouped by note and session, so afterwards you can read back how the session went. The highest possible roll lands in gold and the lowest turns red.

It is not an oracle or a GM emulator itself: it rolls dice and your own tables. It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working.

All rolling is free. There are optional paid skins (a one-time purchase) that only change the look. No account and no telemetry. Open source (MIT).

To be upfront: the code is written by AI agents that my small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, and the full source is on GitHub.

Install: https://community.obsidian.md/plugins/rollwright ("Add to Obsidian")
Source: https://github.com/thijsduinhouwer2002-coder/rollwright

Happy to answer questions here.

Made by Thijs at Dortus
```

Waarom zo: in deze subreddit zijn orakels en tabellen het onderwerp, en er zijn al solo-plugins (Solo RPG Toolkit 39.327 downloads, GEZIEN 8 nov). Daarom zegt de tekst eerlijk wat Rollwright niet is (geen oracle of GM-emulator) en zet hij het rollen op je eigen tabellen vooraan, niet de NAT 20. De AI-zin is letterlijk gelijk aan het forum en r/ObsidianMD.

### Plek 6: awesome-dnd, één pull request, **alleen Thijs zelf**

**Nieuw gevonden (GEZIEN, curl 8 nov 20:50 UTC):** de repo heeft een sjabloon voor pull requests (`.github/PULL_REQUEST_TEMPLATE.md`) met een verplichte afvinklijst. Twee punten daaruit:
- "I am a human, a good community member, and because of this I also made a comment on at least one other pull request about how the requested resource is awesome or not."
- "I've visited the link and verify that I think it is totally awesome."

Gevolg: deze pull request kan **niet via de hoofdchat**. Een Claude kan niet naar waarheid "I am a human" afvinken, en een reactie op de pull request van een ander zou een bericht onder de naam van Thijs zijn bij iemand anders, wat regel 4 en 5 van Thijs niet toestaan. Thijs doet hem dus zelf, of slaat hem over. Dat is eerlijk en past bij de beheerder, die precies dit vraagt. Het plan noemde het sjabloon nog niet; aangepast in `verspreiding.md`.

**Overige regels (GEZIEN, CONTRIBUTING.md):** één bron per pull request; "Recommend something you've actually tried"; "Keep it relevant to D&D or system-agnostic tabletop play" (Rollwright is systeemvrij, met D&D-notatie, past); "Disclose your connection to the resource. Self-promotion is welcome; as long as it is made clear."; AI: "Describe any AI features readers will encounter on the requested link". Vorm: `- [Naam](link) - Korte, feitelijke beschrijving met een punt.` Er staat nog geen dobbelsteen-tool en geen Obsidian-plugin op de lijst (alleen Obsidian Portal, een andere site, GEZIEN).

**Waar in de lijst:** onder `## Desktop Applications` ("Things to download and install"), onderaan. Tweede keuze `### Campaign Tracking`; die keuze laten we aan de beheerder.

**De regel (met punt aan het eind, zoals de regels vragen):**
```
- [Rollwright](https://community.obsidian.md/plugins/rollwright) - Open source Obsidian plugin that rolls dice and random tables inside your campaign notes and logs every roll you click.
```
(Korter dan in run 11: "free" en de skins staan al in de tekst van de pull request, en de regels vragen een korte beschrijving.)

**Titel van de pull request:** `Add Rollwright (dice and random tables in Obsidian notes)`

**Tekst, in het sjabloon:**
```
## What's changing?

Adds one resource, Rollwright, under Desktop Applications. Campaign Tracking could also fit; happy to move it.

## New resource

**Resource URL:** https://community.obsidian.md/plugins/rollwright

**Why add it alongside the resources already listed?**
The list has nothing for Obsidian, which many DMs use for campaign notes, and no dice roller that works inside your notes. Rollwright rolls dice and your own random tables (including lookup tables with a d20 in the header) right inside your notes, and keeps a log of every roll you click per session. It works for D&D and system-agnostic play.

**Are you affiliated with the requested website?**
Yes. I made it (Thijs, Dortus). All rolling is free and open source (MIT); optional paid skins only change the look.

**AI disclosure:**
None in the plugin itself: it has no AI features and only goes online to check a skin license key. The code is written by AI agents that my small studio runs; I direct and test it.

## Checklist

- [x] I've visited the link and verify that I think it is totally awesome.
- [x] I've checked the list and previous issues and PRs for duplicates.
- [x] This PR adds exactly one resource in the appropriate category, or if it adds an additional category, then the table of contents is also updated.
- [x] The entry has a short, factual description ending with punctuation.
- [x] I am a human, a good community member, and because of this I also made a comment on at least one other pull request about how the requested resource is awesome or not. Because I am invested in making this an awesome resource long into the future!
```

**Wat Thijs zelf eerst doet:** (1) Rollwright zelf een keer gebruiken in een notitie (regel "something you've actually tried"). (2) De open pull requests en issues doorzoeken op "Rollwright" en "dice" (dubbel). (3) Bij één open pull request van een ander een eerlijke reactie zetten over die bron, in zijn eigen woorden; alleen als hij die bron echt bekeek. (4) Pas dan de pull request: fork, de regel onderaan Desktop Applications, de tekst hierboven. Vinkt hij iets niet naar waarheid af: niet indienen.

Waarom het toch de moeite is: klein bereik (307 sterren, GEZIEN run 11), maar het blijft staan en het is de enige plek op dit plan die mensen buiten Obsidian bereikt.

### Keuring run 15
Controleur (los van mij, curl op README, CONTRIBUTING, sjabloon en lijst): **akkoord mits**. Moet: "the list has no dice roller yet" klopte niet (Avrae, een dobbelbot, staat onder Discord Bots), aangepast naar "nothing for Obsidian ... and no dice roller that works inside your notes". Kan, verwerkt: "row or item" voor lijsten; regel voor de lijst korter; voorwaarde over accounteisen en wie plaatst. Rood voor de laagste worp staat niet in de README maar wel in de code (`src/rollers/extreme.ts`, max en min) en al in het gekeurde forumbericht. Conclusie dat alleen Thijs de pull request kan doen: juist volgens de controleur.

## Bijwerking 9 nov 2026 (run 20): welk beeld bij het r/ObsidianMD-bericht, en één eerlijke zin bij de video

Door Chris, 9 nov ±01:50 UTC. Aanleiding: Daan legde Thijs een nieuwe film voor (lijst-thijs 8 nov 22:45, ja of nee vóór 9 nov 11:00 UTC): `ontwerp/rollwright/demo-v3.mp4` (16 s, 1280x720, h264, 1,9 MB, GEZIEN met ffprobe) en `demo-v3.gif` (6,9 MB). De tekst van run 10 hierboven gaat uit van de oude GIF. Hieronder staat wat de hoofdchat om 13:45 UTC kiest, zodat het bericht in beide gevallen klopt.

### Wat ik in de film zag (GEZIEN, 8 beelden uit de mp4, één per 2 seconden; de controleur bekeek er 16)
1. Titelkaart "Roll dice right in your notes." met een d20.
2. Het echte venster (rustige Classic): Initiative wordt 13, Damage wordt 13, Wisdom save wordt 20 met het stempel NAT 20 in goud.
3. De NAT 20-kaart wordt groot uit het venster getild met "CRITICAL HIT", warm licht en stralen erachter, onderschrift "A natural 20 lands in gold." met eronder "Free. Click any roll in your note to throw it again."
4. Het logboek vult: Wisdom save 20 (NAT 20), Damage 13, 13. Dat klopt met de drie worpen; rond 13 s schuift het door en is ook een oudere regel "7, 2d6 + 3" te zien, de Damage van vóór de film (gezien door de controleur). Klopt dus, met die ene oudere worp erbij. Onderschrift "Every throw, kept in a session log."
5. Eindkaart: "Live rolls · random tables from your notes · a log for every session", knop "Free in Obsidian Community Plugins", "Made by Thijs at Dortus".

Alles wat de film beweert, staat ook in de gekeurde tekst van run 10 (gouden natuurlijke 20, NAT 20-stempel, een log per sessie, tabellen uit je notities, gratis). Geen nieuwe belofte. Eén ding verdient een zin: het vergroten van de kaart, het woord "CRITICAL HIT", het licht, de stralen en de vonken zitten **niet** in de plugin (de plugin toont alleen het stempel NAT 20). Ook is de film geen doorlopende opname: het venster bestaat uit schermafbeeldingen uit een automatische testrun in de echte app, achter elkaar gezet, en de opgetilde kaart is een uitsnede uit een andere run (Daan zegt dat zelf in `ontwerp/rollwright/bron/film-v3/LEESMIJ.md`). Op Reddit zien mensen eerst het beeld; wie de plugin installeert en geen stralen ziet, voelt zich bedrogen. Volgens regel 5 van Thijs ("alleen beweren wat klopt") zeggen we het dus zelf, in één zin.

### Wat de hoofdchat kiest
**A. Thijs zei "GIF ja" (of "ja") in de projectchat vóór het plaatsen:**
- Soort post: met media, en upload de mp4 als video: download eerst https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/demo-v3.mp4 (opent meestal als speler: rechtsklik, "Video opslaan als"). Een video speelt op Reddit vanzelf af en is scherper dan een GIF van 6,9 MB (GOK, ook het advies van Daan). 16 s en 1,9 MB ligt ver onder de grenzen van Reddit (DERDEN, onder meer https://www.tella.com/blog/how-to-post-videos-on-reddit ; geen officiële bron gelezen, dus de hoofdchat ziet het in het formulier).
- Titel en tekst: precies die van run 10, met **één extra regel** direct onder de eerste alinea:
```
(The zoom, the light, the rays and the "Critical hit" label around the card are added for the video. Everything inside the Obsidian window is the free plugin as it is, captured from the real app.)
```
- Laat het formulier geen tekst toe bij een video: kies dan een gewone tekstpost met precies dezelfde titel en tekst, en zet de video erin als ingevoegd medium (knop voor afbeelding of video in de editor). Lukt ook dat niet: optie B.

**B. Thijs zei nee, of heeft om 13:45 UTC nog niets gezegd:**
- Alles zoals in run 10: de GIF https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/demo.gif (200, 2,1 MB, GEZIEN 01:46 UTC). Geen extra regel, want die GIF is alleen het venster zelf.
- Niet wachten op het antwoord: het bericht gaat om 13:45 UTC of later de deur uit, met het beeld dat op dat moment akkoord is.

Let op bij A: zet Olaf `demo-v3.gif` al als `images/demo.gif` in de repo rollwright (zoals Daan voorstelt), dan staat die film ook in de README. Dan geldt de extra regel ook voor optie B, omdat dezelfde beelden in de GIF zitten. Kijk dus vlak voor het plaatsen naar de GIF in de repo: is het de film met de opgetilde kaart, zet de regel er dan in, wat je ook kiest.

### Blijft gelden uit run 10 en 11
Eerst de zijbalk en de regels van r/ObsidianMD in de browser lezen (Reddit geeft 403 op curl, opnieuw GEZIEN 01:46 UTC, niet omzeild). De gedragscode van Obsidian geldt ook op r/ObsidianMD en zegt: "paid content will always receive additional scrutiny" en "We expect folks to engage meaningfully before promoting their work" (GEZIEN, opnieuw gelezen 01:48 UTC, https://raw.githubusercontent.com/obsidianmd/obsidian-help/master/en/Obsidian/Community%20code%20of%20conduct.md). Daarom staat in de tekst dat alle dobbelen gratis is en reageert Thijs (of de hoofdchat) op elke vraag in de eigen draad. Twijfel over de regels: niet plaatsen, op de lijst van Thijs.

### Nog even nagekeken (GEZIEN 01:45 tot 01:50 UTC)
- Links in het bericht: listing https://community.obsidian.md/plugins/rollwright 200, repo 200, GIF 200.
- De korte tekst op de listing en in `community-plugins.json` is nog die van 0.3.0 ("keep a history of every roll"), dus advies 29 is nog niet uitgevoerd. Het staat bovenaan lijst-thijs. Het bericht zelf hangt er niet van af; het is wel wat mensen zien als ze na het lezen in Obsidian zoeken.
- Afrekenpagina van de skins: beschrijving staat erop, nog steeds geen plaatje (`medias: []`, GEZIEN). Punt staat al op lijst-thijs (regel van 8 nov 22:45); geen nieuwe regel.

### Keuring run 20
Controleur (los van mij, 16 beelden uit de mp4, LEESMIJ en `frames.json`, links en gedragscode met curl): **akkoord mits**. Moet, verwerkt: (1) "recorded in one take" klopte niet (losse schermafbeeldingen uit een testrun, uitsnede uit een andere run) en de zin noemde alleen licht en vonken; nieuwe zin noemt vergroten, licht, stralen en "Critical hit" en zegt "captured from the real app"; (2) het logboek toont ook een oudere Damage 7. Kan, verwerkt: tweede onderschrift genoemd, uitleg mp4 opslaan. Kan, doorgegeven: "één opname" in het voorstel van Daan op lijst-thijs is strikt genomen niet juist (in mijn logboek, voor Daan).

## Bijwerking 9 nov 2026 (run 26): r/ObsidianMD, DEFINITIEF met trailer v4 B als video

Door Chris, 9 nov ±07:45 tot 08:30 UTC, op het bericht van Thijs van 9 nov 08:00. **Dit deel vervangt de keuze A of B van run 20 en het beeld van run 10.** Plaatsen gaat via de hoofdchat, op zijn vroegst **9 nov 13:45 UTC (14:45 NL)**. Titel en tekst hieronder zijn letterlijk te plakken.

### Vlak voor het plaatsen (hoofdchat, ±3 min)
1. Forumdraad nog in orde? https://forum.obsidian.md/t/121721.json : niet gesloten, geen klacht of waarschuwing van een moderator (regel 2 en 7 van Thijs). Stand GEZIEN 07:47 UTC: 1 bericht (alleen dat van Thijs), 19 keer bekeken, niet gesloten, zichtbaar.
2. Lees in de browser de zijbalk en de regels van r/ObsidianMD (Reddit geeft 403 op curl; niet omzeild, ook geen spiegelsites gebruikt). Let op: zelfpromotie, verplichte flair, regels over AI of over video. Twijfel: niet plaatsen, vraag op lijst-thijs (regel 3).
3. Download de video: https://raw.githubusercontent.com/thijsduinhouwer2002-coder/dortus-hq/main/ontwerp/rollwright/v4/demo-v4-b.mp4 (200, 3,5 MB, 16,6 s, 1280x720, h264, GEZIEN 07:47 UTC). Opent meestal als speler: rechtsklik, "Video opslaan als".

### Soort post
Post met media: upload de mp4 als video, en zet de tekst in het tekstveld eronder. Flair: wat de subreddit voor plugins voorschrijft (bijvoorbeeld "Plugins" of "Showcase"; kies volgens de zijbalk). Laat het formulier geen tekst toe bij een video: maak een gewone tekstpost met precies dezelfde titel en tekst en voeg de video in met de knop voor afbeelding of video in de editor. Lukt ook dat niet: dan de GIF https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/demo.gif (dezelfde film, zelfde md5 als `demo-v4-b.gif`, GEZIEN), met dezelfde tekst.

### Titel
```
I made a dice roller plugin where a natural 20 lands in gold, and every roll you click goes into a Roll log
```

### Tekst
```
I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. It is now in the community directory. You write a formula in a note, read the result, and click it to roll again.

About the video, to be clear: the parchment look of the note (the paper, the fonts, the banner, the pinned handout, the cards and the wolf and trap icons) is my own CSS snippet, not part of the plugin. The bestiary pages, the titles and captions, the zoom, and the rays, sparks and red glow were added for the video. The dice, the gold and red results and the Roll log are the free plugin, captured from the real app. Parchment and Arcane at the end are optional paid skins.

What I cared about most is the moment of the roll. Click a result and the die turns and the new number lands. The highest possible roll lands in gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are optional paid skins (a one-time purchase), which is how I hope to keep working on it. No account and no telemetry. Open source (MIT).

To be upfront: the code is written by AI agents that my small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, and the full source is on GitHub.

Install: https://community.obsidian.md/plugins/rollwright ("Add to Obsidian")
Source: https://github.com/thijsduinhouwer2002-coder/rollwright

Happy to answer questions here.

Made by Thijs at Dortus
```

### Wat anders is dan run 10, en waarom
- **Tweede alinea is nieuw** (op verzoek van Thijs): de perkamentstijl is eigen CSS en geen deel van de plugin, Parchment en Arcane zijn optionele skins. Ik heb er de bestiariumbladen, de zoom, de stralen en de onderschriften bij gezet, omdat die ook niet in de plugin zitten (Daan zegt dat zelf in `ontwerp/rollwright/v4/bron/LEESMIJ.md` en `voor-projectchat.md`). Het staat bovenaan, direct na de eerste zin, zodat niemand eerst de film ziet, installeert en zich bedrogen voelt. Het woord "paid" bij de skins staat er met opzet: de gedragscode van Obsidian zegt "paid content will always receive additional scrutiny".
- De wolf en val in de notitie zijn plaatjes in de snippet (game-icons.net, Lorc, CC BY 3.0, volgens Daan), daarom staan ze in het rijtje van de snippet.
- "it tumbles and lands" werd "the die turns and the new number lands": sinds 0.3.2 maakt de d20 in de gratis Classic alleen een kwartslag en vervaagt het getal in beeld (CHANGELOG 0.3.2, GEZIEN); tuimelen is van de betaalde skins. Het forumbericht is ouder en blijft zoals het is (één draad, niet bewerken voor dit kleine punt).
- Verder letterlijk de gekeurde tekst van run 10. Geen nieuwe belofte over wat de plugin doet.

### Wat ik zelf in de film zag (GEZIEN, 9 beelden, één per 2 s, plus het laatste beeld)
Haak "NAT 20" met de kaart Perception 22 en stralen; titel "ROLLWRIGHT, Dice that roll inside your notes"; het venster met de notitie "The Drowned Lantern" op perkament; drie bestiariumbladen naast het venster (The Wolf bij Attack 23, The Trap bij Dex save 2 met NAT 1 in rood, onderschrift "A natural 1 lands in red", The Lantern bij Perception 22 met NAT 20, onderschrift "A natural 20 lands in gold"); het Roll log met Perception 22 NAT 20, Dex save 2 NAT 1, Damage 11 ("Every throw, kept in your session log"); Parchment en Arcane naast elkaar, elk "OPTIONAL SKIN"; eindkaart "A natural 20 lands in gold. Every throw, kept.", knop "Free in Obsidian Community Plugins", "Parchment and Arcane: optional skins", "Made by Thijs at Dortus". Onderin de meeste beelden: "Real plugin footage · Obsidian". Alles wat de film over de plugin beweert, staat in de tekst of in de README van 0.3.3.

### Ook nagekeken (GEZIEN 07:47 UTC)
- Listing https://community.obsidian.md/plugins/rollwright 200, met de nieuwe korte tekst ("A natural 20 lands in gold ... keep your rolls in a Roll log"). `community-plugins.json` op GitHub heeft nog de oude tekst; dat is de lijst die Obsidian zelf bijhoudt en volgt later (GOK).
- README op main van de repo rollwright is 0.3.3 en toont dezelfde film als `images/demo.gif`, met eronder dezelfde eerlijke regel over de snippet en de skins. Bericht en README zeggen dus hetzelfde.
- Downloads: 9 (GEZIEN, community-plugin-stats.json). Dat is de nulmeting voor Reddit.

### Antwoorden klaar voor de draad (concepten, alleen in de eigen draad, kort)
- **"Can I get the CSS snippet?"** `It's a quick snippet I made for the video, not something I've polished for sharing yet. If more people want it I'll look at cleaning it up for the repo.` (Niets beloven met een datum. Wil Thijs hem delen, dan maakt de ploeg hem netjes; de iconen zijn CC BY 3.0 (Lorc), dus alleen met naamsvermelding.)
- **"So the free version doesn't look like this?"** `The rolls, the gold natural 20, the red natural 1 and the Roll log are all free. In the video they sit on my parchment CSS snippet; in your vault the free look takes your theme's colours and fonts. Parchment and Arcane, shown at the end, are the two paid skins.`
- **"Why not just use Dice Roller?"** `Dice Roller is great and Rollwright reads the same dice: notation. I wanted the roll itself to feel like a moment and to keep a log of every roll you click, per session. If Dice Roller does what you need, stick with it.`
- **"AI-written, no thanks."** Niet in discussie gaan. Hooguit: `Fair enough. I wanted to be upfront about it. The source and the tests are public if you want to judge the code.`
- Vragen over geld, terugbetalen, privacy of juridisch: niet beantwoorden, bovenaan lijst-thijs (regel 5).

### Na het plaatsen
De hoofdchat zet de link, datum en de volledige tekst in `commercie/rollwright/berichten-geplaatst.md` en één regel op lijst-thijs (regel 6). Reddit is niet met curl te volgen; ik meet het effect met de downloads (dag 1 na het bericht, dag 3, dag 7) tegen de lat in `groeimaat.md`. Discord (plek 3) op zijn vroegst een dag na Reddit en alleen zonder klachten of verwijdering.

### Keuring run 26
Controleur (los van mij; 17 beelden uit de mp4 plus het laatste, README, LICENSE, CHANGELOG en code van 0.3.3, forumbericht, links en gedragscode met curl): **akkoord mits**. Moet, verwerkt: (1) de eerlijke alinea miste de vonken, het rode waas en de titelkaarten, en "are added" werd "were added"; (2) "tumbles" klopt niet meer voor de gratis Classic sinds 0.3.2; (3) het concept "look like the window in the video" beloofde te veel, want gratis neemt de kleuren en letters van je eigen thema. Kan, verwerkt: handout en kaarten in het rijtje van de snippet, "every roll you click" in het antwoord over Dice Roller, zachtere zin over de snippet met de CC BY-voorwaarde. Bevestigd: alle beweringen kloppen met 0.3.3 (ook "highest possible roll lands in gold": MAX krijgt dezelfde gouden stijl), alle links 200 (github.com gaf via de proxy 504, de API zegt publiek en MIT), Engels zonder gedachtestreepjes. Niet te controleren: de zijbalk van r/ObsidianMD (403); stap 2 blijft dus nodig.
