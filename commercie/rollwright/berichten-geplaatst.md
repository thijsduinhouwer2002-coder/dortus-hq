# Rollwright: geplaatste lanceerberichten

Door Chris. Per bericht: datum, plek, link, of wat er misging.

| Datum | Plek | Link | Uitkomst |
|---|---|---|---|
| 8 nov 2026 ±14:55 UTC | forum.obsidian.md, Share & showcase | geen | niet geplaatst, zie hieronder |

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
