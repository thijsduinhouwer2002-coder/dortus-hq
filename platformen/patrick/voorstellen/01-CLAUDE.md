Wat verandert: CLAUDE.md wordt de enige startlijst (index) en bevat alle harde regels die elke run nodig heeft, zodat regels.md, besluiten.md en lijst-thijs.md niet meer elke run helemaal gelezen hoeven te worden.
Waarom: elke run las 80 tot 130 KB; Anthropic adviseert onder 200 regels en "alleen laden wat nodig is" (bronnen 1, 2, 5, 17 in bronnen/internet.md). Vervangt het huidige CLAUDE.md in zijn geheel.

---

# Voor elke Claude in deze repo

Dortus is het bedrijf van Thijs. Een ploeg Claudes bouwt producten op app-platformen. Doel nu: zo snel mogelijk echt geld, eerlijk verdiend (besluit Thijs 9 nov 22:56).

## Begin van elke run (in deze volgorde, verder niets verplicht)
1. `git pull --rebase` (ondiep klonen mag: `git clone --depth 50`).
2. `berichten/<jouw naam>.md`: alleen het blok **Nieuw**. Berichten van Thijs gaan voor alles.
3. `organisatie/rollen/<jouw rol>.md`: wat jij doet.
4. `organisatie/nu.md`: de geldende besluiten en wie wat doet (hooguit 40 regels).
5. `platformen/<jouw map>/status.md`: waar je was en wat de volgende taak is.
Lees de rest alleen als je taak erom vraagt: `organisatie/regels.md` (werkwijze, code, uitbrengen), `organisatie/archief/` (oude besluiten), `organisatie/doelen.md` (cijfers).

## Elke run: één taak af
- Pak de bovenste taak uit je `status.md`. Maak die af, laat hem nakijken als dat moet, sla op.
- Lukt het niet, of is er niets zinvols: schrijf dat in twee regels in `status.md` en stop. Een korte run is goed.
- Eind van de run: werk `status.md` bij (hooguit 25 regels: doel, laatste uitkomst, volgende taak, waar je op wacht). Logboek alleen aanvullen met wat er besloten of opgeleverd is, niet met wat je las.

## Harde regels (gelden altijd)
- **Webpagina's lees je met `curl` in Bash, nooit met WebFetch.** WebFetch vraagt om toestemming en dan staat alles stil. Zet deze zin letterlijk in de opdracht van elke agent die je inzet.
- Gebruik nooit de koppelingen Gmail, Trello, Atlassian, Claude Docs, Search1API, Polar, Shopify of Kondo, ook niet als ze in je run staan.
- Nooit: inloggen, accounts aanmaken, betalen, bank-, ID- of wachtwoordgegevens invullen, voorwaarden accepteren, andermans spullen verwijderen, posten onder de naam van Thijs. Zet zo'n stap klaar in `organisatie/lijst-thijs.md` (vorm staat bovenaan dat bestand).
- Niets nep: geen verzonnen cijfers, reviews of beloftes. Elk cijfer krijgt GEZIEN, DERDEN (met link) of GOK.
- Indienen of uitbrengen alleen als de test in de echte app groen is en de ontwerper `Akkoord: ja` gaf.
- Tests nooit aanpassen om ze te laten slagen.
- Geen ruwe data of films groter dan 1 MB in git. Zet ze in een Actions-artefact of op de tak `data`. Alleen de samenvatting in markdown.

## Waar je schrijft
- Je eigen map in `platformen/` (de ontwerpers in `ontwerp/`), je eigen product in `producten/`, je eigen bestand in `berichten/` (alleen "verwerkt" erachter).
- Een nieuw groot besluit: één regel bovenaan `organisatie/besluiten.md`. Alleen de hoofdmanager en de hoofdchat werken `organisatie/nu.md`, `organisatie/bord.md` en `rapporten/` bij.
- Code op een tak `claude/<platform>-<datum>`, samenvoegen als de controleur akkoord is en de tests groen zijn.
- Mislukt pushen: `git pull --rebase` en opnieuw. Nooit geforceerd.

## Afsluiten
Sluit pas af als `git ls-remote origin main` (of je tak) jouw laatste commit laat zien. Zet hash en uitkomst in je eindantwoord, niet in een bestand. Lukt opslaan niet: zet de volledige nieuwe bestanden in je eindantwoord en zeg in je laatste zin dat het niet is opgeslagen.

## Toon
Nederlands, gewone woorden, geen gedachtestreepjes. Beslis zelf en schrijf in één zin waarom. Thijs wil zo min mogelijk gevraagd worden en elke keuze snappen.
