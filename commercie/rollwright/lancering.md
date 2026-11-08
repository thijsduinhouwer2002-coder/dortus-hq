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
