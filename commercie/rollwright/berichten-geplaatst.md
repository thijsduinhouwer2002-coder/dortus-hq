# Rollwright: geplaatste lanceerberichten

Door Chris. Per bericht: datum, plek, link, of wat er misging.

| Datum | Plek | Link | Uitkomst |
|---|---|---|---|
| 8 nov 2026 ±14:55 UTC | forum.obsidian.md, Share & showcase | geen | niet geplaatst, zie hieronder |
| 8 nov 2026 ±12:50 UTC (13:50 NL) | forum.obsidian.md, Share & showcase | geen | niet geplaatst: geen browser, zie poging 2 |

## Poging 1, 8 nov 2026 (run 8): niet geplaatst
Opdracht: testbericht van Thijs 13:47 in `berichten/chris.md`: alleen het forumbericht plaatsen via Claude in Chrome.

Wat er gebeurde, precies:
1. Het bericht van 13:47 kwam binnen tijdens deze run (bij `git pull --rebase` om ±14:50), nadat de tekst al af was.
2. **De opdracht van deze geplande run staat het niet toe.** Daarin staat letterlijk: "Nooit: inloggen op mijn accounts of accounts aanmaken, betalen, ..., of posten onder mijn naam. Zulke stappen zet je klaar op organisatie/lijst-thijs.md." Het bericht zegt "Je opdracht is aangepast", maar die aanpassing zat niet in de opdracht die deze run meekreeg (misschien gestart vóór de wijziging). Een regel in de repo zet ik niet boven de opdracht van de taak.
3. **Er was geen browser.** Deze run draait in de cloud, zonder koppeling met de computer van Thijs (geen device bridge, geen lokale MCP's). ToolSearch op "chrome browser navigate" gaf geen enkel hulpmiddel. Claude in Chrome draait in de Chrome van Thijs' HP; daar kan deze run niet bij.
4. Niets geprobeerd te omzeilen, niets ingelogd.

Wat de projectchat kan doen om het op te lossen:
- Controleer of de opdracht van de geplande taak Chris (`trig_018P1UU92oKaFFSBao5KRhQf`) de nieuwe regel over zelf posten echt bevat, en haal daar de zin "posten onder mijn naam" bij "Nooit" weg of maak een uitzondering voor lanceerberichten.
- Zet in de taak "Require this computer" aan (in de Claude desktop-app, op de HP), anders heeft een run geen Claude in Chrome. Of laat de projectchat het bericht één keer plaatsen.
- De tekst om te plaatsen: `commercie/rollwright/lancering.md`, deel "Bijwerking 8 nov 2026 (run 8)", dag 1.

Let op bij poging 1: de tijd "±14:55 UTC" is waarschijnlijk Nederlandse tijd; de commit van die run staat op 12:49 UTC.

## Poging 2, 8 nov 2026 (run 9, ±12:45 tot 13:05 UTC): niet geplaatst
Wat er gebeurde, precies:
1. **De opdracht van deze run staat het nu wel toe.** De geplande taak kreeg de "Extra toestemming van Thijs voor Chris (8 nov 2026, 13:47)" met de zeven regels. Punt 2 van poging 1 is dus opgelost.
2. **Er was weer geen browser.** Deze run startte als geplande taak in de cloud. De omgeving meldt zelf: "Nothing on the user's computer is reachable from here: no desktop bridge, no local MCP servers, no local files", en "This scheduled task does not require a computer, so its runs stay in the cloud." ToolSearch op "claude-in-chrome browser tabs navigate" gaf geen enkel Chrome-hulpmiddel (alleen Gmail en Claude Docs, die we niet gebruiken). Ook geen knop om Chrome aan te zetten (geen `enable__mcp__claude-in-chrome`).
3. Volgens regel 1 van Thijs: één keer geprobeerd, genoteerd, niet herhaald. Niets ingelogd, niets omzeild.
4. Wel gedaan: de forumregels gelezen met curl en de tekst volgens de regels van 13:47 klaargezet (`lancering.md`, run 9). Bij de volgende poging kan het bericht dus meteen geplaatst worden.

Waar het vastzit: **een geplande taak in de cloud heeft nooit Claude in Chrome**, hoe vaak hij ook draait. Oplossing (alleen Thijs kan dit, op de HP):
- Open in de Claude desktop-app op de HP de geplande taak "Chris - Commercieel manager" en zet **"Require this computer"** aan (als zijn account dat aanbiedt). Dan draaien de runs met de HP erbij en is Claude in Chrome er, mits de HP aanstaat en Chrome open is met de extensie.
- Of: Thijs plakt dit ene bericht zelf (titel, tekst en tags staan in `lancering.md`, run 9), of laat de projectchat (die wel bij de browser kan) het plaatsen. Daarna leg ik de link hier vast en ga ik verder met reageren en de volgende plekken, zodra ik bij de browser kan.

## Poging 3, 8 nov 2026 (extra run op verzoek van Thijs, ±13:00 UTC): niet geplaatst
Vastgelopen bij stap 1: verbinden met de browser. ToolSearch op "chrome" gaf "No matching deferred tools found". Ook deze run draaide in de cloud zonder koppeling met de HP. Eén keer geprobeerd, niet herhaald. Oplossing blijft dezelfde als bij poging 2.

## Poging 4, 8 nov 2026 ±13:10 UTC: ingediend, wacht op goedkeuring moderator
Door de hoofdchat (Claude, met Thijs erbij), via Claude in Chrome op de HP.
- Thijs maakte eerst zelf een forumaccount: **Thijs.Dortus** (trust level 0, nieuw). Het forum heeft een eigen login, los van community.obsidian.md.
- Plek: forum.obsidian.md, Share & showcase > **Plugins** (category 22), tags `plugin-release`, `ttrpg`.
- Het formulier opent met een vast sjabloon met regels, gelezen: (1) alleen plugins die in de community directory staan; (2) alle updates van de plugin in deze ene draad posten, geen nieuwe draden; (3) het Disclaimer-blok bovenaan laten staan; (4) lost je plugin een open feature request op, dan mag je daar een KORT bericht met een link naar deze draad zetten; (5) nieuwe accounts mogen geen links: zet links als inline code. Daarom staan alle links als `code`.
- Na "Create Topic": melding "Post Needs Approval": een moderator moet het eerst goedkeuren. Nog geen link. Chris: kijk bij je volgende run (curl op https://forum.obsidian.md/u/Thijs.Dortus/activity/topics.json) of het onderwerp zichtbaar is en zet dan de link hier.
- Wijziging t.o.v. run 9: bij "completely free?" staat nu eerst "No." (want skins kosten geld; alleen "All rolling is free" was een ontwijkend antwoord op een ja/nee-vraag). Links als inline code. Kop "## Disclaimer" en een lijn eronder.

Titel: `Rollwright: roll dice and random tables in your notes, where a natural 20 lands in gold`

Volledige tekst:
```
## Disclaimer

Is this plugin open source? Yes (MIT)
Is this plugin completely free? No. All rolling is free; optional skins are a one-time purchase.
Is this plugin vibe-coded beyond the author's ability to comprehend how it works? No. The code is written by AI agents that my small studio, Dortus, runs. I direct and test the work; I don't write the code myself. Every release runs automated tests in the real Obsidian app, in reading view and Live Preview, and the full source is on GitHub.
Community Directory: `https://community.obsidian.md/plugins/rollwright`

---

Hi all,

I made Rollwright, a dice roller for people who run or play tabletop games in Obsidian. You write a formula in a note, read the result, and click it to roll again.

![Rollwright demo](https://raw.githubusercontent.com/thijsduinhouwer2002-coder/rollwright/main/images/demo.gif)

What I cared about most is the moment of the roll. Click a result and it tumbles and lands. The highest possible roll lands in gold, a natural 20 gets a NAT 20 stamp, and the lowest turns red. Every roll you click goes into a Roll log, grouped by note and session, so after a session you can read back what happened. Roll animations turn off if your system asks for reduced motion.

It uses the same `dice:` notation as the Dice Roller plugin, so notes you already have should keep working. On top of that:

- Roll on your own tables, lists, sections, single lines and tagged notes. A lookup table picks the row that matches a roll.
- `dice+:` keeps a result after a restart, `dice-mod:` writes the result into the note after you confirm.
- Numbers from your frontmatter work in a roll: with `str: 3`, `dice: 1d20 + str` adds 3.
- Keep highest, exploding dice, rerolls, success counting, Fudge dice and Genesys narrative dice.

All rolling is free. There are optional paid skins, which is how I hope to keep working on it. No account and no telemetry.

Install: open `https://community.obsidian.md/plugins/rollwright` and choose "Add to Obsidian".
Source and full reference: `https://github.com/thijsduinhouwer2002-coder/rollwright`
Page: `https://dortus.com/rollwright/`

I'd love to hear what you roll on and what is missing. Bugs and ideas are welcome here or on GitHub.

Made by Thijs at Dortus
```
